from django.contrib import admin
from .models import MyUser, Room
from .forms import UserChangeForm,  UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# class RoomInline(admin.TabularInline):
#     model = Room

# class MyUserAdmin(admin.ModelAdmin):
#     def change_view(self, request, object_id, form_url='', extra_context=None):
#         extra_context = extra_context or {}
#         extra_context['room'] = Room.objects.all

#         return super().change_view(request, object_id, form_url, extra_context=extra_context)

# admin.site.register(MyUser)
# admin.site.register(Room)

# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('fullname', 'position', 'room', 'email', 'role' )
    list_filter= ('is_admin',)
    fieldsets = (
        (None, {'fields' : ('email', 'password',)}),
        ('Personnal info', {'fields': ('fullname',)}),
        ('Permission', {'fields':('user_permissions','is_admin',)}),
    )

    add_fieldsets = (
        (
            None, {
            'classes' : ('wide',),
            'fields' : ('email', 'fullname', 'position', 'room', 'role','user_permissions', 'password1', 'password2',),
            },
        ),
    )
    search_fields = ('email', )
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(MyUser, UserAdmin)