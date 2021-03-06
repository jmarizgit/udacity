import re # gives access to regular expressions library
import ply.lex as lex # import lex analyzer lib

tokens = (
  'LANGLE', # <
  'LANGLESLASH', # </
  'RANGLE', # >
  'EQUAL', # = 
  'STRING', # "hello"
  'WORD', # Welcome!
  )

t_ignore = ' ' # shortcut for whitespace

def t_error(token):
    print("Illegal character '%s'" % token.value[0])
    token.lexer.skip(1)

# Specifying Tokens

# Write code for the LANGLESLASH to match </ in our HTML.

def t_LANGLESLASH(token):
  r'</'
  return token

def t_LANGLE(token):
  r'<'
  return token

def t_RANGLE(token):
  r'>'
  return token


def t_EQUAL(token):
  r'='
  return token

# # match whitespaces
# def t_WHITESPACE(token):
#   r' '
#   pass

# match double quoted string without a " inside
def t_STRING(token):
  r'"[^"]*"'
  token.value = token.value[1:-1] # substring to strip double quotes
  return token  

# WORD is any number of chars EXCEPT <> or space
def t_WORD(token):
  r"[^ <>]+"
  return token

# # match numbers strings and convert them to int
# def t_NUMBER(token):
#   r"[0-9]+"
#   token.value = int(token.value)
#   return token


webpage = "This is <b>my</b> webpage!"

htmllexer = lex.lex() # tells lex to use all token def above
htmllexer.input(webpage) # which string to break up

while True:
  tok = htmllexer.token() # return next token available
  if not tok: break
  print tok



