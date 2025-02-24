from django import forms
from .models import Files, User, Department

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['name_file', 'id_department', 'file_upload']  # 🔥 Enlève 'date'


class CustomUserChangeForm(forms.ModelForm):
    departments_with_roles = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Départements associés"  # Nom plus clair
    )

    class Meta:
        model = User
        fields = ['name_user', 'mail_user', 'password', 'departement_principal', 'departments_with_roles', 'type']

    def clean_departments_with_roles(self):
        departments = self.cleaned_data.get('departments_with_roles')
        user_type = self.cleaned_data.get('type')

        if user_type == 'employe_simple' and departments.count() > 0:
            raise forms.ValidationError("Un employé simple ne peut appartenir qu'à un seul département.")

        return departments

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('type')

        if user_type == 'employe_simple':
            cleaned_data['departments_with_roles'] = []  # Supprime les départements secondaires
        
        return cleaned_data

