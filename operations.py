import globals 

class operation():

    def __init__(self):
        pass
      
    def calcInit():
        # calculate reflection and transmittion coeffecient
        for i in range(0,int(globals.junctionsNum)):
            try:
                if (i==100):
                    t1_2=1
                    t2_1=0
                    r1_2=0
                    r2_1=-1
                else :
                    t1_2 = 2 / (1+(globals.impedanceArray[i]  /globals.impedanceArray[i+1]))
                    t2_1 = 2 / (1+(globals.impedanceArray[i+1]/globals.impedanceArray[i]))
                    r1_2 = t1_2-1
                    r2_1 = t2_1-1
            except:
                if (i==100):
                    t1_2=1
                    t2_1=0
                    r1_2=0
                    r2_1=-1
                else :
                    t1_2 = (2*((globals.impedanceArray[i+1])/(globals.impedanceArray[i]+globals.impedanceArray[i+1])))
                    t2_1 = (2*((globals.impedanceArray[i])  /(globals.impedanceArray[i]+globals.impedanceArray[i+1])))
                    r1_2 = t1_2-1
                    r2_1 = t2_1-1
            globals.Tau_V1_2.append(t1_2)
            globals.Rau_V1_2.append(r1_2)
            globals.Tau_V2_1.append(t2_1)
            globals.Rau_V2_1.append(r2_1)

        Vinst = {"Junction": 1,"dir": 0, "time": 0, "volt": globals.Vp}
        globals.node_list.append(Vinst)
        globals.queue.put(Vinst)

    # returns Transmitted voltage
    def Vstamp_operate_Trans(Vstamp):
        V_trans_newInst = {"Junction": 1,"dir": 0, "time": 0, "volt": 0}
        V_trans_plot = {"Junction": 1, "time": 0, "volt": 0}
        # use Tau
        # update Dir
        V_trans_newInst["dir"] = Vstamp["dir"]
        #update time
        if (Vstamp["dir"] == 0):
            V_trans_newInst["time"] = Vstamp["time"]+globals.times[Vstamp["Junction"]-1]
        else:
            V_trans_newInst["time"] = Vstamp["time"]+globals.times[Vstamp["Junction"]]    
        # update Type
        # update Volt and update Junction
        # Choose direction
        if (Vstamp["dir"] == 0):
            # update Junction
            V_trans_newInst["Junction"] = Vstamp["Junction"]+1
            # update Volt
            V_trans_newInst["volt"] = Vstamp["volt"]*globals.Tau_V1_2[Vstamp["Junction"]-1]
        else:
            # update Junction
            V_trans_newInst["Junction"] = Vstamp["Junction"]-1
            # update Volt
            V_trans_newInst["volt"] = Vstamp["volt"]*globals.Tau_V2_1[Vstamp["Junction"]-1]
        if (V_trans_newInst["dir"] == 0):
            V_trans_plot['Junction']= V_trans_newInst["Junction"]-1
        else: 
            V_trans_plot["Junction"] = V_trans_newInst["Junction"]+1
        V_trans_plot["time"] = V_trans_newInst["time"]
        V_trans_plot["volt"] = V_trans_newInst["volt"]  
        globals.node_list_plot.append(V_trans_plot)   
        # update Lattice diagram
        # darwLatticeLine(V_trans_newInst["Junction"],V_trans_newInst["time"])

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
            V_ref_newInst["time"] = Vstamp["time"]+globals.times[Vstamp["Junction"]-1]
        else:
            V_ref_newInst["time"] = Vstamp["time"]+globals.times[Vstamp["Junction"]]    
        # update Type

        # update Volt and update Junction
        # Choose direction
        if (Vstamp["dir"] == 0):
            # update Junction
            V_ref_newInst["Junction"] = Vstamp["Junction"]-1
            # update Volt
            V_ref_newInst["volt"] = Vstamp["volt"]*globals.Rau_V1_2[Vstamp["Junction"]-1]
        else:
            # update Junction
            V_ref_newInst["Junction"] = Vstamp["Junction"]+1
            # update Volt
            V_ref_newInst["volt"] = Vstamp["volt"]*globals.Rau_V2_1[Vstamp["Junction"]-1]

        # update Time

        # return new inst
        return V_ref_newInst

    #draw window and junction lines #take juncNum,maxtime
    # def InitLatticeDiadg(self):
        #open new window with coordinates
        #draw junction lines
        pass

    #draw line with two nodes on the diaglog and junction lines #take junc,time
    # def darwLatticeLine(self,junc,time):
        #calculate ratio of junction max time
        #draw the line
        pass

    def calcNodes(iterationNum):
        global queue, node_list, junctionsNum
        j = 0
        # self.InitLatticeDiadg()
        # not(queue.empty())
        while(j<iterationNum):
            j += 1
            print(f"i:{j}")
            # remove first element and store first elemnt in the queue
            try:
                element1 = globals.queue.get_nowait()
                print("print element to work on")
                print(element1)

                # calculate Vtrans,Vreflecte
                Vtrans = operation.Vstamp_operate_Trans(element1)
                Vref = operation.Vstamp_operate_Ref(element1)

                if(Vtrans["Junction"] >= 1 and Vtrans["Junction"] <= globals.junctionsNum):
                    # Add to queue
                    print("Put Vtrans:")
                    print(Vtrans)
                    queue.put(Vtrans)
                else: #to update related node
                    if(Vtrans["Junction"] > junctionsNum):
                        Vtrans["Junction"] -=1
                        Vtrans["dir"] =1
                    else:
                        Vtrans["Junction"] +=1
                        Vtrans["dir"] =0
                if(Vref["Junction"] >= 1 and Vref["Junction"] <= globals.junctionsNum):
                    # Add to queue
                    print("Put Vref:")
                    print(Vref)
                    queue.put(Vref)
                else: #to update related node
                    if(Vref["Junction"] > globals.junctionsNum):
                        Vref["Junction"] -=1
                    else:
                        Vref["Junction"] +=1
                        Vref["dir"] =0
                # update nodes list
                print("add to node")
                globals.node_list.append(Vtrans)
                globals.node_list.append(Vref)

                # # remove first element
                print("print what to remove")
                print(element1)
            except:
                print("queue no element")

            print("\n")

    def check_input(value,min,max):
        try:
            if (value.startswith('inf')):
                value = float('inf')
            else:
                value = float(value)

            if (value < min or value > max):
                value='error'

        except:
            value='error'

        print(value)
        return value