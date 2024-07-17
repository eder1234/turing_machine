# TuringTerminal

TuringTerminal is a Python-based simulation of a Turing machine that allows users to manipulate a tape of digits through terminal commands. This project provides an interactive way to understand the basic concepts of Turing machines and computational theory.

## Features

- Initialize a Turing machine with 6 unique digits
- Manipulate the tape using simple commands:
  - Move left
  - Move right
  - Read current cell
  - Write to current cell
  - Swap adjacent cells
- Real-time display of the tape state and head position

## Requirements

- Python 3.6+

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/TuringTerminal.git
```
2. Navigate to the project directory:
```
cd TuringTerminal
```

## Usage

Run the script:
```
python turing_terminal.py
```
Follow the prompts to:
1. Enter 6 unique digits to initialize the tape
2. Input commands to manipulate the Turing machine

### Commands

- `L`: Move the head left
- `R`: Move the head right
- `W`: Write a digit to the current cell
- `S`: Swap the current cell with the next cell
- `Q`: Quit the program

## Example
```
Enter 6 unique digits (0-9): 045672
Tape: 045672, Head at: 0
Enter command (L: Left, R: Right, W: Write, S: Swap, Q: Quit): R
Tape: 045672, Head at: 1
Enter command (L: Left, R: Right, W: Write, S: Swap, Q: Quit): S
Tape: 054672, Head at: 1
Enter command (L: Left, R: Right, W: Write, S: Swap, Q: Quit): W
Enter symbol to write: 9
Tape: 094672, Head at: 1
Enter command (L: Left, R: Right, W: Write, S: Swap, Q: Quit): Q
Final state: Tape: 094672, Head at: 1
```
## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/eder1234/TuringTerminal/issues) if you want to contribute.

## License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.
