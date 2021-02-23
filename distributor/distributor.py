from iconservice import *

TAG = 'Distributor'

class IkuTokenInterface(InterfaceScore):
    @interface 
    def ownerOf(self, _tokenId: str) -> Address:
        pass
    @interface
    def get_token(self, _tokenId: str) -> dict:
        pass

    @interface
    def get_tokens_of_owner(self, _address: str) -> list:
        pass

    @interface
    def update_token(self, _gene: str, _name: str, _price: str, _tokenId: str):
        pass

    @interface
    def approve(self, _to: Address, _tokenId: str):
        pass

    @interface
    def transfer(self, _to: Address, _tokenId: str):
        pass

class CaveTokenInterface(InterfaceScore):
    @interface
    def ownerOf(self, _tokenId: str) -> Address:
        pass

    @interface
    def get_token(self, _tokenId: str) -> dict:
        pass

    @interface
    def get_tokens_of_owner(self, _address: str) -> list:
        pass

    @interface
    def update_token(self, _gene: str, _name: str, _price: str, _tokenId: str):
        pass

    @interface
    def approve(self, _to: Address, _tokenId: str):
        pass

    @interface
    def transfer(self, _to: Address, _tokenId: str):
        pass

    @interface
    def add_horse_to_stable(self, _horseId, _tokenId):
        pass


class Distributor(IconScoreBase):
    #Contributors will buy an NFT(iku) if they want to contribute at first

    _BUY_REQUESTS_DETAILS = "buy_requests_details"
    _IKU_BUY_REQUESTS = "iku_buy_requests"

    _IKU_SELL_REQUESTS = "iku_sell_requests"
    
    _SELL_REQUESTS_SELLER = "sell_request_seller"
    _SELL_REQUESTS_PRICE = "sell_request_price"

    _CANCEL_IKU_SELL = "cancel_iku_sell"

    _IKU_SCORE = "iku_score"
    _ZERO_ADDRESS = Address.from_prefix_and_int(AddressPrefix.EOA, 0)

    @eventlog(indexed=3)
    def BuyRequest(self, _tokenId: str, _tokenType: str, _price: int, _buyer: Address):
        pass

    @eventlog(indexed=3)
    def SellRequest(self, _tokenId: str, _tokenType: str, _price: int, _seller: Address):
        pass

    @eventlog(indexed=3)
    def PaymentTransfer(self, _from: Address, _to: Address, _amount: int, _details: str):
        pass


    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._buy_requests_details = DictDB(self._BUY_REQUESTS_DETAILS, db, value_type=Address, depth=2)
        self._iku_buy_requests = ArrayDB(self._IKU_BUY_REQUESTS, db, value_type=str)

        self._iku_sell_requests = ArrayDB(self._IKU_SELL_REQUESTS, db, value_type=str)
        self._sell_requests_price = DictDB(self._SELL_REQUESTS_PRICE, db, value_type=int, depth=2)
        self._sell_requests_seller = DictDB(self._SELL_REQUESTS_SELLER, db, value_type=Address, depth=2)

        self._cancel_iku_sell = ArrayDB(self._CANCEL_IKU_SELL, db, value_type=str)

        self._iku_score = VarDB(self._IKU_SCORE, db, value_type=Address)


    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()
    
     @external()
    def set_token_address(self, _address: Address, _token: str):
        if self.msg.sender != self.owner:
            revert("Token address set error:You are not authorized,only owner can set the address")
        if _token == "iku":
            self._iku_score.set(_address)
        else:
            revert("Token address set error: Not a valid token name ")

    @external(readonly=True)
    def get_iku_score_address(self):
        return self._iku_score.get()

    @external(readonly=True)
    def get_buy_requests(self) -> dict:
        iku = []
        cave = []
        for ikuId in self._iku_buy_requests:
            iku.append(ikuId)
        for caveId in self._cave_buy_requests:
            cave.append(caveId)
        return {"iku": iku, "cave": cave}

    @external(readonly=True)
    def get_sell_requests(self) -> dict:
        iku = []
        cave = []
        for ikuId in self._iku_sell_requests:
            iku.append(ikuId)
        for caveId in self._cave_sell_requests:
            cave.append(caveId)
        return {"iku": iku, "cave": cave}

    @external(readonly=True)
    def get_iku_sell_details(self):
        req = {}
        for ikuId in self._iku_sell_requests:
            price = self._sell_requests_price[ikuId]["iku"]
            seller = self._sell_requests_seller[ikuId]["iku"]
            req[ikuId] = {"price": price, "seller": seller}
        return req

