import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np



#1. Define application
app=dash.Dash(__name__)
application=app.server


#2. Define styles
styles = {
    'pre': {
        'border': 'thin lightgrey solid',

    }
}
#3. Layout (Exoskeleton)
app.layout  = html.Div([html.Div(
        [
            dcc.Markdown(
                '''
                ### Exploring the Fibonacci sequence using a python function and dashboard
                The below visualization shows the calculation of the Fibonacci spiral (golden spiral) up to 15 number inputs. 
                For the code, please visit my [github]("https://github.com/kanishkan91/Py-Dash-GlobalDisplacementswithHoverFunctionality") page.
                Use the slider under the spiral map to change the digits used in the fibonacci function. The text to the right explains the code used and the updates to the fibonacci code.
                '''.replace('  ', ''),
                className='eight columns offset-by-three'
            )
        ],className='row',
        style={'text-align': 'center', 'margin-bottom': '20px'}
    ),

    html.Div([
    dcc.Graph(id='graph-with-slider',style={'height':600}
              ),
              dcc.Slider(id='slider',
                         min=3,
                         max=15,
                         value=3,
                         marks={'3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
                                '8': '8', '9': '9', '10': '10', '11': '11', '12': '12','13': '13','14': '14','15': '15'}
                         )
],style={'width': '69%', 'float': 'left', 'display': 'inline-block','font':'15','height':'50%'}),
dcc.Textarea(
    placeholder='Enter a value...',
    value=''
          'Actual code used in the calculation of the fibonacci sequence-'
          ''
          ''
          ''
          'The fibonacci function is calculated using the below code,'
          ''
          ''
          '''
        def Fibonacci(signature, n):
        r = len(signature)
        if n < len(signature):
            signature = signature[:len(signature) - (len(signature) - n)]
        else:
            for _ in range(n - r):
                s = sum(signature[-r:])
                signature.insert(len(signature) + 1, s)

        return signature'''''   ,
    style={'display': 'inline-block', 'width': '30%', 'float': 'right','height':'150px'}
),
html.Br(),
html.Br(),
html.Div(id='result',style={'display': 'inline-block', 'width': '30%', 'float': 'right','height':'50px','font':'20'}),
html.Div(id='result2',style={'display': 'inline-block', 'width': '30%', 'float': 'right','height':'50px'}),
html.Div(dcc.Textarea(
    placeholder='Enter a value...',
    value=
          'What is the Fibonacci Sequence?'
          '''
          
          The fibonacci sequence is basically a sequence of numbers formed such that each number is the sum of the 2 preceding ones.The sequence forms the so called golden ratio and the golden spiral (described in the visualization).
          The sequence occurs in biological settings as well, such as branching in trees, arrangement of leaves on a stem, hurricanes.As a great man once said "We will ride the spiral to the end and may just go where no one has been"'''
          '''
        '''''   ,
    style={'display': 'inline-block', 'width': '30%', 'float': 'right','height':'150px'}
))
])

#4. Define First callback
@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('slider', 'value')])

def update_figure(selected_value):
    def Fibonacci(signature, n):
        r = len(signature)
        if n < len(signature):
            signature = signature[:len(signature) - (len(signature) - n)]
        else:
            for _ in range(n - r):
                s = sum(signature[-r:])
                signature.insert(len(signature) + 1, s)

        return signature

    r=Fibonacci([1,2],selected_value)

    finalR = []
    for i in r:
        a = i * np.pi
        finalR.append(a)

    max2 = int(max(r))
    min2 = int(min(r))
    len2 = len(r)
    r2 = []
    for i in range(0, max2):
        r2.append(i)

    min1 = int(min(finalR))
    max1 = int(max(finalR))

    ForTheGraph = [i for i in np.linspace(min1, max1, len(r2))]

    data = [
        go.Scatterpolar(
            r=r,
            theta=finalR,
            mode='markers+text',
            text=r,
            textposition='top left',
            textfont=dict(
                size=10
            ),
            marker=dict(
                color='peru'
            )
        )

        ,
        go.Scatterpolar(
            r=r2,
            theta=ForTheGraph,
            mode='lines',
            marker=dict(
                color='peru'
            )
        )
    ]

    layout = go.Layout(
        showlegend=False
    )

    return {
        'data':data,
        'layout':layout
    }
#5. Define second callback
@app.callback(
    dash.dependencies.Output('result', 'children'),
    [dash.dependencies.Input('slider', 'value')
     ]
)
def update_result(value):
    def Fibonacci(signature, n):
        r = len(signature)
        if n < len(signature):
            signature = signature[:len(signature) - (len(signature) - n)]
        else:
            for _ in range(n - r):
                s = sum(signature[-r:])
                signature.insert(len(signature) + 1, s)

        return signature

    r=Fibonacci([1,2],value)
    el=r[-1]



    return "The next number in the Fibonacci sequence is: {}".format(el)

#5. Define third callback
@app.callback(
    dash.dependencies.Output('result2', 'children'),
    [dash.dependencies.Input('slider', 'value')
     ]
)
def update_result(value):
    def Fibonacci(signature, n):
        r = len(signature)
        if n < len(signature):
            signature = signature[:len(signature) - (len(signature) - n)]
        else:
            for _ in range(n - r):
                s = sum(signature[-r:])
                signature.insert(len(signature) + 1, s)

        return signature

    r=Fibonacci([1,2],value)

    return "Therefore the updated Fibonacci sequence is: {}".format(r)



if __name__ == '__main__':
    application.run_server(debug=True)
