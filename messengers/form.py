from django.forms import Textarea, TextInput, FileInput
from django import forms


from .models import Messages


class NewMessage(forms.ModelForm):
    class Meta:
        model = Messages
        exclude = ["date_sent", "receiver", "sender"]
        labels = {'text': "", 'media': ""}
        widgets = {
            'text': Textarea(attrs={'placeholder': "message"}),
            "media": FileInput(attrs={
                'accept': ".png,.jpeg,.jpg,.mp4,.mp3,.pdf",
                'multiple': True
            })
        }


class Search(forms.Form):
    search = forms.CharField(max_length=100, label="", label_suffix="", widget=TextInput(
        attrs={"placeholder": "Search", "class": "search"}))


class SearchMessages(forms.Form):
    search = forms.CharField(label="", label_suffix="", widget=Textarea(
        attrs={"placeholder": "Search_Messages", "class": "search"}))
