from constituents import Phrase, Token


def list2parsetree(l):
    if len(l) == 2 and isinstance(l[1], str):
        return Token(l[0], l[1])
    else:
        phrase_type = l[0]
        children = []
        for sublist in l[1:]:
            children.append(list2parsetree(sublist))
        return Phrase(phrase_type, children)


if "__main__" == __name__:
    l = ['S',
         ['NP-SBJ',
          ['NP',
           ['DT', 'The'],
              ['NN', 'cat']
           ]
          ],
         ['VP',
             ['VB', 'chases'],
             ['NP-PRD',
              ['NP',
               ['DT', 'the'],
                  ['NN', 'mouse']
               ]
              ]
          ],
         ['.', '.']
         ]

    sent = list2parsetree(l)
    print(sent)
