# COMP 3200 -- DFA-based string acceptor (Thanks to Eric Shade)

char_codes = {'a':0, 'b':1}

transition = [
    [0, 0],      # state 0
    [2, 3],      # state 1 (initial state)
    [0, 3],      # state 2
    [3, 3]       # state 3
]

accepting_states = {1, 3}

def accept(s, state = 1):
    for c in s:
        state = transition[state][char_codes[c]]
    return state in accepting_states





def trace_accept(s, state = 1):
    "same as accept, but prints a trace of the DFA"
    for c in s:
        code = char_codes[c]
        print('\tstate ', state, ": read '", c, "' (code ", code, '): ',
              state, '---', c, '-->', sep='', end='')
        state = transition[state][code]
        print(state)
    print('\tstate ', state, ': end-of-string', sep='')
    return state in accepting_states









if __name__ == '__main__':
    while True:
        try:
            s = input('--> ')
        except EOFError:
            break

        if accept(s):         # use accept or trace_accept
            print('\taccept')
        else:
            print('\treject')
            
