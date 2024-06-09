import time
import os
class FileHandler:

    def __init__(self):
        pass

    def readFile(self, filePath):
        lines = []
        if os.path.isfile(filePath):
            try:
                with open(filePath, 'r') as file:
                    lines = [line.rstrip() for line in file]
            except IOError as e:
                print("File could not be opened.")
                exit(0)
        else:
            print('{} :File was not found in the specified path.'.format(filePath))
            exit(0)
        return lines

    def parseFile(self, lines):
        ''' 
        Line 1: Number of Alphabet Symbols
        Line 2: Alphabet Symbols
        Line 3: Number of States
        Line 4: Number of Transitions
        Lines 5 to 4 + Number of Transitions: Transitions in the format I, a, A -> J, B1B2…BK
        Line 5 + Number of Transitions: Number of Final States
        Line 6 + Number of Transitions: List of Final States
        Remaining Lines: Strings to test, ending with a $
        '''
        # Extract alphabet
        alphabet_count = int(lines[0])
        alphabet = lines[1].split()

        # Extract transitions
        transitions_count = int(lines[3])
        transitions = []
        for i in range(4, 4 + transitions_count):
            parts = lines[i].split('->')
            left_part = parts[0].strip().split(', ')
            right_part = parts[1].strip().split(', ')
            #transitions.append((left_part[0].strip(), left_part[1].strip(), left_part[2].strip(), right_part[0].strip(),right_part[1].strip()))
            transitions.append(left_part + right_part)
        # Extract final states
        final_states_count = int(lines[4 + transitions_count])
        final_states = lines[5 + transitions_count].split()

        # Extract test strings (not needed for the dictionary but required for the rest of the logic)
        test_strings_start = 6 + transitions_count
        test_strings = []
        for i in range(test_strings_start, len(lines) - 1):
            test_strings.append(lines[i])

        # Determine stack symbols and initial state/stack symbol from transitions
        stack_symbols = set()
        for transition in transitions:
            stack_symbols.add(transition[2])
            
        
        stack_symbols = list(stack_symbols)
        
        # Extract states
        states_count = int(lines[2])
        
        states=set()
        for transition in transitions:
            states.add(transition[0])
            
        states=list(states)    
    
        # Assuming the initial state and stack symbol are the first entries in the transitions
        initial_state = transitions[0][0]
        initial_stack = transitions[0][2]

        # Return the required dictionary
        parsed_lines = {
            'states': states,
            'input_symbols': alphabet,
            'stack_symbols': stack_symbols,
            'initial_state': initial_state,
            'initial_stack': initial_stack,
            'final_states': final_states,
            'productions': transitions
        }

        return parsed_lines
    
class PDA:
    def __init__(self):
        self.stack = []


    def split_and_append(self,string):
        result = []
        for char in string:
            result.append(char)
        return result
    
    def compute(self, inputString, parsedLines):
        #Retrieve all information
        inputString += '@'
        initStackSymbol = parsedLines['initial_stack']
        self.stack.append(initStackSymbol)
        finalStates = parsedLines['final_states']
        initialState = parsedLines['initial_state']
        stackSymbols = parsedLines['stack_symbols']
        productions = parsedLines['productions']

        currentStackSymbol = initStackSymbol
        currentState = initialState
        length=len(inputString)
        print('State\tInput\tStack\tMove')
        print('{}\t {}\t {}\t ({}, {})'.format(currentState, '_', initStackSymbol, currentStackSymbol, self.stack))
        for char in inputString:
            
            for production in productions:
                if ((production[0] == currentState) and (production[1] == char) and (production[2] == currentStackSymbol)):
                    length-=1
                    currentState = production[3]
                    if(len(production[4]) == 2):
                        output_list = self.split_and_append(production[4])
                        self.stack.append(output_list[0])
                    elif(len(production[4]) == 3):
                        output_list = self.split_and_append(production[4])
                        self.stack.append(output_list[1])
                        self.stack.append(output_list[0])
                    elif ((production[4] == '@') and (len(self.stack) != 1)):
                        self.stack.pop()
                        break
                    
            previousStackSymbol = currentStackSymbol
            currentStackSymbol = self.stack[len(self.stack)-1]
            print('{}\t {}\t {}\t ({}, {})'.format(currentState, char, previousStackSymbol, currentStackSymbol, self.stack))
            

        if(currentState in finalStates):
            if (length==0 or length==1):
                print('String accepted by PDA.')
            else:
                print('String rejected by PDA beccause the string does not consume completely.')
        else:
            print('String rejected by PDA beccause  the MACHINE is not in the final state')

def main():
    fh = FileHandler()
    pda = PDA()
    automataFilePath = input('Enter the automata file path: ')
    lines = fh.readFile(automataFilePath)
    print('Reading Automata File')
    
    print('Automata File Successfully Read')
    
    inputString = input('Enter input String: ')
    inputString = inputString.rstrip()
    print('Loading Details from Automata File: ')
    
    parsedLines = fh.parseFile(lines)
    print('States: ', parsedLines['states'])
    print('Input Symbols: ', parsedLines['input_symbols'])
    print('Stack Symbols: ', parsedLines['stack_symbols'])
    print('Initial State: ', parsedLines['initial_state'])
    print('Initial Stack Symbol: ', parsedLines['initial_stack'])
    print('Final States: ', parsedLines['final_states'])
    print('Productions List:')
    for production in parsedLines['productions']:
        print('\t', production)
    
    print('Details loaded')
    print('Computing the Transition Table:')
    pda.compute(inputString, parsedLines)

if __name__ == '__main__':
    main()
