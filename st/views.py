from django.shortcuts import render

# Create your views here.
def index(myrequest):
    # pamdict = {'name':'老铁'}
    return render(myrequest,'index.html')
