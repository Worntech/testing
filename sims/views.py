from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, auth
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.conf import settings

from web.views import *

from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.contrib.auth import get_user_model

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.db.models import Sum
from django.shortcuts import get_list_or_404

# FOR PRINTING TABLE
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.text import slugify
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from openpyxl import Workbook
from .models import Patient
from .models import StaffContactinfo


# Create your views here.
# @login_required(login_url='signin')
def admin(request):
    return render(request, 'sims/admin.html')
@login_required(login_url='signinsims')
def addstudents(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # id = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyStaff.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('addstudents')
            elif MyStaff.objects.filter(username=username).exists():
                messages.info(request, f"Id Number {username} Already Taken")
                return redirect('addstudents')
            else:
                user = MyStaff.objects.create_user(username=username, email=email, password=password)
                user.save()
                # messages.info(request, 'Registered Student Succesefull.')
                return redirect('addPatient')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('addstudents')

    else:
        return render(request, 'sims/addstudents.html')
    
# @login_required(login_url='signinsims')
def addstaff(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        # id = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyStaff.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('addstaff')
            elif MyStaff.objects.filter(username=username).exists():
                messages.info(request, f"Id Number {username} Already Taken")
                return redirect('addstaff')
            else:
                user = MyStaff.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'Registered Staff Succesefull.')
                return redirect('addstaffcontactinfo')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('addstaff')

    else:
        return render(request, 'sims/addstaff.html')


def signinsims(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.info(request, 'Loged in succesefull.')
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('signinsims')

    else:
        return render(request, 'sims/signinsims.html')

@login_required(login_url='signinsims')
def logout(request):
    auth.logout(request)
    messages.info(request, 'Loged out succesefull.')
    return redirect('signinsims')

@login_required(login_url='signinsims')
def news(request):
    return render(request, 'sims/news.html')

@login_required(login_url='signinsims')
def dashboard(request):
    countpatient= Patient.objects.all().count()
    count_nhif_patients = Patient.objects.filter(Payment='NHIF').count()
    count_cash_patients = Patient.objects.filter(Payment='Cash payment').count()
    countstaff= StaffContactinfo.objects.all().count()
    context={
        "countpatient":countpatient,
        "countstaff":countstaff,
        "count_nhif_patients":count_nhif_patients,
        "count_cash_patients":count_cash_patients,
    }
    return render(request, 'sims/dashboard.html', context)

# def base(request):
#     # Assuming 'username' is the attribute in MyStaff that corresponds to the user's username
#     logged_in_user = MyStaff.objects.get(username=request.user.username)

#     # Fetching CA results related to the logged-in user using the obtained 'logged_in_user' instance
#     profilename = Patient.objects.filter(Ca_Number__user=logged_in_user)
    
#     context={
#         "profilename":profilename,
#         # "countstaff":countstaff
#     }
#     return render(request, 'sims/base.html', context)

@login_required(login_url='signinsims')
def base(request):
    # Assuming 'username' is the attribute in MyStaff that corresponds to the user's username
    logged_in_user = MyStaff.objects.get(username=request.user.username)

    # Fetching related Patient for the logged-in user
    student_contact_info = Patient.objects.filter(user=logged_in_user).first()

    if student_contact_info:
        # Accessing first name and last name from Patient
        first_name = student_contact_info.First_Name
        last_name = student_contact_info.Last_Name

        return render(request, 'sims/base.html', {'first_name': first_name, 'last_name': last_name})
    else:
        # Handle scenario where there's no related Patient
        return render(request, 'sims/base.html')  


@login_required(login_url='signinsims')
def patient(request):
    patient = Patient.objects.all().order_by("-pk")
    context={
        "patient":patient
    }
    return render(request, 'sims/patient.html', context)



class viewpatient(DetailView):
    model = Patient
    template_name = 'sims/viewpatient.html'
    # count_hit = True
    # HII NI CODES KWA AJILI YA POST DETAIL PAGE KWA KUTUMIA CLASS VIEW ZINAISHIA HAPA

#SASA HIZI ZINAZOANZIA HAPA NI KWA AJILI YA COMMENT KWENYE POST HUSIKA
    form = PatientinfoForm

    def post(self, request, *args, **kwargs):
        form = PatientinfoForm(request.POST)
        if form.is_valid():
            Title = self.get_object()
            form.instance.user = request.user
            form.instance.Title = Title
            form.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        #kwa ajili ya kudisplay comment huo mstari wa chini
        post_comments = Patientinfo.objects.all().filter(Title=self.object.pk)
        
        #zinaendelea za kupost comment kwa admin
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'form':self.form,
                'post_comments':post_comments,
                # 'post_comments_count':post_comments_count,
            })
        return context
    
    
    # FOR CLINIC 
    formclinic = ClinicsForm

    def post(self, request, *args, **kwargs):
        formclinic = ClinicsForm(request.POST)
        if formclinic.is_valid():
            Title = self.get_object()
            formclinic.instance.user = request.user
            formclinic.instance.Title = Title
            formclinic.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = Clinics.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formclinic':self.formclinic,
                'post_comments':post_comments,
            })
        return context
    
    # FOR HISTORY 
    formhistory = HistoryForm

    def post(self, request, *args, **kwargs):
        formhistory = HistoryForm(request.POST)
        if formhistory.is_valid():
            Title = self.get_object()
            formhistory.instance.user = request.user
            formhistory.instance.Title = Title
            formhistory.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = History.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formhistory':self.formhistory,
                'post_comments':post_comments,
            })
        return context
    
    # FOR GENERAL 
    formgeneral = GeneralForm

    def post(self, request, *args, **kwargs):
        formgeneral = GeneralForm(request.POST)
        if formgeneral.is_valid():
            Title = self.get_object()
            formgeneral.instance.user = request.user
            formgeneral.instance.Title = Title
            formgeneral.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = General.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formgeneral':self.formgeneral,
                'post_comments':post_comments,
            })
        return context
    
    
    
    # FOR MANAGEMENT 
    formmanagement = ManagementForm

    def post(self, request, *args, **kwargs):
        formmanagement = ManagementForm(request.POST)
        if formmanagement.is_valid():
            Title = self.get_object()
            formmanagement.instance.user = request.user
            formmanagement.instance.Title = Title
            formmanagement.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = Management.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formmanagement':self.formmanagement,
                'post_comments':post_comments,
            })
        return context
    
    # FOR MEDICATION 
    formmedication = MedicationForm

    def post(self, request, *args, **kwargs):
        formmedication = MedicationForm(request.POST)
        if formmedication.is_valid():
            Title = self.get_object()
            formmedication.instance.user = request.user
            formmedication.instance.Title = Title
            formmedication.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = Medication.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formmedication':self.formmedication,
                'post_comments':post_comments,
            })
        return context
    
    # FOR DIAGNOSIS 
    formdiagnosis = DiagnosisForm

    def post(self, request, *args, **kwargs):
        formdiagnosis = DiagnosisForm(request.POST)
        if formdiagnosis.is_valid():
            Title = self.get_object()
            formdiagnosis.instance.user = request.user
            formdiagnosis.instance.Title = Title
            formdiagnosis.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = Diagnosis.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formdiagnosis':self.formdiagnosis,
                'post_comments':post_comments,
            })
        return context
    
