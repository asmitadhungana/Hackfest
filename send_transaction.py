from iconsdk.utils.convert_type import convert_hex_str_to_int
from iconsdk.wallet.wallet import KeyWallet
wallet = KeyWallet.load("./iconkeystore", "@icon111")
print(f"Private key wallet1: ", wallet.get_private_key())

wallet2 = KeyWallet.load("./iconkeystore2", "@icon222")
print(f"Private key wallet2:", wallet2.get_private_key())
from iconsdk.builder.transaction_builder import (TransactionBuilder, DeployTransactionBuilder, CallTransactionBuilder, MessageTransactionBuilder)
from iconsdk.signed_transaction import SignedTransaction

transaction = TransactionBuilder().from_(wallet.get_address()).to('hxf79349933f569e0b60cd85d788cb31acef9a739b').value(1000000000000000000).step_limit(2000000).nid(3).nonce(100).build()
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
icon_service = IconService(HTTPProvider("https://bicon.net.solidwallet.io/api/v3"))
signed_transaction = SignedTransaction(transaction, wallet)
tx_hash = icon_service.send_transaction(signed_transaction)
print(f"tx_hash: {tx_hash}")
balance = icon_service.get_balance(wallet2.get_address())
print(balance)
balance2 = icon_service.get_balance(wallet2.get_address())
print(balance2)
block = icon_service.get_block(1209)
print(f"block at 1209: {block}")
block = icon_service.get_block('latest')
print(f"latest block: {block}")
print(f"Balance at: {wallet.get_address()}: {icon_service.get_balance(wallet.get_address())}")
print(f"Balance at: {wallet2.get_address()}: {icon_service.get_balance(wallet2.get_address())}")
"""
wallet 2 balance: 2023000000000000000000
wallet 2 balance: 2023000000000000000000
block at 1209: {'version': '0.3', 'height': 1209, 'signature': 'yVwnabn5cXjvkDaCZxZWN5CahIQkgRt+HO7Ze4dDpHQE7VpnSj+5l5MN/7PyKL+WFBN1QxNumCCOchZwarJZCwE=', 'prev_block_hash': 'fa597afab3cc68f67da029f1c48df0f8f8767fd902033a6e36dd4909eeae5dbe', 'merkle_tree_root_hash': '0000000000000000000000000000000000000000000000000000000000000000', 'time_stamp': 1586160194702160, 'confirmed_transaction_list': [], 'block_hash': 'f9f9aa954a567d7798fcbd51d1724660091ee1c0e6fb799fc548838c9d47f37c', 'peer_id': 'hxec79e9c1c882632688f8c8f9a07832bcabe8be8f', 'next_leader': 'hxec79e9c1c882632688f8c8f9a07832bcabe8be8f'}
latest block: {'version': '0.5', 'height': 13281515, 'signature': 'IDFEjPiSlb8gtTWq1vID7f8zwDMC09j6t/4c/OR9MnFOrlDs2jp6mXo1OAWmA+HIh7ogzIZEBCJzR+MAeeO7OwE=', 'prev_block_hash': 'ace622c9f9945f746303db3217a2797d7950bd09eb0162c23d8121722d966d25', 'merkle_tree_root_hash': 'af84f711b737a30f68083a87e32b8b92625d4ddc3ba1184ed1302094eabc5fe3', 'time_stamp': 1613892310788533, 'confirmed_transaction_list': [{'version': 3, 'timestamp': 1613892310788533, 'dataType': 'base', 'data': {'prep': {'irep': '0xa968163f0a57b400000', 'rrep': '0x321', 'totalDelegation': '0x6cb4838e14918ea9d6be51', 'value': '0x3805611404167c65'}, 'result': {'coveredByFee': '0x0', 'coveredByOverIssuedICX': '0x0', 'issue': '0x3805611404167c65'}}, 'txHash': '0xaf84f711b737a30f68083a87e32b8b92625d4ddc3ba1184ed1302094eabc5fe3'}], 'block_hash': '6a59e8bfd59a9d36e0fae4f0061432fccfc1b4a4065d9aedda9536ecf94af834', 'peer_id': 'hxaad52424d4aec9dac7d9f6796da527f471269d2c', 'next_leader': 'hxaad52424d4aec9dac7d9f6796da527f471269d2c'}
Balance at: hxff54214b12f771f0515afe4c0a7d3742a74fb380: 1918946057600000000000
Balance at: hxf79349933f569e0b60cd85d788cb31acef9a739b: 2024000000000000000000
"""
total_supply = icon_service.get_total_supply()
print(f"total_supply: { total_supply }")
tx = icon_service.get_transaction('0xffa6738ffe34aa22b7ae245ef68b32d0ca594b5a7503b856f98f0818f6c03098')
print(f"transaction information: {tx}")
tx_result = icon_service.get_transaction_result(tx_hash)
print(f"transaction status: {tx_result['status']}")
print(f"transaction result: {tx_result}")
