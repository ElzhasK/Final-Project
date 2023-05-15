from django.contrib import admin
from . import models
from .models import Profile, Flashcard


admin.site.register(Profile)

admin.site.register(models.QuizCategory)
admin.site.register(models.QuizQuestion)
admin.site.register(models.SubmittedAnswer)
admin.site.register(Flashcard)