from django import forms
from .models import Database

class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Database
        fields = '__all__'

    def clean_state_code(self):
        state_code = self.cleaned_data.get('state_code')
        if not state_code:
            raise forms.ValidationError('This field is required')
        
        for instance in Database.objects.all():
            if instance.state_code == state_code:
                raise forms.ValidationError(str(state_code) + ' is already documented')
        return state_code
        
    def clean_account_number(self):
        account_number = self.cleaned_data.get('account_number')
        if not account_number:
            raise forms.ValidationError('This field is required')

        for instance in Database.objects.all():
            if instance.account_number == account_number:
                raise forms.ValidationError(str(account_number) + ' is already documented')
        return account_number

    def __init__(self, *args, **kwargs):
        super(DatabaseForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'John Noah'
        self.fields['state_code'].widget.attrs['placeholder'] = 'RV/21C/0325' 
        self.fields['ppa'].widget.attrs['placeholder'] = 'Community Secondary School (UBE) Okehi'
        self.fields['bank_name'].widget.attrs['placeholder'] = 'Union Bank'
        self.fields['account_number'].widget.attrs['placeholder'] = '21321547xx'

        self.fields['name'].required = True
        # self.fields['state_code'].required = True
        self.fields['ppa'].required = True
        self.fields['bank_name'].required = True
        # self.fields['account_number'].required = True