import dash
# from dash import dcc
# from dash import html
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
from Conexion_Consulta import Connection
import projectSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ESCENARIO 1 ***********************************************************************************************

# BRONX ############################################################################################
# Bronx
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.CovidBronx(), con.connection)
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])

queryB= pd.read_sql_query(sql.BeforeCovidBronx(), con.connection)
dfBefore = pd.DataFrame(queryB, columns=["time", "num_accidents"])

queryD= pd.read_sql_query(sql.DuringCovidBronx(), con.connection)
dfDuring = pd.DataFrame(queryD, columns=["time", "num_accidents"])

queryA= pd.read_sql_query(sql.AfterCovidBronx(), con.connection)
dfAfter = pd.DataFrame(queryA, columns=["time", "num_accidents"])

con.closeConnection()

casos=dfCases['num_accidents'].tolist()
before= dfBefore['num_accidents'].tolist()
during= dfDuring['num_accidents'].tolist()
after= dfAfter['num_accidents'].tolist()
times=dfCases['time'].tolist()

data = {
    'Time' : times,
    'Pre-Pandemia' : before,
    'En Pandemia' : during,
    'Post-Pandemia' : after
}
datafame=pd.DataFrame(data)
num_accidents = [before, during, after]

figLineBronx = px.line(datafame, x='Time', y=num_accidents, markers = True, title="Bronx - Número de accidentes por hora")
names = {'wide_variable_0':'Pre-Pandemia', 'wide_variable_1':'En Pandemia', 'wide_variable_2':'Post-Pandemia'}
figLineBronx.for_each_trace(lambda t: t.update(name = names[t.name],
                                      legendgroup = names[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, names[t.name])
                                     ))


# BronxBeforeCovid ---------------------------------------------------------------------------------
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.BeforeCovidBronx(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarBronxBC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieBronxBC = px.pie(dfCases.head(24), names="time", values="num_accidents")

# BronxDuringCovid---------------------------------------------------------------------------------
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.DuringCovidBronx(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarBronxDC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieBronxDC = px.pie(dfCases.head(24), names="time", values="num_accidents")

# BronxAfterCovid ---------------------------------------------------------------------------------
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.AfterCovidBronx(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarBronxAC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieBronxAC = px.pie(dfCases.head(24), names="time", values="num_accidents")
# END BRONX ############################################################################################

# BROOKLYN ############################################################################################
# Brooklyn
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.CovidBrooklyn(), con.connection)
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])

queryB= pd.read_sql_query(sql.BeforeCovidBrooklyn(), con.connection)
dfBefore = pd.DataFrame(queryB, columns=["time", "num_accidents"])

queryD= pd.read_sql_query(sql.DuringCovidBrooklyn(), con.connection)
dfDuring = pd.DataFrame(queryD, columns=["time", "num_accidents"])

queryA= pd.read_sql_query(sql.AfterCovidBrooklyn(), con.connection)
dfAfter = pd.DataFrame(queryA, columns=["time", "num_accidents"])

con.closeConnection()

casos=dfCases['num_accidents'].tolist()
before= dfBefore['num_accidents'].tolist()
during= dfDuring['num_accidents'].tolist()
after= dfAfter['num_accidents'].tolist()
times=dfCases['time'].tolist()

data = {
    'Time' : times,
    'Pre-Pandemia' : before,
    'En Pandemia' : during,
    'Post-Pandemia' : after
}
datafame=pd.DataFrame(data)
num_accidents = [before, during, after]

figLineBrooklyn = px.line(datafame, x='Time', y=num_accidents, markers = True, title="Brooklyn - Número de accidentes por hora")
nombre = {'wide_variable_0':'Pre-Pandemia', 'wide_variable_1':'En Pandemia', 'wide_variable_2':'Post-Pandemia'}
figLineBrooklyn.for_each_trace(lambda t: t.update(name = nombre[t.name],
                                      legendgroup = nombre[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, nombre[t.name])
                                     ))



# BrooklynBeforeCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.BeforeCovidBrooklyn(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarBrooklynBC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieBrooklynBC = px.pie(dfCases.head(24), names="time", values="num_accidents")

# BrooklynDuringCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.DuringCovidBrooklyn(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarBrooklynDC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieBrooklynDC = px.pie(dfCases.head(24), names="time", values="num_accidents")

# BrooklynAfterCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.AfterCovidBrooklyn(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarBrooklynAC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieBrooklynAC = px.pie(dfCases.head(24), names="time", values="num_accidents")
# END BROOKLYN ############################################################################################

# MANHATTAN ############################################################################################
# Manhattan
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.CovidManhattan(), con.connection)
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])

queryB= pd.read_sql_query(sql.BeforeCovidManhattan(), con.connection)
dfBefore = pd.DataFrame(queryB, columns=["time", "num_accidents"])

queryD= pd.read_sql_query(sql.DuringCovidManhattan(), con.connection)
dfDuring = pd.DataFrame(queryD, columns=["time", "num_accidents"])

queryA= pd.read_sql_query(sql.AfterCovidManhattan(), con.connection)
dfAfter = pd.DataFrame(queryA, columns=["time", "num_accidents"])

con.closeConnection()

casos=dfCases['num_accidents'].tolist()
before= dfBefore['num_accidents'].tolist()
during= dfDuring['num_accidents'].tolist()
after= dfAfter['num_accidents'].tolist()
times=dfCases['time'].tolist()

data = {
    'Time' : times,
    'Pre-Pandemia' : before,
    'En Pandemia' : during,
    'Post-Pandemia' : after
}
datafame=pd.DataFrame(data)
num_accidents = [before, during, after]

figLineManhattan = px.line(datafame, x='Time', y=num_accidents, markers = True, title="Manhattan - Número de accidentes por hora")
nombre = {'wide_variable_0':'Pre-Pandemia', 'wide_variable_1':'En Pandemia', 'wide_variable_2':'Post-Pandemia'}
figLineManhattan.for_each_trace(lambda t: t.update(name = nombre[t.name],
                                      legendgroup = nombre[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, nombre[t.name])
                                     ))

# ManhattanBeforeCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.BeforeCovidManhattan(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarManhattanBC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieManhattanBC = px.pie(dfCases.head(24), names="time", values="num_accidents")

# ManhattanDuringCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.DuringCovidManhattan(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarManhattanDC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieManhattanDC = px.pie(dfCases.head(24), names="time", values="num_accidents")


# ManhattanAfterCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.AfterCovidManhattan(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarManhattanAC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieManhattanAC = px.pie(dfCases.head(24), names="time", values="num_accidents")

# END MANHATTAN ############################################################################################

# QUENNS ############################################################################################
#Queens
# Queens
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.CovidQueens(), con.connection)
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])

queryB= pd.read_sql_query(sql.BeforeCovidQueens(), con.connection)
dfBefore = pd.DataFrame(queryB, columns=["time", "num_accidents"])

queryD= pd.read_sql_query(sql.DuringCovidQueens(), con.connection)
dfDuring = pd.DataFrame(queryD, columns=["time", "num_accidents"])

queryA= pd.read_sql_query(sql.AfterCovidQueens(), con.connection)
dfAfter = pd.DataFrame(queryA, columns=["time", "num_accidents"])

con.closeConnection()

casos=dfCases['num_accidents'].tolist()
before= dfBefore['num_accidents'].tolist()
during= dfDuring['num_accidents'].tolist()
after= dfAfter['num_accidents'].tolist()
times=dfCases['time'].tolist()

data = {
    'Time' : times,
    'Pre-Pandemia' : before,
    'En Pandemia' : during,
    'Post-Pandemia' : after
}
datafame=pd.DataFrame(data)
num_accidents = [before, during, after]