# FOR OD 
    formod = ODForm

    def post(self, request, *args, **kwargs):
        formod = ODForm(request.POST)
        if formod.is_valid():
            Title = self.get_object()
            formod.instance.user = request.user
            formod.instance.Title = Title
            formod.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = OD.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formod':self.formod,
                'post_comments':post_comments,
            })
        return context
    
# FOR OS 
    formos = OSForm

    def post(self, request, *args, **kwargs):
        formos = OSForm(request.POST)
        if formos.is_valid():
            Title = self.get_object()
            formos.instance.user = request.user
            formos.instance.Title = Title
            formos.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = OS.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formos':self.formos,
                'post_comments':post_comments,
            })
        return context
    
    # FOR INVESTIGATION 
    forminvestigation = InvestigationForm

    def post(self, request, *args, **kwargs):
        forminvestigation = InvestigationForm(request.POST)
        if forminvestigation.is_valid():
            Title = self.get_object()
            forminvestigation.instance.user = request.user
            forminvestigation.instance.Title = Title
            forminvestigation.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = Investigation.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'forminvestigation':self.forminvestigation,
                'post_comments':post_comments,
            })
        return context
    
    # FOR RE 
    formre = REForm

    def post(self, request, *args, **kwargs):
        formre = REForm(request.POST)
        if formre.is_valid():
            Title = self.get_object()
            formre.instance.user = request.user
            formre.instance.Title = Title
            formre.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = RE.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formre':self.formre,
                'post_comments':post_comments,
            })
        return context
    
    # FOR LE 
    formle = LEForm

    def post(self, request, *args, **kwargs):
        formle = LEForm(request.POST)
        if formle.is_valid():
            Title = self.get_object()
            formle.instance.user = request.user
            formle.instance.Title = Title
            formle.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = LE.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formle':self.formle,
                'post_comments':post_comments,
            })
        return context
    
# FOR VISUAL 
    formvisual = VisualForm

    def post(self, request, *args, **kwargs):
        formvisual = VisualForm(request.POST)
        if formvisual.is_valid():
            Title = self.get_object()
            formvisual.instance.user = request.user
            formvisual.instance.Title = Title
            formvisual.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = Visual.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formvisual':self.formvisual,
                'post_comments':post_comments,
            })
        return context
    
    # FOR IOPA 
    formiopa = IOPAForm

    def post(self, request, *args, **kwargs):
        formiopa = IOPAForm(request.POST)
        if formiopa.is_valid():
            Title = self.get_object()
            formiopa.instance.user = request.user
            formiopa.instance.Title = Title
            formiopa.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = IOPA.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formiopa':self.formiopa,
                'post_comments':post_comments,
            })
        return context
    
    # FOR IOPB
    formiopb = IOPBForm

    def post(self, request, *args, **kwargs):
        formiopb = IOPBForm(request.POST)
        if formiopb.is_valid():
            Title = self.get_object()
            formiopb.instance.user = request.user
            formiopb.instance.Title = Title
            formiopb.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = IOPB.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formiopb':self.formiopb,
                'post_comments':post_comments,
            })
        return context
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # FOR EYELIDR
    formeyelidr = EYELIDRForm

    def post(self, request, *args, **kwargs):
        formeyelidr = EYELIDRForm(request.POST)
        if formeyelidr.is_valid():
            Title = self.get_object()
            formeyelidr.instance.user = request.user
            formeyelidr.instance.Title = Title
            formeyelidr.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = EYELIDR.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formeyelidr':self.formeyelidr,
                'post_comments':post_comments,
            })
        return context
    
