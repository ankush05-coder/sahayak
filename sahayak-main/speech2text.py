from google import genai
# from google.colab import userdata
# userdata.get('GOOGLE_API_KEY')
client = genai.Client(api_key='AIzaSyDcZCLKTI10pj9KNmsn9TgTEQJcqO1K4Ck')

myfile = client.files.upload(file="3.opus")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=["Describe this audio clip only give the text that  appears into the audio clip and also the grade ", myfile]
)

print(response.text)
query=response.text

from langchain_groq import ChatGroq

llm=ChatGroq(model='gemma2-9b-it',api_key='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')
contents = f"""
Based on the query: "{query}", provide a detailed explanation in a clear, simple, and easy-to-understand manner. 

The response should:
- Be limited to approximately 2000 characters.
- Cover all the core concepts relevant to the query.
- Use a structured format with clear headings and bullet points or numbered lists where appropriate.
- Include examples or analogies if needed to improve understanding.
- Avoid overly technical jargon unless necessary, and explain it when used.
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