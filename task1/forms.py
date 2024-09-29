from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, label="Ваше имя")
    password = forms.CharField(min_length=8, label="Ваш пароль")
    password2 = forms.CharField(min_length=8, label="Повторите ваш пароль")
    balance = forms.CharField(min_length=4, label="Сколько денег вы помещаете на счет")
    age = forms.CharField(max_length=3, label="Dаш возраст")
