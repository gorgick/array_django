import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


class AjaxHandler(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'content/base.html')

    def post(self, request, *args, **kwargs):
        print(request.body)
        data = json.loads(request.body)
        print(data)
        float_num = data['number']
        return JsonResponse({'float': f'You got {float_num}'})
