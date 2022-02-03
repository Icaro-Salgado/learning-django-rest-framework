from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# The first part of the serializer class defines the fields that get serialized/deserialized.
# The create() and update() methods define how fully fledged instances are created or modified when calling serializer.save()


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style"]
