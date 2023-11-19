from web3.types import HexBytes
from web3.datastructures import AttributeDict


class Block:

    def __init__(self, block: AttributeDict):
        self.__block = block

    @property
    def base_fee_per_gas(self) -> int:
        return self.__block['baseFeePerGas']

    @property
    def difficulty(self) -> int:
        return self.__block['difficulty']

    @property
    def extra_data(self) -> HexBytes:
        return self.__block['extraData']

    @property
    def gas_limit(self) -> int:
        return self.__block['gasLimit']

    @property
    def gas_used(self) -> int:
        return self.__block['gasUsed']

    @property
    def hash(self) -> HexBytes:
        return self.__block['hash']

    @property
    def logs_bloom(self) -> HexBytes:
        return self.__block['logsBloom']

    @property
    def miner(self) -> str:
        return self.__block['miner']

    @property
    def nonce(self) -> HexBytes:
        return self.__block['nonce']

    @property
    def number(self) -> int:
        return self.__block['number']

    @property
    def parent_hash(self) -> HexBytes:
        return self.__block['parentHash']

    @property
    def receipts_root(self) -> HexBytes:
        return self.__block['receiptsRoot']

    @property
    def sha_3_uncles(self) -> HexBytes:
        return self.__block['sha3Uncles']

    @property
    def size(self) -> int:
        return self.__block['size']

    @property
    def state_root(self) -> HexBytes:
        return self.__block['stateRoot']

    @property
    def timestamp(self) -> HexBytes:
        return self.__block['timestamp']

    @property
    def total_difficulty(self) -> HexBytes:
        return self.__block['totalDifficulty']

    @property
    def transactions(self) -> [HexBytes]:
        return self.__block['transactions']

    @property
    def transactions_root(self) -> HexBytes:
        return self.__block['transactionsRoot']

    @property
    def uncles(self) -> list:
        return self.__block['uncles']

    @property
    def withdrawals(self) -> list:
        return self.__block['withdrawals']

    @property
    def withdrawals_root(self) -> HexBytes:
        return self.__block['withdrawalsRoot']

    def to_dict(self) -> dict:
        return dict(self.__block)

    def raw(self) -> AttributeDict:
        return self.__block
