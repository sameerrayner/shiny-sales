from shiny.express import input,ui
from shinywidgets import render_altair
from shinyswatch import theme
import pandas as pd
import altair as alt

df = pd.read_csv('Sales.csv')

with ui.sidebar():
    ui.input_selectize(id ='var', 
                        label ='Select Variable', 
                        choices =['Product Category','Order Status','Payment Method'],
                        width = '100%')
    
    ui.input_radio_buttons(id ='measure',
                           label ='Select Measure',
                           choices =['Number of Orders', 'Sum of Sales'])


ui.page_opts(title = 'Adventure Works Sales', theme = theme.sketchy)


@render_altair
def col():
    title = alt.TitleParams(f'Adventure Works Sales by {input.var()}')
    if input.measure() == 'Number of Orders':
        return(
            alt.Chart(data = df, title = title).mark_bar(cornerRadius=2, color='#bed3e1').encode(
                y=alt.Y(f'{input.var()}:N'), x=alt.X('count()').title('Number of Orders'))
                )
    else:
        return(
            alt.Chart(data = df, title = title).mark_bar(cornerRadius=2, color='#bed3e1').encode(
                y=alt.Y(f'{input.var()}:N'), x=alt.X('sum(Order Total)').title('Sum of Sales (USD)'))
                )