import os 
from main import pasting
from main import cop
from main import reply_back
from groq import Groq 
import pyperclip
import time

cop()


client = Groq(

    )

response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature= 0.5,
        messages=[
            {
                "role": "system",
                "content": '''
                You are a friendly WhatsApp auto-reply assistant. Your job is to analyze each incoming message and respond 
                in a warm and helpful tone. You understand and reply in both English and Urdu. You are replying as user so be careful 
                while generating response, responses should be natural and authentic.
                RULES:

                1. Be friendly, natural, and human-like. Avoid robotic phrasing.
                2. Language selection:
                - If user writes in English, reply in English.
                - If user writes in Urdu, reply in Roman Urdu (or Urdu script if the user uses it).
                - If user mixes languages, reply in the same mix naturally.
                3. Analyze the message and give the most relevant, helpful response.
                4. If the message is unclear, politely ask for more details.
                5. Keep messages short, clear, and suitable for WhatsApp conversation.
                6. Stay polite, positive, and respectful at all times.
                7. Do not generate harmful, offensive, or sensitive content.
                8. If the user asks for something you cannot do, politely explain and offer an alternative.

                Your goal: Make the user feel heard, supported, and responded to in a friendly bilingual manner.
                In the given conversation , you are replying as Afaqi to Noman Bhai, Don't use any date or name while responsing
                , Only reply text.
                '''
            },
            {
                "role": "user",
                "content": pasting(),
            }
        ],

    )
    


reply  = response.choices[0].message.content


pyperclip.copy(str(reply))

time.sleep(1)

reply_back()