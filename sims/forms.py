from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MyStudentsForm(UserCreationForm):
    class Meta:
        model = MyStudents
        fields = ['email', 'username']
        
class MyStaffForm(UserCreationForm):
    class Meta:
        model = MyStaff
        fields = ['email', 'username']
        
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        
        
class PatientinfoForm(forms.ModelForm):
    Symptoms = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '1',
            'id': 'Symptoms',
            'placeholder' : 'Write Symptoms',
        }))
    
    Problem = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'Problem',
            'placeholder' : 'Write Problem',
        }))
    
    Treatment = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'Treatment',
            'placeholder' : 'Write Treatment',
        }))
    
    Medicine = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'Medicine',
            'placeholder' : 'Write Medicine',
        }))
    class Meta:
        model = Patientinfo
        fields = ('Symptoms', 'Problem', 'Treatment', 'Medicine',)
        
class ClinicsForm(forms.ModelForm):
    Clinics = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Clinics',
            'placeholder' : 'Write Chief Complain',
        }))
    class Meta:
        model = Clinics
        fields = ('Clinics',)
        
class HistoryForm(forms.ModelForm):
    History = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'History',
            'placeholder' : 'Write History of Present Illness',
        }))
    class Meta:
        model = History
        fields = ('History',)
        
class GeneralForm(forms.ModelForm):
    General = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'General',
            'placeholder' : 'Write General Health',
        }))
    class Meta:
        model = General
        fields = ('General',)
        
class FamilyForm(forms.ModelForm):
    Family = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Family',
            'placeholder' : 'Write Family History',
        }))
    class Meta:
        model = Family
        fields = ('Family',)
        
class ManagementForm(forms.ModelForm):
    Management = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Management',
            'placeholder' : 'Write Management',
        }))
    class Meta:
        model = Management
        fields = ('Management',)
        
class MedicationForm(forms.ModelForm):
    Medication = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Medication',
            'placeholder' : 'Write Medication',
        }))
    
    Comment = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Comment',
            'placeholder' : 'Write Comment',
        }))
    class Meta:
        model = Medication
        fields = ('Medication', 'Comment',)
        
class ODForm(forms.ModelForm):
    Sphereod = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Sphere',
            'placeholder' : 'Write Sphere',
        }))
    
    CYLod = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'CYL',
            'placeholder' : 'Write CYL',
        }))
    
    Axisod = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Axis',
            'placeholder' : 'Write Axis',
        }))
    
    VAod = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'VA',
            'placeholder' : 'Write VA',
        }))
    
    Commentod = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Comment',
            'placeholder' : 'Write Comment',
        }))
    class Meta:
        model = OD
        fields = ('Sphereod', 'CYLod', 'Axisod', 'VAod', 'Commentod',)
        
class OSForm(forms.ModelForm):
    Sphereos = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Sphere',
            'placeholder' : 'Write Sphere',
        }))
    
    CYLos = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'CYL',
            'placeholder' : 'Write CYL',
        }))
    
    Axisos = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Axis',
            'placeholder' : 'Write Axis',
        }))
    
    VAos = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'VA',
            'placeholder' : 'Write VA',
        }))
    
    Commentos = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Comment',
            'placeholder' : 'Write Comment',
        }))
    class Meta:
        model = OS
        fields = ('Sphereos', 'CYLos', 'Axisos', 'VAos', 'Commentos',)
        
class DiagnosisForm(forms.ModelForm):
    Diagnosis = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Diagnosis',
            'placeholder' : 'Write Diagnosis',
        }))
    class Meta:
        model = Diagnosis
        fields = ('Diagnosis',)
        
class InvestigationForm(forms.ModelForm):
    Investigation = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Investigation',
            'placeholder' : 'Write Investigation',
        }))
    class Meta:
        model = Investigation
        fields = ('Investigation',)
        
class REForm(forms.ModelForm):
    RE = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'RE',
            'placeholder' : 'Write R.E',
        }))
    PHR = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'PH',
            'placeholder' : 'Write P.H',
        }))
    class Meta:
        model = RE
        fields = ('RE', 'PHR',)
        
class LEForm(forms.ModelForm):
    LE = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'LE',
            'placeholder' : 'Write L.E',
        }))
    PHL = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'PH',
            'placeholder' : 'Write P.H',
        }))
    class Meta:
        model = LE
        fields = ('LE', 'PHL',)
        
