import ply.lex as lex
import os
import codecs

palabrasClaves = (
    'CONJUNCION', 'DISYUNCION', 'NEGACION', 'CUANDO', 'CUANDONO', 'FX', 'DEVOLVER', 'ITERA', 'DURANTE', 'FINAL'
)

types = (
    'KEYWORDS', 'LITERALS', 'ID', 'OPERATORS', 'DELIMITERS'
)

literal = ( 'FALS', 'TRU',)
tokens = types + (
    'ASIGNACION', 'SUM', 'SUBTRAC', 'MULP', 'DIVI', 'POT', 'MOD', 'MAYORQ', 'MNORQ', 'MAYORIG', 'MNORIG',
    'IGUAL', 'DISTINTO', 'PARIZQ', 'PARDER', 'CORIZQ', 'CORDER','LLAIZQ', 'LLADER','AND', 'OR', 'NOT', 'INCREMENTO', 'DECREMENTO', 'NUMERAL', 'PUNTOCOMA', 'COMA', 'COMILLA', 'COMILLAS',
    'ENTERO', 'STRING'
)

t_ignore = r' \t'
t_ASIGNACION = r'>>'
t_SUM = r'\+'
t_SUBTRAC = r'-'
t_MULP= r'\*'
t_DIVI = r'/'
t_POT = r'(\*{2} | \^)'
t_MOD = r'\%'
t_MAYORQ = r'>'
t_MNORQ = r'<'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_AND = r'\^'
t_OR = r'\v'
t_NOT = r'\!'
t_PUNTOCOMA = ';'
t_COMA = r','
t_COMILLA = r'\''
t_COMILLAS = r'\"'

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
    
def t_ID(t):
    r'\w+(_\d\w)*'
    if t.value in palabrasClaves:
        t.type = "KEYWORDS"
    elif t.value in literal:
        t.type = "LITERALS"
    elif t.value.upper() in palabrasClaves:
        invalido(t,'Palabra clave')
        return 
    
    return t

def t_STRING(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t



def t_NUMERAL(t):
    r'\#'
    return t

def t_MNORIG(t):
    r'<<<'
    return t

def t_MAYORIG(t):
    r'>>>'
    return t

def t_IGUAL(t):
    r'='
    return t

def t_DISTINTO(t):
    r'>>!'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'\~\~\~(.|\n)*?\~\~\~'
    t.lexer.lineno += t.value.count('\n')

def t_comments_ONELine(t):
    r'\~\~(.)*\n'
    t.lexer.lineno += 1

def t_error(t):
    print("En la Linea #%d -> Token %r invalido." % (t.lineno, str(t.value)[0]) )
    t.lexer.skip(1)   
    
def invalido(t, arg='problema indefinido'):
    print("En la Linea #%d -> Token %r invalido." % (t.lineno, t.value))
    if arg : print(" porque", arg, "\n")

direccionArchivo = str(os.getcwd())+ '/prueba.fx'
fp = codecs.open(direccionArchivo,"r","utf-8")
traducir = fp.read()
fp.close()

lexer1 = lex.lex()
lexer1.input(traducir)

if __name__ == '__main__':
    while True:
        token1 = lexer1.token()
        if not token1 : break
        print (token1)


