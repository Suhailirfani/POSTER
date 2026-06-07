from django import forms
from .models import Program

GRADE_CHOICES = [
    ('', '-- Select Grade --'),
    ('A', 'Grade A'),
    ('B', 'Grade B'),
    ('C', 'Grade C'),
    ('D', 'Grade D'),
]

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'name_image', 'date', 'place', 'authority', 'authority_image', 'categories', 'teams']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. സാഹിത്യോൽസവം 2025'}),
            'date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'place': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Town Hall, Kozhikode'}),
            'authority': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Kerala Sahitya Akademi'}),
            'categories': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Junior, Senior, General'}),
            'teams': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Red House, Blue House, Green House'}),
        }
        labels = {
            'name': 'Program Name / പരിപാടിയുടെ പേര്',
            'date': 'Date / തീയതി',
            'place': 'Place / സ്ഥലം',
            'authority': 'Organising Authority / സംഘടന',
            'categories': 'Categories (comma separated)',
            'teams': 'Teams (comma separated)',
        }

class ResultForm(forms.Form):
    def __init__(self, *args, **kwargs):
        program = kwargs.pop('program', None)
        super(ResultForm, self).__init__(*args, **kwargs)
        
        category_choices = [('', '-- Select Category --')]
        team_choices = [('', '-- Select Team --')]
        
        if program:
            if program.categories:
                cats = [c.strip() for c in program.categories.split(',') if c.strip()]
                category_choices.extend([(c, c) for c in cats])
            if program.teams:
                tms = [t.strip() for t in program.teams.split(',') if t.strip()]
                team_choices.extend([(t, t) for t in tms])
                
        self.fields['category'].choices = category_choices
        self.fields['first_team'].choices = team_choices
        self.fields['second_team'].choices = team_choices
        self.fields['third_team'].choices = team_choices

    item_name = forms.CharField(
        max_length=200,
        label='Item / ഇനം',
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. കഥാരചന, ഉപന്യാസം...',
            'class': 'form-input',
            'id': 'item_name',
        })
    )
    category = forms.ChoiceField(
        choices=[],
        label='Category / വിഭാഗം',
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'category',
        })
    )

    # 1st Place
    first_name = forms.CharField(
        max_length=200,
        label='1st Place Name / ഒന്നാം സ്ഥാനം',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '1st Place Winner Name',
            'class': 'form-input winner-input',
            'id': 'first_name',
        })
    )
    first_grade = forms.ChoiceField(
        choices=GRADE_CHOICES,
        label='Grade / ഗ്രേഡ്',
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'first_grade',
        })
    )
    first_team = forms.ChoiceField(
        choices=[],
        label='Team / ടീം',
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'first_team',
        })
    )

    # 2nd Place
    second_name = forms.CharField(
        max_length=200,
        label='2nd Place Name / രണ്ടാം സ്ഥാനം',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '2nd Place Winner Name',
            'class': 'form-input winner-input',
            'id': 'second_name',
        })
    )
    second_grade = forms.ChoiceField(
        choices=GRADE_CHOICES,
        label='Grade / ഗ്രേഡ്',
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'second_grade',
        })
    )
    second_team = forms.ChoiceField(
        choices=[],
        label='Team / ടീം',
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'second_team',
        })
    )

    # 3rd Place
    third_name = forms.CharField(
        max_length=200,
        label='3rd Place Name / മൂന്നാം സ്ഥാനം',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '3rd Place Winner Name',
            'class': 'form-input winner-input',
            'id': 'third_name',
        })
    )
    third_grade = forms.ChoiceField(
        choices=GRADE_CHOICES,
        label='Grade / ഗ്രേഡ്',
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'third_grade',
        })
    )
    third_team = forms.ChoiceField(
        choices=[],
        label='Team / ടീം',
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'third_team',
        })
    )

    template_id = forms.IntegerField(
        widget=forms.HiddenInput(attrs={'id': 'selected_template'}),
        initial=1,
    )
