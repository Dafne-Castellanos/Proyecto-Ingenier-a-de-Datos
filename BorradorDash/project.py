import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from Connection import Connection
import projectSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# 1er Escenario

# BronxBeforeCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.BeforeCovidBronx(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])                               
#Grafico de barra
figBarBronxBC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# BronxDuringCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.DuringCovidBronx(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])
#Grafico de barra
figBarBronxDC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# BronxAfterCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.AfterCovidBronx(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])
#Grafico de barra
figBarBronxAC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# BrooklynBeforeCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.BeforeCovidBrooklyn(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])                               
#Grafico de barra
figBarBrooklynBC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# BrooklynDuringCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.DuringCovidBrooklyn(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])
#Grafico de barra
figBarBrooklynDC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# BrooklynAfterCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.AfterCovidBrooklyn(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])
#Grafico de barra
figBarBrooklynAC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# ManhattanBeforeCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.BeforeCovidManhattan(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])                               
#Grafico de barra
figBarManhattanBC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# ManhattanDuringCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.DuringCovidManhattan(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])
#Grafico de barra
figBarManhattanDC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# ManhattanAfterCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.AfterCovidManhattan(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])
#Grafico de barra
figBarManhattanAC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# QueensBeforeCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.BeforeCovidQueens(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])                               
#Grafico de barra
figBarQueensBC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# QueensDuringCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.DuringCovidQueens(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])
#Grafico de barra
figBarQueensDC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# QueensAfterCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.AfterCovidQueens(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])
#Grafico de barra
figBarQueensAC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# StatenIBeforeCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.BeforeCovidStatenI(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])                               
#Grafico de barra
figBarStatenIBC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# StatenIDuringCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.DuringCovidStatenI(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])
#Grafico de barra
figBarStatenIDC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# StatenIAfterCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.AfterCovidStatenI(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time","num_accidents"])
#Grafico de barra
figBarStatenIAC = px.bar(dfCases.head(24), x = "time", y = "num_accidents")

# 2do Escenario

#BronxByArea
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.BronxByArea(), con.connection)
con.closeConnection()
dfBronxByA = pd.dataframe(query, columns=["borough", "accidentality"]
#Grafico de mapa
figMapBronxByA = px.choroplet(dfcases, locations="borough", color = "accidentality", color_continous_scale="aggrnyl")


# Layout
app.layout = html.Div(children=[
    html.H1(children = 'BarGraphics Bronx Collisions'),
    html.H2(children = 'Before Covid'),
    # Bar BronxBeforeCovid
    dcc.Graph(
        id = 'BarBronxCollisionsBeforeCovid',
        figure = figBarBronxBC
    ),
    html.H3(children = 'During Covid'),
    # Bar BronxDuringCovid
    dcc.Graph(
        id = 'BarBronxCollisionsDuringCovid',
        figure = figBarBronxDC
    ),
    html.H4(children = 'After Covid'),
    # Bar BronxAfterCovid
    dcc.Graph(
        id = 'BarBronxCollisionsAfterCovid',
        figure = figBarBronxAC
    ),

    html.H1(children = 'BarGraphics Brooklyn Collisions'),
    html.H2(children = 'Before Covid'),
    # Bar BrooklynBeforeCovid
    dcc.Graph(
        id = 'BarBrooklynCollisionsBeforeCovid',
        figure = figBarBrooklynBC
    ),
    html.H3(children = 'During Covid'),
    # Bar BrooklynDuringCovid
    dcc.Graph(
        id = 'BarBrooklynCollisionsDuringCovid',
        figure = figBarBrooklynDC
    ),
    html.H4(children = 'After Covid'),
    # Bar BrooklynAfterCovid
    dcc.Graph(
        id = 'BarBrooklynCollisionsAfterCovid',
        figure = figBarBrooklynAC
    ),

    html.H1(children = 'BarGraphics Manhattan Collisions'),
    html.H2(children = 'Before Covid'),
    # Bar ManhattanBeforeCovid
    dcc.Graph(
        id = 'BarManhattanCollisionsBeforeCovid',
        figure = figBarManhattanBC
    ),
    html.H3(children = 'During Covid'),
    # Bar ManhattanDuringCovid
    dcc.Graph(
        id = 'BarManhattanCollisionsDuringCovid',
        figure = figBarManhattanDC
    ),
    html.H4(children = 'After Covid'),
    # Bar ManhattanAfterCovid
    dcc.Graph(
        id = 'BarManhattanCollisionsAfterCovid',
        figure = figBarManhattanAC
    ),
    
    html.H1(children = 'BarGraphics Queens Collisions'),
    html.H2(children = 'Before Covid'),
    # Bar QueensBeforeCovid
    dcc.Graph(
        id = 'BarQueensCollisionsBeforeCovid',
        figure = figBarQueensBC
    ),
    html.H3(children = 'During Covid'),
    # Bar QueensDuringCovid
    dcc.Graph(
        id = 'BarQueensCollisionsDuringCovid',
        figure = figBarQueensDC
    ),
    html.H4(children = 'After Covid'),
    # Bar QueensAfterCovid
    dcc.Graph(
        id = 'BarQueensCollisionsAfterCovid',
        figure = figBarQueensAC
    ),

    html.H1(children = 'BarGraphics Staten Island Collisions'),
    html.H2(children = 'Before Covid'),
    # Bar StatenIBeforeCovid
    dcc.Graph(
        id = 'BarStatenICollisionsBeforeCovid',
        figure = figBarStatenIBC
    ),
    html.H3(children = 'During Covid'),
    # Bar StatenIDuringCovid
    dcc.Graph(
        id = 'BarStatenICollisionsDuringCovid',
        figure = figBarStatenIDC
    ),
    html.H4(children = 'After Covid'),
    # Bar StatenIAfterCovid
    dcc.Graph(
        id = 'BarStatenICollisionsAfterCovid',
        figure = figBarStatenIAC
    ),

    html.H1(children = 'Map Bronx Accidentality'),
    html.H2(children = 'By Area'),
    # Map BronxByArea
    dcc.Graph(
        id = 'MapBronxByArea',
        figure = figMapBronxByA
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)

"""
    # Inicializacion app3 dash
app3 = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#During
con3 = Connection()
con3.openConnection()
query3 = pd.read_sql_query(sql.AfterCovidBronx(), con3.connection)
con3.closeConnection()
dfCases3 = pd.DataFrame(query3, columns=["time","num_accidents"])
# Grafico de barras
figBarCases3 = px.bar(dfCases3.head(24), x = "time", y = "num_accidents")
# Layout
app3.layout = html.Div(children=[
    html.H1(children = 'DashBoard Bronx Collisions After Covid'),
    html.H2(children = 'Num_Accidents per hour'),
    dcc.Graph(
        id = 'BarBronxCollisionsAfterCovid',
        figure = figBarCases3
    )
])
if __name__ == '__main__':
    app3.run_server(debug=True)


# Colisiones antes del covid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.cuarto(), con.connection)
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
])"""
