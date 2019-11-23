from django.shortcuts import render
from django.http import HttpResponse
from . forms import ChatForm

# Create your views here.
def chatbot(request):
    # return HttpResponse("This is Chatbot speaking...")
    my_dict = {
        'form':ChatForm(),
        'insert_data':'DATA',
        'lines':[],
        'conversation' : [],
    }
    if (request.method == 'POST'):
        # my_dict['lines'] = request.POST['lines'] + request.POST['txt']
        # my_dict['insert_data'] = '入力文字:' + request.POST['txt']
        # for line in request.POST['lines']:
        #     my_dict['lines'].append(line)
        # my_dict['lines'] = request.POST['lines']
        my_dict['lines'].append(request.POST['txt'])
        my_dict['lines'].extend(request.POST['lines'].split(","))
        # my_dict['lines'].append(request.POST['txt'])
        # my_dict['insert_data'] = "行数" +　str(my_dict['lines'].count)
        # request.POST['lines'] = my_dict['lines']
        # my_dict['conversation'].append(request.POST['txt'])
        # my_dict['form'] = ChatForm(request.POST)
        if len(my_dict['lines']) > 1:
            my_dict['form'] = ChatForm(initial = {
                'lines' : ",".join(map(str,my_dict['lines']))
            })
        else:
            my_dict['form'] = ChatForm(initial = {
                'lines' : my_dict['lines']
            })

    
    return render(request, 'chatbot.html', my_dict)
