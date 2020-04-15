from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes two additional arguments
    `fields` that controls which fields should be displayed.
    `exclude_fields` that controls which fields to be excluded.
    href: https://www.django-rest-framework.org/api-guide/serializers/#dynamically-modifying-fields
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)
        exclude_fields = kwargs.pop("exclude_fields", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude_fields is not None:
            # Drop any fields that are specified in the `exclude_fields` argument.
            exclude = set(exclude_fields)
            existing = set(self.fields)
            for field_name in existing.intersection(exclude):
                self.fields.pop(field_name)
