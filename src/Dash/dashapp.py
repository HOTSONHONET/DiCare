from dash import Dash
from .components import *
import os
import pandas as pd
import dash.dependencies as dd
from dash.dependencies import Input, Output



# Styles
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def init_dashboard(server):
    app = Dash(server = server,
                routes_pathname_prefix = "/dashboard/",
                external_stylesheets = [ext_styles],
                title = "DashBoard"
    )
    app._favicon = "icon.ico"
    app.layout = base_template

    init_callbacks(app)

    return app.server



def init_callbacks(app):

    # Callback for heartrate
    @app.callback(
    Output("hr", "figure"), 
    [Input("ids", "value")])
    def update_hr(d):
        hrs, t = heartrate(d)
        fig = px.line(x=t, y=hrs,)

        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text'],
            title_text = "Heart Rate Monitoring",
            title_x = 0.5,
            xaxis_title="Time",
            yaxis_title="heartrate",

            
        )

        return fig
    
    # Callback for insulin
    @app.callback(
    Output("insulin", "figure"), 
    [Input("ids", "value")])
    def update_insulin(d):
        ins, t = insulin_val(d)
        fig = px.line(x=t, y=ins,)
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text'],
            title_text = "Insulin Level Monitoring",
            title_x = 0.5,
            xaxis_title="Time",
            yaxis_title="insulin levels",

        )
        return fig
    
    # Callback for insulin
    @app.callback(
    Output("carbs", "figure"), 
    [Input("ids", "value")])
    def update_carbs(d):
        cbs, t = carbs_taken(d)
        fig = px.line(x=t, y=cbs,)
        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text'],
            title_text = "Carbs Level Monitoring",
            title_x = 0.5,
            xaxis_title="Time",
            yaxis_title="carbs levels",

        )
        return fig
    
        
        