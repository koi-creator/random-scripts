def xor_encrypt_decrypt_decrypt(text, key):
  ""XOR encryption (same function work for encrypt/decrypt!)"""
  result = ""
  for i, char in enumerate(text):
    result += chr(ord(char) ^ ord(key[i % len(key)]))
  return result

# test

message = "hello"
key = "secret"
encrpted = xor_encrypt_decrypt(message, key)
decrypted = xor_encrypt_decrypt(encrypted,key)
print(f"xor is magic: {decrypted}") 
