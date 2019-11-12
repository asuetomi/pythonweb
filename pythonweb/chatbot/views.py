from django.shortcuts import render
from django.http import HttpResponse
from . forms import ChatForm

# Create your views here.
def chatbot(request):
    # return HttpResponse("This is Chatbot speaking...")
    my_dict = {
        'form':ChatForm(),
        'insert_data':'DATA',
        'lines':'DATA',
    }
    if (request.method == 'POST'):
        my_dict['lines'] = request.POST['lines'] + request.POST['txt']
        my_dict['insert_data'] = '入力文字:' + request.POST['txt']
        my_dict['form'] = ChatForm(request.POST)
    
    return render(request, 'chatbot.html', my_dict)
