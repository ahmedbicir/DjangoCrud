from django import forms

class studentForm(forms.Form):
    # TYPE-TEXT
    name = forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={
        'class':'input',
        'name':'name',
        'placeholder':'Full Names',
    }))

    regno = forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={
        'class':'input',
        'name':'regno',
        'placeholder':'Registration Number'
    }))

    course = forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={
        'class':'input',
        'name':'course',
        'placeholder':'Course'
    }))
 
    # TYPE-NUMBER
    nationalId = forms.CharField(max_length=100,
    widget=forms.NumberInput(attrs={
        'class':'input',
        'name':'nationalId',
        'placeholder':'National Id'
    }))

    # SELECT-OPTIONS
    OPTIONS = (
        ('', 'Choose gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        )
    gender = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'input',
        'name':'gender',
    }), choices=OPTIONS)
    
    # CHECKBOXES
    LANGS = (
        ("PHP", "PHP"),
        ("JAVASCRIPT", "JAVASCRIPT"),
        ("PYTHON", "PYTHON"),
    )
    languages = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
    choices=LANGS)

    # RADIO BUTTONS
    MODES = (('Day','Day'),('Weekends','Weekends'))
    mode=forms.CharField(widget=forms.RadioSelect(choices=MODES))


    # Sign up
class studentSignup(forms.Form):
    # TYPE-TEXT
     studentname = forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={
        'class':'input',
        'name':'studentname',
        'placeholder':'Full Names',
    }))

     regno = forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={
        'class':'input',
        'name':'regno',
        'placeholder':'Registration Number'
    }))
