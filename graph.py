from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    "match": ["M1", "M2", "M3", "M4"],
    "shots": [14, 10, 18, 12]
})

fig = px.line(df, x="match", y="shots")

app.layout = html.Div([
    html.H1("Barcelona Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)