# FOR EYELIDL
    formeyelidl =EYELIDLForm

    def post(self, request, *args, **kwargs):
        formeyelidl = EYELIDLForm(request.POST)
        if formeyelidl.is_valid():
            Title = self.get_object()
            formeyelidl.instance.user = request.user
            formeyelidl.instance.Title = Title
            formeyelidl.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = EYELIDL.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formeyelidl':self.formeyelidl,
                'post_comments':post_comments,
            })
        return context
    
# FOR CONJUNCTIVAR
    formconjuctivar = CONJUNCTIVARForm

    def post(self, request, *args, **kwargs):
        formconjuctivar = CONJUNCTIVARForm(request.POST)
        if formconjuctivar.is_valid():
            Title = self.get_object()
            formconjuctivar.instance.user = request.user
            formconjuctivar.instance.Title = Title
            formconjuctivar.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = CONJUNCTIVAR.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formconjuctivar':self.formconjuctivar,
                'post_comments':post_comments,
            })
        return context
    
# FOR CONJUNCTIVAL
    formconjuctival = CONJUNCTIVALForm

    def post(self, request, *args, **kwargs):
        formconjuctival = CONJUNCTIVALForm(request.POST)
        if formconjuctival.is_valid():
            Title = self.get_object()
            formconjuctival.instance.user = request.user
            formconjuctival.instance.Title = Title
            formconjuctival.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = CONJUNCTIVAL.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formconjuctival':self.formconjuctival,
                'post_comments':post_comments,
            })
        return context
    
