class ProcessIntegers:
    def __init__(self, filename:str = "numbers.txt"):
        self.filename = filename
        self.odd_filename = "triple.txt"
        self.even_filename = "double.txt"
        
    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                return file.readlines()
        except:
            print("File can't be opened.")
    
    def write_file(self, filename:str, content:str):
        with open(filename, "a") as file:
            file.write(f"{str(content)}\n")
            
    def process_file(self, data: list) -> list[int]:
        return [int(line.rstrip("\n")) for line in data]
        
    def process_integers(self):
        data = self.read_file()
        numbers = self.process_file(data)
        for number in numbers:
            if number % 2 == 0:
                self.write_file(self.even_filename, number ** 2)
            else:
                self.write_file(self.odd_filename, number ** 3)

if __name__ == "__main__":
    process = ProcessIntegers()
    process.process_integers()