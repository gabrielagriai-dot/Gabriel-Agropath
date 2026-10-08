import streamlit as st
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold


st.set_page_config(page_title="Gabriel Agro AI", page_icon="🌱", layout="centered")

st.title("🌱 Gabriel Agro AI")
st.subheader("Expert Agricultural Assistant")
st.caption("Specialized in Plant Pathology based on TNAU Agritech guidelines.")
st.divider()


API_KEY = st.secrets.get("GEMINI_API_KEY", "")

if not API_KEY:
    st.info("Please configure your GEMINI_API_KEY in the Streamlit secrets panel to activate the cloud engine.")
    st.stop()


genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-3.8-flash")


user_query = st.text_input(
    label="What do you want to know about plant pathology?",
    placeholder="e.g., Rice blast disease control measures...",
    key="query_input"
)

if user_query:
    prompt = f"""
You are an expert agricultural assistant specialized in plant pathology.
You provide advice based on Tamil Nadu Agricultural University (TNAU) Agritech guidelines.
Provide actionable control measures (cultural, biological, and chemical) for this issue:
Query: {user_query}
"""
    st.write("🔍 **Cloud AI Diagnosis & Recommendation:**")
    
    try:
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }
        
      
        response = model.generate_content(prompt, safety_settings=safety_settings)
        st.write(response.text)
    except Exception as e:
        st.error(f"An error occurred while connecting to the AI service: {e}")

