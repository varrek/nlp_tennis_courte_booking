import os
import streamlit as st
from dotenv import load_dotenv

try:
    from booking_parser import BookingParser
    from models import BookingDetails
except ImportError:
    from .booking_parser import BookingParser
    from .models import BookingDetails

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Tennis Court Booking",
    page_icon="🎾",
    layout="wide"
)

def initialize_session_state():
    """Initialize session state variables if they don't exist."""
    if 'booking_parser' not in st.session_state:
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            st.error("OpenAI API key not found. Please set it in your .env file.")
            st.stop()
        st.session_state.booking_parser = BookingParser(api_key)

def display_booking_details(booking: BookingDetails):
    """Display the extracted booking details in a clean format."""
    formatted_details = booking.format_for_display()
    
    st.subheader("📅 Booking Details")
    
    # Create tabs for different categories of information
    tabs = st.tabs([
        "Core Details",
        "Court Specifications",
        "Match Details",
        "Equipment & Amenities",
        "Environmental",
        "Additional Requirements"
    ])
    
    # Display core details
    with tabs[0]:
        for key, value in formatted_details["Core Details"].items():
            st.write(f"**{key}:**", value)
    
    # Display court specifications
    with tabs[1]:
        for key, value in formatted_details["Court Specifications"].items():
            st.write(f"**{key}:**", value)
    
    # Display match details
    with tabs[2]:
        for key, value in formatted_details["Match Details"].items():
            st.write(f"**{key}:**", value)
    
    # Display equipment and amenities
    with tabs[3]:
        for key, value in formatted_details["Equipment & Amenities"].items():
            st.write(f"**{key}:**", value)
    
    # Display environmental preferences
    with tabs[4]:
        for key, value in formatted_details["Environmental Preferences"].items():
            st.write(f"**{key}:**", value)
    
    # Display additional requirements
    with tabs[5]:
        for key, value in formatted_details["Additional Requirements"].items():
            st.write(f"**{key}:**", value)

def main():
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.title("🎾 Tennis Court Booking Assistant")
    st.markdown("""
    Enter your booking request in natural language, and I'll help you book a tennis court!
    
    Examples:
    - *"Need a clay court for next Tuesday at 7pm in downtown, preferably indoor with lights"*
    - *"Looking for a doubles match this Saturday morning, we're intermediate players and need racket rentals"*
    - *"Want to practice with a ball machine for 90 minutes tomorrow afternoon, preferably when it's not too hot"*
    """)
    
    # Input field for booking request
    booking_request = st.text_area(
        "Enter your booking request:",
        height=100,
        placeholder="Type your booking request here..."
    )
    
    # Process button
    if st.button("Process Booking Request", type="primary"):
        if not booking_request:
            st.warning("Please enter a booking request.")
            return
            
        with st.spinner("Processing your request..."):
            # Parse the booking request
            booking_details = st.session_state.booking_parser.parse_booking_request(booking_request)
            
            if booking_details:
                # Display the extracted details
                display_booking_details(booking_details)
                
                # Add a confirmation button
                if st.button("✅ Confirm Booking"):
                    st.success("Booking confirmed! You will receive a confirmation email shortly.")
            else:
                st.error("Sorry, I couldn't process your booking request. Please try again with more details.")
    
    # Add some helpful information at the bottom
    with st.expander("ℹ️ How to use this booking assistant"):
        st.markdown("""
        1. **Enter your request** in natural language, including as many details as you'd like:
            - Date and time
            - Location
            - Court preferences (hard court, clay, grass, synthetic)
            - Indoor or outdoor preference
            - Lighting requirements
            - Match type (singles or doubles)
            - Duration
            - Equipment rental needs
            - Skill level
            - Weather preferences
            - Additional amenities (seating, refreshments, coaching)
        
        2. **Click 'Process Booking Request'** to see the extracted details
        
        3. **Review the details** in the organized tabs and confirm your booking
        
        The assistant will try to fill in reasonable defaults for any missing information and make smart assumptions based on your preferences.
        """)

if __name__ == "__main__":
    main() 