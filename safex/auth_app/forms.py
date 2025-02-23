from django import forms
from .models import Files, User, Department

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['name_file', 'id_department', 'file_upload']  # 🔥 Enlève 'date'


class CustomUserChangeForm(forms.ModelForm):
    departements_secondaires = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        widget=forms.CheckboxSelectMultiple,  
        required=False,
        label="Départements secondaires"
    )

    class Meta:
        model = User
        fields = ['name_user', 'mail_user', 'password', 'departement_principal', 'departements_secondaires', 'type']

    def clean_departements_secondaires(self):
        departements = self.cleaned_data.get('departements_secondaires')
        user_type = self.cleaned_data.get('type')

        if user_type == 'employe_simple' and departements.count() > 0:
            raise forms.ValidationError("Un employé simple ne peut appartenir qu'à un seul département.")

        return departements

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('type')

        if user_type == 'employe_simple':
            cleaned_data['departements_secondaires'] = []  # Supprime les départements secondaires
        
        return cleaned_data
