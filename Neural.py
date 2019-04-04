import numpy as np
import matplotlib.pyplot as plt
from Draw import Draw

class Neural:

    def __init__ (self, array_input, array_output):
        self.array_input =  np.asarray(array_input)
        self.array_output = np.asarray(array_output)
        self.array_weight = self.InitWeights(len(array_input[0]))
        self.array_error = []

    def InitWeights(self, amount_inputs):
        return np.asarray(np.random.rand(amount_inputs, 1))

    def Start(self, THETA, tolerancia, etha, error, draw = ''):
        while (error >= tolerancia):
            #Get products and function activate's values
            produc_values = np.dot(self.array_input, self.array_weight)
            result_function_activation = self.Hardlim (produc_values)

            #Update weigth
            error = self.GetDifference(result_function_activation)
            DW =np.array([ etha * np.dot(self.array_input.transpose(), error)]).transpose()
            self.array_weight = self.array_weight + DW;
            error = self.GetEuclideanNorm(error)
            self.array_error.append(error)

        #Draw AND
        if(draw == 'AND'):
            Draw.Draw_AND_LineChart(self.array_weight, self.array_input)
        elif(draw == 'OR'):
            Draw.Draw_OR_LineChart(self.array_weight, self.array_input)
        elif(draw == 'XOR'):
            Draw.Draw_XOR_LineChart(self.array_weight)

    def Hardlim(self, array_product):
        lenght_input, data = len(array_product), []
        for i in range(lenght_input):
            values = array_product[i]
            if(values > 0):
                data.append(1)
            else:
                data.append(0)
        return data

    def GetDifference(self, result_function_activation):
        new_list, size_array_output = [], len(self.array_output)
        for i in range(size_array_output):
            new_list.append(self.array_output[i] - result_function_activation[i])
        return new_list

    def GetEuclideanNorm(self, array_error):
        size_array_error, result = len(array_error), 0
        for i in range(size_array_error):
            result += array_error[i] ** 2
        return result