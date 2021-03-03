from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

infile = open('US_fires_9_1.json', 'r')

fire_data = json.load(infile)

brights, lons, lats = [], [], []

for fire in fire_data:
    bright = fire["brightness"]
    lon = fire["longitude"]
    lat = fire["latitude"]
    if bright > 450:
        brights.append(bright)
        lons.append(lon)
        lats.append(lat)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [15 % bright for bright in brights],
        'color':brights,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Brightness'}
    }
}]

my_layout = Layout(title="US Fires - 9/1/2020 through 9/13/2020")

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='global_fires(1-13).html')
