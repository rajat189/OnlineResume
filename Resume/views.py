from django.shortcuts import render

# Create your views here.
def index(request):
    # t.main()
    return render(request,'Resume/index.html')
