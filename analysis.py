import pandas as pd
from bokeh.models import ColumnDataSource, Plot, Range1d, MultiLine, Circle, HoverTool, TapTool, BoxSelectTool
from bokeh.models.widgets import Dropdown
from bokeh.layouts import column
from bokeh.plotting import show, output_notebook, figure
from bokeh.io import push_notebook

# Sample Data
data = {
    'source': ['A', 'B', 'A', 'C', 'C', 'D'],
    'target': ['B', 'C', 'D', 'D', 'E', 'E'],
    'value': [10, 5, 15, 5, 20, 10]
}
df = pd.DataFrame(data)

# Initialize Bokeh output to notebook
output_notebook()

# Drawing the Sankey chart for a selected node
def draw_sankey(node_name=None):
    if node_name:
        filtered_df = df[(df['source'] == node_name) | (df['target'] == node_name)]
    else:
        filtered_df = df

    # Bokeh doesn't have built-in Sankey functionality, so we simulate using multiline for connections.
    # For simplicity, we just represent nodes as circles and connections as lines between them.
    plot = figure(width=600, height=400, title=f"Sankey Diagram for Node {node_name}" if node_name else "Full Sankey Diagram", 
                  tools="pan,box_zoom,reset", toolbar_location="right")

    # Define nodes and positions (for simplicity, just positioning nodes in a linear fashion)
    nodes = list(pd.concat([df['source'], df['target']]).unique())
    nodes_x = list(range(len(nodes)))
    nodes_y = [1] * len(nodes)

    # Draw lines for connections
    lines_x = []
    lines_y = []
    for _, row in filtered_df.iterrows():
        lines_x.append([nodes_x[nodes.index(row['source'])], nodes_x[nodes.index(row['target'])]])
        lines_y.append([1, 1])

    plot.multi_line(lines_x, lines_y, color="green", line_width=2)

    # Draw nodes
    plot.circle(nodes_x, nodes_y, size=20, color="blue", alpha=0.5)

    handle = show(plot, notebook_handle=True)
    push_notebook(handle=handle)

# Using Bokeh's Dropdown widget to select nodes
def update(attr, old, new):
    draw_sankey(node_dropdown.value)

node_list = ["All"] + list(pd.concat([df['source'], df['target']]).unique())
node_dropdown = Dropdown(label="Select Node", button_type="warning", menu=node_list)
node_dropdown.on_change('value', update)

show(column(node_dropdown))

# Display initial Sankey diagram
draw_sankey()