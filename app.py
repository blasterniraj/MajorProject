# Dash App
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Interactive Disaster Data Analysis & Prediction"),
    
    html.Div([
        dcc.Dropdown(
            id='disaster-type',
            options=[{'label': i, 'value': i} for i in data_cleaned['Disaster_Type'].unique()],
            placeholder='Select Disaster Type'
        ),
        dcc.DatePickerRange(
            id='date-range',
            start_date=data_cleaned['Date'].min(),
            end_date=data_cleaned['Date'].max()
        ),
        dcc.Input(id='latitude', type='number', placeholder='Latitude'),
        dcc.Input(id='longitude', type='number', placeholder='Longitude'),
        dcc.Input(id='magnitude', type='number', placeholder='Magnitude'),
        dcc.Input(id='depth', type='number', placeholder='Depth'),
        dcc.Input(id='wind_speed', type='number', placeholder='Wind Speed'),
        dcc.Input(id='rainfall', type='number', placeholder='Rainfall'),
        dcc.Input(id='temperature', type='number', placeholder='Temperature'),
        dcc.Input(id='humidity', type='number', placeholder='Humidity'),
        dcc.Input(id='historical_freq', type='number', placeholder='Historical Frequency'),
        html.Button('Predict', id='predict-button')
    ]),
    
    html.Div([
        html.Div(id='output-prediction', style={'margin-top': '20px'}),
        html.Div(id='output-map', style={'margin-top': '20px'}),
    ])
])

@app.callback(
    Output('output-prediction', 'children'),
    [Input('latitude', 'value'),
     Input('longitude', 'value'),
     Input('magnitude', 'value'),
     Input('depth', 'value'),
     Input('wind_speed', 'value'),
     Input('rainfall', 'value'),
     Input('temperature', 'value'),
     Input('humidity', 'value'),
     Input('historical_freq', 'value')]
)
def predict_disaster(lat, lon, mag, depth, wind, rain, temp, hum, freq):
    if None in [lat, lon, mag, depth, wind, rain, temp, hum, freq]:
        return "Enter all inputs to predict!"
    else:
        new_data = pd.DataFrame({
            'Latitude': [lat], 'Longitude': [lon], 'Magnitude': [mag],
            'Depth': [depth], 'Wind_Speed': [wind], 'Rainfall': [rain],
            'Temperature': [temp], 'Humidity': [hum], 'Historical_Frequency': [freq]
        })
        prediction = best_model.predict(new_data)
        return f"Predicted Disaster Type: {prediction[0]}"

if __name__ == '__main__':
    app.run_server(debug=True)
