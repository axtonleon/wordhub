from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('template_outling/', views.template_outling, name='template_outling'),
    path('fact_checking/', views.fact_checking, name='fact_checking'),
    path('grammer_checking/', views.grammer_checking, name='grammer_checking'),
    path('paraphraser/', views.paraphraser, name='paraphraser'),
    path('word_search/', views.word_search, name='word_search'),
    path('keyword_extractor/', views.keyword_extractor, name='keyword_extractor'),
    path('summerizer/', views.summerizer, name='summerizer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)