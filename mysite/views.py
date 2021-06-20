
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
      return render(request,'index.html')

def analyze(request):
      djtext= request.POST.get('text','default')
      
      extraspaceremover= request.POST.get('extraspaceremover','default')
      newlineremover= request.POST.get('newlineremover','default')
      fullcaps= request.POST.get('fullcaps','default')
      removepunc= request.POST.get('removepunc','off')
      
      if removepunc== "on":
             punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
             analyzed = ""
             for char in djtext:
               if char not in punctuations:
                  analyzed = analyzed +char

             params = { 'purpose': 'Remove Punctuations','analyzed_text':analyzed}
             djtext = analyzed
   
           
      if(fullcaps=="on"):
            analyzed = ""     
            for char in djtext:
                analyzed= analyzed + char.upper()
            params = { 'purpose': 'Change to uppercase','analyzed_text':analyzed}
            djtext = analyzed

      if(newlineremover=="on"):
            analyzed = ""     
            for char in djtext:
                  if char !="\n" and char !="\r":
                    analyzed= analyzed + char
            params = { 'purpose': 'Removed NEwlines','analyzed_text':analyzed}
            djtext = analyzed
      
      if(extraspaceremover=="on"):
            analyzed = ""     
            for index, char in enumerate (djtext) :
                  if djtext[index] == " " and djtext[index+1]==" ":
                        pass
                  else:
                       analyzed= analyzed + char
            params = { 'purpose': 'Removed Extra space','analyzed_text':analyzed}
            djtext = analyzed
            
            return HttpResponse("Error")
      return render (request, 'analyze.html',params) 








    