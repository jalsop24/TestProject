
import csv
from pathlib import Path

file_path = Path("./partnerize.csv")

# Set object only contain unique elements
# Has O(1) lookup time
categories = set()

# __name__ keeps track of how the code in this file is being run. Is it being run directly or via import?
print(f"{__name__=}")

# Type annotations - not necessary but very useful
def func(arg: str) -> str:
    return arg

def main():
    print("this is main")

    # Path objects have many useful methods such as is_file()
    if not file_path.is_file():
        # f-strings allow for easy string formatting
        print(f"could not find file at {file_path}")
        return
    
    # Explicitly define encoding as otherwise open uses the system default (which isn't utf-8 on windows!)
    # newline = "" is recommended if you are to use a csv reader 
    with open(file_path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            categories.add(row["category"])

    print(len(categories))

if __name__ == "__main__":
    main()
