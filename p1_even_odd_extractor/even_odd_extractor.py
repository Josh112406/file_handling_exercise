class OddEvenExtractor:
    def __init__(self, filename: str = "./numbers.txt"):
        self.filename =  filename
        
    def read_file(self):
        with open(self.filename, 'r') as file:
            numbers = [number.rstrip("\n") for number in file.readlines()]
            
        return numbers
    
    
        
OddEvenExtractor().read_file()