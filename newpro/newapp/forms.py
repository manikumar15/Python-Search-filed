from django import forms
from .models import News,Python,Api,Html,Search



class Newsletter(forms.ModelForm):
    Email=forms.CharField(required=True,max_length=50)

    class Meta:
        model = News
        widgets = {'Email': forms.EmailInput(), }
        fields = ['Email',]

class Pythonform(forms.ModelForm):
	name=forms.CharField(required=True,max_length=50)
	email=forms.CharField(required=True,max_length=50)
	phone=forms.IntegerField()
	message=forms.CharField(max_length=20)
	class Meta:
		model = Python
		fields = '__all__'

class Apiform(forms.ModelForm):
	name=forms.CharField(required=True,max_length=50)
	email=forms.CharField(required=True,max_length=50)
	phone=forms.IntegerField()
	message=forms.CharField(max_length=20)
	class Meta:
		model = Api
		fields = '__all__'

class Htmlform(forms.ModelForm):
	name=forms.CharField(required=True,max_length=50)
	email=forms.CharField(required=True,max_length=50)
	phone=forms.IntegerField()
	message=forms.CharField(max_length=20)
	class Meta:
		model = Html
		fields = '__all__'

class Searchform(forms.ModelForm):
    class Meta:
        model=Search
        fields = "__all__"