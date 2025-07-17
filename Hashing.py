
def Hashing(str):
 #utilize hashlib to return a hex version of string
  
  encoded_str = str.encode()
  hashed_str = hashlib.sha256(encoded_str)
  hex = hashed_str.hexdigest()
  return hex
