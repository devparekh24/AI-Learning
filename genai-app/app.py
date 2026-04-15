import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("AI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")


def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    user_input = input("Ask something: ")
    answer = generate_response(user_input)
    print("\nAI:", answer)
