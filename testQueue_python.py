import math
from queue import Queue
import operator
import json
#impedance = [400, 100, math.inf] #case1
#impedance = [12, 24, 6]#case2
impedance = [0, 400, 40, math.inf]#case3
time= [0, 1.5, 2]
vp= 1

Junction_num = len(impedance)-1

node_list = []
node_list_plot = []
node_list_print = []
queue = Queue(maxsize=400)

Tau_V1_2 = []
Tau_V2_1 = []
Rau_V1_2 = []
Rau_V2_1 = []


# calculate reflection and transmittion coeffecient
for i in range(Junction_num):
    try:
        if (i==0):
            t1_2=1
            t2_1=0
            r1_2=0
            r2_1=-1
        else :
            t1_2 = 2 / (1+(impedance[i]/impedance[i+1]))
            t2_1 = 2 / (1+(impedance[i+1]/impedance[i]))
            r1_2 = t1_2-1
            r2_1 = t2_1-1
    except:
        if (i==0):
            t1_2=1
            t2_1=0
            r1_2=0
            r2_1=-1
        else :
            t1_2 = (2*((impedance[i+1])/(impedance[i]+impedance[i+1])))
            t2_1 = (2*((impedance[i])/(impedance[i]+impedance[i+1])))
            r1_2 = t1_2-1
            r2_1 = t2_1-1
    Tau_V1_2.append(t1_2)
    Rau_V1_2.append(r1_2)
    Tau_V2_1.append(t2_1)
    Rau_V2_1.append(r2_1)

print("Tau_V1_2")
print(Tau_V1_2)
print("Rau_V1_2")
print(Rau_V1_2)

print("Tau_V2_1")
print(Tau_V2_1)
print("Rau_V2_1")
print(Rau_V2_1)


# init
Vinst = {"Junction": 1,"dir": 0, "time": 0, "volt": 1}
node_list.append(Vinst)
queue.put(Vinst)

# returns Transmitted voltage
def Vstamp_operate_Trans(Vstamp):
    V_trans_newInst = {"Junction": 1,"dir": 0, "time": 0, "volt": 0}
    V_trans_plot = {"Junction": 1, "time": 0, "volt": 0}
    # use Tau
    # update Dir
    V_trans_newInst["dir"] = Vstamp["dir"]
    #update time
    if (Vstamp["dir"] == 0):
        V_trans_newInst["time"] = Vstamp["time"]+time[Vstamp["Junction"]-1]
    else:
        V_trans_newInst["time"] = Vstamp["time"]+time[Vstamp["Junction"]]    
    # update Type

    # update Volt and update Junction
    # Choose direction
    if (Vstamp["dir"] == 0):
        # update Junction
        V_trans_newInst["Junction"] = Vstamp["Junction"]+1
        # update Volt
        V_trans_newInst["volt"] = Vstamp["volt"]*Tau_V1_2[Vstamp["Junction"]-1]
    else:
        # update Junction
        V_trans_newInst["Junction"] = Vstamp["Junction"]-1
        # update Volt
        V_trans_newInst["volt"] = Vstamp["volt"]*Tau_V2_1[Vstamp["Junction"]-1]

    if (V_trans_newInst["dir"] == 0):
        V_trans_plot['Junction']= V_trans_newInst["Junction"]-1
    else: 
        V_trans_plot["Junction"] = V_trans_newInst["Junction"]+1
    V_trans_plot["time"] = V_trans_newInst["time"]
    V_trans_plot["volt"] = V_trans_newInst["volt"]    
    node_list_plot.append(V_trans_plot)   
    # update Time

    # return new inst
    return V_trans_newInst



# returns reflected voltage
def Vstamp_operate_Ref(Vstamp):
    V_ref_newInst = {"Junction": 1, "dir": 0, "time": 0, "volt": 0}
    # use Rau
    # update Dir
    V_ref_newInst["dir"] = 1 ^ (Vstamp["dir"])
    #update time
    if (Vstamp["dir"] == 0):
        V_ref_newInst["time"] = Vstamp["time"]+time[Vstamp["Junction"]-1]
    else:
        V_ref_newInst["time"] = Vstamp["time"]+time[Vstamp["Junction"]]    
    # update Type

    # update Volt and update Junction
    # Choose direction
    if (Vstamp["dir"] == 0):
        # update Junction
        V_ref_newInst["Junction"] = Vstamp["Junction"]-1
        # update Volt
        V_ref_newInst["volt"] = Vstamp["volt"]*Rau_V1_2[Vstamp["Junction"]-1]
    else:
        # update Junction
        V_ref_newInst["Junction"] = Vstamp["Junction"]+1
        # update Volt
        V_ref_newInst["volt"] = Vstamp["volt"]*Rau_V2_1[Vstamp["Junction"]-1]

    # update Time

    # return new inst
    return V_ref_newInst


i = 0
# not(queue.empty())
while(i<25):
    i += 1
    print(f"i:{i}")
    # remove first element and store first elemnt in the queue
    try:
        element1 = queue.get_nowait()
        print("print element to work on")
        print(element1)

        # calculate Vtrans,Vreflecte
        Vtrans = Vstamp_operate_Trans(element1)
        Vref = Vstamp_operate_Ref(element1)
        if(Vtrans["Junction"] >= 1 and Vtrans["Junction"] <= Junction_num):
            # Add to queue
            print("Put Vtrans:")
            print(Vtrans)
            queue.put(Vtrans)
        else: #to update related node
            if(Vtrans["Junction"] > Junction_num):
                Vtrans["Junction"] -=1
                Vtrans["dir"] =1
            else:
                Vtrans["Junction"] +=1
                Vtrans["dir"] =0
        if(Vref["Junction"] >= 1 and Vref["Junction"] <= Junction_num):
            # Add to queue
            print("Put Vref:")
            print(Vref)
            queue.put(Vref)
        else: #to update related node
            if(Vref["Junction"] > Junction_num):
                Vref["Junction"] -=1
            else:
                Vref["Junction"] +=1
                Vref["dir"] =0
        # update nodes list
        print("add to node")
        node_list.append(Vtrans)
        node_list.append(Vref)

        # # remove first element
        print("print what to remove")
        print(element1)
    except:
        print("queue no element")

    print("\n")

print("print node list")
for i in range(1,Junction_num+1):
    for element in node_list_plot: 
        if (element["Junction"] == i):
            node_list_print.append(element)  
    node_list_print.sort(key=lambda node: node["time"])
    #print(node_list_print)
    print(json.dumps(node_list_print, indent=4))
    print("\n")
    print("####################################################################")
    node_list_print.clear()        


# categorize list for every Junction
# print every Junction alone
#print("print node list")
#sorted_list=sorted(node_list,)
#node_list.sort(key=operator.itemgetter('Junction'))
#print(node_list)
#print(json.dumps(node_list, indent=4))
#node_list_plot.sort(key=operator.itemgetter('Junction'))
#print(json.dumps(node_list_plot, indent=4))
