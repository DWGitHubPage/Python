# Python3.7.3

import numpy as np 
import matplotlib.pyplot as plt

  
def estimate_coeff(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    mean_x, mean_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*mean_y*mean_x 
    SS_xx = np.sum(x*x) - n*mean_x*mean_x 
  
    # calculating regression coefficients 
    a_1 = SS_xy / SS_xx 
    a_0 = mean_y - a_1*mean_x 
  
    return(a_0, a_1) 
  
def plot_regression_line(x, y, a): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "purple", 
               marker = "o", s = 100) 
  
    # predicted response vector 
    y_predict = a[0] + a[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_predict, color = "orange") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show()
    
  
def main(): 
    # observations 
    x = np.array([9, 6, 3, 16, 15, 12.5, 9, 2]) 
    y = np.array([9, 6, 3, 16, 15, 12.5, 9, 2])
  
    # estimating coefficients 
    b = estimate_coeff(x, y) 
    print("Estimated coefficients:\nb_0 = {}  \
\nb_1 = {}".format(b[0], b[1])) 
  
    # plotting regression line 
    plot_regression_line(x, y, b) 
  
if __name__ == "__main__": 
    main() 
