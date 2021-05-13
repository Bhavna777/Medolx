from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from .models import Message
from .serializers import MessageSerializer, UserSerializer
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html')



def doctors(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'doctors.html',{'doctors':doctors})


def doctor(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    mydict={'doctor':doctor}
    return render(request,'doctor.html',context=mydict)


def products(request):
    products=models.Product.objects.all().filter()
    return render(request,'products.html',{'products':products})


def product(request,pk):
    product=models.Product.objects.get(id=pk)
    mydict={'product':product}
    return render(request,'product.html',context=mydict)



def blogs(request):
    blogs=models.Blog.objects.all().filter()
    return render(request,'blogs.html',{'blogs':blogs})


def blog(request,pk):
    blog=models.Blog.objects.get(id=pk)
    mydict={'blog':blog}
    return render(request,'blog.html',context=mydict)



def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('dashboard')
        else:
            return HttpResponseRedirect('signin')
    return render(request, 'signin.html')



def signup(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            patient=patientForm.save(commit=False)
            patient.user=user
            patient.status=True
            patient.save()

            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)

        return HttpResponseRedirect('signin')
    return render(request,'signup.html',context=mydict)


def contact(request):
    if request.method=='POST':
        contactForm=forms.ContactForm(request.POST, request.FILES)
        if contactForm.is_valid():
            contact=contactForm.save()
            contact.save()

    return render(request, 'contact.html')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'dashboard.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    # return render(request, 'admin_dashboard.html')
    #for both table in admin dashboard
    doctors=models.Doctor.objects.all().order_by('-id')
    patients=models.Patient.objects.all().order_by('-id')
    #for three cards
    doctorcount=models.Doctor.objects.all().filter(status=True).count()
    pendingdoctorcount=models.Doctor.objects.all().filter(status=False).count()

    patientcount=models.Patient.objects.all().filter(status=True).count()
    pendingpatientcount=models.Patient.objects.all().filter(status=False).count()

    # appointmentcount=models.Appointment.objects.all().filter(status=True).count()
    # pendingappointmentcount=models.Appointment.objects.all().filter(status=False).count()
    mydict={
    'doctors':doctors,
    'patients':patients,
    'doctorcount':doctorcount,
    'pendingdoctorcount':pendingdoctorcount,
    'patientcount':patientcount,
    'pendingpatientcount':pendingpatientcount,
    # 'appointmentcount':appointmentcount,
    # 'pendingappointmentcount':pendingappointmentcount,
    }
    return render(request,'admin_dashboard.html',context=mydict)


@user_passes_test(lambda u: u.is_superuser)
def admin_doctor(request):
    return render(request, 'admin_doctor.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_view_doctor(request):
    # return render(request, 'admin_view_doctor.html')
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'admin_view_doctor.html',{'doctors':doctors})


@user_passes_test(lambda u: u.is_superuser)
def admin_add_doctor(request):
    # return render(request, 'admin_add_doctor.html')
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST, request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor.status=True
            doctor.save()

            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)

        return HttpResponseRedirect('admin_view_doctor')
    return render(request,'admin_add_doctor.html',context=mydict)


@user_passes_test(lambda u: u.is_superuser)
def admin_update_doctor(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)

    userForm=forms.DoctorUserForm(instance=user)
    doctorForm=forms.DoctorForm(request.FILES,instance=doctor)
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST,instance=user)
        doctorForm=forms.DoctorForm(request.POST,request.FILES,instance=doctor)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.status=True
            doctor.save()
            return redirect('admin_view_doctor')
    return render(request,'admin_update_doctor.html',context=mydict)

@user_passes_test(lambda u: u.is_superuser)
def admin_delete_doctor(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)
    user.delete()
    doctor.delete()
    return redirect('admin_view_doctor')

