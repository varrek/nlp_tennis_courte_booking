from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, validator


class CourtType(str, Enum):
    HARD = "hard"
    CLAY = "clay"
    GRASS = "grass"
    SYNTHETIC = "synthetic"


class CourtLocation(str, Enum):
    INDOOR = "indoor"
    OUTDOOR = "outdoor"


class MatchType(str, Enum):
    SINGLES = "singles"
    DOUBLES = "doubles"


class SkillLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    PROFESSIONAL = "professional"


class Equipment(str, Enum):
    RACKET = "racket"
    BALLS = "balls"
    SHOES = "shoes"


class WeatherPreference(str, Enum):
    SUNNY = "sunny"
    COVERED = "covered"
    TEMPERATURE_CONTROLLED = "temperature_controlled"


class BookingDetails(BaseModel):
    date_time: datetime
    location: str
    duration_minutes: int = 60
    court_type: Optional[CourtType] = None
    court_location: Optional[CourtLocation] = None
    lighting_required: Optional[bool] = None
    match_type: Optional[MatchType] = None
    number_of_players: Optional[int] = None
    skill_level: Optional[SkillLevel] = None
    equipment_rental: Optional[List[Equipment]] = None
    ball_machine_required: Optional[bool] = None
    coaching_requested: Optional[bool] = None
    weather_preference: Optional[WeatherPreference] = None
    temperature_preference: Optional[str] = None
    seating_required: Optional[bool] = None
    refreshments_required: Optional[bool] = None
    additional_notes: Optional[str] = None

    class Config:
        use_enum_values = True

    def format_for_display(self) -> dict:
        """Format the booking details for display in the UI."""
        return {
            "Core Details": {
                "Date & Time": self.date_time.strftime("%Y-%m-%d %H:%M"),
                "Location": self.location,
                "Duration": f"{self.duration_minutes} minutes"
            },
            "Court Specifications": {
                "Court Type": self.court_type.value if isinstance(self.court_type, CourtType) else str(self.court_type) if self.court_type else "Not specified",
                "Indoor/Outdoor": self.court_location.value if isinstance(self.court_location, CourtLocation) else str(self.court_location) if self.court_location else "Not specified",
                "Lighting Required": "Yes" if self.lighting_required else "No" if self.lighting_required is False else "Not specified"
            },
            "Match Details": {
                "Match Type": self.match_type.value if isinstance(self.match_type, MatchType) else str(self.match_type) if self.match_type else "Not specified",
                "Number of Players": str(self.number_of_players) if self.number_of_players else "Not specified",
                "Skill Level": self.skill_level.value if isinstance(self.skill_level, SkillLevel) else str(self.skill_level) if self.skill_level else "Not specified"
            },
            "Equipment & Amenities": {
                "Equipment Rental": ", ".join(e.value if isinstance(e, Equipment) else str(e) for e in self.equipment_rental) if self.equipment_rental else "None",
                "Ball Machine": "Yes" if self.ball_machine_required else "No" if self.ball_machine_required is False else "Not specified",
                "Coaching": "Yes" if self.coaching_requested else "No" if self.coaching_requested is False else "Not specified"
            },
            "Environmental Preferences": {
                "Weather": self.weather_preference.value if isinstance(self.weather_preference, WeatherPreference) else str(self.weather_preference) if self.weather_preference else "Not specified",
                "Temperature": self.temperature_preference if self.temperature_preference else "Not specified"
            },
            "Additional Requirements": {
                "Seating": "Yes" if self.seating_required else "No" if self.seating_required is False else "Not specified",
                "Refreshments": "Yes" if self.refreshments_required else "No" if self.refreshments_required is False else "Not specified",
                "Notes": self.additional_notes if self.additional_notes else "None"
            }
        } 