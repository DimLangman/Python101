import base64
# encodata = base64.b64encode(b'Encode this text')
# print("Encoded text with base 64 is")
# print(encodata)

inputtxt = input("Enter text: ")
print (inputtxt)
print("Encoded text with base 64 is")
data1 = base64.b64encode(inputtxt.encode())
print(data1)

print("Decoded text with base 64 is")
data2 = base64.b64decode(data1).decode('utf-8')
print(data2)

data3 = base64.b64decode(b'NzJ0Z25ncGxncm0=').decode('utf-8')
print (data3)