# FOR CORNEAR
    formcornear = CORNEARForm

    def post(self, request, *args, **kwargs):
        formcornear = CORNEARForm(request.POST)
        if formcornear.is_valid():
            Title = self.get_object()
            formcornear.instance.user = request.user
            formcornear.instance.Title = Title
            formcornear.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = CORNEAR.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formcornear':self.formcornear,
                'post_comments':post_comments,
            })
        return context
    
    # FOR CORNEAL
    formcorneal = CORNEALForm

    def post(self, request, *args, **kwargs):
        formcorneal = CORNEALForm(request.POST)
        if formcorneal.is_valid():
            Title = self.get_object()
            formcorneal.instance.user = request.user
            formcorneal.instance.Title = Title
            formcorneal.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = CORNEAL.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formcorneal':self.formcorneal,
                'post_comments':post_comments,
            })
        return context
    
    # FOR ACR
    formacr = ACRForm

    def post(self, request, *args, **kwargs):
        formacr = ACRForm(request.POST)
        if formacr.is_valid():
            Title = self.get_object()
            formacr.instance.user = request.user
            formacr.instance.Title = Title
            formacr.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = ACR.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formacr':self.formacr,
                'post_comments':post_comments,
            })
        return context
    
    # FOR ACL
    formacl = ACLForm

    def post(self, request, *args, **kwargs):
        formacl = ACLForm(request.POST)
        if formacl.is_valid():
            Title = self.get_object()
            formacl.instance.user = request.user
            formacl.instance.Title = Title
            formacl.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = ACL.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formacl':self.formacl,
                'post_comments':post_comments,
            })
        return context
    
    # FOR ACL
    formacl = ACLForm

    def post(self, request, *args, **kwargs):
        formacl = ACLForm(request.POST)
        if formacl.is_valid():
            Title = self.get_object()
            formacl.instance.user = request.user
            formacl.instance.Title = Title
            formacl.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = ACL.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formacl':self.formacl,
                'post_comments':post_comments,
            })
        return context
    
    # FOR PUPILR
    formpupilr = PUPILRForm

    def post(self, request, *args, **kwargs):
        formpupilr = PUPILRForm(request.POST)
        if formpupilr.is_valid():
            Title = self.get_object()
            formpupilr.instance.user = request.user
            formpupilr.instance.Title = Title
            formpupilr.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = PUPILR.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formpupilr':self.formpupilr,
                'post_comments':post_comments,
            })
        return context
    
    # FOR PUPILL
    formpupill = PUPILLForm

    def post(self, request, *args, **kwargs):
        formpupill = PUPILLForm(request.POST)
        if formpupill.is_valid():
            Title = self.get_object()
            formpupill.instance.user = request.user
            formpupill.instance.Title = Title
            formpupill.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = PUPILL.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formpupill':self.formpupill,
                'post_comments':post_comments,
            })
        return context
    
    # FOR IRISR
    formirisr = IRISRForm

    def post(self, request, *args, **kwargs):
        formirisr = IRISRForm(request.POST)
        if formirisr.is_valid():
            Title = self.get_object()
            formirisr.instance.user = request.user
            formirisr.instance.Title = Title
            formirisr.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = IRISR.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formirisr':self.formirisr,
                'post_comments':post_comments,
            })
        return context
    
    # FOR IRISL
    formirisl = IRISLForm

    def post(self, request, *args, **kwargs):
        formirisl = IRISLForm(request.POST)
        if formirisl.is_valid():
            Title = self.get_object()
            formirisl.instance.user = request.user
            formirisl.instance.Title = Title
            formirisl.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = IRISL.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formirisl':self.formirisl,
                'post_comments':post_comments,
            })
        return context
    
    # FOR LENSR
    formlensr = LENSRForm

    def post(self, request, *args, **kwargs):
        formlensr = LENSRForm(request.POST)
        if formlensr.is_valid():
            Title = self.get_object()
            formlensr.instance.user = request.user
            formlensr.instance.Title = Title
            formlensr.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = LENSR.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formlensr':self.formlensr,
                'post_comments':post_comments,
            })
        return context
    
    # FOR LENSL
    formlensl = LENSLForm

    def post(self, request, *args, **kwargs):
        formlensl = LENSLForm(request.POST)
        if formlensl.is_valid():
            Title = self.get_object()
            formlensl.instance.user = request.user
            formlensl.instance.Title = Title
            formlensl.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = LENSL.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formlensl':self.formlensl,
                'post_comments':post_comments,
            })
        return context
    
    # FOR VITREOUSR
    formvitreousr = VITREOUSRForm

    def post(self, request, *args, **kwargs):
        formvitreousr = VITREOUSRForm(request.POST)
        if formvitreousr.is_valid():
            Title = self.get_object()
            formvitreousr.instance.user = request.user
            formvitreousr.instance.Title = Title
            formvitreousr.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = VITREOUSR.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formvitreousr':self.formvitreousr,
                'post_comments':post_comments,
            })
        return context
    
    # FOR VITREOUSL
    formvitreousl = VITREOUSLForm

    def post(self, request, *args, **kwargs):
        formvitreousl = VITREOUSLForm(request.POST)
        if formvitreousl.is_valid():
            Title = self.get_object()
            formvitreousl.instance.user = request.user
            formvitreousl.instance.Title = Title
            formvitreousl.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = VITREOUSL.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formvitreousl':self.formvitreousl,
                'post_comments':post_comments,
            })
        return context
    
    # FOR RETINAR
    formretinar = RETINARForm

    def post(self, request, *args, **kwargs):
        formretinar = RETINARForm(request.POST)
        if formretinar.is_valid():
            Title = self.get_object()
            formretinar.instance.user = request.user
            formretinar.instance.Title = Title
            formretinar.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = RETINAR.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formretinar':self.formretinar,
                'post_comments':post_comments,
            })
        return context
    
        # FOR RETINAL
    formretinal = RETINALForm

    def post(self, request, *args, **kwargs):
        formretinal = RETINALForm(request.POST)
        if formretinal.is_valid():
            Title = self.get_object()
            formretinal.instance.user = request.user
            formretinal.instance.Title = Title
            formretinal.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_comments = RETINAL.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formretinal':self.formretinal,
                'post_comments':post_comments,
            })
        return context
    
    # FOR FAMILY 
    formfamily = FamilyForm

    def post(self, request, *args, **kwargs):
        formfamily = FamilyForm(request.POST)
        formclinic = ClinicsForm(request.POST)
        formhistory = HistoryForm(request.POST)
        formgeneral = GeneralForm(request.POST)
        formmanagement = ManagementForm(request.POST)
        formmedication = MedicationForm(request.POST)
        formdiagnosis = DiagnosisForm(request.POST)
        formod = ODForm(request.POST)
        formos = OSForm(request.POST)
        forminvestigation = InvestigationForm(request.POST)
        formre = REForm(request.POST)
        formle = LEForm(request.POST)
        formvisual = VisualForm(request.POST)
        formiopa = IOPAForm(request.POST)
        formiopb = IOPBForm(request.POST)
        
        
        formeyelidr = EYELIDRForm(request.POST)
        formeyelidl = EYELIDLForm(request.POST)
        formconjuctivar = CONJUNCTIVARForm(request.POST)
        formconjuctival = CONJUNCTIVALForm(request.POST)
        formcornear = CORNEARForm(request.POST)
        formcorneal = CORNEALForm(request.POST)
        formacr = ACRForm(request.POST)
        formacl = ACLForm(request.POST)
        formpupilr = PUPILRForm(request.POST)
        formpupill = PUPILLForm(request.POST)
        formirisr = IRISRForm(request.POST)
        formirisl = IRISLForm(request.POST)
        formlensr = LENSRForm(request.POST)
        formlensl = LENSLForm(request.POST)
        formvitreousr = VITREOUSRForm(request.POST)
        formvitreousl = VITREOUSLForm(request.POST)
        formretinar = RETINARForm(request.POST)
        formretinal = RETINALForm(request.POST)
        
        
        
        if formfamily.is_valid():
            Title = self.get_object()
            formfamily.instance.user = request.user
            formfamily.instance.Title = Title
            formfamily.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formmanagement.is_valid():
            Title = self.get_object()
            formmanagement.instance.user = request.user
            formmanagement.instance.Title = Title
            formmanagement.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formmedication.is_valid():
            Title = self.get_object()
            formmedication.instance.user = request.user
            formmedication.instance.Title = Title
            formmedication.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formdiagnosis.is_valid():
            Title = self.get_object()
            formdiagnosis.instance.user = request.user
            formdiagnosis.instance.Title = Title
            formdiagnosis.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formod.is_valid():
            Title = self.get_object()
            formod.instance.user = request.user
            formod.instance.Title = Title
            formod.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formos.is_valid():
            Title = self.get_object()
            formos.instance.user = request.user
            formos.instance.Title = Title
            formos.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if forminvestigation.is_valid():
            Title = self.get_object()
            forminvestigation.instance.user = request.user
            forminvestigation.instance.Title = Title
            forminvestigation.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formre.is_valid():
            Title = self.get_object()
            formre.instance.user = request.user
            formre.instance.Title = Title
            formre.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formle.is_valid():
            Title = self.get_object()
            formle.instance.user = request.user
            formle.instance.Title = Title
            formle.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formvisual.is_valid():
            Title = self.get_object()
            formvisual.instance.user = request.user
            formvisual.instance.Title = Title
            formvisual.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formiopa.is_valid():
            Title = self.get_object()
            formiopa.instance.user = request.user
            formiopa.instance.Title = Title
            formiopa.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formiopb.is_valid():
            Title = self.get_object()
            formiopb.instance.user = request.user
            formiopb.instance.Title = Title
            formiopb.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
            
            
            
            
            
            
            
            
            
            
        if formeyelidr.is_valid():
            Title = self.get_object()
            formeyelidr.instance.user = request.user
            formeyelidr.instance.Title = Title
            formeyelidr.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formeyelidl.is_valid():
            Title = self.get_object()
            formeyelidl.instance.user = request.user
            formeyelidl.instance.Title = Title
            formeyelidl.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formconjuctivar.is_valid():
            Title = self.get_object()
            formconjuctivar.instance.user = request.user
            formconjuctivar.instance.Title = Title
            formconjuctivar.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formconjuctival.is_valid():
            Title = self.get_object()
            formconjuctival.instance.user = request.user
            formconjuctival.instance.Title = Title
            formconjuctival.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formcornear.is_valid():
            Title = self.get_object()
            formcornear.instance.user = request.user
            formcornear.instance.Title = Title
            formcornear.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formcorneal.is_valid():
            Title = self.get_object()
            formcorneal.instance.user = request.user
            formcorneal.instance.Title = Title
            formcorneal.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formacr.is_valid():
            Title = self.get_object()
            formacr.instance.user = request.user
            formacr.instance.Title = Title
            formacr.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formacl.is_valid():
            Title = self.get_object()
            formacl.instance.user = request.user
            formacl.instance.Title = Title
            formacl.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formpupilr.is_valid():
            Title = self.get_object()
            formpupilr.instance.user = request.user
            formpupilr.instance.Title = Title
            formpupilr.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formpupill.is_valid():
            Title = self.get_object()
            formpupill.instance.user = request.user
            formpupill.instance.Title = Title
            formpupill.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formirisr.is_valid():
            Title = self.get_object()
            formirisr.instance.user = request.user
            formirisr.instance.Title = Title
            formirisr.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formirisl.is_valid():
            Title = self.get_object()
            formirisl.instance.user = request.user
            formirisl.instance.Title = Title
            formirisl.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formlensr.is_valid():
            Title = self.get_object()
            formlensr.instance.user = request.user
            formlensr.instance.Title = Title
            formlensr.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formlensl.is_valid():
            Title = self.get_object()
            formlensl.instance.user = request.user
            formlensl.instance.Title = Title
            formlensl.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formvitreousr.is_valid():
            Title = self.get_object()
            formvitreousr.instance.user = request.user
            formvitreousr.instance.Title = Title
            formvitreousr.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formvitreousl.is_valid():
            Title = self.get_object()
            formvitreousl.instance.user = request.user
            formvitreousl.instance.Title = Title
            formvitreousl.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formretinar.is_valid():
            Title = self.get_object()
            formretinar.instance.user = request.user
            formretinar.instance.Title = Title
            formretinar.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formretinal.is_valid():
            Title = self.get_object()
            formretinal.instance.user = request.user
            formretinal.instance.Title = Title
            formretinal.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formclinic.is_valid():
            Title = self.get_object()
            formclinic.instance.user = request.user
            formclinic.instance.Title = Title
            formclinic.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formhistory.is_valid():
            Title = self.get_object()
            formhistory.instance.user = request.user
            formhistory.instance.Title = Title
            formhistory.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
            
        if formgeneral.is_valid():
            Title = self.get_object()
            formgeneral.instance.user = request.user
            formgeneral.instance.Title = Title
            formgeneral.save()

            return redirect(reverse("viewpatient", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        post_clinic = Clinics.objects.all().filter(Title=self.object.pk)
        post_history = History.objects.all().filter(Title=self.object.pk)
        post_family = Family.objects.all().filter(Title=self.object.pk)
        post_general = General.objects.all().filter(Title=self.object.pk)
        post_management = Management.objects.all().filter(Title=self.object.pk)
        post_medication = Medication.objects.all().filter(Title=self.object.pk)
        post_diagnosis = Diagnosis.objects.all().filter(Title=self.object.pk)
        post_od = OD.objects.all().filter(Title=self.object.pk)
        post_os = OS.objects.all().filter(Title=self.object.pk)
        post_investigation = Investigation.objects.all().filter(Title=self.object.pk)
        post_re = RE.objects.all().filter(Title=self.object.pk)
        post_le = LE.objects.all().filter(Title=self.object.pk)
        post_visual = Visual.objects.all().filter(Title=self.object.pk)
        post_iopa = IOPA.objects.all().filter(Title=self.object.pk)
        post_iopb = IOPB.objects.all().filter(Title=self.object.pk)
        
        
        post_eyelidr = EYELIDR.objects.all().filter(Title=self.object.pk)
        post_eyelidl = EYELIDL.objects.all().filter(Title=self.object.pk)
        post_conjunctivar = CONJUNCTIVAR.objects.all().filter(Title=self.object.pk)
        post_conjunctival = CONJUNCTIVAL.objects.all().filter(Title=self.object.pk)
        post_cornear = CORNEAR.objects.all().filter(Title=self.object.pk)
        post_corneal = CORNEAL.objects.all().filter(Title=self.object.pk)
        post_acr = ACR.objects.all().filter(Title=self.object.pk)
        post_acl = ACL.objects.all().filter(Title=self.object.pk)
        post_pupilr = PUPILR.objects.all().filter(Title=self.object.pk)
        post_pupill = PUPILL.objects.all().filter(Title=self.object.pk)
        post_irisr = IRISR.objects.all().filter(Title=self.object.pk)
        post_irisl = IRISL.objects.all().filter(Title=self.object.pk)
        post_lensr = LENSR.objects.all().filter(Title=self.object.pk)
        post_lensl = LENSL.objects.all().filter(Title=self.object.pk)
        post_vitreousr = VITREOUSR.objects.all().filter(Title=self.object.pk)
        post_vitreousl = VITREOUSL.objects.all().filter(Title=self.object.pk)
        post_retinar = RETINAR.objects.all().filter(Title=self.object.pk)
        post_retinal = RETINAL.objects.all().filter(Title=self.object.pk)
        
        context = super().get_context_data(**kwargs)
        context.update({
                'formfamily':self.formfamily,
                'formclinic':self.formclinic,
                'formhistory':self.formhistory,
                'formgeneral':self.formgeneral,
                'formmanagement':self.formmanagement,
                'formmedication':self.formmedication,
                'formdiagnosis':self.formdiagnosis,
                'formod':self.formod,
                'formos':self.formos,
                'forminvestigation':self.forminvestigation,
                'formre':self.formre,
                'formle':self.formle,
                'formvisual':self.formvisual,
                'formiopa':self.formiopa,
                'formiopb':self.formiopb,
                
                'formeyelidr':self.formeyelidr,
                'formeyelidl':self.formeyelidl,
                'formconjuctivar':self.formconjuctivar,
                'formconjuctival':self.formconjuctival,
                'formcornear':self.formcornear,
                'formcorneal':self.formcorneal,
                'formacr':self.formacr,
                'formacl':self.formacl,
                'formpupilr':self.formpupilr,
                'formpupill':self.formpupill,
                'formirisr':self.formirisr,
                'formirisl':self.formirisl,
                'formlensr':self.formlensr,
                'formlensl':self.formlensl,
                'formvitreousr':self.formvitreousr,
                'formvitreousl':self.formvitreousl,
                'formretinar':self.formretinar,
                'formretinal':self.formretinal,
                
                'post_clinic':post_clinic,
                'post_history':post_history,
                'post_family':post_family,
                'post_general':post_general,
                'post_management':post_management,
                'post_medication':post_medication,
                'post_diagnosis':post_diagnosis,
                'post_od':post_od,
                'post_os':post_os,
                'post_investigation':post_investigation,
                'post_re':post_re,
                'post_le':post_le,
                'post_visual':post_visual,
                'post_iopa':post_iopa,
                'post_iopb':post_iopb,
                
                
                'post_eyelidr':post_eyelidr,
                'post_eyelidl':post_eyelidl,
                'post_conjunctivar':post_conjunctivar,
                'post_conjunctival':post_conjunctival,
                'post_cornear':post_cornear,
                'post_corneal':post_corneal,
                'post_acr':post_acr,
                'post_acl':post_acl,
                'post_pupilr':post_pupilr,
                'post_pupill':post_pupill,
                'post_irisr':post_irisr,
                'post_irisl':post_irisl,
                'post_lensr':post_lensr,
                'post_lensl':post_lensl,
                'post_vitreousr':post_vitreousr,
                'post_vitreousl':post_vitreousl,
                'post_retinar':post_retinar,
                'post_retinal':post_retinal,
            })
        return context
    
    

@login_required(login_url='signinsims')
def studentaccount(request):
    studentaccount = MyStaff.objects.all()
    # countstaff= MyStaff.objects.all().count()
    context={
        "studentaccount":studentaccount,
        # "countstaff":countstaff
    }
    return render(request, 'sims/studentaccount.html', context)

@login_required(login_url='signinsims')
def staff(request):
    stafflist = StaffContactinfo.objects.all().order_by("-pk")
    # countstaff= MyStaff.objects.all().count()
    context={
        "stafflist":stafflist,
        # "countstaff":countstaff
    }
    return render(request, 'sims/staff.html', context)


@login_required(login_url='signinsims')
def news(request):
    return render(request, 'sims/news.html')

@login_required(login_url='signinsims')
def payments(request):
    return render(request, 'sims/payments.html')

@login_required(login_url='signinsims')
def profile(request):
    current_user = request.user
    
    try:
        user_instance = get_object_or_404(MyStaff, username=current_user.username)
        Patient= Patient.objects.filter(user=user_instance)

        context={
            "Patient":Patient,
            "user_instance":user_instance,
            "current_user":current_user
        }
        return render(request, 'sims/profile.html', context)

    except MyStaff.DoesNotExist:
        raise Http404("User does not exist")  # Handle case where user is not found

@login_required(login_url='signinsims')
def myprofile(request):
    current_user = request.user
    
    try:
        user_instance = get_object_or_404(MyStaff, username=current_user.username)
        staffcontactinfo= StaffContactinfo.objects.filter(user=user_instance)

        context={
            "staffcontactinfo":staffcontactinfo,
            "user_instance":user_instance,
            "current_user":current_user
        }
        return render(request, 'sims/myprofile.html', context)

    except MyStaff.DoesNotExist:
        raise Http404("User does not exist")  # Handle case where user is not found

@login_required(login_url='signinsims')
def addPatient(request):
    Patient = PatientForm()
    if request.method == "POST":
        Patient = PatientForm(request.POST, files=request.FILES)
        if Patient.is_valid():
            Patient.save()
            messages.info(request, 'Patient Added Succesefull.')
            return redirect('addPatient')

    context={
        "Patient":Patient
    }
    return render(request, 'sims/addPatient.html', context)

@login_required(login_url='signinsims')
def addstaffcontactinfo(request):
    staffcontactinfo = StaffContactinfoForm()
    if request.method == "POST":
        staffcontactinfo = StaffContactinfoForm(request.POST, files=request.FILES)
        if staffcontactinfo.is_valid():
            staffcontactinfo.save()
            messages.info(request, 'Student Registered Succesefull.')
            return redirect('addstaff')

    context={
        "staffcontactinfo":staffcontactinfo
    }
    return render(request, 'sims/addstaffcontactinfo.html', context)

# views for viewing
@login_required(login_url='signinsims')
def viewstudentaccount(request, id):
    studentaccountview = MyStaff.objects.get(id=id)
    
    context = {"studentaccountview":studentaccountview}
    return render(request, 'sims/viewstudentaccount.html', context)

@login_required(login_url='signinsims')
def viewpatientinfo(request, id):
    patientinfoview = Patient.objects.get(id=id)
    
    context = {"patientinfoview":patientinfoview}
    return render(request, 'sims/viewpatientinfo.html', context)

@login_required(login_url='signinsims')
def viewstaffinfo(request, id):
    staffinfoview = StaffContactinfo.objects.get(id=id)
    
    context = {"staffinfoview":staffinfoview}
    return render(request, 'sims/viewstaffinfo.html', context)

# view for updating the information
@login_required(login_url='signinsims')
def updatepatient(request, pk):
    a = Patient.objects.get(pk=pk)
    patient =PatientForm(instance=a)
    if request.method == "POST":
        patient = PatientForm(request.POST, files=request.FILES, instance=a)
        if patient.is_valid():
            patient.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('patient')
    context = {"patient":patient}
    return render(request, 'sims/updatepatient.html', context)

@login_required(login_url='signinsims')
def updatestaffcontactinfo(request, id):
    b = StaffContactinfo.objects.get(id=id)
    staffinfo =StaffContactinfoForm(instance=b)
    if request.method == "POST":
        staffinfo = StaffContactinfoForm(request.POST, files=request.FILES, instance=b)
        if staffinfo.is_valid():
            staffinfo.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('staff')
    context = {"staffinfo":staffinfo}
    return render(request, 'sims/updatestaffcontactinfo.html', context)

@login_required(login_url='signinsims')
def updatestudentaccount(request, id):
    c = MyStaff.objects.get(id=id)
    studentaccount =MyStaffForm(instance=c)
    if request.method == "POST":
        studentaccount = MyStaffForm(request.POST, files=request.FILES, instance=c)
    if studentaccount.is_valid():
        cleaned_data = studentaccount.cleaned_data
        # Check if the new username is different from the existing one
        if 'username' in cleaned_data and cleaned_data['username'] != c.username:
            # If it's different, update the instance and save
            c.username = cleaned_data['username']
            c.save()
            messages.info(request, 'Updated successfully.')
            return redirect('students')
        else:
            # Username remains unchanged, proceed without modifying
            messages.info(request, 'No changes made.')
            return redirect('students')
    context = {"studentaccount":studentaccount}
    return render(request, 'sims/updatestudentaccount.html', context)

# view for deleting information
@login_required(login_url='signinsims')
def deletepatient(request, pk):
    patientdelete = Patient.objects.get(pk=pk)
    if request.method == "POST":
        patientdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('patient')
    
    context = {"patientdelete":patientdelete}
    return render(request, 'sims/deletepatient.html', context)

@login_required(login_url='signinsims')
def deletestaffcontactinfo(request, id):
    staffcontactinfodelete = StaffContactinfo.objects.get(id=id)
    if request.method == "POST":
        staffcontactinfodelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('staff')
    
    context = {"staffcontactinfodelete":staffcontactinfodelete}
    return render(request, 'sims/deletestaffcontactinfo.html', context)

@login_required(login_url='signinsims')
def deletestudentaccount(request, id):
    studentaccountdelete = MyStaff.objects.get(id=id)
    if request.method == "POST":
        studentaccountdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('studentaccount')
    
    context = {"studentaccountdelete":studentaccountdelete}
    return render(request, 'sims/deletestudentaccount.html', context)


@login_required(login_url='signinsims')
def change_password(request):
    if request.method == 'POST':
        passwordchange = PasswordChangeForm(request.user, request.POST)
        if passwordchange.is_valid():
            user = passwordchange.save()
            # This is to keep the user logged in after password change
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('signinsims')  # Redirect to the same page after successful password change
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        passwordchange = PasswordChangeForm(request.user)
    return render(request, 'sims/change_password.html', {'passwordchange': passwordchange})


# FOR PRINTING ALL TABLES

def export_patients_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="patients.csv"'

    patients = Patient.objects.all()

    header = ['Patient ID', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Place', 'Age', 'Phone', 'Payment', 'Cost', 'Date']
    csv_data = ','.join(header) + '\n'
    for patient in patients:
        csv_data += ','.join([
            patient.Patient_Id,
            patient.First_Name,
            patient.Middle_Name,
            patient.Last_Name,
            patient.Sex,
            patient.Place,
            patient.Age,
            patient.Phone,
            patient.Payment,
            patient.Cost,
            patient.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ]) + '\n'

    response.write(csv_data)
    return response

def export_patients_to_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="patients.pdf"'

    patients = Patient.objects.all()

    table_data = [['Patient ID', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Place', 'Age', 'Phone', 'Payment', 'Cost', 'Date']]
    for patient in patients:
        table_data.append([
            patient.Patient_Id,
            patient.First_Name,
            patient.Middle_Name,
            patient.Last_Name,
            patient.Sex,
            patient.Place,
            patient.Age,
            patient.Phone,
            patient.Payment,
            patient.Cost,
            patient.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ])

    doc = SimpleDocTemplate(response, pagesize=letter)
    table = Table(table_data)

    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    doc.build([table])

    return response

def export_patients_to_excel(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="patients.xlsx"'

    patients = Patient.objects.all()

    wb = Workbook()
    ws = wb.active

    ws.append(['Patient ID', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Place', 'Age', 'Phone', 'Payment', 'Cost', 'Date'])
    for patient in patients:
        ws.append([
            patient.Patient_Id,
            patient.First_Name,
            patient.Middle_Name,
            patient.Last_Name,
            patient.Sex,
            patient.Place,
            patient.Age,
            patient.Phone,
            patient.Payment,
            patient.Cost,
            patient.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ])

    wb.save(response)
    return response




# FOR PRINTING ALL TABLES OF STAFF CONTACT INFORMATION

def export_staff_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="staff.csv"'

    staffs = StaffContactinfo.objects.all()

    header = ['Staff ID', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Level_Of_Education', 'Professional', 'Phone', 'Region', 'Date']
    csv_data = ','.join(header) + '\n'
    for staff in staffs:
        csv_data += ','.join([
            staff.user.username if staff.user else '',
            staff.First_Name,
            staff.Middle_Name,
            staff.Last_Name,
            staff.Sex,
            staff.Level_Of_Education,
            staff.Professional,
            staff.Phone,
            staff.Region,
            staff.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ]) + '\n'

    response.write(csv_data)
    return response

def export_staff_to_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="staff.pdf"'

    staffs = StaffContactinfo.objects.all()

    table_data = [['Staff ID', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Level_Of_Education', 'Professional', 'Phone', 'Region', 'Date']]
    for staff in staffs:
        table_data.append([
            staff.user,
            staff.First_Name,
            staff.Middle_Name,
            staff.Last_Name,
            staff.Sex,
            staff.Level_Of_Education,
            staff.Professional,
            staff.Phone,
            staff.Region,
            staff.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ])

    doc = SimpleDocTemplate(response, pagesize=letter)
    table = Table(table_data)

    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    doc.build([table])

    return response

def export_staff_to_excel(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="staff.xlsx"'

    staffs = StaffContactinfo.objects.all()

    wb = Workbook()
    ws = wb.active

    ws.append(['Staff ID', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Level_Of_Education', 'Professional', 'Phone', 'Region', 'Date'])
    for staff in staffs:
        ws.append([
            staff.user.username if staff.user else '',
            staff.First_Name,
            staff.Middle_Name,
            staff.Last_Name,
            staff.Sex,
            staff.Level_Of_Education,
            staff.Professional,
            staff.Phone,
            staff.Region,
            staff.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ])

    wb.save(response)
    return response
