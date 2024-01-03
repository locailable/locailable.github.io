from django.db.models.base import Model
#from django.forms import ModelForm, widgets
from django import forms
from .models import Business, BusinessOwner, Availability, Review

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['owner', 'business_name', 'featured_image', 'address', 'availability']
#        widgets = {
#            'tags': forms.CheckboxSelectMultiple(),
#        }

#    def __init__(self, *args, **kwargs):
#        super(BusinessForm, self).__init__(*args, **kwargs)
#
#        for name, field in self.fields.items():
#            field.widget.attrs.update({'class': 'input'})


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['business', 'body', 'value']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['business', 'available_tables']



#    def __init__(self, *args, **kwargs):
#        super(ReviewForm, self).__init__(*args, **kwargs)
#
#        for name, field in self.fields.items():
#            field.widget.attrs.update({'class': 'input'})





#class BusinessOwnerForm(forms.ModelForm):
#    class Meta:
#        model = BusinessOwner
#        fields = ['user', 'bio', 'business']



