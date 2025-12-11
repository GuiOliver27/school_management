from django.http import JsonResponse


def estudantes(requests):
    if requests.method == "GET":
        estudantes = {"id": 1, "nome": "Guru", "idade": 20}
        return JsonResponse(estudantes)