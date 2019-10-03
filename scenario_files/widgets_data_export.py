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
        description='Export Scenario 1',
        disabled=False,
        button_style='',
        tooltip='Export to CSV',
        icon='check')
    widget_dict['button_linear_growth'] = widgets.Button(
        description='Export Scenario 2',
        disabled=False,
        button_style='',
        tooltip='Export to CSV',
        icon='check')
    widget_dict['button_3yr_growth'] = widgets.Button(
        description='Export Scenario 3',
        disabled=False,
        button_style='',
        tooltip='Export to CSV',
        icon='check')
   
    
    list_of_buttons = [widget_dict['button_no_growth'],
                       widget_dict['button_linear_growth'],
                       widget_dict['button_3yr_growth']]
    widget = widgets.HBox(list_of_buttons)
    return widget_dict, widget




