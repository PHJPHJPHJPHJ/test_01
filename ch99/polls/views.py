from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice
# from django.views.decorators.csrf import csrf_exempt
# import random

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question' : question})



"""
nextId = 4
topics = [
    {'id' : 1,
     'title' : '전자통신컴퓨터공학부',
     'body' : '전자통신컴퓨터공학부에 오신것을 환영합니다.'},
     {'id' : 2,
     'title' : '간호학과',
     'body' : '간호학과에 오신것을 환영합니다.'},
     {'id' : 3,
     'title' : '유아교육과',
     'body' : '유아교육과에 오신것을 환영합니다.'},
]   

def HTML_Temp(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}"> {topic["title"]}</a></li>'
    return f'''
    <html>
        <head>
        </head>
        <body>
            <h1><a href="/">Django</a></h1>
            <ol>
                {ol}
            </ol>
            {articleTag}
            <ul>
                <li><a href="/create/">create</a></li>
            </ul>
        </body>
    </html>
    '''

def index(request):
    article = '''
    <h2>Welcome</h2>
    <p>안녕하세요.</br><b>쟝고입니다.</b></p>
    '''
    return HttpResponse(HTML_Temp(article))

@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''

        return HttpResponse(HTML_Temp(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId, "title":title, "body":body}
        topics.append(newTopic)
        nextId+=1
        return HttpResponse(HTML_Temp('aaa'))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTML_Temp(article))

def lotto(request):
    c = ''
    b = random.sample(range(1, 46), 6)
    b.sort()
    for i in range(6):
        c += str(b[i]) + ' '
    return HttpResponse('오늘의 행운 번호는 '+c+'입니다.')
"""