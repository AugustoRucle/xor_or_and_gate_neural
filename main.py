from Neural import Neural
from Draw import Draw

THETA = 1
tolerancia = 0.00005
etha = 1
error = 2 * tolerancia

# Input
# [ value_theta, value_and, value_and ]
input_values = [[1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 1, 1]]

# Output
output_values =  [0 , 1, 1, 0]

neural = Neural(input_values, output_values)
neural.Start(THETA, tolerancia, etha, error, 'XOR')
Draw.Draw_Error_LineChart(neural.array_error)