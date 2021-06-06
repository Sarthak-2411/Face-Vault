from django.db.models import base
from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.
def home(request):
    if request.user.username == '':        
        return redirect('page_not_found')
    base_folder = 'media/'
    user_folder = 'User'+str(request.user.id)+'/'
    file_list = list_of_files(user_folder)
    fs = FileSystemStorage()      
    files=[]
    for f in file_list:
        data = {}
        data['name'] = f
        d = fs.get_created_time(user_folder+f)
        data['date_uploaded'] = d.date
        size = format((fs.size(user_folder+f)/1024)/1024, '.2f')  
        data['size'] =  str(size) + " MB"
        files.append(data)

    return render(request, 'home_page/home_page.html',{'files':files})

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        # name = fs.save(uploaded_file.name, uploaded_file)
        base_folder = 'media/'
        user_folder = 'User'+str(request.user.id)+'/'
        file = user_folder+uploaded_file.name

        if fs.exists(file):
            fs.delete(file)    
             
        fs.save(file,uploaded_file)

        return redirect('home')
    return redirect('page_not_found')

def edit_file(request, old_name, new_name):
    if request.user.username == '':        
        return redirect('page_not_found')
    base_folder = 'media/'
    user_folder = 'User'+str(request.user.id)+'/'
    os.rename(base_folder+user_folder+old_name,     base_folder+user_folder+new_name)
    # return HttpResponse('oldname = '+ old_name + '  newname = '+new_name)
    return redirect('home')

def delete_file(request, name):
    if request.user.username == '':        
        return redirect('page_not_found')
    base_folder = 'media/'
    user_folder = 'User'+str(request.user.id)+'/'
    fs = FileSystemStorage()
    fs.delete(user_folder+name)

    return redirect('home')

def download(request,file):
    if request.user.username == '':        
        return redirect('page_not_found')
    base_folder = 'media/'
    user_folder = 'User'+str(request.user.id)+'/'
    try:
        with open(base_folder+user_folder+file, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(base_folder+user_folder+file)
            return response
    except Exception:
        return redirect('page_not_found')

    return redirect('home')

def open_file(request,file):
    if request.user.username == '':        
        return redirect('page_not_found')
    
    base_folder = 'media/'
    user_folder = 'User'+str(request.user.id)+'/'
    try:
        with open(base_folder+user_folder+file, 'rb') as fh:
            extension = fh.name.split('.')[1]
            if(extension == 'pdf'):
                response = HttpResponse(fh.read(), content_type="application/pdf")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(base_folder+user_folder+file)
                return response
            elif(extension == 'txt'):
               return HttpResponse(fh.read(), content_type="text/plain")
            else:                 
                response = HttpResponse(fh.read(), content_type='application/*')
                response['Content-Disposition'] = 'inline;filename' + os.path.basename(base_folder+user_folder+file)
                return response

    except Exception:
        return redirect('page_not_found')

def list_of_files(folder):
    files=[]
    for base, dir, file in os.walk('media/'+folder):
            for i in file:
                files.append(i)
    return files
