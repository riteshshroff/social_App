from django.shortcuts import render, redirect
from social_app.models import Users, Post, Friends
from django.db.models import Q

import datetime

# Create your views here.
def home(request):
    if request.session:     
        mobile = request.session.get('mobile', False)    
        try:
            ssn = Users.objects.get(mobile=mobile)
            name = ssn.fname + ' ' +  ssn.lname        
            post = Post.objects.all().order_by('-id')                           
            context = {
                'name':name,
                'post':post,
                'ssn':ssn,               
            }
            return render(request, 'social_home.html', context)                            
        except:
            return render(request, 'home.html', {'msg':'Your session is expired.'})    
    else:
        return render(request, 'home.html', {'msg':'Your session is expired.'})

def social_home(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        if mobile and password:
            try:
                usr = Users.objects.get(mobile=mobile)
                pwd = usr.password
                email = usr.email
                if pwd:
                    request.session['mobile'] = mobile
                    request.session['email'] = email
                    return redirect('/')
                else:
                    return render(request, 'home.html', {'msg':'Your password is incorrect.'})    
            except:
                return render(request, 'home.html', {'msg':'Mobile number does not exist.'})
        else:
            return render(request, 'home.html', {'msg':'Both field is required.'})
    else:
        return render(request, 'home.html', {'msg':'Your method is not post.'})

def user_signup(request):
    return render(request, 'signup.html')

def save_users(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        if fname and lname and email and mobile and password:
            try:                
                rp_email = Users.objects.get(email=email)
                rp_mobile = rp_email.mobile
                if rp_mobile:
                    context = {
                        'fname':fname,
                        'lname':lname,
                        'email':email,
                        'mobile':mobile,
                        'msg':'This Mobile number is already exist.'
                    }
                    return render(request, 'home.html', context)                
                context = {
                    'fname':fname,
                    'lname':lname,
                    'email':email,
                    'mobile':mobile,
                    'msg':'This email id is already exist.'
                }
                return render(request, 'home.html', context)
            except:
                Users(fname=fname, lname=lname, email=email, mobile=mobile, 
                password=password, profile_image=None, background_image=None).save()
                return render(request, 'home.html', {'msg':'Please login with credentials.'})
        else:
            context = {'msg':'All field is required.'}
            return render(request, 'home.html', context)
    else:
        return render(request, 'SocialHome.html', {'msg':'Your method is not post.'})

def save_post(request):
    if request.method == 'POST':    
        if request.session:
            title = request.POST.get('title')
            editor1 = request.POST.get('editor1')
            sns = request.session['mobile']
            try:                
                user = Users.objects.get(mobile=sns)               
                Post(title=title, posts=editor1, user=user).save()            
                return redirect('/')
            except:
                return redirect('/')
        else:
            return render(request, 'home.html', {'msg':'Your session is expired.'})
    else:
        return render(request, 'home.html', {'msg':'Your method is not post.'})
    
def logout(request):
    request.session.flush()
    return redirect('/')

def users_profile(request):    
    if request.session:           
        mobile = request.session.get('mobile')                
        ssn = Users.objects.get(mobile=mobile)
        name = ssn.fname + ' ' +  ssn.lname                    
        context = {
            'name':name,      
            'ssn':ssn,
        }
        return render(request, 'user_profile.html', context)                    
    else:
        return render(request, 'home.html', {'msg':'Your session is expired.'})

def update_user_profile(request):
    if request.method == 'POST':
        if request.session:    
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')            
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            ids = request.POST.get('ids')
            address = request.POST.get('address')
            country = request.POST.get('country')
            relationship = request.POST.get('relationship')
            profile_image = request.FILES.get('profile_image')
            background_image = request.FILES.get('background_image')
            current_date = datetime.datetime.now()
            if not address:
                address = None
            if not country:
                country = None
            if not relationship:
                relationship = None
            if profile_image is None:
                profile_image = None
            if background_image is None:
                background_image = None
            usr = Users.objects.get(id=ids)            
            password = usr.password            
            Users( password=password,id=ids,fname=fname,lname=lname,email=email,mobile=mobile,address=address,country=country,
            relationship=relationship, profile_image=profile_image, background_image=background_image,
            created_at=current_date).save()            
            return redirect('/users-profile/')
        else:
            return render(request, 'home.html', {'msg':'Your session is expired.'})
    else:
        return render(request, 'home.html', {'msg':'Method is not post.'})

def add_friend(request):
    if request.session:
        ids = request.GET.get('ids')
        usr = Users.objects.get(id=ids)
        ssn = request.session.get('mobile')                                                     
        user = Users.objects.get(mobile=ssn)
        user_id = user.id               
        name = user.fname + ' ' +  user.lname
        post = Post.objects.all().order_by('-id')
        if str(ids) == str(user_id):         
            context = {
                'name':name,
                'post':post,
                'ssn':user,
                'msg':'Choose another name to add as friend.'
            }       
            return render(request, 'social_home.html', context)                                            
        already_friend = Friends.objects.filter(Q(friend=ids) & Q(user=user))         
        if already_friend:                                                        
            context = {
                'name':name,
                'post':post,
                'ssn':user,
                'msg':'Already exist in your friend list.'
            }
            return render(request, 'social_home.html', context)                 
        else:
            Friends(friend=usr, user=user).save()
            context = {
                'name':name,
                'post':post,
                'ssn':user,
                'msg':'Add successfully.'
            }
            return render(request, 'social_home.html', context) 
    else:
        return render(request, 'home.html', {'msg':'Your session is expired.'})

def user_connections(request):
    if request.session:
        ssn = request.session.get('mobile', False)        
        user = Users.objects.get(mobile=ssn)
        ids = user.id    
        friend_list = Friends.objects.filter(user=user) 
        name = user.fname + ' ' +  user.lname
        if friend_list:               
            context = {
                'flist':friend_list,
                'name':name,
                'ssn':user,
            }
            return render(request, 'user_connections.html', context)
        else:
            context = {                
                    'name':name,
                    'ssn':user,                    
                }
            return render(request, 'user_connections.html', context)
    else:
        return render(request, 'home.html', {'msg':'Your session is expired.'})

def mutual_connections(request):
    if request.session:
        ssn = request.session.get('mobile', False)        
        user = Users.objects.get(mobile=ssn)
        name = user.fname + ' ' +  user.lname
        friend_list = Friends.objects.filter(user=user)
        if friend_list:
            for x in friend_list:           
                frnd = Friends.objects.filter(user__fname=x)              
                context = {
                    'flist':frnd,
                    'name':name,
                    'ssn':user,
                }  
                return render(request, 'mutual_connections.html', context)  
        else:
            context = {                
                'name':name,
                'ssn':user,
            }  
            return render(request, 'mutual_connections.html', context) 
    else:
        return render(request, 'home.html', {'msg':'Your session is expired.'})

def view_connection_details(request):
    if request.session:
        ssn = request.session.get('mobile', False)        
        user = Users.objects.get(mobile=ssn)
        name = user.fname + ' ' +  user.lname
        ids = request.GET.get('ids')
        if ids:
            user_id = Users.objects.get(id=ids)
            context = {
                'ssn':user,
                'name':name,
                'details':user_id,
            }
            return render(request, 'user_connection_details.html', context)
        else:
            return redirect('/user-connections/')
    else:
        return render(request, 'home.html', {'msg':'Your session is expired.'})

def view_mutual_connections_details(request):
    if request.session:
        ssn = request.session.get('mobile', False)        
        user = Users.objects.get(mobile=ssn)
        name = user.fname + ' ' +  user.lname
        ids = request.GET.get('ids')
        if ids:
            user_id = Users.objects.get(id=ids)
            context = {
                'ssn':user,
                'name':name,
                'details':user_id,
            }
            return render(request, 'mutual_connection_details.html', context)
        else:
            return redirect('/mutual-connections/')
    else:
        return render(request, 'home.html', {'msg':'Your session is expired.'})    

def search_connections(request):
    if request.session:
        search = request.POST.get('search')
        ssn = request.session.get('mobile', False)        
        user = Users.objects.get(mobile=ssn)
        name = user.fname + ' ' +  user.lname
        if search:
            flist = Users.objects.filter(Q(fname__icontains=search) | Q(lname__icontains=search) | Q(email__icontains=search) | Q(mobile__icontains=search))                                                
            if flist:                
                for x in flist:                                            
                    lis = Friends.objects.filter(Q(friend=x) & Q(user=user))
                    if lis:                    
                        context = {
                            'ssn':user,
                            'name':name,
                            'search':search,
                            'flist':flist,
                            'lis':lis,
                        }            
                        return render(request, 'social_home.html', context)
                    else:
                        context = {
                            'ssn':user,
                            'name':name,
                            'search':search,                                        
                        }            
                        return render(request, 'social_home.html', context)
            else:
                context = {
                    'ssn':user,
                    'name':name,
                    'search':search,                                        
                }            
                return render(request, 'social_home.html', context)
        else:
            return render(request, 'social_home.html', )        
    else:
        return render(request, 'home.html', {'msg':'Your session is expired.'})























