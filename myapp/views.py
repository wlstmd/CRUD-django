from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

nextId = 4
topics = [
  {'id':1, 'title':'routing', 'body':'Routing is ..'},
  {'id':2, 'title':'view', 'body':'View is ..'},
  {'id':3, 'title':'Model', 'body':'Model is ..'},
]

def index(request):
    return render(request, 'myapp/index.html', {'topics': topics})

def read(request, id):
    topic = next((topic for topic in topics if topic['id'] == int(id)), None)
    if topic:
        return render(request, 'myapp/read.html', {'topic': topic, 'topics': topics, 'current_topic_id': id, 'current_page': 'read'})
    else:
        return HttpResponse('No topic found with given id')

@csrf_exempt
def create(request):
  global nextId
  if request.method =='POST':
    title = request.POST["title"]
    body = request.POST["body"]
    newTopic = {"id":nextId, "title":title, "body":body}
    topics.append(newTopic)
    url = '/read/' + str(nextId)
    nextId = nextId + 1
    return redirect(url)
  return render(request, 'myapp/create.html', {'topics': topics, 'current_page': 'create'})


@csrf_exempt
def update(request, id):
  topic = next((topic for topic in topics if topic['id'] == int(id)), None)
  if request.method == 'POST' and topic:
    topic['title'] = request.POST['title']
    topic['body'] = request.POST['body']
    return redirect(f'/read/{id}')
  return render(request, 'myapp/update.html', {'topic': topic, 'topics': topics, 'current_topic_id': id})

@csrf_exempt
def delete(request, id):
  global topics
  topics = [topic for topic in topics if topic["id"] != int(id)]
  return redirect('/')