@user_passes_test(lambda u: u.is_superuser)
def admin_patient(request):
    return render(request, 'admin_patient.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_view_patient(request):
    # return render(request, 'admin_view_patient.html')
    patients=models.Patient.objects.all().filter()
    return render(request,'admin_view_patient.html',{'patients':patients})
    print(patients)

@user_passes_test(lambda u: u.is_superuser)
def admin_add_patient(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            patient=patientForm.save(commit=False)
            patient.user=user
            patient.status=True
            patient.save()

            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)

        return HttpResponseRedirect('admin_view_patient')
    return render(request,'admin_add_patient.html',context=mydict)


@user_passes_test(lambda u: u.is_superuser)
def admin_update_patient(request,pk):
    # return render(request, 'admin_update_patient.html')
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)

    userForm=forms.PatientUserForm(instance=user)
    patientForm=forms.PatientForm(request.FILES,instance=patient)
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST,instance=user)
        patientForm=forms.PatientForm(request.POST,request.FILES,instance=patient)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.status=True
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient.save()
            return redirect('admin_view_patient')
    return render(request,'admin_update_patient.html',context=mydict)


@user_passes_test(lambda u: u.is_superuser)
def admin_delete_patient(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return redirect('admin_view_patient')


@user_passes_test(lambda u: u.is_superuser)
def admin_view_product(request):
    # return render(request, 'admin_view_product.html')
    products=models.Product.objects.all().filter()
    return render(request,'admin_view_product.html',{'products':products})


@user_passes_test(lambda u: u.is_superuser)
def admin_add_product(request):
    productForm=forms.ProductForm()
    mydict={'productForm':productForm}
    if request.method=='POST':
        productForm=forms.ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            product=productForm.save()
            product.save()

            # my_product_group = Group.objects.get_or_create(name='PRODUCT')
            # my_product_group[0].user_set.add(name)

        return HttpResponseRedirect('admin_view_product')
    return render(request,'admin_add_product.html',context=mydict)

@user_passes_test(lambda u: u.is_superuser)
def admin_update_product(request,pk):
    product=models.Product.objects.get(id=pk)

    productForm=forms.ProductForm(request.FILES,instance=product)
    mydict={'productForm':productForm}
    if request.method=='POST':
        productForm=forms.ProductForm(request.POST,request.FILES,instance=product)
        if productForm.is_valid():
            product=productForm.save()
            product.save()
            return redirect('admin_view_product')
    return render(request,'admin_update_product.html',context=mydict)


@user_passes_test(lambda u: u.is_superuser)
def admin_delete_product(request,pk):
    product=models.Product.objects.get(id=pk)
    product.delete()
    return redirect('admin_view_product')



@user_passes_test(lambda u: u.is_superuser)
def admin_view_blog(request):
    # return render(request, 'admin_view_product.html')
    blogs=models.Blog.objects.all().filter()
    return render(request,'admin_view_blog.html',{'blogs':blogs})

@user_passes_test(lambda u: u.is_superuser)
def admin_add_blog(request):
    blogForm=forms.BlogForm()
    mydict={'blogForm':blogForm}
    if request.method=='POST':
        blogForm=forms.BlogForm(request.POST, request.FILES)
        if blogForm.is_valid():
            blog=blogForm.save()
            blog.save()


        return HttpResponseRedirect('admin_view_blog')
    return render(request,'admin_add_blog.html',context=mydict)



@user_passes_test(lambda u: u.is_superuser)
def admin_update_blog(request,pk):
    blog=models.Blog.objects.get(id=pk)

    blogForm=forms.BlogForm(request.FILES,instance=blog)
    mydict={'blogForm':blogForm}
    if request.method=='POST':
        blogForm=forms.BlogForm(request.POST,request.FILES,instance=blog)
        if blogForm.is_valid():
            blog=blogForm.save()
            blog.save()
            return redirect('admin_view_blog')
    return render(request,'admin_update_blog.html',context=mydict)


@user_passes_test(lambda u: u.is_superuser)
def admin_delete_blog(request,pk):
    blog=models.Blog.objects.get(id=pk)
    blog.delete()
    return redirect('admin_view_blog')


@user_passes_test(lambda u: u.is_superuser)
def admin_view_message(request):
    # return render(request, 'admin_view_product.html')
    contacts=models.Contact.objects.all().filter()
    return render(request,'admin_view_message.html',{'contacts':contacts})




# ChatApp View 



@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == "GET":
        return render(request, 'chat/chat.html',
                      {'users': User.objects.exclude(username=request.user.username)})


def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect('chat')
    if request.method == "GET":
        return render(request, "chat/messages.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)})





def logout_view(request):
    logout(request)
    return redirect('/')