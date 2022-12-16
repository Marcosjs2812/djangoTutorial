from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titel", max_length=200)
    description = forms.CharField(
        label="Descripción de la tarea", widget=forms.Textarea)


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)
