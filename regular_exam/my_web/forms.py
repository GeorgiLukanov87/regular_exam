from django import forms

from regular_exam.my_web.models import Profile, Fruit


# PROFILE FORMS:
class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password')
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password'
                }
            ),
        }


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url', 'age',)

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
            'age': 'Age',
        }


class ProfileDeleteForm(ProfileBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Fruit.objects.all().delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitCreateForm(FruitBaseForm):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description', 'nutrition',)
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description'
                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info'
                }
            ),
        }


# FRUIT FORMS:
class FruitEditForm(FruitBaseForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitDeleteForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
            field.required = False

    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description',)
