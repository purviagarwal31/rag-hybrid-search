# pipeline/api.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from pipeline.search import hybrid_search

@api_view(['GET'])
def search_api(request):
    query = request.GET.get('q', '')
    if not query:
        return Response({'error': 'Query parameter `q` is required'}, status=400)

    results = hybrid_search(query)
    return Response(results)
