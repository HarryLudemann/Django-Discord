from django import forms  

class ChangePrivileges(forms.Form):
    identifier = forms.CharField(max_length=200, required = False, label="New Prefix")
    funinspire = forms.CharField(max_length=200, required = False, label="Inspire")
    funcomeback = forms.CharField(max_length=200, required = False, label="Comeback")
    funcat = forms.CharField(max_length=200, required = False, label="Cat")
    fundog = forms.CharField(max_length=200, required = False, label="Dog")
    funfox = forms.CharField(max_length=200, required = False, label="Fox")
    basicping = forms.CharField(max_length=200, required = False, label="Ping")
    adminquit = forms.CharField(max_length=200, required = False, label="Quit")
    adminchangeprefix = forms.CharField(max_length=200, required = False, label="Change Prefix")
    admintest = forms.CharField(max_length=200, required = False, label="Test")
   
 