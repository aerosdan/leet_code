from collections import OrderedDict

RomanToIntDict: OrderedDict = OrderedDict({
    "I": 1,
    "V": 5,
    "X": 10,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
})

class Solution:
    def romanToInt(self, roman_number: str) -> int:
        total = 0
        keys_list = list(RomanToIntDict.keys())
        for pos, letter in enumerate(roman_number):
            current_letter_position = keys_list.index(letter)
            letter_int_value = RomanToIntDict[letter]

            if pos+1 < len(roman_number):
                next_letter = roman_number[pos+1]
                next_letter_position = keys_list.index(next_letter)
                if current_letter_position < next_letter_position:

                    letter_int_value = -letter_int_value

            total+=letter_int_value

        return total

print(Solution().romanToInt('VI'))