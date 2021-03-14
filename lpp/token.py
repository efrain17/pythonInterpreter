from enum import (
    auto,
    Enum,
    unique,
)
from typing import NamedTuple, Dict


@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    EOF = auto()
    ELSE = auto()
    FUNCTION = auto()
    FALSE = auto()
    IDENT = auto()
    IF = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LET = auto()
    LPAREN = auto()
    LT = auto()
    PLUS = auto()
    RBRACE = auto()
    RT = auto()
    RETURN = auto()
    RPAREN = auto()
    TRUE = auto()
    SEMICOLON = auto()


class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'


def lookup_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'si': TokenType.IF,
        'si_no': TokenType.ELSE,
        'variable': TokenType.LET,
        'verdadero': TokenType.TRUE,
        'regresa': TokenType.RETURN,
        'procedimiento': TokenType.FUNCTION,
        'falso': TokenType.FALSE,
    }
    return keywords.get(literal, TokenType.IDENT)