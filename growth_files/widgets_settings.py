from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from IPython.core.display import Javascript
from IPython.display import display
import pyugend2
import time
import pandas as pd
import datetime
import math
import builtins
from IPython.lib import deepreload
builtins.reload = deepreload.reload
import warnings
warnings.filterwarnings('ignore')
from fitter import Fitter
import numpy as np


## Default values

default_numbers_mgmt = {'f1': 2,
                       'f2': 3,
                       'f3':3,
                       'm1':11,
                       'm2':13,
                       'm3':42}

default_attrition_rate_mgmt = {'f1': 0.0615,
                       'f2': 0.00,
                       'f3':0.0600,
                       'm1':0.0859,
                       'm2':0.0473,
                       'm3':0.0414}
                        
default_hiring_rate_mgmt = {'f1': round(14/68, 3),
                       'f2': round(4/68, 3),
                       'f3': round(0/68, 3),
                       'm1': round(36/68, 3),
                       'm2': round(8/68, 3),
                       'm3': round(6/68, 3)}

default_promotion_rate_mgmt = {'f1': 0.0769,
                       'f2': 0.1111,
                       'f3':0.0,
                       'm1':0.0707,
                       'm2':0.0946,
                       'm3':0.0}
    
default_model_settings = {'duration':20,
                          'lowerbound': 64,
                          'upperbound':84,
                          'variation_range':3,
                          't_fpct': 0.25} 

# Create common professor labels
prof_labels = {'f1': 'Women Assistant Professors',
              'f2': 'Women Associate Professors',
              'f3': 'Women Full Professors',
              'm1': 'Men Assistant Professors',
              'm2': 'Men Associate Professors',
              'm3': 'Men Full Professors'}

widget_sequence = ['f1','f2','f3','m1','m2','m3']

style = {'description_width': 'initial'}
def widget_panel(labels,default_values, number_type):
    dict = {}
    if number_type == 'integer':
        for k,v in labels.items():
            dict[k] = widgets.IntText(value = default_values[k],
                                     description= v,
                                     disabled = False,
                                     style=style)
            dict['default_'+k] = widgets.Label(value = 'default value: ' + str(default_values[k]))
        widget_left = widgets.VBox([dict[k] for k in widget_sequence])
        widget_right = widgets.VBox([dict['default_'+k] for k in widget_sequence])
        widget = widgets.HBox([widget_left, widget_right])

    if number_type == 'float':
        for k,v in labels.items():
            dict[k] = widgets.FloatText(value = default_values[k],
                                     description= v,
                                     disabled = False,
                                     min = 0,
                                     max = 1,
                                     step = 0.01,
                                     style=style)
            dict['default_'+k] = widgets.Label(value = 'default value: ' + str(default_values[k]))

            initial_average = round(np.mean([default_values[k] for k in widget_sequence]), 4)
            dict['avgll'] = widgets.HTML(value = 'Average rate: ')
            dict['avgl'] = widgets.HTML(value = str(initial_average))
            dict['davgll'] = widgets.HTML(value='Default average rate: ')
            dict['davgl'] = widgets.HTML(value=str(initial_average))

        widget_left = widgets.VBox([dict[k] for k in widget_sequence] + [dict['davgll'], dict['avgll']])
        widget_right = widgets.VBox([dict['default_'+k] for k in widget_sequence]+ [dict['davgl'], dict['avgl']])
        widget = widgets.HBox([widget_left, widget_right])
    return dict,widget

numbers_dict, numbers_widget = widget_panel(prof_labels,default_numbers_mgmt,'integer')
attrition_dict, attrition_widget = widget_panel(prof_labels,default_attrition_rate_mgmt,'float')
hiring_dict, hiring_widget = widget_panel(prof_labels,default_hiring_rate_mgmt,'float')
promotion_dict, promotion_widget = widget_panel(prof_labels,default_promotion_rate_mgmt,'float')

## Model Settings Widget



