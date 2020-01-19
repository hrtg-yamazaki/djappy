from django import forms
from .models import Category

class TitleSearchForm(forms.Form):
    keyword = forms.CharField(
        label='タイトル検索',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder':'タイトルを入力'})
    )

class CategorySearchForm(forms.Form):
    category_id = forms.ModelChoiceField(
        label='カテゴリ検索',
        queryset= Category.objects.all()
    )