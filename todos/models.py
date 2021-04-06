from django.db import models
from django.forms.models import ModelForm
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Todo Item")
    descr = models.CharField(max_length=150, verbose_name="Todo Description", null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    is_completed = models.BooleanField(verbose_name="Completed")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TodoForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'descr', 'is_completed']