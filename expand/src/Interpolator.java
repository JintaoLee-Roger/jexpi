/**
 * Copyright (c) 2024 Jintao Li. All rights reserved. University of Science and Technology of China
 * (USTC), Computational and Interpretation Group (CIG).
 * 
 * @author: Jintao Li
 * @version: 2024.2.19
 * 
 * @class: Interpolator
 * @brief: Linear Interpolator for **nonuniform** sampling
 **/

package model;

import edu.mines.jtk.dsp.*;
import static edu.mines.jtk.util.ArrayMath.*;

public class Interpolator { 

  public Interpolator(double[] x, double[] y) {
    _x = x;
    _y = y;
    _n = y.length;
    // _is_uniform = false;
  }

  public Interpolator(double[] y) {
    _n = y.length;
    // _is_uniform = true;
    // Sampling _s = new Sampling(_n, 1.0, 0.0);
    _x = new Sampling(_n, 1.0, 0.0).getValues();
    _y = y;
  }

  public Interpolator(double d, double f, double[] y) {
    _n = y.length;
    // _is_uniform = true;
    // Sampling _s = new Sampling(_n, d, f);
    _x = new Sampling(_n, d, f).getValues();
    _y = y;
  }

  public double interpolate(double xnew) {
    int i = findNearestIndex(xnew);
    if (i == -1)
        return _y[0];
    else if ( i == -2)
        return _y[_n - 1];
    else
        return interpolate(_x[i], _y[i], _x[i+1], _y[i+1], xnew);
  }

  public double[] interpolate(double[] xnew) {
    int N = xnew.length;
    double[] out = zerodouble(N);
    for (int j = 0; j < N; ++j) {
        int i = findNearestIndex(xnew[j]);
        if (i == -1)
            out[j] = _y[0];
        else if (i == -2)
            out[j] = _y[_n - 1];
        else
            out[j] = interpolate(_x[i], _y[i], _x[i+1], _y[i+1], xnew[j]);
    }

    return out;
  }

  public int findNearestIndex(double xnew) {
    int i = 0;
    if (xnew < _x[0]) return -1;

    for (; i < _n - 1; ++i) {
      if (_x[i] <= xnew && xnew <= _x[i+1]) 
        break;
    }

    if (i == _n - 1) return -2;

    return i;
  }

  /* private */
  private double[] _x;
  private double[] _y;
//   private Sampling _s;
//   private boolean _is_uniform;
  private int _n;

  private static double interpolate(
    double x0, double y0, double x1, double y1, double x) 
  {
    if (x1 == x0) return y0; // 防止除以0
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0);
  }
}
