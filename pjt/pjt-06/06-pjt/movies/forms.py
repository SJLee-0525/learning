from .models import Movie, Comment, ImageUpload
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
        fields = ('title', 'description', 'image',)
        # fields = '__all__'


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['image']


class CommentForm(forms.ModelForm):

    content = forms.CharField(
        label='댓글 쓰기',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '댓글을 작성해 주세요.',
                'style': 'width: 600px; height: 120px;',
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('content',)