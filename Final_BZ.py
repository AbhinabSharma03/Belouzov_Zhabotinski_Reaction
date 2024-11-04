import numpy as np
import matplotlib.pyplot as plt

# Defining the system of equations
def x_prime(x, y, a):
    return a - x - (4 * x * y) / (1 + x**2)

def y_prime(x, y, b):
    return b * x * (1 - y / (1 + x**2))

# Runge-Kutta 4th Order Solver
def rk_4(x0, y0, a, b, h, t_max):

    steps = int(t_max / h) # Number of steps
    x_values = np.zeros(steps + 1)
    y_values = np.zeros(steps + 1)
    t_values = np.linspace(0, t_max, steps + 1)
    
    # Initial conditions
    x_values[0] = x0
    y_values[0] = y0
    
    for n in range(steps):
        # x calculations
        kx_1 = h * x_prime(x_values[n], y_values[n], a)
        kx_2 = h * x_prime(x_values[n] + kx_1 / 2, y_values[n] + h / 2, a)
        kx_3 = h * x_prime(x_values[n] + kx_2 / 2, y_values[n] + h / 2, a)
        kx_4 = h * x_prime(x_values[n] + kx_3, y_values[n] + h, a)
        
        # y calculations
        ky_1 = h * y_prime(x_values[n], y_values[n], b)
        ky_2 = h * y_prime(x_values[n] + h / 2, y_values[n] + ky_1 / 2, b)
        ky_3 = h * y_prime(x_values[n] + h / 2, y_values[n] + ky_2 / 2, b)
        ky_4 = h * y_prime(x_values[n] + h, y_values[n] + ky_3, b)
        
        # Update x and y values
        x_values[n + 1] = x_values[n] + (1/6) * (kx_1 + 2 * kx_2 + 2 * kx_3 + kx_4)
        y_values[n + 1] = y_values[n] + (1/6) * (ky_1 + 2 * ky_2 + 2 * ky_3 + ky_4)
    
    return x_values, y_values, t_values

# Parameters for the BZ reaction
h = 0.01 # Time step
t_max = 10 # Maximum time

##################################
Oscillations = True # True If you want to see the osciallatory behavior with the specified value.
##################################

if Oscillations:
    #a and b values for the oscillating case found out from lots and lots of hit and trials
    a = 1000
    b = 652
    
    # Fixed points
    x0 = a / 5
    y0 = 1 + (a**2) / 25
    
    # Run the RK4 solver
    x_values, y_values, t_values = rk_4(x0, y0, a, b, h, t_max)
    
    # Plot results
    plt.figure(figsize=(15, 5))
    
    plt.subplot(131)
    plt.plot(x_values, y_values)
    plt.xlabel('x(t)')
    plt.ylabel('y(t)')
    plt.title(f'Phase Portrait (a={a}, b={b})')
    plt.grid()
    
    plt.subplot(132)
    plt.plot(t_values, x_values)
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('x vs t')
    plt.grid()
    
    plt.subplot(133)
    plt.plot(t_values, y_values)
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.title('y vs t')
    plt.grid()
    
    plt.tight_layout()
    plt.show()
else:
    
    a_values = np.linspace(100, 1000, 5)  
    b_values = np.linspace(100, 650, 5)   
    
    
    for fig_num in range(5):
        
        plt.figure(figsize=(10, 5))
        
        for i in range(2): 
            current_index = 2 * fig_num + i 
            a = a_values[current_index]
            b = b_values[current_index]
            
            # Fixed points
            x0 = a / 5
            y0 = 1 + (a**2) / 25
            
            # Run the RK4 solver
            x_values, y_values, t_values = rk_4(x0, y0, a, b, h, t_max)
            
            # Phase Portrait
            plt.subplot(2, 3, 3*i + 1)
            plt.plot(x_values, y_values)
            plt.xlabel('x(t)')
            plt.ylabel('y(t)')
            plt.title(f'Phase Portrait (a={a:.1f}, b={b:.1f})')
            plt.grid()
            
            # x vs t
            plt.subplot(2, 3, 3*i + 2)
            plt.plot(t_values, x_values)
            plt.xlabel('t')
            plt.ylabel('x(t)')
            plt.title(f'x vs t (a={a:.1f}, b={b:.1f})')
            plt.grid()
            
            # y vs t
            plt.subplot(2, 3, 3*i + 3)
            plt.plot(t_values, y_values)
            plt.xlabel('t')
            plt.ylabel('y(t)')
            plt.title(f'y vs t (a={a:.1f}, b={b:.1f})')
            plt.grid()
            
            print(f'Plot {current_index + 1}/10: a={a:.1f}, b={b:.1f}')
        
        plt.tight_layout()
        plt.show()