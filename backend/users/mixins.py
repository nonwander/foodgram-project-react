from rest_framework import serializers
from rest_framework.serializers import Serializer

from users.models import Follow


class IsSubscribedMixin(Serializer):
    is_subscribed = serializers.SerializerMethodField()

    def get_is_subscribed(self, data):
        request = self.context.get('request')
        if request is None or request.user.is_anonymous:
            return False
        return Follow.objects.filter(
            author=data, user=self.context.get('request').user
        ).exists()
