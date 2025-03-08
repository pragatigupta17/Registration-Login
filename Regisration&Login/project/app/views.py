from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        name=request.POST.get('username')
        email=request.POST.get('email')
        detail=request.POST.get('detail')
        phone=request.POST.get('phone')
        dob=request.POST.get('dob')
        subscribe=request.POST.getlist('subscribe')
        gender=request.POST.get('gender')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        profile_pic=request.FILES.get('profile-pic')
        resume=request.FILES.get('resume')
        print(name,email,detail,phone,dob,subscribe,gender,password,cpassword,profile_pic,resume)
        user = Student.objects.filter(email=email)
        if user:
            x = "Email already exist"
            return render(request, 'register.html', {'msg': x})
        else:
            pass
            if password==cpassword:
                user = Student.objects.create(name=name, email=email, detail=detail, phone=phone,dob=dob,subscribe=subscribe,gender=gender,password=password,profile_pic=profile_pic,resume=resume)
                x="Regisration Successfully"
                return render(request,'login.html',{'msg':x})
            else:
                x="Password and Confirm Password does not match"
                return render(request,'register.html',{'msg':x,'name':name, 'email':email, 'detail':detail, 'phone':phone,'dob':dob,'subscribe':subscribe,'gender':gender,'profile_pic':profile_pic,'resume':resume})
        
    else:
            return render(request, 'register.html')

def login(request):
    print(request.method)
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user = Student.objects.filter(email=email)
        print(user)
        if user:
            data = Student.objects.get(email=email)
            # print(data.name)
            # print(data.email)
            # print(data.detail)
            # print(data.phone)
            # print(data.subscribe)
            # print(data.gender)
            # print(data.dob)
            # print(data.profile_pic)
            # print(data.resume)
            # print(data.password)
            user_data={
                'name':data.name,
                'email':data.email,
                'detail':data.detail,
                'phone':data.phone,
                'subscribe':data.subscribe,
                'gender':data.gender,
                'dob':data.dob,
                'profile_pic':data.profile_pic,
                'resume':data.resume,
                'password':data.password,
            }
            print(user_data)
            pass1 = data.password
            if pass1 == password:
                return render(request,'dashboard.html',{'name':data.name,'email':data.email,'data':user_data,})
            else:
                msg = "Email and password not match"
                return render(request, 'login.html',{'msg':msg})
        else:
            mag = "Email id not exist"
            return render(request,'register.html',{'msg':mag})
    else:
        return render(request, 'login.html')

