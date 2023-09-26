import pandas as pd
import plotly.graph_objects as go
import ipywidgets as widgets
from IPython.display import display

# Sample Data
data = {
    'source': ['A', 'B', 'A', 'C', 'C', 'D'],
    'target': ['B', 'C', 'D', 'D', 'E', 'E'],
    'value': [10, 5, 15, 5, 20, 10]
}
df = pd.DataFrame(data)

# Function to draw the Sankey chart for a selected node
def draw_sankey(node_name=None):
    if node_name:
        filtered_df = df[(df['source'] == node_name) | (df['target'] == node_name)]
    else:
        filtered_df = df

    label_list = list(pd.concat([filtered_df['source'], filtered_df['target']]).unique())
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=label_list,
        ),
        link=dict(
            source=filtered_df['source'].apply(lambda x: label_list.index(x)),
            target=filtered_df['target'].apply(lambda x: label_list.index(x)),
            value=filtered_df['value']
        )
    )])
    
    if node_name:
        fig.update_layout(title_text=f"Sankey Diagram for Node {node_name}", font_size=10)
    else:
        fig.update_layout(title_text="Full Sankey Diagram", font_size=10)
        
    fig.show()

# Dropdown widget
node_dropdown = widgets.Dropdown(
    options=[('All', None)] + [(node, node) for node in pd.concat([df['source'], df['target']]).unique()],
    value=None,
    description='Node:'
)

# Display the widget and interactivity
widgets.interactive(draw_sankey, node_name=node_dropdown)