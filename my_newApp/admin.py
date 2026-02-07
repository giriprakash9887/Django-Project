from django.contrib import admin

# Register your models here.

from .models import BlogPost,Profiles,Blog,Comment,Student,Course,BlogPermissionPost,Author,Book

admin.site.register(BlogPost)
admin.site.register(Profiles)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(BlogPermissionPost)

admin.site.register(Author)
admin.site.register(Book)


