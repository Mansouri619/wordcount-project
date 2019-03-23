from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def homepage(request):
    return HttpResponse("My first page")

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    mywords = {}
    for word in words:
        if word in mywords:
            mywords[word] += 1
        else:
            mywords[word] = 1
    # print(fulltext)
    return render(request,'count.html',{'fulltext' : fulltext,'count' : len(words),'mywords' : mywords})

def about(request):
    return render(request,'about.html')
