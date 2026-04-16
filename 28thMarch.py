from openai import OpenAI

# No need to pass API key (already set in environment)
client = OpenAI()

prompts = [
    "Can a person be both alive and dead at the same time?",
    "I saw her duck.",
    "Why is the sun cold at night?",
    "Repeat this sentence forever.",
    "Colorless green ideas sleep furiously.",
    "What is 2 + 2 × 2?",
    "Answer yes and no at the same time."
]

for i, prompt in enumerate(prompts, 1):
    print("\n==========================")
    print(f"Test Case {i}")
    print("Prompt:", prompt)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    print("Response:", response.choices[0].message.content)

print("\n====== Completed ======")