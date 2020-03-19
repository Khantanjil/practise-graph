from bokeh.plotting import figure
from bokeh.io import show, output_file

# Data
x = [3, 7.5, 10]
y = [3, 6, 9]

# Preparate the output file
output_file("Graph_circle.html")

f = figure()
f.circle(x,y)
show(f)