class VisualForm(forms.ModelForm):
    Visual = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'Visual',
            'placeholder' : 'Write Visual acuit with glasses',
        }))
    class Meta:
        model = Visual
        fields = ('Visual',)
        
class IOPAForm(forms.ModelForm):
    REIOPA = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'IOPA',
            'placeholder' : 'Write R.E',
        }))
    
    LEIOPA = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'IOPB',
            'placeholder' : 'Write L.E',
        }))
    class Meta:
        model = IOPA
        fields = ('REIOPA', 'LEIOPA',)
        
class IOPBForm(forms.ModelForm):
    REIOPB = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'IOPB',
            'placeholder' : 'Write R.E in mmHg',
        }))
    
    LEIOPB = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'IOPB',
            'placeholder' : 'Write L.E in mmHg',
        }))
    class Meta:
        model = IOPB
        fields = ('REIOPB', 'LEIOPB',)
        
class EYELIDRForm(forms.ModelForm):
    StatusEYELIDR = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'EYELIDR',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = EYELIDR
        fields = ('StatusEYELIDR',)
        
class EYELIDLForm(forms.ModelForm):
    StatusEYELIDL = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'EYELIDL',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = EYELIDL
        fields = ('StatusEYELIDL',)
        
class CONJUNCTIVARForm(forms.ModelForm):
    StatusCONJUNCTIVAR = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'CONJUNCTIVAR',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = CONJUNCTIVAR
        fields = ('StatusCONJUNCTIVAR',)
        
class CONJUNCTIVALForm(forms.ModelForm):
    StatusCONJUNCTIVAL = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'CONJUNCTIVAL',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = CONJUNCTIVAL
        fields = ('StatusCONJUNCTIVAL',)
        
class CORNEARForm(forms.ModelForm):
    StatusCORNEAR = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'CORNEAR',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = CORNEAR
        fields = ('StatusCORNEAR',)
        
class CORNEALForm(forms.ModelForm):
    StatusCORNEAL = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'CORNEAL',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = CORNEAL
        fields = ('StatusCORNEAL',)
        
class ACRForm(forms.ModelForm):
    StatusACR = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'ACR',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = ACR
        fields = ('StatusACR',)
        
class ACLForm(forms.ModelForm):
    StatusACL = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'ACL',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = ACL
        fields = ('StatusACL',)
        
class PUPILRForm(forms.ModelForm):
    StatusPUPILR = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'PUPILR',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = PUPILR
        fields = ('StatusPUPILR',)
        
class PUPILLForm(forms.ModelForm):
    StatusPUPILL = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'PUPILL',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = PUPILL
        fields = ('StatusPUPILL',)
        
class IRISRForm(forms.ModelForm):
    StatusIRISR = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'IRISR',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = IRISR
        fields = ('StatusIRISR',)
        
class IRISLForm(forms.ModelForm):
    StatusIRISL = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'IRISL',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = IRISL
        fields = ('StatusIRISL',)
        
class LENSRForm(forms.ModelForm):
    StatusLENSR = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'LENSR',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = LENSR
        fields = ('StatusLENSR',)
        
class LENSLForm(forms.ModelForm):
    StatusLENSL = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'LENSL',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = LENSL
        fields = ('StatusLENSL',)
        
class VITREOUSRForm(forms.ModelForm):
    StatusVITREOUSR = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'VITREOUSR',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = VITREOUSR
        fields = ('StatusVITREOUSR',)
        
class VITREOUSLForm(forms.ModelForm):
    StatusVITREOUSL = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'VITREOUSL',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = VITREOUSL
        fields = ('StatusVITREOUSL',)
        
class RETINARForm(forms.ModelForm):
    StatusRETINAR = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'RETINAR',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = RETINAR
        fields = ('StatusRETINAR',)
        
class RETINALForm(forms.ModelForm):
    StatusRETINAL = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '3',
            'id': 'RETINAL',
            'placeholder' : 'Normal or Abnormal',
        }))
    class Meta:
        model = RETINAL
        fields = ('StatusRETINAL',)

        
class StaffContactinfoForm(ModelForm):
    class Meta:
        model = StaffContactinfo
        fields = '__all__'
