from django.shortcuts import render, redirect
from .form import RegistrationForm, LoginForm, UserUpdateForm, ProfileUpdateForm, MusicForm
from django.contrib.auth import authenticate, login, logout
from . import models 
from .models import Music, Flashcard 
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.http import HttpResponse
import random


def quiz(request):
    return render(request, 'quiz.html')



def main(request):
    return render(request, 'main.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('quiz')
            else:
                form.add_error(None, 'Invalid login credentials.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

def category(request):
    categories = models.QuizCategory.objects.all()
    return render(request, 'category.html', {'data': categories})

@login_required
def questions(request, cat_id):
    category=models.QuizCategory.objects.get(id=cat_id)
    question=models.QuizQuestion.objects.filter(category=category).order_by('id').first()
    return render(request, 'questions.html', {'question': question, 'category':category})


@login_required
def submit(request, cat_id, q_id):
    if request.method=='POST':
        category = models.QuizCategory.objects.get(id=cat_id)
        question = models.QuizQuestion.objects.filter(category=category, id__gt=q_id).exclude(id=q_id).order_by(
            'id').first()
        if 'skip' in request.POST:
            if question:
                q=models.QuizQuestion.objects.get(id=q_id)
                user=request.user
                ans='Not Submitted'
                models.SubmittedAnswer.objects.create(user=user, question=q, answer=ans)
                return render(request, 'questions.html', {'question': question, 'category': category})
        else:
            q=models.QuizQuestion.objects.get(id=q_id)
            user=request.user
            ans=request.POST['answer']
            models.SubmittedAnswer.objects.create(user=user, question=q, answer=ans )

        if question:
           return render(request, 'questions.html', {'question': question, 'category':category})
        else:
           result=models.SubmittedAnswer.objects.filter(user=request.user)
           skipped = models.SubmittedAnswer.objects.filter(user=request.user, answer="Not Submitted").count()
           attempt = models.SubmittedAnswer.objects.filter(user=request.user).exclude(answer="Not Submitted").count()

           rightAnswer=0
           percent=0
           for row in result:
               if row.question.right_ans == row.answer:
                    rightAnswer+=1

           percent=(rightAnswer*100)/10

           return render(request, 'result.html', {'result': result, 'total_skipped': skipped, 'attempt': attempt, 'rightAnswer': rightAnswer,'percent': percent})
    else:
        return HttpResponse('ERROR!')
    

def music_list(request):
    musics = Music.objects.all()
    return render(request, 'music_list.html', {'musics': musics})

@permission_required('quiz.add_music', raise_exception=True)
def add_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music_list')
    else:
        form = MusicForm()
    return render(request, 'add_music.html', {'form': form})

@permission_required('quiz.delete_music', raise_exception=True)
def remove_music(request, id):
    Music.objects.filter(id=id).delete()
    return redirect('music_list')

def flashcard_view(request):
    flashcard = random.choice(Flashcard.objects.all())
    context = {'flashcard': flashcard}
    return render(request, 'flashcard.html', context)


def all_questions(request):
    questions = models.QuizQuestion.objects.all()
    return render(request, 'all_questions.html', {'questions': questions})


def instructions(request):
    return render(request, 'instruction.html')