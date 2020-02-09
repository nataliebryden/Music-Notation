
'''
Write a program to read the hnr1.abc file and print the Id, title (one only), time and key signatures line by line.
ABC notation is a shorthand form of musical notation. In basic form it uses the letters A through G to represent the 
given notes, with other elements used to place added value on these - sharp, flat, the length of the note, key, 
ornamentation. Later, with computers becoming a major means of communication, others saw the possibilities of using 
this form of notation as an ASCII code that could facilitate the sharing of music online, also adding a new and simple 
language for software developers. In this later form it remains a language for notating music using the ASCII character set.

Each tune consists of headers + notation. The headers start with a character followed by a : (colon)
The notation follows the headers.
Each tune begins with the X: - This is also the index field.
Titles begin with T:
A tune can have multiple titles, but we are only interested in the first one. If there are more, we just ignore the rest
The time signature is stored in the M: line
The key signature is stored in he K: line
You can ignore the notation, we are just interested in the headers
There are 100 tunes in this file. Below is an example of the sort of output the program should produce:

195 ... Road to Lisdoonvarna, The ... Time sig: C| ... Key sig: D ... 
196 ... Jenny's Wedding ... Time sig: C| ... Key sig: D ... 
197 ... Dark Girl in Blue, The ... Time sig: C| ... Key sig: D ... 
198 ... Knotted Cord, The ... Time sig: C| ... Key sig: Ador ... 
'''


with open('hnr1.abc', 'r') as file1:
    new_string = ""
    prev_line = ""
    for current_line in file1:
        if current_line[0] == 'X':
            new_string += current_line[2:-1]
        if prev_line and prev_line[0] == 'T':
            prev_line = current_line
            continue
        if current_line[0] == 'T':
            new_string += ' ... ' + current_line[2:-1]
        if current_line[0] == 'M':
             new_string += ' ... Time Sig:' + current_line[2:-1]
        if current_line[0] == 'K':
            new_string += ' ... Key Sig:' + current_line[2:]
        prev_line = current_line
    print(new_string)
