
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Match, Message, SwipeAction, UserPreferences

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Specify fields to display in the list view for CustomUser in admin
    list_display = ('username', 'email', 'gender', 'is_active', 'last_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('last_active',)

# Register other models
admin.site.register(Match)
admin.site.register(Message)
admin.site.register(SwipeAction)
admin.site.register(UserPreferences)
