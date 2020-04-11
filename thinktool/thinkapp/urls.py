from django.urls import path
from . import views

# app_name="testuu"
urlpatterns = [
    # path('', views.testindex, name='testindex'),
    path('SortAdd', views.SortAdd.as_view() , name='SortAdd'),
    path('SortList', views.SortList, name='SortList'),
    path('FrameAdd', views.FrameAdd.as_view(), name='FrameAdd'),
    path('', views.frameList, name='frameList'),
    path('SolutionAdd/<int:frameT_id>', views.SolutionAdd.as_view(), name='SolutionAdd'),
    path('framedetail/<int:frameT_id>', views.framedetail, name='framedetail'),
    path('solutiontail/<int:frameT_id>', views.solutiontail, name='solutiontail'),

]
