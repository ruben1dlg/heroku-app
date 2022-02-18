from dash import Dash, html, dcc, Input, Output
import altair as alt


# Read in global data
df = data.gapminder()

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.layout = html.Div([
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='pop',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in ['pop', 'life_expect', 'fertility']])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart = alt.Chart(df).mark_point().encode(
        x=xcol,
        y='pop',
        tooltip='country').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)