from scanner.block import Block
from scanner.transaction import Transaction
from web3.datastructures import AttributeDict


class DataProvider:

    __block: Block
    __transactions: {Transaction}

    @property
    def block(self) -> Block:
        return self.__block

    @block.setter
    def block(self, block: AttributeDict) -> None:
        self.__transactions = {}
        self.__block = Block(block)

    @property
    def transactions(self) -> {Transaction}:
        return self.__transactions

    @transactions.setter
    def transactions(self, transaction: AttributeDict) -> None:
        self.__transactions[transaction['hash']] = Transaction(transaction)
