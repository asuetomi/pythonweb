from django.shortcuts import render
from django.http import HttpResponse
from . forms import ChatForm

# Create your views here.
def chatbot(request):
    # return HttpResponse("This is Chatbot speaking...")
    my_dict = {
        'form':ChatForm(),
        # 'insert_data':'DATA',
        'lines':[],
        # 'conversation' : [],
        'mode':'chat',
        'prompt':'何か言って',
    }
    if (request.method == 'POST'):
        my_dict['lines'].append(request.POST['txt'])
        my_dict['lines'].extend(request.POST['lines'].split(","))
        if 'chat' == request.POST['mode']:
            # チャット
            my_dict['prompt'] = request.POST['txt']
            my_dict['mode'] = 'chat'
            pass

        if 'siritori' == request.POST['mode']:
            # しりとり
            pass

        if len(my_dict['lines']) > 1:
            my_dict['form'] = ChatForm(initial = {
                'lines' : ",".join(map(str,my_dict['lines']))
            })
        else:
            my_dict['form'] = ChatForm(initial = {
                'txt'   : {'label': my_dict['prompt']},
                'lines' : my_dict['lines'],
                'prompt': my_dict['prompt'],
                'mode'  : my_dict['mode']
            })

    
    return render(request, 'chatbot.html', my_dict)
