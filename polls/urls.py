from django.urls import path

from . import views

""" app_name = 'polls' """
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
# ex: /problems
# ex: /problems/problem_id
# ex: /problems/problem_id/details
# ex: /problems/problem_id/contact_method
# ex: /problems/problem_id/????
