from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models import CharField


# from django.contrib.gis.db import models as gis_models
# from django.contrib.postgres.fields import ArrayField

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('non_binary', 'Non-binary'),
        ('other', 'Other'),
    ]

    INTEREST_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('non_binary', 'Non-binary'),
        ('all', 'All'),
    ]

    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    interested_in = models.JSONField(default=list, blank=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    last_active = models.DateTimeField(auto_now=True)
    preferences = models.JSONField(default=dict, blank=True)

    # Override the related_name for groups and user_permissions to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='CustomUser_groups',  # Custom related name
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='CustomUser_permissions',  # Custom related name
        blank=True,
        help_text='Specific permissions for this user.'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Match(models.Model):
    user1 =models.ForeignKey(CustomUser, related_name='matches_as_user1', on_delete=models.CASCADE)
    user2 =models.ForeignKey(CustomUser, related_name='matches_as_user2', on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('user1','user2')

class Message(models.Model):
    sender =models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver =models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    attachment =models.FileField(upload_to='chat_attachments/',null=True, blank=True)
    timestamp =models.DateTimeField(auto_now_add=True)
    is_read =models.BooleanField(default=False)


class SwipeAction(models.Model):
    SWIPE_CHOICES =[
        ('like','Like'),
        ('dislike','Dislike'),
        ('super like','SuperLike'),
    ]

    swiper =models.ForeignKey(CustomUser, related_name='swipes', on_delete=models.CASCADE)
    swiped =models.ForeignKey(CustomUser, related_name='swiped', on_delete=models.CASCADE)
    action =models.CharField(max_length=10, choices=SWIPE_CHOICES)
    timestamp =models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('swiper','swiped')

class UserPreferences(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='detailed_preferences')
    age_min = models.IntegerField(default=18)
    age_max = models.IntegerField(default=70)
    distance_max=models.IntegerField(default=100)
    show_me_on_app =models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user}'s preferences"
