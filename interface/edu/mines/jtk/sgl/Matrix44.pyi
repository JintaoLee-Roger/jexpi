from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class Matrix44:
    """
    A 4-by-4 matrix.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an identity matrix.
        """

    @overload
    def __init__(self, m00: double, m01: double, m02: double, m03: double,
                 m10: double, m11: double, m12: double, m13: double,
                 m20: double, m21: double, m22: double, m23: double,
                 m30: double, m31: double, m32: double, m33: double) -> None:
        """
        Constructs a matrix with specified elements.
        
        Parameters
        -----------
        m00 : double
            the element with (row,col) indices (0,0)
        m01 : double
            the element with (row,col) indices (0,1)
        m02 : double
            the element with (row,col) indices (0,2)
        m03 : double
            the element with (row,col) indices (0,3)
        m10 : double
            the element with (row,col) indices (1,0)
        m11 : double
            the element with (row,col) indices (1,1)
        m12 : double
            the element with (row,col) indices (1,2)
        m13 : double
            the element with (row,col) indices (1,3)
        m20 : double
            the element with (row,col) indices (2,0)
        m21 : double
            the element with (row,col) indices (2,1)
        m22 : double
            the element with (row,col) indices (2,2)
        m23 : double
            the element with (row,col) indices (2,3)
        m30 : double
            the element with (row,col) indices (3,0)
        m31 : double
            the element with (row,col) indices (3,1)
        m32 : double
            the element with (row,col) indices (3,2)
        m33 : double
            the element with (row,col) indices (3,3)
        """

    @overload
    def __init__(self, m: Double1D) -> None:
        """
        Constructs a matrix with specified elements. The specified array of
        elements is referenced by (not copied into) the constructed matrix.
        Therefore, any changes to the matrix will be reflected in changes to
        the elements of the specified array.
        
        Parameters
        -----------
        m : Double1D
            the array[16] of matrix elements.
        """

    @overload
    def __init__(self, m: Matrix44) -> None:
        """
        Constructs a copy of the specified matrix.
        
        Parameters
        -----------
        m : Matrix44
            the matrix.
        """

    def set(self, m00: double, m01: double, m02: double, m03: double,
            m10: double, m11: double, m12: double, m13: double, m20: double,
            m21: double, m22: double, m23: double, m30: double, m31: double,
            m32: double, m33: double) -> None:
        """
        Sets all elements of this matrix.
        
        Parameters
        -----------
        m00 : double
            the element with (row,col) indices (0,0)
        m01 : double
            the element with (row,col) indices (0,1)
        m02 : double
            the element with (row,col) indices (0,2)
        m03 : double
            the element with (row,col) indices (0,3)
        m10 : double
            the element with (row,col) indices (1,0)
        m11 : double
            the element with (row,col) indices (1,1)
        m12 : double
            the element with (row,col) indices (1,2)
        m13 : double
            the element with (row,col) indices (1,3)
        m20 : double
            the element with (row,col) indices (2,0)
        m21 : double
            the element with (row,col) indices (2,1)
        m22 : double
            the element with (row,col) indices (2,2)
        m23 : double
            the element with (row,col) indices (2,3)
        m30 : double
            the element with (row,col) indices (3,0)
        m31 : double
            the element with (row,col) indices (3,1)
        m32 : double
            the element with (row,col) indices (3,2)
        m33 : double
            the element with (row,col) indices (3,3)
        """

    def inverse(self) -> Matrix44:
        """
        Returns the inverse Minv of this matrix M.
        Returns
        --------
        output : Matrix44
            the inverse Minv.
        """

    def inverseEquals(self) -> Matrix44:
        """
        Replaces this matrix M with its inverse Minv.
        Returns
        --------
        output : Matrix44
            this matrix, inverted.
        """

    def transpose(self) -> Matrix44:
        """
        Returns the transpose M' of this matrix M.
        Returns
        --------
        output : Matrix44
            the transpose M'.
        """

    def transposeEquals(self) -> Matrix44:
        """
        Replaces this matrix M with its transpose M'.
        Returns
        --------
        output : Matrix44
            this matrix, transposed.
        """

    @overload
    def times(self, a: Matrix44) -> Matrix44:
        """
        Returns the product MA of this matrix M and a matrix A.
        
        Parameters
        -----------
        a : Matrix44
            the matrix A.
        
        Returns
        --------
        output : Matrix44
            the product MA.
        """

    def timesEquals(self, a: Matrix44) -> Matrix44:
        """
        Replaces this matrix M with the matrix product MA.
        
        Parameters
        -----------
        a : Matrix44
            the matrix A.
        
        Returns
        --------
        output : Matrix44
            the product MA.
        """

    def timesTranspose(self, a: Matrix44) -> Matrix44:
        """
        Returns the product MA' of this matrix M and the transpose of a matrix A.
        
        Parameters
        -----------
        a : Matrix44
            the matrix A.
        
        Returns
        --------
        output : Matrix44
            the product MA'.
        """

    def timesTransposeEquals(self, a: Matrix44) -> Matrix44:
        """
        Replaces this matrix M with the matrix product MA'.
        
        Parameters
        -----------
        a : Matrix44
            the matrix A.
        
        Returns
        --------
        output : Matrix44
            the product MA'.
        """

    @overload
    def transposeTimes(self, a: Matrix44) -> Matrix44:
        """
        Returns the product M'A of the transpose of this matrix M and a matrix A.
        
        Parameters
        -----------
        a : Matrix44
            the matrix A.
        
        Returns
        --------
        output : Matrix44
            the product M'A.
        """

    def transposeTimesEquals(self, a: Matrix44) -> Matrix44:
        """
        Replaces this matrix M with the matrix product M'A.
        
        Parameters
        -----------
        a : Matrix44
            the matrix A.
        
        Returns
        --------
        output : Matrix44
            the product M'A.
        """

    @overload
    def times(self, p: Point3) -> Point3:
        """
        Returns the product Mp of this matrix M and a point p.
        The coordinate w of the specified point is assumed to equal 1.0;
        and the returned point is homogenized, that is, scaled such that
        its coordinate w equals 1.0.
        
        Parameters
        -----------
        p : Point3
            the point p.
        
        Returns
        --------
        output : Point3
            the product Mp.
        """

    @overload
    def times(self, p: Point4) -> Point4:
        """
        Returns the product Mp of this matrix M and a point p.
        
        Parameters
        -----------
        p : Point4
            the point p.
        
        Returns
        --------
        output : Point4
            the product Mp.
        """

    @overload
    def transposeTimes(self, p: Point3) -> Point3:
        """
        Returns the product M'p of the transpose of this matrix M and a point p.
        The coordinate w of the specified point is assumed to equal 1.0; and
        the returned point is homogenized, that is, scaled such that its
        coordinate w equals 1.0.
        
        Parameters
        -----------
        p : Point3
            the point p.
        
        Returns
        --------
        output : Point3
            the product M'p.
        """

    @overload
    def transposeTimes(self, p: Point4) -> Point4:
        """
        Returns the product M'p of the transpose of this matrix M and a point p.
        
        Parameters
        -----------
        p : Point4
            the point p.
        
        Returns
        --------
        output : Point4
            the product M'p.
        """

    @overload
    def times(self, v: Vector3) -> Vector3:
        """
        Returns the product Mv of this matrix M and a vector v.
        Uses only the upper-left 3-by-3 elements of this matrix.
        
        Parameters
        -----------
        v : Vector3
            the vector v.
        
        Returns
        --------
        output : Vector3
            the product Mv.
        """

    @overload
    def transposeTimes(self, v: Vector3) -> Vector3:
        """
        Returns the product M'v of the transpose of this matrix M and a vector v.
        Uses only the upper-left 3-by-3 elements of this matrix.
        
        Parameters
        -----------
        v : Vector3
            the vector v.
        
        Returns
        --------
        output : Vector3
            the product M'v.
        """

    @staticmethod
    def identity(self) -> Matrix44:
        """
        Returns a new identity matrix.
        Returns
        --------
        output : Matrix44
            an identity matrix.
        """

    @overload
    @staticmethod
    def translate(self, tx: double, ty: double, tz: double) -> Matrix44:
        """
        Returns a new translation matrix.
        
        Parameters
        -----------
        tx : double
            the x component of the translation.
        ty : double
            the y component of the translation.
        tz : double
            the z component of the translation.
        
        Returns
        --------
        output : Matrix44
            the translation matrix.
        """

    @overload
    @staticmethod
    def translate(self, tv: Vector3) -> Matrix44:
        """
        Returns a new translation matrix.
        
        Parameters
        -----------
        tv : Vector3
            the translation vector.
        
        Returns
        --------
        output : Matrix44
            the translation matrix.
        """

    @staticmethod
    def scale(self, sx: double, sy: double, sz: double) -> Matrix44:
        """
        Returns a new scaling matrix.
        
        Parameters
        -----------
        sx : double
            the x component of the scaling.
        sy : double
            the y component of the scaling.
        sz : double
            the z component of the scaling.
        
        Returns
        --------
        output : Matrix44
            the scaling matrix.
        """

    @overload
    @staticmethod
    def rotate(self, ra: double, rx: double, ry: double,
               rz: double) -> Matrix44:
        """
        Returns a new rotation matrix.
        The rotation is about a specified vector axis.
        
        Parameters
        -----------
        ra : double
            the angle of rotation, in degrees.
        rx : double
            the x component of the vector axis of rotation
        ry : double
            the y component of the vector axis of rotation
        rz : double
            the z component of the vector axis of rotation
        
        Returns
        --------
        output : Matrix44
            the rotation matrix.
        """

    @overload
    @staticmethod
    def rotate(self, ra: double, rv: Vector3) -> Matrix44:
        """
        Returns a new rotation matrix.
        The rotation is about a specified vector axis.
        
        Parameters
        -----------
        ra : double
            the angle of rotation, in degrees.
        rv : Vector3
            the vector axis of rotation.
        
        Returns
        --------
        output : Matrix44
            the rotation matrix.
        """

    @staticmethod
    def rotateX(self, ra: double) -> Matrix44:
        """
        Returns a new rotation matrix.
        The rotation is about the x axis.
        
        Parameters
        -----------
        ra : double
            the angle of rotation, in degrees.
        
        Returns
        --------
        output : Matrix44
            the rotation matrix.
        """

    @staticmethod
    def rotateY(self, ra: double) -> Matrix44:
        """
        Returns a new rotation matrix.
        The rotation is about the y axis.
        
        Parameters
        -----------
        ra : double
            the angle of rotation, in degrees.
        
        Returns
        --------
        output : Matrix44
            the rotation matrix.
        """

    @staticmethod
    def rotateZ(self, ra: double) -> Matrix44:
        """
        Returns a new rotation matrix.
        The rotation is about the z axis.
        
        Parameters
        -----------
        ra : double
            the angle of rotation, in degrees.
        
        Returns
        --------
        output : Matrix44
            the rotation matrix.
        """

    @staticmethod
    def ortho(self, left: double, right: double, bottom: double, top: double,
              znear: double, zfar: double) -> Matrix44:
        """
        Returns a new orthographic-projection matrix. Parameters
        correspond to those for the OpenGL standard function glOrtho.
        
        Parameters
        -----------
        left : double
            the coordinate for the left clipping plane.
        right : double
            the coordinate for the right clipping plane.
        bottom : double
            the coordinate for the bottom clipping plane.
        top : double
            the coordinate for the top clipping plane.
        znear : double
            the distance to the near depth clipping plane
        zfar : double
            the distance to the far depth clipping plane
        
        Returns
        --------
        output : Matrix44
            the orthographic-projection matrix.
        """

    @staticmethod
    def frustum(self, left: double, right: double, bottom: double, top: double,
                znear: double, zfar: double) -> Matrix44:
        """
        Returns a new perspective-projection matrix. Parameters
        correspond to those for the OpenGL standard function glFrustum.
        
        Parameters
        -----------
        left : double
            the coordinate for the left clipping plane.
        right : double
            the coordinate for the right clipping plane.
        bottom : double
            the coordinate for the bottom clipping plane.
        top : double
            the coordinate for the top clipping plane.
        znear : double
            the distance to the near depth clipping plane
        zfar : double
            the distance to the far depth clipping plane
        
        Returns
        --------
        output : Matrix44
            the perspective-projection matrix.
        """

    @staticmethod
    def perspective(self, fovy: double, aspect: double, znear: double,
                    zfar: double) -> Matrix44:
        """
        Returns a new perspective-projection matrix. Parameters correspond
        to those for the OpenGL standard function gluPerspective.
        
        Parameters
        -----------
        fovy : double
            the field of view, in degrees, in the vertical direction.
        aspect : double
            the aspect ratio width/height.
        znear : double
            the distance to the near depth clipping plane
        zfar : double
            the distance to the far depth clipping plane
        
        Returns
        --------
        output : Matrix44
            this perspective-projection matrix.
        """

    def setIdentity(self) -> Matrix44:
        """
        Sets this matrix to an identity matrix.
        Returns
        --------
        output : Matrix44
            this identity matrix.
        """

    @overload
    def setTranslate(self, tx: double, ty: double, tz: double) -> Matrix44:
        """
        Sets this matrix to a translation-only matrix.
        
        Parameters
        -----------
        tx : double
            the x component of the translation.
        ty : double
            the y component of the translation.
        tz : double
            the z component of the translation.
        
        Returns
        --------
        output : Matrix44
            this translation-only matrix.
        """

    @overload
    def setTranslate(self, tv: Vector3) -> Matrix44:
        """
        Sets this matrix to a translation-only matrix.
        
        Parameters
        -----------
        tv : Vector3
            the translation vector.
        
        Returns
        --------
        output : Matrix44
            this translation-only matrix.
        """

    def setScale(self, sx: double, sy: double, sz: double) -> Matrix44:
        """
        Sets this matrix to a scaling-only matrix.
        
        Parameters
        -----------
        sx : double
            the x component of the scaling.
        sy : double
            the y component of the scaling.
        sz : double
            the z component of the scaling.
        
        Returns
        --------
        output : Matrix44
            this scaling-only matrix.
        """

    @overload
    def setRotate(self, ra: double, rx: double, ry: double,
                  rz: double) -> Matrix44:
        """
        Sets this matrix to a rotation-only matrix.
        The rotation is about a specified vector axis.
        
        Parameters
        -----------
        ra : double
            the angle of rotation, in degrees.
        rx : double
            the x component of the vector axis of rotation
        ry : double
            the y component of the vector axis of rotation
        rz : double
            the z component of the vector axis of rotation
        
        Returns
        --------
        output : Matrix44
            this rotation-only matrix.
        """

    @overload
    def setRotate(self, ra: double, rv: Vector3) -> Matrix44:
        """
        Sets this matrix to a rotation-only matrix.
        The rotation is about a specified axis.
        
        Parameters
        -----------
        ra : double
            the angle of rotation, in degrees.
        rv : Vector3
            the vector axis of rotation.
        
        Returns
        --------
        output : Matrix44
            this rotation-only matrix.
        """

    def setRotateX(self, ra: double) -> Matrix44:
        """
        Sets this matrix to a rotation-only matrix.
        The rotation is about the x axis.
        
        Parameters
        -----------
        ra : double
            the angle of rotation, in degrees.
        
        Returns
        --------
        output : Matrix44
            this rotation-only matrix.
        """

    def setRotateY(self, ra: double) -> Matrix44:
        """
        Sets this matrix to a rotation-only matrix.
        The rotation is about the y axis.
        
        Parameters
        -----------
        ra : double
            the angle of rotation, in degrees.
        
        Returns
        --------
        output : Matrix44
            this rotation-only matrix.
        """

    def setRotateZ(self, ra: double) -> Matrix44:
        """
        Sets this matrix to a rotation-only matrix.
        The rotation is about the z axis.
        
        Parameters
        -----------
        ra : double
            the angle of rotation, in degrees.
        
        Returns
        --------
        output : Matrix44
            this rotation-only matrix.
        """

    def setOrtho(self, left: double, right: double, bottom: double,
                 top: double, znear: double, zfar: double) -> Matrix44:
        """
        Sets this matrix to a orthographic-projection matrix. Parameters
        correspond to those for the OpenGL standard function glOrtho.
        
        Parameters
        -----------
        left : double
            the coordinate for the left clipping plane.
        right : double
            the coordinate for the right clipping plane.
        bottom : double
            the coordinate for the bottom clipping plane.
        top : double
            the coordinate for the top clipping plane.
        znear : double
            the distance to the near depth clipping plane
        zfar : double
            the distance to the far depth clipping plane
        
        Returns
        --------
        output : Matrix44
            this orthographic-projection matrix.
        """

    def setFrustum(self, left: double, right: double, bottom: double,
                   top: double, znear: double, zfar: double) -> Matrix44:
        """
        Sets this matrix to a perspective-projection matrix. Parameters
        correspond to those for the OpenGL standard function glFrustum.
        
        Parameters
        -----------
        left : double
            the coordinate for the left clipping plane.
        right : double
            the coordinate for the right clipping plane.
        bottom : double
            the coordinate for the bottom clipping plane.
        top : double
            the coordinate for the top clipping plane.
        znear : double
            the distance to the near depth clipping plane
        zfar : double
            the distance to the far depth clipping plane
        
        Returns
        --------
        output : Matrix44
            this perspective-projection matrix.
        """

    def setPerspective(self, fovy: double, aspect: double, znear: double,
                       zfar: double) -> Matrix44:
        """
        Sets this matrix to a perspective-projection matrix. Parameters
        correspond to those for the OpenGL standard function gluPerspective.
        
        Parameters
        -----------
        fovy : double
            the field of view, in degrees, in the vertical direction.
        aspect : double
            the aspect ratio width/height.
        znear : double
            the distance to the near depth clipping plane
        zfar : double
            the distance to the far depth clipping plane
        
        Returns
        --------
        output : Matrix44
            this perspective-projection matrix.
        """

    def toString(self) -> String:
        """
    
        """
