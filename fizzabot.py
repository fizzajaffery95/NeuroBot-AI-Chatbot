from google import genai

client = genai.Client(api_key="AQ.Ab8RN6LMYHVdalXlaw5l7zUzG3h3QhJiM4d3PNjoCZ3LP2qptA")

system_prompt = """
You are NeuroBot, a friendly AI Study Assistant.

Rules:
- Help students learn AI, Python, and Prompt Engineering.
- Be polite and encouraging.
- Keep answers simple.
- Politely refuse unsafe requests.
"""

print("NeuroBot is ready!")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"{system_prompt}\n\nUser: {user}"
    )

    print("\nNeuroBot:")
    print(response.text)
    print()