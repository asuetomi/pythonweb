from django.shortcuts import render
from django.http import HttpResponse
from . forms import ChatForm
from . chat import chat

# Create your views here.
def chatbot(request):
    # return HttpResponse("This is Chatbot speaking...")
    my_dict = {
        'form':ChatForm(),
        # 'insert_data':'DATA',
        'txt':"",
        'lines':[],
        # 'conversation' : [],
        'mode':'chat',
        'prompt':'何か言って',
    }
    if (request.method == 'POST'):
        my_dict['lines'].append(request.POST['prompt'])
        if 'chat' == request.POST['mode'] or 'answer' == request.POST['mode'] :
            # チャット
            my_dict['txt'] = request.POST['txt']
            my_dict = chat(my_dict)
            # my_dict['prompt'] = request.POST['txt']
            # my_dict['mode'] = 'chat'

        if 'siritori' == request.POST['mode']:
            # しりとり
            pass

        my_dict['lines'].extend(request.POST['lines'].split(","))

        if len(my_dict['lines']) > 1:
            my_dict['form'] = ChatForm(initial = {
                # 'txt'   : {'label': my_dict['prompt'],'value':"",},
                'lines' : ",".join(map(str,my_dict['lines'])),
                'prompt': my_dict['prompt'],
                'mode'  : my_dict['mode'],
            })
        else:
            my_dict['form'] = ChatForm(initial = {
                # 'txt'   : {'label': my_dict['prompt'],'value':"",},
                'lines' : my_dict['lines'],
                'prompt': my_dict['prompt'],
                'mode'  : my_dict['mode'],
            })

    
    return render(request, 'chatbot.html', my_dict)
