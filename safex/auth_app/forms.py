from django import forms
from .models import Files, User, Department

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['name_file', 'date', 'id_department', 'file_upload']

class UserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmer le mot de passe")
    id_dep = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Permet de sélectionner plusieurs départements avec des cases à cocher
        required=False,
        label="Départements"
    )

    class Meta:
        model = User
        fields = ['name_user', 'mail_user', 'password', 'password2', 'id_dep', 'type', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")

        return cleaned_data

    def clean_id_dep(self):
        id_dep = self.cleaned_data.get('id_dep')
        user_type = self.cleaned_data.get('type')

        # ✅ Seuls les chefs de service et directeurs généraux peuvent avoir plusieurs départements
        if user_type not in ['chef_service', 'directeur_general'] and len(id_dep) > 1:
            raise forms.ValidationError('Seuls les chefs de service et les directeurs généraux peuvent appartenir à plusieurs départements.')

        return id_dep

class CustomUserChangeForm(forms.ModelForm):
    id_dep = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Sélection multiple des départements
        required=False,
        label="Départements"
    )

    class Meta:
        model = User
        fields = ['name_user', 'mail_user', 'password', 'id_dep', 'type', 'role']

    def clean_id_dep(self):
        id_dep = self.cleaned_data.get('id_dep')
        user_type = self.cleaned_data.get('type')

        if user_type not in ['chef_service', 'directeur_general'] and len(id_dep) > 1:
            raise forms.ValidationError('Seuls les chefs de service et les directeurs généraux peuvent appartenir à plusieurs départements.')

        return id_dep
