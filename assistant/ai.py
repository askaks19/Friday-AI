from client import client

SYSTEM_PROMPT = (
    "You are a virtual assistant named Friday. "
    "You give short, clear, helpful responses."
)

def ai_process(command: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{SYSTEM_PROMPT}\nUser: {command}"
    )
    return response.text

