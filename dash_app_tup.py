import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
	html.H1("Dragos's dash app",
		style= {
			'textAlign' : 'center',
			#'color' : '#ffff'
		}),
	html.Div('Dash - Bla bla bla'),

	dcc.Graph(
		id= 'sample-graph',
		figure= {
			'data': [
				{'x': [4,6,8], 'y' : [12,16,18], 'type': 'bar', 'name': 'First Chart'},
				{'x': [4,6,8], 'y' : [20,24,26], 'type': 'bar', 'name': 'Second Chart'}
			],
			'layout' : {
				#'plot_bcolor' : '#D3D3D3',
				#;paper_bcolor' : '#00FFFF',
				#'font' : {
				#	'color' : '#ff0000'
				# },
				'title': 'simple bar char'
			}
		}
	)
])
if __name__ == '__main__':
	app.run_server(port=4050)