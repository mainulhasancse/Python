from rest_framework.fields import (
    CharField,
    DateField,
    EmailField,
    IntegerField,
    SlugField,
    URLField
)

from rest_framework.serializers import Serializer

class TagSerializer(Serializer):
    """Serialize Tag data"""

    id = IntegerField(read_only=True)
    name = CharField(max_length=31)
    slug = SlugField(max_length=31, allow_blank=True)

class StartupSerializer(Serializer):
    """Serialize Startup data"""

    id = IntegerField(read_only=True)
    name = CharField(max_length=31)
    slug = SlugField(max_length=31)
    description = CharField()
    founded_date = DateField()
    contact = EmailField()
    website = URLField(max_length=255)
    tags = TagSerializer(many=True)

class NewsLinkSerializer(Serializer):
    """Serialize NewsLink data"""

    id = IntegerField(read_only=True)
    title = CharField(max_length=63)
    slug = SlugField(max_length=63)
    pub_date = DateField()
    link = URLField(max_length=255)
    startup = StartupSerializer()

