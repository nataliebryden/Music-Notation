# Music-Notation
Music Notation

ABC notation is a shorthand form of musical notation. In basic form it uses the letters A through G to represent the given notes, with other elements used to place added value on these - sharp, flat, the length of the note, key, ornamentation. Later, with computers becoming a major means of communication, others saw the possibilities of using this form of notation as an ASCII code that could facilitate the sharing of music online, also adding a new and simple language for software developers. In this later form it remains a language for notating music using the ASCII character set.

Write a program to read the attached file and print the Id, title (one only), time and key signatures line by line.

    Each tune consists of headers + notation. The headers start with a character followed by a : (colon)
    The notation follows the headers.
    Each tune begins with the X: - This is also the index field.
    Titles begin with T:
    A tune can have multiple titles, but we are only interested in the first one. If there are more, we just ignore the rest
    The time signature is stored in the M: line
    The key signature is stored in he K: line
    You can ignore the notation, we are just interested in the headers

Below is an example of the sort of output the program should produce:

195 ... Road to Lisdoonvarna, The ... Time sig: C| ... Key sig: D ...
196 ... Jenny's Wedding ... Time sig: C| ... Key sig: D ...
197 ... Dark Girl in Blue, The ... Time sig: C| ... Key sig: D ...
198 ... Knotted Cord, The ... Time sig: C| ... Key sig: Ador ...
199 ... Lucy's Tune ... Time sig: C| ... Key sig: Em ...
200 ... Banks of the Liffey, The ... Time sig: C| ... Key sig: G ...
-------------------------------
There are 100 tunes in the file
-------------------------------
