from django.forms import ModelForm, TextInput, FileInput, NumberInput, Textarea
from housedesignapp.models import *


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            'name',
            'image',
            'price',
            'description'
        )
        widgets = {
            'name' : TextInput(attrs={
                'class' : 'input input-accent w-full',
                'placeholder' : 'Enter Name' 
            }),
            'image' : FileInput(attrs={
                'class' : 'file-input file-input-bordered',
                'placeholder' : 'Image'
            }),
            'price' : NumberInput(attrs={
                'class' : 'input input-accent w-full',
                'placeholder' : 'Enter Price'
            }),
            'description' : Textarea(attrs={
                'class' : 'textarea textarea-accent',
                'placeholder' : 'Enter Description'
            })
        }