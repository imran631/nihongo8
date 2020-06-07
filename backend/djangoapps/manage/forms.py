import logging

from django import forms
from django.utils.translation import gettext_lazy as _

from backend.models import JLPT_SEARCH_CHOICES, TYPE_SEARCH_CHOICES, QUIZ_SEARCH_CHOICES

logger = logging.getLogger(__name__)


class WordForm(forms.Form):

    WORD_SEARCH_CHOICES = [
        ('kanji', _('Kanji')),
        ('hiragana', _('Hiragana')),
        ('katakana', _('Katakana')),
        ('hangul', _('Hangul')),
    ]

    level = forms.ChoiceField(
        choices=JLPT_SEARCH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control custom-select'
        })
    )

    type = forms.ChoiceField(
        choices=TYPE_SEARCH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control custom-select'
        })
    )

    search_type = forms.ChoiceField(
        choices=WORD_SEARCH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control custom-select'
        })
    )

    search_text = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': ""
        })
    )


class QuizForm(forms.Form):

    WORD_SEARCH_CHOICES = [
        ('quiz', _('Quiz')),
        ('hangul', _('Hangul')),
        ('right_answer', _('Right answer')),
        ('point', _('Point')),
    ]

    level = forms.ChoiceField(
        choices=JLPT_SEARCH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control custom-select'
        })
    )

    type = forms.ChoiceField(
        choices=QUIZ_SEARCH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control custom-select'
        })
    )

    search_type = forms.ChoiceField(
        choices=WORD_SEARCH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control custom-select'
        })
    )

    search_text = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': ""
        })
    )


class ProblemForm(forms.Form):

    WORD_SEARCH_CHOICES = [
        ('title', _('Title')),
        ('content', _('Content')),
    ]

    DIFFICULT_SEARCH_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]

    level = forms.ChoiceField(
        choices=JLPT_SEARCH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control custom-select'
        })
    )

    type = forms.ChoiceField(
        choices=QUIZ_SEARCH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control custom-select'
        })
    )

    difficult = forms.ChoiceField(
        choices=DIFFICULT_SEARCH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control custom-select'
        })
    )

    search_type = forms.ChoiceField(
        choices=WORD_SEARCH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control custom-select'
        })
    )

    search_text = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': ""
        })
    )