import anthropic

client = anthropic.Anthropic(
    api_key="your-api-key-here"  # Better: use environment variable
)

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

print(message.content)
