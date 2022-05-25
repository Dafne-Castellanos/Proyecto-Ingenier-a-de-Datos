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

# ESCENARIO 1 ********************************************************************************************************************************************

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

# FIN ESCENARIO 1 *************************************************************************************************************************

# ESCENARIO 2 **********************************************************************************************************************
# Poblacion
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.accidentRPopulation(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["borough", "accidentality_rate_population"])
# Grafico de barra
figBarRPopulation = px.bar(dfCases.head(5), x="borough", y="accidentality_rate_population")
# grafico de pie
figPieRPopulation = px.pie(dfCases.head(5), names="borough", values="accidentality_rate_population")
# grafico de lineas
figLineRPopulation= px.line(dfCases.head(5), x="borough", y="accidentality_rate_population")


# Area
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.accidentRArea(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["borough", "accidentality_rate_area"])
# Grafico de barra
figBarRArea = px.bar(dfCases.head(5), x="borough", y="accidentality_rate_area")
# grafico de pie
figPieRArea = px.pie(dfCases.head(5), names="borough", values="accidentality_rate_area")
# grafico de lineas
figLineRArea= px.line(dfCases.head(5), x="borough", y="accidentality_rate_area")

# FIN ESCENARIO2 ************************************************************************************************


# ESCENARIO 3 ************************************************************************************************

# tipo Persona
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.typePerson(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["tipo_persona", "cantidad_personas"])
# Grafico de barra
figBartypePerson = px.bar(dfCases.head(4), x="tipo_persona", y="cantidad_personas")
# Grafico de pie
figPietypePerson = px.pie(dfCases.head(4), names="tipo_persona", values="cantidad_personas")


# sexo Persona
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.sexPerson(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["sexo_persona", "cantidad_personas"])
# Grafico de barra
figBarsexPerson = px.bar(dfCases.head(3), x="sexo_persona", y="cantidad_personas")
# Grafico de pie
figPiesexPerson = px.pie(dfCases.head(3), names="sexo_persona", values="cantidad_personas")

# FIN ESCENARIO 3 ************************************************************************************************


# ESCENARIO 4 ******************************************************************************************
# # Daño del vehiculo
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.damageVehicle(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["daño_vehiculo", "cantidad_vehiculos"])
# Grafico de barra
figBardamageVehicle = px.bar(dfCases.head(19), x="daño_vehiculo", y="cantidad_vehiculos")
# Grafico de pie
figPiedamageVehicle = px.pie(dfCases.head(19), names="daño_vehiculo", values="cantidad_vehiculos")


# Tipo del vehiculo
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.typeVehicle(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["tipo_vehiculo", "cantidad_vehiculos"])
# Grafico de barra
figBartypeVehicle = px.bar(dfCases.head(12), x="tipo_vehiculo", y="cantidad_vehiculos")
# Grafico de pie
figPietypeVehicle = px.pie(dfCases.head(12), names="tipo_vehiculo", values="cantidad_vehiculos")

# FIN ESCENARIO 4 *******************************************************************************************


# Layout ---------------------------------------------------------------------------------------------------------------------------------
app.layout = html.Div(children=[
    html.H1(children='  ', style={'text-align': 'center'}),
    html.H1(children='DASHBOARD - Base de datos Colisiones NYC', style={'padding-top': '50px','padding-bottom': '50px','text-align':'center'}),
    html.H2(children='1. Número de accidentes antes, durante y después de la pandemia por distrito', style={'color': 'blue', 'text-align':'center', 'padding-bottom': '30px'}),
    # BRONX
    html.H3(children='Bronx'),
    dcc.Graph(
        id='lineBronx',
        figure=figLineBronx
    ),
    html.Div(className="row", children=[
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
    html.Div(className="row", children=[
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

# escenario2
html.H2(children='2. Tasas de accidentalidad por Distrito', style={'color': 'blue', 'text-align':'center', 'padding-bottom': '30px'}),
    html.H3(children='Tasa de accidentatidad por población de los distritos de Nueva York'),
        html.Div(className="row", children=[
            # Col for vertical bars
            html.Div(className="col-10 col-xl-4", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H5(children='Gráfico de Barras'),
                    ]),
                    html.Div(className="population", children=[
                        dcc.Graph(
                            id='BarPopulation',
                            figure=figBarRPopulation
                        ),
                    ]),
                ]),
            ]),
            html.Div(className="col-10 col-xl-4", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H5(children='Gráfico Circular'),
                    ]),
                    html.Div(className="population", children=[
                        dcc.Graph(
                            id='PiePopulation',
                            figure=figPieRPopulation
                        ),
                    ]),

                ]),
            ]),
            html.Div(className="col-10 col-xl-4", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H5(children='Gráfico Lineas'),
                    ]),
                    html.Div(className="population", children=[
                        dcc.Graph(
                            id='LinePopulation',
                            figure=figLineRPopulation
                        ),
                    ]),
                ]),
            ]),

        ], style={'padding-left': '200px', 'padding-right': '30px', 'padding-bottom': '30px'}),
    html.H3(children='Tasa de accidentatidad por área de los distritos de Nueva York'),
            html.Div(className="row", children=[
                html.Div(className="col-10 col-xl-4", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header", children=[
                            html.H5(children='Gráfico de Barras'),
                        ]),
                        html.Div(className="area", children=[
                            dcc.Graph(
                                id='BarArea',
                                figure=figBarRArea
                            ),
                        ]),
                    ]),
                ]),
                html.Div(className="col-10 col-xl-4", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header", children=[
                            html.H5(children='Gráfico Circular'),
                        ]),
                        html.Div(className="area", children=[
                            dcc.Graph(
                                id='PieArea',
                                figure=figPieRArea
                            ),
                        ]),
                    ]),
                ]),
                html.Div(className="col-10 col-xl-4", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header", children=[
                            html.H5(children='Gráfico Lineas'),
                        ]),
                        html.Div(className="area", children=[
                            dcc.Graph(
                                id='LineArea',
                                figure=figLineRArea
                            ),
                        ]),
                    ]),
                ]),
            ], style={'padding-left': '200px', 'padding-right': '30px', 'padding-bottom': '30px'}),
