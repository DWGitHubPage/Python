# Python3.7.1
# Bokeh Visual Example

import pandas as pd
import numpy as np

from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel


# Set up figures
fig = figure(title="Bokeh Coordinates",
             background_fill_color='yellow',
             background_fill_alpha=0.5,
             border_fill_color='blue',
             border_fill_alpha=0.25,
             x_range=(0, 3), y_range=(0, 3),
             toolbar_location=None,
             plot_height=300,
             plot_width=300,
             h_symmetry=True,
             x_axis_label='X Label',
             x_axis_type='datetime',
             x_axis_location='above',
             y_axis_label='Y Label',
             y_axis_type='linear',
             y_axis_location='left',
             title_location='right',
             tools='save')

# Where the visualization will be rendered.
output_file('output_file_test.html',
            title='Bokeh Figure')

output_notebook()  # Render inline in Jupyter Notebook.

# X-Y coordinates.
x = [1, 1.5, 2]
y = [1, 1.5, 2.5]


fig.circle(x=x, y=y,
           color='purple', size=15, alpha=0.5)

# Remove the gridlines from the
fig.grid.grid_line_color = None

# See what it looks like.
show(fig)
