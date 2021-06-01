from django import forms  

class ChangePrivileges(forms.Form):
    guildid = forms.CharField(max_length=200, required = False, label="Guild ID")
    identifier = forms.CharField(max_length=200, required = False, label="New Prefix")
    funinspire = forms.CharField(max_length=200, required = False, label="Guild ID")
    funcomeback = forms.CharField(max_length=200, required = False, label="New Prefix")
    funcat = forms.CharField(max_length=200, required = False, label="Guild ID")
    fundog = forms.CharField(max_length=200, required = False, label="New Prefix")
    funfox = forms.CharField(max_length=200, required = False, label="Guild ID")
    basicping = forms.CharField(max_length=200, required = False, label="New Prefix")
    adminquit = forms.CharField(max_length=200, required = False, label="Guild ID")
    adminchangeprefix = forms.CharField(max_length=200, required = False, label="New Prefix")
    admintest = forms.CharField(max_length=200, required = False, label="Guild ID")
   