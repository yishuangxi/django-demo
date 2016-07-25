from django.http import HttpResponse, JsonResponse


def test(request):
    return JsonResponse({"code": 1, "data": {"name": "lifeng", "age": 30}})


def messages(request):

    return JsonResponse({
        "code": 1,
        "data": [
            {
                "title": "title 1",
                "content": "content 1"
            }, {
                "title": "title 2",
                "content": "content 2"
            }
        ]})
