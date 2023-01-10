from django.shortcuts import render, redirect
import openai
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from itertools import chain
def check_words(word):
    words = word.split()
    return len(words)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def template_outling(request):
    if request.method == 'POST':
        word = request.POST['word']
        openai.api_key = "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"

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Give an essay outline on the topic :\n\n "+ word,
        temperature=0,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        

        result = response["choices"][0]["text"]
        return render(request, 'template_outling.html', {'result': result, 'word':word})
    return render(request, 'template_outling.html')

def fact_checking(request):
    if request.method == 'POST':
        word = request.POST['word']
        openai.api_key = "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"

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write a note on :\n\n "+ word,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        

        result = response["choices"][0]["text"]
        return render(request, 'Fact_checker.html', {'result': result, 'word':word})
    return render(request, 'Fact_checker.html')

def grammer_checking(request):
    if request.method == 'POST':
        word = request.POST['word']
        confirmed = check_words(word)
        if confirmed <= 100:
            openai.api_key = "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"

            response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Convert to standard english grammer :\n\n "+ word,
            temperature=0,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
            

            result = response["choices"][0]["text"]
            return render(request, 'Grammer_checker.html', {'result': result, 'word':word})
        else:
            error = "number of word is greater than 100, please reduce to see result"
            return render(request, 'Grammer_checker.html', {'result': error, 'word':word})

    return render(request, 'Grammer_checker.html')

def paraphraser(request):
    if request.method == 'POST':
        word = request.POST['word']
        openai.api_key = "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"
        confirmed = check_words(word)
        if confirmed <= 100:
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Pharaphrase this text :\n\n "+ word,
            temperature=0.5,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
            

            result = response["choices"][0]["text"]
            return render(request, 'Paraphraser.html', {'result': result, 'word':word})
        else:
            error = "number of word is greater than 100, please reduce to see result"
            return render(request, 'Paraphraser.html', {'result': error, 'word':word})

    return render(request, 'Paraphraser.html')

def word_search(request):
    if request.method == 'POST':
        word = request.POST['word']
        openai.api_key = "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"

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="What is a :\n\n "+ word,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        

        result = response["choices"][0]["text"]
        return render(request, 'word_search.html', {'result': result, 'word':word})
    return render(request, 'word_search.html')


def keyword_extractor(request):
    if request.method == 'POST':
        word = request.POST['word']
        openai.api_key = "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"

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Extract the key words from this text :\n\n "+ word,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        

        result = response["choices"][0]["text"]
        return render(request, 'keyword_extractor.html', {'result': result, 'word':word})
    return render(request, 'keyword_extractor.html')

def summerizer(request):
    if request.method == 'POST':
        word = request.POST['word']
        openai.api_key = "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"

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=" summerize this text :\n\n "+ word,
        temperature=0,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        

        result = response["choices"][0]["text"]
        return render(request, 'summerizer.html', {'result': result, 'word':word})
    return render(request, 'summerizer.html')