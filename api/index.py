import os

from flask import Flask
from langchain.llms import OpenAI

app = Flask(__name__)

os.environ["OPENAI_API_KEY"] = "mk-WOb5xz6NB9NfXJM6REnzs4RGqcdYe0Q64hnbLulzPOEAXiP0"
os.environ['OPENAI_API_BASE'] = 'https://api.aiproxy.io/v1'

@app.route('/')
def home():
    llm = OpenAI(temperature=0.9)
    text = "What would be a good company name a company that makes colorful socks?"

    return llm(text)
