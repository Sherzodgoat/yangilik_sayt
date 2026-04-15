from django import forms
from news_app.models import Contact, News, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']  # faqat comment text


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'