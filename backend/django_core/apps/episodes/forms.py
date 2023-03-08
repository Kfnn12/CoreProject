from django_admin_hstore_widget.forms import HStoreFormField

from django import forms

from .models import EpisodeModel


class EpisodeAdminModelForm(forms.ModelForm[EpisodeModel]):
    providers = HStoreFormField()

    class Meta:
        model = EpisodeModel
        fields = "__all__"
