from scanner.block import Block
from scanner.transaction import Transaction


class DataProvider:

    __block: Block
    __transactions: {Transaction}

    @property
    def block(self) -> Block:
        return self.__block

    @block.setter
    def block(self, block: Block) -> None:
        self.__transactions = {}
        self.__block = block

    @property
    def transactions(self) -> {Transaction}:
        return self.__transactions

    @transactions.setter
    def transactions(self, transaction: Transaction) -> None:
        self.__transactions[transaction.hash] = transaction
