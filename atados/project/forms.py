# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from bootstrap_toolkit.widgets import BootstrapTextInput
from atados.project.models import (Project,
                                   ProjectDonation,
                                   ProjectWork)


class ProjectCreateForm(forms.ModelForm):

    def __init__(self, organisation, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)

        self.organisation = organisation

        self.fields['email'].widget.attrs.update({
            'placeholder' : _('example@example.com')})

        self.fields['details'].widget.attrs.update({
            'placeholder' : _('Add more info about this project')})

    def clean_name(self):
        name = self.cleaned_data.get('name')
        slug = slugify(name)
        if slug and self.instance.slug != slug and Project.objects.filter(
                slug=slug, organisation=self.organisation).count():
            raise forms.ValidationError(_('This name (or a very similar) is already is use.'))
        return name

class ProjectDonationCreateForm(ProjectCreateForm):

    class Meta:
        model = ProjectDonation
        exclude = ('organisation', 'slug')

class ProjectJustOnceCreateForm(ProjectCreateForm):

    class Meta:
        model = ProjectWork
        exclude = ('organisation', 'slug', 'monthly_hours')

class ProjectPeriodicCreateForm(ProjectCreateForm):

    def __init__(self, *args, **kwargs):
        super(ProjectPeriodicCreateForm, self).__init__(*args, **kwargs)
        self.fields['monthly_hours'].required = True
        self.fields['classification'].empty_label = ""

    class Meta:
        model = ProjectWork
        exclude = ('organisation', 'slug')
