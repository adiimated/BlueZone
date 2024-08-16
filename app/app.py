import streamlit as st

# Page configuration
st.set_page_config(page_title="Blue Zone Project", layout="wide")

# Function to display the Introduction
def show_introduction():
    st.title("The Blue Zone Project")
    st.header("Background")
    st.write("""
    The desire to live a long and healthy life is universal. This project draws inspiration from "blue zones," 
    areas identified by Dan Buettner and National Geographic where people live significantly longer and healthier lives. 
    These regions include Sardinia (Italy), Okinawa (Japan), Loma Linda (California), Ikaria (Greece), and Nicoya (Costa Rica). 
    The concept of blue zones offers insights into factors that contribute to longevity and reduced chronic illness.
    """)
    
    st.header("Problem")
    st.write("""
    Despite high healthcare spending—averaging 13,493 dollars per person and totaling $4.5 trillion annually—the U.S. healthcare 
    system underperforms in various health metrics compared to other developed nations. The life expectancy in the U.S. has 
    recently fallen below that of China, highlighting flaws in the American healthcare system. Furthermore, although the U.S. 
    leads in cancer screenings and has seen a significant reduction in cancer deaths, the healthcare system is plagued with 
    inconsistencies and inefficiencies, particularly in how it manages chronic conditions.
    """)
    
    st.header("Goal")
    st.write("""
    - Identify American counties with the highest number of centenarians and investigate the contributing factors to such longevity.
    - Examine the impact of healthcare variables, environmental conditions, lifestyle choices, socioeconomic status, and demography on life expectancy.
    - Explore disparities between rural and urban areas in terms of healthcare and lifestyle factors.
    - Evaluate variations in life expectancy among U.S. counties to provide a nuanced understanding of the local healthcare systems.
    """)

# Function to display the Literature Review
def show_literature_review():
    st.title("Literature Review")
    st.header("Objective")
    st.write("""
    Conduct a detailed literature review to identify the factors linked to longevity in the well-known global Blue Zones.
    """)
    
    st.header("Key Findings")
    st.write("""
    The following table summarizes the key factors associated with the longevity observed in Blue Zones:
    """)
    
    # Displaying table data
    table_data = {
        "Factor Category": ["Diet and Nutrition", "Physical Activity", "Social Engagement", "Psychological Health", "Environmental Factors", "Healthcare Access"],
        "Description": [
            "Predominantly plant-based diets with minimal meat consumption, linked to reduced rates of chronic diseases.",
            "Daily life integrates moderate physical activities like walking and gardening instead of structured exercises.",
            "Strong social connections and an active social life significantly impact mental health and longevity.",
            "Traits include high life satisfaction, a sense of purpose, and effective stress management techniques.",
            "Supportive physical and social environments, including clean air and community-oriented living.",
            "Easy access to healthcare and preventive services, coupled with economic stability, supports overall health."
        ]
    }
    
    st.table(table_data)

# Creating tabs for navigation
tab1, tab2 = st.tabs(["Introduction", "Literature Review"])

with tab1:
    show_introduction()

with tab2:
    show_literature_review()
