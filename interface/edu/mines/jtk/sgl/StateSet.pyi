from typing import overload
from edu.mines.jtk.mapping import *


class StateSet:
    """
    A set of OpenGL states. State sets can be associated with nodes in
    a scene graph. During the draw process for a node, these states are
    applied in the method {@link Node#drawBegin(DrawContext)}, before
    the method {@link Node#draw(DrawContext)} is called.
    
    If two states of the same class with the same attributes are added
    to a state set, then the order in which those states are applied
    is undefined. Generally,
    Nothing prevents two states of the same class from being added to
    the same state set. Howev
    """

    @staticmethod
    def forTwoSidedShinySurface(self, color: Color) -> StateSet:
        """
        Returns a new state set with color, light model, and material states.
        The specified color is used only when per-vertex colors are not used.
        The light model state is set for two-sided lighting. The material
        state is set with color material ambient and diffuse, specular color
        white, and shininess set to 100.
        
        This method exists only to provide a simple way to construct a commonly
        used state set. It does nothing that cannot be accomplished (more
        tediously) by constructing a state set and adding each of its states
        using other methods.
        
        Parameters
        -----------
        color : Color
            the color to be set.
        
        Returns
        --------
        output : StateSet
            the state set.
        """

    def add(self, state: State) -> None:
        """
        Adds the specified state to this set.
        
        Parameters
        -----------
        state : State
            the state.
        """

    def remove(self, state: State) -> None:
        """
        Removes the specified state from this set.
        
        Parameters
        -----------
        state : State
            the state.
        """

    def contains(self, stateClass: Class) -> bool:
        """
        Determines whether this set contains a state of the specified class.
        
        Parameters
        -----------
        stateClass : Class
            the state class.
        
        Returns
        --------
        output : bool
            true; if this state contains such a state; false, otherwise.
        """

    def find(self, stateClass: Class) -> State:
        """
        Finds a state in this set of the specified class.
        
        Parameters
        -----------
        stateClass : Class
            the state class.
        
        Returns
        --------
        output : State
            the state; null, if the set contains no such state.
        """

    def getStates(self) -> Iterator:
        """
        Gets an iterator for all states in this set.
        Returns
        --------
        output : Iterator
            the iterator.
        """

    def getBlendState(self) -> BlendState:
        """
        Gets the blend state in this set, if present.
        Returns
        --------
        output : BlendState
            the blend state; null, if none.
        """

    def getColorState(self) -> ColorState:
        """
        Gets the color state in this set, if present.
        Returns
        --------
        output : ColorState
            the color state; null, if none.
        """

    def getLightModelState(self) -> LightModelState:
        """
        Gets the light model state in this set, if present.
        Returns
        --------
        output : LightModelState
            the light model state; null, if none.
        """

    def getLineState(self) -> LineState:
        """
        Gets the line state in this set, if present.
        Returns
        --------
        output : LineState
            the line state; null, if none.
        """

    def getMaterialState(self) -> MaterialState:
        """
        Gets the material state in this set, if present.
        Returns
        --------
        output : MaterialState
            the material state; null, if none.
        """

    def getPointState(self) -> PointState:
        """
        Gets the point state in this set, if present.
        Returns
        --------
        output : PointState
            the point state; null, if none.
        """

    def getPolygonState(self) -> PolygonState:
        """
        Gets the polygon state in this set, if present.
        Returns
        --------
        output : PolygonState
            the polygon state; null, if none.
        """

    def apply(self) -> None:
        """
        Applies all states in this set.
        """

    def getAttributeBits(self) -> int:
        """
        Gets the combined attribute bits for all states in this set.
        Returns
        --------
        output : int
            the attribute bits.
        """
