import plotly.graph_objects as go
import chart_studio.plotly as py

celdas=['A', 'B', 'C']
valores = [20, 14, 23]

colores = ['dodgerblue','tomato','yellow']

fig = go.Figure(data=
    [go.Bar(
        x=celdas, 
        y=valores,
        text=valores,
        textposition='auto',
        marker_color=colores)])
fig['layout']['yaxis1'].update(title='Valores', range=[0, 30], autorange=False)
fig['layout']['xaxis'].update(title='Valores X')
fig.update_layout(title_text='Reporte')

#fig.write_html("hola.html")

py.plot(fig, filename='test')


