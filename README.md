# Implementation-PushDown-Automata
Acceptance by Pushdown Automaton (PDA)
Objective:
To implement a program that receives an input file containing several strings and a PDA. The program should determine if each string is accepted by the PDA or not.

Input File Format:
The input file will contain information about the PDA and the strings to be tested in the following format:

Line 1: Number of alphabet symbols.

Line 2: Alphabet symbols separated by spaces.

Line 3: Number of states.

Line 4: Number of transitions.

Line 5 and onwards: Transitions, each on a new line, in the format:
I, a, A -> J, B1B2…BK

This means from state I, reading symbol a, and with A at the top of the stack, move to state J and replace A with B1B2…BK on the stack.

Line with number of accepting states.

Line with accepting states (separated by spaces).

Subsequent lines: Strings to be tested.

End of file marked by $.

Implementation Instructions:
First, read and parse the input file.
Extract and store information related to the alphabet, states, transitions, and accepting states.
Use the extracted information to construct a PDA.
For each input string, simulate the PDA to determine if the string is accepted or not.
Output "Accepted" if the string is accepted by the PDA, otherwise output "Rejected".
Example Input:
2
a b
3
4
0, a, Z -> 1, AZ
1, a, A -> 1, AA
1, b, A -> 2, @
2, b, A -> 2, @
1
2
aab
abb
$
Expected Output:
aab: Accept
abb: Reject
Important:
Use the @ symbol to denote the empty string (lambda transitions).
Ensure that the PDA correctly identifies the accepting states.
