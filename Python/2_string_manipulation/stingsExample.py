"""
Simple example for manipulating strings.

Make this:
Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high. Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are!

Into this:
Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high.
        Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are!


Following these rules:
1. After the 3 "," change line after the last one
2. If there is a "!" put one "\t" at the start of the line and change line after the "!"
3. If there is a "." put two "\t" at the start of the line and change line after the "."
"""

poem = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high. Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are!"

# Split string to words to create an array
words = poem.split(" ")

output = [] # The result of the algorithm
words_index = 0 # To keep track which word is being processed

comma_counter = 0 # Used for counting the "," for rule 1
last_position_of_nl = 0 # Used for remembering where the last "\n" was for rule 2

for word in words:

    # Rule 1
    if word[-1] == ",": comma_counter += 1
    if comma_counter == 3:
        comma_counter = 0
        output.append(word + "\n")
        last_position_of_nl = words_index
        words_index += 1
        continue
    
    # Rule 2
    if word[-1] == "!":
        output[last_position_of_nl] = output[last_position_of_nl] + "\t"
        output.append(word + "\n")
        last_position_of_nl = words_index
        words_index += 1
        continue

    # Rule 3
    if word[-1] == ".":
        output[last_position_of_nl] = output[last_position_of_nl] + "\t"*2
        output.append(word + "\n")
        last_position_of_nl = words_index
        words_index += 1
        continue
    
    # If no rule applies to this word, just add a " "
    output.append(word + " ")
    words_index += 1

output = "".join(output)

print(output)