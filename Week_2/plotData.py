import matplotlib.pyplot as plt

#   plotData Plots the data points x and y 
#   plotData(x,y) plots the data points and gives the figure axes labels of
#   population and profit.

def plotData(x, y):

    # ====================== YOUR CODE HERE ======================
    # Readings    : https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html
    
    # Instructions: Plot the training data into a figure using the 
    #               plt.scatter and plt.show functions. Set the axes labels using
    #               the "xlabel" and "ylabel" functions. Assume the 
    #               population and revenue data have been passed in
    #               as the x and y arguments of this function.
    #
    # Hint: You can use the c="#ff0000" and marker="x" option with plt.scatter to have the markers
    #       appear as red crosses. Furthermore, you can make the
    #       markers larger by using plt.scatter(..., , s=50)

    plt.scatter(x, y, c="#ff0000", marker="x", s=50)
    plt.xlabel('Population of City in 10,000s')
    plt.ylabel('Profit in $10,000s')
    plt.show()

    # ============================================================

