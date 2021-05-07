import base64
file = open("txt", "r")
data = file.read()
code = " "
for i in range(50):
    code = base64.b64decode(data)
    data = code

print(data)
