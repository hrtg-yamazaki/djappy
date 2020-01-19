from django import forms

class UserSearchForm(forms.Form):
    keyword = forms.CharField(
        label='ユーザー検索',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder':'ユーザー名を入力'})
    )