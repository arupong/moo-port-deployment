from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'first_app/4_cover_port.html')

def home(request):
    return render(request,'first_app/1_Online_portfolio.html')

def cert(request):
    return render(request,'first_app/2_Certification.html')

def lightQuiz(request):
    return render(request,'first_app/3_Port_quiz.html')

def c4game(request):
    return render(request,'first_app/C4Game.html')
