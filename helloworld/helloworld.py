from iconservice import *
from iconsdk import *
from iconsdk.wallet.wallet import KeyWallet
from iconsdk.builder.transaction_builder import TransactionBuilder
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.icon_service import IconService
from iconsdk.signed_transaction import SignedTransaction

TAG = 'HelloWorld'
reserve = 10000


class HelloWorld(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()
    
    @external(readonly=True)
    def hello(self) -> str:
        wallet = KeyWallet.load("./iconkeystore", "@icon111")
        wallet2 = KeyWallet.load("./iconkeystore2", "@icon222")
        transaction = TransactionBuilder().from_(wallet.get_address()).to(
            'hxf79349933f569e0b60cd85d788cb31acef9a739b').value(1000000000000000000).step_limit(2000000).nid(3).nonce(
            100).build()
        icon_service = IconService(HTTPProvider("https://bicon.net.solidwallet.io/api/v3"))
        signed_transaction = SignedTransaction(transaction, wallet)
        tx_hash = icon_service.send_transaction(signed_transaction)
        print(tx_hash)
        balance = icon_service.get_balance(wallet2.get_address())
        print(balance)
        return('Transaction Complete')

