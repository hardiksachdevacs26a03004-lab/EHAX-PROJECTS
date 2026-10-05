# EHAX-PROJECTS
so to start this project i first gave the problem to claude and tell me the topics i needed to learn before starting it included REPL,JSON,IF EXCEPT statemnets, and split strip functions
<br>
then i began learning each topic by building few basic codes that gave clarity about the topic and its use
<br>
i started out with defining the the functions for the input commands like SET, GET, EXISTS, DEL, SAVE and LOAD. 
<br>
after this i built the main logic inside the while true (since it's a REPL program) loop
<br><br><br>
some areas where i had difficulty and errors are:
<br>
1. in the load function when assigning the the dict variable its value  with the help of json, i made a mistake of not making the dict variable global. it was by default a local variable so it couldn't be accessed in the while loop.
<br>
2.code crashed when there was a typo in command or an entry was missing. fixed it by using if-else statements and try except logic
<br>
3.at first i tried to split the file by spaces in between but the code didnt work for when either the key or the value consisted of more than one word. fixed it by splitting the input string with the help of "," and it solved the problem.
<br>
biggest challenge was to keep in mind all the boundary cases that could crag the CLI and had to use AI to help me with it. 

