from django.shortcuts import render
from frenin.forms import UserForm
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from freninhelper import freninhelper
from django.contrib.auth.decorators import login_required

# Create your views here.
def reggin(request):
    #context = RequestContext(request)
    user_form=UserForm()
    registered = False
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        user_form = UserForm(data=request.POST)
        
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        useru = authenticate(username=username, password=password)
        print 'auth usr'
        print useru
        print username,password#ln25

        #check if user exists
        if useru:
            userp = authenticate(username=username, password=password)
            print 'auth psw'
            # check if psw provided is correct for the user
            if userp:
                print 'user logged in'
                login(request,userp)
                #return HttpResponseRedirect('/frenin/')
                return HttpResponseRedirect('/frenin/')
            else:#psw was incorrect
                print "Invalid login details: {0}, {1}".format(username, password)
                return HttpResponse("Invalid login details supplied.")
        else:   #no user = register user
            #user_form = UserForm(data=request.POST)
            if user_form.is_valid() and freninhelper(username).is_valid:
                # Save the user's form data to the database.
                userr = user_form.save()
                userr.set_password(password)
                userr.save()
                registered=True
                userp = authenticate(username=username, password=password)
                login(request,userp)
                '''return render_to_response('rango/register.html',{'user_form': user_form,'registered': registered},context)'''
                return HttpResponseRedirect('/frenin/')

            else:
                print user_form.errors
                return HttpResponse("You typed something Invalid, my friend")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        context = user_form
        template = loader.get_template('frenin/reggin.html')
        return render(request,'frenin/reggin.html',{'user_form': user_form, 'registered': registered})
        #return HttpResponse(template.render(context))
        #return render_to_response('rango/reggin.html', {}, context)
        #return render(request, 'polls/reggin.html', context)

def status(request):
    if request.user.is_authenticated():
        return HttpResponse('You are logged in as '+request.user.username)
        
    else:
        return HttpResponse("You are not logged in.")

def check_matches(request):
    if request.user.is_authenticated():
        fr=freninhelper(request.user.username)
        fr.getMatches()
        fr.saveMatches(fr.mrow,'data.csv')
        return render(request,'frenin/index.html')
        
    else:
        return HttpResponse("You are not logged in.")
        #fre_id=freninhelper('Crides').getId()
    #return HttpResponse(fre_id)
'''
@login_required
def check_matches(request):
    return HttpResponse("Since you're logged in, you can see this text!")
'''

def d3view(request):
    #return HttpResponse("d3")
    return render(request,'frenin/index.html')

def regout(request):
    logout(request)
    return HttpResponseRedirect('/frenin/')

def home(request):
    if request.user.is_authenticated():
        #return HttpResponse('You are logged in as '+request.user.username)
        print "show regout"
        status=True
    else:
        #return HttpResponse("You are not logged in.")
        print "show reggin"
        status=False
    
    return render(request,'frenin/home.html',{'status':status})
