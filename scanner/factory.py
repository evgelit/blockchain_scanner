from scanner.scanner import Scanner

class ScannerFactory:

    @staticmethod
    def create(http_provider) -> Scanner:
        return Scanner(http_provider)