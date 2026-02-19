import base64

message = "Hello Sandbox!"
encoded = base64.b64encode(message.encode()).decode()
decoded = base64.b64decode(encoded).decode()

print(f"Original: {message}")
print(f"Base64: {encoded}")
print(f"Decoded: {decoded}")
