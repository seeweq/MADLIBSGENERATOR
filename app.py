import random
)
# open txt file
with open('madlib.txt', 'r') as f:
# read the txt file
    lines = f.read().splitlines()
    print(lines)
    
     # choose radom line
    random_line = random.choice(lines)
        
    # print the random line
    print(random_line)
    # prompt user to enter missing word
    missing_word = input("enter missing word: ")
    #  replace noun with _____
    madlib = random_line.replace('blank', missing_word)
    print(madlib)
