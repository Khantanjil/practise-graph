# Importing Bokeh

from bokeh.plotting import figure
from bokeh.io import show, output_file

# Data
x = [3,7.5,10]
y = [3,6,9]

# Output file on html
output_file("graph.html")

f = figure()

# Create plot point
f.triangle(x,y)
show(f)