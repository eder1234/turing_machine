class TuringMachine:
    def __init__(self, input_string):
        self.tape = list(input_string) + ['B'] * 10  # Add some blank spaces
        self.head_position = 0

    def move_left(self):
        if self.head_position > 0:
            self.head_position -= 1

    def move_right(self):
        if self.head_position < len(self.tape) - 1:
            self.head_position += 1

    def read(self):
        return self.tape[self.head_position]

    def write(self, symbol):
        self.tape[self.head_position] = symbol

    def swap_adjacent(self):
        if self.head_position < len(self.tape) - 1:
            self.tape[self.head_position], self.tape[self.head_position + 1] = \
                self.tape[self.head_position + 1], self.tape[self.head_position]

    def display(self):
        tape_str = ''.join(self.tape).rstrip('B')
        return f"Tape: {tape_str}, Head at: {self.head_position}"

def is_valid_input(input_string):
    return len(input_string) == 6 and len(set(input_string)) == 6 and input_string.isdigit()

def main():
    while True:
        input_string = input("Enter 6 unique digits (0-9): ")
        if is_valid_input(input_string):
            break
        print("Invalid input. Please enter 6 unique digits.")

    tm = TuringMachine(input_string)
    print(tm.display())

    while True:
        command = input("Enter command (L: Left, R: Right, W: Write, S: Swap, Q: Quit): ").upper()
        
        if command == 'L':
            tm.move_left()
        elif command == 'R':
            tm.move_right()
        elif command == 'W':
            symbol = input("Enter symbol to write: ")
            if len(symbol) == 1 and symbol.isdigit():
                tm.write(symbol)
            else:
                print("Invalid symbol. Please enter a single digit.")
        elif command == 'S':
            tm.swap_adjacent()
        elif command == 'Q':
            break
        else:
            print("Invalid command.")
        
        print(tm.display())

    print("Final state:", tm.display())

if __name__ == "__main__":
    main()
