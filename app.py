import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlalchemy as sal
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

colors = {
    'text': '#b7410e'
}

# this connects to the SQL database 
engine = sal.create_engine('sqlite:///marswind.db')

#t his loads the main datafram we will be working with from the table master in the database
df = pd.read_sql('SELECT * FROM master', engine)

# this creates the selection list in the drop down
unique_sols = df['sol'].unique().tolist()

# this will display stuff on the web page
app.layout = html.Div([ 
	html.H2(
        children='Wind Direction on Planet Mars',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='A little web application made with Dash for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Br(),

    html.Label('Pick a Sol with complete and valid data:'),
    dcc.Dropdown(
        id='sol-selector',
        options=[{'label': i, 'value': i} for i in unique_sols],
        value=708,
        style=dict(
                    width='40%',
                    verticalAlign="middle"
                )
    ),

    dcc.Graph(id='wind-rose')
])

# this manages the user inputs from the widgets on the web page
@app.callback(
	Output('wind-rose', 'figure'),
	Input('sol-selector', 'value')
    )

# this will be called when the dropdown is selected
def update_graph(sol):
	sol_df = df[df['sol'] == sol]
	#fig = px.bar(x=sol_df['ct'])
	fig = px.bar_polar(r=sol_df['ct'], theta=sol_df['compass_point'])
	return fig


if __name__ == '__main__':
    app.run_server(debug=True)