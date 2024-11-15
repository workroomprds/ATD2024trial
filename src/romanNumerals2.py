#!/usr/bin/env python3
def romanToArabic(roman_numeral):
    """Convert a Roman numeral to an Arabic number."""
    roman_values = {
        'I': 1,
    }
    return roman_values[roman_numeral]

def arabicToRoman(number):
    """Convert an Arabic number to a Roman numeral."""
    roman_symbols = [
        (1, 'I'),
    ]
    
    for value, symbol in roman_symbols:
        if number == value:
            return symbol
    return ""
