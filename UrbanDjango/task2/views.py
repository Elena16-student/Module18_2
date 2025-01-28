from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func_templ(request):
    return render(request, 'second_task/func_templ.html')

class TemplateClass(TemplateView):
    template_name = 'second_task/class_templ.html'
