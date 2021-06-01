from django import forms  

class ChangePrefix(forms.Form):
    GuildID = forms.CharField(max_length=200, required = False, label="Guild ID")
    Prefix = forms.CharField(max_length=200, required = False, label="New Prefix")
