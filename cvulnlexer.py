# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:29:37 2019

@author: amanb, SE (edited by KJ)
"""

import ply.lex as lex #library import
# List of token names.   This is always required
tokens = [
'PLUS' ,        # +                                 # OPERATORS #
'MINUS' ,       # -
'MULTIPLY',     # *
'DIVIDE',       # /
'MODULO',       # %

'NOT',          # ~
'EQUALS',       # =

'LT',           # <                                 # COMPARATORS #
'GT',           # >
'LTE',          # <=
'GTE',          # >=
'DOUBLEEQUAL',  # ==
'NE',           # !=
'AND',          # &
'OR' ,          # |                                                

'LPAREN',       # (                                 # BRACKETS #
'RPAREN',       # )
'LBRACE',       # [
'RBRACE',       # ]
'BLOCKSTART',   # {
'BLOCKEND',     # }

'INTEGER',      # int                               # DATA TYPES#
'FLOAT',       # dbl
'CHAR',     #char
'STRING',       #str
'ID',
'KW',

'SEMI',     #;
'COMMENTML',  # --
'COMMENTSL'
]

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULTIPLY   = r'\*'
t_DIVIDE  = r'/'
t_MODULO = r'%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_BLOCKSTART = r'\{'
t_BLOCKEND = r'\}'
t_NOT = r'\~'
t_EQUALS = r'\='
t_GT = r'\>'
t_LT = r'\<'
t_LTE = r'\<\='
t_GTE = r'\>\='
t_DOUBLEEQUAL = r'\=\='
t_NE = r'\!\='
t_AND = r'\&'
t_OR = r'\|'
t_COMMENTML = r'/\*.*'
t_COMMENTSL = r'//.*'
t_SEMI = r';'
t_ignore  = ' \t'

#Rules for INTEGER and FLOAT tokens
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_FLOAT(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t

def t_CHAR(t):
    r'\'.\''
    return t

def t_STRING(t):
    r'".*"'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    t.type = kw.get(t.value,'ID')    # Check for keywords
    return t
    
kw = {'if': 'IF', 'then': 'THEN', 'else': 'ELSE', 'while': 'WHILE', 'gets': 'GETS', 'fgets': 'FGETS', 'getline': 'GETLINE', 'read': 'READ', 'scanf': 'SCANF', 'malloc': 'MALLOC', 'printf': 'PRINTF'}
tokens.append('ID')
tokens += list(kw.values())

# zip_tokens = {tokens[i] : i for i in range(len(tokens))}
# data = '''
# printf('N');
# malloc(33);
# malloc(33);
# //hello
# 2 + 3 = 4;
# printf('sdf')
# '''

# lexer = lex.lex()

# # Give the lexer some input
# lexer.input(data)
# x = list(lexer)

# Tokenize
# tokenized = [zip_tokens[tok.type] + 1 for tok in x]
# print(tokenized)
# print(zip_tokens)

def TOK(someText):
    lexer = lex.lex()
    lexer.input(someText)
    x = list(lexer)
    zip_tokens = {tokens[i] : i for i in range(len(tokens))}
    tokenized = [zip_tokens[tok.type] + 1 for tok in x]
