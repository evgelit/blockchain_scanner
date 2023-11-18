import os
from dotenv import load_dotenv
from scanner.factory import ScannerFactory
from pprint import pprint

load_dotenv()

scanner = ScannerFactory.create(os.getenv('PROVIDER'))
blocks_available = scanner.get_block_number()
print(f"{blocks_available} blocks available")
block_to_load = int(input("Select block to load: "))
scanner.load_block(block_to_load)

pprint(dict(scanner.data_provider.block.__dict__["_Block__block"]))

print(f"{len(scanner.data_provider.block.transactions)} transaction in block")
pool = int(input(f"Transaction pool size: "))
scanner.load_transaction(pool=pool)

for transaction in scanner.data_provider.transactions.values():
    pprint(dict(transaction.__dict__["_Transaction__transaction"]))
