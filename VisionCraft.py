import streamlit as st
from streamlit import caching
import openai
from bs4 import BeautifulSoup
import requests

OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

Streamlit App
st.title("AI-Powered Business Idea Generator")

Industry Selection
industries = ["Technology", "Healthcare", "E-commerce", "Finance", "Education"]
selected_industry = st.selectbox("Select an industry", industries)

Trend Analysis
@st.cache
def get_trends(industry):
    url = f"https://www.google.com/search?q={industry}+trends"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    trends = [h3.text for h3 in soup.find_all('h3')]
    return trends

trends = get_trends(selected_industry)

AI-Generated Business Ideas
@st.cache
def generate_business_ideas(industry, trends):
    prompt = f"Generate innovative business ideas for the {industry} industry, incorporating the following trends: {', '.join(trends)}."
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024)
    ideas = response.choices[0].text.split('\n')
    return ideas

business_ideas = generate_business_ideas(selected_industry, trends)

Display Business Ideas
st.write("AI-Generated Business Ideas:")
for idea in business_ideas:
    st.write(idea)

Competitive Analysis
@st.cache
def competitive_analysis(idea):
    url = f"https://www.google.com/search?q={idea}+competitors"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    competitors = [h3.text for h3 in soup.find_all('h3')]
    return competitors

Revenue Model and SWOT Analysis
@st.cache
def revenue_model_and_swot_analysis(idea):
    prompt = f"Provide a revenue model and SWOT analysis for the business idea: {idea}."
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024)
    analysis = response.choices[0].text
    return analysis

Display Competitive Analysis, Revenue Model, and SWOT Analysis
st.write("Competitive Analysis:")
competitors = competitive_analysis(business_ideas[0])
for competitor in competitors:
    st.write(competitor)

st.write("Revenue Model and SWOT Analysis:")
analysis = revenue_model_and_swot_analysis(business_ideas[0])
st.write(analysis)
