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


class ChosenSimpleDropdownFilter(SimpleListFilter):
    template = 'django_admin_listfilter_dropdown/chosen_dropdown_filter.html'


class ChosenDropdownFilter(AllValuesFieldListFilter):
    template = 'django_admin_listfilter_dropdown/chosen_dropdown_filter.html'


class ChosenChoiceDropdownFilter(ChoicesFieldListFilter):
    template = 'django_admin_listfilter_dropdown/chosen_dropdown_filter.html'


class ChosenRelatedDropdownFilter(RelatedFieldListFilter):
    template = 'django_admin_listfilter_dropdown/chosen_dropdown_filter.html'


class ChosenRelatedOnlyDropdownFilter(RelatedOnlyFieldListFilter):
    template = 'django_admin_listfilter_dropdown/chosen_dropdown_filter.html'
