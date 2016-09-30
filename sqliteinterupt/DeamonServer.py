from DeamonInterface import DeamonInterface;

class DeamonServer(DeamonInterface):

    def __init__(self, inputport, inputip):
        self.port = inputport;
        self.ip = inputip;

    #def connect(self):

