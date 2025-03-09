import streamlit as st
import openai
from bs4 import BeautifulSoup
import requests
import os

# OpenAI API Key
openai.api_key = os.getenv('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')  # Ensure this matches your GitHub secret

# Streamlit App
st.title("AI-Powered Business Idea Generator")

# Industry Selection
industries = ["Technology", "Healthcare", "E-commerce", "Finance", "Education"]
selected_industry = st.selectbox("Select an industry", industries)

# Trend Analysis
@st.cache_data
def get_trends(industry):
    try:
        url = f"https://www.google.com/search?q={industry}+trends"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        trends = [h3.text for h3 in soup.find_all('h3')]
        return trends
    except Exception as e:
        st.error(f"Error fetching trends: {e}")
        return []

trends = get_trends(selected_industry)

# AI-Generated Business Ideas
@st.cache_data
def generate_business_ideas(industry, trends):
    if not trends:
        return []
    prompt = f"Generate innovative business ideas for the {industry} industry, incorporating the following trends: {', '.join(trends)}."
    try:
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024)
        ideas = response.choices[0].text.strip().split('\n')
        return ideas
    except Exception as e:
        st.error(f"Error generating business ideas: {e}")
        return []

business_ideas = generate_business_ideas(selected_industry, trends)

# Display Business Ideas
st.write("AI-Generated Business Ideas:")
if business_ideas:
    for idea in business_ideas:
        st.write(idea)
else:
    st.write("No business ideas generated.")

# Competitive Analysis
@st.cache_data
def competitive_analysis(idea):
    try:
        url = f"https://www.google.com/search?q={idea}+competitors"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        competitors = [h3.text for h3 in soup.find_all('h3')]
        return competitors
    except Exception as e:
        st.error(f"Error fetching competitors: {e}")
        return []

# Revenue Model and SWOT Analysis
@st.cache_data
def revenue_model_and_swot_analysis(idea):
    try:
        prompt = f"Provide a revenue model and SWOT analysis for the business idea: {idea}."
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024)
        analysis = response.choices[0].text.strip()
        return analysis
    except Exception as e:
        st.error(f"Error generating SWOT analysis: {e}")
        return "No analysis available."

# Display Competitive Analysis, Revenue Model, and SWOT Analysis
if business_ideas:
    st.write("Competitive Analysis:")
    competitors = competitive_analysis(business_ideas[0])
    if competitors:
        for competitor in competitors:
            st.write(competitor)
    else:
        st.write("No competitors found.")

    st.write("Revenue Model and SWOT Analysis:")
    analysis = revenue_model_and_swot_analysis(business_ideas[0])
    st.write(analysis)
else:
    st.write("No business ideas available for analysis.")
