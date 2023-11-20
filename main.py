import os
from dotenv import load_dotenv
from scanner.factory import ScannerFactory
from pprint import pprint

load_dotenv()


def main():
    scanner = ScannerFactory.create(os.getenv('PROVIDER'))
    scanner.load_contract("0x49d1e0F45b5293eff9B1EfD04BfCACfE028F010C")
    return
    blocks_available = scanner.get_block_number()
    print(f"{blocks_available} blocks available")
    block_to_load = int(input("Select block to load: "))
    scanner.load_block(block_to_load)
    pprint(scanner.data_provider.block.to_dict())
    print(f"{len(scanner.data_provider.block.transactions)} transaction in block")
    pool = int(input(f"Transaction pool size: "))
    scanner.load_transaction(pool=pool)
    #for transaction in scanner.data_provider.transactions.values():
        #pprint(transaction.to_dict())


if __name__ == "__main__":
    main()
