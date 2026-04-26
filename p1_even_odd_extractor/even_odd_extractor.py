import os
class OddEvenExtractor:
    def __init__(self, filename: str = "./numbers.txt"):
        self.filename =  filename
        
    def read_file(self) -> list[int]:
        try:
            with open(self.filename, 'r') as file:
                numbers = [int(number.rstrip("\n")) for number in file.readlines()]
    
            return numbers
        except:
            print("Make sure the file only contains integers.")
            
    def file_exists(self, file: str) -> bool:
        if not os.path.exists(file):
            return False
        return True
    
    def write_file(self, filename: str):
        pass
        
    def categorize(self):
        data = self.read_file()
        odd = []
        even = []
        for number in data:
            if number % 2 == 0:
                even.append
OddEvenExtractor().read_file()