from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.contrib import messages
import uuid

from django.contrib.auth import get_user_model


# user table--------------------------------------------------------------------
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, username, first_name, password=None):
#         if not email:
#             raise ValueError("email is required")
#         if not username:
#             raise ValueError("Your user name is required")
#         if not first_name:
#             raise ValueError("Your First Name is required")
#         # if not last_name:
#         #     raise ValueError("Your Last Name is required")
#         # if not id:
#         #     raise ValueError("Your Middle Name is required")
        
        

#         user=self.model(
#             email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             # last_name=last_name,
#             # middle_name=middle_name,
#             # phone=phone,
#             # id=id,
#             # course=course,
            
            
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, email, username, password=None):
#         user=self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#             # first_name=first_name,
#             # last_name=last_name,

#         )
#         user.is_admin=True
#         user.is_staff=True
        
#         user.is_superuser=True
#         user.save(using=self._db)
#         return user





class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

class MyStudents(AbstractBaseUser):

    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    # first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="username", max_length=100, unique=True)
    # id=models.CharField(verbose_name="id", max_length=100, unique=True, primary_key=True)
    # last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class MyStaff(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    # first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="username", max_length=100, unique=True)
    # id=models.CharField(verbose_name="id", max_length=100, unique=False, primary_key=True)
    # last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
class Patient(models.Model):
    user_type = [
    ("NHIF", "NHIF"),
    ("Cash payment", "Cash payment"),
]
    sex = [
    ("Male", "Male"),
    ("Female", "Female"),
]

    Patient_Id = models.IntegerField(primary_key=True)
    # Patient_Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Sex = models.CharField(max_length=40, choices=sex)
    Place = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Payment = models.CharField(max_length=40, choices=user_type)
    Cost = models.CharField(max_length=100)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    def __str__(self):
        return str(self.Patient_Id)
    
class Patientinfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    Symptoms = models.TextField()
    Problem = models.TextField()
    Treatment = models.TextField()
    Medicine = models.TextField()

    def __str__(self):
        return self.user.username
    
   # history
class Clinics(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    Clinics = models.TextField()

    def __str__(self):
        return self.user.username
    
class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    History = models.TextField()

    def __str__(self):
        return self.user.username
    
class General(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    General = models.TextField()

    def __str__(self):
        return self.user.username
    
class Family(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    Family = models.TextField()

    def __str__(self):
        return self.user.username
    

    
class Management(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    Management = models.TextField()

    def __str__(self):
        return self.user.username
    
class Medication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    Medication = models.TextField()
    Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class Diagnosis(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    Diagnosis = models.TextField()

    def __str__(self):
        return self.user.username
    
class OD(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    Sphereod = models.TextField()
    CYLod = models.TextField()
    Axisod = models.TextField()
    VAod = models.TextField()
    Commentod = models.TextField()

    def __str__(self):
        return self.user.username
    
class OS(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    Sphereos = models.TextField()
    CYLos = models.TextField()
    Axisos = models.TextField()
    VAos = models.TextField()
    Commentos = models.TextField()

    def __str__(self):
        return self.user.username
    
class Investigation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    Investigation = models.TextField()

    def __str__(self):
        return self.user.username
    
class RE(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    RE = models.TextField()
    PHR = models.TextField()

    def __str__(self):
        return self.user.username
    
class LE(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    LE = models.TextField()
    PHL = models.TextField()

    def __str__(self):
        return self.user.username
    
class Visual(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    Visual = models.TextField()

    def __str__(self):
        return self.user.username
    
class IOPA(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    REIOPA = models.TextField()
    LEIOPA = models.TextField()

    def __str__(self):
        return self.user.username
    
class IOPB(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    REIOPB = models.TextField()
    LEIOPB = models.TextField()

    def __str__(self):
        return self.user.username
    
class EYELIDR(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusEYELIDR = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class EYELIDL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusEYELIDL = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class CONJUNCTIVAR(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusCONJUNCTIVAR = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class CONJUNCTIVAL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusCONJUNCTIVAL = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class CORNEAR(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusCORNEAR = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class CORNEAL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusCORNEAL = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class ACR(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusACR = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class ACL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusACL = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class PUPILR(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusPUPILR = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class PUPILL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusPUPILL = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class IRISR(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusIRISR = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class IRISL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusIRISL = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class LENSR(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusLENSR = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class LENSL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusLENSL = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class VITREOUSR(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusVITREOUSR = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class VITREOUSL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusVITREOUSL = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class RETINAR(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusRETINAR = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username
    
class RETINAL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Patient', on_delete=models.CASCADE)
    StatusRETINAL = models.TextField()
    # Comment = models.TextField()

    def __str__(self):
        return self.user.username

class StaffContactinfo(models.Model):
    region = [
    ("Arusha", "Arusha"),
    ("Dodoma", "Dodoma"),
    ("Mwanza", "Mwanza"),
    ("Iringa", "Iringa"),
    ("Tabora", "Tabora"),

    ("Mara", "Mara"),
    ("Kagera", "Kagera"),
    ("Simiyu", "Simiyu"),
    ("Shinyanga", "Shinyanga"),
    ("Geita", "Geita"),

    ("Kigoma", "Kigoma"),
    ("Tabora", "Tabora"),
    ("Manyara", "Manyara"),
    ("Kilimanjaro", "Kilimanjaro"),
    ("Katavi", "Katavi"),

    ("Singida", "Singida"),
    ("Tanga", "Tanga"),
    ("Morogoro", "Morogoro"),
    ("Pwani", "Pwani"),
    ("Rukwa", "Rukwa"),

    ("Mbeya", "Mbeya"),
    ("Songwe", "Songwe"),
    ("Njombe", "Njombe"),
    ("Ruvuma", "Ruvuma"),
    ("Mtwara", "Mtwara"),

    ("Lindi", "Lindi"),
    ("Songwe", "Songwe"),

]
    user_type = [
    ("Doctor", "Doctor"),
    ("Nurse", "Nurse"),
]
    professional = [
    ("Eye", "Eye"),
    ("Teeth", "Teeth"),
    ("Other", "Other"),
]
    level = [
    ("Certificate", "Certificate"),
    ("Diploma", "Diploma"),
    ("Bachelor", "Bachelor"),
    ("Master", "Master"),
    ("Phd", "Phd"),
    ("Other", "Other"),
]
    
    sex = [
    ("Male", "Male"),
    ("Female", "Female"),
]

    user = models.ForeignKey(MyStaff, on_delete=models.CASCADE)
    User_type = models.CharField(max_length=40, choices=user_type)
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Sex = models.CharField(max_length=40, choices=sex)
    Level_Of_Education = models.CharField(max_length=40, choices=level)
    Professional = models.CharField(max_length=40, choices=professional)
    Region = models.CharField(max_length=40, choices=region)
    Phone = models.CharField(max_length=100)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
