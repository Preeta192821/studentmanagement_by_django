from django.shortcuts import render
from django.contrib.auth import authenticate
# Create your views here.


def Admindashboard(request):
	return render(request,'admindashboard.html')


def Adminlogin(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}    
    return render(request,'admindashboard.html',d)
  
def Logout(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    logout(request)
    return redirect('adminlogin')


















































