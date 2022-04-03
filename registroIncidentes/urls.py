from django.contrib import admin
from django.urls import path, re_path, include

def testURL(self):
    print('=====Test URL==========')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',testURL),
    re_path('',include('applications.mainapp.urls'))
]
