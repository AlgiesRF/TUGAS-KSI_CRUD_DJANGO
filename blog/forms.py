from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'email',
        ]

        widgets={
            'title': forms.TextInput(
                attrs= {
                    'class' : 'form',
                    'placeholder':'Masukkan Judul',
                }
            )
        }






# from django import forms

# class classform(forms.Form):
#     namac = forms.CharField(
#         label = 'Nama Lengkap',
#         widget = forms.TextInput(
#             attrs={
#                 'class':'field padding-bottom--24',
#                 'type':'nama',
#                 'placeholder':'Masukkan Nama',
#             }
#         )
#     )
#     alamatc = forms.CharField(
#         label = 'Alamat',
#         widget = forms.TextInput(
#             attrs={
#                 'class':'field padding-bottom--24',
#                 'type':'alamat',
#                 'placeholder':'Masukkan Alamat',
#             }
#         )
#     )