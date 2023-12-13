from dataclasses import dataclass
from enum import IntEnum, auto


"""
#######################################
ENTITIES
#######################################
"""
class Digit(IntEnum):
    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()

@dataclass
class Line:
    digits: list[Digit]
    original_string: str

@dataclass
class Document:
    lines: list[Line]


"""
#######################################
SYSTEMS
#######################################
"""
def create_digit(character: str) -> Digit:
    for digit in Digit:
        if digit == int(character):
            return digit
    raise NotImplementedError(f"{character=} is not a valid value")

def is_digit_in_string(string: str) -> bool:
    for char in string:
        if char.isdigit():
            return True
    return False

def create_line(raw_line: str) -> Line:
    original_string = raw_line
    if PROBLEM_NUMBER == 2:
        parsed_raw_line = ""
        while len(raw_line) > 0:
            for digit_name in get_digit_strings():
                if raw_line.startswith(digit_name.lower()):
                    parsed_raw_line += str(Digit[digit_name])
            if raw_line[0].isdigit():
                parsed_raw_line += raw_line[0]
            raw_line = raw_line[1:]
        raw_line = parsed_raw_line
    digits: list[Digit] = []
    for character in raw_line:
        if character.isdigit():
            digits.append(create_digit(character))
    return Line(digits, original_string)

def create_document(raw_document: list[str]) -> Document:
    lines: list[Line] = []
    for raw_line in raw_document:
        lines.append(create_line(raw_line))
    return Document(lines)

def get_calibration_number(line: Line) -> int:
    tens = line.digits[0] * 10
    units = line.digits[-1]
    return tens + units

def get_calibration_sum(lines_values: list[int]) -> int:
    return sum(lines_values)

def get_digit_strings() -> list[str]:
    digit_names: list[str] = []
    for digit_value in Digit:
        digit_names.append(digit_value.name)
    return digit_names

def print_line(line: Line) -> None:
    print(f"{line.original_string} - {str(line.digits)}")


"""
#######################################
SOLUTION
#######################################
"""
PROBLEM_NUMBER: int = 2

def main() -> None:
    with open(r"Advent of code\days\1\input.txt", mode="r", encoding="utf-8") as file:
        raw_document: list[str] = file.read().split("\n")
        document = create_document(raw_document)
    lines_values: list[int] = []
    for line in document.lines:
        lines_values.append(get_calibration_number(line))
    print(get_calibration_sum(lines_values))

if __name__ == "__main__":
    main()
