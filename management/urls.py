from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', Management_Views, name='back'),
    url(r'^aqks/$', Aqks_Views, name='aqks'),
    url(r'^rzaqks/$', Rzaqks_Views, name='rzaqks'),
    url(r'^rzcs/$', Rzcs_Views, name='rzcs'),
    url(r'^rzcsks/$', Rzcsks_Views, name='rzcsks'),
    url(r'^show_score/$', Show_Score_Views, name='show_score'),
    url(r'^save_score/$', Save_Score_Views, name='save_score'),
    url(r'^select_object/$', Select_Object_Views, name='select_object'),
    url(r'^select_object/maintain_data/$', Maintain_Data_Views, name='maintain_data'),
    url(r'^saveobject/$', SaveObject, name='saveobject'),
    url(r'^delete_data/$', DeleteData, name='delete_data'),
    url(r'^show_select_object/$', Show_Select_Object_Views),
    url(r'^show_select_score/$', Show_Select_Score_Views),
    url(r'^updata_score/$', Updata_Score_Views),

]
