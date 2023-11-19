from web3.types import HexBytes
from web3.datastructures import AttributeDict


class Transaction:

    def __init__(self, transaction: AttributeDict):
        self.__transaction = transaction

    @property
    def access_list(self) -> list:
        return self.__transaction['accessList']

    @property
    def block_hash(self) -> HexBytes:
        return self.__transaction['blockHash']

    @property
    def chain_id(self) -> int:
        return self.__transaction['chainId']

    @property
    def from_(self) -> str:
        return self.__transaction['from']

    @property
    def gas(self) -> int:
        return self.__transaction['gas']

    @property
    def gas_price(self) -> int:
        return self.__transaction['gasPrice']

    @property
    def hash(self) -> HexBytes:
        return self.__transaction['hash']

    @property
    def input(self) -> HexBytes:
        return self.__transaction['input']

    @property
    def max_fee_per_gas(self) -> int:
        return self.__transaction['maxFeePerGas']

    @property
    def max_priority_fee_per_gas(self) -> int:
        return self.__transaction['maxPriorityFeePerGas']

    @property
    def nonce(self) -> int:
        return self.__transaction['nonce']

    @property
    def r(self) -> HexBytes:
        return self.__transaction['r']

    @property
    def s(self) -> HexBytes:
        return self.__transaction['s']

    @property
    def to(self) -> str:
        return self.__transaction['to']

    @property
    def transaction_index(self) -> int:
        return self.__transaction['transactionIndex']

    @property
    def type(self) -> int:
        return self.__transaction['type']

    @property
    def v(self) -> int:
        return self.__transaction['v']

    @property
    def value(self) -> int:
        return self.__transaction['value']

    @property
    def y_parity(self) -> int:
        return self.__transaction['y_parity']

    def to_dict(self) -> dict:
        return dict(self.__transaction)

    def raw(self) -> AttributeDict:
        return self.__transaction
