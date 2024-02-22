from typing import overload, List
from edu.mines.jtk.mapping import *
from edu.mines.jtk.util import *


class ParameterSet:
    """
    A parameter set - a collection of named parameters and parameter subsets.
    A parameter set forms a tree in which the parameters represent leaf nodes
    and parameter subsets represent branches.
    """

    @overload
    def __init__(self) -> None:
        """
        Construct an empty nameless root parameter set.
        """

    @overload
    def __init__(self, name: String) -> None:
        """
        Construct an empty named root parameter set.
        
        Parameters
        -----------
        name : String
            parameter set name.
        """

    def clone(self) -> Object:
        """
        Clone this parameter set.
        The clone will be an orphan; its parent parameter set will be null.
        Returns
        --------
        output : Object
            a clone of this parameter set.
        """

    def replaceWith(self, parset: ParameterSet) -> ParameterSet:
        """
        Replace the contents of this parameter set with a copy of
        the contents of the specified parameter set.
        Do not change this parameter set's parent.
        those in this parameter set.
        
        Parameters
        -----------
        parset : ParameterSet
            the parameter set with contents that will replace
        
        Returns
        --------
        output : ParameterSet
            this parameter set, with contents replaced.
        """

    def getName(self) -> String:
        """
        Get the parameter set name.
        Returns
        --------
        output : String
            parameter set name.
        """

    def setName(self, name: String) -> None:
        """
        Set the parameter set name.
        If the parameter set has a parent parameter set, ignore a null name.
        
        Parameters
        -----------
        name : String
            parameter set name.
        """

    def getParameter(self, name: String) -> Parameter:
        """
        Get a parameter.
        parameter with the specified name.
        
        Parameters
        -----------
        name : String
            name of the parameter to get.
        
        Returns
        --------
        output : Parameter
            parameter; null, if the parameter set does not contain a
        """

    def getParameterSet(self, name: String) -> ParameterSet:
        """
        Get a parameter subset.
        subset with the specified name.
        
        Parameters
        -----------
        name : String
            name of the subset to get.
        
        Returns
        --------
        output : ParameterSet
            subset; null, if the parameter set does not contain a
        """

    def addParameter(self, name: String) -> Parameter:
        """
        Add a new parameter to this parameter set.
        If this parameter set already contains a parameter or subset
        with the specified name, replace that parameter or subset with
        with the new parameter.
        
        Parameters
        -----------
        name : String
            name of the parameter to add.
        
        Returns
        --------
        output : Parameter
            parameter; null, if name is null.
        """

    def addParameterSet(self, name: String) -> ParameterSet:
        """
        Add a new parameter subset to this parameter set.
        If this parameter set already contains a parameter or subset
        with the specified name, replace that parameter or subset with
        with the new parameter subset.
        
        Parameters
        -----------
        name : String
            name of the parameter subset to add.
        
        Returns
        --------
        output : ParameterSet
            parameter subset; null, if name is null.
        """

    def getBoolean(self, name: String, defaultValue: bool) -> bool:
        """
        Get the boolean value of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        converted to boolean.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultValue : bool
            default value returned if this parameter set
        
        Returns
        --------
        output : bool
            parameter value or default value.
        """

    def getInt(self, name: String, defaultValue: int) -> int:
        """
        Get the int value of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        converted to int.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultValue : int
            default value returned if this parameter set
        
        Returns
        --------
        output : int
            parameter value or default value.
        """

    def getLong(self, name: String, defaultValue: long) -> long:
        """
        Get the long value of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        converted to long.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultValue : long
            default value returned if this parameter set
        
        Returns
        --------
        output : long
            parameter value or default value.
        """

    def getFloat(self, name: String, defaultValue: float) -> float:
        """
        Get the float value of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        converted to float.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultValue : float
            default value returned if this parameter set
        
        Returns
        --------
        output : float
            parameter value or default value.
        """

    def getDouble(self, name: String, defaultValue: double) -> double:
        """
        Get the double value of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        converted to double.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultValue : double
            default value returned if this parameter set
        
        Returns
        --------
        output : double
            parameter value or default value.
        """

    def getString(self, name: String, defaultValue: String) -> String:
        """
        Get the String value of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        converted to String.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultValue : String
            default value returned if this parameter set
        
        Returns
        --------
        output : String
            parameter value or default value.
        """

    def getBooleans(self, name: String,
                    defaultValues: List[bool]) -> List[bool]:
        """
        Get the boolean values of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        converted to boolean.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultValues : List[bool]
            default values returned if this parameter set
        
        Returns
        --------
        output : List[bool]
            parameter values or default values.
        """

    def getInts(self, name: String, defaultValues: Int1D) -> Int1D:
        """
        Get the int values of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        converted to int.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultValues : Int1D
            default values returned if this parameter set
        
        Returns
        --------
        output : Int1D
            parameter values or default values.
        """

    def getLongs(self, name: String, defaultValues: Long1D) -> Long1D:
        """
        Get the long values of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        converted to long.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultValues : Long1D
            default values returned if this parameter set
        
        Returns
        --------
        output : Long1D
            parameter values or default values.
        """

    def getFloats(self, name: String, defaultValues: Float1D) -> Float1D:
        """
        Get the float values of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        converted to float.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultValues : Float1D
            default values returned if this parameter set
        
        Returns
        --------
        output : Float1D
            parameter values or default values.
        """

    def getDoubles(self, name: String, defaultValues: Double1D) -> Double1D:
        """
        Get the double values of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        converted to double.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultValues : Double1D
            default values returned if this parameter set
        
        Returns
        --------
        output : Double1D
            parameter values or default values.
        """

    def getStrings(self, name: String, defaultValues: List[str]) -> List[str]:
        """
        Get the String values of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        converted to String.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultValues : List[str]
            default values returned if this parameter set
        
        Returns
        --------
        output : List[str]
            parameter values or default values.
        """

    def getUnits(self, name: String, defaultUnits: String) -> String:
        """
        Get the units of a named parameter in this parameter set.
        does not contain a parameter with the specified name.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        defaultUnits : String
            default units returned if this parameter set
        
        Returns
        --------
        output : String
            parameter units or default units.
        """

    def setBoolean(self, name: String, value: bool) -> None:
        """
        Set the boolean value of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its value.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        value : bool
            parameter value.
        """

    def setInt(self, name: String, value: int) -> None:
        """
        Set the int value of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its value.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        value : int
            parameter value.
        """

    def setLong(self, name: String, value: long) -> None:
        """
        Set the long value of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its value.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        value : long
            parameter value.
        """

    def setFloat(self, name: String, value: float) -> None:
        """
        Set the float value of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its value.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        value : float
            parameter value.
        """

    def setDouble(self, name: String, value: double) -> None:
        """
        Set the double value of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its value.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        value : double
            parameter value.
        """

    def setString(self, name: String, value: String) -> None:
        """
        Set the String value of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its value.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        value : String
            parameter value.
        """

    def setBooleans(self, name: String, values: List[bool]) -> None:
        """
        Set the boolean values of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its values.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        values : List[bool]
            parameter values.
        """

    def setInts(self, name: String, values: Int1D) -> None:
        """
        Set the int values of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its values.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        values : Int1D
            parameter values.
        """

    def setLongs(self, name: String, values: Long1D) -> None:
        """
        Set the long values of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its values.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        values : Long1D
            parameter values.
        """

    def setFloats(self, name: String, values: Float1D) -> None:
        """
        Set the float values of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its values.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        values : Float1D
            parameter values.
        """

    def setDoubles(self, name: String, values: Double1D) -> None:
        """
        Set the double values of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its values.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        values : Double1D
            parameter values.
        """

    def setStrings(self, name: String, values: List[str]) -> None:
        """
        Set the String values of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its values.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        values : List[str]
            parameter values.
        """

    def setUnits(self, name: String, units: String) -> None:
        """
        Set the units of a named parameter in this parameter set.
        If this parameter set does not contain the named parameter, add
        the parameter to this set before setting its units.
        
        Parameters
        -----------
        name : String
            name of the parameter.
        units : String
            parameter units.
        """

    @overload
    def copyTo(self, parent: ParameterSet) -> ParameterSet:
        """
        Copy this parameter.set to the specified parent parameter set
        without changing its name.
        the parent of the destination parameter set.
        If the parent is null, the destination parameter set will be an orphan.
        
        Parameters
        -----------
        parent : ParameterSet
            the parameter set into which to copy this parameter set;
        
        Returns
        --------
        output : ParameterSet
            the destination parameter set.
        """

    @overload
    def copyTo(self, parent: ParameterSet, name: String) -> ParameterSet:
        """
        Copy this parameter.set to the specified parent parameter set
        while changing its name.
        the parent of the destination parameter set.
        If the parent is null, the destination parameter set will be an orphan.
        
        Parameters
        -----------
        parent : ParameterSet
            the parameter set into which to copy this parameter set;
        name : String
            the destination parameter set name.
        
        Returns
        --------
        output : ParameterSet
            the destination parameter set.
        """

    @overload
    def moveTo(self, parent: ParameterSet) -> ParameterSet:
        """
        Move this parameter set to the specified parent parameter set
        without changing its name.
        the parent of the destination parameter set.
        If the parent is null, the destination parameter set will be an orphan.
        
        Parameters
        -----------
        parent : ParameterSet
            the parameter set into which to move this parameter set;
        
        Returns
        --------
        output : ParameterSet
            the destination parameter set.
        """

    @overload
    def moveTo(self, parent: ParameterSet, name: String) -> ParameterSet:
        """
        Move this parameter set to the specified parent parameter set
        while changing its name.
        the parent of the destination parameter set.
        If the parent is null, the destination parameter set will be an orphan.
        The parent cannot be this parameter set or a subset of this parameter set.
        
        Parameters
        -----------
        parent : ParameterSet
            the parameter set into which to move this parameter set;
        name : String
            the destination parameter set name.
        
        Returns
        --------
        output : ParameterSet
            the destination parameter set.
        """

    @overload
    def remove(self) -> None:
        """
        Remove this parameter set from its parent parameter set.
        In other words, orphan this parameter set.
        If this parameter set is already an orphan, do nothing.
        """

    @overload
    def remove(self, name: String) -> None:
        """
        Remove a named parameter or subset from this parameter set.
        If this parameter set does not contain a parameter or subset
        with the specified name, do nothing.
        
        Parameters
        -----------
        name : String
            name of the parameter or subset to remove.
        """

    def countParameters(self) -> int:
        """
        Count the parameters in this parameter set.
        Returns
        --------
        output : int
            number of parameters in this parameter set.
        """

    def countParameterSets(self) -> int:
        """
        Count the parameter subsets in this parameter set.
        Returns
        --------
        output : int
            number of subsets in this parameter set.
        """

    def clear(self) -> None:
        """
        Clear this parameter set by removing all its parameters
        and parameter subsets.
        """

    def getParent(self) -> ParameterSet:
        """
        Get the parameter set that contains this parameter set.
        a root parameter set with no parent, perhaps because it was
        orphaned by removing it from its parent.
        Returns
        --------
        output : ParameterSet
            parent parameter set; null, if the parameter set is
        """

    def getParameters(self) -> Iterator:
        """
        Gets an iterator for the parameters in this parameter set.
        Returns
        --------
        output : Iterator
            the iterator.
        """

    def getParameterSets(self) -> Iterator:
        """
        Gets an iterator for the parameter sets in this parameter set.
        Returns
        --------
        output : Iterator
            the iterator.
        """

    def fromString(self, s: String) -> None:
        """
        Replace this parameter set with that represented in the specified
        XML-formatted string (the same format written by method toString).
        formatted.
        
        Parameters
        -----------
        s : String
            XML-formatted string representation of parameter set.
        """

    def toString(self) -> String:
        """
        Get a string representation of this parameter set.
        This XML-formatted string represents the parameter name and
        all parameters and subsets contained in this parameter set.
        Returns
        --------
        output : String
            string representation of this parameter set.
        """

    def equals(self, o: Object) -> bool:
        """
        Compares two parameter sets for equality.
        Parameter sets are equal if their names and any contained
        parameters and parameter sets are equal.
        Returns
        --------
        output : bool
            true, if the parameter sets are equal; false, otherwise.
        """

    def hashCode(self) -> int:
        """
        Computes the hash code of this parameter set.
        Returns
        --------
        output : int
            the hash code.
        """

    def writeExternal(self, out: ObjectOutput) -> None:
        """
        Serializes this parameter set by writing its XML string
        representation to the specified object output.
        
        Parameters
        -----------
        out : ObjectOutput
            the object output to which to write this parameter set.
        """

    def readExternal(self, ins: ObjectInput) -> None:
        """
        Restores this parameter set by reading its XML string
        representation from the specified object input.
        restored cannot be found.
        of this parameter set is not properly formatted.
        
        Parameters
        -----------
        in : ObjectInput
            the object input from which to read this parameter set.
        """
