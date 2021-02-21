from iconservice import *
from .ODIContracts.tokens.IRC2 import IRC2
from .ODIContracts.tokens.IRC2mintable import IRC2Mintable
from .ODIContracts.tokens.IRC2burnable import IRC2Burnable

TAG = 'SampleToken'

class SampleToken(IRC2Mintable, IRC2Burnable):
    pass
