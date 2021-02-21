from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
icon_service = IconService(HTTPProvider("http://localhost:9000", 3))
block = icon_service.get_block(1209)