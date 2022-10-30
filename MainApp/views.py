from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import csv

# Create your views here.
data=open('C:\Users\HP\NIFTY_F1_Xm8mAtb.txt')
read=csv.reader(data)
class JSON(View):
    def get(self,request):
        global read
        cs=self.read
        return HttpResponse(cs,contenttype='application/json')
