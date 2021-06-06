from OnlineVault.settings import BASE_DIR
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from PIL import Image 
import os
from django.contrib.auth import login   
# Create your views here.
def webcam(request, status):
    #1 = login
    #2 = signup
    #3 = not match
    #4 = Error in matching
    messages={1:'Please verify your Face', 2:'Please capture your Face',
    3:'Face does not match Try again !',
    4:'Please Make sure only single person is there in camera and your face is not hidden'}
    if status not in messages.keys():
        return HttpResponse("Beta masti nai")
    msg = messages[status]
   
    return render(request,'face_recog/webcam.html',{'msg':msg})

def capture_and_store(request, status):
     
    
    if request.method == 'POST': 
       
        # u = User.objects.filter(email = request.session['user_mail']).first()
        identity = request.session['user_id']
        print("IDentity:",identity)
        user_photo = 'User'+str(identity)+'.jpg'
        temporary_dir = os.path.join(BASE_DIR,'temp')
        user_image_dir = os.path.join(BASE_DIR,'UserImages')


        myface = request.FILES['myface']
        print(request.FILES['myface'])
        fs_temp = FileSystemStorage(location=os.path.join(BASE_DIR,'temp'))
        fs_User = FileSystemStorage(location=os.path.join(BASE_DIR,'UserImages'))
             
        import face_recognition         
        if os.path.isfile(os.path.join(user_image_dir,user_photo)):

            # image.save(os.path.join(temporary_dir,user_photo))
            if fs_temp.exists(user_photo):
                fs_temp.delete(user_photo)
            fs_temp.save(user_photo, myface)  
            #comparison
            old_image = face_recognition.load_image_file(os.path.join(user_image_dir,user_photo))
            #face_encoding_array = face_recognition.face_encodings(old_image)

            new_image = face_recognition.load_image_file(os.path.join(temporary_dir,user_photo))
            #unknown_encoding = face_recognition.face_encodings(new_image)
            fs_temp.delete(user_photo)
            try:
                face_encoding_array = face_recognition.face_encodings(old_image)
                unknown_encoding = face_recognition.face_encodings(new_image)
                result = face_recognition.compare_faces(face_encoding_array,unknown_encoding[0])            
                print("number of face: in saved photo: ", len(face_encoding_array))
                print("number of face: in recently clicked photo: ", len(unknown_encoding))
                
                print(os.path.join(temporary_dir,user_photo))
                print(os.path.join(user_image_dir,user_photo))
                if len(face_encoding_array)!=1:
                    raise Exception
                if result[0]:
                    print("Face matched")
                    if request.user.is_authenticated:
                        return redirect('home')
                    login(request,User.objects.get(id=identity))
                    return redirect('home')
                else:

                    print("face not matched")
                    return redirect('captureandstore',3)
                   
            except Exception:
                print("Face not found")
                return redirect('captureandstore',4)
                
            
        else:
            # image.save(os.path.join(user_image_dir,user_photo))
            fs_User.save(user_photo, myface)  
            try:
                oi = face_recognition.load_image_file(os.path.join(user_image_dir,user_photo))
                face_encoding_array = face_recognition.face_encodings(oi)
                print(len(face_encoding_array))
                if len(face_encoding_array)!=1:
                    raise Exception
            except Exception:
                print("Exception oddurec")
                fs_User.delete(user_photo)  
                return redirect('captureandstore',4)
            login(request,User.objects.get(id=identity))
            return redirect('home')
    
    if(status==1):
        caption={'msg':"Please Verify Your Face"}
    elif(status==2):
        caption={'msg':"Please capture your Face"}
    elif(status==3):
        caption={'msg':"Face does not match Try again !"}
    elif(status==4):
        caption={'msg':"Please Make sure only single person is there in camera and your face is not hidden"}
    else:
        caption={'msg':''}


    return render(request,  'face_recog/capture_and_store.html',caption)
    


















#////////////////////////
def capture_face(request):
    
    import cv2    
    import face_recognition
    vid = cv2.VideoCapture(0)
    ret, frame = vid.read()
    image = Image.fromarray(frame,'RGB')
    
    user_photo = 'User'+str(request.user.id)+'.jpg'
    temporary_dir = os.path.join(BASE_DIR,'temp')
    user_image_dir = os.path.join(BASE_DIR,'UserImages')
    if os.path.isfile(os.path.join(user_image_dir,user_photo)):

        image.save(os.path.join(temporary_dir,user_photo))
        #comparison
        old_image = face_recognition.load_image_file(os.path.join(user_image_dir,user_photo))
        #face_encoding_array = face_recognition.face_encodings(old_image)

        new_image = face_recognition.load_image_file(os.path.join(temporary_dir,user_photo))
        #unknown_encoding = face_recognition.face_encodings(new_image)
        try:
            face_encoding_array = face_recognition.face_encodings(old_image)
            unknown_encoding = face_recognition.face_encodings(new_image)
            result = face_recognition.compare_faces(face_encoding_array,unknown_encoding[0])            
            print("number of face: in saved photo: ", len(face_encoding_array))
            print("number of face: in recently clicked photo: ", len(unknown_encoding))
            if result[0]:
                return redirect('home')
            else:
                
                return redirect('webcam',status=3)
        except Exception:
            
            return redirect('webcam',status=4)
        
    else:

        image.save(os.path.join(user_image_dir,user_photo))
        try:

            oi = face_recognition.load_image_file(os.path.join(user_image_dir,user_photo))
            face_encoding_array = face_recognition.face_encodings(oi)
            if len(face_encoding_array)>1:
                raise Exception
        except Exception:
            return redirect('webcam',status=4)

        return redirect('home')

    

