import pandas as pd
from bokeh.plotting import show, output_notebook, curdoc
from bokeh.layouts import column
from bokeh.models.widgets import Select

# Sample Data
data = {
    'source': ['A', 'B', 'A', 'C', 'C', 'D'],
    'target': ['B', 'C', 'D', 'D', 'E', 'E'],
    'value': [10, 5, 15, 5, 20, 10]
}
df = pd.DataFrame(data)

output_notebook()

def draw_sankey(node_name=None):
    if node_name and node_name != "All":
        filtered_df = df[(df['source'] == node_name) | (df['target'] == node_name)]
    else:
        filtered_df = df

    # ... [rest of the Sankey drawing code, identical to previous]

    return plot

def update(attr, old, new):
    layout.children[1] = draw_sankey(new)

node_list = ["All"] + list(pd.concat([df['source'], df['target']]).unique())
dropdown = Select(title="Select Node:", value="All", options=node_list)
dropdown.on_change('value', update)

initial_sankey = draw_sankey()
layout = column(dropdown, initial_sankey)

curdoc().add_root(layout)
show(layout)