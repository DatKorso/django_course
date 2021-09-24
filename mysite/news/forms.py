from django import forms
from .models import News

#class NewsForm(forms.Form):
#    title = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={"class": "form-control"}))
#    content = forms.CharField(required=False, label='Содержимое', widget=forms.Textarea(attrs={
#        "class": "form-control",
#        "rows": 5,
#    }))
#    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Выберите категорию',
#                                      label='Категория', widget=forms.Select(
#        attrs={"class": "form-control"}))

class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Выберите категорию"

    class Meta:
        model = News

        #Чтобы сразу все поля
        #fields = '__all__'

        fields = ['title', 'content', 'category']
        labels = {
            'title': 'Заголовок',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }