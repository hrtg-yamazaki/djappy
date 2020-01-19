from django import forms

class TitleSearchForm(forms.Form):
    keyword = forms.CharField(
        label='タイトル検索',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder':'タイトルを入力'})
    )