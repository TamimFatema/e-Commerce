from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Category (models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default='')
    sub_category = models.ForeignKey(
        Sub_Category, on_delete=models.CASCADE, default='')
    image = models.ImageField(upload_to='kinakta/pimage')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={
                             'exists': 'This User Exists'})


class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_emaill(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(
                self.fields['email'].error_message['exists'])
        return self.cleaned_data['email']
