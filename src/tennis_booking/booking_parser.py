from datetime import datetime
import json
from typing import Optional, Dict, Any

import dateparser
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser

from src.tennis_booking.models import BookingDetails, CourtType, CourtLocation, MatchType, SkillLevel, Equipment, WeatherPreference

BOOKING_PROMPT = """
You are a tennis court booking assistant. Parse the following booking request and extract all relevant details.
If a detail is not mentioned, leave it as null, except for location which should default to "Main Tennis Center" if not specified.

For the date and time, you MUST return them in one of these exact formats:
1. For relative dates: "tomorrow at HH:MM" or "today at HH:MM" or "next tuesday at HH:MM"
2. For specific dates: "YYYY-MM-DD HH:MM"

Always use 24-hour format for time (00-23). For example:
- "7pm" should be "19:00"
- "9am" should be "09:00"
- "noon" should be "12:00"
- "midnight" should be "00:00"

Examples of correct date_time formats:
- "Need a court tomorrow at 7pm" → "tomorrow at 19:00"
- "Book for next Tuesday evening" → "next tuesday at 19:00"
- "Want to play at 9am" → "today at 09:00"
- "Book for March 25th at 3pm" → "2024-03-25 15:00"

Please pay special attention to the following aspects:
1. Core booking details (date, time, location, duration)
2. Court specifications (surface type, indoor/outdoor, lighting needs)
3. Match details (singles/doubles, number of players, skill level)
4. Equipment and amenities (racket rental, balls, ball machine, coaching)
5. Environmental preferences (weather, temperature)
6. Additional requirements (seating, refreshments)

Booking request: {booking_request}

{format_instructions}
"""


class BookingParser:
    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0,
            openai_api_key=openai_api_key
        )
        self.parser = PydanticOutputParser(pydantic_object=BookingDetails)
        self.prompt = ChatPromptTemplate.from_template(
            template=BOOKING_PROMPT
        )

    def parse_booking_request(self, request_text: str) -> Optional[BookingDetails]:
        """
        Parse a natural language booking request and extract structured booking details.
        
        Args:
            request_text: The natural language booking request
            
        Returns:
            BookingDetails object containing the parsed information
        """
        try:
            messages = self.prompt.format_messages(
                booking_request=request_text,
                format_instructions=self.parser.get_format_instructions()
            )
            
            llm_response = self.llm(messages)
            response_content = llm_response.content
            print(f"LLM Response: {response_content}")  # Debug print
            
            # Parse the JSON response
            response_dict = json.loads(response_content)
            
            # Ensure location is set
            if not response_dict.get('location'):
                response_dict['location'] = "Main Tennis Center"
            
            # Parse the date_time string into a datetime object
            if isinstance(response_dict.get('date_time'), str):
                date_str = response_dict['date_time'].lower()
                
                # Try parsing with dateparser first
                parsed_datetime = dateparser.parse(
                    date_str,
                    settings={
                        'PREFER_DATES_FROM': 'future',
                        'RELATIVE_BASE': datetime.now(),
                        'PREFER_DAY_OF_MONTH': 'current',
                        'RETURN_AS_TIMEZONE_AWARE': False,
                        'TO_TIMEZONE': 'UTC',
                        'STRICT_PARSING': False
                    }
                )
                
                if not parsed_datetime:
                    # If dateparser fails, try manual parsing for common formats
                    if "today at " in date_str:
                        time_str = date_str.split("at ")[1].strip()
                        parsed_datetime = datetime.combine(
                            datetime.now().date(),
                            datetime.strptime(time_str, "%H:%M").time()
                        )
                    elif "tomorrow at " in date_str:
                        time_str = date_str.split("at ")[1].strip()
                        parsed_datetime = datetime.combine(
                            datetime.now().date(),
                            datetime.strptime(time_str, "%H:%M").time()
                        )
                        parsed_datetime = parsed_datetime.replace(day=parsed_datetime.day + 1)
                    else:
                        # Try exact format as last resort
                        try:
                            parsed_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                        except ValueError:
                            raise ValueError(f"Could not parse date/time: {date_str}")
                
                if parsed_datetime:
                    response_dict['date_time'] = parsed_datetime
                else:
                    raise ValueError(f"Could not parse date/time: {date_str}")
            
            # Create BookingDetails object
            booking_details = BookingDetails(**response_dict)
            
            # Post-process the parsed details
            self._apply_booking_rules(booking_details)
            
            return booking_details
            
        except Exception as e:
            print(f"Error parsing booking request: {str(e)}")
            return None

    def _apply_booking_rules(self, booking: BookingDetails):
        """Apply business rules and defaults to the booking details."""
        # Set number of players based on match type if not specified
        if booking.match_type and not booking.number_of_players:
            booking.number_of_players = 4 if booking.match_type == MatchType.DOUBLES else 2
            
        # Set lighting requirement based on time if not specified
        if booking.date_time and booking.lighting_required is None:
            hour = booking.date_time.hour
            booking.lighting_required = hour < 7 or hour >= 18
            
        # Set court location based on weather preference if not specified
        if booking.weather_preference and not booking.court_location:
            if booking.weather_preference in [WeatherPreference.COVERED, WeatherPreference.TEMPERATURE_CONTROLLED]:
                booking.court_location = CourtLocation.INDOOR

    def _parse_date_time(self, date_str: str, time_str: str) -> datetime:
        """Helper method to parse date and time strings into datetime object."""
        try:
            # Add your date parsing logic here
            # This is a placeholder - you would want to add more sophisticated
            # date/time parsing based on your needs
            return datetime.now()
        except Exception as e:
            print(f"Error parsing date/time: {str(e)}")
            return datetime.now() 