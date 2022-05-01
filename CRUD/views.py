from django.shortcuts import render, get_object_or_404
from .models import Question
from .forms import QuestionForm

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'CRUD/index.html', {'questions': questions})

def create(request):
    context = {}
    question_form_create = QuestionForm(request.POST or None)
    if question_form_create.is_valid():
        question_form_create.save()
        return render(request, 'CRUD/create.html', {'question': question_form_create})
    context['question'] = question_form_create
    return render(request, 'CRUD/create.html', context)

def update(request, id):
    context = {}
    question = get_object_or_404(Question, pk=id)
    question_form_update = QuestionForm(request.POST or None, instance=question)
    if question_form_update.is_valid():
        question_form_update.save()
    context['question'] = question_form_update
    return render(request, 'CRUD/update.html', context)

def delete(request, id):
    question = get_object_or_404(Question, pk=id)
    if request.method == 'POST':
        question.delete()