# feedforward


class neuron:
    def __init__(self,w,b):
        self.w=w
        self.b=b

    def feedforward(self,input):
    #output y = f(wx+b)

        lamda = self.w*input +self.b
        output = self.getAct(lamda)
        self.input  = input
        self.output = output

        return output

    def getAct(self,x):
        return max(0.0,x)

    def getActgrad(self,x):
        if x>0.0:
            return x
        else:    
            return 0.0

    def propbackword(self,target):
        a=0.1
        self.w = self.w - a*(self.output-target)*self.getActgrad(self.output)*self.input
        self.b = self.b - a*(self.output-target)*self.getActgrad(self.output)

neuron = neuron(2.0,1.0)

# print ('input 1.0 -> output {}'.format(neuron.feedforward(1.0)))
# print ('input 2.0 -> output {}'.format(neuron.feedforward(2.0)))
for i in range(1,100):
    print ('input 1.0 -> output{}'.format(neuron.feedforward(1.0)))
    neuron.propbackword(4.0)
