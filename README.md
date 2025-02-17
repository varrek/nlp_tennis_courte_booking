# Tennis Court Booking Assistant

A Python-based tennis court booking application that uses natural language processing to understand and process booking requests. The application leverages Streamlit for the user interface, LangChain for LLM integration, and the OpenAI API for natural language processing.

## Features

- Natural language booking requests
- Intelligent extraction of booking details:
  - Date and time
  - Location
  - Court type (hard, clay, grass, synthetic)
  - Indoor/outdoor preference
  - Match type (singles/doubles)
  - Equipment needs
  - Additional amenities
- Smart defaults and business rules
- Clean, intuitive user interface
- Real-time processing and feedback

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/varrek/nlp_tennis_courte_booking.git
cd nlp_tennis_courte_booking
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your-api-key-here
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Enter your booking request in natural language. Examples:
   - "Need a clay court for next Tuesday at 7pm"
   - "Looking for a doubles match tomorrow morning at 9am"
   - "Want to practice with a ball machine for 90 minutes"

3. The application will extract and display:
   - Core booking details (date, time, location, duration)
   - Court specifications (surface type, indoor/outdoor, lighting)
   - Match details (singles/doubles, number of players, skill level)
   - Equipment and amenities (rentals, ball machine, coaching)
   - Environmental preferences (weather, temperature)
   - Additional requirements (seating, refreshments)

4. Review the details and confirm your booking

## Project Structure

- `app.py`: Main Streamlit application
- `booking_parser.py`: LangChain integration and booking request parser
- `models.py`: Data models and enums
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not included in repository)

## Development

The application uses:
- Streamlit for the user interface
- LangChain for LLM integration
- OpenAI API for natural language processing
- Pydantic for data validation
- Python-dotenv for environment variable management

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 