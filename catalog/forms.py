from django import forms
from catalog.models import Product

forbidden_words = ['казино', 'криптовалюта', 'крипта',
                       'биржа', 'дешево', 'бесплатно', 'обман',
                       'полиция', 'радар'
                       ]
class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('owner',)


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        if name and any(word in name.lower() for word in forbidden_words):
            self.add_error('name', 'Недопустимое название продукта!')
        if description and any(word in description.lower() for word in forbidden_words):
            self.add_error('description', 'Описание содержит запрещённые слова!')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'