figLineQueens = px.line(datafame, x='Time', y=num_accidents, markers = True, title="Queens - Número de accidentes por hora")
nombre = {'wide_variable_0':'Pre-Pandemia', 'wide_variable_1':'En Pandemia', 'wide_variable_2':'Post-Pandemia'}
figLineQueens.for_each_trace(lambda t: t.update(name = nombre[t.name],
                                      legendgroup = nombre[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, nombre[t.name])
                                     ))

# QueensBeforeCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.BeforeCovidQueens(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarQueensBC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieQueensBC = px.pie(dfCases.head(24), names="time", values="num_accidents")

# QueensDuringCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.DuringCovidQueens(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarQueensDC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieQueensDC = px.pie(dfCases.head(24), names="time", values="num_accidents")

# QueensAfterCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.AfterCovidQueens(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarQueensAC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieQueensAC = px.pie(dfCases.head(24), names="time", values="num_accidents")
# END QUEENS ############################################################################################

# STATEN ISLAND ############################################################################################
# StatenIsland
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.CovidStatenI(), con.connection)
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])

queryB= pd.read_sql_query(sql.BeforeCovidStatenI(), con.connection)
dfBefore = pd.DataFrame(queryB, columns=["time", "num_accidents"])

queryD= pd.read_sql_query(sql.DuringCovidStatenI(), con.connection)
dfDuring = pd.DataFrame(queryD, columns=["time", "num_accidents"])

queryA= pd.read_sql_query(sql.AfterCovidStatenI(), con.connection)
dfAfter = pd.DataFrame(queryA, columns=["time", "num_accidents"])

con.closeConnection()

casos=dfCases['num_accidents'].tolist()
before= dfBefore['num_accidents'].tolist()
during= dfDuring['num_accidents'].tolist()
after= dfAfter['num_accidents'].tolist()
times=dfCases['time'].tolist()

data = {
    'Time' : times,
    'Pre-Pandemia' : before,
    'En Pandemia' : during,
    'Post-Pandemia' : after
}
datafame=pd.DataFrame(data)
num_accidents = [before, during, after]

figLineStatenI = px.line(datafame, x='Time', y=num_accidents, markers = True, title="StatenI - Número de accidentes por hora")
nombre = {'wide_variable_0':'Pre-Pandemia', 'wide_variable_1':'En Pandemia', 'wide_variable_2':'Post-Pandemia'}
figLineStatenI.for_each_trace(lambda t: t.update(name = nombre[t.name],
                                      legendgroup = nombre[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, nombre[t.name])
                                     ))

# StatenIBeforeCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.BeforeCovidStatenI(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarStatenIBC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieStatenIBC = px.pie(dfCases.head(24), names="time", values="num_accidents")

# StatenIDuringCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.DuringCovidStatenI(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarStatenIDC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieStatenIDC = px.pie(dfCases.head(24), names="time", values="num_accidents")

