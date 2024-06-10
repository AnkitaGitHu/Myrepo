

from .forms import *
from django.forms import ModelForm

from .models import *

class BloodForms(ModelForm):
  class Meta:
    model = Blood
    fields = "__all__"  



