from django import forms
from .models import Post, Category, Comments
from tinymce.widgets import TinyMCE

class AddPostForm(forms.ModelForm):
    ### Zmiana nazw wyswietlanych pol w formularzu
    def __init__(self,*args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label='Tytuł'
        self.fields['author'].label = 'Autor'
        self.fields['tag'].label = 'Tagi'
        self.fields['category'].label = 'Kategoria'
        self.fields['snippet'].label = 'Streszczenie'
        self.fields['body'].label = 'Treść artykułu'
        self.fields['post_picture'].label = 'Zdjęcie tytułowe'
    ###--------------------------------------------

    class Meta:
        model=Post
        fields=['title','tag','author','category','snippet','body','post_picture']

        category=Category.objects.all().values_list('category','category')
        category_list=[]
        for item in category:
            category_list.append(item)

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Tytuł',}),
            'tag':forms.TextInput(attrs={'class':'form-control','placeholder':'Tagi'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Autor','value':'','type':'hidden','id':'aut'}),
            'category':forms.Select(choices=category_list,attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dodaj krótki opis artykułu...'}),
            'body':TinyMCE(attrs={'class':'form-control','placeholder':'Napisz swój artykuł...'})

        }
