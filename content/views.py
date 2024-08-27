import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from content.models import Work


class AjaxHandler(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'content/base.html')

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        num = data['number']
        day_of_week = data['day']
        lst = list(Work.objects.filter(workdays__contains=[num]).values('name'))
        return JsonResponse({'People': f"{day_of_week}: {[i.get('name') for i in lst]}"})
