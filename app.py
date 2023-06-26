# app.py
import streamlit as st
import pandas as pd
import base64

import scrab_flipkart

# Define your Streamlit app
def main():
    # Create UI components
    st.title("Flipkart Web Scraper")

    # Add an introduction and explanation
    
    st.markdown("This app allows you to scrape Flipkart website to get product information.")
    st.markdown("Enter the product name and click 'Scrape' to retrieve the data.")
    st.markdown("The scraped data will be displayed as a table, and you can download it as a CSV file.")

    product_name = st.text_input("Enter product name:")
    submit_button = st.button("Scrape")

    # When the user clicks the submit button
    if submit_button:
        st.info('Please wait while we scrape the website. This may take a few minutes...')
        # Call the scrap() function with the user's input
        scraped_data = scrab_flipkart.scrab(product_name)

        # Display the scraped data as a DataFrame
        if scraped_data is not None and not scraped_data.empty:
            st.write("Scraped data:")
            st.dataframe(scraped_data)
            

            csv = scraped_data.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="scraped_data.csv">Download CSV</a>'
            st.markdown(href, unsafe_allow_html=True)

            
        else:
            st.write("No data found.")
            

# Run the app
if __name__ == "__main__":
    main()
