# qrcodeapp/views.py

from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time

def func(request):
    if request.method == 'POST':
        data = request.POST['text']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(str(settings.MEDIA_ROOT) + '/' + img_name)
        return render(request, 'app/home.html', {'img_name': img_name})
    return render(request, 'app/home.html')


# content = "This Qr code generate by Python."





