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

- Python 3.10 or higher
- OpenAI API key

## Local Development

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

4. Run the application:
```bash
streamlit run run_app.py
```

## Deployment to Streamlit Cloud

1. Fork this repository to your GitHub account.

2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in with your GitHub account.

3. Click "New app" and select this repository.

4. Set the following:
   - Main file path: `run_app.py`
   - Python version: 3.10

5. Add your OpenAI API key as a secret:
   - In the app settings, go to "Secrets"
   - Add your API key in the following format:
     ```toml
     OPENAI_API_KEY="your-api-key-here"
     ```

6. Deploy!

## Project Structure

```
├── .streamlit/
│   └── config.toml      # Streamlit configuration
├── src/
│   └── tennis_booking/
│       ├── __init__.py
│       ├── app.py       # Main Streamlit application
│       ├── booking_parser.py  # LangChain integration
│       └── models.py    # Data models and enums
├── .env                 # Environment variables (local development)
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── run_app.py          # Application entry point
└── setup.py            # Package configuration
```

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