from typing import overload
from edu.mines.jtk.mapping import *


class Localize:
    """
    Localize messages for end users, using a Formatter pattern and a
    localized resource bundle.
    In a class like MyPanel.java you might have lines like this:
    <pre>
    double value = 3.14;
    String msg = "The value "+value+" is too large";
    </pre>
    Instead, in the same package as MyPanel.java, create a file
    MyPanel.properties, with this line:
    <pre>
    too_large = The value %g is too large.
    </pre>
    Then you can replace the original lines by this.
    <pre>
    private static Localize local = new Localize(MyPanel.class);
    ...
    double value = 3.14;
    String msg = local.format("too_large", value);
    </pre>
    If you create an additional file called MyPanel_es.properties, then
    that file will be used automatically in Spanish-speaking locales.
    """

    @overload
    def __init__(self, clazz: Class) -> None:
        """
        Construct for localized messages.
        Class&lt;Foo&gt; is assumed to have property files Foo.properties,
        Foo_es.properties, etc. Uses default Locale.
        
        Parameters
        -----------
        clazz : Class
            Name of client class that requires localization
        """

    @overload
    def __init__(self, clazz: Class, resourceBundleName: String) -> None:
        """
        Construct for localized messages.
        localizing messages. If null, then Class&lt;Foo&gt; is assumed to have
        property files Foo.properties, Foo_es.properties, etc. Uses default
        Locale.
        
        Parameters
        -----------
        clazz : Class
            Name of client class that requires localization
        resourceBundleName : String
            Name of ResourceBundle to be used for
        """

    @overload
    def __init__(self, clazz: Class, resourceBundleName: String,
                 locale: Locale) -> None:
        """
        Construct for localized messages.
        localizing messages. If null, then Class&lt;Foo&gt; is assumed to have
        property files Foo.properties, Foo_es.properties, etc.
        default Locale.
        
        Parameters
        -----------
        clazz : Class
            Name of client class that requires localization
        resourceBundleName : String
            Name of ResourceBundle to be used for
        locale : Locale
            Locale to use for localization. If null, then will use
        """

    def format(self, key: String, args: Object) -> String:
        """
        Format a localized message, with java.util.Formatter and the appropriate
        resource.
        found, then will be used as the format.
        
        Parameters
        -----------
        key : String
            used to specify format string in properties file. If not
        args : Object
            Optional arguments to be passed to Formatter.format method.
        
        Returns
        --------
        output : String
            formatted localized String
        """

    @staticmethod
    def getResourceBundle(self, clazz: Class, resourceBundleName: String,
                          locale: Locale) -> ResourceBundle:
        """
        Get a resource bundle associated with a class.
        localizing messages. If null, then Class&lt;Foo&gt; is assumed to have
        property files Foo.properties, Foo_es.properties, etc.
        default Locale.
        
        Parameters
        -----------
        clazz : Class
            Name of client class that requires resource bundle.
        resourceBundleName : String
            Name of ResourceBundle to be used for
        locale : Locale
            Locale to use for localization. If null, then will use
        
        Returns
        --------
        output : ResourceBundle
            ResourceBundle for this locale.
        """

    @staticmethod
    def getMessage(self, throwable: Throwable) -> String:
        """
        Get the best localized message from a Throwable that may contain other Throwables as a cause.
        
        Parameters
        -----------
        throwable : Throwable
            a Throwable that may contain other Throwables as a cause.
        
        Returns
        --------
        output : String
            best localized message, unwrapping as necessary.
        """

    def toString(self) -> String:
        """
    
        """

    @overload
    @staticmethod
    def filter(self, message: String, catalog: ResourceBundle) -> String:
        """
        Filter the specified string with the specified resource bundle.
        """

    @overload
    @staticmethod
    def filter(self, message: String, resourceClass: Class) -> String:
        """
        Filter the specified string with a ResourceBundle
        """

    @staticmethod
    def timeWords(self, seconds: long) -> String:
        """
        Convert a number of seconds into words
        """
