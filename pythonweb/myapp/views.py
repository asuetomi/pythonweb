from django.shortcuts import render
from django.http import HttpResponse
from . forms import TestForm

# Create your views here.
def index(request):
    return HttpResponse("Hello")

def index_template(request):
    return render(request, 'index.html')

def index_dic(request):
    my_dict = {
        'test1':"test1の文字列",
        'test2':"test2の文字列",
    }
    return render(request,'index.html', my_dict)

def formtest(request):
    my_dict = {
        'form':TestForm(),
        'insert_data':'DATA',
    }
    if (request.method == 'POST'):
        my_dict['insert_data'] = '文字:' + request.POST['txt'] + '<br/>数値:' + request.POST['num']
        my_dict['form'] = TestForm(request.POST)
    
    return render(request, 'formtest.html', my_dict)
