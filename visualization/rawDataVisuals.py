import pandas
import plotly.express as px
import chart_studio.plotly as py
import chart_studio
import chart_studio.tools as tls
import plotly.io as pio

def displayHeatmap():
    pandas.set_option('display.precision', 9)

    data = pandas.read_csv("results.csv")

    print((data["Lat"][1]))

    fig = px.density_mapbox(data, z = "Download Speed", lat = "Lat", lon = "Lon", hover_name = "Date", hover_data = ["ConnType", "Download Speed", "Download Size", "Upload Speed", "Upload Size", "Latency"], color_continuous_scale=px.colors.sequential.Rainbow, zoom = 7, height = 500)
    fig.update_layout(mapbox_style = "open-street-map")
    fig.update_layout(margin = {"r":0,"t":0,"l":0,"b":0})
    fig.show()
    pandas.get_option('display.precision')

    username = 'ttaylor22' # your username
    api_key = 'g6dHWkJagRFbh9ou1jHC' # your api key - go to profile > settings > regenerate key
    chart_studio.tools.set_credentials_file(username = username, api_key = api_key)
    py.plot(fig, filename = 'droneHeatmap', auto_open=True)

    tls.get_embed('https://plotly.com/~ttaylor22/1') #change to your url

    pio.write_html(fig, file='index.html', auto_open=True)
    
if __name__ == '__main__':
    displayHeatmap()