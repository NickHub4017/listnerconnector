from inputDeamonFactory import inputDeamonFactory

factory=inputDeamonFactory()
inputdeamon=factory.getinputDeamon("client")

if(inputdeamon.connect()):
    inputdeamon.getdata()
