python
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# Create a Dash app
app = dash.Dash(__name__)

# Sample data (you can replace this with your dataset)
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 20, 15, 25]
}
df = pd.DataFrame(data)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1('Basic Data Dashboard'),
    
    dcc.Graph(id='bar-chart'),
    
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': cat, 'value': cat} for cat in df['Category']],
        value='A'
    )
])

# Define callback to update the bar chart based on dropdown selection
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_chart(selected_category):
    filtered_df = df[df['Category'] == selected_category]
    figure = {
        'data': [
            {'x': filtered_df['Category'], 'y': filtered_df['Value'], 'type': 'bar', 'name': selected_category}
        ],
        'layout': {
            'title': f'Bar Chart for Category {selected_category}',
            'xaxis': {'title': 'Category'},
            'yaxis': {'title': 'Value'}
        }
    }
    return figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


