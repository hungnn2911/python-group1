from django.db import models


# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class Room(models.Model):

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Notification(models.Model):

    recieve = models.ForeignKey("MyUser",on_delete=models.PROTECT, null=True) 
    message = models.TextField()

class Jobsummary(models.Model):
    description = models.TextField()
    document = models.CharField(max_length=255)
    room = models.ForeignKey("Room", on_delete=models.PROTECT, null=True)

    deadline_plan = models.DateField()
    deadline = models.DateField()

    STATUSES = [(0, "Pending"), (1, "Assigned"), (2, "Finished")]
    status = models.SmallIntegerField(choices=STATUSES, null=True)
    user = models.ForeignKey("MyUser", on_delete=models.PROTECT, null=True)

    SUMMARY_TYPES=[(0, "KLGBcuochop "), (1, "KLGBvanhanh"), (2,"KLGB_DTXD_SCL"), (3, "KLGBKhac")]
    type_summary= models.IntegerField(choices=SUMMARY_TYPES, null=True)

    upload_file = models.FileField(upload_to='uploads/', null=True)

    assign = models.SmallIntegerField(null=True, blank=True)
    
    class Meta:
        permissions = (("can_assign_job", "Can assign job"), ("can_receive_job", "Can receive Job"), )

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


    

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class MyUser(AbstractBaseUser, PermissionsMixin):
  
    position = models.CharField(max_length=255)

    ROLES = [(0, "Admin"), (1, "Secretary"), (2, "Manager"), (3, "Staff")]
   
    role = models.IntegerField(choices=ROLES, null=True)

    room = models.ForeignKey("Room", on_delete=models.CASCADE, null=True)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    
    fullname = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    # def display_room(self):
    #     return ', '.join(genre.name for genre in self.genre.all()[:3])

    # display_genre.short_description = 'Genre'

