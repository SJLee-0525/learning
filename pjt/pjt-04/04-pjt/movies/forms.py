from .models import Movie
from .models import ImageUpload
from django import forms    

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 작성해 주세요.',
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '설명을 작성해 주세요.',
            }
        )
    )

    image = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    
    class Meta():
        model = Movie
        fields = '__all__'


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['image']