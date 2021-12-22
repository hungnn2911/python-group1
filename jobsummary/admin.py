from django.contrib import admin
from .models import MyUser, Room



# class RoomInline(admin.TabularInline):
#     model = Room

# class MyUserAdmin(admin.ModelAdmin):
#     def change_view(self, request, object_id, form_url='', extra_context=None):
#         extra_context = extra_context or {}
#         extra_context['room'] = Room.objects.all

#         return super().change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(MyUser)
admin.site.register(Room)

# Register your models here.
