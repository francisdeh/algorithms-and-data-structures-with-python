"""
You’ve decided to save up for a new phone, by putting aside money daily into a money pot.
You want to choose a starting value, and every day put in the same amount you put in the day before,
plus the starting value, until you reach a maximum amount you aren’t comfortable putting in.
You decide to write a program which, given a starting value and a maximum value,
calculates the amount of money you have saved.
starting value: **2** max value: **9**  -> 2 + 4 + 6 + 8 = 20
"""


def calculate_amount_saved(mn, mx):
    if mx < mn: raise ValueError("Min is less than Max")
    if mn < 0 or mx < 0: raise ValueError("Min and Max cannot be less than 0")
    current_value = mn
    savings_list = [mn]  # starting value
    while current_value < mx:
        current_value = mn + savings_list[-1]
        if current_value < mx:
            savings_list.append(current_value)
    print(savings_list)
    return sum(savings_list)


print(calculate_amount_saved(2, 9))

"""
## A2. Reversed Words
NASA has established a line of communication with aliens. 
The only problem is the aliens seem to only understand sentences, 
if they’re said backwards. Help NASA contact the aliens by writing a 
program which reverses the order of the words in a sentence.
For example:

"The greatest victory is that which requires no battle"
 -> "battle no requires which that is victory greatest The"
"""


def speak_to_aliens(sentence):
    return " ".join(sentence.split(" ")[::-1])


print(speak_to_aliens("The greatest victory is that which requires no battle"))
