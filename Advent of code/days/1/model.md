their calibration document has been amended, the Elves are having trouble reading the values on the document.

The calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?



---------------------------------------------------------------------------------------------------------------------------


ENTITIES
    - Document
        - Line (>=1)
            - Chunk (1>=)
                - Alfa (>=0)
                    - a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z (1)
                - Digit (>=1)
                    - 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 (1)

SYSTEMS
    - get_calibration_number(_: Line) -> int
    - get_calibration_sum(_: list\[int\]) -> int
