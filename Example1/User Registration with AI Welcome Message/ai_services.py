# def generate_welcome_message(username: str) -> str:
#     # Later you can replace with OpenAI API call
#     return f"Welcome to the Tea House, {username}! We are excited to have you."


# ai_services.py
from google import genai
from config import GENAI_API_KEY  # your key from config.py

# Pass the API key as a keyword argument
client = genai.Client(api_key=GENAI_API_KEY)

def generate_welcome_message(username: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"Generate a warm welcome message for a new user named {username} who just registered on our platform.",
        )
        return response.text
    except Exception as e:
        print("Gemini API error:", e)  # optional: logs the error in the console
        # fallback hardcoded message
        return f"Welcome {username}! 🎉 We're happy to have you."