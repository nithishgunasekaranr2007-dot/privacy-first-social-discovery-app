from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Social Discovery API is running!",
        "status": "success"
    })


def health_check(request):
    return JsonResponse({
        "status": "healthy"
    })
