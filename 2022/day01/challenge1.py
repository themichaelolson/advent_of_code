# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
def main(i: str) -> int:
    return max(map(lambda c: sum(map(int, c.split("\n"))), i.split("\n\n")))

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(main(f.read()))
