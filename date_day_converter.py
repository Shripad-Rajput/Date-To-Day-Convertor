import streamlit as st
from datetime import datetime
import calendar

def main():
    st.title("Date to Day Converter")
    # Input: Date
    date_input = st.date_input("Select a date", datetime.now())

    # Button to convert date to day
    if st.button("Convert"):
        # Convert date to day of the week
        day_of_week = calendar.day_name[date_input.weekday()]
        st.sub(f"The day for the selected date {date_input} is: **{day_of_week}**")

if __name__ == "__main__":
    main()
