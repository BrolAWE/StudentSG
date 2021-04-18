from core.models import Participant
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        labels = {'last_name': 'Фамилия', 'first_name': 'Имя', 'second_name': 'Отчество'
            , 'email': 'E-mail', 'phone': 'Телефон', 'city': 'Город', 'organization': 'Образовательная организация'
            , 'nomination': 'Номинация', 'file': 'Файл', 'brief': 'Текст письма', 'site': 'Ссылка на сайт',
                  'video': 'Ссылка на видео'}

        widgets = {
            'brief': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-registrationForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout(
            'last_name',
            'first_name',
            'second_name',
            'email',
            'phone',
            'city',
            'organization',
            'nomination',
            'file',
            'brief',
            Row(
                Column('site', css_class='form-group col-md-6 mb-0'),
                Column('video', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Отправить')
        )
