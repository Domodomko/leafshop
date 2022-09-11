from modeltranslation.translator import translator, TranslationOptions
from shop.models import Category, Product, AboutTeaContent, ShopPolicy


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )
    required_languages = ('en', 'ru')


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
    required_languages = ('en', 'ru')


class AboutTeaContentTranslationOptions(TranslationOptions):
    fields = ('about_tea', 'camelia', 'names_of_tea', 'black_tea', 'green_tea')
    required_languages = ('en', 'ru')


class ShopPolicyTranslationOptions(TranslationOptions):
    fields = ('term_of_service', 'shipping_policy', 'return_policy', 'privacy_policy')
    required_languages = ('en', 'ru')


translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(AboutTeaContent, AboutTeaContentTranslationOptions)
translator.register(ShopPolicy, ShopPolicyTranslationOptions)
