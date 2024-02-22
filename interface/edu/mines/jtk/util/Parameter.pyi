
from typing import overload, List
from edu.mines.jtk.mapping import *


class Parameter:
    """
    A parameter - a named value (or array of values) with a type and
    (optional) units.
    A parameter's type may be set explicitly or by by setting its value(s).
    A parameter value set as one type may be got as another type, provided
    that the implied conversion is supported. For example, any float may be
    converted to a String, but only some Strings may be converted to floats.
    Getting a parameter value never changes the intrinsic parameter type.
    A ParameterConvertException is thrown when a conversion fails.
    Parameters typically reside in a parameter set. A parameter set contains
    parameters and parameter subsets, thereby creating a tree with parameters
    as leaves.
    """

    @overload
    def __init__(self, name: String) -> None:
        """
        Construct an empty named parameter.
        
        Parameters
        -----------
        name : String
            parameter name.
        """
    @overload
    def __init__(self, name: String, value: bool) -> None:
        """
        Construct a named parameter with boolean value.
        
        Parameters
        -----------
        name : String
            parameter name.
        value : bool
            parameter value.
        """
    @overload
    def __init__(self, name: String, value: int) -> None:
        """
        Construct a named parameter with int value.
        
        Parameters
        -----------
        name : String
            parameter name.
        value : int
            parameter value.
        """
    @overload
    def __init__(self, name: String, value: long) -> None:
        """
        Construct a named parameter with long value.
        
        Parameters
        -----------
        name : String
            parameter name.
        value : long
            parameter value.
        """
    @overload
    def __init__(self, name: String, value: float) -> None:
        """
        Construct a named parameter with float value.
        
        Parameters
        -----------
        name : String
            parameter name.
        value : float
            parameter value.
        """
    @overload
    def __init__(self, name: String, value: double) -> None:
        """
        Construct a named parameter with double value.
        
        Parameters
        -----------
        name : String
            parameter name.
        value : double
            parameter value.
        """
    @overload
    def __init__(self, name: String, value: String) -> None:
        """
        Construct a named parameter with String value.
        
        Parameters
        -----------
        name : String
            parameter name.
        value : String
            parameter value.
        """
    @overload
    def __init__(self, name: String, values: List[bool]) -> None:
        """
        Construct a named parameter with boolean values.
        
        Parameters
        -----------
        name : String
            parameter name.
        values : List[bool]
            parameter values.
        """
    @overload
    def __init__(self, name: String, values: Int1D) -> None:
        """
        Construct a named parameter with int values.
        
        Parameters
        -----------
        name : String
            parameter name.
        values : Int1D
            parameter values.
        """
    @overload
    def __init__(self, name: String, values: Long1D) -> None:
        """
        Construct a named parameter with long values.
        
        Parameters
        -----------
        name : String
            parameter name.
        values : Long1D
            parameter values.
        """
    @overload
    def __init__(self, name: String, values: Float1D) -> None:
        """
        Construct a named parameter with float values.
        
        Parameters
        -----------
        name : String
            parameter name.
        values : Float1D
            parameter values.
        """
    @overload
    def __init__(self, name: String, values: Double1D) -> None:
        """
        Construct a named parameter with double values.
        
        Parameters
        -----------
        name : String
            parameter name.
        values : Double1D
            parameter values.
        """
    @overload
    def __init__(self, name: String, values: String1D) -> None:
        """
        Construct a named parameter with String values.
        
        Parameters
        -----------
        name : String
            parameter name.
        values : String1D
            parameter values.
        """
    @overload
    def __init__(self, name: String, value: bool, units: String) -> None:
        """
        Construct a named parameter with boolean value and units.
        
        Parameters
        -----------
        name : String
            parameter name.
        value : bool
            parameter value.
        units : String
            parameter units.
        """
    @overload
    def __init__(self, name: String, value: int, units: String) -> None:
        """
        Construct a named parameter with int value and units.
        
        Parameters
        -----------
        name : String
            parameter name.
        value : int
            parameter value.
        units : String
            parameter units.
        """
    @overload
    def __init__(self, name: String, value: long, units: String) -> None:
        """
        Construct a named parameter with long value and units.
        
        Parameters
        -----------
        name : String
            parameter name.
        value : long
            parameter value.
        units : String
            parameter units.
        """
    @overload
    def __init__(self, name: String, value: float, units: String) -> None:
        """
        Construct a named parameter with float value and units.
        
        Parameters
        -----------
        name : String
            parameter name.
        value : float
            parameter value.
        units : String
            parameter units.
        """
    @overload
    def __init__(self, name: String, value: double, units: String) -> None:
        """
        Construct a named parameter with double value and units.
        
        Parameters
        -----------
        name : String
            parameter name.
        value : double
            parameter value.
        units : String
            parameter units.
        """
    @overload
    def __init__(self, name: String, value: String, units: String) -> None:
        """
        Construct a named parameter with String value and units.
        
        Parameters
        -----------
        name : String
            parameter name.
        value : String
            parameter value.
        units : String
            parameter units.
        """
    @overload
    def __init__(self, name: String, values: List[bool], units: String) -> None:
        """
        Construct a named parameter with boolean values and units.
        
        Parameters
        -----------
        name : String
            parameter name.
        values : List[bool]
            parameter values.
        units : String
            parameter units.
        """
    @overload
    def __init__(self, name: String, values: Int1D, units: String) -> None:
        """
        Construct a named parameter with int values and units.
        
        Parameters
        -----------
        name : String
            parameter name.
        values : Int1D
            parameter values.
        units : String
            parameter units.
        """
    @overload
    def __init__(self, name: String, values: Long1D, units: String) -> None:
        """
        Construct a named parameter with long values and units.
        
        Parameters
        -----------
        name : String
            parameter name.
        values : Long1D
            parameter values.
        units : String
            parameter units.
        """
    @overload
    def __init__(self, name: String, values: Float1D, units: String) -> None:
        """
        Construct a named parameter with float values and units.
        
        Parameters
        -----------
        name : String
            parameter name.
        values : Float1D
            parameter values.
        units : String
            parameter units.
        """
    @overload
    def __init__(self, name: String, values: Double1D, units: String) -> None:
        """
        Construct a named parameter with double values and units.
        
        Parameters
        -----------
        name : String
            parameter name.
        values : Double1D
            parameter values.
        units : String
            parameter units.
        """
    @overload
    def __init__(self, name: String, values: String1D, units: String) -> None:
        """
        Construct a named parameter with String values and units.
        
        Parameters
        -----------
        name : String
            parameter name.
        values : String1D
            parameter values.
        units : String
            parameter units.
        """
    @overload
    def __init__(self, name: String, parent: ParameterSet) -> None:
        """
    
        """
    def clone(self) -> Object:
        """
        Clone this parameter.
        The clone will be an orphan; its parent parameter set will be null.
        Returns
        --------
        output : Object
            a clone of this parameter.
        """
    def replaceWith(self, par: Parameter) -> Parameter:
        """
        Replace the contents of this parameter with a copy of
        the contents of the specified parameter.
        Do not change this parameter's parent.
        those in this parameter.
        
        Parameters
        -----------
        par : Parameter
            the parameter with contents that will replace
        
        Returns
        --------
        output : Parameter
            this parameter, with contents replaced.
        """
    @overload
    def copyTo(self, parent: ParameterSet) -> Parameter:
        """
        Copy this parameter to the specified parent parameter set
        without changing its name.
        the parent of the destination parameter.
        If the parent is null, the destination parameter will be an orphan.
        
        Parameters
        -----------
        parent : ParameterSet
            the parameter set into which to copy this parameter;
        
        Returns
        --------
        output : Parameter
            the destination parameter.
        """
    @overload
    def copyTo(self, parent: ParameterSet, name: String) -> Parameter:
        """
        Copy this parameter.to the specified parent parameter set
        while changing its name.
        the parent of the destination parameter.
        If the parent is null, the destination parameter will be an orphan.
        
        Parameters
        -----------
        parent : ParameterSet
            the parameter set into which to copy this parameter;
        name : String
            the destination parameter name.
        
        Returns
        --------
        output : Parameter
            the destination parameter.
        """
    @overload
    def moveTo(self, parent: ParameterSet) -> Parameter:
        """
        Move this parameter to the specified parent parameter set
        without changing its name.
        the parent of the destination parameter.
        If the parent is null, the destination parameter will be an orphan.
        
        Parameters
        -----------
        parent : ParameterSet
            the parameter set into which to move this parameter;
        
        Returns
        --------
        output : Parameter
            the destination parameter.
        """
    @overload
    def moveTo(self, parent: ParameterSet, name: String) -> Parameter:
        """
        Move this parameter to the specified parent parameter set
        while changing its name.
        the parent of the destination parameter.
        If the parent is null, the destination parameter will be an orphan.
        
        Parameters
        -----------
        parent : ParameterSet
            the parameter set into which to move this parameter;
        name : String
            the destination parameter name.
        
        Returns
        --------
        output : Parameter
            the destination parameter.
        """
    def remove(self) -> None:
        """
        Remove this parameter from its parent parameter set.
        In other words, orphan this parameter.
        If this parameter is already an orphan, do nothing.
        """
    def getName(self) -> String:
        """
        Get the parameter name.
        Returns
        --------
        output : String
            parameter name.
        """
    def setName(self, name: String) -> None:
        """
        Set the parameter name.
        If the parameter has a parent parameter set, ignore a null name.
        
        Parameters
        -----------
        name : String
            parameter name.
        """
    def getUnits(self) -> String:
        """
        Get the parameter units.
        Returns
        --------
        output : String
            parameter units; null, if the parameter has no units.
        """
    def setUnits(self, units: String) -> None:
        """
        Set the parameter units.
        
        Parameters
        -----------
        units : String
            parameter units. For no units, specify null.
        """
    def getType(self) -> int:
        """
        Get the parameter type.
        Returns
        --------
        output : int
            parameter type.
        """
    def setType(self, type: int) -> None:
        """
        Set the parameter type.
        To specify a null (empty) parameter value, set its type to null.
        values cannot be converted to the specified type.
        
        Parameters
        -----------
        type : int
            parameter type.
        """
    def getParent(self) -> ParameterSet:
        """
        Get the parameter set that contains this parameter.
        parent, because it was orphaned by removing it from its parent.
        Returns
        --------
        output : ParameterSet
            parent parameter set; null, if the parameter has no
        """
    def getBoolean(self) -> bool:
        """
        Get parameter value as boolean.
        If the parameter contains an array of values, get the last value.
        converted to boolean.
        Returns
        --------
        output : bool
            parameter value.
        """
    def getInt(self) -> int:
        """
        Get parameter value as int.
        If the parameter contains an array of values, get the last value.
        converted to int.
        Returns
        --------
        output : int
            parameter value.
        """
    def getLong(self) -> long:
        """
        Get parameter value as long.
        If the parameter contains an array of values, get the last value.
        converted to long.
        Returns
        --------
        output : long
            parameter value.
        """
    def getFloat(self) -> float:
        """
        Get parameter value as float.
        If the parameter contains an array of values, get the last value.
        converted to float.
        Returns
        --------
        output : float
            parameter value.
        """
    def getDouble(self) -> double:
        """
        Get parameter value as double.
        If the parameter contains an array of values, get the last value.
        converted to double.
        Returns
        --------
        output : double
            parameter value.
        """
    def getString(self) -> String:
        """
        Get parameter value as String.
        If the parameter contains an array of values, get the last value.
        converted to String.
        Returns
        --------
        output : String
            parameter value.
        """
    def getBooleans(self) -> List[bool]:
        """
        Get parameter values as array of booleans.
        cannot be converted to boolean.
        Returns
        --------
        output : List[bool]
            parameter values.
        """
    def getInts(self) -> Int1D:
        """
        Get parameter values as array of ints.
        cannot be converted to int.
        Returns
        --------
        output : Int1D
            parameter values.
        """
    def getLongs(self) -> Long1D:
        """
        Get parameter values as array of longs.
        cannot be converted to long.
        Returns
        --------
        output : Long1D
            parameter values.
        """
    def getFloats(self) -> Float1D:
        """
        Get parameter values as array of floats.
        cannot be converted to float.
        Returns
        --------
        output : Float1D
            parameter values.
        """
    def getDoubles(self) -> Double1D:
        """
        Get parameter values as array of doubles.
        cannot be converted to double.
        Returns
        --------
        output : Double1D
            parameter values.
        """
    def getStrings(self) -> String1D:
        """
        Get parameter values as array of Strings.
        cannot be converted to String.
        Returns
        --------
        output : String1D
            parameter values.
        """
    def setBoolean(self, value: bool) -> None:
        """
        Set parameter value as boolean.
        
        Parameters
        -----------
        value : bool
            parameter value.
        """
    def setInt(self, value: int) -> None:
        """
        Set parameter value as int.
        
        Parameters
        -----------
        value : int
            parameter value.
        """
    def setLong(self, value: long) -> None:
        """
        Set parameter value as long.
        
        Parameters
        -----------
        value : long
            parameter value.
        """
    def setFloat(self, value: float) -> None:
        """
        Set parameter value as float.
        
        Parameters
        -----------
        value : float
            parameter value.
        """
    def setDouble(self, value: double) -> None:
        """
        Set parameter value as double.
        
        Parameters
        -----------
        value : double
            parameter value.
        """
    def setString(self, value: String) -> None:
        """
        Set parameter value as String.
        
        Parameters
        -----------
        value : String
            parameter value.
        """
    def setBooleans(self, values: List[bool]) -> None:
        """
        Set parameter values as an array of booleans.
        
        Parameters
        -----------
        values : List[bool]
            parameter values.
        """
    def setInts(self, values: Int1D) -> None:
        """
        Set parameter values as an array of ints.
        
        Parameters
        -----------
        values : Int1D
            parameter values.
        """
    def setLongs(self, values: Long1D) -> None:
        """
        Set parameter values as an array of longs.
        
        Parameters
        -----------
        values : Long1D
            parameter values.
        """
    def setFloats(self, values: Float1D) -> None:
        """
        Set parameter values as an array of floats.
        
        Parameters
        -----------
        values : Float1D
            parameter values.
        """
    def setDoubles(self, values: Double1D) -> None:
        """
        Set parameter values as an array of doubles.
        
        Parameters
        -----------
        values : Double1D
            parameter values.
        """
    def setStrings(self, values: String1D) -> None:
        """
        Set parameter values as an array of Strings.
        
        Parameters
        -----------
        values : String1D
            parameter values.
        """
    def isNull(self) -> bool:
        """
        Tests if parameter type is null.
        Returns
        --------
        output : bool
            true, if parameter type is null; false, otherwise.
        """
    def isBoolean(self) -> bool:
        """
        Tests if parameter type is boolean.
        Returns
        --------
        output : bool
            true, if parameter type is boolean; false, otherwise.
        """
    def isInt(self) -> bool:
        """
        Tests if parameter type is int.
        Returns
        --------
        output : bool
            true, if parameter type is int; false, otherwise.
        """
    def isLong(self) -> bool:
        """
        Tests if parameter type is long.
        Returns
        --------
        output : bool
            true, if parameter type is long; false, otherwise.
        """
    def isFloat(self) -> bool:
        """
        Tests if parameter type is float.
        Returns
        --------
        output : bool
            true, if parameter type is float; false, otherwise.
        """
    def isDouble(self) -> bool:
        """
        Tests if parameter type is double.
        Returns
        --------
        output : bool
            true, if parameter type is double; false, otherwise.
        """
    def isString(self) -> bool:
        """
        Tests if parameter type is String.
        Returns
        --------
        output : bool
            true, if parameter type is String; false, otherwise.
        """
    def toString(self) -> String:
        """
        Get a string representation of this parameter.
        This XML-formatted string represents the parameter name, type,
        (optional) units and value(s).
        Returns
        --------
        output : String
            string representation of this parameter.
        """
    def equals(self, o: Object) -> bool:
        """
        Compares two parameters for equality.
        Parameters are equal if their names, units, types, and values are equal.
        Returns
        --------
        output : bool
            true, if the parameters are equal; false, otherwise.
        """
    def hashCode(self) -> int:
        """
        Computes the hash code of this paramater.
        The hash code depends on the parameter name, units, type, and values.
        Returns
        --------
        output : int
            the hash code.
        """