from typing import overload
from edu.mines.jtk.mapping import *


class Units:
    """
    A class for dimensional analysis of and conversions among units of measure.
    For example, you can determine that ft/s and km/s have the same physical
    dimensions (length/time), and you can convert ft/s to km/s and vice-versa.
    However, you cannot convert s/ft to ft/s.
    
    A typical pattern for dealing with units is to (1) check the dimensions,
    (2) convert parameters to SI units, and (3) use the parameters, now with
    consistent (SI) units.
    
    Here is a simple example:
    <pre><code>
    // Ensure frequency units have dimensions of inverse time.
    if (!freqUnits.haveDimensionsOf(Units.inv(timeUnits))) {
    // handle error
    }
    // Convert both frequency and time to SI units.
    freq = freqUnits.toSI(freq);
    time = timeUnits.toSI(time);
    // Use frequency and time, without worrying about units.
    ...
    </code></pre>
    
    When converting many values from some units to some other units
    (with the same dimensions) it is more efficient to compute a shift
    and scale factor and then use these instead of calling conversion
    methods. For example,
    <pre><code>
    // Determine shift and scale.
    double shift = toUnits.doubleShiftFrom(fromUnits);
    double scale = toUnits.doubleScaleFrom(fromUnits);
    // Use shift and scale to convert lots of values.
    for (int i=0; i&lt;n; ++i) to[i] = shift+scalefrom[i];
    </code></pre>
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs dimensionless units.
        """

    @overload
    def __init__(self, definition: String) -> None:
        """
        Constructs units from a units definition.
        combination of units already defined.
        
        Parameters
        -----------
        definition : String
            the units definition (e.g., "coulomb/volt").
        """

    def clone(self) -> Object:
        """
        Clones these units.
        Returns
        --------
        output : Object
            a clone of these units.
        """

    @overload
    def equals(self, object: Object) -> bool:
        """
        Determines whether specified object equals these units.
        
        Parameters
        -----------
        object : Object
            the object to compare with these units.
        
        Returns
        --------
        output : bool
            true, if equal; false, otherwise.
        """

    @overload
    def equals(self, units: Units) -> bool:
        """
        Determines whether specified units equal these units.
        
        Parameters
        -----------
        units : Units
            the units to compare with these units.
        
        Returns
        --------
        output : bool
            true, if equal; false, otherwise.
        """

    @overload
    def toSI(self, value: float) -> float:
        """
        Converts the specified value in these units to the corresponding value
        in SI base units (seconds, meters, moles, etc.). For example, if these
        units are "km", then convert will multiply the specified value by 1000.
        
        Parameters
        -----------
        value : float
            the value to convert.
        
        Returns
        --------
        output : float
            the converted value.
        """

    @overload
    def toSI(self, value: double) -> double:
        """
        Converts the specified value in these units to the corresponding value
        in SI base units (seconds, meters, moles, etc.). For example, if these
        units are "km", then convert will multiply the specified value by 1000.
        
        Parameters
        -----------
        value : double
            the value to convert.
        
        Returns
        --------
        output : double
            the converted value.
        """

    @overload
    def fromSI(self, value: float) -> float:
        """
        Converts the specified value in SI base units (seconds, meters, moles,
        etc.) to the corresponding value in these units. For example, if these
        units are "km", then convert will divide the specified value by 1000.
        
        Parameters
        -----------
        value : float
            the value to convert.
        
        Returns
        --------
        output : float
            the converted value.
        """

    @overload
    def fromSI(self, value: double) -> double:
        """
        Converts the specified value in SI base units (seconds, meters, moles,
        etc.) to the corresponding value in these units. For example, if these
        units are "km", then convert will divide the specified value by 1000.
        
        Parameters
        -----------
        value : double
            the value to convert.
        
        Returns
        --------
        output : double
            the converted value.
        """

    def floatShiftFrom(self, units: Units) -> float:
        """
        Returns the shift needed to convert values from the specified
        units to these units.
        The specified units must have the dimensions of these units.
        
        Parameters
        -----------
        units : Units
            the units from which to convert.
        
        Returns
        --------
        output : float
            the shift.
        """

    def doubleShiftFrom(self, units: Units) -> double:
        """
        Returns the shift needed to convert values from the specified
        units to these units.
        The specified units must have the dimensions of these units.
        
        Parameters
        -----------
        units : Units
            the units from which to convert.
        
        Returns
        --------
        output : double
            the shift.
        """

    def floatScaleFrom(self, units: Units) -> float:
        """
        Returns the scale factor needed to convert values from the specified
        units to these units.
        The specified units must have the dimensions of these units.
        
        Parameters
        -----------
        units : Units
            the units from which to convert.
        
        Returns
        --------
        output : float
            the scale factor.
        """

    def doubleScaleFrom(self, units: Units) -> double:
        """
        Returns the scale factor needed to convert values from the specified
        units to these units.
        The specified units must have the dimensions of these units.
        
        Parameters
        -----------
        units : Units
            the units from which to convert.
        
        Returns
        --------
        output : double
            the scale factor.
        """

    def haveDimensions(self) -> bool:
        """
        Determines whether these units have dimensions.
        Returns
        --------
        output : bool
            true, if these units have dimensions; false, otherwise.
        """

    def haveDimensionsOf(self, units: Units) -> bool:
        """
        Determines whether these units have the dimensions of specified units.
        
        Parameters
        -----------
        units : Units
            units with which to compare dimensions.
        
        Returns
        --------
        output : bool
            true, if units are the same; false, otherwise.
        """

    def standardDefinition(self) -> String:
        """
        Gets the standard definition of these units. A standard definition is
        the definition expressed entirely in base SI units.
        Returns
        --------
        output : String
            the standard definition of these units.
        """

    @staticmethod
    def add(self, units: Units, s: double) -> Units:
        """
        Adds a scalar to units.
        
        Parameters
        -----------
        units : Units
            first operand.
        s : double
            second operand.
        
        Returns
        --------
        output : Units
            the sum units + s.
        """

    @staticmethod
    def sub(self, units: Units, s: double) -> Units:
        """
        Subtracts a scalar from units.
        
        Parameters
        -----------
        units : Units
            first operand.
        s : double
            second operand.
        
        Returns
        --------
        output : Units
            the difference units - s.
        """

    @overload
    @staticmethod
    def mul(self, units: Units, s: double) -> Units:
        """
        Multiplies units by scalar.
        
        Parameters
        -----------
        units : Units
            first operand.
        s : double
            second operand.
        
        Returns
        --------
        output : Units
            the product units  s.
        """

    @overload
    @staticmethod
    def div(self, units: Units, s: double) -> Units:
        """
        Divides units by scalar.
        
        Parameters
        -----------
        units : Units
            first operand.
        s : double
            second operand.
        
        Returns
        --------
        output : Units
            the quotient units1 / s.
        """

    @overload
    @staticmethod
    def mul(self, units1: Units, units2: Units) -> Units:
        """
        Multiplies units by units.
        
        Parameters
        -----------
        units1 : Units
            first operand.
        units2 : Units
            second operand.
        
        Returns
        --------
        output : Units
            the product units1  units2.
        """

    @overload
    @staticmethod
    def div(self, units1: Units, units2: Units) -> Units:
        """
        Divides units by units.
        
        Parameters
        -----------
        units1 : Units
            first operand.
        units2 : Units
            second operand.
        
        Returns
        --------
        output : Units
            the quotient units1 / units2.
        """

    @staticmethod
    def inv(self, units: Units) -> Units:
        """
        Inverts units.
        
        Parameters
        -----------
        units : Units
            to invert.
        
        Returns
        --------
        output : Units
            the inverse 1 / units.
        """

    @staticmethod
    def pow(self, units: Units, p: int) -> Units:
        """
        Raises units to a power.
        
        Parameters
        -----------
        units : Units
            first operand.
        p : int
            second operand.
        
        Returns
        --------
        output : Units
            the power units^p.
        """

    @staticmethod
    def define(self, name: String, plural: bool, definition: String) -> bool:
        """
        Adds a definition of units to the table of units.
        
        An extensive default table of units may be provided, so that explicit
        definition using this method may be unnecessary.
        
        Most units are defined in terms of other units already defined. However,
        some units, such as "ampere" and "second", are base units representing
        the physical dimensions, such as electric current and time, respectively.
        We define derived units in terms of base units and other derived
        units. Only one base units should be defined for each physical dimension.
        definition is null, then the name is assumed to define new base units,
        such as "meter".
        Multiplication is denoted by a space, '.', or ''.
        Division is denoted by a '/'.
        Addition and subtraction are denoted by '+' and '-'.
        Note: only addition and subtraction of constants is
        supported, and the constant must appear on the right-hand-side
        of the '+' or '-', as in "degK - 273.15", not "-273.15 + degK".
        Exponentiation is denoted by '^', as in s^2.
        Units will not be defined if (1) units with the specified name
        already exist or (2) the limit on the number of base units
        has been exceeded.
        combination of existing units.
        
        Parameters
        -----------
        name : String
            the string by which the units will be known (e.g,, "farad").
        plural : bool
            true, if the name has a simple plural form, as in "farads".
        definition : String
            the units definition, as in "coulomb/volt". If the
        
        Returns
        --------
        output : bool
            true, if the units were successfully defined; false, otherwise.
        """

    @staticmethod
    def isValidDefinition(self, definition: String) -> bool:
        """
        Determines if a string is a valid units definition.
        Valid definitions are those consistent with
        the format described above.
        
        Parameters
        -----------
        definition : String
            the units definition in question (e.g., "coulomb/volt").
        
        Returns
        --------
        output : bool
            true, if the units definition is valid; false, otherwise.
        """

    @staticmethod
    def isDefined(self, name: String) -> bool:
        """
        Determines whether units with the specified name are defined.
        
        Parameters
        -----------
        name : String
            the string by which the units are known (e.g., "farad")
        
        Returns
        --------
        output : bool
            true, if the units are currently defined; false, otherwise.
        """
