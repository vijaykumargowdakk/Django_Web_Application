from django.shortcuts import render
from django.http import HttpResponse
from num2words import num2words
from PIL import Image, ImageDraw, ImageFont
import io

def index(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        words = num2words(int(amount), to='currency', lang='en_IN').replace('euro', 'Rupees').replace('cents', 'Paise')
        return render(request, 'app7/index.html', {'amount': amount, 'words': words})
    return render(request, 'app7/index.html')

def cheque(request):
    amount = request.GET.get('amount')
    words = request.GET.get('words')
    img = Image.new('RGB', (1000, 400), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Ensure you have this font installed or adjust the path to a font available on your system
    font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'  # Update this if necessary
    try:
        font = ImageFont.truetype(font_path, 40)
    except IOError:
        font = ImageFont.load_default()

    d.text((50, 150), f"Amount: {amount}", fill=(0, 0, 0), font=font)
    d.text((50, 150), f"In Words: {words}", fill=(0, 0, 0), font=font)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(), content_type="image/png")
