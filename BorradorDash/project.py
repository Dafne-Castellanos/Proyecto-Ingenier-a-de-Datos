import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import projectSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Colisiones antes del covid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.CuatroBronx(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["person_age", "sex", "person_type"])

# Grafico barras
figBarCases = px.bar(dfCases.head(20), x="sex", y="person_age")

# Layout 
app.layout = html.Div(children=[
    html.H1(children='Dashboard NYC Collisions '),
    html.H2(children='Bronx residentes caracteristics'),
    dcc.Graph(
        id='barBronxResidentsCaracteristics',
        figure=figBarCases
    )  
])

if __name__ == '__main__':
    app.run_server(debug=True)
