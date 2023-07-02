from django import forms
from catalog.models import Blog, Product, Version
from django.forms import formset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'image',)


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('version_name',)


class ProductForm(forms.ModelForm):
    versions = formset_factory(VersionForm, extra=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', css_class='form-control'),
            Field('description', css_class='form-control'),
            Field('preview', css_class='form-control'),
            Field('category', css_class='form-control'),
            Field('price', css_class='form-control'),
            Field('Versions', css_class='form-control'),
        )

    class Meta:
        model = Product
        fields = ("name", "description", "preview", "category", "price")


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name', '')
        description = cleaned_data.get('description', '')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        for word in forbidden_words:
            if word in name.lower() or word in description.lower():
                raise forms.ValidationError("Недопустимое содержимое в названии или описании продукта.")

        versions = cleaned_data.get('versions')
        if versions:
            for version_form in versions:
                if not version_form.is_valid():
                    raise forms.ValidationError("Недопустимое содержимое в версии продукта.")
        return cleaned_data

    def save_versions(self, product):
        versions = self.cleaned_data.get('versions')
        if versions:
            for version_form in versions:
                version = version_form.save(commit=False)
                version.product = product
                version.save()

