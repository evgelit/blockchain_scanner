from web3 import Web3
from scanner.data_provider import DataProvider


class Scanner:

    __provider: Web3
    __data_provider: DataProvider = DataProvider()

    def __init__(
            self,
            http_provider: str
    ):
        self.__provider = Web3(Web3.HTTPProvider(http_provider))

    def get_block_number(self):
        return self.__provider.eth.get_block_number()

    def load_block(
            self,
            block_number: int = None
    ):
        self.__data_provider.block = self.__provider.eth.get_block(
            'latest' if block_number is None else block_number
        )

    def load_transaction(
            self,
            pool: int = 1,
            offset: int = 0
    ):
        for transaction_index in range(offset, pool + offset):
            transaction_entity = self.__provider.eth.get_transaction(
                self.__data_provider.block.transactions[transaction_index]
            )
            self.__data_provider.transactions = transaction_entity

    @property
    def data_provider(self) -> DataProvider:
        return self.__data_provider
