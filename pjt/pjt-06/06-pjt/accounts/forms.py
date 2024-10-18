from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms   

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='사용자 이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디를 작성해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )

    email = forms.CharField(
        label='이메일 주소',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일을 작성해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )

    # first_name = forms.CharField(
    #     label='이름',
    #     required=False,
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': '이름을 작성해 주세요.',
    #             'style': 'width: 400px; height: 40px;',
    #         }
    #     )
    # )

    # last_name = forms.CharField(
    #     label='성',
    #     required=False,
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': '성을 작성해 주세요.',
    #             'style': 'width: 400px; height: 40px;',
    #         }
    #     )
    # )

    password1 = forms.CharField(
        label='새 비밀번호',
        widget=forms.TextInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': '새 비밀번호를 입력해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )

    password2 = forms.CharField(
        label='새 비밀번호(확인)',
        widget=forms.TextInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': '새 비밀번호를 다시 입력해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )
    
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):
    label='사용자 이름',
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디를 작성해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )

    email = forms.CharField(
        required=False,
        label='이메일 주소',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일을 작성해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )

    first_name = forms.CharField(
        label='이름',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '이름을 작성해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )

    last_name = forms.CharField(
        label='성',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '성을 작성해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'username',)


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='기존 비밀번호',
        widget=forms.TextInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': '기존 비밀번호를 입력해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )

    new_password1 = forms.CharField(
        label='새 비밀번호',
        widget=forms.TextInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': '새 비밀번호를 입력해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )

    new_password2 = forms.CharField(
        label='새 비밀번호(확인)',
        widget=forms.TextInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': '새 비밀번호를 다시 입력해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )

    class Meta(PasswordChangeForm):
        model = get_user_model()
        fields = '__all__'


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='사용자 이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '사용자 이름을 입력해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )

    password = forms.CharField(
        label='비밀번호',
        widget=forms.TextInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': '비밀번호를 입력해 주세요.',
                'style': 'width: 400px; height: 40px;',
            }
        )
    )

    class Meta(AuthenticationForm):
        model = get_user_model()
        fields = '__all__'