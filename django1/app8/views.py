from django.shortcuts import render
from datetime import datetime

def index(request):
    encoded_message = None
    if request.method == 'POST':
        message = request.POST.get('message')
        today = datetime.today()
        day = today.day
        if day % 2 == 0:
            encoded_message = encode_message(message, even=True)
        else:
            encoded_message = encode_message(message, even=False)
        return render(request, 'app8/index.html', {'encoded_message': encoded_message, 'message': message})
    return render(request, 'app8/index.html')

def encode_message(message, even):
    result = []
    for char in message.upper():
        if 'A' <= char <= 'Z':
            if even:
                code = 500 + ord(char) - ord('A') + 1
            else:
                code = ord(char) - ord('A') + 1
            result.append(f'{code:02d}')
        else:
            result.append(char)
    return ' '.join(result)
