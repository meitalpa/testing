import pandas as pd
import dash
import dash_html_components as html
import base64
from facets_overview.generic_feature_statistics_generator import GenericFeatureStatisticsGenerator


DEBUG = True
data = pd.read_csv("dataset.csv")
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
gfsg = GenericFeatureStatisticsGenerator()
proto = gfsg.ProtoFromDataFrames([{'name': 'train', 'table': data}])
protostr = base64.b64encode(proto.SerializeToString()).decode("utf-8")

app = dash.Dash('')

app.layout = html.Div(children=[
    html.Iframe(
        width="1200",
        height="800",
        srcDoc= """
       <script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/1.3.3/webcomponents-lite.js"></script>
        <link rel="import" href="https://raw.githubusercontent.com/PAIR-code/facets/1.0.0/facets-dist/facets-jupyter.html" >
        <facets-overview id="elem"></facets-overview>
        <script>
          document.querySelector("#elem").protoInput = "{protostr}";
        </script>""".format(protostr=protostr)
    ),
])
server = app.server

if __name__ == '__main__':
    app.run_server(debug=DEBUG)
