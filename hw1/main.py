import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

models = [
    "gemini-3-flash-preview",
    "gemini-3.1-flash-lite-preview"
]

prompt = "Explain in three short sentences why version control is important."

print("Prompt:", prompt)
print()

for model in models:
    print("=" * 50)
    print("MODEL:", model)

    start = time.time()

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    end = time.time()

    print("Response:")
    print(response.text)

    usage = getattr(response, "usage_metadata", None)

    if usage:
        print("Input tokens:", usage.prompt_token_count)
        print("Output tokens:", usage.candidates_token_count)
        print("Total tokens:", usage.total_token_count)

    print("Latency:", round(end - start, 3), "seconds")