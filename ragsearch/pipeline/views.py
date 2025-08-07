from django.shortcuts import render
from django.http import HttpResponse
from pipeline.search import hybrid_search

def index(request):
    return HttpResponse("RAG System is Live!")

def search_view(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = hybrid_search(query)

    return render(request, 'search.html', {'query': query, 'results': results})
