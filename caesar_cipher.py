def encrypt (text, shift):
  result = ""
  for char in text:
    if char.isalpha():
      ascii_offset = 65 if char.isupper() else 97
      result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
    else:
      result += char
  return result

def decrypt(text, -shift):
  return encrypt(text, -shift)

#testing
if _name_ == "__main__":
  message = "Hello, why you here?"
  shift = 5

  encrypted = encrypt(message, shift)
  decrypted = decrypt(encrypted, shift)

  print(f"Original: {message}")
  print(f"Encrypted: {encrypted}")
  print(f"Decrypted: {decrypted}")