# StatenIAfterCovid
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.AfterCovidStatenI(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarStatenIAC = px.bar(dfCases.head(24), x="time", y="num_accidents")
# grafico de pie
figPieStatenIAC = px.pie(dfCases.head(24), names="time", values="num_accidents")
# END STATEN ISLAND ############################################################################################

# FIN ESCENARIO 1 ***********************************************************************************************

# 2do Escenario
'''
# BronxByArea
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.BronxByArea(), con.connection)
con.closeConnection()
dfBronxByA = pd.dataframe(query, columns=["borough", "accidentality"]
# Grafico de mapa
figMapBronxByA = px.choroplet(dfcases, locations="borough", color="accidentality", color_continous_scale="aggrnyl")
'''

# ESCENARIO 4 ******************************************************************************************
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.cuarto(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["time", "num_accidents"])
# Grafico de barra
figBarCuarto = px.bar(dfCases.head(24), x="time", y="num_accidents")


# FIN ESCENARIO 4 ***************************************************************************************


# Layout ----------------------------------------
app.layout = html.Div(children=[

# CASOS BRONX -----------------------------------------
    html.H1(children='  ', style={'text-align': 'center'}),
    html.H1(children='DASHBOARD - Base de datos Colisiones NYC', style={'padding-top': '50px','padding-bottom': '50px','text-align':'center'}),
    html.H2(children='1. Número de accidentes antes, durante y después de la pandemia por distrito', style={'color': 'blue', 'text-align':'center', 'padding-bottom': '30px'}),
    html.H3(children='Bronx'),
#Linea
    dcc.Graph(
        id='lineBronx',
        figure=figLineBronx
    ),
    # Row for cases
    html.Div(className="row", children=[
        # Col for vertical bars
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Pre-Pandemia'),
                ]),
                html.Div(className="Before Covid", children=[
                    html.H6(children='Gráfico de Barras',style={'text-align': 'center','padding-top': '10px'}),
                    dcc.Graph(
                        id='BarBronxCollisionsBeforeCovid',
                        figure=figBarBronxBC
                    ),
                    html.H6(children='Gráfico Circular',style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieBronxCollisionsBeforeCovid',
                        figure=figPieBronxBC
                    ),

                ]),

            ]),
        ]),
    # Col for vertical bars
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='En Pandemia'),
                ]),
                html.Div(className="During Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarBronxCollisionsDuringCovid',
                        figure=figBarBronxDC
                    ),
                    html.H6(children='Gráfico Circular',style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieBronxCollisionsDuringCovid',
                        figure=figPieBronxDC
                    ),
                ]),

            ]),
        ]),
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Post-Pandemia'),
                ]),
                html.Div(className="After Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarBronxCollisionsAfterCovid',
                        figure=figBarBronxAC
                    ),

                    html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieBronxCollisionsAfterCovid',
                        figure=figPieBronxAC
                    ),

                ]),

            ]),
        ]),

    ],style={'padding-left': '30px',   'padding-right': '30px', 'padding-bottom': '30px'}),
# FIN CASOS BRONX -----------------------------------------

# BROOKLYN ---------------------------------
    html.H3(children='Brooklyn'),
    dcc.Graph(
        id='lineBrooklyn',
        figure=figLineBrooklyn
    ),
    # Row for cases
    html.Div(className="row", children=[
        # Col for vertical bars
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Pre-Pandemia'),
                ]),
                html.Div(className="Before Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarBrooklynCollisionsBeforeCovid',
                        figure=figBarBrooklynBC
                    ),
                    html.H6(children='Gráfico Circular',style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieBrooklynCollisionsBeforeCovid',
                        figure=figPieBrooklynBC
                    ),
                ]),
            ]),
        ]),
        # Col for vertical bars
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='En Pandemia'),
                ]),
                html.Div(className="During Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarBrooklynCollisionsDuringCovid',
                        figure=figBarBrooklynDC
                    ),

                    html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieBrooklynCollisionsDuringCovid',
                        figure=figPieBrooklynDC
                    ),
                ]),

            ]),
        ]),
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Post-Pandemia'),
                ]),
                html.Div(className="After Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarBrooklynCollisionsAfterCovid',
                        figure=figBarBrooklynAC
                    ),
                    html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieBrooklynCollisionsAfterCovid',
                        figure=figPieBrooklynAC
                    ),
                ]),

            ]),
        ]),

    ],style={'padding-left': '30px',   'padding-right': '30px', 'padding-bottom': '30px'}),
# FIN BROOKLYN ---------------------------------

