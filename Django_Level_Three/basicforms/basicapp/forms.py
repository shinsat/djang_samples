from django import forms
from django.utils.safestring import mark_safe

# Very Basic Example of a Django Form
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class FormName(forms.Form):
    name = forms.CharField()
    name2 = forms.CharField()
    name3 = forms.CharField()
    email = forms.EmailField()

    CHOICES = [('select1', 'select 1'),
               ('select2', 'select 2'),
               ('select3', 'select 3')]
    like = forms.ChoiceField(choices=CHOICES,
                             widget=forms.RadioSelect(
                                 renderer=HorizontalRadioRenderer,
                                 attrs={
                                     'class': 'inline'
                                 }
                             ))

    text = forms.CharField(widget=forms.Textarea)
