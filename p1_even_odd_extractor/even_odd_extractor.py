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
    
    def write_file(self, filename: str, content: int):
        if not self.file_exists(filename):
            with open(filename, 'w') as file:
                file.write(f"{content}\n")
        else:
            with open(filename, 'w') as file:
                file.write(f"{content}\n")
                
    def categorize(self):
        data = self.read_file()
        for number in data:
            if number % 2 == 0:
                self.write_file("even.txt", number)
            else:
                self.write_file("even.txt", number)
                
OddEvenExtractor().read_file()