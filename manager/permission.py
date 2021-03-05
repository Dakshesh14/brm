from django.shortcuts import render

def check_if_admin(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        else:
            return render(request,"extras/alert.html",{
                "alert":"Unauthorized",
                "message":"Seems like Unauthorized to add blogs yet please add a catchy About Me and you might be allowed to add blogs!",
            })
    
    return wrapper_function