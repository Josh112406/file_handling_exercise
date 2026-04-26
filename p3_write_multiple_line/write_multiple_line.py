class WriteMulipleLines:
    def __init__(self, filename: str = "mylife.txt"):
        self.filename = filename
        
    def write_multiple_lines(self):
        try: 
            with open(self.filename, "a") as file:
                while True:
                    text = input("Enter line: ")
                    more = input("Are there more lines (y/n)? ")
                    
                    file.write(f"{text}\n")
                    if more != "y":
                        break
                    
        except:
            print("Error writing to file.")
            