# #################

#------------------------------------------------------------------------------------------------------------------
# escenario 3
html.H2(children='3. Tipos y sexos de las personas involucradas en los Accidentes', style={'color': 'blue', 'text-align':'center', 'padding-bottom': '30px'}),
    html.H3(children='Tipos de Personas involucrados en los Accidentes de Nueva York'),
    html.Div(className="row", children=[
        # Col for vertical bars
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Gráfico de Barras'),
                ]),
                html.Div(className="tipoPersona", children=[
                    dcc.Graph(
                        id='BartypePerson',
                        figure=figBartypePerson
                    ),
                ]),
            ]),
        ]),
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Gráfico Circular'),
                ]),
                html.Div(className="tipoPersona", children=[
                    dcc.Graph(
                        id='PietypePerson',
                        figure=figPietypePerson
                    ),
                ]),
            ]),
        ]),
    ], style={'padding-left': '200px', 'padding-right': '30px', 'padding-bottom': '30px'}),
    html.H3(children='Sexos de las personas involucradas en los Accidentes de Nueva York'),
    html.Div(className="row", children=[
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Gráfico de Barras'),
                ]),
                html.Div(className="sexPerson", children=[
                    dcc.Graph(
                        id='BarsexPerson',
                        figure=figBarsexPerson
                    ),
                ]),

            ]),
        ]),
        html.Div(className="col-12 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Gráfico Circular'),
                ]),
                html.Div(className="sexPerson", children=[
                    dcc.Graph(
                        id='PiesexPerson',
                        figure=figPiesexPerson
                    ),
                ]),

            ]),
        ]),

    ], style={'padding-left': '200px', 'padding-right': '30px', 'padding-bottom': '30px'}),
#------------------------------------------------------------------------------------------------------------------

    html.H2(children='4. Tipos y daños de los vehículos involucrados en los Accidentes', style={'color': 'blue', 'text-align':'center', 'padding-bottom': '30px'}),
    html.H3(children='Tipos de Vehículos involucrados en los Accidentes de Nueva York'),
    html.Div(className="row", children=[
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Gráfico de Barras'),
                ]),
                html.Div(className="tipoVehiculo", children=[
                    dcc.Graph(
                        id='BartypeVehicle',
                        figure=figBartypeVehicle
                    ),
                ]),
            ]),
        ]),
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Gráfico Circular'),
                ]),
                html.Div(className="tipoVehiculo", children=[
                    dcc.Graph(
                        id='PietypeVehicle',
                        figure=figPietypeVehicle
                    ),
                ]),
            ]),
        ]),
    ], style={'padding-left': '200px', 'padding-right': '30px', 'padding-bottom': '30px'}),


    html.H3(children='Daños en los Vehículos involucrados en los Accidentes de Nueva York'),
    html.Div(className="row", children=[
        html.Div(className="col-10 col-xl-4", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Gráfico de Barras'),
                ]),
                html.Div(className="tipoVehiculo", children=[
                    dcc.Graph(
                        id='BardamageVehicle',
                        figure=figBardamageVehicle
                    ),
                ]),
            ]),
        ]),
        html.Div(className="col-12 col-xl-7", children=[
            html.Div(className="card border-info", children=[
                html.Div(className="card-header", children=[
                    html.H5(children='Gráfico Circular'),
                ]),
                html.Div(className="tipoVehiculo", children=[
                    dcc.Graph(
                        id='PiedamageVehicle',
                        figure=figPiedamageVehicle
                    ),
                ]),
            ]),
        ]),
    ], style={'padding-left': '200px', 'padding-right': '30px', 'padding-bottom': '30px'}),

])

if __name__ == '__main__':
    app.run_server(debug=True)
