
word = "3 x Small (Regular), Ice Cream (Regular), Apple Pie (Regular), Caramel (Regular), Almonds (Regular), Ice Cream (Regular), Peanut Butter (Regular), Bananas (Regular), Granola (Regular), Ice Cream (Regular),"

word_list = word.split()
patterns = ["Small", "Regular", "Large", "Pint", "Milkshake"]  # Substring that will be searched for in string
occur = 0  # Count for how many times substring occurs in each String
increment_int = 0  # Used to increment number values down one so values aren't counted twice
pattern_inc = 0  # Used to increment through pattern list

for i in range(0, len(word_list)):

    while pattern_inc <= 4:  # Loop to increment through patterns list

        if word_list[i] == patterns[pattern_inc]:  # Conditional to increment if substring is found in string
            occur += 1

        pattern_inc += 1

    if len(word_list[i]) == 1 and word_list[i + 1] == 'x':  # Checks if index length 1 and the following index is an x
        increment_int += int(word_list[i]) - 1  # Increment by 1 less that int value in list
        occur += increment_int  # Used to stop redundancy in counting

    pattern_inc = 0  # Resets pattern_inc at the end of while loop

print(occur)

