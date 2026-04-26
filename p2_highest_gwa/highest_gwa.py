class HighestGWA:
    def __init__(self, filename: str = "gwa.txt"):
        self.filename = filename
        
    def read_file(self) -> list[str]:
        with open(self.filename, 'r') as file:
            content = [line.rstrip("\n") for line in file.readlines()]
        return content
    
    def get_highest(self, data: list):
        new_data = [info.split(",") for info in data]
        highest_gwa = max(new_data, key = lambda x: x[1])
        print(f"Highest GWA\nStudent: {highest_gwa[0]}\nGWA: {highest_gwa[1]}")
