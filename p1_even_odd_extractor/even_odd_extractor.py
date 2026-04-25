class OddEvenExtractor:
    def __init__(self, filename: str = "numbers.txt"):
        self.filename =  filename
        
    def read_file(self):
        with open(self.filename, 'r') as file:
            numbers = file.readlines()
            
        print(numbers)
        
OddEvenExtractor().read_file