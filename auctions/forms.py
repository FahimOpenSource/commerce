
from django.forms import ModelForm,Textarea
from .models import AuctionListing

class AuctionForm(ModelForm):
    class Meta:
        model = AuctionListing
        fields = ['title','url','description','price']
        widgets = { 'title': Textarea(attrs={'class': 'form-control'}) }
