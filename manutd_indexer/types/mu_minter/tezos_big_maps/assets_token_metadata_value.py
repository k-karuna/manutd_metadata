# generated by DipDup 8.0.0b4

from __future__ import annotations

from typing import Any
from typing import Dict

from pydantic import BaseModel, ConfigDict

from manutd_indexer.models import TEZOS_STORAGE_PREFIX
from manutd_indexer.models import TokenMetadataBigMapModelMixin


class AssetsTokenMetadataValue(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    token_id: str
    token_info: Dict[str, str]

    def get_field_dto(self) -> Dict[str, Any]:
        name = TokenMetadataBigMapModelMixin.metadata_key.model_field_name
        value = self.token_info.get('')
        try:
            value = bytes.fromhex(value).decode()
        except ValueError:
            pass

        return {name: value.removeprefix(TEZOS_STORAGE_PREFIX)}
