from django.shortcuts import render
# from django.core.files.storage import default_storage

from .models import DataBase

import PyPDF2
import pyttsx3
import shutil

import os

# Create your views here.


def index(request):

    # try:import shutil
    # os.rmdir("./media")

    try:
        shutil.rmtree("./media")
    except:
        print()

    try:
        os.mkdir("./media")
    except:
        print()

    # if request.method == 'POST':
    #     name = request.POST.get('name')

    #     path = f"./media/{name}"
    #     if os.path.isfile(path):
    #         os.remove(path)
    #     DataBase.objects.filter(name=name).delete()
    #     return render(request, "index.html")

    return render(request, "index.html")


def player(request):

    if request.method == "POST":

        file = request.FILES['file']
        name = file.name

        print(name)
        dataBase = DataBase.objects.create(file=file, name=name)
        dataBase.save()

        path = open(f'./media/{name}', 'rb')
        pdfReader = PyPDF2.PdfReader(path)
        count = len(pdfReader.pages)
        print(count)
        text = ""
        for i in range(count):
            page = pdfReader.pages[i]
            text += page.extract_text()
        print("output : ")
        print(text)

        speak = pyttsx3.init()
        speak.save_to_file(text, f"./media/{name}.mp3")
        speak.runAndWait()
        #####

        context = {
            'name': name,
        }

        return render(request, "player.html", context=context)

    return render(request, "player.html")
