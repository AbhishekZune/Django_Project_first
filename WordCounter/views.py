# I have created this file
from itertools import count
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("HOME")
    return render(request , 'index.html')

def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    #check checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    charnumber=request.POST.get('charnumber','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    #check which check box is on  
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        count = 0
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
            if char in punctuation:
                count += 1
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed, 'no_of_Punctuations': count}
        #return HttpResponse("Number of punction in text are : {}".format(count))
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(charnumber == 'on'):
        charno = 0
        for char in djtext:
            charno += 1
        params = {'purpose': 'Numbers of Characters','analyzed_text': charno}
        djtext = str(charno)
        #return render(request, 'analyze.html', params)

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Lines are removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extraw Space', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")
    return render(request, 'analyze.html', params)
#def capitalize(request):
#    return HttpResponse("capitalize first")

#def newlineremove(request):
#    return HttpResponse("newlineremove")

#def spaceremover(request):
#    return HttpResponse("spaceremover <a href='/'>back</a>")

#def charcount(request):
#    return HttpResponse("charcount")
