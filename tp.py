import google.generativeai as genai
from langchain_groq import ChatGroq
# example.py
import os
from io import BytesIO
import streamlit as st
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

# Load environment variables
load_dotenv()

# Initialize ElevenLabs with API Key
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "sk_0eb7f6bbe92ceb0a669aae6c8c5a45e620d022a51ea45693")
elevenlabs = ElevenLabs(api_key=ELEVENLABS_API_KEY)

# Streamlit audio input
audio_value = st.audio_input("Record a voice message")

if audio_value is not None:
    st.audio(audio_value)

    # Convert the uploaded file to BytesIO
    audio_data = BytesIO(audio_value.getvalue())

    # Transcribe using ElevenLabs API
    try:
        transcription = elevenlabs.speech_to_text.convert(
            file=audio_data,
            model_id="scribe_v1",            # Only supported model currently
            tag_audio_events=True,           # Tag laughter, applause, etc.
            language_code="None",             # Set language (or None for auto)
            diarize=True                     # Annotate who is speaking
        )

        # Display transcription result in Streamlit
        st.subheader("Transcription Result:")
        st.json(transcription)
        querry = transcription.text
        st.write(transcription.text)  # Display the transcription text
    except Exception as e:
        st.error(f"Transcription failed: {str(e)}")


    GROQ_API_KEY ="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"
    llm=ChatGroq(
        model='gemma2-9b-it',
        api_key=GROQ_API_KEY,
    )
    llm_response = llm.invoke(
        querry
    )
    st.subheader("LLM Response:")
    st.write(llm_response.content)  # Display the LLM response
    st.write("Audio transcription and LLM response completed successfully.")
    