from modeltranslation.translator import register, TranslationOptions
from .models import ProfileUser


@register(ProfileUser)
class ProfileUserTranslationOptions(TranslationOptions):
    fields = ('first_name','about',)

