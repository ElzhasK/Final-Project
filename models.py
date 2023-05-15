from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class QuizCategory(models.Model):
    quizName = models.CharField(max_length=200)
    quizImage = models.ImageField(upload_to='quiz_img/')
    quizDetail = models.TextField()

    def __str__(self):
        return self.quizName


class QuizQuestion(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question = models.TextField()
    ans_1 = models.CharField(max_length=200)
    ans_2 = models.CharField(max_length=200)
    ans_3 = models.CharField(max_length=200)
    ans_4 = models.CharField(max_length=200)
    right_ans = models.CharField(max_length=200)
    time = models.IntegerField()

    def __str__(self):
        return self.question


class SubmittedAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Music(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    music_file = models.FileField(upload_to='music/')

    def __str__(self):
        return self.title
    
class Flashcard(models.Model):
    text = models.TextField()