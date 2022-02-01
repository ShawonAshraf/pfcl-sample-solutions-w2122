from constituents import Phrase, Token

t_The = Token('DT', 'The')
t_cat = Token('NN', 'cat')
t_chases = Token('VB', 'chases')
t_the = Token('DT', 'the')
t_mouse = Token('NN', 'mouse')
t_d = Token('PUNCT', '.')

np_The_cat = Phrase('NP', [t_The, t_cat])
np_the_mouse = Phrase('NP', [t_the, t_mouse])
vp_chases_the_mouse = Phrase('VP', [t_chases, np_the_mouse])

sent = Phrase('S', [np_The_cat, vp_chases_the_mouse, t_d])
