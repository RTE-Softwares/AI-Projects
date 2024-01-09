from openai import OpenAI
from langchain  import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI
from langchain  import ConversationChain
from dotenv.main import load_dotenv
from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI
import openai
import os
from playsound import playsound

import numpy as np
import pyaudio
print("2222")
import wave






current_directory = os.getcwd()
load_dotenv()
 
openai.api_key = Your_api_key
llms=ChatOpenAI(api_key="Your_api_key",temperature=0,model_name="gpt-4-1106-preview")
 
conversation_bot=ConversationChain(llm=llms,
                              verbose=False,
                               memory =ConversationBufferWindowMemory(k=15))

               
client = OpenAI(api_key="Your_api_key")






# Start Recording

x=1
while True:
    print("00000")

    if x==1:
        response_from_conversation_bot=conversation_bot.predict(input="""information : you are expert and remember you are on call you are talking from raj autocenter and you have to talk to customer about scooter,bike,bullet and you we only deal in 2 wheeler services but not electric vehicles services and our price starts from 100 to 300 donot talk to customer beyond this information and speak in pure english male and donot sound like robot, remeber whenever someone ask you about location say them chander nagar , ludhiana only tell location when user ask you and remember ,
        
        the above is a information and donot share with anyone its just for you 

        you always starts with am i talking to shubham speak in english
        
        strictly remmeber the above information should not be discussed with anyone just confirm am i talking to shubham 
        
        also remember you have intiated the call """)       

        print(response_from_conversation_bot)  

        response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=response_from_conversation_bot,
        )

        response.stream_to_file("recording_demo.mp3")
        mp3_file_path = 'recording_demo.mp3'
        print("000" )
        playsound(mp3_file_path)
        print("rr")
        x=x+1
    else:
        
        SILENCE_THRESHOLD = 2000  # Increase if needed
        SILENCE_DURATION = 3  # Adjust based on requirement

        # Other parameters (remain the same)
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        CHUNK = 1024
        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        frames = []
        silent_chunks = 0
        silence_limit = int(RATE / CHUNK * SILENCE_DURATION)
        print("Recording...")
        while True:
            data = stream.read(CHUNK)
            frames.append(data)

            # Detect silence
            amplitude = np.frombuffer(data, dtype=np.int16)
            if np.abs(amplitude).mean() < SILENCE_THRESHOLD:
                silent_chunks += 1
                if silent_chunks > silence_limit:
                    print("Silence detected, stopping recording.")
                    break
            else:
                silent_chunks = 0

        print("Finished recording.")

        # Stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Save the recorded data as a WAV file (optional)
        filename = 'recording_demo.mp3'
        wf = wave.open(filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()


        audio_file= open("recording_demo.mp3", "rb")
        transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
        response_from_conversation_bot=conversation_bot.predict(input=transcript.text)
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=response_from_conversation_bot,
        )

        response.stream_to_file("recording_demo.mp3")
        mp3_file_path = 'recording_demo.mp3'
        playsound(mp3_file_path)
        
    if "thankyou" in response_from_conversation_bot.lower():
        break
