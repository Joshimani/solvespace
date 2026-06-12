from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('profile_pic', 'username', 'bio', 'email')
    search_fields = ('username','email')
    list_filter = ('created_at',)