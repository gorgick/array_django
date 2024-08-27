import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from content.models import Work


class AjaxHandler(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'content/base.html')

    def post(self, request, *args, **kwargs):
        print(request.body)
        data = json.loads(request.body)
        print(data)
        float_num = data['number']
        workers = list(Work.objects.filter(workdays__contains=[float_num]).values('name'))
        return JsonResponse({'float': f'You got {float_num}'})
