from typing import overload
from edu.mines.jtk.mapping import *


class UnitsParser:
    """
    Parser (generated from UnitsParser.jj via JavaCC) to create Units
    from a string that conforms to the following (extended BNF) grammar:
    <pre>
    unit -&gt; expr EOF
    expr -&gt; term ( ("+" | "-") (DOUBLE|INTEGER) )?
    term -&gt; factor ( ("")? factor | "/" factor )
    factor -&gt; primary ("^" INTEGER)?
    primary -&gt; NAME | (DOUBLE|INTEGER) | "(" expr ")"
    </pre>
    """

    @overload
    def __init__(self, stream: java) -> None:
        """
    
        """

    @overload
    def __init__(self, stream: java) -> None:
        """
    
        """

    @overload
    def __init__(self, tm: UnitsParserTokenManager) -> None:
        """
    
        """

    @staticmethod
    def units(self) -> Units:
        """
    
        """

    @staticmethod
    def expr(self) -> Units:
        """
    
        """

    @staticmethod
    def term(self) -> Units:
        """
    
        """

    @staticmethod
    def factor(self) -> Units:
        """
    
        """

    @staticmethod
    def primary(self) -> Units:
        """
    
        """

    @overload
    @staticmethod
    def ReInit(self, stream: java) -> None:
        """
    
        """

    @overload
    @staticmethod
    def ReInit(self, stream: java) -> None:
        """
    
        """

    @overload
    def ReInit(self, tm: UnitsParserTokenManager) -> None:
        """
    
        """

    @overload
    @staticmethod
    def getNextToken(self) -> Token:
        """
    
        """

    @staticmethod
    def getToken(self, index: int) -> Token:
        """
    
        """

    @staticmethod
    def generateParseException(self) -> ParseException:
        """
    
        """

    @staticmethod
    def enable_tracing(self) -> None:
        """
    
        """

    @staticmethod
    def disable_tracing(self) -> None:
        """
    
        """
