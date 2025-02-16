from django.core.paginator import Paginator
from asgiref.sync import sync_to_async

from block.exceptions import BlockNotFoundException
from block.models import Block
from block.schemas import BlockSchema
from block.serializers import BlockSerializer


class BlockAPI:

    @classmethod
    async def get_blocks(
            cls,
            currency: str | None,
            provider: str | None,
            page: int,
            page_size: int,
    ):
        def fetch_blocks():
            queryset = Block.objects.select_related("currency", "provider").all()

            if currency:
                queryset = queryset.filter(currency__name__iexact=currency)

            if provider:
                queryset = queryset.filter(provider__name__iexact=provider)

            paginator = Paginator(queryset, page_size)
            current_page = paginator.get_page(page)

            return [BlockSchema.model_validate(BlockSerializer(block).data) for block in current_page]

        return await sync_to_async(fetch_blocks)()

    @classmethod
    async def get_block_by_currency_and_number(
            cls,
            currency: str,
            number: int,
    ):
        def fetch_blocks():
            block = Block.objects.filter(currency__name__iexact=currency, number=number).first()
            if not block:
                raise BlockNotFoundException()
            return BlockSchema.model_validate(BlockSerializer(block).data)

        return await sync_to_async(fetch_blocks)()

    @classmethod
    async def get_block_by_id(
            cls,
            block_id: int,
    ):
        def fetch_block():
            block = Block.objects.filter(id=block_id).first()
            if not block:
                raise BlockNotFoundException()
            return BlockSchema.model_validate(BlockSerializer(block).data)

        return await sync_to_async(fetch_block)()
