import base64

base64string = input('Give me your base64:  ')

text = base64.b64decode(base64string).decode('utf-8')

print(f"String ==> {text}")
