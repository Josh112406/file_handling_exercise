class HighestGWA:
    def __init__(self, filename: str = "gwa.txt"):
        self.filename = filename
        
    def read_file(self) -> list[str]:
        with open(self.filename, 'r') as file:
            content = [line.rstrip("\n") for line in file.readlines()]
        return content