class DeamonInterface():
    port=8080;
    ip="127.0.0.1";

    def __init__(self):
        print "Deamon Server initiated"

    def connect(self):
        print "Connecting"