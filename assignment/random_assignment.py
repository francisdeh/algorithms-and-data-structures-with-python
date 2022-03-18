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

"""
## B5. Padding

Your colleague has recently started ice-skating, and after an injury, has become obsessed with padding his clothes in order to prevent future injuries. His padding obsession has become so severe, that all the documents you write together must also be padded. 

For every sentence, each word must be padded with enough spaces on each side, that each word has the same amount of characters as the longest word in that sentence.

```
'let's pad this sentence'
'  let's    pad    this  sentence'
```"""


def apply_padding(sentence):
    max_length = 0
    split_sentence = sentence.split(" ")
    for word in split_sentence:
        if len(word) > max_length:
            max_length = len(word)

    new_sentence = ''
    for word in split_sentence:
        if len(word) < max_length:
            new_sentence += " " * (max_length - len(word)) + word
        else:
            new_sentence += " " + word
    return new_sentence


print("let's pad this sentence")
print(apply_padding("let's pad this sentence"))


"""
## B1. Password Parsing

Your task is to create a solution which checks if a given password is valid or invalid, based on a policy.

For example, suppose you have the following inputs:

```
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```

Each input gives the **password policy** and then the **password**. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, `1-3 a` means that the password must contain `a` at least `1` time and at most `3` times.

In the above example, *`2`* passwords are valid. The middle password, `cdefg`, is not; it contains no instances of `b`, but needs at least `1`. The first and third passwords are valid: they contain one `a` or nine `c`, both within the limits of their respective policies.
"""