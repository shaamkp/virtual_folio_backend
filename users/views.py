# from django.shortcuts import render

# from users.models import Profile


# def index(request):
#     profile = Profile.objects.all()

#     context = {
#         "profile" : profile
#     }

#     return render(request, "index.html",context=context)




# def profile(request,pk):
#     profile = Profile.objects.get(pk=pk)[:2]
     
#     context={
#         "profile" : profile
#     }
    
#     return render(request, "index.html",context=context)

