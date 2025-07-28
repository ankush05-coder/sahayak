from google import genai
# from google.colab import userdata
# userdata.get('GOOGLE_API_KEY')
# client = genai.Client(api_key='AIzaSyDcZCLKTI10pj9KNmsn9TgTEQJcqO1K4Ck')

myfile = client.files.upload(file="hind.opus")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=["Describe this audio clip only give the text that  appears into the audio clip and also the grade ", myfile]
)

print(response.text)
query=response.text

from langchain_groq import ChatGroq
lang = input("Enter the language you want to translate to (e.g., Hindi ,kanada): ")
grade = input("Enter the grade level (e.g., 5th, 6th): ")
# llm=ChatGroq(model='gemma2-9b-it',api_key='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')
contents = f"""
Based on the query: "{query}", provide a detailed explanation in a clear, simple, and easy-to-understand manner in {lang} language, suitable for a {grade}-level student. 
    based on the grade level select any one from below: 
    - For lower grades (3-5): Use simple language, relatable examples, and visual analogies (e.g., comparing concepts to everyday objects or actions). Avoid technical terms and keep explanations short.

    - For middle school (6-8): Introduce more structure with basic definitions, simple examples, and analogies, but include some technical terms and concepts. Use clear step-by-step explanations.

    - For high school (9-12): Use a more formal tone, include relevant technical terms where necessary, and explain them. Provide examples that connect to real-life scenarios and more complex concepts.

The response should:
- Be limited to approximately 200 characters.
- Cover all the core concepts relevant to the query in a way that aligns with the student's grade.
- Use a structured format with a topic explanation and its types.
- Include examples, analogies, or visuals where necessary to enhance understanding.
- Avoid overly technical jargon unless necessary, and explain it in simple terms when used.
"""

resp=llm.invoke(contents)


print(resp.content)

from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client(api_key='AIzaSyDcZCLKTI10pj9KNmsn9TgTEQJcqO1K4Ck')

response = client.models.generate_content(
   model="gemini-2.5-flash-preview-tts",
   contents=resp.content,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='output.wav'
wave_file(file_name, data) # Saves the file to current directory


# from google import genai
# from google.cloud import translate_v2 as translate
# import wave

# # Set up Google Translate Client
# translate_client = translate.Client()

# # User-driven language inputs for translation
# source_lang = 'en-US'  # Replace with the language code of the original text
# target_lang = 'hi-IN'  # Replace with the language code you want to translate to

# # Initialize Google GenAI Client for Content and TTS
# client = genai.Client(api_key='AIzaSyDcZCLKTI10pj9KNmsn9TgTEQJcqO1K4Ck')

# # Function to translate text using Google Translate API
# def translate_text(text, target_language):
#     result = translate_client.translate(text, target_lang=target_language)
#     return result['translatedText']

# # Step 1: Upload the audio file
# myfile = client.files.upload(file="2.opus")

# # Step 2: Generate content (i.e., text) from the audio file
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#      contents=["Describe this audio clip only give the text that appears into the audio clip and also the grade", myfile]
# )

# # Extract the response text (this is the content from the audio)
# audio_text = response.text
# print(f"Extracted Audio Text: {audio_text}")

# # Step 3: Translate the extracted text to the target language
# translated_text = translate_text(audio_text, target_lang)
# print(f"Translated Text: {translated_text}")

# # Step 4: Generate an explanation from the translated text
# from langchain_groq import ChatGroq

# llm = ChatGroq(model='gemma2-9b-it', api_key='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')

# contents = f"""
# Based on the query: "{translated_text}", provide a detailed explanation in a clear, simple, and easy-to-understand manner. 

# The response should:
# - Be limited to approximately 2000 characters.
# - Cover all the core concepts relevant to the query.
# - Use a structured format with clear headings and bullet points or numbered lists where appropriate.
# - Include examples or analogies if needed to improve understanding.
# - Avoid overly technical jargon unless necessary, and explain it when used.
# """

# # Invoke the LLM to generate a response
# resp = llm.invoke(contents)
# print(f"LLM Response: {resp.content}")

# # Step 5: Convert the LLM response to speech in the target language
# from google import genai
# from google.genai import types

# # Set up the wave file to save the output:
# def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
#     with wave.open(filename, "wb") as wf:
#         wf.setnchannels(channels)
#         wf.setsampwidth(sample_width)
#         wf.setframerate(rate)
#         wf.writeframes(pcm)

# response = client.models.generate_content(
#     model="gemini-2.5-flash-preview-tts",
#     contents=resp.content,
#     config=types.GenerateContentConfig(
#         response_modalities=["AUDIO"],
#         speech_config=types.SpeechConfig(
#             voice_config=types.VoiceConfig(
#                 prebuilt_voice_config=types.PrebuiltVoiceConfig(
#                     voice_name='Kore',
#                 )
#             )
#         ),
#     )
# )

# # Extract the generated speech data
# data = response.candidates[0].content.parts[0].inline_data.data

# # Save the audio file
# file_name = 'output_translated_speech.wav'
# wave_file(file_name, data)
# print(f"Audio file saved as: {file_name}")
