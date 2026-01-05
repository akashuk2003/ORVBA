from django.shortcuts import redirect

def admin_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        # Check if user is authenticated AND (is_admin OR is_superuser)
        if request.user.is_authenticated and (request.user.is_admin or request.user.is_superuser):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('admin_login') # We will create this URL next
    return wrapper_func