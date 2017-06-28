# feedforward


class neuron:
    def __init__(self,w,b):
        self.w=w
        self.b=b

    def feedforward(self,input):
    #output y = f(wx+b)

        lamda = self.w*input +self.b
        return self.getAct(lamda)
    def getAct(self,x):
        return max(0.0,x)

neuron = neuron(2.0,1.0)
print ('input 1.0 -> output {}'.format(neuron.feedforward(1.0)))
print ('input 2.0 -> output {}'.format(neuron.feedforward(2.0)))