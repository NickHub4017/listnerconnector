import sys
import getopt
import sys
import os


from ConfigClient.PnpConfig import updatedata
from initdb import initdbclass
def usage():
    print "-d --help"
    print "-d --conip <ip> controldeamonIP"
    print "-d --conport <port> controldeamonPort"
    print "-d--contype <type> controldeamontype"
    print "-d --contproto <type> controldeamonprotocol"
    print "-d --inpip <ip> inputdeamonIP"
    print "-d --inport <port> inputdeamonPort"
    print "-d --inptype <type> inputdeamontype"
    print "-d --inpproto <type> inputdeamonprotocol"
    print "-d --outip <ip> outputdeamonIP"
    print "-d --outport <port> outputdeamonPort"
    print "-d --outtype <type> outputdeamontype"
    print "-d --outproto <type> outputdeamonprotocol"
    print "-d --loadfile <filename>  loadconfigdata form file"
    print "-t view all programs which use the current port needed"
    print "-r remove all intermidate files and database. Databse will recreate with the config file"
    print "-f loadconfig file loacted at the same as this python file"
    print "-b get database values"
    print "-k kill the current instance of Pnp -Warning Files maybe kept locked"

def processCleanUp():
    tmp = os.popen("ps aux").read()
    pslist=[]
    #print tmp
    for line in tmp.split("\n"):
        x=1
        line=line.strip()
        procdata=line.split(" ")
        for c in range(0,procdata.count('')):
            procdata.remove('')
        #print procdata
        try:
            if("controldeamon.py" in procdata[11]):
                try:
                    pslist.append(int(procdata[1]))
                except Exception as e:
                    print "Error occured in init process cleanup:- "+e.message
        except Exception as e:
            pass
    #print pslist
    for p in pslist:
        try:
            if(os.getpid()!=p):
                print p,os.getpid()
                os.kill(p,9)
        except Exception as e:
            print "Error occured in init process cleanup (Killing):- " + e.message


currentDb = initdbclass()

try:
    opts, args = getopt.getopt(sys.argv[1:], "hdbfrtk", ["help=", "conip=","conport=","contype=","inpip=","inport=","inptype=","outip=","outport=","outtype=","loadfile=","contproto=","inpproto=","outproto="])
    #print "Try"
except getopt.GetoptError as e:
    usage()
    sys.exit(2)



if(('-d','') in opts):
    for i in opts:
        # print i
        updatedata(i[0], i[1])

elif(('-b','') in opts):
    currentDb.getAlldebug()

elif(('-f','') in opts):
    pathoffile = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.yml"))
    updatedata("--loadfile",pathoffile )

elif(('-r','') in opts):
    try:
        os.remove("/tmp/pnp.db");
    except:
        pass
    try:
        os.remove("/tmp/inppipe");
    except:
        pass
    try:
        os.remove("/tmp/outpipe");
    except:
        pass

    pathoffile = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.yml"))
    updatedata("--loadfile", pathoffile)
    print "/tmp/pnp.db was deleted and recreate with config.yml's data"


elif(('-t','') in opts):
    datarow = currentDb.getnodedata("cntrldeamon");
    controlport = str(datarow[3])
    tmp = os.popen("netstat -nlp | grep "+controlport).read()
    tmp=tmp.split(" ")
    for c in range(0, tmp.count('')):
        tmp.remove('')
    print tmp,"\n-----------------ControlDeamon--------------------------\n"

    datarow = currentDb.getnodedata("inpdeamon");
    inputport=str(datarow[3])
    tmp = os.popen("netstat -nlp | grep "+inputport).read()
    tmp=tmp.split(" ")
    for c in range(0, tmp.count('')):
        tmp.remove('')
    print tmp,"\n-----------------InputDeamon--------------------------\n"

    datarow = currentDb.getnodedata("oudeamon");
    outport=str(datarow[3])
    tmp = os.popen("netstat -nlp | grep "+outport).read()
    tmp=tmp.split(" ")
    for c in range(0, tmp.count('')):
        tmp.remove('')
    print tmp,"\n-----------------OutputDeamon--------------------------\n"

elif(('-k','') in opts):
    processCleanUp()