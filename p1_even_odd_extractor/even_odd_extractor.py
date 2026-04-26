import os
class OddEvenExtractor:
    def __init__(self, filename: str = "./numbers.txt"):
        self.filename =  filename
        
    def read_file(self):
        with open(self.filename, 'r') as file:
            numbers = [number.rstrip("\n") for number in file.readlines()]
            
        return numbers
    
    def file_exists(self, file: str):
        pass
    
    def write_file(self, filename: str):
        pass
        
    def categorize(self):
        pass
OddEvenExtractor().read_file()