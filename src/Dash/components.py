import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
import numpy as np
import dash_table
from .apis import *


# Dummy ids
ids = [f"patient#2018tag_{d}" for d in range(10)]



ext_styles = dbc.themes.BOOTSTRAP
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="http://127.0.0.1:5000/")),
        dbc.NavItem(dbc.NavLink("DashBoard",
                href="http://127.0.0.1:5000/dashboard")),
        dbc.NavItem(dbc.NavLink(
                "Contact", 
                href="https://www.linkedin.com/in/rudra-prasad-dash-85491910b/",
                target="_blank"
                ),            
            ),
    ],
    brand="DiCare",
    brand_style={
        "fontWeight":"bold"
        },
    brand_href="http://127.0.0.1:5000/",
    color="primary",
    dark=True,
)

# Dropdown ids
ids = dcc.Dropdown(
                id='ids',
                options=[{'label': i, 'value': i.split("_")[1]} for i in ids],
                value='Patient Ids',
)

# Line plots
hr = dcc.Graph(id='hr')
insulin = dcc.Graph(id='insulin')
carbs = dcc.Graph(id='carbs')

# Age
age_val = html.P(id='age')



base_template = html.Div(children=[
    navbar,
    dbc.Row(children=[
        dbc.Col(children=[
            ids,
            ],
        style={"maxWidth" : "60%", "textAlign" : "center", "marginTop" : "20px", "marginLeft" : "20px"}
        )
    ]),
    dbc.Row(children=[age_val]),
    dbc.Row(children=[
        dbc.Col(children=[
            hr,
        ]),
        dbc.Col(children=[
            insulin,
        ]),
        dbc.Col(children=[
            carbs,
        ])
    ], style={
        "marginTop" : "30px"
    })
    
    
], )