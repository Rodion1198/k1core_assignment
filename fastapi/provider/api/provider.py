from asgiref.sync import sync_to_async

from provider.models import Provider
from provider.schemas import ProviderSchema
from provider.serializers import ProviderSerializer


class ProviderAPI:

    @classmethod
    async def get_all(cls):
        providers = await sync_to_async(list)(Provider.objects.all())
        return [ProviderSchema.model_validate(ProviderSerializer(provider).data) for provider in providers]
