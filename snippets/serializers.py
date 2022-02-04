from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet

# The first part of the serializer class defines the fields that get serialized/deserialized.
# The create() and update() methods define how fully fledged instances are created or modified when calling serializer.save()


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(view_name="snippet-highlight", format="html")

    class Meta:
        model = Snippet
        fields = ["url", "id", "highlight", "owner", "title", "code", "linenos", "language", "style"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name="snippet-detail", read_only=True)

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]
