/**
 * Copyright (c) 2021 Jintao Li. All rights reserved. University of Science and Technology of China
 * (USTC), Computational and Interpretation Group (CIG).
 * 
 * @author: Jintao Li
 * @version: 2024.02.20
 * 
 * @class: BasicArrayMethod (static)
 * @brief: A supplement (mean, std, concat, ...) of edu.mines.jtk.util.ArrayMath
 **/

package model;

import static edu.mines.jtk.util.ArrayMath.*;
import java.awt.Color;
import java.awt.image.IndexColorModel;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class BasicArrayMethod {

    /**
     * Concatenate two 3D arrays along an existing axis.
     * 
     * @param x 1st 3D array.
     * @param y 2st 3D array.
     * @param dim The axis along which the arrays will be joined. This param can be {0, 1, 2}, which
     *        means the arrays joined along {time, xline, inline} axis.
     */
    public static float[][][] concat(float[][][] x, float[][][] y, int dim) {
        if (dim == 0) { // time
            int n1 = x[0][0].length + y[0][0].length;
            int n2 = x[0].length;
            int n3 = x.length;
            float[][][] output = new float[n3][n2][n1];
            copy(x[0][0].length, n2, n3, 0, 0, 0, x, 0, 0, 0, output);
            copy(y[0][0].length, n2, n3, 0, 0, 0, y, x[0][0].length, 0, 0, output);
            return output;
        } else if (dim == 1) { // xline
            int n1 = x[0][0].length;
            int n2 = x[0].length + y[0].length;
            int n3 = x.length;
            float[][][] output = new float[n3][n2][n1];
            copy(n1, x[0].length, n3, 0, 0, 0, x, 0, 0, 0, output);
            copy(n1, y[0].length, n3, 0, 0, 0, y, 0, x[0].length, 0, output);
            return output;
        } else if (dim == 2) { // inline
            int n1 = x[0][0].length;
            int n2 = x[0].length;
            int n3 = x.length + y.length;
            float[][][] output = new float[n3][n2][n1];
            copy(n1, n2, x.length, 0, 0, 0, x, 0, 0, 0, output);
            copy(n1, n2, y.length, 0, 0, 0, y, 0, 0, x.length, output);
            return output;
        } else {
            return new float[1][1][1];
        }
    }

    public static float mean(float[][][] sx) {
        int n1 = sx[0][0].length;
        int n2 = sx[0].length;
        int n3 = sx.length;

        float m = 0;
        m = sum(sx);
        m = m / (n1 * n2 * n3);
        return m;
    }

    public static float mean(float[][] sx) {
        int n1 = sx[0].length;
        int n2 = sx.length;

        float m = sum(sx) / (n1 * n2);
        return m;
    }

    public static float mean(float[] sx) {
        int n = sx.length;
        float m = sum(sx) / n;
        return m;
    }

    public static float std(float[][][] sx) {
        int n1 = sx[0][0].length;
        int n2 = sx[0].length;
        int n3 = sx.length;

        float std = 0;
        std = sum(pow(sub(sx, mean(sx)), 2)) / (n1 * n2 * n3);
        return sqrt(std);
    }

    public static float std(float[][][] sx, int ddof) {
        int n1 = sx[0][0].length;
        int n2 = sx[0].length;
        int n3 = sx.length;

        float std = 0;
        std = sum(pow(sub(sx, mean(sx)), 2)) / (n1 * n2 * n3 - ddof);
        return sqrt(std);
    }

    public static float std(float[][] sx) {
        int n1 = sx[0].length;
        int n2 = sx.length;

        float std = 0;
        std = sum(pow(sub(sx, mean(sx)), 2)) / (n1 * n2);
        return sqrt(std);
    }

    public static float std(float[][] sx, int ddof) {
        int n1 = sx[0].length;
        int n2 = sx.length;

        float std = 0;
        std = sum(pow(sub(sx, mean(sx)), 2)) / (n1 * n2 - ddof);
        return sqrt(std);
    }

    public static float std(float[] sx) {
        int n = sx.length;

        float std = 0;
        std = sum(pow(sub(sx, mean(sx)), 2)) / n;
        return sqrt(std);
    }

    public static float std(float[] sx, int ddof) {
        int n = sx.length;

        float std = 0;
        std = sum(pow(sub(sx, mean(sx)), 2)) / (n - ddof);
        return sqrt(std);
    }

    /**
     * Get a time slice from a 3D volume.
     * 
     * @param gx The 3D volume.
     * @param index The index of time.
     */
    public static float[][] sliceOXX(float[][][] gx, int index) {
        int n3 = gx.length;
        int n2 = gx[0].length;
        float[][] output = new float[n3][n2];
        for (int i = 0; i < n3; i++) {
            for (int j = 0; j < n2; j++) {
                output[i][j] = gx[i][j][index];
            }
        }
        return output;
    }

    /**
     * Get a vertical slice from a 3D volume in the direction of inline, i.e. freeze the xline, take
     * a vertical slice.
     * 
     * @param gx The 3D volume.
     * @param index The index of xline.
     */
    public static float[][] sliceXOX(float[][][] gx, int index) {
        int n3 = gx.length;
        int n1 = gx[0][0].length;
        float[][] output = new float[n3][n1];
        for (int i = 0; i < n3; i++) {
            for (int j = 0; j < n1; j++) {
                output[i][j] = gx[i][index][j];
            }
        }
        return output;
    }

    /**
     * Get a vertical slice from a 3D volume in the direction of xline, i.e. freeze the inline, take
     * a vertical slice.
     * 
     * @param gx The 3D volume.
     * @param index The index of inline.
     */
    public static float[][] sliceXXO(float[][][] gx, int index) {
        int n2 = gx[0].length;
        int n1 = gx[0][0].length;
        float[][] output = new float[n2][n1];
        for (int i = 0; i < n2; i++) {
            for (int j = 0; j < n1; j++) {
                output[i][j] = gx[index][i][j];
            }
        }
        return output;
    }

    /**
     * Get a trace from a 3D volume.
     * 
     * @param gx The 3D volume
     * @param xl The index of xline
     * @param inl The index of inline
     */
    public static float[] trace(float[][][] gx, int xl, int inl) {
        return gx[inl][xl];
    }

    /**
     * Get a trace from a 2D vertical slice.
     * 
     * @param gx The 2D vertical slice
     * @param idx The index
     */
    public static float[] trace(float[][] gx, int idx) {
        return gx[idx];
    }

    /**
     * Get a horiontal line from a 2D vertical slice.
     * 
     * @param gx The 2D vertical slice
     * @param idx The index
     */
    public static float[] traceh(float[][] gx, int idx) {
        int n3 = gx.length;
        int n2 = gx[0].length;

        float[] out = zerofloat(n3);
        for (int i3 = 0; i3 < n3; ++i3) {
            out[i3] = gx[i3][idx];
        }

        return out;
    }
    public static double[] traceh(double[][] gx, int idx) {
        int n3 = gx.length;
        int n2 = gx[0].length;

        double[] out = zerodouble(n3);
        for (int i3 = 0; i3 < n3; ++i3) {
            out[i3] = gx[i3][idx];
        }

        return out;
    }

    public static float[][] rot90(float[][] gx) {
        // rotate 90 degrees
        int n3 = gx.length;
        int n2 = gx[0].length;
        float[][] out = zerofloat(n3, n2);

        for (int i3 = 0; i3 < n3; ++i3) {
            for (int i2 = 0; i2 < n2; ++i2) {
                out[i2][n3 - i3 - 1] = gx[i3][i2];
            }
        }
        return out;
    }

    public static float[][] rot90(float[][] gx, int times) {
        // rotate 90*times degrees
        assert times > 0 : "times must > 0";
        times = (times - 1) % 4;

        int n3 = gx.length;
        int n2 = gx[0].length;
        float[][] out = zerofloat(n3, n2);

        for (int i = 0; i <= times; ++i) {
            if (i % 2 == 0) {
                out = rot90(gx);
            } else {
                gx = rot90(out);
            }
        }

        return (times % 2 == 0) ? out : gx;
    }

    public static float[][] fliplr(float[][] gx) {
        // Flip array in the left/right direction.
        int n3 = gx.length;
        int n2 = gx[0].length;
        float[][] out = zerofloat(n2, n3);

        for (int i3 = 0; i3 < n3; ++i3) {
            for (int i2 = 0; i2 < n2; ++i2) {
                out[i3][i2] = gx[i3][n2 - i2 - 1];
            }
        }
        return out;
    }

    public static float[][] flipud(float[][] gx) {
        // Flip array in the up/down direction.
        int n3 = gx.length;
        int n2 = gx[0].length;
        float[][] out = zerofloat(n2, n3);

        for (int i3 = 0; i3 < n3; ++i3) {
            for (int i2 = 0; i2 < n2; ++i2) {
                out[i3][i2] = gx[n3 - i3 - 1][i2];
            }
        }
        return out;
    }

    public static float[][][] flip(float[][][] gx, int dim) {
        int n3 = gx.length;
        int n2 = gx[0].length;
        int n1 = gx[0][0].length;
        float[][][] out = zerofloat(n1, n2, n3);

        if (0 == dim) {
            for (int i3 = 0; i3 < n3; ++i3) {
                out[i3] = fliplr(gx[i3]);
            }
        } else if (1 == dim) {
            for (int i3 = 0; i3 < n3; ++i3) {
                out[i3] = flipud(gx[i3]);
            }
        } else if (2 == dim) {
            for (int i1 = 0; i1 < n1; ++i1) {
                for (int i2 = 0; i2 < n2; ++i2) {
                    for (int i3 = 0; i3 < n3; ++i3) {
                        out[i3][i2][i1] = gx[n3 - i3 - 1][i2][i1];
                    }
                }
            }
        } else {
            return new float[1][1][1];
        }

        return out;
    }

    public static float[][][] expend_dims(float[][] gx, int dim) {
        int n1 = gx.length;
        int n2 = gx[0].length;

        if (dim == 0) {
            float[][][] out = zerofloat(n2, n1, 1);
            out[0] = gx;
            return out;
        } else {
            return new float[1][1][1];
        }

    }

    /**
     * downsample function
     * 
     * @param gx float array
     * @param step int, interval
     * @param start int array, start index
     */
    public static float[] downsample(float[] gx, int step, int start[]) {
        int n1 = gx.length;

        int nn1 = (n1 - start[0] + step - 1) / step;

        float[] out = zerofloat(nn1);

        for (int i = 0; i < nn1; i++) {
            out[i] = gx[start[0] + i * step];
        }

        return out;
    }

    public static float[] downsample(float[] gx, int step) {
        int[] start = zeroint(1);
        return downsample(gx, step, start);
    }

    public static float[] downsample(float[] gx) {
        return downsample(gx, 2);
    }

    public static float[][] downsample(float[][] gx, int step, int start[]) {
        int n2 = gx.length;
        int n1 = gx[0].length;

        int nn2 = (n2 - start[1] + step - 1) / step;
        int nn1 = (n1 - start[0] + step - 1) / step;
        float[][] out = zerofloat(nn1, nn2);

        for (int j = 0; j < nn2; j++) {
            for (int i = 0; i < nn1; i++) {
                out[j][i] = gx[start[1] + j * step][start[0] + i * step];
            }
        }

        return out;
    }

    public static float[][] downsample(float[][] gx, int step) {
        int[] start = zeroint(2);
        return downsample(gx, step, start);
    }

    public static float[][] downsample(float[][] gx) {
        return downsample(gx, 2);
    }

    public static float[][][] downsample(float[][][] gx, int step, int start[]) {
        int n3 = gx.length;
        int n2 = gx[0].length;
        int n1 = gx[0][0].length;

        int nn1 = (n1 - start[0] + step - 1) / step;
        int nn2 = (n2 - start[1] + step - 1) / step;
        int nn3 = (n3 - start[2] + step - 1) / step;

        float[][][] out = zerofloat(nn1, nn2, nn3);

        for (int k = 0; k < nn3; k++) {
            for (int j = 0; j < nn2; j++) {
                for (int i = 0; i < nn1; i++) {
                    out[k][j][i] =
                            gx[start[2] + k * step][start[1] + j * step][start[0] + i * step];
                }
            }
        }

        return out;
    }

    public static float[][][] downsample(float[][][] gx, int step) {
        int[] start = zeroint(3);
        return downsample(gx, step, start);
    }

    public static float[][][] downsample(float[][][] gx) {
        return downsample(gx, 2);
    }

    /**
     * Get shape function
     * 
     * @param gx src, float array
     */
    public static int[] shape(float[] gx) {
        int[] dim = zeroint(1);
        dim[0] = gx.length;

        return dim;
    }

    public static int[] shape(float[][] gx) {
        int[] dim = zeroint(2);
        dim[0] = gx[0].length;
        dim[1] = gx.length;

        return dim;
    }

    public static int[] shape(float[][][] gx) {
        int[] dim = zeroint(3);
        dim[0] = gx[0][0].length;
        dim[1] = gx[0].length;
        dim[2] = gx.length;

        return dim;
    }

    /**
     * Transpose the specified 3-D array.
     * 
     * @param rx the array; must be regular.
     * @return the transposed array.
     */
    public static float[][][] transpose(float[][][] rx) {
        int n3 = rx.length;
        int n2 = rx[0].length;
        int n1 = rx[0][0].length;
        float[][][] ry = new float[n1][n2][n3];
        for (int i3 = 0; i3 < n3; ++i3) {
            for (int i2 = 0; i2 < n2; ++i2) {
                for (int i1 = 0; i1 < n1; ++i1) {
                    ry[i1][i2][i3] = rx[i3][i2][i1];
                }
            }
        }
        return ry;
    }

    /**
     * Transpose the specified 2-D array.
     * 
     * @param rx the array; must be regular.
     * @return the transposed array.
     */    
    public static float[][] transpose(float[][] rx) {
        int n2 = rx.length;
        int n1 = rx[0].length;
        float[][] ry = new float[n1][n2];
        for (int i2 = 0; i2 < n2; ++i2) {
            for (int i1 = 0; i1 < n1; ++i1) {
                ry[i1][i2] = rx[i2][i1];
            }
        }
        return ry;
    }

    public static float[] zerofloat_like(float[] x) {
        return zerofloat(x.length);
    }
    public static float[] zerofloat_like(double[] x) {
        return zerofloat(x.length);
    }
    public static float[] zerofloat_like(int[] x) {
        return zerofloat(x.length);
    }
    public static float[][] zerofloat_like(float[][] x) {
        return zerofloat(x[0].length, x.length);
    }
    public static float[][] zerofloat_like(double[][] x) {
        return zerofloat(x[0].length, x.length);
    }
    public static float[][] zerofloat_like(int[][] x) {
        return zerofloat(x[0].length, x.length);
    }
    public static float[][][] zerofloat_like(float[][][] x) {
        return zerofloat(x[0][0].length, x[0].length, x.length);
    }
    public static float[][][] zerofloat_like(double[][][] x) {
        return zerofloat(x[0][0].length, x[0].length, x.length);
    }
    public static float[][][] zerofloat_like(int[][][] x) {
        return zerofloat(x[0][0].length, x[0].length, x.length);
    }

    public static double[] zerodouble_like(double[] x) {
        return zerodouble(x.length);
    }
    public static double[] zerodouble_like(float[] x) {
        return zerodouble(x.length);
    }
    public static double[] zerodouble_like(int[] x) {
        return zerodouble(x.length);
    }
    public static double[][] zerodouble_like(double[][] x) {
        return zerodouble(x[0].length, x.length);
    }
    public static double[][] zerodouble_like(float[][] x) {
        return zerodouble(x[0].length, x.length);
    }
    public static double[][] zerodouble_like(int[][] x) {
        return zerodouble(x[0].length, x.length);
    }
    public static double[][][] zerodouble_like(double[][][] x) {
        return zerodouble(x[0][0].length, x[0].length, x.length);
    }
    public static double[][][] zerodouble_like(float[][][] x) {
        return zerodouble(x[0][0].length, x[0].length, x.length);
    }
    public static double[][][] zerodouble_like(int[][][] x) {
        return zerodouble(x[0][0].length, x[0].length, x.length);
    }


    public static int[] zeroint_like(int[] x) {
        return zeroint(x.length);
    }
    public static int[] zeroint_like(float[] x) {
        return zeroint(x.length);
    }
    public static int[] zeroint_like(double[] x) {
        return zeroint(x.length);
    }
    public static int[][] zeroint_like(int[][] x) {
        return zeroint(x[0].length, x.length);
    }
    public static int[][] zeroint_like(float[][] x) {
        return zeroint(x[0].length, x.length);
    }
    public static int[][] zeroint_like(double[][] x) {
        return zeroint(x[0].length, x.length);
    }
    public static int[][][] zeroint_like(int[][][] x) {
        return zeroint(x[0][0].length, x[0].length, x.length);
    }
    public static int[][][] zeroint_like(float[][][] x) {
        return zeroint(x[0][0].length, x[0].length, x.length);
    }
    public static int[][][] zeroint_like(double[][][] x) {
        return zeroint(x[0][0].length, x[0].length, x.length);
    }

    public static double[] float2double(float[] x) {
        double[] out = zerodouble_like(x);
        for (int i = 0; i < x.length; i++) {
            out[i] = x[i];
        }
        return out;
    }
    public static double[][] float2double(float[][] x) {
        double[][] out = zerodouble_like(x);
        for (int i = 0; i < x.length; i++) {
            for (int j = 0; j < x[0].length; j++) {
                out[i][j] = x[i][j];
            }
        }
        return out;
    }
    public static double[][][] float2double(float[][][] x) {
        double[][][] out = zerodouble_like(x);
        for (int i = 0; i < x.length; i++) {
            for (int j = 0; j < x[0].length; j++) {
                for (int k = 0; k < x[0][0].length; k++) {
                    out[i][j][k] = x[i][j][k];
                }
            }
        }
        return out;
    }

    public static float[] double2float(double[] x) {
        float[] out = zerofloat_like(x);
        for (int i = 0; i < x.length; i++) {
            out[i] = (float)x[i];
        }
        return out;
    }
    public static float[][] double2float(double[][] x) {
        float[][] out = zerofloat_like(x);
        for (int i = 0; i < x.length; i++) {
            for (int j = 0; j < x[0].length; j++) {
                out[i][j] = (float)x[i][j];
            }
        }
        return out;
    }
    public static float[][][] double2float(double[][][] x) {
        float[][][] out = zerofloat_like(x);
        for (int i = 0; i < x.length; i++) {
            for (int j = 0; j < x[0].length; j++) {
                for (int k = 0; k < x[0][0].length; k++) {
                    out[i][j][k] = (float)x[i][j][k];
                }
            }
        }
        return out;
    }


    public static double[][] readTxtArray(String fname, int skip, String delimiter) {
        ArrayList<double[]> dataList = new ArrayList<>();

        try {
            File file = new File(fname);
            Scanner scanner = new Scanner(file);

            // 跳过指定数量的行
            for (int i = 0; i < skip; i++) {
                if (scanner.hasNextLine()) {
                    scanner.nextLine();
                }
            }

            // 读取文件剩余部分
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                // 使用指定的分隔符分割每行，去除多余的空格，并转换为float
                String[] items = line.split(delimiter + "\\s*");
                double[] floatItems = new double[items.length];
                for (int i = 0; i < items.length; i++) {
                    floatItems[i] = Float.parseFloat(items[i].trim());
                }
                dataList.add(floatItems);
            }

            scanner.close();
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.err.println("Error parsing number: " + e.getMessage());
        }

        // 转换ArrayList<float[]>为float[][]
        double[][] dataArray = new double[dataList.size()][];
        for (int i = 0; i < dataList.size(); i++) {
            dataArray[i] = dataList.get(i);
        }

        return dataArray;
    }

    public static double[][] readTxtArray(String fname, int skip) {
        return readTxtArray(fname, skip, " ");
    }

    public static double[][] readTxtArray(String fname) {
        return readTxtArray(fname, 0, " ");
    }

}