model_settings_dict = {'lowerbound': widgets.IntText(value = default_model_settings['lowerbound'],
                                                description = 'Department Size Lowerbound',
                                                disabled = False,
                                                style = style),
                  'upperbound': widgets.IntText(value = default_model_settings['upperbound'],
                                                description = 'Department Size Upperbound',
                                                disabled = False,
                                                style = style),
                  'variation_range': widgets.IntText(value = default_model_settings['variation_range'],
                                                description = 'Department Size Churn Range',
                                                disabled = False,
                                                style = style),
                  'duration': widgets.IntText(value = default_model_settings['duration'],
                                                description = 'Simulation Duration',
                                                disabled = False,
                                                style = style),
                  'target_percentage_women': widgets.FloatText(value = default_model_settings['t_fpct'],
                                                description = 'Target Women Faculty Percentage',
                                                disabled = False,
                                                min = 0,
                                                max = 1.0,
                                                step = 0.01,
                                                style = style),
                  'default_lowerbound': widgets.Label(value = 'default value: ' + str(default_model_settings['lowerbound'])),
                  'default_upperbound': widgets.Label(value = 'default value: ' + str(default_model_settings['upperbound'])),
                  'default_variation_range': widgets.Label(value = 'default value: ' + str(default_model_settings['variation_range'])),
                  'default_target_percentage_women': widgets.Label(value = 'default value: ' + str(default_model_settings['t_fpct'])),
                  'default_duration': widgets.Label(value = 'default value: ' + str(default_model_settings['duration'])),                 
                   }

model_settings_left = widgets.VBox([model_settings_dict['duration'],
                                    model_settings_dict['lowerbound'],
                                    model_settings_dict['upperbound'],
                                    model_settings_dict['variation_range'],
                                    model_settings_dict['target_percentage_women']])

model_settings_right = widgets.VBox([model_settings_dict['default_duration'],
                                     model_settings_dict['default_lowerbound'],
                                     model_settings_dict['default_upperbound'],
                                     model_settings_dict['default_variation_range'],
                                     model_settings_dict['default_target_percentage_women']])

model_settings_widget= widgets.HBox([model_settings_left, model_settings_right])



#Widget for growth settings

def growth_widget_panel(duration):
    style = {'description_width': 'initial'}
    widget_dict = {}
    vbox_list = []
    # build linear growth widget
    widget_dict['label_linear_growth'] = widgets.Label(value = 'Linear Growth Annual Rate(decimal)')
    widget_dict['widget_linear_growth_rate'] = widgets.FloatText(value = 0.0167,
                                     description= '',
                                     disabled = False,
                                     min = 0,
                                     max = 0.5,
                                     step = 0.01,
                                     style=style)
    widget_dict['hbox_linear_growth_rate'] = widgets.HBox([widget_dict['label_linear_growth'],
                                         widget_dict['widget_linear_growth_rate']])

    vbox_list.extend([widget_dict['hbox_linear_growth_rate']])
    # build 3 year growth rate widget
    increments3 = math.ceil(duration/3)
    widget_dict['increment3'] = increments3
    widget_dict['hbox_label_increment3_section'] = widgets.HBox([widgets.Label(value='3 Year Growth Rates(decimal)')])
    vbox_list.extend([widget_dict['hbox_label_increment3_section']])
    
    for i in range(increments3):
        widget_dict['label_increment3_'+ str(i)] = widgets.Label(value='Rate')
        widget_dict['widget_increment3_' + str(i)] = widgets.FloatText(value = 0.0,
                                     description= '',
                                     disabled = False,
                                     min = 0,
                                     max = 1.0,
                                     step = 0.01,
                                     style=style)
        
        widget_dict['hbox_increment3_' + str(i)] = widgets.HBox([widget_dict['label_increment3_'+ str(i)],
                                                                 widget_dict['widget_increment3_' + str(i)]])
    increment_3_vbox_list = [widget_dict['hbox_increment3_' + str(i)] for i in range(increments3)]
    widget_dict['vbox_increment3'] = widgets.VBox(increment_3_vbox_list)
    vbox_list.extend([widget_dict['vbox_increment3']])
    
    # build 4 year growth rate widget

    increments4 = math.ceil(duration/4)
    widget_dict['increment4'] = increments4
    widget_dict['hbox_label_increment4_section'] = widgets.HBox([widgets.Label(value='4 Year Growth Rates(decimal)')])
    vbox_list.extend([widget_dict['hbox_label_increment4_section']])
    
    for i in range(increments4):
        widget_dict['label_increment4_'+ str(i)] = widgets.Label(value='Rate')
        widget_dict['widget_increment4_' + str(i)] = widgets.FloatText(value = 0.0,
                                     description= '',
                                     disabled = False,
                                     min = 0,
                                     max = 1.0,
                                     step = 0.01,
                                     style=style)
        
        widget_dict['hbox_increment4_' + str(i)] = widgets.HBox([widget_dict['label_increment4_'+ str(i)],
                                                                 widget_dict['widget_increment4_' + str(i)]])
    increment_4_vbox_list = [widget_dict['hbox_increment4_' + str(i)] for i in range(increments4)]
    widget_dict['vbox_increment4'] = widgets.VBox(increment_4_vbox_list)
    vbox_list.extend([widget_dict['vbox_increment4']])
    widget = widgets.VBox(vbox_list)
    return widget_dict, widget
    
