from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Usuario

class CustomLoginForm(AuthenticationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'bg-[#333333] rounded-md w-full', 'placeholder': 'Email'}))

    class Meta:
        model = Usuario
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'bg-[#333333] rounded-md w-full'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de Usuário'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password'].widget.attrs['class'] = 'bg-[#333333] rounded-md w-full'
        self.fields['password'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password'].label = ''
        self.fields['password'].help_text = ''

class SignUpForm(UserCreationForm):

    email = forms.EmailField(label='',max_length=254, widget=forms.TextInput(attrs={'class': 'bg-[#333333] rounded-md w-[350px]', 'placeholder': 'Email'}) , required=True)
    

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].widget.attrs['class'] = 'bg-[#333333] rounded-md w-[350px]'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmação de senha'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'bg-[#333333] rounded-md w-[350px]'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['username'].widget.attrs['class'] = 'bg-[#333333] rounded-md w-[350px]'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''



class FormHomepage(forms.Form):
    email = forms.EmailField(label='',max_length=254, widget=forms.TextInput(attrs={'class': 'w-[35rem] text-white bg-[#0F1118] rounded-md focus:outline-none focus:ring focus:ring-[#E50914] py-[1.5rem] px-3 text-black', 'placeholder': 'Email'}) , required=True)


