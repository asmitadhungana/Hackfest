from iconservice import *

TAG = 'Iku'

class TokenStandard(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def symbol(self) -> str:
        pass

    @abstractmethod
    def balanceOf(self, _owner: Address) -> int:
        pass

    @abstractmethod
    def ownerOf(self, _tokenId: str) -> Address:
        pass

    @abstractmethod
    def getApproved(self, _tokenId: str) -> Address:
        pass

    @abstractmethod
    def approve(self, _to: Address, _tokenId: str):
        pass

    @abstractmethod
    def transfer(self, _to: Address, _tokenId: str):
        pass

    @abstractmethod
    def transferFrom(self, _from: Address, _to: Address, _tokenId: str):
        pass



class Iku(IconScoreBase, TokenStandard):
    _TOKEN_OWNER = "token_owner"
    _OWNER_TOKEN_COUNT = "owner_token_list"
    _TOKENS = "tokens"
    _TOKEN_APPROVALS = "token_approvals"
    _TOKEN_ID_LIST = "token_id_list"

    _SUPER_ADMIN = "super_admin"
    _ADMIN_LIST = "admin_list"

    _DISTRIBUTOR_SCORE = "distributor_score"
    _PROGRESS_SCORE = "progress_score"

    _ZERO_ADDRESS = Address.from_prefix_and_int(AddressPrefix.EOA, 0)

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()
    
    @external(readonly=True)
    def hello(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return "Hello"
