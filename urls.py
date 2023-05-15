from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('quiz/', views.quiz, name='quiz'),
    path('main/', views.main, name='main'),
    path('registration/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('category/', views.category, name='category'),
    path('questions/<int:cat_id>', views.questions, name='questions'),
    path('submit/<int:cat_id>/<int:q_id>', views.submit, name='submit'),
    path('music_list/', views.music_list, name='music_list'),
    path('add_music/', views.add_music, name='add_music'),
    path('remove_music/<int:id>/', views.remove_music, name='remove_music'),
    path('flashcard/', views.flashcard_view, name='flashcard'),
    path('all-questions/', views.all_questions, name='all_questions'),
    path('instructions/', views.instructions, name='instructions'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
