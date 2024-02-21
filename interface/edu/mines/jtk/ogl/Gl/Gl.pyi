from typing import overload
from edu.mines.jtk.mapping import *

GL_AMBIENT_AND_DIFFUSE = 0

class Gl:
    """
    OpenGL standard constants and functions.
    """

    @staticmethod
    def glActiveTexture(self, texture: int) -> None:
        """
    
        """

    @staticmethod
    def glBindBuffer(self, target: int, buffer: int) -> None:
        """
    
        """

    @staticmethod
    def glBindFramebuffer(self, target: int, framebuffer: int) -> None:
        """
    
        """

    @staticmethod
    def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None:
        """
    
        """

    @staticmethod
    def glBindTexture(self, target: int, texture: int) -> None:
        """
    
        """

    @staticmethod
    def glBlendEquation(self, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glBlendEquationSeparate(self, modeRGB: int, modeAlpha: int) -> None:
        """
    
        """

    @staticmethod
    def glBlendFunc(self, sfactor: int, dfactor: int) -> None:
        """
    
        """

    @staticmethod
    def glBlendFuncSeparate(self, sfactorRGB: int, dfactorRGB: int,
                            sfactorAlpha: int, dfactorAlpha: int) -> None:
        """
    
        """

    @staticmethod
    def glBufferData(self, target: int, size: long, data: Buffer,
                     usage: int) -> None:
        """
    
        """

    @staticmethod
    def glBufferSubData(self, target: int, offset: long, size: long,
                        data: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCheckFramebufferStatus(self, target: int) -> int:
        """
    
        """

    @staticmethod
    def glClear(self, mask: int) -> None:
        """
    
        """

    @staticmethod
    def glClearColor(self, red: float, green: float, blue: float,
                     alpha: float) -> None:
        """
    
        """

    @staticmethod
    def glClearDepthf(self, d: float) -> None:
        """
    
        """

    @staticmethod
    def glClearStencil(self, s: int) -> None:
        """
    
        """

    @staticmethod
    def glColorMask(self, red: bool, green: bool, blue: bool,
                    alpha: bool) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCompressedTexImage2D(self, target: int, level: int,
                               internalformat: int, width: int, height: int,
                               border: int, imageSize: int,
                               data: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCompressedTexImage2D(self, target: int, level: int,
                               internalformat: int, width: int, height: int,
                               border: int, imageSize: int,
                               data_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCompressedTexSubImage2D(self, target: int, level: int, xoffset: int,
                                  yoffset: int, width: int, height: int,
                                  format: int, imageSize: int,
                                  data: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCompressedTexSubImage2D(self, target: int, level: int, xoffset: int,
                                  yoffset: int, width: int, height: int,
                                  format: int, imageSize: int,
                                  data_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glCopyTexImage2D(self, target: int, level: int, internalformat: int,
                         x: int, y: int, width: int, height: int,
                         border: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyTexSubImage2D(self, target: int, level: int, xoffset: int,
                            yoffset: int, x: int, y: int, width: int,
                            height: int) -> None:
        """
    
        """

    @staticmethod
    def glCullFace(self, mode: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteBuffers(self, n: int, buffers: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteBuffers(self, n: int, buffers: Int1D,
                        buffers_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteFramebuffers(self, n: int, framebuffers: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteFramebuffers(self, n: int, framebuffers: Int1D,
                             framebuffers_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteRenderbuffers(self, n: int, renderbuffers: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteRenderbuffers(self, n: int, renderbuffers: Int1D,
                              renderbuffers_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteTextures(self, n: int, textures: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteTextures(self, n: int, textures: Int1D,
                         textures_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glDepthFunc(self, func: int) -> None:
        """
    
        """

    @staticmethod
    def glDepthMask(self, flag: bool) -> None:
        """
    
        """

    @staticmethod
    def glDepthRangef(self, n: float, f: float) -> None:
        """
    
        """

    @staticmethod
    def glDisable(self, cap: int) -> None:
        """
    
        """

    @staticmethod
    def glDrawArrays(self, mode: int, first: int, count: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawElements(self, mode: int, count: int, type: int,
                       indices_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glEnable(self, cap: int) -> None:
        """
    
        """

    @staticmethod
    def glFinish(self) -> None:
        """
    
        """

    @staticmethod
    def glFlush(self) -> None:
        """
    
        """

    @staticmethod
    def glFramebufferRenderbuffer(self, target: int, attachment: int,
                                  renderbuffertarget: int,
                                  renderbuffer: int) -> None:
        """
    
        """

    @staticmethod
    def glFramebufferTexture2D(self, target: int, attachment: int,
                               textarget: int, texture: int,
                               level: int) -> None:
        """
    
        """

    @staticmethod
    def glFrontFace(self, mode: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenBuffers(self, n: int, buffers: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenBuffers(self, n: int, buffers: Int1D,
                     buffers_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGenerateMipmap(self, target: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenFramebuffers(self, n: int, framebuffers: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenFramebuffers(self, n: int, framebuffers: Int1D,
                          framebuffers_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenRenderbuffers(self, n: int, renderbuffers: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenRenderbuffers(self, n: int, renderbuffers: Int1D,
                           renderbuffers_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenTextures(self, n: int, textures: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenTextures(self, n: int, textures: Int1D,
                      textures_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetBooleanv(self, pname: int, data: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetBooleanv(self, pname: int, data: Byte1D,
                      data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetBufferParameteriv(self, target: int, pname: int,
                               params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetBufferParameteriv(self, target: int, pname: int, params: Int1D,
                               params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetError(self) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glGetFloatv(self, pname: int, data: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFloatv(self, pname: int, data: Float1D, data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFramebufferAttachmentParameteriv(self, target: int,
                                              attachment: int, pname: int,
                                              params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFramebufferAttachmentParameteriv(self, target: int,
                                              attachment: int, pname: int,
                                              params: Int1D,
                                              params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetIntegerv(self, pname: int, data: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetIntegerv(self, pname: int, data: Int1D, data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetRenderbufferParameteriv(self, target: int, pname: int,
                                     params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetRenderbufferParameteriv(self, target: int, pname: int,
                                     params: Int1D,
                                     params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetString(self, name: int) -> String:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexParameterfv(self, target: int, pname: int,
                            params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexParameterfv(self, target: int, pname: int, params: Float1D,
                            params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexParameteriv(self, target: int, pname: int,
                            params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexParameteriv(self, target: int, pname: int, params: Int1D,
                            params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glHint(self, target: int, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glIsBuffer(self, buffer: int) -> bool:
        """
    
        """

    @staticmethod
    def glIsEnabled(self, cap: int) -> bool:
        """
    
        """

    @staticmethod
    def glIsFramebuffer(self, framebuffer: int) -> bool:
        """
    
        """

    @staticmethod
    def glIsRenderbuffer(self, renderbuffer: int) -> bool:
        """
    
        """

    @staticmethod
    def glIsTexture(self, texture: int) -> bool:
        """
    
        """

    @staticmethod
    def glLineWidth(self, width: float) -> None:
        """
    
        """

    @staticmethod
    def glPixelStorei(self, pname: int, param: int) -> None:
        """
    
        """

    @staticmethod
    def glPolygonOffset(self, factor: float, units: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glReadPixels(self, x: int, y: int, width: int, height: int,
                     format: int, type: int, pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glReadPixels(self, x: int, y: int, width: int, height: int,
                     format: int, type: int,
                     pixels_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glRenderbufferStorage(self, target: int, internalformat: int,
                              width: int, height: int) -> None:
        """
    
        """

    @staticmethod
    def glSampleCoverage(self, value: float, invert: bool) -> None:
        """
    
        """

    @staticmethod
    def glScissor(self, x: int, y: int, width: int, height: int) -> None:
        """
    
        """

    @staticmethod
    def glStencilFunc(self, func: int, ref: int, mask: int) -> None:
        """
    
        """

    @staticmethod
    def glStencilMask(self, mask: int) -> None:
        """
    
        """

    @staticmethod
    def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexImage2D(self, target: int, level: int, internalformat: int,
                     width: int, height: int, border: int, format: int,
                     type: int, pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexImage2D(self, target: int, level: int, internalformat: int,
                     width: int, height: int, border: int, format: int,
                     type: int, pixels_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glTexParameterf(self, target: int, pname: int, param: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexParameterfv(self, target: int, pname: int,
                         params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexParameterfv(self, target: int, pname: int, params: Float1D,
                         params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTexParameteri(self, target: int, pname: int, param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexParameteriv(self, target: int, pname: int,
                         params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexParameteriv(self, target: int, pname: int, params: Int1D,
                         params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexSubImage2D(self, target: int, level: int, xoffset: int,
                        yoffset: int, width: int, height: int, format: int,
                        type: int, pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexSubImage2D(self, target: int, level: int, xoffset: int,
                        yoffset: int, width: int, height: int, format: int,
                        type: int, pixels_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glViewport(self, x: int, y: int, width: int, height: int) -> None:
        """
    
        """

    @staticmethod
    def glTexStorage1D(self, target: int, levels: int, internalformat: int,
                       width: int) -> None:
        """
    
        """

    @staticmethod
    def glTexStorage2D(self, target: int, levels: int, internalformat: int,
                       width: int, height: int) -> None:
        """
    
        """

    @staticmethod
    def glTexStorage3D(self, target: int, levels: int, internalformat: int,
                       width: int, height: int, depth: int) -> None:
        """
    
        """

    @staticmethod
    def glTextureStorage1DEXT(self, texture: int, target: int, levels: int,
                              internalformat: int, width: int) -> None:
        """
    
        """

    @staticmethod
    def glTextureStorage2DEXT(self, texture: int, target: int, levels: int,
                              internalformat: int, width: int,
                              height: int) -> None:
        """
    
        """

    @staticmethod
    def glTextureStorage3DEXT(self, texture: int, target: int, levels: int,
                              internalformat: int, width: int, height: int,
                              depth: int) -> None:
        """
    
        """

    @staticmethod
    def glMapBuffer(self, target: int, access: int) -> ByteBuffer:
        """
    
        """

    @staticmethod
    def glUnmapBuffer(self, target: int) -> bool:
        """
    
        """

    @staticmethod
    def glRenderbufferStorageMultisample(self, target: int, samples: int,
                                         internalformat: int, width: int,
                                         height: int) -> None:
        """
    
        """

    @staticmethod
    def glMapBufferRange(self, target: int, offset: long, length: long,
                         access: int) -> ByteBuffer:
        """
    
        """

    @staticmethod
    def glFlushMappedBufferRange(self, target: int, offset: long,
                                 length: long) -> None:
        """
    
        """

    @staticmethod
    def glGetGraphicsResetStatus(self) -> int:
        """
    
        """

    @staticmethod
    def glReadnPixels(self, x: int, y: int, width: int, height: int,
                      format: int, type: int, bufSize: int,
                      data: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnUniformfv(self, program: int, location: int, bufSize: int,
                        params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnUniformfv(self, program: int, location: int, bufSize: int,
                        params: Float1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnUniformiv(self, program: int, location: int, bufSize: int,
                        params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnUniformiv(self, program: int, location: int, bufSize: int,
                        params: Int1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def isGL(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL4bc(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL4(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL3bc(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL3(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL2(self) -> bool:
        """
    
        """

    @staticmethod
    def isGLES1(self) -> bool:
        """
    
        """

    @staticmethod
    def isGLES2(self) -> bool:
        """
    
        """

    @staticmethod
    def isGLES3(self) -> bool:
        """
    
        """

    @staticmethod
    def isGLES(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL2ES1(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL2ES2(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL2ES3(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL3ES3(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL4ES3(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL2GL3(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL4core(self) -> bool:
        """
    
        """

    @staticmethod
    def isGL3core(self) -> bool:
        """
    
        """

    @staticmethod
    def isGLcore(self) -> bool:
        """
    
        """

    @staticmethod
    def isGLES2Compatible(self) -> bool:
        """
    
        """

    @staticmethod
    def isGLES3Compatible(self) -> bool:
        """
    
        """

    @staticmethod
    def isGLES31Compatible(self) -> bool:
        """
    
        """

    @staticmethod
    def isGLES32Compatible(self) -> bool:
        """
    
        """

    @staticmethod
    def isFunctionAvailable(self, glFunctionName: String) -> bool:
        """
    
        """

    @staticmethod
    def isExtensionAvailable(self, glExtensionName: String) -> bool:
        """
    
        """

    @staticmethod
    def isNPOTTextureAvailable(self) -> bool:
        """
    
        """

    @staticmethod
    def isTextureFormatBGRA8888Available(self) -> bool:
        """
    
        """

    @staticmethod
    def glClearDepth(self, depth: double) -> None:
        """
    
        """

    @staticmethod
    def glDepthRange(self, zNear: double, zFar: double) -> None:
        """
    
        """

    @staticmethod
    def isVBOArrayBound(self) -> bool:
        """
    
        """

    @staticmethod
    def isVBOElementArrayBound(self) -> bool:
        """
    
        """

    @overload
    @staticmethod
    def glLightfv(self, light: int, pname: int, params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLightfv(self, light: int, pname: int, params: Float1D,
                  params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMaterialf(self, face: int, pname: int, param: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMaterialfv(self, face: int, pname: int, params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMaterialfv(self, face: int, pname: int, params: Float1D,
                     params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glColor4f(self, red: float, green: float, blue: float,
                  alpha: float) -> None:
        """
    
        """

    @staticmethod
    def glShadeModel(self, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glMatrixMode(self, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glPushMatrix(self) -> None:
        """
    
        """

    @staticmethod
    def glPopMatrix(self) -> None:
        """
    
        """

    @staticmethod
    def glLoadIdentity(self) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLoadMatrixf(self, m: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLoadMatrixf(self, m: Float1D, m_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultMatrixf(self, m: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultMatrixf(self, m: Float1D, m_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTranslatef(self, x: float, y: float, z: float) -> None:
        """
    
        """

    @staticmethod
    def glRotatef(self, angle: float, x: float, y: float, z: float) -> None:
        """
    
        """

    @staticmethod
    def glScalef(self, x: float, y: float, z: float) -> None:
        """
    
        """

    @staticmethod
    def glOrthof(self, left: float, right: float, bottom: float, top: float,
                 zNear: float, zFar: float) -> None:
        """
    
        """

    @staticmethod
    def glFrustumf(self, left: float, right: float, bottom: float, top: float,
                   zNear: float, zFar: float) -> None:
        """
    
        """

    @staticmethod
    def glEnableClientState(self, arrayName: int) -> None:
        """
    
        """

    @staticmethod
    def glDisableClientState(self, arrayName: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexPointer(self, array: GLArrayData) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexPointer(self, size: int, type: int, stride: int,
                        pointer: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexPointer(self, size: int, type: int, stride: int,
                        pointer_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColorPointer(self, array: GLArrayData) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColorPointer(self, size: int, type: int, stride: int,
                       pointer: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColorPointer(self, size: int, type: int, stride: int,
                       pointer_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormalPointer(self, array: GLArrayData) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormalPointer(self, type: int, stride: int, pointer: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormalPointer(self, type: int, stride: int,
                        pointer_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoordPointer(self, array: GLArrayData) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoordPointer(self, size: int, type: int, stride: int,
                          pointer: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoordPointer(self, size: int, type: int, stride: int,
                          pointer_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glClearIndex(self, c: float) -> None:
        """
    
        """

    @staticmethod
    def glIndexMask(self, mask: int) -> None:
        """
    
        """

    @staticmethod
    def glLineStipple(self, factor: int, pattern: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPolygonStipple(self, mask: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPolygonStipple(self, mask: Byte1D, mask_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPolygonStipple(self, mask: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPolygonStipple(self, mask: Byte1D, mask_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glEdgeFlag(self, flag: bool) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glEdgeFlagv(self, flag: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glEdgeFlagv(self, flag: Byte1D, flag_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glClipPlane(self, plane: int, equation: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glClipPlane(self, plane: int, equation: Double1D,
                    equation_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetClipPlane(self, plane: int, equation: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetClipPlane(self, plane: int, equation: Double1D,
                       equation_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glPushAttrib(self, mask: int) -> None:
        """
    
        """

    @staticmethod
    def glPopAttrib(self) -> None:
        """
    
        """

    @staticmethod
    def glRenderMode(self, mode: int) -> int:
        """
    
        """

    @staticmethod
    def glClearAccum(self, red: float, green: float, blue: float,
                     alpha: float) -> None:
        """
    
        """

    @staticmethod
    def glAccum(self, op: int, value: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLoadMatrixd(self, m: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLoadMatrixd(self, m: Double1D, m_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultMatrixd(self, m: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultMatrixd(self, m: Double1D, m_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glRotated(self, angle: double, x: double, y: double,
                  z: double) -> None:
        """
    
        """

    @staticmethod
    def glScaled(self, x: double, y: double, z: double) -> None:
        """
    
        """

    @staticmethod
    def glTranslated(self, x: double, y: double, z: double) -> None:
        """
    
        """

    @staticmethod
    def glIsList(self, list: int) -> bool:
        """
    
        """

    @staticmethod
    def glDeleteLists(self, list: int, range: int) -> None:
        """
    
        """

    @staticmethod
    def glGenLists(self, range: int) -> int:
        """
    
        """

    @staticmethod
    def glNewList(self, list: int, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glEndList(self) -> None:
        """
    
        """

    @staticmethod
    def glCallList(self, list: int) -> None:
        """
    
        """

    @staticmethod
    def glCallLists(self, n: int, type: int, lists: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glListBase(self, base: int) -> None:
        """
    
        """

    @staticmethod
    def glBegin(self, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glEnd(self) -> None:
        """
    
        """

    @staticmethod
    def glVertex2d(self, x: double, y: double) -> None:
        """
    
        """

    @staticmethod
    def glVertex2f(self, x: float, y: float) -> None:
        """
    
        """

    @staticmethod
    def glVertex2i(self, x: int, y: int) -> None:
        """
    
        """

    @staticmethod
    def glVertex2s(self, x: short, y: short) -> None:
        """
    
        """

    @staticmethod
    def glVertex3d(self, x: double, y: double, z: double) -> None:
        """
    
        """

    @staticmethod
    def glVertex3f(self, x: float, y: float, z: float) -> None:
        """
    
        """

    @staticmethod
    def glVertex3i(self, x: int, y: int, z: int) -> None:
        """
    
        """

    @staticmethod
    def glVertex3s(self, x: short, y: short, z: short) -> None:
        """
    
        """

    @staticmethod
    def glVertex4d(self, x: double, y: double, z: double, w: double) -> None:
        """
    
        """

    @staticmethod
    def glVertex4f(self, x: float, y: float, z: float, w: float) -> None:
        """
    
        """

    @staticmethod
    def glVertex4i(self, x: int, y: int, z: int, w: int) -> None:
        """
    
        """

    @staticmethod
    def glVertex4s(self, x: short, y: short, z: short, w: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex2dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex2dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex2fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex2fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex2iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex2iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex2sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex2sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex3dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex3dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex3fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex3fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex3iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex3iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex3sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex3sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex4dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex4dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex4fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex4fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex4iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex4iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex4sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex4sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glNormal3b(self, nx: byte, ny: byte, nz: byte) -> None:
        """
    
        """

    @staticmethod
    def glNormal3d(self, nx: double, ny: double, nz: double) -> None:
        """
    
        """

    @staticmethod
    def glNormal3i(self, nx: int, ny: int, nz: int) -> None:
        """
    
        """

    @staticmethod
    def glNormal3s(self, nx: short, ny: short, nz: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormal3bv(self, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormal3bv(self, v: Byte1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormal3dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormal3dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormal3fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormal3fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormal3iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormal3iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormal3sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormal3sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glIndexd(self, c: double) -> None:
        """
    
        """

    @staticmethod
    def glIndexf(self, c: float) -> None:
        """
    
        """

    @staticmethod
    def glIndexi(self, c: int) -> None:
        """
    
        """

    @staticmethod
    def glIndexs(self, c: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glIndexdv(self, c: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glIndexdv(self, c: Double1D, c_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glIndexfv(self, c: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glIndexfv(self, c: Float1D, c_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glIndexiv(self, c: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glIndexiv(self, c: Int1D, c_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glIndexsv(self, c: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glIndexsv(self, c: Short1D, c_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glColor3b(self, red: byte, green: byte, blue: byte) -> None:
        """
    
        """

    @staticmethod
    def glColor3d(self, red: double, green: double, blue: double) -> None:
        """
    
        """

    @staticmethod
    def glColor3f(self, red: float, green: float, blue: float) -> None:
        """
    
        """

    @staticmethod
    def glColor3i(self, red: int, green: int, blue: int) -> None:
        """
    
        """

    @staticmethod
    def glColor3s(self, red: short, green: short, blue: short) -> None:
        """
    
        """

    @staticmethod
    def glColor3ub(self, red: byte, green: byte, blue: byte) -> None:
        """
    
        """

    @staticmethod
    def glColor3ui(self, red: int, green: int, blue: int) -> None:
        """
    
        """

    @staticmethod
    def glColor3us(self, red: short, green: short, blue: short) -> None:
        """
    
        """

    @staticmethod
    def glColor4b(self, red: byte, green: byte, blue: byte,
                  alpha: byte) -> None:
        """
    
        """

    @staticmethod
    def glColor4d(self, red: double, green: double, blue: double,
                  alpha: double) -> None:
        """
    
        """

    @staticmethod
    def glColor4i(self, red: int, green: int, blue: int, alpha: int) -> None:
        """
    
        """

    @staticmethod
    def glColor4s(self, red: short, green: short, blue: short,
                  alpha: short) -> None:
        """
    
        """

    @staticmethod
    def glColor4ui(self, red: int, green: int, blue: int, alpha: int) -> None:
        """
    
        """

    @staticmethod
    def glColor4us(self, red: short, green: short, blue: short,
                   alpha: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3bv(self, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3bv(self, v: Byte1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3ubv(self, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3ubv(self, v: Byte1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3uiv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3uiv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3usv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3usv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4bv(self, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4bv(self, v: Byte1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4ubv(self, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4ubv(self, v: Byte1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4uiv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4uiv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4usv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4usv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord1d(self, s: double) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord1f(self, s: float) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord1i(self, s: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord1s(self, s: short) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord2d(self, s: double, t: double) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord2f(self, s: float, t: float) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord2i(self, s: int, t: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord2s(self, s: short, t: short) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord3d(self, s: double, t: double, r: double) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord3f(self, s: float, t: float, r: float) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord3i(self, s: int, t: int, r: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord3s(self, s: short, t: short, r: short) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord4d(self, s: double, t: double, r: double, q: double) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord4f(self, s: float, t: float, r: float, q: float) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord4i(self, s: int, t: int, r: int, q: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord4s(self, s: short, t: short, r: short, q: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord1dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord1dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord1fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord1fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord1iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord1iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord1sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord1sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord2dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord2dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord2fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord2fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord2iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord2iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord2sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord2sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord3dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord3dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord3fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord3fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord3iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord3iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord3sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord3sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord4dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord4dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord4fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord4fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord4iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord4iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord4sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord4sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glRasterPos2d(self, x: double, y: double) -> None:
        """
    
        """

    @staticmethod
    def glRasterPos2f(self, x: float, y: float) -> None:
        """
    
        """

    @staticmethod
    def glRasterPos2i(self, x: int, y: int) -> None:
        """
    
        """

    @staticmethod
    def glRasterPos2s(self, x: short, y: short) -> None:
        """
    
        """

    @staticmethod
    def glRasterPos3d(self, x: double, y: double, z: double) -> None:
        """
    
        """

    @staticmethod
    def glRasterPos3f(self, x: float, y: float, z: float) -> None:
        """
    
        """

    @staticmethod
    def glRasterPos3i(self, x: int, y: int, z: int) -> None:
        """
    
        """

    @staticmethod
    def glRasterPos3s(self, x: short, y: short, z: short) -> None:
        """
    
        """

    @staticmethod
    def glRasterPos4d(self, x: double, y: double, z: double,
                      w: double) -> None:
        """
    
        """

    @staticmethod
    def glRasterPos4f(self, x: float, y: float, z: float, w: float) -> None:
        """
    
        """

    @staticmethod
    def glRasterPos4i(self, x: int, y: int, z: int, w: int) -> None:
        """
    
        """

    @staticmethod
    def glRasterPos4s(self, x: short, y: short, z: short, w: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos2dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos2dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos2fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos2fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos2iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos2iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos2sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos2sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos3dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos3dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos3fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos3fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos3iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos3iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos3sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos3sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos4dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos4dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos4fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos4fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos4iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos4iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos4sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRasterPos4sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glRectd(self, x1: double, y1: double, x2: double, y2: double) -> None:
        """
    
        """

    @staticmethod
    def glRectf(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """
    
        """

    @staticmethod
    def glRecti(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """
    
        """

    @staticmethod
    def glRects(self, x1: short, y1: short, x2: short, y2: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRectdv(self, v1: DoubleBuffer, v2: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRectdv(self, v1: Double1D, v1_offset: int, v2: Double1D,
                 v2_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRectfv(self, v1: FloatBuffer, v2: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRectfv(self, v1: Float1D, v1_offset: int, v2: Float1D,
                 v2_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRectiv(self, v1: IntBuffer, v2: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRectiv(self, v1: Int1D, v1_offset: int, v2: Int1D,
                 v2_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRectsv(self, v1: ShortBuffer, v2: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glRectsv(self, v1: Short1D, v1_offset: int, v2: Short1D,
                 v2_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glLighti(self, light: int, pname: int, param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLightiv(self, light: int, pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLightiv(self, light: int, pname: int, params: Int1D,
                  params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetLightiv(self, light: int, pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetLightiv(self, light: int, pname: int, params: Int1D,
                     params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glLightModeli(self, pname: int, param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLightModeliv(self, pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLightModeliv(self, pname: int, params: Int1D,
                       params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMateriali(self, face: int, pname: int, param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMaterialiv(self, face: int, pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMaterialiv(self, face: int, pname: int, params: Int1D,
                     params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMaterialiv(self, face: int, pname: int,
                        params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMaterialiv(self, face: int, pname: int, params: Int1D,
                        params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glColorMaterial(self, face: int, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glPixelZoom(self, xfactor: float, yfactor: float) -> None:
        """
    
        """

    @staticmethod
    def glPixelTransferf(self, pname: int, param: float) -> None:
        """
    
        """

    @staticmethod
    def glPixelTransferi(self, pname: int, param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelMapfv(self, map: int, mapsize: int,
                     values: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelMapfv(self, map: int, mapsize: int, values: Float1D,
                     values_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelMapfv(self, map: int, mapsize: int,
                     values_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelMapuiv(self, map: int, mapsize: int, values: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelMapuiv(self, map: int, mapsize: int, values: Int1D,
                      values_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelMapuiv(self, map: int, mapsize: int,
                      values_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelMapusv(self, map: int, mapsize: int,
                      values: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelMapusv(self, map: int, mapsize: int, values: Short1D,
                      values_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelMapusv(self, map: int, mapsize: int,
                      values_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelMapfv(self, map: int, values: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelMapfv(self, map: int, values: Float1D,
                        values_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelMapfv(self, map: int, values_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelMapuiv(self, map: int, values: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelMapuiv(self, map: int, values: Int1D,
                         values_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelMapuiv(self, map: int, values_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelMapusv(self, map: int, values: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelMapusv(self, map: int, values: Short1D,
                         values_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelMapusv(self, map: int, values_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glBitmap(self, width: int, height: int, xorig: float, yorig: float,
                 xmove: float, ymove: float, bitmap: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glBitmap(self, width: int, height: int, xorig: float, yorig: float,
                 xmove: float, ymove: float, bitmap: Byte1D,
                 bitmap_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glBitmap(self, width: int, height: int, xorig: float, yorig: float,
                 xmove: float, ymove: float,
                 bitmap_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawPixels(self, width: int, height: int, format: int, type: int,
                     pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawPixels(self, width: int, height: int, format: int, type: int,
                     pixels_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glCopyPixels(self, x: int, y: int, width: int, height: int,
                     type: int) -> None:
        """
    
        """

    @staticmethod
    def glTexGend(self, coord: int, pname: int, param: double) -> None:
        """
    
        """

    @staticmethod
    def glTexGenf(self, coord: int, pname: int, param: float) -> None:
        """
    
        """

    @staticmethod
    def glTexGeni(self, coord: int, pname: int, param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexGendv(self, coord: int, pname: int, params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexGendv(self, coord: int, pname: int, params: Double1D,
                   params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexGenfv(self, coord: int, pname: int, params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexGenfv(self, coord: int, pname: int, params: Float1D,
                   params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexGeniv(self, coord: int, pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexGeniv(self, coord: int, pname: int, params: Int1D,
                   params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexGendv(self, coord: int, pname: int,
                      params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexGendv(self, coord: int, pname: int, params: Double1D,
                      params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexGenfv(self, coord: int, pname: int,
                      params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexGenfv(self, coord: int, pname: int, params: Float1D,
                      params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexGeniv(self, coord: int, pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexGeniv(self, coord: int, pname: int, params: Int1D,
                      params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMap1d(self, target: int, u1: double, u2: double, stride: int,
                order: int, points: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMap1d(self, target: int, u1: double, u2: double, stride: int,
                order: int, points: Double1D, points_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMap1f(self, target: int, u1: float, u2: float, stride: int,
                order: int, points: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMap1f(self, target: int, u1: float, u2: float, stride: int,
                order: int, points: Float1D, points_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMap2d(self, target: int, u1: double, u2: double, ustride: int,
                uorder: int, v1: double, v2: double, vstride: int, vorder: int,
                points: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMap2d(self, target: int, u1: double, u2: double, ustride: int,
                uorder: int, v1: double, v2: double, vstride: int, vorder: int,
                points: Double1D, points_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMap2f(self, target: int, u1: float, u2: float, ustride: int,
                uorder: int, v1: float, v2: float, vstride: int, vorder: int,
                points: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMap2f(self, target: int, u1: float, u2: float, ustride: int,
                uorder: int, v1: float, v2: float, vstride: int, vorder: int,
                points: Float1D, points_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapdv(self, target: int, query: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapdv(self, target: int, query: int, v: Double1D,
                   v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapfv(self, target: int, query: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapfv(self, target: int, query: int, v: Float1D,
                   v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapiv(self, target: int, query: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapiv(self, target: int, query: int, v: Int1D,
                   v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glEvalCoord1d(self, u: double) -> None:
        """
    
        """

    @staticmethod
    def glEvalCoord1f(self, u: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glEvalCoord1dv(self, u: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glEvalCoord1dv(self, u: Double1D, u_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glEvalCoord1fv(self, u: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glEvalCoord1fv(self, u: Float1D, u_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glEvalCoord2d(self, u: double, v: double) -> None:
        """
    
        """

    @staticmethod
    def glEvalCoord2f(self, u: float, v: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glEvalCoord2dv(self, u: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glEvalCoord2dv(self, u: Double1D, u_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glEvalCoord2fv(self, u: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glEvalCoord2fv(self, u: Float1D, u_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMapGrid1d(self, un: int, u1: double, u2: double) -> None:
        """
    
        """

    @staticmethod
    def glMapGrid1f(self, un: int, u1: float, u2: float) -> None:
        """
    
        """

    @staticmethod
    def glMapGrid2d(self, un: int, u1: double, u2: double, vn: int, v1: double,
                    v2: double) -> None:
        """
    
        """

    @staticmethod
    def glMapGrid2f(self, un: int, u1: float, u2: float, vn: int, v1: float,
                    v2: float) -> None:
        """
    
        """

    @staticmethod
    def glEvalPoint1(self, i: int) -> None:
        """
    
        """

    @staticmethod
    def glEvalPoint2(self, i: int, j: int) -> None:
        """
    
        """

    @staticmethod
    def glEvalMesh1(self, mode: int, i1: int, i2: int) -> None:
        """
    
        """

    @staticmethod
    def glEvalMesh2(self, mode: int, i1: int, i2: int, j1: int,
                    j2: int) -> None:
        """
    
        """

    @staticmethod
    def glFogi(self, pname: int, param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFogiv(self, pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFogiv(self, pname: int, params: Int1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glFeedbackBuffer(self, size: int, type: int,
                         buffer: FloatBuffer) -> None:
        """
    
        """

    @staticmethod
    def glPassThrough(self, token: float) -> None:
        """
    
        """

    @staticmethod
    def glSelectBuffer(self, size: int, buffer: IntBuffer) -> None:
        """
    
        """

    @staticmethod
    def glInitNames(self) -> None:
        """
    
        """

    @staticmethod
    def glLoadName(self, name: int) -> None:
        """
    
        """

    @staticmethod
    def glPushName(self, name: int) -> None:
        """
    
        """

    @staticmethod
    def glPopName(self) -> None:
        """
    
        """

    @staticmethod
    def glIndexub(self, c: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glIndexubv(self, c: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glIndexubv(self, c: Byte1D, c_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glPushClientAttrib(self, mask: int) -> None:
        """
    
        """

    @staticmethod
    def glPopClientAttrib(self) -> None:
        """
    
        """

    @staticmethod
    def glIndexPointer(self, type: int, stride: int, ptr: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glEdgeFlagPointer(self, stride: int, ptr: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glEdgeFlagPointer(self, stride: int, ptr_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glArrayElement(self, i: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glInterleavedArrays(self, format: int, stride: int,
                            pointer: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glInterleavedArrays(self, format: int, stride: int,
                            pointer_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPrioritizeTextures(self, n: int, textures: IntBuffer,
                             priorities: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPrioritizeTextures(self, n: int, textures: Int1D,
                             textures_offset: int, priorities: Float1D,
                             priorities_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glAreTexturesResident(self, n: int, textures: IntBuffer,
                              residences: ByteBuffer) -> bool:
        """
    
        """

    @overload
    @staticmethod
    def glAreTexturesResident(self, n: int, textures: Int1D,
                              textures_offset: int, residences: Byte1D,
                              residences_offset: int) -> bool:
        """
    
        """

    @staticmethod
    def glMultiTexCoord1d(self, target: int, s: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord1dv(self, target: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord1dv(self, target: int, v: Double1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord1f(self, target: int, s: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord1fv(self, target: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord1fv(self, target: int, v: Float1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord1i(self, target: int, s: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord1iv(self, target: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord1iv(self, target: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord1s(self, target: int, s: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord1sv(self, target: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord1sv(self, target: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord2d(self, target: int, s: double, t: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord2dv(self, target: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord2dv(self, target: int, v: Double1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord2f(self, target: int, s: float, t: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord2fv(self, target: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord2fv(self, target: int, v: Float1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord2i(self, target: int, s: int, t: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord2iv(self, target: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord2iv(self, target: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord2s(self, target: int, s: short, t: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord2sv(self, target: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord2sv(self, target: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord3d(self, target: int, s: double, t: double,
                          r: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord3dv(self, target: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord3dv(self, target: int, v: Double1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord3f(self, target: int, s: float, t: float,
                          r: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord3fv(self, target: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord3fv(self, target: int, v: Float1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord3i(self, target: int, s: int, t: int, r: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord3iv(self, target: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord3iv(self, target: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord3s(self, target: int, s: short, t: short,
                          r: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord3sv(self, target: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord3sv(self, target: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord4d(self, target: int, s: double, t: double, r: double,
                          q: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord4dv(self, target: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord4dv(self, target: int, v: Double1D,
                           v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord4fv(self, target: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord4fv(self, target: int, v: Float1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord4i(self, target: int, s: int, t: int, r: int,
                          q: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord4iv(self, target: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord4iv(self, target: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord4s(self, target: int, s: short, t: short, r: short,
                          q: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord4sv(self, target: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord4sv(self, target: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLoadTransposeMatrixf(self, m: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLoadTransposeMatrixf(self, m: Float1D, m_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLoadTransposeMatrixd(self, m: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLoadTransposeMatrixd(self, m: Double1D, m_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultTransposeMatrixf(self, m: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultTransposeMatrixf(self, m: Float1D, m_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultTransposeMatrixd(self, m: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultTransposeMatrixd(self, m: Double1D, m_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glFogCoordf(self, coord: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFogCoordfv(self, coord: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFogCoordfv(self, coord: Float1D, coord_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glFogCoordd(self, coord: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFogCoorddv(self, coord: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFogCoorddv(self, coord: Double1D, coord_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFogCoordPointer(self, type: int, stride: int,
                          pointer: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFogCoordPointer(self, type: int, stride: int,
                          pointer_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glSecondaryColor3b(self, red: byte, green: byte, blue: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3bv(self, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3bv(self, v: Byte1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glSecondaryColor3d(self, red: double, green: double,
                           blue: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glSecondaryColor3f(self, red: float, green: float,
                           blue: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glSecondaryColor3i(self, red: int, green: int, blue: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glSecondaryColor3s(self, red: short, green: short,
                           blue: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glSecondaryColor3ub(self, red: byte, green: byte, blue: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3ubv(self, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3ubv(self, v: Byte1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glSecondaryColor3ui(self, red: int, green: int, blue: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3uiv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3uiv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glSecondaryColor3us(self, red: short, green: short,
                            blue: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3usv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3usv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColorPointer(self, size: int, type: int, stride: int,
                                pointer: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColorPointer(self, size: int, type: int, stride: int,
                                pointer_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glWindowPos2d(self, x: double, y: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos2dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos2dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glWindowPos2f(self, x: float, y: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos2fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos2fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glWindowPos2i(self, x: int, y: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos2iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos2iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glWindowPos2s(self, x: short, y: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos2sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos2sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glWindowPos3d(self, x: double, y: double, z: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos3dv(self, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos3dv(self, v: Double1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glWindowPos3f(self, x: float, y: float, z: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos3fv(self, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos3fv(self, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glWindowPos3i(self, x: int, y: int, z: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos3iv(self, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos3iv(self, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glWindowPos3s(self, x: short, y: short, z: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos3sv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWindowPos3sv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glClearNamedBufferData(self, buffer: int, internalformat: int,
                               format: int, type: int, data: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glClearNamedBufferSubData(self, buffer: int, internalformat: int,
                                  offset: long, size: long, format: int,
                                  type: int, data: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glNamedFramebufferParameteri(self, framebuffer: int, pname: int,
                                     param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedFramebufferParameteriv(self, framebuffer: int, pname: int,
                                         param: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedFramebufferParameteriv(self, framebuffer: int, pname: int,
                                         param: Int1D,
                                         param_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnMapdv(self, target: int, query: int, bufSize: int,
                    v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnMapdv(self, target: int, query: int, bufSize: int, v: Double1D,
                    v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnMapfv(self, target: int, query: int, bufSize: int,
                    v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnMapfv(self, target: int, query: int, bufSize: int, v: Float1D,
                    v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnMapiv(self, target: int, query: int, bufSize: int,
                    v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnMapiv(self, target: int, query: int, bufSize: int, v: Int1D,
                    v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnPixelMapfv(self, map: int, bufSize: int,
                         values: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnPixelMapfv(self, map: int, bufSize: int, values: Float1D,
                         values_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnPixelMapuiv(self, map: int, bufSize: int,
                          values: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnPixelMapuiv(self, map: int, bufSize: int, values: Int1D,
                          values_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnPixelMapusv(self, map: int, bufSize: int,
                          values: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnPixelMapusv(self, map: int, bufSize: int, values: Short1D,
                          values_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnPolygonStipple(self, bufSize: int, pattern: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnPolygonStipple(self, bufSize: int, pattern: Byte1D,
                             pattern_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetnColorTable(self, target: int, format: int, type: int,
                         bufSize: int, table: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glGetnConvolutionFilter(self, target: int, format: int, type: int,
                                bufSize: int, image: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glGetnSeparableFilter(self, target: int, format: int, type: int,
                              rowBufSize: int, row: Buffer, columnBufSize: int,
                              column: Buffer, span: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glGetnHistogram(self, target: int, reset: bool, format: int, type: int,
                        bufSize: int, values: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glGetnMinmax(self, target: int, reset: bool, format: int, type: int,
                     bufSize: int, values: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glProgramStringARB(self, target: int, format: int, len: int,
                           string: String) -> None:
        """
    
        """

    @staticmethod
    def glBindProgramARB(self, target: int, program: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteProgramsARB(self, n: int, programs: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteProgramsARB(self, n: int, programs: Int1D,
                            programs_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenProgramsARB(self, n: int, programs: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenProgramsARB(self, n: int, programs: Int1D,
                         programs_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramEnvParameter4dARB(self, target: int, index: int, x: double,
                                   y: double, z: double, w: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParameter4dvARB(self, target: int, index: int,
                                    params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParameter4dvARB(self, target: int, index: int,
                                    params: Double1D,
                                    params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramEnvParameter4fARB(self, target: int, index: int, x: float,
                                   y: float, z: float, w: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParameter4fvARB(self, target: int, index: int,
                                    params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParameter4fvARB(self, target: int, index: int,
                                    params: Float1D,
                                    params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramLocalParameter4dARB(self, target: int, index: int, x: double,
                                     y: double, z: double, w: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParameter4dvARB(self, target: int, index: int,
                                      params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParameter4dvARB(self, target: int, index: int,
                                      params: Double1D,
                                      params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramLocalParameter4fARB(self, target: int, index: int, x: float,
                                     y: float, z: float, w: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParameter4fvARB(self, target: int, index: int,
                                      params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParameter4fvARB(self, target: int, index: int,
                                      params: Float1D,
                                      params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramEnvParameterdvARB(self, target: int, index: int,
                                      params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramEnvParameterdvARB(self, target: int, index: int,
                                      params: Double1D,
                                      params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramEnvParameterfvARB(self, target: int, index: int,
                                      params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramEnvParameterfvARB(self, target: int, index: int,
                                      params: Float1D,
                                      params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramLocalParameterdvARB(self, target: int, index: int,
                                        params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramLocalParameterdvARB(self, target: int, index: int,
                                        params: Double1D,
                                        params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramLocalParameterfvARB(self, target: int, index: int,
                                        params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramLocalParameterfvARB(self, target: int, index: int,
                                        params: Float1D,
                                        params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramivARB(self, target: int, pname: int,
                          params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramivARB(self, target: int, pname: int, params: Int1D,
                          params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetProgramStringARB(self, target: int, pname: int,
                              string: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glIsProgramARB(self, program: int) -> bool:
        """
    
        """

    @staticmethod
    def glUniform1i64ARB(self, location: int, x: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform2i64ARB(self, location: int, x: long, y: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform3i64ARB(self, location: int, x: long, y: long,
                         z: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform4i64ARB(self, location: int, x: long, y: long, z: long,
                         w: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1i64vARB(self, location: int, count: int,
                          value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1i64vARB(self, location: int, count: int, value: Long1D,
                          value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2i64vARB(self, location: int, count: int,
                          value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2i64vARB(self, location: int, count: int, value: Long1D,
                          value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3i64vARB(self, location: int, count: int,
                          value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3i64vARB(self, location: int, count: int, value: Long1D,
                          value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4i64vARB(self, location: int, count: int,
                          value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4i64vARB(self, location: int, count: int, value: Long1D,
                          value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform1ui64ARB(self, location: int, x: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform2ui64ARB(self, location: int, x: long, y: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform3ui64ARB(self, location: int, x: long, y: long,
                          z: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform4ui64ARB(self, location: int, x: long, y: long, z: long,
                          w: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1ui64vARB(self, location: int, count: int,
                           value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1ui64vARB(self, location: int, count: int, value: Long1D,
                           value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2ui64vARB(self, location: int, count: int,
                           value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2ui64vARB(self, location: int, count: int, value: Long1D,
                           value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3ui64vARB(self, location: int, count: int,
                           value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3ui64vARB(self, location: int, count: int, value: Long1D,
                           value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4ui64vARB(self, location: int, count: int,
                           value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4ui64vARB(self, location: int, count: int, value: Long1D,
                           value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformi64vARB(self, program: int, location: int,
                            params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformi64vARB(self, program: int, location: int, params: Long1D,
                            params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformui64vARB(self, program: int, location: int,
                             params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformui64vARB(self, program: int, location: int, params: Long1D,
                             params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnUniformi64vARB(self, program: int, location: int, bufSize: int,
                             params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnUniformi64vARB(self, program: int, location: int, bufSize: int,
                             params: Long1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnUniformui64vARB(self, program: int, location: int, bufSize: int,
                              params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnUniformui64vARB(self, program: int, location: int, bufSize: int,
                              params: Long1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform1i64ARB(self, program: int, location: int,
                                x: long) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform2i64ARB(self, program: int, location: int, x: long,
                                y: long) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform3i64ARB(self, program: int, location: int, x: long,
                                y: long, z: long) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform4i64ARB(self, program: int, location: int, x: long,
                                y: long, z: long, w: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1i64vARB(self, program: int, location: int, count: int,
                                 value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1i64vARB(self, program: int, location: int, count: int,
                                 value: Long1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2i64vARB(self, program: int, location: int, count: int,
                                 value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2i64vARB(self, program: int, location: int, count: int,
                                 value: Long1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3i64vARB(self, program: int, location: int, count: int,
                                 value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3i64vARB(self, program: int, location: int, count: int,
                                 value: Long1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4i64vARB(self, program: int, location: int, count: int,
                                 value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4i64vARB(self, program: int, location: int, count: int,
                                 value: Long1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform1ui64ARB(self, program: int, location: int,
                                 x: long) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform2ui64ARB(self, program: int, location: int, x: long,
                                 y: long) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform3ui64ARB(self, program: int, location: int, x: long,
                                 y: long, z: long) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform4ui64ARB(self, program: int, location: int, x: long,
                                 y: long, z: long, w: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1ui64vARB(self, program: int, location: int,
                                  count: int, value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1ui64vARB(self, program: int, location: int,
                                  count: int, value: Long1D,
                                  value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2ui64vARB(self, program: int, location: int,
                                  count: int, value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2ui64vARB(self, program: int, location: int,
                                  count: int, value: Long1D,
                                  value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3ui64vARB(self, program: int, location: int,
                                  count: int, value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3ui64vARB(self, program: int, location: int,
                                  count: int, value: Long1D,
                                  value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4ui64vARB(self, program: int, location: int,
                                  count: int, value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4ui64vARB(self, program: int, location: int,
                                  count: int, value: Long1D,
                                  value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColorTable(self, target: int, internalformat: int, width: int,
                     format: int, type: int, table: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColorTable(self, target: int, internalformat: int, width: int,
                     format: int, type: int,
                     table_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColorTableParameterfv(self, target: int, pname: int,
                                params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColorTableParameterfv(self, target: int, pname: int, params: Float1D,
                                params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColorTableParameteriv(self, target: int, pname: int,
                                params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColorTableParameteriv(self, target: int, pname: int, params: Int1D,
                                params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyColorTable(self, target: int, internalformat: int, x: int,
                         y: int, width: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetColorTable(self, target: int, format: int, type: int,
                        table: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetColorTable(self, target: int, format: int, type: int,
                        table_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetColorTableParameterfv(self, target: int, pname: int,
                                   params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetColorTableParameterfv(self, target: int, pname: int,
                                   params: Float1D,
                                   params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetColorTableParameteriv(self, target: int, pname: int,
                                   params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetColorTableParameteriv(self, target: int, pname: int,
                                   params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColorSubTable(self, target: int, start: int, count: int, format: int,
                        type: int, data: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColorSubTable(self, target: int, start: int, count: int, format: int,
                        type: int, data_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glCopyColorSubTable(self, target: int, start: int, x: int, y: int,
                            width: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glConvolutionFilter1D(self, target: int, internalformat: int,
                              width: int, format: int, type: int,
                              image: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glConvolutionFilter1D(self, target: int, internalformat: int,
                              width: int, format: int, type: int,
                              image_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glConvolutionFilter2D(self, target: int, internalformat: int,
                              width: int, height: int, format: int, type: int,
                              image: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glConvolutionFilter2D(self, target: int, internalformat: int,
                              width: int, height: int, format: int, type: int,
                              image_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glConvolutionParameterf(self, target: int, pname: int,
                                params: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glConvolutionParameterfv(self, target: int, pname: int,
                                 params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glConvolutionParameterfv(self, target: int, pname: int,
                                 params: Float1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glConvolutionParameteri(self, target: int, pname: int,
                                params: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glConvolutionParameteriv(self, target: int, pname: int,
                                 params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glConvolutionParameteriv(self, target: int, pname: int, params: Int1D,
                                 params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyConvolutionFilter1D(self, target: int, internalformat: int,
                                  x: int, y: int, width: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyConvolutionFilter2D(self, target: int, internalformat: int,
                                  x: int, y: int, width: int,
                                  height: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetConvolutionFilter(self, target: int, format: int, type: int,
                               image: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetConvolutionFilter(self, target: int, format: int, type: int,
                               image_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetConvolutionParameterfv(self, target: int, pname: int,
                                    params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetConvolutionParameterfv(self, target: int, pname: int,
                                    params: Float1D,
                                    params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetConvolutionParameteriv(self, target: int, pname: int,
                                    params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetConvolutionParameteriv(self, target: int, pname: int,
                                    params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetSeparableFilter(self, target: int, format: int, type: int,
                             row: Buffer, column: Buffer,
                             span: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetSeparableFilter(self, target: int, format: int, type: int,
                             row_buffer_offset: long,
                             column_buffer_offset: long,
                             span_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSeparableFilter2D(self, target: int, internalformat: int, width: int,
                            height: int, format: int, type: int, row: Buffer,
                            column: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSeparableFilter2D(self, target: int, internalformat: int, width: int,
                            height: int, format: int, type: int,
                            row_buffer_offset: long,
                            column_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetHistogram(self, target: int, reset: bool, format: int, type: int,
                       values: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetHistogram(self, target: int, reset: bool, format: int, type: int,
                       values_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetHistogramParameterfv(self, target: int, pname: int,
                                  params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetHistogramParameterfv(self, target: int, pname: int,
                                  params: Float1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetHistogramParameteriv(self, target: int, pname: int,
                                  params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetHistogramParameteriv(self, target: int, pname: int, params: Int1D,
                                  params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMinmax(self, target: int, reset: bool, format: int, type: int,
                    values: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMinmax(self, target: int, reset: bool, format: int, type: int,
                    values_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMinmaxParameterfv(self, target: int, pname: int,
                               params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMinmaxParameterfv(self, target: int, pname: int, params: Float1D,
                               params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMinmaxParameteriv(self, target: int, pname: int,
                               params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMinmaxParameteriv(self, target: int, pname: int, params: Int1D,
                               params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glHistogram(self, target: int, width: int, internalformat: int,
                    sink: bool) -> None:
        """
    
        """

    @staticmethod
    def glMinmax(self, target: int, internalformat: int, sink: bool) -> None:
        """
    
        """

    @staticmethod
    def glResetHistogram(self, target: int) -> None:
        """
    
        """

    @staticmethod
    def glResetMinmax(self, target: int) -> None:
        """
    
        """

    @staticmethod
    def glCurrentPaletteMatrixARB(self, index: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixIndexubvARB(self, size: int, indices: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixIndexubvARB(self, size: int, indices: Byte1D,
                            indices_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixIndexusvARB(self, size: int, indices: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixIndexusvARB(self, size: int, indices: Short1D,
                            indices_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixIndexuivARB(self, size: int, indices: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixIndexuivARB(self, size: int, indices: Int1D,
                            indices_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixIndexPointerARB(self, size: int, type: int, stride: int,
                                pointer: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixIndexPointerARB(self, size: int, type: int, stride: int,
                                pointer_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glMaxShaderCompilerThreadsARB(self, count: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFramebufferSampleLocationsfvARB(self, target: int, start: int,
                                          count: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFramebufferSampleLocationsfvARB(self, target: int, start: int,
                                          count: int, v: Float1D,
                                          v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedFramebufferSampleLocationsfvARB(self, framebuffer: int,
                                               start: int, count: int,
                                               v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedFramebufferSampleLocationsfvARB(self, framebuffer: int,
                                               start: int, count: int,
                                               v: Float1D,
                                               v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glEvaluateDepthValuesARB(self) -> None:
        """
    
        """

    @staticmethod
    def glDeleteObjectARB(self, obj: long) -> None:
        """
    
        """

    @staticmethod
    def glGetHandleARB(self, pname: int) -> long:
        """
    
        """

    @staticmethod
    def glDetachObjectARB(self, containerObj: long, attachedObj: long) -> None:
        """
    
        """

    @staticmethod
    def glCreateShaderObjectARB(self, shaderType: int) -> long:
        """
    
        """

    @overload
    @staticmethod
    def glShaderSourceARB(self, shaderObj: long, count: int, string: String1D,
                          length: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glShaderSourceARB(self, shaderObj: long, count: int, string: String1D,
                          length: Int1D, length_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glCompileShaderARB(self, shaderObj: long) -> None:
        """
    
        """

    @staticmethod
    def glCreateProgramObjectARB(self) -> long:
        """
    
        """

    @staticmethod
    def glAttachObjectARB(self, containerObj: long, obj: long) -> None:
        """
    
        """

    @staticmethod
    def glLinkProgramARB(self, programObj: long) -> None:
        """
    
        """

    @staticmethod
    def glUseProgramObjectARB(self, programObj: long) -> None:
        """
    
        """

    @staticmethod
    def glValidateProgramARB(self, programObj: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform1fARB(self, location: int, v0: float) -> None:
        """
    
        """

    @staticmethod
    def glUniform2fARB(self, location: int, v0: float, v1: float) -> None:
        """
    
        """

    @staticmethod
    def glUniform3fARB(self, location: int, v0: float, v1: float,
                       v2: float) -> None:
        """
    
        """

    @staticmethod
    def glUniform4fARB(self, location: int, v0: float, v1: float, v2: float,
                       v3: float) -> None:
        """
    
        """

    @staticmethod
    def glUniform1iARB(self, location: int, v0: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform2iARB(self, location: int, v0: int, v1: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform3iARB(self, location: int, v0: int, v1: int, v2: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform4iARB(self, location: int, v0: int, v1: int, v2: int,
                       v3: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1fvARB(self, location: int, count: int,
                        value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1fvARB(self, location: int, count: int, value: Float1D,
                        value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2fvARB(self, location: int, count: int,
                        value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2fvARB(self, location: int, count: int, value: Float1D,
                        value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3fvARB(self, location: int, count: int,
                        value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3fvARB(self, location: int, count: int, value: Float1D,
                        value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4fvARB(self, location: int, count: int,
                        value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4fvARB(self, location: int, count: int, value: Float1D,
                        value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1ivARB(self, location: int, count: int,
                        value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1ivARB(self, location: int, count: int, value: Int1D,
                        value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2ivARB(self, location: int, count: int,
                        value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2ivARB(self, location: int, count: int, value: Int1D,
                        value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3ivARB(self, location: int, count: int,
                        value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3ivARB(self, location: int, count: int, value: Int1D,
                        value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4ivARB(self, location: int, count: int,
                        value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4ivARB(self, location: int, count: int, value: Int1D,
                        value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix2fvARB(self, location: int, count: int, transpose: bool,
                              value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix2fvARB(self, location: int, count: int, transpose: bool,
                              value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix3fvARB(self, location: int, count: int, transpose: bool,
                              value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix3fvARB(self, location: int, count: int, transpose: bool,
                              value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix4fvARB(self, location: int, count: int, transpose: bool,
                              value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix4fvARB(self, location: int, count: int, transpose: bool,
                              value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetObjectParameterfvARB(self, obj: long, pname: int,
                                  params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetObjectParameterfvARB(self, obj: long, pname: int, params: Float1D,
                                  params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetObjectParameterivARB(self, obj: long, pname: int,
                                  params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetObjectParameterivARB(self, obj: long, pname: int, params: Int1D,
                                  params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetInfoLogARB(self, obj: long, maxLength: int, length: IntBuffer,
                        infoLog: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetInfoLogARB(self, obj: long, maxLength: int, length: Int1D,
                        length_offset: int, infoLog: Byte1D,
                        infoLog_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetAttachedObjectsARB(self, containerObj: long, maxCount: int,
                                count: IntBuffer, obj: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetAttachedObjectsARB(self, containerObj: long, maxCount: int,
                                count: Int1D, count_offset: int, obj: Long1D,
                                obj_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetUniformLocationARB(self, programObj: long, name: String) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveUniformARB(self, programObj: long, index: int,
                              maxLength: int, length: IntBuffer,
                              size: IntBuffer, type: IntBuffer,
                              name: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveUniformARB(self, programObj: long, index: int,
                              maxLength: int, length: Int1D,
                              length_offset: int, size: Int1D,
                              size_offset: int, type: Int1D, type_offset: int,
                              name: Byte1D, name_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformfvARB(self, programObj: long, location: int,
                          params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformfvARB(self, programObj: long, location: int,
                          params: Float1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformivARB(self, programObj: long, location: int,
                          params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformivARB(self, programObj: long, location: int, params: Int1D,
                          params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetShaderSourceARB(self, obj: long, maxLength: int,
                             length: IntBuffer, source: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetShaderSourceARB(self, obj: long, maxLength: int, length: Int1D,
                             length_offset: int, source: Byte1D,
                             source_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightbvARB(self, size: int, weights: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightbvARB(self, size: int, weights: Byte1D,
                      weights_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightsvARB(self, size: int, weights: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightsvARB(self, size: int, weights: Short1D,
                      weights_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightivARB(self, size: int, weights: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightivARB(self, size: int, weights: Int1D,
                      weights_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightfvARB(self, size: int, weights: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightfvARB(self, size: int, weights: Float1D,
                      weights_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightdvARB(self, size: int, weights: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightdvARB(self, size: int, weights: Double1D,
                      weights_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightubvARB(self, size: int, weights: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightubvARB(self, size: int, weights: Byte1D,
                       weights_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightusvARB(self, size: int, weights: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightusvARB(self, size: int, weights: Short1D,
                       weights_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightuivARB(self, size: int, weights: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightuivARB(self, size: int, weights: Int1D,
                       weights_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightPointerARB(self, size: int, type: int, stride: int,
                           pointer: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glWeightPointerARB(self, size: int, type: int, stride: int,
                           pointer_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexBlendARB(self, count: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib1dARB(self, index: int, x: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1dvARB(self, index: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1dvARB(self, index: int, v: Double1D,
                             v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib1fARB(self, index: int, x: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1fvARB(self, index: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1fvARB(self, index: int, v: Float1D,
                             v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib1sARB(self, index: int, x: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1svARB(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1svARB(self, index: int, v: Short1D,
                             v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib2dARB(self, index: int, x: double, y: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2dvARB(self, index: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2dvARB(self, index: int, v: Double1D,
                             v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib2fARB(self, index: int, x: float, y: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2fvARB(self, index: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2fvARB(self, index: int, v: Float1D,
                             v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib2sARB(self, index: int, x: short, y: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2svARB(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2svARB(self, index: int, v: Short1D,
                             v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib3dARB(self, index: int, x: double, y: double,
                            z: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3dvARB(self, index: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3dvARB(self, index: int, v: Double1D,
                             v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib3fARB(self, index: int, x: float, y: float,
                            z: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3fvARB(self, index: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3fvARB(self, index: int, v: Float1D,
                             v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib3sARB(self, index: int, x: short, y: short,
                            z: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3svARB(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3svARB(self, index: int, v: Short1D,
                             v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4NbvARB(self, index: int, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4NbvARB(self, index: int, v: Byte1D,
                              v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4NivARB(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4NivARB(self, index: int, v: Int1D,
                              v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4NsvARB(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4NsvARB(self, index: int, v: Short1D,
                              v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib4NubARB(self, index: int, x: byte, y: byte, z: byte,
                              w: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4NubvARB(self, index: int, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4NubvARB(self, index: int, v: Byte1D,
                               v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4NuivARB(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4NuivARB(self, index: int, v: Int1D,
                               v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4NusvARB(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4NusvARB(self, index: int, v: Short1D,
                               v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4bvARB(self, index: int, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4bvARB(self, index: int, v: Byte1D,
                             v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib4dARB(self, index: int, x: double, y: double, z: double,
                            w: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4dvARB(self, index: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4dvARB(self, index: int, v: Double1D,
                             v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib4fARB(self, index: int, x: float, y: float, z: float,
                            w: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4fvARB(self, index: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4fvARB(self, index: int, v: Float1D,
                             v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4ivARB(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4ivARB(self, index: int, v: Int1D,
                             v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib4sARB(self, index: int, x: short, y: short, z: short,
                            w: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4svARB(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4svARB(self, index: int, v: Short1D,
                             v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4ubvARB(self, index: int, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4ubvARB(self, index: int, v: Byte1D,
                              v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4uivARB(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4uivARB(self, index: int, v: Int1D,
                              v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4usvARB(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4usvARB(self, index: int, v: Short1D,
                              v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribPointerARB(self, index: int, size: int, type: int,
                                 normalized: bool, stride: int,
                                 pointer: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribPointerARB(self, index: int, size: int, type: int,
                                 normalized: bool, stride: int,
                                 pointer_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glEnableVertexAttribArrayARB(self, index: int) -> None:
        """
    
        """

    @staticmethod
    def glDisableVertexAttribArrayARB(self, index: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribdvARB(self, index: int, pname: int,
                               params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribdvARB(self, index: int, pname: int, params: Double1D,
                               params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribfvARB(self, index: int, pname: int,
                               params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribfvARB(self, index: int, pname: int, params: Float1D,
                               params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribivARB(self, index: int, pname: int,
                               params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribivARB(self, index: int, pname: int, params: Int1D,
                               params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glBlendBarrier(self) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord1bOES(self, texture: int, s: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord1bvOES(self, texture: int, coords: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord1bvOES(self, texture: int, coords: Byte1D,
                              coords_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord2bOES(self, texture: int, s: byte, t: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord2bvOES(self, texture: int, coords: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord2bvOES(self, texture: int, coords: Byte1D,
                              coords_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord3bOES(self, texture: int, s: byte, t: byte,
                             r: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord3bvOES(self, texture: int, coords: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord3bvOES(self, texture: int, coords: Byte1D,
                              coords_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord4bOES(self, texture: int, s: byte, t: byte, r: byte,
                             q: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord4bvOES(self, texture: int, coords: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord4bvOES(self, texture: int, coords: Byte1D,
                              coords_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord1bOES(self, s: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord1bvOES(self, coords: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord1bvOES(self, coords: Byte1D, coords_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord2bOES(self, s: byte, t: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord2bvOES(self, coords: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord2bvOES(self, coords: Byte1D, coords_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord3bOES(self, s: byte, t: byte, r: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord3bvOES(self, coords: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord3bvOES(self, coords: Byte1D, coords_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord4bOES(self, s: byte, t: byte, r: byte, q: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord4bvOES(self, coords: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord4bvOES(self, coords: Byte1D, coords_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertex2bOES(self, x: byte, y: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex2bvOES(self, coords: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex2bvOES(self, coords: Byte1D, coords_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertex3bOES(self, x: byte, y: byte, z: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex3bvOES(self, coords: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex3bvOES(self, coords: Byte1D, coords_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertex4bOES(self, x: byte, y: byte, z: byte, w: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex4bvOES(self, coords: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex4bvOES(self, coords: Byte1D, coords_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glQueryMatrixxOES(self, mantissa: IntBuffer,
                          exponent: IntBuffer) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glQueryMatrixxOES(self, mantissa: Int1D, mantissa_offset: int,
                          exponent: Int1D, exponent_offset: int) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glClipPlanef(self, plane: int, equation: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glClipPlanef(self, plane: int, equation: Float1D,
                     equation_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetClipPlanef(self, plane: int, equation: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetClipPlanef(self, plane: int, equation: Float1D,
                        equation_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glBlendFuncIndexedAMD(self, buf: int, src: int, dst: int) -> None:
        """
    
        """

    @staticmethod
    def glBlendFuncSeparateIndexedAMD(self, buf: int, srcRGB: int, dstRGB: int,
                                      srcAlpha: int, dstAlpha: int) -> None:
        """
    
        """

    @staticmethod
    def glBlendEquationIndexedAMD(self, buf: int, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glBlendEquationSeparateIndexedAMD(self, buf: int, modeRGB: int,
                                          modeAlpha: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform1i64NV(self, location: int, x: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform2i64NV(self, location: int, x: long, y: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform3i64NV(self, location: int, x: long, y: long,
                        z: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform4i64NV(self, location: int, x: long, y: long, z: long,
                        w: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1i64vNV(self, location: int, count: int,
                         value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1i64vNV(self, location: int, count: int, value: Long1D,
                         value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2i64vNV(self, location: int, count: int,
                         value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2i64vNV(self, location: int, count: int, value: Long1D,
                         value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3i64vNV(self, location: int, count: int,
                         value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3i64vNV(self, location: int, count: int, value: Long1D,
                         value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4i64vNV(self, location: int, count: int,
                         value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4i64vNV(self, location: int, count: int, value: Long1D,
                         value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform1ui64NV(self, location: int, x: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform2ui64NV(self, location: int, x: long, y: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform3ui64NV(self, location: int, x: long, y: long,
                         z: long) -> None:
        """
    
        """

    @staticmethod
    def glUniform4ui64NV(self, location: int, x: long, y: long, z: long,
                         w: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1ui64vNV(self, location: int, count: int,
                          value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1ui64vNV(self, location: int, count: int, value: Long1D,
                          value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2ui64vNV(self, location: int, count: int,
                          value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2ui64vNV(self, location: int, count: int, value: Long1D,
                          value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3ui64vNV(self, location: int, count: int,
                          value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3ui64vNV(self, location: int, count: int, value: Long1D,
                          value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4ui64vNV(self, location: int, count: int,
                          value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4ui64vNV(self, location: int, count: int, value: Long1D,
                          value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformi64vNV(self, program: int, location: int,
                           params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformi64vNV(self, program: int, location: int, params: Long1D,
                           params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform1i64NV(self, program: int, location: int,
                               x: long) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform2i64NV(self, program: int, location: int, x: long,
                               y: long) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform3i64NV(self, program: int, location: int, x: long,
                               y: long, z: long) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform4i64NV(self, program: int, location: int, x: long,
                               y: long, z: long, w: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1i64vNV(self, program: int, location: int, count: int,
                                value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1i64vNV(self, program: int, location: int, count: int,
                                value: Long1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2i64vNV(self, program: int, location: int, count: int,
                                value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2i64vNV(self, program: int, location: int, count: int,
                                value: Long1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3i64vNV(self, program: int, location: int, count: int,
                                value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3i64vNV(self, program: int, location: int, count: int,
                                value: Long1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4i64vNV(self, program: int, location: int, count: int,
                                value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4i64vNV(self, program: int, location: int, count: int,
                                value: Long1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform1ui64NV(self, program: int, location: int,
                                x: long) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform2ui64NV(self, program: int, location: int, x: long,
                                y: long) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform3ui64NV(self, program: int, location: int, x: long,
                                y: long, z: long) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform4ui64NV(self, program: int, location: int, x: long,
                                y: long, z: long, w: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1ui64vNV(self, program: int, location: int, count: int,
                                 value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1ui64vNV(self, program: int, location: int, count: int,
                                 value: Long1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2ui64vNV(self, program: int, location: int, count: int,
                                 value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2ui64vNV(self, program: int, location: int, count: int,
                                 value: Long1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3ui64vNV(self, program: int, location: int, count: int,
                                 value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3ui64vNV(self, program: int, location: int, count: int,
                                 value: Long1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4ui64vNV(self, program: int, location: int, count: int,
                                 value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4ui64vNV(self, program: int, location: int, count: int,
                                 value: Long1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribParameteriAMD(self, index: int, pname: int,
                                    param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenNamesAMD(self, identifier: int, num: int,
                      names: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenNamesAMD(self, identifier: int, num: int, names: Int1D,
                      names_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteNamesAMD(self, identifier: int, num: int,
                         names: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteNamesAMD(self, identifier: int, num: int, names: Int1D,
                         names_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glIsNameAMD(self, identifier: int, name: int) -> bool:
        """
    
        """

    @staticmethod
    def glQueryObjectParameteruiAMD(self, target: int, id: int, pname: int,
                                    param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfMonitorGroupsAMD(self, numGroups: IntBuffer, groupsSize: int,
                                  groups: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfMonitorGroupsAMD(self, numGroups: Int1D,
                                  numGroups_offset: int, groupsSize: int,
                                  groups: Int1D, groups_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfMonitorCountersAMD(self, group: int, numCounters: IntBuffer,
                                    maxActiveCounters: IntBuffer,
                                    counterSize: int,
                                    counters: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfMonitorCountersAMD(self, group: int, numCounters: Int1D,
                                    numCounters_offset: int,
                                    maxActiveCounters: Int1D,
                                    maxActiveCounters_offset: int,
                                    counterSize: int, counters: Int1D,
                                    counters_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfMonitorGroupStringAMD(self, group: int, bufSize: int,
                                       length: IntBuffer,
                                       groupString: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfMonitorGroupStringAMD(self, group: int, bufSize: int,
                                       length: Int1D, length_offset: int,
                                       groupString: Byte1D,
                                       groupString_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfMonitorCounterStringAMD(self, group: int, counter: int,
                                         bufSize: int, length: IntBuffer,
                                         counterString: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfMonitorCounterStringAMD(self, group: int, counter: int,
                                         bufSize: int, length: Int1D,
                                         length_offset: int,
                                         counterString: Byte1D,
                                         counterString_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetPerfMonitorCounterInfoAMD(self, group: int, counter: int,
                                       pname: int, data: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenPerfMonitorsAMD(self, n: int, monitors: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenPerfMonitorsAMD(self, n: int, monitors: Int1D,
                             monitors_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeletePerfMonitorsAMD(self, n: int, monitors: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeletePerfMonitorsAMD(self, n: int, monitors: Int1D,
                                monitors_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSelectPerfMonitorCountersAMD(self, monitor: int, enable: bool,
                                       group: int, numCounters: int,
                                       counterList: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSelectPerfMonitorCountersAMD(self, monitor: int, enable: bool,
                                       group: int, numCounters: int,
                                       counterList: Int1D,
                                       counterList_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glBeginPerfMonitorAMD(self, monitor: int) -> None:
        """
    
        """

    @staticmethod
    def glEndPerfMonitorAMD(self, monitor: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfMonitorCounterDataAMD(self, monitor: int, pname: int,
                                       dataSize: int, data: IntBuffer,
                                       bytesWritten: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfMonitorCounterDataAMD(self, monitor: int, pname: int,
                                       dataSize: int, data: Int1D,
                                       data_offset: int, bytesWritten: Int1D,
                                       bytesWritten_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTexStorageSparseAMD(self, target: int, internalFormat: int,
                              width: int, height: int, depth: int, layers: int,
                              flags: int) -> None:
        """
    
        """

    @staticmethod
    def glTextureStorageSparseAMD(self, texture: int, target: int,
                                  internalFormat: int, width: int, height: int,
                                  depth: int, layers: int, flags: int) -> None:
        """
    
        """

    @staticmethod
    def glBufferParameteri(self, target: int, pname: int, param: int) -> None:
        """
    
        """

    @staticmethod
    def glObjectPurgeableAPPLE(self, objectType: int, name: int,
                               option: int) -> int:
        """
    
        """

    @staticmethod
    def glObjectUnpurgeableAPPLE(self, objectType: int, name: int,
                                 option: int) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glGetObjectParameterivAPPLE(self, objectType: int, name: int,
                                    pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetObjectParameterivAPPLE(self, objectType: int, name: int,
                                    pname: int, params: Int1D,
                                    params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTextureRangeAPPLE(self, target: int, length: int,
                            pointer: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayRangeAPPLE(self, length: int, pointer: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glFlushVertexArrayRangeAPPLE(self, length: int,
                                     pointer: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayParameteriAPPLE(self, pname: int, param: int) -> None:
        """
    
        """

    @staticmethod
    def glEnableVertexAttribAPPLE(self, index: int, pname: int) -> None:
        """
    
        """

    @staticmethod
    def glDisableVertexAttribAPPLE(self, index: int, pname: int) -> None:
        """
    
        """

    @staticmethod
    def glIsVertexAttribEnabledAPPLE(self, index: int, pname: int) -> bool:
        """
    
        """

    @overload
    @staticmethod
    def glMapVertexAttrib1dAPPLE(self, index: int, size: int, u1: double,
                                 u2: double, stride: int, order: int,
                                 points: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMapVertexAttrib1dAPPLE(self, index: int, size: int, u1: double,
                                 u2: double, stride: int, order: int,
                                 points: Double1D, points_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMapVertexAttrib1fAPPLE(self, index: int, size: int, u1: float,
                                 u2: float, stride: int, order: int,
                                 points: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMapVertexAttrib1fAPPLE(self, index: int, size: int, u1: float,
                                 u2: float, stride: int, order: int,
                                 points: Float1D, points_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMapVertexAttrib2dAPPLE(self, index: int, size: int, u1: double,
                                 u2: double, ustride: int, uorder: int,
                                 v1: double, v2: double, vstride: int,
                                 vorder: int, points: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMapVertexAttrib2dAPPLE(self, index: int, size: int, u1: double,
                                 u2: double, ustride: int, uorder: int,
                                 v1: double, v2: double, vstride: int,
                                 vorder: int, points: Double1D,
                                 points_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMapVertexAttrib2fAPPLE(self, index: int, size: int, u1: float,
                                 u2: float, ustride: int, uorder: int,
                                 v1: float, v2: float, vstride: int,
                                 vorder: int, points: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMapVertexAttrib2fAPPLE(self, index: int, size: int, u1: float,
                                 u2: float, ustride: int, uorder: int,
                                 v1: float, v2: float, vstride: int,
                                 vorder: int, points: Float1D,
                                 points_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawBuffersATI(self, n: int, bufs: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawBuffersATI(self, n: int, bufs: Int1D, bufs_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glPNTrianglesiATI(self, pname: int, param: int) -> None:
        """
    
        """

    @staticmethod
    def glPNTrianglesfATI(self, pname: int, param: float) -> None:
        """
    
        """

    @staticmethod
    def glUniformBufferEXT(self, program: int, location: int,
                           buffer: int) -> None:
        """
    
        """

    @staticmethod
    def glGetUniformBufferSizeEXT(self, program: int, location: int) -> int:
        """
    
        """

    @staticmethod
    def glGetUniformOffsetEXT(self, program: int, location: int) -> long:
        """
    
        """

    @staticmethod
    def glLockArraysEXT(self, first: int, count: int) -> None:
        """
    
        """

    @staticmethod
    def glUnlockArraysEXT(self) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCullParameterdvEXT(self, pname: int, params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCullParameterdvEXT(self, pname: int, params: Double1D,
                             params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCullParameterfvEXT(self, pname: int, params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCullParameterfvEXT(self, pname: int, params: Float1D,
                             params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glDepthBoundsEXT(self, zmin: double, zmax: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixLoadfEXT(self, mode: int, m: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixLoadfEXT(self, mode: int, m: Float1D, m_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixLoaddEXT(self, mode: int, m: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixLoaddEXT(self, mode: int, m: Double1D, m_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixMultfEXT(self, mode: int, m: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixMultfEXT(self, mode: int, m: Float1D, m_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixMultdEXT(self, mode: int, m: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixMultdEXT(self, mode: int, m: Double1D, m_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMatrixLoadIdentityEXT(self, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glMatrixRotatefEXT(self, mode: int, angle: float, x: float, y: float,
                           z: float) -> None:
        """
    
        """

    @staticmethod
    def glMatrixRotatedEXT(self, mode: int, angle: double, x: double,
                           y: double, z: double) -> None:
        """
    
        """

    @staticmethod
    def glMatrixScalefEXT(self, mode: int, x: float, y: float,
                          z: float) -> None:
        """
    
        """

    @staticmethod
    def glMatrixScaledEXT(self, mode: int, x: double, y: double,
                          z: double) -> None:
        """
    
        """

    @staticmethod
    def glMatrixTranslatefEXT(self, mode: int, x: float, y: float,
                              z: float) -> None:
        """
    
        """

    @staticmethod
    def glMatrixTranslatedEXT(self, mode: int, x: double, y: double,
                              z: double) -> None:
        """
    
        """

    @staticmethod
    def glMatrixFrustumEXT(self, mode: int, left: double, right: double,
                           bottom: double, top: double, zNear: double,
                           zFar: double) -> None:
        """
    
        """

    @staticmethod
    def glMatrixOrthoEXT(self, mode: int, left: double, right: double,
                         bottom: double, top: double, zNear: double,
                         zFar: double) -> None:
        """
    
        """

    @staticmethod
    def glMatrixPopEXT(self, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glMatrixPushEXT(self, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glClientAttribDefaultEXT(self, mask: int) -> None:
        """
    
        """

    @staticmethod
    def glPushClientAttribDefaultEXT(self, mask: int) -> None:
        """
    
        """

    @staticmethod
    def glTextureParameterfEXT(self, texture: int, target: int, pname: int,
                               param: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureParameterfvEXT(self, texture: int, target: int, pname: int,
                                params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureParameterfvEXT(self, texture: int, target: int, pname: int,
                                params: Float1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTextureParameteriEXT(self, texture: int, target: int, pname: int,
                               param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureParameterivEXT(self, texture: int, target: int, pname: int,
                                params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureParameterivEXT(self, texture: int, target: int, pname: int,
                                params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureImage1DEXT(self, texture: int, target: int, level: int,
                            internalformat: int, width: int, border: int,
                            format: int, type: int, pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureImage1DEXT(self, texture: int, target: int, level: int,
                            internalformat: int, width: int, border: int,
                            format: int, type: int,
                            pixels_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureImage2DEXT(self, texture: int, target: int, level: int,
                            internalformat: int, width: int, height: int,
                            border: int, format: int, type: int,
                            pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureImage2DEXT(self, texture: int, target: int, level: int,
                            internalformat: int, width: int, height: int,
                            border: int, format: int, type: int,
                            pixels_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureSubImage1DEXT(self, texture: int, target: int, level: int,
                               xoffset: int, width: int, format: int,
                               type: int, pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureSubImage1DEXT(self, texture: int, target: int, level: int,
                               xoffset: int, width: int, format: int,
                               type: int, pixels_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureSubImage2DEXT(self, texture: int, target: int, level: int,
                               xoffset: int, yoffset: int, width: int,
                               height: int, format: int, type: int,
                               pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureSubImage2DEXT(self, texture: int, target: int, level: int,
                               xoffset: int, yoffset: int, width: int,
                               height: int, format: int, type: int,
                               pixels_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glCopyTextureImage1DEXT(self, texture: int, target: int, level: int,
                                internalformat: int, x: int, y: int,
                                width: int, border: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyTextureImage2DEXT(self, texture: int, target: int, level: int,
                                internalformat: int, x: int, y: int,
                                width: int, height: int, border: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyTextureSubImage1DEXT(self, texture: int, target: int, level: int,
                                   xoffset: int, x: int, y: int,
                                   width: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyTextureSubImage2DEXT(self, texture: int, target: int, level: int,
                                   xoffset: int, yoffset: int, x: int, y: int,
                                   width: int, height: int) -> None:
        """
    
        """

    @staticmethod
    def glGetTextureImageEXT(self, texture: int, target: int, level: int,
                             format: int, type: int, pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTextureParameterfvEXT(self, texture: int, target: int, pname: int,
                                   params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTextureParameterfvEXT(self, texture: int, target: int, pname: int,
                                   params: Float1D,
                                   params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTextureParameterivEXT(self, texture: int, target: int, pname: int,
                                   params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTextureParameterivEXT(self, texture: int, target: int, pname: int,
                                   params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTextureLevelParameterfvEXT(self, texture: int, target: int,
                                        level: int, pname: int,
                                        params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTextureLevelParameterfvEXT(self, texture: int, target: int,
                                        level: int, pname: int,
                                        params: Float1D,
                                        params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTextureLevelParameterivEXT(self, texture: int, target: int,
                                        level: int, pname: int,
                                        params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTextureLevelParameterivEXT(self, texture: int, target: int,
                                        level: int, pname: int, params: Int1D,
                                        params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureImage3DEXT(self, texture: int, target: int, level: int,
                            internalformat: int, width: int, height: int,
                            depth: int, border: int, format: int, type: int,
                            pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureImage3DEXT(self, texture: int, target: int, level: int,
                            internalformat: int, width: int, height: int,
                            depth: int, border: int, format: int, type: int,
                            pixels_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureSubImage3DEXT(self, texture: int, target: int, level: int,
                               xoffset: int, yoffset: int, zoffset: int,
                               width: int, height: int, depth: int,
                               format: int, type: int, pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureSubImage3DEXT(self, texture: int, target: int, level: int,
                               xoffset: int, yoffset: int, zoffset: int,
                               width: int, height: int, depth: int,
                               format: int, type: int,
                               pixels_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glCopyTextureSubImage3DEXT(self, texture: int, target: int, level: int,
                                   xoffset: int, yoffset: int, zoffset: int,
                                   x: int, y: int, width: int,
                                   height: int) -> None:
        """
    
        """

    @staticmethod
    def glBindMultiTextureEXT(self, texunit: int, target: int,
                              texture: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoordPointerEXT(self, texunit: int, size: int, type: int,
                                  stride: int, pointer: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexEnvfEXT(self, texunit: int, target: int, pname: int,
                          param: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexEnvfvEXT(self, texunit: int, target: int, pname: int,
                           params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexEnvfvEXT(self, texunit: int, target: int, pname: int,
                           params: Float1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexEnviEXT(self, texunit: int, target: int, pname: int,
                          param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexEnvivEXT(self, texunit: int, target: int, pname: int,
                           params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexEnvivEXT(self, texunit: int, target: int, pname: int,
                           params: Int1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexGendEXT(self, texunit: int, coord: int, pname: int,
                          param: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexGendvEXT(self, texunit: int, coord: int, pname: int,
                           params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexGendvEXT(self, texunit: int, coord: int, pname: int,
                           params: Double1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexGenfEXT(self, texunit: int, coord: int, pname: int,
                          param: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexGenfvEXT(self, texunit: int, coord: int, pname: int,
                           params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexGenfvEXT(self, texunit: int, coord: int, pname: int,
                           params: Float1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexGeniEXT(self, texunit: int, coord: int, pname: int,
                          param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexGenivEXT(self, texunit: int, coord: int, pname: int,
                           params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexGenivEXT(self, texunit: int, coord: int, pname: int,
                           params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexEnvfvEXT(self, texunit: int, target: int, pname: int,
                              params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexEnvfvEXT(self, texunit: int, target: int, pname: int,
                              params: Float1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexEnvivEXT(self, texunit: int, target: int, pname: int,
                              params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexEnvivEXT(self, texunit: int, target: int, pname: int,
                              params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexGendvEXT(self, texunit: int, coord: int, pname: int,
                              params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexGendvEXT(self, texunit: int, coord: int, pname: int,
                              params: Double1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexGenfvEXT(self, texunit: int, coord: int, pname: int,
                              params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexGenfvEXT(self, texunit: int, coord: int, pname: int,
                              params: Float1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexGenivEXT(self, texunit: int, coord: int, pname: int,
                              params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexGenivEXT(self, texunit: int, coord: int, pname: int,
                              params: Int1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexParameteriEXT(self, texunit: int, target: int, pname: int,
                                param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexParameterivEXT(self, texunit: int, target: int, pname: int,
                                 params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexParameterivEXT(self, texunit: int, target: int, pname: int,
                                 params: Int1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexParameterfEXT(self, texunit: int, target: int, pname: int,
                                param: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexParameterfvEXT(self, texunit: int, target: int, pname: int,
                                 params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexParameterfvEXT(self, texunit: int, target: int, pname: int,
                                 params: Float1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexImage1DEXT(self, texunit: int, target: int, level: int,
                             internalformat: int, width: int, border: int,
                             format: int, type: int, pixels: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexImage2DEXT(self, texunit: int, target: int, level: int,
                             internalformat: int, width: int, height: int,
                             border: int, format: int, type: int,
                             pixels: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexSubImage1DEXT(self, texunit: int, target: int, level: int,
                                xoffset: int, width: int, format: int,
                                type: int, pixels: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexSubImage2DEXT(self, texunit: int, target: int, level: int,
                                xoffset: int, yoffset: int, width: int,
                                height: int, format: int, type: int,
                                pixels: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCopyMultiTexImage1DEXT(self, texunit: int, target: int, level: int,
                                 internalformat: int, x: int, y: int,
                                 width: int, border: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyMultiTexImage2DEXT(self, texunit: int, target: int, level: int,
                                 internalformat: int, x: int, y: int,
                                 width: int, height: int, border: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyMultiTexSubImage1DEXT(self, texunit: int, target: int,
                                    level: int, xoffset: int, x: int, y: int,
                                    width: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyMultiTexSubImage2DEXT(self, texunit: int, target: int,
                                    level: int, xoffset: int, yoffset: int,
                                    x: int, y: int, width: int,
                                    height: int) -> None:
        """
    
        """

    @staticmethod
    def glGetMultiTexImageEXT(self, texunit: int, target: int, level: int,
                              format: int, type: int, pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexParameterfvEXT(self, texunit: int, target: int,
                                    pname: int, params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexParameterfvEXT(self, texunit: int, target: int,
                                    pname: int, params: Float1D,
                                    params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexParameterivEXT(self, texunit: int, target: int,
                                    pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexParameterivEXT(self, texunit: int, target: int,
                                    pname: int, params: Int1D,
                                    params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexLevelParameterfvEXT(self, texunit: int, target: int,
                                         level: int, pname: int,
                                         params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexLevelParameterfvEXT(self, texunit: int, target: int,
                                         level: int, pname: int,
                                         params: Float1D,
                                         params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexLevelParameterivEXT(self, texunit: int, target: int,
                                         level: int, pname: int,
                                         params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexLevelParameterivEXT(self, texunit: int, target: int,
                                         level: int, pname: int, params: Int1D,
                                         params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexImage3DEXT(self, texunit: int, target: int, level: int,
                             internalformat: int, width: int, height: int,
                             depth: int, border: int, format: int, type: int,
                             pixels: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexSubImage3DEXT(self, texunit: int, target: int, level: int,
                                xoffset: int, yoffset: int, zoffset: int,
                                width: int, height: int, depth: int,
                                format: int, type: int,
                                pixels: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCopyMultiTexSubImage3DEXT(self, texunit: int, target: int,
                                    level: int, xoffset: int, yoffset: int,
                                    zoffset: int, x: int, y: int, width: int,
                                    height: int) -> None:
        """
    
        """

    @staticmethod
    def glEnableClientStateIndexedEXT(self, array: int, index: int) -> None:
        """
    
        """

    @staticmethod
    def glDisableClientStateIndexedEXT(self, array: int, index: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFloatIndexedvEXT(self, target: int, index: int,
                              data: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFloatIndexedvEXT(self, target: int, index: int, data: Float1D,
                              data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetDoubleIndexedvEXT(self, target: int, index: int,
                               data: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetDoubleIndexedvEXT(self, target: int, index: int, data: Double1D,
                               data_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glEnableIndexed(self, target: int, index: int) -> None:
        """
    
        """

    @staticmethod
    def glDisableIndexed(self, target: int, index: int) -> None:
        """
    
        """

    @staticmethod
    def glIsEnabledIndexed(self, target: int, index: int) -> bool:
        """
    
        """

    @overload
    @staticmethod
    def glGetIntegerIndexedv(self, target: int, index: int,
                             data: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetIntegerIndexedv(self, target: int, index: int, data: Int1D,
                             data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetBooleanIndexedv(self, target: int, index: int,
                             data: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetBooleanIndexedv(self, target: int, index: int, data: Byte1D,
                             data_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glCompressedTextureImage3DEXT(self, texture: int, target: int,
                                      level: int, internalformat: int,
                                      width: int, height: int, depth: int,
                                      border: int, imageSize: int,
                                      bits: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCompressedTextureImage2DEXT(self, texture: int, target: int,
                                      level: int, internalformat: int,
                                      width: int, height: int, border: int,
                                      imageSize: int, bits: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCompressedTextureImage1DEXT(self, texture: int, target: int,
                                      level: int, internalformat: int,
                                      width: int, border: int, imageSize: int,
                                      bits: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCompressedTextureSubImage3DEXT(self, texture: int, target: int,
                                         level: int, xoffset: int,
                                         yoffset: int, zoffset: int,
                                         width: int, height: int, depth: int,
                                         format: int, imageSize: int,
                                         bits: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCompressedTextureSubImage2DEXT(self, texture: int, target: int,
                                         level: int, xoffset: int,
                                         yoffset: int, width: int, height: int,
                                         format: int, imageSize: int,
                                         bits: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCompressedTextureSubImage1DEXT(self, texture: int, target: int,
                                         level: int, xoffset: int, width: int,
                                         format: int, imageSize: int,
                                         bits: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glGetCompressedTextureImageEXT(self, texture: int, target: int,
                                       lod: int, img: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCompressedMultiTexImage3DEXT(self, texunit: int, target: int,
                                       level: int, internalformat: int,
                                       width: int, height: int, depth: int,
                                       border: int, imageSize: int,
                                       bits: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCompressedMultiTexImage2DEXT(self, texunit: int, target: int,
                                       level: int, internalformat: int,
                                       width: int, height: int, border: int,
                                       imageSize: int, bits: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCompressedMultiTexImage1DEXT(self, texunit: int, target: int,
                                       level: int, internalformat: int,
                                       width: int, border: int, imageSize: int,
                                       bits: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCompressedMultiTexSubImage3DEXT(self, texunit: int, target: int,
                                          level: int, xoffset: int,
                                          yoffset: int, zoffset: int,
                                          width: int, height: int, depth: int,
                                          format: int, imageSize: int,
                                          bits: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCompressedMultiTexSubImage2DEXT(self, texunit: int, target: int,
                                          level: int, xoffset: int,
                                          yoffset: int, width: int,
                                          height: int, format: int,
                                          imageSize: int,
                                          bits: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glCompressedMultiTexSubImage1DEXT(self, texunit: int, target: int,
                                          level: int, xoffset: int, width: int,
                                          format: int, imageSize: int,
                                          bits: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glGetCompressedMultiTexImageEXT(self, texunit: int, target: int,
                                        lod: int, img: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixLoadTransposefEXT(self, mode: int, m: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixLoadTransposefEXT(self, mode: int, m: Float1D,
                                  m_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixLoadTransposedEXT(self, mode: int, m: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixLoadTransposedEXT(self, mode: int, m: Double1D,
                                  m_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixMultTransposefEXT(self, mode: int, m: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixMultTransposefEXT(self, mode: int, m: Float1D,
                                  m_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixMultTransposedEXT(self, mode: int, m: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMatrixMultTransposedEXT(self, mode: int, m: Double1D,
                                  m_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedBufferDataEXT(self, buffer: int, size: long, data: Buffer,
                             usage: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedBufferSubDataEXT(self, buffer: int, offset: long, size: long,
                                data: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glMapNamedBufferEXT(self, buffer: int, access: int) -> ByteBuffer:
        """
    
        """

    @staticmethod
    def glUnmapNamedBufferEXT(self, buffer: int) -> bool:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedBufferParameterivEXT(self, buffer: int, pname: int,
                                       params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedBufferParameterivEXT(self, buffer: int, pname: int,
                                       params: Int1D,
                                       params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetNamedBufferSubDataEXT(self, buffer: int, offset: long, size: long,
                                   data: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glTextureBufferEXT(self, texture: int, target: int,
                           internalformat: int, buffer: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexBufferEXT(self, texunit: int, target: int,
                            internalformat: int, buffer: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureParameterIivEXT(self, texture: int, target: int, pname: int,
                                 params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureParameterIivEXT(self, texture: int, target: int, pname: int,
                                 params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureParameterIuivEXT(self, texture: int, target: int, pname: int,
                                  params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTextureParameterIuivEXT(self, texture: int, target: int, pname: int,
                                  params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTextureParameterIivEXT(self, texture: int, target: int,
                                    pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTextureParameterIivEXT(self, texture: int, target: int,
                                    pname: int, params: Int1D,
                                    params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTextureParameterIuivEXT(self, texture: int, target: int,
                                     pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTextureParameterIuivEXT(self, texture: int, target: int,
                                     pname: int, params: Int1D,
                                     params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexParameterIivEXT(self, texunit: int, target: int, pname: int,
                                  params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexParameterIivEXT(self, texunit: int, target: int, pname: int,
                                  params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexParameterIuivEXT(self, texunit: int, target: int, pname: int,
                                   params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexParameterIuivEXT(self, texunit: int, target: int, pname: int,
                                   params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexParameterIivEXT(self, texunit: int, target: int,
                                     pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexParameterIivEXT(self, texunit: int, target: int,
                                     pname: int, params: Int1D,
                                     params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexParameterIuivEXT(self, texunit: int, target: int,
                                      pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultiTexParameterIuivEXT(self, texunit: int, target: int,
                                      pname: int, params: Int1D,
                                      params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParameters4fvEXT(self, program: int, target: int,
                                            index: int, count: int,
                                            params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParameters4fvEXT(self, program: int, target: int,
                                            index: int, count: int,
                                            params: Float1D,
                                            params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedProgramLocalParameterI4iEXT(self, program: int, target: int,
                                           index: int, x: int, y: int, z: int,
                                           w: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParameterI4ivEXT(self, program: int, target: int,
                                            index: int,
                                            params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParameterI4ivEXT(self, program: int, target: int,
                                            index: int, params: Int1D,
                                            params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParametersI4ivEXT(self, program: int, target: int,
                                             index: int, count: int,
                                             params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParametersI4ivEXT(self, program: int, target: int,
                                             index: int, count: int,
                                             params: Int1D,
                                             params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedProgramLocalParameterI4uiEXT(self, program: int, target: int,
                                            index: int, x: int, y: int, z: int,
                                            w: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParameterI4uivEXT(self, program: int, target: int,
                                             index: int,
                                             params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParameterI4uivEXT(self, program: int, target: int,
                                             index: int, params: Int1D,
                                             params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParametersI4uivEXT(self, program: int, target: int,
                                              index: int, count: int,
                                              params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParametersI4uivEXT(self, program: int, target: int,
                                              index: int, count: int,
                                              params: Int1D,
                                              params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedProgramLocalParameterIivEXT(self, program: int, target: int,
                                              index: int,
                                              params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedProgramLocalParameterIivEXT(self, program: int, target: int,
                                              index: int, params: Int1D,
                                              params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedProgramLocalParameterIuivEXT(self, program: int, target: int,
                                               index: int,
                                               params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedProgramLocalParameterIuivEXT(self, program: int, target: int,
                                               index: int, params: Int1D,
                                               params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glEnableClientStateiEXT(self, array: int, index: int) -> None:
        """
    
        """

    @staticmethod
    def glDisableClientStateiEXT(self, array: int, index: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFloati_vEXT(self, pname: int, index: int,
                         params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFloati_vEXT(self, pname: int, index: int, params: Float1D,
                         params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetDoublei_vEXT(self, pname: int, index: int,
                          params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetDoublei_vEXT(self, pname: int, index: int, params: Double1D,
                          params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetPointeri_vEXT(self, pname: int, index: int,
                           params: PointerBuffer) -> None:
        """
    
        """

    @staticmethod
    def glNamedProgramStringEXT(self, program: int, target: int, format: int,
                                len: int, string: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glNamedProgramLocalParameter4dEXT(self, program: int, target: int,
                                          index: int, x: double, y: double,
                                          z: double, w: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParameter4dvEXT(self, program: int, target: int,
                                           index: int,
                                           params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParameter4dvEXT(self, program: int, target: int,
                                           index: int, params: Double1D,
                                           params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedProgramLocalParameter4fEXT(self, program: int, target: int,
                                          index: int, x: float, y: float,
                                          z: float, w: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParameter4fvEXT(self, program: int, target: int,
                                           index: int,
                                           params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedProgramLocalParameter4fvEXT(self, program: int, target: int,
                                           index: int, params: Float1D,
                                           params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedProgramLocalParameterdvEXT(self, program: int, target: int,
                                             index: int,
                                             params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedProgramLocalParameterdvEXT(self, program: int, target: int,
                                             index: int, params: Double1D,
                                             params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedProgramLocalParameterfvEXT(self, program: int, target: int,
                                             index: int,
                                             params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedProgramLocalParameterfvEXT(self, program: int, target: int,
                                             index: int, params: Float1D,
                                             params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedProgramivEXT(self, program: int, target: int, pname: int,
                               params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedProgramivEXT(self, program: int, target: int, pname: int,
                               params: Int1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetNamedProgramStringEXT(self, program: int, target: int, pname: int,
                                   string: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glNamedRenderbufferStorageEXT(self, renderbuffer: int,
                                      internalformat: int, width: int,
                                      height: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedRenderbufferParameterivEXT(self, renderbuffer: int,
                                             pname: int,
                                             params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedRenderbufferParameterivEXT(self, renderbuffer: int,
                                             pname: int, params: Int1D,
                                             params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedRenderbufferStorageMultisampleEXT(self, renderbuffer: int,
                                                 samples: int,
                                                 internalformat: int,
                                                 width: int,
                                                 height: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedRenderbufferStorageMultisampleCoverageEXT(
            self, renderbuffer: int, coverageSamples: int, colorSamples: int,
            internalformat: int, width: int, height: int) -> None:
        """
    
        """

    @staticmethod
    def glCheckNamedFramebufferStatusEXT(self, framebuffer: int,
                                         target: int) -> int:
        """
    
        """

    @staticmethod
    def glNamedFramebufferTexture1DEXT(self, framebuffer: int, attachment: int,
                                       textarget: int, texture: int,
                                       level: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedFramebufferTexture2DEXT(self, framebuffer: int, attachment: int,
                                       textarget: int, texture: int,
                                       level: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedFramebufferTexture3DEXT(self, framebuffer: int, attachment: int,
                                       textarget: int, texture: int,
                                       level: int, zoffset: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedFramebufferRenderbufferEXT(self, framebuffer: int,
                                          attachment: int,
                                          renderbuffertarget: int,
                                          renderbuffer: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedFramebufferAttachmentParameterivEXT(
            self, framebuffer: int, attachment: int, pname: int,
            params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedFramebufferAttachmentParameterivEXT(
            self, framebuffer: int, attachment: int, pname: int, params: Int1D,
            params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGenerateTextureMipmapEXT(self, texture: int, target: int) -> None:
        """
    
        """

    @staticmethod
    def glGenerateMultiTexMipmapEXT(self, texunit: int, target: int) -> None:
        """
    
        """

    @staticmethod
    def glFramebufferDrawBufferEXT(self, framebuffer: int, mode: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFramebufferDrawBuffersEXT(self, framebuffer: int, n: int,
                                    bufs: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFramebufferDrawBuffersEXT(self, framebuffer: int, n: int,
                                    bufs: Int1D, bufs_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glFramebufferReadBufferEXT(self, framebuffer: int, mode: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFramebufferParameterivEXT(self, framebuffer: int, pname: int,
                                       params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFramebufferParameterivEXT(self, framebuffer: int, pname: int,
                                       params: Int1D,
                                       params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedCopyBufferSubDataEXT(self, readBuffer: int, writeBuffer: int,
                                    readOffset: long, writeOffset: long,
                                    size: long) -> None:
        """
    
        """

    @staticmethod
    def glNamedFramebufferTextureEXT(self, framebuffer: int, attachment: int,
                                     texture: int, level: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedFramebufferTextureLayerEXT(self, framebuffer: int,
                                          attachment: int, texture: int,
                                          level: int, layer: int) -> None:
        """
    
        """

    @staticmethod
    def glNamedFramebufferTextureFaceEXT(self, framebuffer: int,
                                         attachment: int, texture: int,
                                         level: int, face: int) -> None:
        """
    
        """

    @staticmethod
    def glTextureRenderbufferEXT(self, texture: int, target: int,
                                 renderbuffer: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexRenderbufferEXT(self, texunit: int, target: int,
                                  renderbuffer: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayVertexOffsetEXT(self, vaobj: int, buffer: int, size: int,
                                     type: int, stride: int,
                                     offset: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayColorOffsetEXT(self, vaobj: int, buffer: int, size: int,
                                    type: int, stride: int,
                                    offset: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayEdgeFlagOffsetEXT(self, vaobj: int, buffer: int,
                                       stride: int, offset: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayIndexOffsetEXT(self, vaobj: int, buffer: int, type: int,
                                    stride: int, offset: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayNormalOffsetEXT(self, vaobj: int, buffer: int, type: int,
                                     stride: int, offset: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayTexCoordOffsetEXT(self, vaobj: int, buffer: int,
                                       size: int, type: int, stride: int,
                                       offset: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayMultiTexCoordOffsetEXT(self, vaobj: int, buffer: int,
                                            texunit: int, size: int, type: int,
                                            stride: int, offset: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayFogCoordOffsetEXT(self, vaobj: int, buffer: int,
                                       type: int, stride: int,
                                       offset: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexArraySecondaryColorOffsetEXT(self, vaobj: int, buffer: int,
                                             size: int, type: int, stride: int,
                                             offset: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayVertexAttribOffsetEXT(self, vaobj: int, buffer: int,
                                           index: int, size: int, type: int,
                                           normalized: bool, stride: int,
                                           offset: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayVertexAttribIOffsetEXT(self, vaobj: int, buffer: int,
                                            index: int, size: int, type: int,
                                            stride: int, offset: long) -> None:
        """
    
        """

    @staticmethod
    def glEnableVertexArrayEXT(self, vaobj: int, array: int) -> None:
        """
    
        """

    @staticmethod
    def glDisableVertexArrayEXT(self, vaobj: int, array: int) -> None:
        """
    
        """

    @staticmethod
    def glEnableVertexArrayAttribEXT(self, vaobj: int, index: int) -> None:
        """
    
        """

    @staticmethod
    def glDisableVertexArrayAttribEXT(self, vaobj: int, index: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexArrayIntegervEXT(self, vaobj: int, pname: int,
                                    param: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexArrayIntegervEXT(self, vaobj: int, pname: int, param: Int1D,
                                    param_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetVertexArrayPointervEXT(self, vaobj: int, pname: int,
                                    param: PointerBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexArrayIntegeri_vEXT(self, vaobj: int, index: int, pname: int,
                                      param: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexArrayIntegeri_vEXT(self, vaobj: int, index: int, pname: int,
                                      param: Int1D, param_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetVertexArrayPointeri_vEXT(self, vaobj: int, index: int, pname: int,
                                      param: PointerBuffer) -> None:
        """
    
        """

    @staticmethod
    def glMapNamedBufferRangeEXT(self, buffer: int, offset: long, length: long,
                                 access: int) -> ByteBuffer:
        """
    
        """

    @staticmethod
    def glFlushMappedNamedBufferRangeEXT(self, buffer: int, offset: long,
                                         length: long) -> None:
        """
    
        """

    @staticmethod
    def glNamedBufferStorageEXT(self, buffer: int, size: long, data: Buffer,
                                flags: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform1dEXT(self, program: int, location: int,
                              x: double) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform2dEXT(self, program: int, location: int, x: double,
                              y: double) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform3dEXT(self, program: int, location: int, x: double,
                              y: double, z: double) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform4dEXT(self, program: int, location: int, x: double,
                              y: double, z: double, w: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1dvEXT(self, program: int, location: int, count: int,
                               value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1dvEXT(self, program: int, location: int, count: int,
                               value: Double1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2dvEXT(self, program: int, location: int, count: int,
                               value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2dvEXT(self, program: int, location: int, count: int,
                               value: Double1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3dvEXT(self, program: int, location: int, count: int,
                               value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3dvEXT(self, program: int, location: int, count: int,
                               value: Double1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4dvEXT(self, program: int, location: int, count: int,
                               value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4dvEXT(self, program: int, location: int, count: int,
                               value: Double1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2dvEXT(self, program: int, location: int,
                                     count: int, transpose: bool,
                                     value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2dvEXT(self, program: int, location: int,
                                     count: int, transpose: bool,
                                     value: Double1D,
                                     value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3dvEXT(self, program: int, location: int,
                                     count: int, transpose: bool,
                                     value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3dvEXT(self, program: int, location: int,
                                     count: int, transpose: bool,
                                     value: Double1D,
                                     value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4dvEXT(self, program: int, location: int,
                                     count: int, transpose: bool,
                                     value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4dvEXT(self, program: int, location: int,
                                     count: int, transpose: bool,
                                     value: Double1D,
                                     value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2x3dvEXT(self, program: int, location: int,
                                       count: int, transpose: bool,
                                       value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2x3dvEXT(self, program: int, location: int,
                                       count: int, transpose: bool,
                                       value: Double1D,
                                       value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2x4dvEXT(self, program: int, location: int,
                                       count: int, transpose: bool,
                                       value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2x4dvEXT(self, program: int, location: int,
                                       count: int, transpose: bool,
                                       value: Double1D,
                                       value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3x2dvEXT(self, program: int, location: int,
                                       count: int, transpose: bool,
                                       value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3x2dvEXT(self, program: int, location: int,
                                       count: int, transpose: bool,
                                       value: Double1D,
                                       value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3x4dvEXT(self, program: int, location: int,
                                       count: int, transpose: bool,
                                       value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3x4dvEXT(self, program: int, location: int,
                                       count: int, transpose: bool,
                                       value: Double1D,
                                       value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4x2dvEXT(self, program: int, location: int,
                                       count: int, transpose: bool,
                                       value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4x2dvEXT(self, program: int, location: int,
                                       count: int, transpose: bool,
                                       value: Double1D,
                                       value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4x3dvEXT(self, program: int, location: int,
                                       count: int, transpose: bool,
                                       value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4x3dvEXT(self, program: int, location: int,
                                       count: int, transpose: bool,
                                       value: Double1D,
                                       value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTextureBufferRangeEXT(self, texture: int, target: int,
                                internalformat: int, buffer: int, offset: long,
                                size: long) -> None:
        """
    
        """

    @staticmethod
    def glTextureStorage2DMultisampleEXT(self, texture: int, target: int,
                                         samples: int, internalformat: int,
                                         width: int, height: int,
                                         fixedsamplelocations: bool) -> None:
        """
    
        """

    @staticmethod
    def glTextureStorage3DMultisampleEXT(self, texture: int, target: int,
                                         samples: int, internalformat: int,
                                         width: int, height: int, depth: int,
                                         fixedsamplelocations: bool) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayBindVertexBufferEXT(self, vaobj: int, bindingindex: int,
                                         buffer: int, offset: long,
                                         stride: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayVertexAttribFormatEXT(self, vaobj: int, attribindex: int,
                                           size: int, type: int,
                                           normalized: bool,
                                           relativeoffset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayVertexAttribIFormatEXT(self, vaobj: int, attribindex: int,
                                            size: int, type: int,
                                            relativeoffset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayVertexAttribLFormatEXT(self, vaobj: int, attribindex: int,
                                            size: int, type: int,
                                            relativeoffset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayVertexAttribBindingEXT(self, vaobj: int, attribindex: int,
                                            bindingindex: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayVertexBindingDivisorEXT(self, vaobj: int,
                                             bindingindex: int,
                                             divisor: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayVertexAttribLOffsetEXT(self, vaobj: int, buffer: int,
                                            index: int, size: int, type: int,
                                            stride: int, offset: long) -> None:
        """
    
        """

    @staticmethod
    def glTexturePageCommitmentEXT(self, texture: int, level: int,
                                   xoffset: int, yoffset: int, zoffset: int,
                                   width: int, height: int, depth: int,
                                   commit: bool) -> None:
        """
    
        """

    @staticmethod
    def glVertexArrayVertexAttribDivisorEXT(self, vaobj: int, index: int,
                                            divisor: int) -> None:
        """
    
        """

    @staticmethod
    def glColorMaskIndexed(self, index: int, r: bool, g: bool, b: bool,
                           a: bool) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParameters4fvEXT(self, target: int, index: int, count: int,
                                     params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParameters4fvEXT(self, target: int, index: int, count: int,
                                     params: Float1D,
                                     params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParameters4fvEXT(self, target: int, index: int,
                                       count: int,
                                       params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParameters4fvEXT(self, target: int, index: int,
                                       count: int, params: Float1D,
                                       params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glIndexFuncEXT(self, func: int, ref: float) -> None:
        """
    
        """

    @staticmethod
    def glIndexMaterialEXT(self, face: int, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glApplyTextureEXT(self, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glTextureLightEXT(self, pname: int) -> None:
        """
    
        """

    @staticmethod
    def glTextureMaterialEXT(self, face: int, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glPixelTransformParameteriEXT(self, target: int, pname: int,
                                      param: int) -> None:
        """
    
        """

    @staticmethod
    def glPixelTransformParameterfEXT(self, target: int, pname: int,
                                      param: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelTransformParameterivEXT(self, target: int, pname: int,
                                       params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelTransformParameterivEXT(self, target: int, pname: int,
                                       params: Int1D,
                                       params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelTransformParameterfvEXT(self, target: int, pname: int,
                                       params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPixelTransformParameterfvEXT(self, target: int, pname: int,
                                       params: Float1D,
                                       params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelTransformParameterivEXT(self, target: int, pname: int,
                                          params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelTransformParameterivEXT(self, target: int, pname: int,
                                          params: Int1D,
                                          params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelTransformParameterfvEXT(self, target: int, pname: int,
                                          params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPixelTransformParameterfvEXT(self, target: int, pname: int,
                                          params: Float1D,
                                          params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glPolygonOffsetClampEXT(self, factor: float, units: float,
                                clamp: float) -> None:
        """
    
        """

    @staticmethod
    def glProvokingVertexEXT(self, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glRasterSamplesEXT(self, samples: int,
                           fixedsamplelocations: bool) -> None:
        """
    
        """

    @staticmethod
    def glStencilClearTagEXT(self, stencilTagBits: int,
                             stencilClearTag: int) -> None:
        """
    
        """

    @staticmethod
    def glActiveStencilFaceEXT(self, face: int) -> None:
        """
    
        """

    @staticmethod
    def glClearColorIi(self, red: int, green: int, blue: int,
                       alpha: int) -> None:
        """
    
        """

    @staticmethod
    def glClearColorIui(self, red: int, green: int, blue: int,
                        alpha: int) -> None:
        """
    
        """

    @staticmethod
    def glTextureNormalEXT(self, mode: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryObjecti64vEXT(self, id: int, pname: int,
                                params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryObjecti64vEXT(self, id: int, pname: int, params: Long1D,
                                params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryObjectui64vEXT(self, id: int, pname: int,
                                 params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryObjectui64vEXT(self, id: int, pname: int, params: Long1D,
                                 params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glBeginVertexShaderEXT(self) -> None:
        """
    
        """

    @staticmethod
    def glEndVertexShaderEXT(self) -> None:
        """
    
        """

    @staticmethod
    def glBindVertexShaderEXT(self, id: int) -> None:
        """
    
        """

    @staticmethod
    def glGenVertexShadersEXT(self, range: int) -> int:
        """
    
        """

    @staticmethod
    def glDeleteVertexShaderEXT(self, id: int) -> None:
        """
    
        """

    @staticmethod
    def glShaderOp1EXT(self, op: int, res: int, arg1: int) -> None:
        """
    
        """

    @staticmethod
    def glShaderOp2EXT(self, op: int, res: int, arg1: int, arg2: int) -> None:
        """
    
        """

    @staticmethod
    def glShaderOp3EXT(self, op: int, res: int, arg1: int, arg2: int,
                       arg3: int) -> None:
        """
    
        """

    @staticmethod
    def glSwizzleEXT(self, res: int, ins: int, outX: int, outY: int, outZ: int,
                     outW: int) -> None:
        """
    
        """

    @staticmethod
    def glWriteMaskEXT(self, res: int, ins: int, outX: int, outY: int,
                       outZ: int, outW: int) -> None:
        """
    
        """

    @staticmethod
    def glInsertComponentEXT(self, res: int, src: int, num: int) -> None:
        """
    
        """

    @staticmethod
    def glExtractComponentEXT(self, res: int, src: int, num: int) -> None:
        """
    
        """

    @staticmethod
    def glGenSymbolsEXT(self, datatype: int, storagetype: int, range: int,
                        components: int) -> int:
        """
    
        """

    @staticmethod
    def glSetInvariantEXT(self, id: int, type: int, addr: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glSetLocalConstantEXT(self, id: int, type: int, addr: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantbvEXT(self, id: int, addr: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantbvEXT(self, id: int, addr: Byte1D, addr_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantsvEXT(self, id: int, addr: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantsvEXT(self, id: int, addr: Short1D, addr_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantivEXT(self, id: int, addr: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantivEXT(self, id: int, addr: Int1D, addr_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantfvEXT(self, id: int, addr: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantfvEXT(self, id: int, addr: Float1D, addr_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantdvEXT(self, id: int, addr: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantdvEXT(self, id: int, addr: Double1D,
                       addr_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantubvEXT(self, id: int, addr: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantubvEXT(self, id: int, addr: Byte1D, addr_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantusvEXT(self, id: int, addr: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantusvEXT(self, id: int, addr: Short1D,
                        addr_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantuivEXT(self, id: int, addr: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantuivEXT(self, id: int, addr: Int1D, addr_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantPointerEXT(self, id: int, type: int, stride: int,
                            addr: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVariantPointerEXT(self, id: int, type: int, stride: int,
                            addr_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glEnableVariantClientStateEXT(self, id: int) -> None:
        """
    
        """

    @staticmethod
    def glDisableVariantClientStateEXT(self, id: int) -> None:
        """
    
        """

    @staticmethod
    def glBindLightParameterEXT(self, light: int, value: int) -> int:
        """
    
        """

    @staticmethod
    def glBindMaterialParameterEXT(self, face: int, value: int) -> int:
        """
    
        """

    @staticmethod
    def glBindTexGenParameterEXT(self, unit: int, coord: int,
                                 value: int) -> int:
        """
    
        """

    @staticmethod
    def glBindTextureUnitParameterEXT(self, unit: int, value: int) -> int:
        """
    
        """

    @staticmethod
    def glBindParameterEXT(self, value: int) -> int:
        """
    
        """

    @staticmethod
    def glIsVariantEnabledEXT(self, id: int, cap: int) -> bool:
        """
    
        """

    @overload
    @staticmethod
    def glGetVariantBooleanvEXT(self, id: int, value: int,
                                data: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVariantBooleanvEXT(self, id: int, value: int, data: Byte1D,
                                data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVariantIntegervEXT(self, id: int, value: int,
                                data: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVariantIntegervEXT(self, id: int, value: int, data: Int1D,
                                data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVariantFloatvEXT(self, id: int, value: int,
                              data: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVariantFloatvEXT(self, id: int, value: int, data: Float1D,
                              data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetInvariantBooleanvEXT(self, id: int, value: int,
                                  data: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetInvariantBooleanvEXT(self, id: int, value: int, data: Byte1D,
                                  data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetInvariantIntegervEXT(self, id: int, value: int,
                                  data: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetInvariantIntegervEXT(self, id: int, value: int, data: Int1D,
                                  data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetInvariantFloatvEXT(self, id: int, value: int,
                                data: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetInvariantFloatvEXT(self, id: int, value: int, data: Float1D,
                                data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetLocalConstantBooleanvEXT(self, id: int, value: int,
                                      data: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetLocalConstantBooleanvEXT(self, id: int, value: int, data: Byte1D,
                                      data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetLocalConstantIntegervEXT(self, id: int, value: int,
                                      data: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetLocalConstantIntegervEXT(self, id: int, value: int, data: Int1D,
                                      data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetLocalConstantFloatvEXT(self, id: int, value: int,
                                    data: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetLocalConstantFloatvEXT(self, id: int, value: int, data: Float1D,
                                    data_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexWeightfEXT(self, weight: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexWeightfvEXT(self, weight: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexWeightfvEXT(self, weight: Float1D, weight_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexWeightPointerEXT(self, size: int, type: int, stride: int,
                                 pointer: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexWeightPointerEXT(self, size: int, type: int, stride: int,
                                 pointer_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glFrameTerminatorGREMEDY(self) -> None:
        """
    
        """

    @staticmethod
    def glStringMarkerGREMEDY(self, len: int, string: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glBlendFuncSeparateINGR(self, sfactorRGB: int, dfactorRGB: int,
                                sfactorAlpha: int, dfactorAlpha: int) -> None:
        """
    
        """

    @staticmethod
    def glSyncTextureINTEL(self, texture: int) -> None:
        """
    
        """

    @staticmethod
    def glUnmapTexture2DINTEL(self, texture: int, level: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMapTexture2DINTEL(self, texture: int, level: int, access: int,
                            stride: IntBuffer,
                            layout: IntBuffer) -> ByteBuffer:
        """
    
        """

    @overload
    @staticmethod
    def glMapTexture2DINTEL(self, texture: int, level: int, access: int,
                            stride: Int1D, stride_offset: int, layout: Int1D,
                            layout_offset: int) -> ByteBuffer:
        """
    
        """

    @staticmethod
    def glBeginPerfQueryINTEL(self, queryHandle: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCreatePerfQueryINTEL(self, queryId: int,
                               queryHandle: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCreatePerfQueryINTEL(self, queryId: int, queryHandle: Int1D,
                               queryHandle_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glDeletePerfQueryINTEL(self, queryHandle: int) -> None:
        """
    
        """

    @staticmethod
    def glEndPerfQueryINTEL(self, queryHandle: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFirstPerfQueryIdINTEL(self, queryId: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFirstPerfQueryIdINTEL(self, queryId: Int1D,
                                   queryId_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNextPerfQueryIdINTEL(self, queryId: int,
                                  nextQueryId: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNextPerfQueryIdINTEL(self, queryId: int, nextQueryId: Int1D,
                                  nextQueryId_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfCounterInfoINTEL(self, queryId: int, counterId: int,
                                  counterNameLength: int,
                                  counterName: ByteBuffer,
                                  counterDescLength: int,
                                  counterDesc: ByteBuffer,
                                  counterOffset: IntBuffer,
                                  counterDataSize: IntBuffer,
                                  counterTypeEnum: IntBuffer,
                                  counterDataTypeEnum: IntBuffer,
                                  rawCounterMaxValue: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfCounterInfoINTEL(self, queryId: int, counterId: int,
                                  counterNameLength: int, counterName: Byte1D,
                                  counterName_offset: int,
                                  counterDescLength: int, counterDesc: Byte1D,
                                  counterDesc_offset: int,
                                  counterOffset: Int1D,
                                  counterOffset_offset: int,
                                  counterDataSize: Int1D,
                                  counterDataSize_offset: int,
                                  counterTypeEnum: Int1D,
                                  counterTypeEnum_offset: int,
                                  counterDataTypeEnum: Int1D,
                                  counterDataTypeEnum_offset: int,
                                  rawCounterMaxValue: Long1D,
                                  rawCounterMaxValue_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfQueryDataINTEL(self, queryHandle: int, flags: int,
                                dataSize: int, data: Buffer,
                                bytesWritten: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfQueryDataINTEL(self, queryHandle: int, flags: int,
                                dataSize: int, data: Buffer,
                                bytesWritten: Int1D,
                                bytesWritten_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfQueryIdByNameINTEL(self, queryName: ByteBuffer,
                                    queryId: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfQueryIdByNameINTEL(self, queryName: Byte1D,
                                    queryName_offset: int, queryId: Int1D,
                                    queryId_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfQueryInfoINTEL(self, queryId: int, queryNameLength: int,
                                queryName: ByteBuffer, dataSize: IntBuffer,
                                noCounters: IntBuffer, noInstances: IntBuffer,
                                capsMask: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetPerfQueryInfoINTEL(self, queryId: int, queryNameLength: int,
                                queryName: Byte1D, queryName_offset: int,
                                dataSize: Int1D, dataSize_offset: int,
                                noCounters: Int1D, noCounters_offset: int,
                                noInstances: Int1D, noInstances_offset: int,
                                capsMask: Int1D, capsMask_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glBeginConditionalRenderNVX(self, id: int) -> None:
        """
    
        """

    @staticmethod
    def glEndConditionalRenderNVX(self) -> None:
        """
    
        """

    @staticmethod
    def glMultiDrawArraysIndirectBindlessNV(self, mode: int, indirect: Buffer,
                                            drawCount: int, stride: int,
                                            vertexBufferCount: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiDrawElementsIndirectBindlessNV(self, mode: int, type: int,
                                              indirect: Buffer, drawCount: int,
                                              stride: int,
                                              vertexBufferCount: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiDrawArraysIndirectBindlessCountNV(
            self, mode: int, indirect: Buffer, drawCount: int,
            maxDrawCount: int, stride: int, vertexBufferCount: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiDrawElementsIndirectBindlessCountNV(
            self, mode: int, type: int, indirect: Buffer, drawCount: int,
            maxDrawCount: int, stride: int, vertexBufferCount: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCreateStatesNV(self, n: int, states: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCreateStatesNV(self, n: int, states: Int1D,
                         states_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteStatesNV(self, n: int, states: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteStatesNV(self, n: int, states: Int1D,
                         states_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glIsStateNV(self, state: int) -> bool:
        """
    
        """

    @staticmethod
    def glStateCaptureNV(self, state: int, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glGetCommandHeaderNV(self, tokenID: int, size: int) -> int:
        """
    
        """

    @staticmethod
    def glGetStageIndexNV(self, shadertype: int) -> short:
        """
    
        """

    @overload
    @staticmethod
    def glDrawCommandsNV(self, primitiveMode: int, buffer: int,
                         indirects: PointerBuffer, sizes: IntBuffer,
                         count: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawCommandsNV(self, primitiveMode: int, buffer: int,
                         indirects: PointerBuffer, sizes: Int1D,
                         sizes_offset: int, count: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawCommandsAddressNV(self, primitiveMode: int,
                                indirects: LongBuffer, sizes: IntBuffer,
                                count: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawCommandsAddressNV(self, primitiveMode: int, indirects: Long1D,
                                indirects_offset: int, sizes: Int1D,
                                sizes_offset: int, count: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawCommandsStatesNV(self, buffer: int, indirects: PointerBuffer,
                               sizes: IntBuffer, states: IntBuffer,
                               fbos: IntBuffer, count: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawCommandsStatesNV(self, buffer: int, indirects: PointerBuffer,
                               sizes: Int1D, sizes_offset: int, states: Int1D,
                               states_offset: int, fbos: Int1D,
                               fbos_offset: int, count: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawCommandsStatesAddressNV(self, indirects: LongBuffer,
                                      sizes: IntBuffer, states: IntBuffer,
                                      fbos: IntBuffer, count: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawCommandsStatesAddressNV(self, indirects: Long1D,
                                      indirects_offset: int, sizes: Int1D,
                                      sizes_offset: int, states: Int1D,
                                      states_offset: int, fbos: Int1D,
                                      fbos_offset: int, count: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCreateCommandListsNV(self, n: int, lists: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCreateCommandListsNV(self, n: int, lists: Int1D,
                               lists_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteCommandListsNV(self, n: int, lists: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteCommandListsNV(self, n: int, lists: Int1D,
                               lists_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glIsCommandListNV(self, list: int) -> bool:
        """
    
        """

    @overload
    @staticmethod
    def glListDrawCommandsStatesClientNV(self, list: int, segment: int,
                                         indirects: PointerBuffer,
                                         sizes: IntBuffer, states: IntBuffer,
                                         fbos: IntBuffer, count: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glListDrawCommandsStatesClientNV(self, list: int, segment: int,
                                         indirects: PointerBuffer,
                                         sizes: Int1D, sizes_offset: int,
                                         states: Int1D, states_offset: int,
                                         fbos: Int1D, fbos_offset: int,
                                         count: int) -> None:
        """
    
        """

    @staticmethod
    def glCommandListSegmentsNV(self, list: int, segments: int) -> None:
        """
    
        """

    @staticmethod
    def glCompileCommandListNV(self, list: int) -> None:
        """
    
        """

    @staticmethod
    def glCallCommandListNV(self, list: int) -> None:
        """
    
        """

    @staticmethod
    def glSubpixelPrecisionBiasNV(self, xbits: int, ybits: int) -> None:
        """
    
        """

    @staticmethod
    def glConservativeRasterParameterfNV(self, pname: int,
                                         value: float) -> None:
        """
    
        """

    @staticmethod
    def glCopyImageSubDataNV(self, srcName: int, srcTarget: int, srcLevel: int,
                             srcX: int, srcY: int, srcZ: int, dstName: int,
                             dstTarget: int, dstLevel: int, dstX: int,
                             dstY: int, dstZ: int, width: int, height: int,
                             depth: int) -> None:
        """
    
        """

    @staticmethod
    def glDrawTextureNV(self, texture: int, sampler: int, x0: float, y0: float,
                        x1: float, y1: float, z: float, s0: float, t0: float,
                        s1: float, t1: float) -> None:
        """
    
        """

    @staticmethod
    def glMapControlPointsNV(self, target: int, index: int, type: int,
                             ustride: int, vstride: int, uorder: int,
                             vorder: int, packed: bool,
                             points: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMapParameterivNV(self, target: int, pname: int,
                           params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMapParameterivNV(self, target: int, pname: int, params: Int1D,
                           params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMapParameterfvNV(self, target: int, pname: int,
                           params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMapParameterfvNV(self, target: int, pname: int, params: Float1D,
                           params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetMapControlPointsNV(self, target: int, index: int, type: int,
                                ustride: int, vstride: int, packed: bool,
                                points: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapParameterivNV(self, target: int, pname: int,
                              params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapParameterivNV(self, target: int, pname: int, params: Int1D,
                              params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapParameterfvNV(self, target: int, pname: int,
                              params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapParameterfvNV(self, target: int, pname: int, params: Float1D,
                              params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapAttribParameterivNV(self, target: int, index: int, pname: int,
                                    params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapAttribParameterivNV(self, target: int, index: int, pname: int,
                                    params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapAttribParameterfvNV(self, target: int, index: int, pname: int,
                                    params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMapAttribParameterfvNV(self, target: int, index: int, pname: int,
                                    params: Float1D,
                                    params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glEvalMapsNV(self, target: int, mode: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultisamplefvNV(self, pname: int, index: int,
                             val: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultisamplefvNV(self, pname: int, index: int, val: Float1D,
                             val_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glSampleMaskIndexedNV(self, index: int, mask: int) -> None:
        """
    
        """

    @staticmethod
    def glTexRenderbufferNV(self, target: int, renderbuffer: int) -> None:
        """
    
        """

    @staticmethod
    def glFragmentCoverageColorNV(self, color: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCoverageModulationTableNV(self, n: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCoverageModulationTableNV(self, n: int, v: Float1D,
                                    v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetCoverageModulationTableNV(self, bufsize: int,
                                       v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetCoverageModulationTableNV(self, bufsize: int, v: Float1D,
                                       v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glCoverageModulationNV(self, components: int) -> None:
        """
    
        """

    @staticmethod
    def glRenderbufferStorageMultisampleCoverageNV(self, target: int,
                                                   coverageSamples: int,
                                                   colorSamples: int,
                                                   internalformat: int,
                                                   width: int,
                                                   height: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramVertexLimitNV(self, target: int, limit: int) -> None:
        """
    
        """

    @staticmethod
    def glFramebufferTextureFaceEXT(self, target: int, attachment: int,
                                    texture: int, level: int,
                                    face: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramLocalParameterI4iNV(self, target: int, index: int, x: int,
                                     y: int, z: int, w: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParameterI4ivNV(self, target: int, index: int,
                                      params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParameterI4ivNV(self, target: int, index: int,
                                      params: Int1D,
                                      params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParametersI4ivNV(self, target: int, index: int,
                                       count: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParametersI4ivNV(self, target: int, index: int,
                                       count: int, params: Int1D,
                                       params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramLocalParameterI4uiNV(self, target: int, index: int, x: int,
                                      y: int, z: int, w: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParameterI4uivNV(self, target: int, index: int,
                                       params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParameterI4uivNV(self, target: int, index: int,
                                       params: Int1D,
                                       params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParametersI4uivNV(self, target: int, index: int,
                                        count: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramLocalParametersI4uivNV(self, target: int, index: int,
                                        count: int, params: Int1D,
                                        params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramEnvParameterI4iNV(self, target: int, index: int, x: int,
                                   y: int, z: int, w: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParameterI4ivNV(self, target: int, index: int,
                                    params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParameterI4ivNV(self, target: int, index: int,
                                    params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParametersI4ivNV(self, target: int, index: int, count: int,
                                     params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParametersI4ivNV(self, target: int, index: int, count: int,
                                     params: Int1D,
                                     params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramEnvParameterI4uiNV(self, target: int, index: int, x: int,
                                    y: int, z: int, w: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParameterI4uivNV(self, target: int, index: int,
                                     params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParameterI4uivNV(self, target: int, index: int,
                                     params: Int1D,
                                     params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParametersI4uivNV(self, target: int, index: int,
                                      count: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramEnvParametersI4uivNV(self, target: int, index: int,
                                      count: int, params: Int1D,
                                      params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramLocalParameterIivNV(self, target: int, index: int,
                                        params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramLocalParameterIivNV(self, target: int, index: int,
                                        params: Int1D,
                                        params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramLocalParameterIuivNV(self, target: int, index: int,
                                         params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramLocalParameterIuivNV(self, target: int, index: int,
                                         params: Int1D,
                                         params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramEnvParameterIivNV(self, target: int, index: int,
                                      params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramEnvParameterIivNV(self, target: int, index: int,
                                      params: Int1D,
                                      params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramEnvParameterIuivNV(self, target: int, index: int,
                                       params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramEnvParameterIuivNV(self, target: int, index: int,
                                       params: Int1D,
                                       params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramSubroutineParametersuivNV(self, target: int, count: int,
                                           params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramSubroutineParametersuivNV(self, target: int, count: int,
                                           params: Int1D,
                                           params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramSubroutineParameteruivNV(self, target: int, index: int,
                                             param: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramSubroutineParameteruivNV(self, target: int, index: int,
                                             param: Int1D,
                                             param_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertex2h(self, x: short, y: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex2hv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex2hv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertex3h(self, x: short, y: short, z: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex3hv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex3hv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertex4h(self, x: short, y: short, z: short, w: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex4hv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertex4hv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glNormal3h(self, nx: short, ny: short, nz: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormal3hv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNormal3hv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glColor3h(self, red: short, green: short, blue: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3hv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor3hv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glColor4h(self, red: short, green: short, blue: short,
                  alpha: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4hv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glColor4hv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord1h(self, s: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord1hv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord1hv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord2h(self, s: short, t: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord2hv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord2hv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord3h(self, s: short, t: short, r: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord3hv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord3hv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoord4h(self, s: short, t: short, r: short, q: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord4hv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexCoord4hv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord1h(self, target: int, s: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord1hv(self, target: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord1hv(self, target: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord2h(self, target: int, s: short, t: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord2hv(self, target: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord2hv(self, target: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord3h(self, target: int, s: short, t: short,
                          r: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord3hv(self, target: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord3hv(self, target: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord4h(self, target: int, s: short, t: short, r: short,
                          q: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord4hv(self, target: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiTexCoord4hv(self, target: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glFogCoordh(self, fog: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFogCoordhv(self, fog: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFogCoordhv(self, fog: Short1D, fog_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glSecondaryColor3h(self, red: short, green: short,
                           blue: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3hv(self, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSecondaryColor3hv(self, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexWeighth(self, weight: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexWeighthv(self, weight: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexWeighthv(self, weight: Short1D, weight_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib1h(self, index: int, x: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1hv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1hv(self, index: int, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib2h(self, index: int, x: short, y: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2hv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2hv(self, index: int, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib3h(self, index: int, x: short, y: short,
                         z: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3hv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3hv(self, index: int, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib4h(self, index: int, x: short, y: short, z: short,
                         w: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4hv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4hv(self, index: int, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribs1hv(self, index: int, n: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribs1hv(self, index: int, n: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribs2hv(self, index: int, n: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribs2hv(self, index: int, n: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribs3hv(self, index: int, n: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribs3hv(self, index: int, n: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribs4hv(self, index: int, n: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribs4hv(self, index: int, n: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenOcclusionQueriesNV(self, n: int, ids: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenOcclusionQueriesNV(self, n: int, ids: Int1D,
                                ids_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteOcclusionQueriesNV(self, n: int, ids: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteOcclusionQueriesNV(self, n: int, ids: Int1D,
                                   ids_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glIsOcclusionQueryNV(self, id: int) -> bool:
        """
    
        """

    @staticmethod
    def glBeginOcclusionQueryNV(self, id: int) -> None:
        """
    
        """

    @staticmethod
    def glEndOcclusionQueryNV(self) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetOcclusionQueryivNV(self, id: int, pname: int,
                                params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetOcclusionQueryivNV(self, id: int, pname: int, params: Int1D,
                                params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetOcclusionQueryuivNV(self, id: int, pname: int,
                                 params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetOcclusionQueryuivNV(self, id: int, pname: int, params: Int1D,
                                 params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramBufferParametersfvNV(self, target: int, bindingIndex: int,
                                      wordIndex: int, count: int,
                                      params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramBufferParametersfvNV(self, target: int, bindingIndex: int,
                                      wordIndex: int, count: int,
                                      params: Float1D,
                                      params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramBufferParametersIivNV(self, target: int, bindingIndex: int,
                                       wordIndex: int, count: int,
                                       params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramBufferParametersIivNV(self, target: int, bindingIndex: int,
                                       wordIndex: int, count: int,
                                       params: Int1D,
                                       params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramBufferParametersIuivNV(self, target: int, bindingIndex: int,
                                        wordIndex: int, count: int,
                                        params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramBufferParametersIuivNV(self, target: int, bindingIndex: int,
                                        wordIndex: int, count: int,
                                        params: Int1D,
                                        params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glPixelDataRangeNV(self, target: int, length: int,
                           pointer: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glFlushPixelDataRangeNV(self, target: int) -> None:
        """
    
        """

    @staticmethod
    def glPrimitiveRestartNV(self) -> None:
        """
    
        """

    @staticmethod
    def glPrimitiveRestartIndexNV(self, index: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFramebufferSampleLocationsfvNV(self, target: int, start: int,
                                         count: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFramebufferSampleLocationsfvNV(self, target: int, start: int,
                                         count: int, v: Float1D,
                                         v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedFramebufferSampleLocationsfvNV(self, framebuffer: int,
                                              start: int, count: int,
                                              v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glNamedFramebufferSampleLocationsfvNV(self, framebuffer: int,
                                              start: int, count: int,
                                              v: Float1D,
                                              v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glResolveDepthValuesNV(self) -> None:
        """
    
        """

    @staticmethod
    def glTextureBarrierNV(self) -> None:
        """
    
        """

    @staticmethod
    def glBindTransformFeedbackNV(self, target: int, id: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteTransformFeedbacksNV(self, n: int, ids: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteTransformFeedbacksNV(self, n: int, ids: Int1D,
                                     ids_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenTransformFeedbacksNV(self, n: int, ids: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenTransformFeedbacksNV(self, n: int, ids: Int1D,
                                  ids_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glIsTransformFeedbackNV(self, id: int) -> bool:
        """
    
        """

    @staticmethod
    def glPauseTransformFeedbackNV(self) -> None:
        """
    
        """

    @staticmethod
    def glResumeTransformFeedbackNV(self) -> None:
        """
    
        """

    @staticmethod
    def glDrawTransformFeedbackNV(self, mode: int, id: int) -> None:
        """
    
        """

    @staticmethod
    def glVDPAUInitNV(self, vdpDevice: Buffer, getProcAddress: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glVDPAUFiniNV(self) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVDPAURegisterVideoSurfaceNV(self, vdpSurface: Buffer, target: int,
                                      numTextureNames: int,
                                      textureNames: IntBuffer) -> long:
        """
    
        """

    @overload
    @staticmethod
    def glVDPAURegisterVideoSurfaceNV(self, vdpSurface: Buffer, target: int,
                                      numTextureNames: int,
                                      textureNames: Int1D,
                                      textureNames_offset: int) -> long:
        """
    
        """

    @overload
    @staticmethod
    def glVDPAURegisterOutputSurfaceNV(self, vdpSurface: Buffer, target: int,
                                       numTextureNames: int,
                                       textureNames: IntBuffer) -> long:
        """
    
        """

    @overload
    @staticmethod
    def glVDPAURegisterOutputSurfaceNV(self, vdpSurface: Buffer, target: int,
                                       numTextureNames: int,
                                       textureNames: Int1D,
                                       textureNames_offset: int) -> long:
        """
    
        """

    @staticmethod
    def glVDPAUIsSurfaceNV(self, surface: long) -> bool:
        """
    
        """

    @staticmethod
    def glVDPAUUnregisterSurfaceNV(self, surface: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVDPAUGetSurfaceivNV(self, surface: long, pname: int, bufSize: int,
                              length: IntBuffer, values: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVDPAUGetSurfaceivNV(self, surface: long, pname: int, bufSize: int,
                              length: Int1D, length_offset: int, values: Int1D,
                              values_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVDPAUSurfaceAccessNV(self, surface: long, access: int) -> None:
        """
    
        """

    @staticmethod
    def glVDPAUMapSurfacesNV(self, numSurfaces: int,
                             surfaces: PointerBuffer) -> None:
        """
    
        """

    @staticmethod
    def glVDPAUUnmapSurfacesNV(self, numSurface: int,
                               surfaces: PointerBuffer) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribL1i64NV(self, index: int, x: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribL2i64NV(self, index: int, x: long, y: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribL3i64NV(self, index: int, x: long, y: long,
                              z: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribL4i64NV(self, index: int, x: long, y: long, z: long,
                              w: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL1i64vNV(self, index: int, v: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL1i64vNV(self, index: int, v: Long1D,
                               v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL2i64vNV(self, index: int, v: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL2i64vNV(self, index: int, v: Long1D,
                               v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL3i64vNV(self, index: int, v: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL3i64vNV(self, index: int, v: Long1D,
                               v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL4i64vNV(self, index: int, v: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL4i64vNV(self, index: int, v: Long1D,
                               v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribL1ui64NV(self, index: int, x: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribL2ui64NV(self, index: int, x: long, y: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribL3ui64NV(self, index: int, x: long, y: long,
                               z: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribL4ui64NV(self, index: int, x: long, y: long, z: long,
                               w: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL1ui64vNV(self, index: int, v: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL1ui64vNV(self, index: int, v: Long1D,
                                v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL2ui64vNV(self, index: int, v: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL2ui64vNV(self, index: int, v: Long1D,
                                v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL3ui64vNV(self, index: int, v: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL3ui64vNV(self, index: int, v: Long1D,
                                v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL4ui64vNV(self, index: int, v: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL4ui64vNV(self, index: int, v: Long1D,
                                v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribLi64vNV(self, index: int, pname: int,
                                 params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribLi64vNV(self, index: int, pname: int, params: Long1D,
                                 params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribLui64vNV(self, index: int, pname: int,
                                  params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribLui64vNV(self, index: int, pname: int, params: Long1D,
                                  params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribLFormatNV(self, index: int, size: int, type: int,
                                stride: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI1iEXT(self, index: int, x: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI2iEXT(self, index: int, x: int, y: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI3iEXT(self, index: int, x: int, y: int, z: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI4iEXT(self, index: int, x: int, y: int, z: int,
                             w: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI1uiEXT(self, index: int, x: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI2uiEXT(self, index: int, x: int, y: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI3uiEXT(self, index: int, x: int, y: int,
                              z: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI4uiEXT(self, index: int, x: int, y: int, z: int,
                              w: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI1ivEXT(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI1ivEXT(self, index: int, v: Int1D,
                              v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI2ivEXT(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI2ivEXT(self, index: int, v: Int1D,
                              v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI3ivEXT(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI3ivEXT(self, index: int, v: Int1D,
                              v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4ivEXT(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4ivEXT(self, index: int, v: Int1D,
                              v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI1uivEXT(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI1uivEXT(self, index: int, v: Int1D,
                               v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI2uivEXT(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI2uivEXT(self, index: int, v: Int1D,
                               v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI3uivEXT(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI3uivEXT(self, index: int, v: Int1D,
                               v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4uivEXT(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4uivEXT(self, index: int, v: Int1D,
                               v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4bvEXT(self, index: int, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4bvEXT(self, index: int, v: Byte1D,
                              v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4svEXT(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4svEXT(self, index: int, v: Short1D,
                              v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4ubvEXT(self, index: int, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4ubvEXT(self, index: int, v: Byte1D,
                               v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4usvEXT(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4usvEXT(self, index: int, v: Short1D,
                               v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribIPointerEXT(self, index: int, size: int, type: int,
                                  stride: int, pointer: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribIivEXT(self, index: int, pname: int,
                                params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribIivEXT(self, index: int, pname: int, params: Int1D,
                                params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribIuivEXT(self, index: int, pname: int,
                                 params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribIuivEXT(self, index: int, pname: int, params: Int1D,
                                 params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glBeginVideoCaptureNV(self, video_capture_slot: int) -> None:
        """
    
        """

    @staticmethod
    def glBindVideoCaptureStreamBufferNV(self, video_capture_slot: int,
                                         stream: int, frame_region: int,
                                         offset: long) -> None:
        """
    
        """

    @staticmethod
    def glBindVideoCaptureStreamTextureNV(self, video_capture_slot: int,
                                          stream: int, frame_region: int,
                                          target: int, texture: int) -> None:
        """
    
        """

    @staticmethod
    def glEndVideoCaptureNV(self, video_capture_slot: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVideoCaptureivNV(self, video_capture_slot: int, pname: int,
                              params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVideoCaptureivNV(self, video_capture_slot: int, pname: int,
                              params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVideoCaptureStreamivNV(self, video_capture_slot: int, stream: int,
                                    pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVideoCaptureStreamivNV(self, video_capture_slot: int, stream: int,
                                    pname: int, params: Int1D,
                                    params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVideoCaptureStreamfvNV(self, video_capture_slot: int, stream: int,
                                    pname: int, params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVideoCaptureStreamfvNV(self, video_capture_slot: int, stream: int,
                                    pname: int, params: Float1D,
                                    params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVideoCaptureStreamdvNV(self, video_capture_slot: int, stream: int,
                                    pname: int, params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVideoCaptureStreamdvNV(self, video_capture_slot: int, stream: int,
                                    pname: int, params: Double1D,
                                    params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVideoCaptureNV(self, video_capture_slot: int,
                         sequence_num: IntBuffer,
                         capture_time: LongBuffer) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glVideoCaptureNV(self, video_capture_slot: int, sequence_num: Int1D,
                         sequence_num_offset: int, capture_time: Long1D,
                         capture_time_offset: int) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glVideoCaptureStreamParameterivNV(self, video_capture_slot: int,
                                          stream: int, pname: int,
                                          params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVideoCaptureStreamParameterivNV(self, video_capture_slot: int,
                                          stream: int, pname: int,
                                          params: Int1D,
                                          params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVideoCaptureStreamParameterfvNV(self, video_capture_slot: int,
                                          stream: int, pname: int,
                                          params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVideoCaptureStreamParameterfvNV(self, video_capture_slot: int,
                                          stream: int, pname: int,
                                          params: Float1D,
                                          params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVideoCaptureStreamParameterdvNV(self, video_capture_slot: int,
                                          stream: int, pname: int,
                                          params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVideoCaptureStreamParameterdvNV(self, video_capture_slot: int,
                                          stream: int, pname: int,
                                          params: Double1D,
                                          params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glFramebufferTextureMultiviewOVR(self, target: int, attachment: int,
                                         texture: int, level: int,
                                         baseViewIndex: int,
                                         numViews: int) -> None:
        """
    
        """

    @staticmethod
    def glHintPGI(self, target: int, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glFinishTextureSUNX(self) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribPointer(self, indx: int, size: int, type: int,
                              normalized: bool, stride: int,
                              ptr: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawElementsInstanced(self, mode: int, count: int, type: int,
                                indices: Buffer, instancecount: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawRangeElements(self, mode: int, start: int, end: int, count: int,
                            type: int, indices: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribIPointer(self, index: int, size: int, type: int,
                               stride: int, pointer: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glAlphaFunc(self, func: int, ref: float) -> None:
        """
    
        """

    @staticmethod
    def glFogf(self, pname: int, param: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFogfv(self, pname: int, params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glFogfv(self, pname: int, params: Float1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetLightfv(self, light: int, pname: int,
                     params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetLightfv(self, light: int, pname: int, params: Float1D,
                     params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMaterialfv(self, face: int, pname: int,
                        params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMaterialfv(self, face: int, pname: int, params: Float1D,
                        params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexEnvfv(self, tenv: int, pname: int,
                      params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexEnvfv(self, tenv: int, pname: int, params: Float1D,
                      params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glLightModelf(self, pname: int, param: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLightModelfv(self, pname: int, params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glLightModelfv(self, pname: int, params: Float1D,
                       params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glLightf(self, light: int, pname: int, param: float) -> None:
        """
    
        """

    @staticmethod
    def glMultiTexCoord4f(self, target: int, s: float, t: float, r: float,
                          q: float) -> None:
        """
    
        """

    @staticmethod
    def glNormal3f(self, nx: float, ny: float, nz: float) -> None:
        """
    
        """

    @staticmethod
    def glPointParameterf(self, pname: int, param: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPointParameterfv(self, pname: int, params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPointParameterfv(self, pname: int, params: Float1D,
                           params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glPointSize(self, size: float) -> None:
        """
    
        """

    @staticmethod
    def glTexEnvf(self, target: int, pname: int, param: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexEnvfv(self, target: int, pname: int, params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexEnvfv(self, target: int, pname: int, params: Float1D,
                   params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glClientActiveTexture(self, texture: int) -> None:
        """
    
        """

    @staticmethod
    def glColor4ub(self, red: byte, green: byte, blue: byte,
                   alpha: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexEnviv(self, tenv: int, pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexEnviv(self, tenv: int, pname: int, params: Int1D,
                      params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glLogicOp(self, opcode: int) -> None:
        """
    
        """

    @staticmethod
    def glTexEnvi(self, target: int, pname: int, param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexEnviv(self, target: int, pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexEnviv(self, target: int, pname: int, params: Int1D,
                   params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glOrtho(self, left: double, right: double, bottom: double, top: double,
                near_val: double, far_val: double) -> None:
        """
    
        """

    @staticmethod
    def glFrustum(self, left: double, right: double, bottom: double,
                  top: double, zNear: double, zFar: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawElements(self, mode: int, count: int, type: int,
                       indices: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glAttachShader(self, program: int, shader: int) -> None:
        """
    
        """

    @staticmethod
    def glBindAttribLocation(self, program: int, index: int,
                             name: String) -> None:
        """
    
        """

    @staticmethod
    def glBlendColor(self, red: float, green: float, blue: float,
                     alpha: float) -> None:
        """
    
        """

    @staticmethod
    def glCompileShader(self, shader: int) -> None:
        """
    
        """

    @staticmethod
    def glCreateProgram(self) -> int:
        """
    
        """

    @staticmethod
    def glCreateShader(self, type: int) -> int:
        """
    
        """

    @staticmethod
    def glDeleteProgram(self, program: int) -> None:
        """
    
        """

    @staticmethod
    def glDeleteShader(self, shader: int) -> None:
        """
    
        """

    @staticmethod
    def glDetachShader(self, program: int, shader: int) -> None:
        """
    
        """

    @staticmethod
    def glDisableVertexAttribArray(self, index: int) -> None:
        """
    
        """

    @staticmethod
    def glEnableVertexAttribArray(self, index: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveAttrib(self, program: int, index: int, bufSize: int,
                          length: IntBuffer, size: IntBuffer, type: IntBuffer,
                          name: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveAttrib(self, program: int, index: int, bufSize: int,
                          length: Int1D, length_offset: int, size: Int1D,
                          size_offset: int, type: Int1D, type_offset: int,
                          name: Byte1D, name_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveUniform(self, program: int, index: int, bufSize: int,
                           length: IntBuffer, size: IntBuffer, type: IntBuffer,
                           name: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveUniform(self, program: int, index: int, bufSize: int,
                           length: Int1D, length_offset: int, size: Int1D,
                           size_offset: int, type: Int1D, type_offset: int,
                           name: Byte1D, name_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetAttachedShaders(self, program: int, maxCount: int,
                             count: IntBuffer, shaders: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetAttachedShaders(self, program: int, maxCount: int, count: Int1D,
                             count_offset: int, shaders: Int1D,
                             shaders_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetAttribLocation(self, program: int, name: String) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramiv(self, program: int, pname: int,
                       params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramiv(self, program: int, pname: int, params: Int1D,
                       params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramInfoLog(self, program: int, bufSize: int,
                            length: IntBuffer, infoLog: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramInfoLog(self, program: int, bufSize: int, length: Int1D,
                            length_offset: int, infoLog: Byte1D,
                            infoLog_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetShaderiv(self, shader: int, pname: int,
                      params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetShaderiv(self, shader: int, pname: int, params: Int1D,
                      params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetShaderInfoLog(self, shader: int, bufSize: int, length: IntBuffer,
                           infoLog: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetShaderInfoLog(self, shader: int, bufSize: int, length: Int1D,
                           length_offset: int, infoLog: Byte1D,
                           infoLog_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetShaderSource(self, shader: int, bufSize: int, length: IntBuffer,
                          source: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetShaderSource(self, shader: int, bufSize: int, length: Int1D,
                          length_offset: int, source: Byte1D,
                          source_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformfv(self, program: int, location: int,
                       params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformfv(self, program: int, location: int, params: Float1D,
                       params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformiv(self, program: int, location: int,
                       params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformiv(self, program: int, location: int, params: Int1D,
                       params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetUniformLocation(self, program: int, name: String) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribfv(self, index: int, pname: int,
                            params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribfv(self, index: int, pname: int, params: Float1D,
                            params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribiv(self, index: int, pname: int,
                            params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribiv(self, index: int, pname: int, params: Int1D,
                            params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glIsProgram(self, program: int) -> bool:
        """
    
        """

    @staticmethod
    def glIsShader(self, shader: int) -> bool:
        """
    
        """

    @staticmethod
    def glLinkProgram(self, program: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glShaderSource(self, shader: int, count: int, string: String1D,
                       length: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glShaderSource(self, shader: int, count: int, string: String1D,
                       length: Int1D, length_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glStencilFuncSeparate(self, face: int, func: int, ref: int,
                              mask: int) -> None:
        """
    
        """

    @staticmethod
    def glStencilMaskSeparate(self, face: int, mask: int) -> None:
        """
    
        """

    @staticmethod
    def glStencilOpSeparate(self, face: int, sfail: int, dpfail: int,
                            dppass: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform1f(self, location: int, v0: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1fv(self, location: int, count: int,
                     value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1fv(self, location: int, count: int, value: Float1D,
                     value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform1i(self, location: int, v0: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1iv(self, location: int, count: int,
                     value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1iv(self, location: int, count: int, value: Int1D,
                     value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform2f(self, location: int, v0: float, v1: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2fv(self, location: int, count: int,
                     value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2fv(self, location: int, count: int, value: Float1D,
                     value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform2i(self, location: int, v0: int, v1: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2iv(self, location: int, count: int,
                     value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2iv(self, location: int, count: int, value: Int1D,
                     value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform3f(self, location: int, v0: float, v1: float,
                    v2: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3fv(self, location: int, count: int,
                     value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3fv(self, location: int, count: int, value: Float1D,
                     value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform3i(self, location: int, v0: int, v1: int, v2: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3iv(self, location: int, count: int,
                     value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3iv(self, location: int, count: int, value: Int1D,
                     value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform4f(self, location: int, v0: float, v1: float, v2: float,
                    v3: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4fv(self, location: int, count: int,
                     value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4fv(self, location: int, count: int, value: Float1D,
                     value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform4i(self, location: int, v0: int, v1: int, v2: int,
                    v3: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4iv(self, location: int, count: int,
                     value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4iv(self, location: int, count: int, value: Int1D,
                     value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix2fv(self, location: int, count: int, transpose: bool,
                           value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix2fv(self, location: int, count: int, transpose: bool,
                           value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix3fv(self, location: int, count: int, transpose: bool,
                           value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix3fv(self, location: int, count: int, transpose: bool,
                           value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix4fv(self, location: int, count: int, transpose: bool,
                           value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix4fv(self, location: int, count: int, transpose: bool,
                           value: Float1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUseProgram(self, program: int) -> None:
        """
    
        """

    @staticmethod
    def glValidateProgram(self, program: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib1f(self, index: int, x: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1fv(self, index: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1fv(self, index: int, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib2f(self, index: int, x: float, y: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2fv(self, index: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2fv(self, index: int, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib3f(self, index: int, x: float, y: float,
                         z: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3fv(self, index: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3fv(self, index: int, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib4f(self, index: int, x: float, y: float, z: float,
                         w: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4fv(self, index: int, v: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4fv(self, index: int, v: Float1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribPointer(self, index: int, size: int, type: int,
                              normalized: bool, stride: int,
                              pointer_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glTexImage2DMultisample(self, target: int, samples: int,
                                internalformat: int, width: int, height: int,
                                fixedsamplelocations: bool) -> None:
        """
    
        """

    @staticmethod
    def glTexImage3DMultisample(self, target: int, samples: int,
                                internalformat: int, width: int, height: int,
                                depth: int,
                                fixedsamplelocations: bool) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultisamplefv(self, pname: int, index: int,
                           val: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetMultisamplefv(self, pname: int, index: int, val: Float1D,
                           val_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glSampleMaski(self, index: int, mask: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDebugMessageControl(self, source: int, type: int, severity: int,
                              count: int, ids: IntBuffer,
                              enabled: bool) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDebugMessageControl(self, source: int, type: int, severity: int,
                              count: int, ids: Int1D, ids_offset: int,
                              enabled: bool) -> None:
        """
    
        """

    @staticmethod
    def glDebugMessageInsert(self, source: int, type: int, id: int,
                             severity: int, length: int, buf: String) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetDebugMessageLog(self, count: int, bufSize: int,
                             sources: IntBuffer, types: IntBuffer,
                             ids: IntBuffer, severities: IntBuffer,
                             lengths: IntBuffer,
                             messageLog: ByteBuffer) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glGetDebugMessageLog(self, count: int, bufSize: int, sources: Int1D,
                             sources_offset: int, types: Int1D,
                             types_offset: int, ids: Int1D, ids_offset: int,
                             severities: Int1D, severities_offset: int,
                             lengths: Int1D, lengths_offset: int,
                             messageLog: Byte1D,
                             messageLog_offset: int) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glPushDebugGroup(self, source: int, id: int, length: int,
                         message: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPushDebugGroup(self, source: int, id: int, length: int,
                         message: Byte1D, message_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glPopDebugGroup(self) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glObjectLabel(self, identifier: int, name: int, length: int,
                      label: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glObjectLabel(self, identifier: int, name: int, length: int,
                      label: Byte1D, label_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetObjectLabel(self, identifier: int, name: int, bufSize: int,
                         length: IntBuffer, label: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetObjectLabel(self, identifier: int, name: int, bufSize: int,
                         length: Int1D, length_offset: int, label: Byte1D,
                         label_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glObjectPtrLabel(self, ptr: Buffer, length: int,
                         label: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glObjectPtrLabel(self, ptr: Buffer, length: int, label: Byte1D,
                         label_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetObjectPtrLabel(self, ptr: Buffer, bufSize: int, length: IntBuffer,
                            label: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetObjectPtrLabel(self, ptr: Buffer, bufSize: int, length: Int1D,
                            length_offset: int, label: Byte1D,
                            label_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyImageSubData(self, srcName: int, srcTarget: int, srcLevel: int,
                           srcX: int, srcY: int, srcZ: int, dstName: int,
                           dstTarget: int, dstLevel: int, dstX: int, dstY: int,
                           dstZ: int, srcWidth: int, srcHeight: int,
                           srcDepth: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramBinary(self, program: int, bufSize: int, length: IntBuffer,
                           binaryFormat: IntBuffer, binary: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramBinary(self, program: int, bufSize: int, length: Int1D,
                           length_offset: int, binaryFormat: Int1D,
                           binaryFormat_offset: int, binary: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glProgramBinary(self, program: int, binaryFormat: int, binary: Buffer,
                        length: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexImage3D(self, target: int, level: int, internalformat: int,
                     width: int, height: int, depth: int, border: int,
                     format: int, type: int, pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexImage3D(self, target: int, level: int, internalformat: int,
                     width: int, height: int, depth: int, border: int,
                     format: int, type: int,
                     pixels_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexSubImage3D(self, target: int, level: int, xoffset: int,
                        yoffset: int, zoffset: int, width: int, height: int,
                        depth: int, format: int, type: int,
                        pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexSubImage3D(self, target: int, level: int, xoffset: int,
                        yoffset: int, zoffset: int, width: int, height: int,
                        depth: int, format: int, type: int,
                        pixels_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glCopyTexSubImage3D(self, target: int, level: int, xoffset: int,
                            yoffset: int, zoffset: int, x: int, y: int,
                            width: int, height: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCompressedTexImage3D(self, target: int, level: int,
                               internalformat: int, width: int, height: int,
                               depth: int, border: int, imageSize: int,
                               data: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCompressedTexImage3D(self, target: int, level: int,
                               internalformat: int, width: int, height: int,
                               depth: int, border: int, imageSize: int,
                               data_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCompressedTexSubImage3D(self, target: int, level: int, xoffset: int,
                                  yoffset: int, zoffset: int, width: int,
                                  height: int, depth: int, format: int,
                                  imageSize: int, data: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCompressedTexSubImage3D(self, target: int, level: int, xoffset: int,
                                  yoffset: int, zoffset: int, width: int,
                                  height: int, depth: int, format: int,
                                  imageSize: int,
                                  data_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glFramebufferTexture3D(self, target: int, attachment: int,
                               textarget: int, texture: int, level: int,
                               zoffset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexParameterIiv(self, target: int, pname: int,
                          params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexParameterIiv(self, target: int, pname: int, params: Int1D,
                          params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexParameterIuiv(self, target: int, pname: int,
                           params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexParameterIuiv(self, target: int, pname: int, params: Int1D,
                           params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexParameterIiv(self, target: int, pname: int,
                             params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexParameterIiv(self, target: int, pname: int, params: Int1D,
                             params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexParameterIuiv(self, target: int, pname: int,
                              params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexParameterIuiv(self, target: int, pname: int, params: Int1D,
                              params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSamplerParameterIiv(self, sampler: int, pname: int,
                              param: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSamplerParameterIiv(self, sampler: int, pname: int, param: Int1D,
                              param_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSamplerParameterIuiv(self, sampler: int, pname: int,
                               param: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSamplerParameterIuiv(self, sampler: int, pname: int, param: Int1D,
                               param_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetSamplerParameterIiv(self, sampler: int, pname: int,
                                 params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetSamplerParameterIiv(self, sampler: int, pname: int, params: Int1D,
                                 params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetSamplerParameterIuiv(self, sampler: int, pname: int,
                                  params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetSamplerParameterIuiv(self, sampler: int, pname: int,
                                  params: Int1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glDrawArraysInstancedBaseInstance(self, mode: int, first: int,
                                          count: int, instancecount: int,
                                          baseinstance: int) -> None:
        """
    
        """

    @staticmethod
    def glDrawElementsInstancedBaseInstance(self, mode: int, count: int,
                                            type: int,
                                            indices_buffer_offset: long,
                                            instancecount: int,
                                            baseinstance: int) -> None:
        """
    
        """

    @staticmethod
    def glDrawElementsInstancedBaseVertexBaseInstance(
            self, mode: int, count: int, type: int,
            indices_buffer_offset: long, instancecount: int, basevertex: int,
            baseinstance: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenQueries(self, n: int, ids: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenQueries(self, n: int, ids: Int1D, ids_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteQueries(self, n: int, ids: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteQueries(self, n: int, ids: Int1D, ids_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glIsQuery(self, id: int) -> bool:
        """
    
        """

    @staticmethod
    def glBeginQuery(self, target: int, id: int) -> None:
        """
    
        """

    @staticmethod
    def glEndQuery(self, target: int) -> None:
        """
    
        """

    @staticmethod
    def glQueryCounter(self, id: int, target: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryiv(self, target: int, pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryiv(self, target: int, pname: int, params: Int1D,
                     params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryObjectiv(self, id: int, pname: int,
                           params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryObjectiv(self, id: int, pname: int, params: Int1D,
                           params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryObjectuiv(self, id: int, pname: int,
                            params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryObjectuiv(self, id: int, pname: int, params: Int1D,
                            params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryObjecti64v(self, id: int, pname: int,
                             params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryObjecti64v(self, id: int, pname: int, params: Long1D,
                             params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryObjectui64v(self, id: int, pname: int,
                              params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryObjectui64v(self, id: int, pname: int, params: Long1D,
                              params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glActiveShaderProgram(self, pipeline: int, program: int) -> None:
        """
    
        """

    @staticmethod
    def glBindProgramPipeline(self, pipeline: int) -> None:
        """
    
        """

    @staticmethod
    def glCreateShaderProgramv(self, type: int, count: int,
                               strings: String1D) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteProgramPipelines(self, n: int, pipelines: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteProgramPipelines(self, n: int, pipelines: Int1D,
                                 pipelines_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenProgramPipelines(self, n: int, pipelines: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenProgramPipelines(self, n: int, pipelines: Int1D,
                              pipelines_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramPipelineInfoLog(self, pipeline: int, bufSize: int,
                                    length: IntBuffer,
                                    infoLog: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramPipelineInfoLog(self, pipeline: int, bufSize: int,
                                    length: Int1D, length_offset: int,
                                    infoLog: Byte1D,
                                    infoLog_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramPipelineiv(self, pipeline: int, pname: int,
                               params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetProgramPipelineiv(self, pipeline: int, pname: int, params: Int1D,
                               params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glIsProgramPipeline(self, pipeline: int) -> bool:
        """
    
        """

    @staticmethod
    def glProgramParameteri(self, program: int, pname: int,
                            value: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform1f(self, program: int, location: int,
                           v0: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1fv(self, program: int, location: int, count: int,
                            value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1fv(self, program: int, location: int, count: int,
                            value: Float1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform1i(self, program: int, location: int, v0: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1iv(self, program: int, location: int, count: int,
                            value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1iv(self, program: int, location: int, count: int,
                            value: Int1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform2f(self, program: int, location: int, v0: float,
                           v1: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2fv(self, program: int, location: int, count: int,
                            value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2fv(self, program: int, location: int, count: int,
                            value: Float1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform2i(self, program: int, location: int, v0: int,
                           v1: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2iv(self, program: int, location: int, count: int,
                            value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2iv(self, program: int, location: int, count: int,
                            value: Int1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform3f(self, program: int, location: int, v0: float,
                           v1: float, v2: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3fv(self, program: int, location: int, count: int,
                            value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3fv(self, program: int, location: int, count: int,
                            value: Float1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform3i(self, program: int, location: int, v0: int, v1: int,
                           v2: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3iv(self, program: int, location: int, count: int,
                            value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3iv(self, program: int, location: int, count: int,
                            value: Int1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform4f(self, program: int, location: int, v0: float,
                           v1: float, v2: float, v3: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4fv(self, program: int, location: int, count: int,
                            value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4fv(self, program: int, location: int, count: int,
                            value: Float1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform4i(self, program: int, location: int, v0: int, v1: int,
                           v2: int, v3: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4iv(self, program: int, location: int, count: int,
                            value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4iv(self, program: int, location: int, count: int,
                            value: Int1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2fv(self, program: int, location: int,
                                  count: int, transpose: bool,
                                  value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2fv(self, program: int, location: int,
                                  count: int, transpose: bool, value: Float1D,
                                  value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3fv(self, program: int, location: int,
                                  count: int, transpose: bool,
                                  value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3fv(self, program: int, location: int,
                                  count: int, transpose: bool, value: Float1D,
                                  value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4fv(self, program: int, location: int,
                                  count: int, transpose: bool,
                                  value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4fv(self, program: int, location: int,
                                  count: int, transpose: bool, value: Float1D,
                                  value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUseProgramStages(self, pipeline: int, stages: int,
                           program: int) -> None:
        """
    
        """

    @staticmethod
    def glValidateProgramPipeline(self, pipeline: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform1ui(self, program: int, location: int,
                            v0: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform2ui(self, program: int, location: int, v0: int,
                            v1: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform3ui(self, program: int, location: int, v0: int,
                            v1: int, v2: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform4ui(self, program: int, location: int, v0: int,
                            v1: int, v2: int, v3: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1uiv(self, program: int, location: int, count: int,
                             value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1uiv(self, program: int, location: int, count: int,
                             value: Int1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2uiv(self, program: int, location: int, count: int,
                             value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2uiv(self, program: int, location: int, count: int,
                             value: Int1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3uiv(self, program: int, location: int, count: int,
                             value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3uiv(self, program: int, location: int, count: int,
                             value: Int1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4uiv(self, program: int, location: int, count: int,
                             value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4uiv(self, program: int, location: int, count: int,
                             value: Int1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2x3fv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2x3fv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3x2fv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3x2fv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2x4fv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2x4fv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4x2fv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4x2fv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3x4fv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3x4fv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4x3fv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4x3fv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: Float1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glApplyFramebufferAttachmentCMAAINTEL(self) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawBuffers(self, n: int, bufs: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawBuffers(self, n: int, bufs: Int1D, bufs_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glReleaseShaderCompiler(self) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glShaderBinary(self, n: int, shaders: IntBuffer, binaryformat: int,
                       binary: Buffer, length: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glShaderBinary(self, n: int, shaders: Int1D, shaders_offset: int,
                       binaryformat: int, binary: Buffer, length: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetShaderPrecisionFormat(self, shadertype: int, precisiontype: int,
                                   range: IntBuffer,
                                   precision: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetShaderPrecisionFormat(self, shadertype: int, precisiontype: int,
                                   range: Int1D, range_offset: int,
                                   precision: Int1D,
                                   precision_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribPointer(self, array: GLArrayData) -> None:
        """
    
        """

    @staticmethod
    def glUniform(self, data: GLUniformData) -> None:
        """
    
        """

    @staticmethod
    def glReadBuffer(self, mode: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexLevelParameterfv(self, target: int, level: int, pname: int,
                                 params: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexLevelParameterfv(self, target: int, level: int, pname: int,
                                 params: Float1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexLevelParameteriv(self, target: int, level: int, pname: int,
                                 params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexLevelParameteriv(self, target: int, level: int, pname: int,
                                 params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawRangeElements(self, mode: int, start: int, end: int, count: int,
                            type: int, indices_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix2x3fv(self, location: int, count: int, transpose: bool,
                             value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix2x3fv(self, location: int, count: int, transpose: bool,
                             value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix3x2fv(self, location: int, count: int, transpose: bool,
                             value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix3x2fv(self, location: int, count: int, transpose: bool,
                             value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix2x4fv(self, location: int, count: int, transpose: bool,
                             value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix2x4fv(self, location: int, count: int, transpose: bool,
                             value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix4x2fv(self, location: int, count: int, transpose: bool,
                             value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix4x2fv(self, location: int, count: int, transpose: bool,
                             value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix3x4fv(self, location: int, count: int, transpose: bool,
                             value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix3x4fv(self, location: int, count: int, transpose: bool,
                             value: Float1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix4x3fv(self, location: int, count: int, transpose: bool,
                             value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformMatrix4x3fv(self, location: int, count: int, transpose: bool,
                             value: Float1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glColorMaski(self, index: int, r: bool, g: bool, b: bool,
                     a: bool) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetBooleani_v(self, target: int, index: int,
                        data: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetBooleani_v(self, target: int, index: int, data: Byte1D,
                        data_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetIntegeri_v(self, target: int, index: int,
                        data: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetIntegeri_v(self, target: int, index: int, data: Int1D,
                        data_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glEnablei(self, target: int, index: int) -> None:
        """
    
        """

    @staticmethod
    def glDisablei(self, target: int, index: int) -> None:
        """
    
        """

    @staticmethod
    def glIsEnabledi(self, target: int, index: int) -> bool:
        """
    
        """

    @staticmethod
    def glBeginTransformFeedback(self, primitiveMode: int) -> None:
        """
    
        """

    @staticmethod
    def glEndTransformFeedback(self) -> None:
        """
    
        """

    @staticmethod
    def glBindBufferRange(self, target: int, index: int, buffer: int,
                          offset: long, size: long) -> None:
        """
    
        """

    @staticmethod
    def glBindBufferBase(self, target: int, index: int, buffer: int) -> None:
        """
    
        """

    @staticmethod
    def glTransformFeedbackVaryings(self, program: int, count: int,
                                    varyings: String1D,
                                    bufferMode: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(self, program: int, index: int,
                                      bufSize: int, length: IntBuffer,
                                      size: IntBuffer, type: IntBuffer,
                                      name: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(self, program: int, index: int,
                                      bufSize: int, length: Int1D,
                                      length_offset: int, size: Int1D,
                                      size_offset: int, type: Int1D,
                                      type_offset: int, name: Byte1D,
                                      name_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glBeginConditionalRender(self, id: int, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glEndConditionalRender(self) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribIPointer(self, index: int, size: int, type: int,
                               stride: int,
                               pointer_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribIiv(self, index: int, pname: int,
                             params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribIiv(self, index: int, pname: int, params: Int1D,
                             params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribIuiv(self, index: int, pname: int,
                              params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribIuiv(self, index: int, pname: int, params: Int1D,
                              params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI4i(self, index: int, x: int, y: int, z: int,
                          w: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI4ui(self, index: int, x: int, y: int, z: int,
                           w: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4iv(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4iv(self, index: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4uiv(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4uiv(self, index: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformuiv(self, program: int, location: int,
                        params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformuiv(self, program: int, location: int, params: Int1D,
                        params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetFragDataLocation(self, program: int, name: String) -> int:
        """
    
        """

    @staticmethod
    def glUniform1ui(self, location: int, v0: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform2ui(self, location: int, v0: int, v1: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform3ui(self, location: int, v0: int, v1: int, v2: int) -> None:
        """
    
        """

    @staticmethod
    def glUniform4ui(self, location: int, v0: int, v1: int, v2: int,
                     v3: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1uiv(self, location: int, count: int,
                      value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform1uiv(self, location: int, count: int, value: Int1D,
                      value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2uiv(self, location: int, count: int,
                      value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform2uiv(self, location: int, count: int, value: Int1D,
                      value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3uiv(self, location: int, count: int,
                      value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform3uiv(self, location: int, count: int, value: Int1D,
                      value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4uiv(self, location: int, count: int,
                      value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniform4uiv(self, location: int, count: int, value: Int1D,
                      value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glClearBufferiv(self, buffer: int, drawbuffer: int,
                        value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glClearBufferiv(self, buffer: int, drawbuffer: int, value: Int1D,
                        value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glClearBufferuiv(self, buffer: int, drawbuffer: int,
                         value: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glClearBufferuiv(self, buffer: int, drawbuffer: int, value: Int1D,
                         value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glClearBufferfv(self, buffer: int, drawbuffer: int,
                        value: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glClearBufferfv(self, buffer: int, drawbuffer: int, value: Float1D,
                        value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glClearBufferfi(self, buffer: int, drawbuffer: int, depth: float,
                        stencil: int) -> None:
        """
    
        """

    @staticmethod
    def glGetStringi(self, name: int, index: int) -> String:
        """
    
        """

    @staticmethod
    def glBlitFramebuffer(self, srcX0: int, srcY0: int, srcX1: int, srcY1: int,
                          dstX0: int, dstY0: int, dstX1: int, dstY1: int,
                          mask: int, filter: int) -> None:
        """
    
        """

    @staticmethod
    def glFramebufferTextureLayer(self, target: int, attachment: int,
                                  texture: int, level: int,
                                  layer: int) -> None:
        """
    
        """

    @staticmethod
    def glBindVertexArray(self, array: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteVertexArrays(self, n: int, arrays: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteVertexArrays(self, n: int, arrays: Int1D,
                             arrays_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenVertexArrays(self, n: int, arrays: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenVertexArrays(self, n: int, arrays: Int1D,
                          arrays_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glIsVertexArray(self, array: int) -> bool:
        """
    
        """

    @staticmethod
    def glDrawArraysInstanced(self, mode: int, first: int, count: int,
                              instancecount: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDrawElementsInstanced(self, mode: int, count: int, type: int,
                                indices_buffer_offset: long,
                                instancecount: int) -> None:
        """
    
        """

    @staticmethod
    def glTexBuffer(self, target: int, internalformat: int,
                    buffer: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyBufferSubData(self, readTarget: int, writeTarget: int,
                            readOffset: long, writeOffset: long,
                            size: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformIndices(self, program: int, uniformCount: int,
                            uniformNames: String1D,
                            uniformIndices: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformIndices(self, program: int, uniformCount: int,
                            uniformNames: String1D, uniformIndices: Int1D,
                            uniformIndices_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveUniformsiv(self, program: int, uniformCount: int,
                              uniformIndices: IntBuffer, pname: int,
                              params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveUniformsiv(self, program: int, uniformCount: int,
                              uniformIndices: Int1D,
                              uniformIndices_offset: int, pname: int,
                              params: Int1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetUniformBlockIndex(self, program: int,
                               uniformBlockName: String) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveUniformBlockiv(self, program: int, uniformBlockIndex: int,
                                  pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveUniformBlockiv(self, program: int, uniformBlockIndex: int,
                                  pname: int, params: Int1D,
                                  params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveUniformBlockName(self, program: int, uniformBlockIndex: int,
                                    bufSize: int, length: IntBuffer,
                                    uniformBlockName: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveUniformBlockName(self, program: int, uniformBlockIndex: int,
                                    bufSize: int, length: Int1D,
                                    length_offset: int,
                                    uniformBlockName: Byte1D,
                                    uniformBlockName_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUniformBlockBinding(self, program: int, uniformBlockIndex: int,
                              uniformBlockBinding: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribDivisor(self, index: int, divisor: int) -> None:
        """
    
        """

    @staticmethod
    def glMinSampleShading(self, value: float) -> None:
        """
    
        """

    @staticmethod
    def glBlendEquationi(self, buf: int, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glBlendEquationSeparatei(self, buf: int, modeRGB: int,
                                 modeAlpha: int) -> None:
        """
    
        """

    @staticmethod
    def glBlendFunci(self, buf: int, src: int, dst: int) -> None:
        """
    
        """

    @staticmethod
    def glBlendFuncSeparatei(self, buf: int, srcRGB: int, dstRGB: int,
                             srcAlpha: int, dstAlpha: int) -> None:
        """
    
        """

    @staticmethod
    def glBindTransformFeedback(self, target: int, id: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteTransformFeedbacks(self, n: int, ids: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDeleteTransformFeedbacks(self, n: int, ids: Int1D,
                                   ids_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenTransformFeedbacks(self, n: int, ids: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGenTransformFeedbacks(self, n: int, ids: Int1D,
                                ids_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glIsTransformFeedback(self, id: int) -> bool:
        """
    
        """

    @staticmethod
    def glPauseTransformFeedback(self) -> None:
        """
    
        """

    @staticmethod
    def glResumeTransformFeedback(self) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetInternalformativ(self, target: int, internalformat: int,
                              pname: int, bufSize: int,
                              params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetInternalformativ(self, target: int, internalformat: int,
                              pname: int, bufSize: int, params: Int1D,
                              params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glBindImageTexture(self, unit: int, texture: int, level: int,
                           layered: bool, layer: int, access: int,
                           format: int) -> None:
        """
    
        """

    @staticmethod
    def glMemoryBarrier(self, barriers: int) -> None:
        """
    
        """

    @staticmethod
    def glFramebufferParameteri(self, target: int, pname: int,
                                param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFramebufferParameteriv(self, target: int, pname: int,
                                    params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetFramebufferParameteriv(self, target: int, pname: int,
                                    params: Int1D, params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glInvalidateFramebuffer(self, target: int, numAttachments: int,
                                attachments: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glInvalidateFramebuffer(self, target: int, numAttachments: int,
                                attachments: Int1D,
                                attachments_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glInvalidateSubFramebuffer(self, target: int, numAttachments: int,
                                   attachments: IntBuffer, x: int, y: int,
                                   width: int, height: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glInvalidateSubFramebuffer(self, target: int, numAttachments: int,
                                   attachments: Int1D, attachments_offset: int,
                                   x: int, y: int, width: int,
                                   height: int) -> None:
        """
    
        """

    @staticmethod
    def glTexStorage2DMultisample(self, target: int, samples: int,
                                  internalformat: int, width: int, height: int,
                                  fixedsamplelocations: bool) -> None:
        """
    
        """

    @staticmethod
    def glTexStorage3DMultisample(self, target: int, samples: int,
                                  internalformat: int, width: int, height: int,
                                  depth: int,
                                  fixedsamplelocations: bool) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnUniformuiv(self, program: int, location: int, bufSize: int,
                         params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnUniformuiv(self, program: int, location: int, bufSize: int,
                         params: Int1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glPrimitiveBoundingBox(self, minX: float, minY: float, minZ: float,
                               minW: float, maxX: float, maxY: float,
                               maxZ: float, maxW: float) -> None:
        """
    
        """

    @staticmethod
    def glFramebufferTextureEXT(self, target: int, attachment: int,
                                texture: int, level: int) -> None:
        """
    
        """

    @staticmethod
    def isPBOPackBound(self) -> bool:
        """
    
        """

    @staticmethod
    def isPBOUnpackBound(self) -> bool:
        """
    
        """

    @staticmethod
    def glPolygonMode(self, face: int, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glDrawBuffer(self, mode: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetDoublev(self, pname: int, params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetDoublev(self, pname: int, params: Double1D,
                     params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glPixelStoref(self, pname: int, param: float) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexImage1D(self, target: int, level: int, internalFormat: int,
                     width: int, border: int, format: int, type: int,
                     pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexImage1D(self, target: int, level: int, internalFormat: int,
                     width: int, border: int, format: int, type: int,
                     pixels_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexImage(self, target: int, level: int, format: int, type: int,
                      pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetTexImage(self, target: int, level: int, format: int, type: int,
                      pixels_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexSubImage1D(self, target: int, level: int, xoffset: int,
                        width: int, format: int, type: int,
                        pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glTexSubImage1D(self, target: int, level: int, xoffset: int,
                        width: int, format: int, type: int,
                        pixels_buffer_offset: long) -> None:
        """
    
        """

    @staticmethod
    def glCopyTexImage1D(self, target: int, level: int, internalformat: int,
                         x: int, y: int, width: int, border: int) -> None:
        """
    
        """

    @staticmethod
    def glCopyTexSubImage1D(self, target: int, level: int, xoffset: int,
                            x: int, y: int, width: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCompressedTexImage1D(self, target: int, level: int,
                               internalformat: int, width: int, border: int,
                               imageSize: int, data: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCompressedTexImage1D(self, target: int, level: int,
                               internalformat: int, width: int, border: int,
                               imageSize: int,
                               data_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCompressedTexSubImage1D(self, target: int, level: int, xoffset: int,
                                  width: int, format: int, imageSize: int,
                                  data: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glCompressedTexSubImage1D(self, target: int, level: int, xoffset: int,
                                  width: int, format: int, imageSize: int,
                                  data_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetCompressedTexImage(self, target: int, level: int,
                                img: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetCompressedTexImage(self, target: int, level: int,
                                img_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiDrawArrays(self, mode: int, first: IntBuffer, count: IntBuffer,
                          drawcount: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glMultiDrawArrays(self, mode: int, first: Int1D, first_offset: int,
                          count: Int1D, count_offset: int,
                          drawcount: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiDrawElements(self, mode: int, count: IntBuffer, type: int,
                            indices: PointerBuffer, drawcount: int) -> None:
        """
    
        """

    @staticmethod
    def glPointParameteri(self, pname: int, param: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPointParameteriv(self, pname: int, params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glPointParameteriv(self, pname: int, params: Int1D,
                           params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glGetBufferSubData(self, target: int, offset: long, size: long,
                           data: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribdv(self, index: int, pname: int,
                            params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribdv(self, index: int, pname: int, params: Double1D,
                            params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib1d(self, index: int, x: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1dv(self, index: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1dv(self, index: int, v: Double1D,
                          v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib1s(self, index: int, x: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1sv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib1sv(self, index: int, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib2d(self, index: int, x: double, y: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2dv(self, index: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2dv(self, index: int, v: Double1D,
                          v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib2s(self, index: int, x: short, y: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2sv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib2sv(self, index: int, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib3d(self, index: int, x: double, y: double,
                         z: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3dv(self, index: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3dv(self, index: int, v: Double1D,
                          v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib3s(self, index: int, x: short, y: short,
                         z: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3sv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib3sv(self, index: int, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4Nbv(self, index: int, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4Nbv(self, index: int, v: Byte1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4Niv(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4Niv(self, index: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4Nsv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4Nsv(self, index: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib4Nub(self, index: int, x: byte, y: byte, z: byte,
                           w: byte) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4Nubv(self, index: int, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4Nubv(self, index: int, v: Byte1D,
                            v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4Nuiv(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4Nuiv(self, index: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4Nusv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4Nusv(self, index: int, v: Short1D,
                            v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4bv(self, index: int, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4bv(self, index: int, v: Byte1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib4d(self, index: int, x: double, y: double, z: double,
                         w: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4dv(self, index: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4dv(self, index: int, v: Double1D,
                          v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4iv(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4iv(self, index: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttrib4s(self, index: int, x: short, y: short, z: short,
                         w: short) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4sv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4sv(self, index: int, v: Short1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4ubv(self, index: int, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4ubv(self, index: int, v: Byte1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4uiv(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4uiv(self, index: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4usv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttrib4usv(self, index: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glClampColor(self, target: int, clamp: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI1i(self, index: int, x: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI2i(self, index: int, x: int, y: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI3i(self, index: int, x: int, y: int, z: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI1ui(self, index: int, x: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI2ui(self, index: int, x: int, y: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribI3ui(self, index: int, x: int, y: int, z: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI1iv(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI1iv(self, index: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI2iv(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI2iv(self, index: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI3iv(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI3iv(self, index: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI1uiv(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI1uiv(self, index: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI2uiv(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI2uiv(self, index: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI3uiv(self, index: int, v: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI3uiv(self, index: int, v: Int1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4bv(self, index: int, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4bv(self, index: int, v: Byte1D, v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4sv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4sv(self, index: int, v: Short1D,
                           v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4ubv(self, index: int, v: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4ubv(self, index: int, v: Byte1D,
                            v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4usv(self, index: int, v: ShortBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribI4usv(self, index: int, v: Short1D,
                            v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glBindFragDataLocation(self, program: int, color: int,
                               name: String) -> None:
        """
    
        """

    @staticmethod
    def glFramebufferTexture1D(self, target: int, attachment: int,
                               textarget: int, texture: int,
                               level: int) -> None:
        """
    
        """

    @staticmethod
    def glPrimitiveRestartIndex(self, index: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveUniformName(self, program: int, uniformIndex: int,
                               bufSize: int, length: IntBuffer,
                               uniformName: ByteBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveUniformName(self, program: int, uniformIndex: int,
                               bufSize: int, length: Int1D, length_offset: int,
                               uniformName: Byte1D,
                               uniformName_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProvokingVertex(self, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glDrawTransformFeedback(self, mode: int, id: int) -> None:
        """
    
        """

    @staticmethod
    def glDrawTransformFeedbackStream(self, mode: int, id: int,
                                      stream: int) -> None:
        """
    
        """

    @staticmethod
    def glBeginQueryIndexed(self, target: int, index: int, id: int) -> None:
        """
    
        """

    @staticmethod
    def glEndQueryIndexed(self, target: int, index: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryIndexediv(self, target: int, index: int, pname: int,
                            params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetQueryIndexediv(self, target: int, index: int, pname: int,
                            params: Int1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform1d(self, program: int, location: int,
                           v0: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1dv(self, program: int, location: int, count: int,
                            value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform1dv(self, program: int, location: int, count: int,
                            value: Double1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform2d(self, program: int, location: int, v0: double,
                           v1: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2dv(self, program: int, location: int, count: int,
                            value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform2dv(self, program: int, location: int, count: int,
                            value: Double1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform3d(self, program: int, location: int, v0: double,
                           v1: double, v2: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3dv(self, program: int, location: int, count: int,
                            value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform3dv(self, program: int, location: int, count: int,
                            value: Double1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniform4d(self, program: int, location: int, v0: double,
                           v1: double, v2: double, v3: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4dv(self, program: int, location: int, count: int,
                            value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniform4dv(self, program: int, location: int, count: int,
                            value: Double1D, value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2dv(self, program: int, location: int,
                                  count: int, transpose: bool,
                                  value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2dv(self, program: int, location: int,
                                  count: int, transpose: bool, value: Double1D,
                                  value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3dv(self, program: int, location: int,
                                  count: int, transpose: bool,
                                  value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3dv(self, program: int, location: int,
                                  count: int, transpose: bool, value: Double1D,
                                  value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4dv(self, program: int, location: int,
                                  count: int, transpose: bool,
                                  value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4dv(self, program: int, location: int,
                                  count: int, transpose: bool, value: Double1D,
                                  value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2x3dv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2x3dv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: Double1D,
                                    value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3x2dv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3x2dv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: Double1D,
                                    value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2x4dv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix2x4dv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: Double1D,
                                    value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4x2dv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4x2dv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: Double1D,
                                    value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3x4dv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix3x4dv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: Double1D,
                                    value_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4x3dv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformMatrix4x3dv(self, program: int, location: int,
                                    count: int, transpose: bool,
                                    value: Double1D,
                                    value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribL1d(self, index: int, x: double) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribL2d(self, index: int, x: double, y: double) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribL3d(self, index: int, x: double, y: double,
                          z: double) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribL4d(self, index: int, x: double, y: double, z: double,
                          w: double) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL1dv(self, index: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL1dv(self, index: int, v: Double1D,
                           v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL2dv(self, index: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL2dv(self, index: int, v: Double1D,
                           v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL3dv(self, index: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL3dv(self, index: int, v: Double1D,
                           v_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL4dv(self, index: int, v: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glVertexAttribL4dv(self, index: int, v: Double1D,
                           v_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribLPointer(self, index: int, size: int, type: int,
                               stride: int,
                               pointer_buffer_offset: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribLdv(self, index: int, pname: int,
                             params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetVertexAttribLdv(self, index: int, pname: int, params: Double1D,
                             params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveAtomicCounterBufferiv(self, program: int, bufferIndex: int,
                                         pname: int,
                                         params: IntBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetActiveAtomicCounterBufferiv(self, program: int, bufferIndex: int,
                                         pname: int, params: Int1D,
                                         params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glClearBufferData(self, target: int, internalformat: int, format: int,
                          type: int, data: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glClearBufferSubData(self, target: int, internalformat: int,
                             offset: long, size: long, format: int, type: int,
                             data: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetInternalformati64v(self, target: int, internalformat: int,
                                pname: int, bufSize: int,
                                params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetInternalformati64v(self, target: int, internalformat: int,
                                pname: int, bufSize: int, params: Long1D,
                                params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glInvalidateTexSubImage(self, texture: int, level: int, xoffset: int,
                                yoffset: int, zoffset: int, width: int,
                                height: int, depth: int) -> None:
        """
    
        """

    @staticmethod
    def glInvalidateTexImage(self, texture: int, level: int) -> None:
        """
    
        """

    @staticmethod
    def glInvalidateBufferSubData(self, buffer: int, offset: long,
                                  length: long) -> None:
        """
    
        """

    @staticmethod
    def glInvalidateBufferData(self, buffer: int) -> None:
        """
    
        """

    @staticmethod
    def glGetnCompressedTexImage(self, target: int, lod: int, bufSize: int,
                                 pixels: Buffer) -> None:
        """
    
        """

    @staticmethod
    def glGetnTexImage(self, target: int, level: int, format: int, type: int,
                       bufSize: int, pixels: Buffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnUniformdv(self, program: int, location: int, bufSize: int,
                        params: DoubleBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetnUniformdv(self, program: int, location: int, bufSize: int,
                        params: Double1D, params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glBufferPageCommitmentARB(self, target: int, offset: long, size: long,
                                  commit: bool) -> None:
        """
    
        """

    @staticmethod
    def glNamedBufferPageCommitmentEXT(self, buffer: int, offset: long,
                                       size: long, commit: bool) -> None:
        """
    
        """

    @staticmethod
    def glNamedBufferPageCommitmentARB(self, buffer: int, offset: long,
                                       size: long, commit: bool) -> None:
        """
    
        """

    @staticmethod
    def glTexPageCommitmentARB(self, target: int, level: int, xoffset: int,
                               yoffset: int, zoffset: int, width: int,
                               height: int, depth: int, commit: bool) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDebugMessageEnableAMD(self, category: int, severity: int, count: int,
                                ids: IntBuffer, enabled: bool) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glDebugMessageEnableAMD(self, category: int, severity: int, count: int,
                                ids: Int1D, ids_offset: int,
                                enabled: bool) -> None:
        """
    
        """

    @staticmethod
    def glDebugMessageInsertAMD(self, category: int, severity: int, id: int,
                                length: int, buf: String) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetDebugMessageLogAMD(self, count: int, bufsize: int,
                                categories: IntBuffer, severities: IntBuffer,
                                ids: IntBuffer, lengths: IntBuffer,
                                message: ByteBuffer) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glGetDebugMessageLogAMD(self, count: int, bufsize: int,
                                categories: Int1D, categories_offset: int,
                                severities: Int1D, severities_offset: int,
                                ids: Int1D, ids_offset: int, lengths: Int1D,
                                lengths_offset: int, message: Byte1D,
                                message_offset: int) -> int:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformui64vNV(self, program: int, location: int,
                            params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetUniformui64vNV(self, program: int, location: int, params: Long1D,
                            params_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiDrawArraysIndirectAMD(self, mode: int, indirect: Buffer,
                                     primcount: int, stride: int) -> None:
        """
    
        """

    @staticmethod
    def glMultiDrawElementsIndirectAMD(self, mode: int, type: int,
                                       indirect: Buffer, primcount: int,
                                       stride: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSetMultisamplefvAMD(self, pname: int, index: int,
                              val: FloatBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glSetMultisamplefvAMD(self, pname: int, index: int, val: Float1D,
                              val_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glStencilOpValueAMD(self, face: int, value: int) -> None:
        """
    
        """

    @staticmethod
    def glTessellationFactorAMD(self, factor: float) -> None:
        """
    
        """

    @staticmethod
    def glTessellationModeAMD(self, mode: int) -> None:
        """
    
        """

    @staticmethod
    def glImportSyncEXT(self, external_sync_type: int, external_sync: long,
                        flags: int) -> long:
        """
    
        """

    @staticmethod
    def glMakeBufferResidentNV(self, target: int, access: int) -> None:
        """
    
        """

    @staticmethod
    def glMakeBufferNonResidentNV(self, target: int) -> None:
        """
    
        """

    @staticmethod
    def glIsBufferResidentNV(self, target: int) -> bool:
        """
    
        """

    @staticmethod
    def glMakeNamedBufferResidentNV(self, buffer: int, access: int) -> None:
        """
    
        """

    @staticmethod
    def glMakeNamedBufferNonResidentNV(self, buffer: int) -> None:
        """
    
        """

    @staticmethod
    def glIsNamedBufferResidentNV(self, buffer: int) -> bool:
        """
    
        """

    @overload
    @staticmethod
    def glGetBufferParameterui64vNV(self, target: int, pname: int,
                                    params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetBufferParameterui64vNV(self, target: int, pname: int,
                                    params: Long1D,
                                    params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedBufferParameterui64vNV(self, buffer: int, pname: int,
                                         params: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetNamedBufferParameterui64vNV(self, buffer: int, pname: int,
                                         params: Long1D,
                                         params_offset: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetIntegerui64vNV(self, value: int, result: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetIntegerui64vNV(self, value: int, result: Long1D,
                            result_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glUniformui64NV(self, location: int, value: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformui64vNV(self, location: int, count: int,
                         value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glUniformui64vNV(self, location: int, count: int, value: Long1D,
                         value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glProgramUniformui64NV(self, program: int, location: int,
                               value: long) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformui64vNV(self, program: int, location: int, count: int,
                                value: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glProgramUniformui64vNV(self, program: int, location: int, count: int,
                                value: Long1D, value_offset: int) -> None:
        """
    
        """

    @staticmethod
    def glTexImage2DMultisampleCoverageNV(self, target: int,
                                          coverageSamples: int,
                                          colorSamples: int,
                                          internalFormat: int, width: int,
                                          height: int,
                                          fixedSampleLocations: bool) -> None:
        """
    
        """

    @staticmethod
    def glTexImage3DMultisampleCoverageNV(self, target: int,
                                          coverageSamples: int,
                                          colorSamples: int,
                                          internalFormat: int, width: int,
                                          height: int, depth: int,
                                          fixedSampleLocations: bool) -> None:
        """
    
        """

    @staticmethod
    def glTextureImage2DMultisampleNV(self, texture: int, target: int,
                                      samples: int, internalFormat: int,
                                      width: int, height: int,
                                      fixedSampleLocations: bool) -> None:
        """
    
        """

    @staticmethod
    def glTextureImage3DMultisampleNV(self, texture: int, target: int,
                                      samples: int, internalFormat: int,
                                      width: int, height: int, depth: int,
                                      fixedSampleLocations: bool) -> None:
        """
    
        """

    @staticmethod
    def glTextureImage2DMultisampleCoverageNV(
            self, texture: int, target: int, coverageSamples: int,
            colorSamples: int, internalFormat: int, width: int, height: int,
            fixedSampleLocations: bool) -> None:
        """
    
        """

    @staticmethod
    def glTextureImage3DMultisampleCoverageNV(
            self, texture: int, target: int, coverageSamples: int,
            colorSamples: int, internalFormat: int, width: int, height: int,
            depth: int, fixedSampleLocations: bool) -> None:
        """
    
        """

    @staticmethod
    def glBufferAddressRangeNV(self, pname: int, index: int, address: long,
                               length: long) -> None:
        """
    
        """

    @staticmethod
    def glVertexFormatNV(self, size: int, type: int, stride: int) -> None:
        """
    
        """

    @staticmethod
    def glNormalFormatNV(self, type: int, stride: int) -> None:
        """
    
        """

    @staticmethod
    def glColorFormatNV(self, size: int, type: int, stride: int) -> None:
        """
    
        """

    @staticmethod
    def glIndexFormatNV(self, type: int, stride: int) -> None:
        """
    
        """

    @staticmethod
    def glTexCoordFormatNV(self, size: int, type: int, stride: int) -> None:
        """
    
        """

    @staticmethod
    def glEdgeFlagFormatNV(self, stride: int) -> None:
        """
    
        """

    @staticmethod
    def glSecondaryColorFormatNV(self, size: int, type: int,
                                 stride: int) -> None:
        """
    
        """

    @staticmethod
    def glFogCoordFormatNV(self, type: int, stride: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribFormatNV(self, index: int, size: int, type: int,
                               normalized: bool, stride: int) -> None:
        """
    
        """

    @staticmethod
    def glVertexAttribIFormatNV(self, index: int, size: int, type: int,
                                stride: int) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetIntegerui64i_vNV(self, value: int, index: int,
                              result: LongBuffer) -> None:
        """
    
        """

    @overload
    @staticmethod
    def glGetIntegerui64i_vNV(self, value: int, index: int, result: Long1D,
                              result_offset: int) -> None:
        """
    
        """

    @staticmethod
    def setSwapInterval(self, interval: int) -> None:
        """
    
        """
