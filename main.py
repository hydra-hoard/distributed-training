# get number of deivces and model to run on

# train !

class Device:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

d1 = Device(1,1)
d2 = Device(1,2)

devices = [d1,d2]

def processingTime(d):

def computePingTime(d1, d2):
    


def computeLatencyTime(devices):
    for d in devices:
        pingTimes = []
        for e in devices:
            t = computePingTime(d,e)
            pingTimes.append(t)
        times.append(pingTimes)
    
    return times

def computeProcessingTime(devices):
    processing = []
    for d in devices:
        score = processingTime(d)
        processing.append(score)
    
    return processing