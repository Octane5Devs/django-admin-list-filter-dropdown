from django.contrib.admin.filters import (
    SimpleListFilter,
    AllValuesFieldListFilter,
    ChoicesFieldListFilter,
    RelatedFieldListFilter,
    RelatedOnlyFieldListFilter
)


class SimpleDropdownFilter(SimpleListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'


class DropdownFilter(AllValuesFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'


class ChoiceDropdownFilter(ChoicesFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'


class RelatedDropdownFilter(RelatedFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'


class RelatedOnlyDropdownFilter(RelatedOnlyFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'


class SelectizeSimpleDropdownFilter(SimpleListFilter):
    template = 'django_admin_listfilter_dropdown/selectize_dropdown_filter.html'


class SelectizeDropdownFilter(AllValuesFieldListFilter):
    template = 'django_admin_listfilter_dropdown/selectize_dropdown_filter.html'


class SelectizeChoiceDropdownFilter(ChoicesFieldListFilter):
    template = 'django_admin_listfilter_dropdown/selectize_dropdown_filter.html'


class SelectizeRelatedDropdownFilter(RelatedFieldListFilter):
    template = 'django_admin_listfilter_dropdown/selectize_dropdown_filter.html'


class SelectizeRelatedOnlyDropdownFilter(RelatedOnlyFieldListFilter):
    template = 'django_admin_listfilter_dropdown/selectize_dropdown_filter.html'