growth_rate_dict, growth_rate_widget = growth_widget_panel(default_model_settings['duration'])

# Generic name constants
columns = ['Prof. Group',
           'Initial Number',
           'Attrition Rate',
           'Hiring Rate',
           'Promotion Rate']
row_labels = ['Women Assistant Professors',
              'Women Associate Professors',
              'Women Full Professors',
              'Men Assistant Professors',
              'Men Associate Professors',
              'Men Full Professors']

simulation_columns = ['Simulation Duration (years)',
                      'Department Size Lowerbound',
                      'Department Size Upperbound',
                      'Department Churn Range']


def display_model_settings():
    df = pd.DataFrame({'Prof. Group': row_labels,
                       'Initial Number': [numbers_dict[k].value for k in widget_sequence],
                       'Attrition Rate': [attrition_dict[k].value for k in widget_sequence],
                       'Hiring Rate': [hiring_dict[k].value for k in widget_sequence],
                       'Promotion Rate': [promotion_dict[k].value for k in widget_sequence]})
    df.set_index('Prof. Group')
    df = df[columns]
    out = widgets.Output()
    with out:
        display(df)

    return widgets.HBox([out])

def display_model_settings():
    df = pd.DataFrame({'Prof. Group': row_labels,
                       'Initial Number': [numbers_dict[k].value for k in widget_sequence],
                       'Attrition Rate': [attrition_dict[k].value for k in widget_sequence],
                       'Hiring Rate': [hiring_dict[k].value for k in widget_sequence],
                       'Promotion Rate': [promotion_dict[k].value for k in widget_sequence]})
    df.set_index('Prof. Group')
    df = df[columns]
    out = widgets.Output()
    with out:
        display(df)

    return widgets.HBox([out])

def display_model_settings_nowidget():
    df = pd.DataFrame({'Prof. Group': row_labels,
                           'Initial Number': [numbers_dict[k].value for k in widget_sequence],
                           'Attrition Rate': [attrition_dict[k].value for k in widget_sequence],
                           'Hiring Rate': [hiring_dict[k].value for k in widget_sequence],
                           'Promotion Rate': [promotion_dict[k].value for k in widget_sequence]})
    df.set_index('Prof. Group')
    df = df[columns]
    return df

def display_simulation_settings():
    df = pd.DataFrame({'Simulation Duration (years)': [model_settings_dict['duration'].value],
                       'Department Size Lowerbound': [model_settings_dict['lowerbound'].value],
                       'Department Size Upperbound': [model_settings_dict['upperbound'].value],
                       'Department Churn Range': [model_settings_dict['variation_range'].value]})
    df = df[simulation_columns]
    out = widgets.Output()
    with out:
        display(df)
    return widgets.HBox([out])


def display_model_choices():
    model_choices_list = [i for i in model_choice_widget_right.value]
    df = pd.DataFrame(model_choices_list, columns=['Model Names'])
    out = widgets.Output()
    with out:
        display(df)
    return widgets.HBox([out])


def display_growth_settings():
    model_dict = {}
    model_dict['label_linear_growth'] = widgets.Label(value='Linear Growth Rate:')
    model_dict['value_linear_growth'] = widgets.Label(value=str(growth_rate_dict['widget_linear_growth_rate'].value))
    model_dict['hbox_linear_growth'] = widgets.HBox([model_dict['label_linear_growth'],
                                                     model_dict['value_linear_growth']])
    model_dict['label_3yr_growth'] = widgets.Label(value='3 Year Growth Rates:')
    yr3_values = [growth_rate_dict['widget_increment3_' + str(i)].value for i in range(growth_rate_dict['increment3'])]
    model_dict['value_3yr_growth'] = widgets.Label(value=','.join(str(x) for x in yr3_values))
    model_dict['hbox_3yr_growth'] = widgets.HBox([model_dict['label_3yr_growth'],
                                                  model_dict['value_3yr_growth']])

    model_dict['label_4yr_growth'] = widgets.Label(value='4 Year Growth Rates:')
    yr4_values = [growth_rate_dict['widget_increment4_' + str(i)].value for i in range(growth_rate_dict['increment4'])]
    model_dict['value_4yr_growth'] = widgets.Label(value=','.join(str(x) for x in yr4_values))
    model_dict['hbox_4yr_growth'] = widgets.HBox([model_dict['label_4yr_growth'],
                                                  model_dict['value_4yr_growth']])
    return widgets.VBox([model_dict['hbox_linear_growth'],
                         model_dict['hbox_3yr_growth'],
                         model_dict['hbox_4yr_growth']])









