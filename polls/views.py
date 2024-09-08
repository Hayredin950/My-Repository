from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question

# Create your views here.

def index(request):
    ql=Question.objects.order_by('-pd')
    return render(request,'polls/index.html',{'ql':ql})

def detail(request, qid):
    try:
        q=Question.objects.get(pk=qid)
    except Question.DoesNotExist:
        raise Http404("question ain't available")
    return render(request,'polls/detail.html',{'q':q})


def result(request, qid):
    q=get_object_or_404(Question,pk=qid)
    return render(request,'polls/result.html',{'q':q})


    
def vote(request, qid):
    q = get_object_or_404(Question, pk = qid)
    try:
        sc = q.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls / detail.html', {
            'q': q,
            'error_message': "You didn't select a choice.",
        })
    else:
        sc.v +=1
        sc.save()
    
        return HttpResponseRedirect(reverse('polls:result', args =(qid, )))
        