from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from IPython.core.display import Javascript
from IPython.display import display
import pyugend2
import time
import datetime
import builtins
from IPython.lib import deepreload
builtins.reload = deepreload.reload
import warnings
warnings.filterwarnings('ignore')
from fitter import Fitter


def data_export_widget():
    
    style = {'description_width': 'initial'}
    widget_dict = {}
    vbox_list = []
    widget_dict['button_no_growth'] = widgets.Button(
        description='Export No Growth Model',
        disabled=False,
        button_style='',
        tooltip='Export to CSV',
        icon='check')
    widget_dict['button_linear_growth'] = widgets.Button(
        description='Export Linear Growth Model',
        disabled=False,
        button_style='',
        tooltip='Export to CSV',
        icon='check')
    widget_dict['button_3yr_growth'] = widgets.Button(
        description='Export 3yr Growth Model',
        disabled=False,
        button_style='',
        tooltip='Export to CSV',
        icon='check')
    widget_dict['button_4yr_growth'] = widgets.Button(
        description='Export 4yr Growth Model',
        disabled=False,
        button_style='',
        tooltip='Export to CSV',
        icon='check')    
    
    list_of_buttons = [widget_dict['button_no_growth'],
                       widget_dict['button_linear_growth'],
                       widget_dict['button_3yr_growth'],
                       widget_dict['button_4yr_growth']]
    widget = widgets.HBox(list_of_buttons)
    return widget_dict, widget


data_export_button_dict, button_panel = data_export_widget()

def on_button_clicked_no_growth(b):
    model_no_growth.summary_matrix.to_csv('no_growth_summary.csv', index=False, header=True)

def on_button_clicked_linear_growth(b):
    model_linear_growth.summary_matrix.to_csv('linear_growth_summary.csv', index=False, header=True)

def on_button_clicked_3yr_growth(b):
    model_3yr_growth_rate.summary_matrix.to_csv('3yr_growth_summary.csv', index=False, header=True)
    
def on_button_clicked_4yr_growth(b):
    model_4yr_growth_rate.summary_matrix.to_csv('4yr_growth_summary.csv', index=False, header=True)
    
    
data_export_button_dict['button_no_growth'].on_click(on_button_clicked_no_growth)    
data_export_button_dict['button_linear_growth'].on_click(on_button_clicked_linear_growth)    
data_export_button_dict['button_3yr_growth'].on_click(on_button_clicked_3yr_growth)    
data_export_button_dict['button_4yr_growth'].on_click(on_button_clicked_4yr_growth)    

