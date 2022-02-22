from django.core.exceptions import ValidationError
from django import forms
import os
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

    def clean_voice_sample(self):
         file = self.cleaned_data.get('voice_sample',False)
         if file:
             if file.size > 5*1024*1024:
                   raise ValidationError("File is too large ( > 5mb )")
             if not file.content_type in ["audio/mpeg","audio/aac"]:
                   raise ValidationError("Not a valid mp3/aac audio")
             if not os.path.splitext(file.name)[1] in [".mp3",".wav" ,".aac"]:
                   raise ValidationError("Audio file has no proper extension i.e .mp3 or .aac ")
             
             return file
         else:
             raise ValidationError("Couldn't read uploaded file")



   
