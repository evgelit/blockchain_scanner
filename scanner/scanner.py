from web3 import Web3
from scanner.data_provider import DataProvider
import json
from pprint import pprint


class Scanner:

    __provider: Web3
    __data_provider: DataProvider = DataProvider()

    def __init__(
            self,
            http_provider: str
    ):
        self.__provider = Web3(Web3.HTTPProvider(http_provider))

    def get_block_number(self) -> int:
        return self.__provider.eth.get_block_number()

    def load_block(
            self,
            block_number: int = None
    ) -> None:
        self.__data_provider.block = self.__provider.eth.get_block(
            'latest' if block_number is None else block_number
        )

    def load_transaction(
            self,
            pool: int = 1,
            offset: int = 0
    ) -> None:
        for transaction_index in range(offset, pool + offset):
            transaction_entity = self.__provider.eth.get_transaction(
                self.__data_provider.block.transactions[transaction_index]
            )
            receipt = self.__provider.eth.get_transaction_receipt(self.__data_provider.block.transactions[transaction_index])

            print(self.__data_provider.block.transactions[transaction_index], receipt['contractAddress'])
            self.__data_provider.transactions = transaction_entity

    def load_contract(
            self, hash
    ) -> None:

        with open('erc20_abi.json') as abi_file:
            abi = json.load(abi_file)
        contract_entity = self.__provider.eth.contract(hash, abi=abi)
        pprint(contract_entity.functions.__dict__)

    @property
    def data_provider(self) -> DataProvider:
        return self.__data_provider
