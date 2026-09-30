from django.contrib import admin

# Register your models here.

from .models import BlogPost, Comment, Test, Students

admin.site.register(BlogPost)
admin.site.register(Comment)

admin.site.register(Test)
admin.site.register(Students)


# admin.site.register(MyUser)



