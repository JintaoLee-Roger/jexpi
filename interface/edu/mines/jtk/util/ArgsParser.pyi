from typing import overload
from edu.mines.jtk.mapping import *


class ArgsParser:
    """
    Parses command-line arguments for options and values, using conventions
    like those used by the UNIX function getopt; e.g., "-a". Also supports
    GNU-style long options; e.g., "--alpha".
    
    Short options in command-line arguments have the form "-a". A short
    options may have a value, as in "-a3.14" or "-a 3.14". Multiple short
    options without values may be specified together, so that "-ab" is
    equivalent to "-a -b". (Note that if a value is expected for option
    "-a", then "-ab" specifies "b" as that value.)
    
    Long options in command-line arguments have the form "--alpha". A long
    option may also have a value, as in "--alpha=3.14" or "--alpha 3.14".
    Long option names may be abbreviated, provided that the abbreviation is
    unique among all long options. For example, "--a=3.14" is equivalent to
    "--alpha=3.14", provided that no other long option begins with "--a".
    
    For both short and long options, it is an error to specify a value where
    one is not expected, or to omit a value where one is expected.
    
    Option parsing ends with the first argument that is not an option, i.e.,
    one that does not begin with a hyphen "-". As a special case, parsing
    also ends after the special option "--".
    
    Typical usage within the standard method main is:
    <pre><code>
    public static void main(String[] args) {
    float a = 3.14f;
    boolean b = false;
    String fileName = null;
    try {
    String shortOpts = "ha:b";
    String[] longOpts = {"help","alpha=","beta"};
    ArgsParser ap = new ArgsParser(args,shortOpts,longOpts);
    String[] opts = ap.getOptions();
    String[] vals = ap.getValues();
    for (int i=0; i&lt;opts.length; ++i) {
    String opt = opts[i];
    String val = vals[i];
    if (opt.equals("-h") || opt.equals("--help")) {
    printUsageAndExit(0);
    } else if (opt.equals("-a") || opt.equals("--alpha")) {
    a = ap.toFloat(val);
    } else if (opt.equals("-b") || opt.equals("--beta")) {
    b = true;
    }
    }
    args = ap.getOtherArgs();
    if (args.length!=1)
    printUsageAndExit(-1);
    fileName = args[0];
    } catch (OptionException oe) {
    System.err.println(oe.getMessage());
    printUsageAndExit(-1);
    }
    // ...
    }
    </code></pre>
    """

    @overload
    def __init__(self, args: String1D, shortOpts: String) -> None:
        """
        Constructs an argument parser for the specified arguments and
        short options specification.
        specified by a single character. For options that require values,
        this character must be followed by a single colon ':'. For example,
        "a:b" specifies two options "-a" and "-b", and the first option "-a"
        requires a value.
        
        Parameters
        -----------
        args : String1D
            the command-line arguments, as passed to the method main.
        shortOpts : String
            the short options specification. Each option is
        """

    @overload
    def __init__(self, args: String1D, shortOpts: String,
                 longOpts: String1D) -> None:
        """
        Constructs an argument parser for the specified arguments and
        short and long options specifications.
        specified by a single character. For options that require values,
        this character must be followed by a single colon ':'. For example,
        "a:b" specifies two options "-a" and "-b", and the first option "-a"
        requires a value.
        is specified by a single string, containing the long option name.
        For options that require values, this string must end in the
        character "=". For example, the string "--alpha=" specifies a
        long option "--alpha" that requires a value.
        
        Parameters
        -----------
        args : String1D
            the command-line arguments, as passed to the method main.
        shortOpts : String
            the short options specification. Each option is
        longOpts : String1D
            the long options specification. Each option is
        """

    def getOptions(self) -> String1D:
        """
        Gets the options parsed.
        Each string is of the form "-a", for short options, or "--alpha", for
        long options. Note that the hyphen "-" or double-hyphen "--" is
        included in the strings. For long options, the complete names are
        returned, even if abbreviations were parsed.
        Returns
        --------
        output : String1D
            the options parsed.
        """

    def getValues(self) -> String1D:
        """
        Gets the values corresponding to the options parsed.
        The value is null for any option that does not expect a value.
        Returns
        --------
        output : String1D
            the values parsed.
        """

    def getOtherArgs(self) -> String1D:
        """
        Gets the other arguments, those that do not correspond to options.
        Returns
        --------
        output : String1D
            the other arguments.
        """

    @staticmethod
    def toBoolean(self, s: String) -> bool:
        """
        Converts a string value to a boolean.
        
        Parameters
        -----------
        s : String
            the string value.
        
        Returns
        --------
        output : bool
            the boolean.
        """

    @staticmethod
    def toDouble(self, s: String) -> double:
        """
        Converts a string value to a double.
        
        Parameters
        -----------
        s : String
            the string value.
        
        Returns
        --------
        output : double
            the double.
        """

    @staticmethod
    def toFloat(self, s: String) -> float:
        """
        Converts a string value to a float.
        
        Parameters
        -----------
        s : String
            the string value.
        
        Returns
        --------
        output : float
            the float.
        """

    @staticmethod
    def toInt(self, s: String) -> int:
        """
        Converts a string value to an int.
        
        Parameters
        -----------
        s : String
            the string value.
        
        Returns
        --------
        output : int
            the int.
        """

    @staticmethod
    def toLong(self, s: String) -> long:
        """
        Converts a string value to a long.
        
        Parameters
        -----------
        s : String
            the string value.
        
        Returns
        --------
        output : long
            the long.
        """
