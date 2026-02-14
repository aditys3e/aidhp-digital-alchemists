import anthropic
import os

# It's recommended to use environment variables for API keys
# Set your API key as: export ANTHROPIC_API_KEY='your-api-key-here'
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

# message.content is a list of content blocks
# Access the text content from the first block
print(message.content[0].text)
