from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from users.decorators import login_required
from users.models import User
from .forms import QuestForm, AnswerForm
from .models import Question, Answer

@login_required
def dashboard(request):
    questions = Question.objects.filter(status='active').order_by('-created_at')
    return render(request, 'dashboard.html', {'questions':questions})

@login_required
def post_question(request):
    if request.method == "POST":
        form = QuestForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            user = User.objects.get(id=request.session.get('user_id'))
            question=form.save(commit=False)
            question.author = user
            question.save()
            
            messages.success(
                request, 'Question Posted Successful'
            )
            return redirect('dashboard')
    else:
        form =QuestForm()

    context = {
        'form': form
        }
    return render(request, 'post_question.html', context)

@login_required
def question_details(request, slug):
    question = get_object_or_404(
        Question,
        slug=slug
    )

    answers = question.answers.all()

    context = {
        'question': question,
        'answers': answers,
    }

    return render(
        request,
        'question_details.html',
        context
    )

@login_required
def post_answer(request, slug):
    question = get_object_or_404(Question, slug=slug)

    if request.method == "POST":
        form = AnswerForm(
            request.POST
        )

        if form.is_valid():
            user = User.objects.get(id=request.session.get('user_id'))
            answer =form.save(commit=False)
            answer.user = user
            answer.question = question
            answer.save()

            messages.success(
                request, 'Answer posted successful'
            )
            return redirect('question_details', slug=question.slug)
    form = AnswerForm()
    context = {
        'question': question,
        'form': form
        
    }
    return render(request, 'post_answer.html', context)

@login_required
def update_question(request, slug):
    user = User.objects.get(
        id=request.session.get('user_id')
    )

    question = get_object_or_404(
        Question,
        slug=slug
    )

    if question.author != user:
        messages.error(
            request,
            'You cannot edit someone else post'
        )
        return redirect('dashboard')

    form = QuestForm(
        request.POST or None,
        request.FILES or None,
        instance=question
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Question updated successful'
            )

            return redirect(
                'question_details',
                slug=question.slug
            )

    context = {
        'form': form
    }

    return render(
        request,
        'update_question.html',
        context
    )

@login_required
def question_upvotes(request, slug):
    question = get_object_or_404(Question, slug=slug)

    if request.method == 'POST':
        user = User.objects.get(id=request.session.get('user_id'))
        
        question.upvotes.add(user)

    return redirect(
        'question_details',
        slug=question.slug
        )


@login_required
def delete_question(request, slug):
    user = User.objects.get(id=request.session.get('user_id'))
    question = get_object_or_404(Question, slug=slug, author=user)
        
    if request.method == "POST":
        question.delete()
        
        messages.success(
        request, 'Question deleted!'
        )

        return redirect("dashboard")
    return render(request, 'delete_question.html', {'question': question})



    