# MANHATTAN ---------------------------------------------------------
    html.H3(children='Manhattan'),
    dcc.Graph(
        id='lineManhattan',
        figure=figLineManhattan
    ),
    # Row for cases
    html.Div(className="row", children=[
        # Col for vertical bars
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Pre-Pandemia'),
                ]),
                html.Div(className="Before Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarManhattanCollisionsBeforeCovid',
                        figure=figBarManhattanBC
                    ),
                    html.H6(children='Gráfico Circular',style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieManhattanCollisionsBeforeCovid',
                        figure=figPieManhattanBC
                    ),
                ]),

            ]),
        ]),
        # Col for vertical bars
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='En Pandemia'),
                ]),
                html.Div(className="During Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarManhattanCollisionsDuringCovid',
                        figure=figBarManhattanDC
                    ),

                    html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieManhattanCollisionsDuringCovid',
                        figure=figPieManhattanDC
                    ),
                ]),

            ]),
        ]),
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Post-Pandemia'),
                ]),
                html.Div(className="After Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarManhattanCollisionsAfterCovid',
                        figure=figBarManhattanAC
                    ),

                    html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieManhattanCollisionsAfterCovid',
                        figure=figPieManhattanAC
                    ),
                ]),

            ]),
        ]),

    ],style={'padding-left': '30px',   'padding-right': '30px', 'padding-bottom': '30px'}),
# FIN MANHATTAN ---------------------------------

# QUEENS ---------------------------------------
    html.H3(children='Queens'),
    dcc.Graph(
        id='lineQueens',
        figure=figLineQueens
    ),
    # Row for cases
    html.Div(className="row", children=[
        # Col for vertical bars
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Pre-Pandemia'),
                ]),
                html.Div(className="Before Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarQueensCollisionsBeforeCovid',
                        figure=figBarQueensBC
                    ),
                    html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieQueensCollisionsBeforeCovid',
                        figure=figPieQueensBC
                    ),
                ]),

            ]),
        ]),
        # Col for vertical bars
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='En Pandemia'),
                ]),
                html.Div(className="During Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarQueensCollisionsDuringCovid',
                        figure=figBarQueensDC

                    ),
                    html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieQueensCollisionsDuringCovid',
                        figure=figPieQueensDC
                    ),
                ]),

            ]),
        ]),
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Post-Pandemia'),
                ]),
                html.Div(className="After Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarQueensCollisionsAfterCovid',
                        figure=figBarQueensAC
                    ),

                    html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieQueensCollisionsAfterCovid',
                        figure=figPieQueensAC
                    ),
                ]),

            ]),
        ]),

    ],style={'padding-left': '30px',   'padding-right': '30px', 'padding-bottom': '30px'}),
# FIN DE QUEENS -----------------------

# STATEN ISLAND -------------------------------------------------
    html.H3(children='Staten Island'),

    dcc.Graph(
        id='lineStatenI',
        figure=figLineStatenI
    ),
    # Row for cases
    html.Div(className="row", children=[
        # Col for vertical bars
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Pre-Pandemia'),
                ]),
                html.Div(className="Before Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                            id='BarStatenICollisionsBeforeCovid',
                            figure=figBarStatenIBC
                    ),
                    html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieStatenICollisionsBeforeCovid',
                        figure=figPieStatenIBC
                    ),
                ]),

            ]),
        ]),
        # Col for vertical bars
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='En Pandemia'),
                ]),
                html.Div(className="During Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarStatenICollisionsDuringCovid',
                        figure=figBarStatenIDC
                    ),
                    html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieStatenICollisionsDuringCovid',
                        figure=figPieStatenIDC
                    ),

                ]),

            ]),
        ]),
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Post-Pandemia'),
                ]),
                html.Div(className="After Covid", children=[
                    html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                    dcc.Graph(
                        id='BarStatenICollisionsAfterCovid',
                        figure=figBarStatenIAC
                    ),

                    html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                    dcc.Graph(
                        id='PieStatenICollisionsAfterCovid',
                        figure=figPieStatenIAC
                    ),
                ]),

            ]),
        ]),

    ],style={'padding-left': '30px',   'padding-right': '30px', 'padding-bottom': '30px'}),
# FIN DE STATEN ISLAND -----------------------


    '''html.H1(children='Map Bronx Accidentality'),
    html.H2(children='By Area'),
    # Map BronxByArea
    dcc.Graph(
        id='MapBronxByArea',
        figure=figMapBronxByA
    ),'''
])

if __name__ == '__main__':
    app.run_server(debug=True)
