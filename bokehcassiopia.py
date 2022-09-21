# Python3.7.1
# Bokeh Visual Example

import pandas as pd
import numpy as np

from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel

# Where the visualization will be rendered.
output_file('output_file_test.html', title='Empty Bokeh Figure')
output_notebook()  # Render inline in Jupyter Notebook.


# X-Y coordinate data.
x = [1.4, 3, 4.9, 6, 7.6]
y = [5.9, 3, 3.6, 1, 3.4]

# Output the visualization directly in the notebook.
output_file('first_glyphs.html', title='First Glyphs')


# Create a figure with no toolbar and axis ranges of [0, 5].
fig = figure(title='Cassiopea',
             plot_height=300, plot_width=300,
             x_range=(0, 10), y_range=(0, 10),
             toolbar_location=None)

# Draw the coordinates as circles.
fig.circle(x=x, y=y,
           color='red', size=10, alpha=0.5)

# Remove the gridlines from the figure object.
fig.grid.grid_line_color = None

# See what it looks like.
show(fig)
