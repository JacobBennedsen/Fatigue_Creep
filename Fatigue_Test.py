import sys
import time
import csv
from collections import deque
import traceback
import matplotlib.pyplot as plt
import numpy as np
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *

try:
    from PhidgetHelperFunctions import *
except ImportError:
    sys.stderr.write("\nCould not find PhidgetHelperFunctions. Either add PhdiegtHelperFunctions.py to your project folder "
                     "or remove the import from your project.")
    sys.stderr.write("\nPress ENTER to end program.")
    readin = sys.stdin.readline()
    sys.exit()

"""
* Configures the device's DataInterval and ChangeTrigger.
* Displays info about the attached phidget channel.
* Fired when a Phidget channel with onAttachHandler registered attaches
*
* @param self The Phidget channel that fired the attach event
"""

def onAttachHandler(self):
    
    ph = self
    try:
        #If you are unsure how to use more than one Phidget channel with this event, we recommend going to
        #www.phidgets.com/docs/Using_Multiple_Phidgets for information
        
        print("\nAttach Event:")
        
        """
        * Get device information and display it.
        """
        channelClassName = ph.getChannelClassName()
        serialNumber = ph.getDeviceSerialNumber()
        channel = ph.getChannel()
        if(ph.getDeviceClass() == DeviceClass.PHIDCLASS_VINT):
            hubPort = ph.getHubPort()
            print("\n\t-> Channel Class: " + channelClassName + "\n\t-> Serial Number: " + str(serialNumber) +
                "\n\t-> Hub Port: " + str(hubPort) + "\n\t-> Channel " + str(channel) + "\n")
        else:
            print("\n\t-> Channel Class: " + channelClassName + "\n\t-> Serial Number: " + str(serialNumber) +
                    "\n\t-> Channel " + str(channel) + "\n")
    
        """
        * Set the DataInterval inside of the attach handler to initialize the device with this value.
        * DataInterval defines the minimum time between VoltageRatioChange events.
        * DataInterval can be set to any value from MinDataInterval to MaxDataInterval.
        """
        print("\n\tSetting DataInterval to 1000ms")
        ph.setDataInterval(1000)

        """
        * Set the VoltageRatioChangeTrigger inside of the attach handler to initialize the device with this value.
        * VoltageRatioChangeTrigger will affect the frequency of VoltageRatioChange events, by limiting them to only occur when
        * the voltage ratio changes by at least the value set.
        """
        print("\tSetting Voltage Ratio ChangeTrigger to 0.0")
        ph.setVoltageRatioChangeTrigger(0.0)
        
        """
        * Set the SensorType inside of the attach handler to initialize the device with this value.
        * You can find the appropriate SensorType for your sensor in its User Guide and the VoltageRatioInput API
        * SensorType will apply the appropriate calculations to the voltage ratio reported by the device
        * to convert it to the sensor's units.
        * SensorType can only be set for Sensor Port voltage ratio inputs (VINT Ports and Analog Input Ports)
        """
        if(ph.getChannelSubclass() == ChannelSubclass.PHIDCHSUBCLASS_VOLTAGERATIOINPUT_SENSOR_PORT):
            print("\tSetting VoltageRatio SensorType")
            ph.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_VOLTAGERATIO)
            
        
    except PhidgetException as e:
        print("\nError in Attach Event:")
        DisplayError(e)
        traceback.print_exc()
        return

"""
* Displays info about the detached phidget channel.
* Fired when a Phidget channel with onDetachHandler registered detaches
*
* @param self The Phidget channel that fired the attach event
"""
def onDetachHandler(self):

    ph = self

    try:
        #If you are unsure how to use more than one Phidget channel with this event, we recommend going to
        #www.phidgets.com/docs/Using_Multiple_Phidgets for information
        
        print("\nDetach Event:")
        
        """
        * Get device information and display it.
        """
        channelClassName = ph.getChannelClassName()
        serialNumber = ph.getDeviceSerialNumber()
        channel = ph.getChannel()
        if(ph.getDeviceClass() == DeviceClass.PHIDCLASS_VINT):
            hubPort = ph.getHubPort()
            print("\n\t-> Channel Class: " + channelClassName + "\n\t-> Serial Number: " + str(serialNumber) +
                "\n\t-> Hub Port: " + str(hubPort) + "\n\t-> Channel " + str(channel) + "\n")
        else:
            print("\n\t-> Channel Class: " + channelClassName + "\n\t-> Serial Number: " + str(serialNumber) +
                    "\n\t-> Channel " + str(channel) + "\n")
        
    except PhidgetException as e:
        print("\nError in Detach Event:")
        DisplayError(e)
        traceback.print_exc()
        return


"""
* Writes phidget error info to stderr.
* Fired when a Phidget channel with onErrorHandler registered encounters an error in the library
*
* @param self The Phidget channel that fired the attach event
* @param errorCode the code associated with the error of enum type ph.ErrorEventCode
* @param errorString string containing the description of the error fired
"""
def onErrorHandler(self, errorCode, errorString):

    sys.stderr.write("[Phidget Error Event] -> " + errorString + " (" + str(errorCode) + ")\n")

"""
* Outputs the VoltageRatioInput's most recently reported voltage ratio.
* Fired when a VoltageRatioInput channel with onVoltageRatioChangeHandler registered meets DataInterval and ChangeTrigger criteria
*
* @param self The VoltageRatioInput channel that fired the VoltageRatioChange event
* @param voltageRatio The reported voltage ratio from the VoltageRatioInput channel
"""

def onVoltageRatioChangeHandler(self, voltageRatio):

    #If you are unsure how to use more than one Phidget channel with this event, we recommend going to
    #www.phidgets.com/docs/Using_Multiple_Phidgets for information

    print("[VoltageRatio Event] -> Voltage Ratio: " + str(voltageRatio))

"""
* Creates, configures, and opens a VoltageRatioInput channel.
* Displays Voltage Ratio events for 10 seconds
* Closes out VoltageRatioInput channel
*
* @return 0 if the program exits successfully, 1 if it exits with errors.
"""
def main():
    try:
        """
        * Allocate a new Phidget Channel object
        """
        try:
            ch0 = VoltageRatioInput()
            ch1 = VoltageRatioInput()
            ch2 = VoltageRatioInput()
            ch3 = VoltageRatioInput()
            ch4 = VoltageRatioInput()
            ch5 = VoltageRatioInput()
            ch6 = VoltageRatioInput()
            ch7 = VoltageRatioInput()
            ch8 = VoltageRatioInput()
            ch9 = VoltageRatioInput()
            digi = DigitalInput()
            
        except PhidgetException as e:
            sys.stderr.write("Runtime Error -> Creating VoltageRatioInput: \n\t")
            DisplayError(e)
            raise
        except RuntimeError as e:
            sys.stderr.write("Runtime Error -> Creating VoltageRatioInput: \n\t" + e)
            raise

        """
        * Set matching parameters to specify which channel to open
        """
        
        #You may remove this line and hard-code the addressing parameters to fit your application
        #channelInfo = AskForDeviceParameters(ch)
        
        ch0.setDeviceSerialNumber(474147)
        ch0.setHubPort(0)
        ch0.setIsHubPortDevice(0)
        ch0.setChannel(0)
        
        ch1.setDeviceSerialNumber(474147)
        ch1.setHubPort(0)
        ch1.setIsHubPortDevice(0)
        ch1.setChannel(1)
        
        ch2.setDeviceSerialNumber(474147)
        ch2.setHubPort(0)
        ch2.setIsHubPortDevice(0)
        ch2.setChannel(2)
        
        ch3.setDeviceSerialNumber(474147)
        ch3.setHubPort(0)
        ch3.setIsHubPortDevice(0)
        ch3.setChannel(3)
        
        ch4.setDeviceSerialNumber(474147)
        ch4.setHubPort(0)
        ch4.setIsHubPortDevice(0)
        ch4.setChannel(0)
        
        ch5.setDeviceSerialNumber(000000)
        ch5.setHubPort(0)
        ch5.setIsHubPortDevice(0)
        ch5.setChannel(1)
        
        ch6.setDeviceSerialNumber(000000)
        ch6.setHubPort(0)
        ch6.setIsHubPortDevice(0)
        ch6.setChannel(2)
        
        ch7.setDeviceSerialNumber(000000)
        ch7.setHubPort(0)
        ch7.setIsHubPortDevice(0)
        ch7.setChannel(3)
        
        ch8.setDeviceSerialNumber(000000)
        ch8.setHubPort(0)
        ch8.setIsHubPortDevice(0)
        ch8.setChannel(0)
        
        ch9.setDeviceSerialNumber(000000)
        ch9.setHubPort(0)
        ch9.setIsHubPortDevice(0)
        ch9.setChannel(1)
        
        digi.setDeviceSerialNumber(000000)
        digi.setHubPort(0)
        digisetIsHubPortDevice(0)
        digi.setChannel(0)
        
        
        """
        * Add event handlers before calling open so that no events are missed.
        """
        print("\n--------------------------------------")
        print("\nSetting OnAttachHandler...")
        ch0.setOnAttachHandler(onAttachHandler)
        ch1.setOnAttachHandler(onAttachHandler)
        ch2.setOnAttachHandler(onAttachHandler)
        ch3.setOnAttachHandler(onAttachHandler)
        ch4.setOnAttachHandler(onAttachHandler)
        ch5.setOnAttachHandler(onAttachHandler)
        ch6.setOnAttachHandler(onAttachHandler)
        ch7.setOnAttachHandler(onAttachHandler)
        ch8.setOnAttachHandler(onAttachHandler)
        ch9.setOnAttachHandler(onAttachHandler)
        
        print("Setting OnDetachHandler...")
        ch0.setOnDetachHandler(onDetachHandler)
        ch1.setOnDetachHandler(onDetachHandler)
        ch2.setOnDetachHandler(onDetachHandler)
        ch3.setOnDetachHandler(onDetachHandler)
        ch4.setOnDetachHandler(onDetachHandler)
        ch5.setOnDetachHandler(onDetachHandler)
        ch6.setOnDetachHandler(onDetachHandler)
        ch7.setOnDetachHandler(onDetachHandler)
        ch8.setOnDetachHandler(onDetachHandler)
        ch9.setOnDetachHandler(onDetachHandler)
        
        print("Setting OnErrorHandler...")
        ch0.setOnErrorHandler(onErrorHandler)
        ch1.setOnErrorHandler(onErrorHandler)
        ch2.setOnErrorHandler(onErrorHandler)
        ch3.setOnErrorHandler(onErrorHandler)
        ch4.setOnErrorHandler(onErrorHandler)
        ch5.setOnErrorHandler(onErrorHandler)
        ch6.setOnErrorHandler(onErrorHandler)
        ch7.setOnErrorHandler(onErrorHandler)
        ch8.setOnErrorHandler(onErrorHandler)
        ch9.setOnErrorHandler(onErrorHandler)
        
        """
        * Open the channel with a timeout
        """
        
        print("\nOpening and Waiting for Attachment...")
        
        try:
            ch0.openWaitForAttachment(5000)
            ch1.openWaitForAttachment(5000)
            ch2.openWaitForAttachment(5000)
            ch3.openWaitForAttachment(5000)
            ch4.openWaitForAttachment(5000)
            ch5.openWaitForAttachment(5000)
            ch6.openWaitForAttachment(5000)
            ch7.openWaitForAttachment(5000)
            ch8.openWaitForAttachment(5000)
            ch9.openWaitForAttachment(5000)
            digi.openWaitForAttachment(5000)
        except PhidgetException as e:
            PrintOpenErrorMessage(e, ch0)
            PrintOpenErrorMessage(e, ch1)
            PrintOpenErrorMessage(e, ch2)
            PrintOpenErrorMessage(e, ch3)
            PrintOpenErrorMessage(e, ch4)
            PrintOpenErrorMessage(e, ch5)
            PrintOpenErrorMessage(e, ch6)
            PrintOpenErrorMessage(e, ch7)
            PrintOpenErrorMessage(e, ch8)
            PrintOpenErrorMessage(e, ch9)
            raise EndProgramSignal("Program Terminated: Open Failed")
        
        print("Sampling data for 10 seconds...")
        
        print("You can do stuff with your Phidgets here and/or in the event handlers.")
        
        time.sleep(5)
    
        #Create csv file to write data to
        file_path = os.path.join('C:','Users','Jacob Bennedsen','Desktop','Python Files','Learning','Fatigue_Test.csv')
        csvfile = open(file_path, 'w')
        filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\n', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        #Write header row to csv
        filewriter.writerow(['Signal Iteration','Time (s)','ch0 (V/V)','ch1 (V/V)','ch2 (V/V)','ch3 (V/V)','ch4 (V/V)','ch5 (V/V)','ch6 (V/V)','ch7 (V/V)','ch8 (V/V)','ch9 (V/V)'])
        
        delay = 1 #seconds
        
        #Initialize lists to be used for data plotting
        logged_time = list()
        w0 = list()
        w1 = list()
        w2 = list()
        w3 = list()
        w4 = list()
        w5 = list()
        w6 - list()
        w7 = list()
        w8 = list()
        w9 = list()
        
        d = deque([0,0]) #Deque to check for change in state
        d.maxlen(2) #Set max length of deque to 2
        sig_count = 0 #Count of changes in state
        i = 0 #Iteration of loop
        
        start_time = time.monotonic() #Start time betweeen state change timer
        elapsed_time = 0 #Initialize the elapsed time
        
        while elapsed_time < 30: #Loop while the time between state changes is less than 30 sec
            elapsed_time = time.monotonic()-start_time #Update elapsed time
            d.append(digi.getState()) #Get the latest PLC signal value
            
            if d[0] != d[1]: #Check if the latest and previous values changed
                start_time = time.monotonic() #If yes then reset time between state changes
                sig_count += 1 #Increment signal count
                
            t = i*delay #Timestamp based upon loop iterations and data collection delay
            
            #Store latest voltage ratio from each channel in a variable
            v0 = ch0.getVoltageRatio()
            v1 = ch1.getVoltageRatio()
            v2 = ch2.getVoltageRatio()
            v3 = ch3.getVoltageRatio()
            v4 = ch4.getVoltageRatio()
            v5 = ch5.getVoltageRatio()
            v6 = ch6.getVoltageRatio()
            v7 = ch7.getVoltageRatio()
            v8 = ch8.getVoltageRatio()
            v9 = ch9.getVoltageRatio()
            
            logged_time.append(t) #Add latest time to list
            w0.append(v0) #Add latest voltage ratio to list
            w1.append(v1)
            w2.append(v2)
            w3.append(v3)
            w4.append(v4)
            w5.append(v5)
            w6.append(v6)
            w7.append(v7)
            w8.append(v8)
            w9.append(v9)
           
            #Write the collected data to a csv
            filewriter.writerow([sig_count,t,v0,v1,v2,v3,v4,v5,v6,v7,v8,v9])
            
            i += 1 #Increment iterations
            
            time.sleep(delay) #Wait for the specified time before looping again
            
        csvfile.close()
        
        #Plot data
        plt.plot(logged_time, w0, label='ch0')
        plt.plot(logged_time, w1, label='ch1')
        plt.plot(logged_time, w2, label='ch2')
        plt.plot(logged_time, w3, label='ch3')
        plt.plot(logged_time, w4, label='ch4')
        plt.plot(logged_time, w5, label='ch5')
        plt.plot(logged_time, w6, label='ch6')
        plt.plot(logged_time, w7, label='ch7')
        plt.plot(logged_time, w8, label='ch8')
        plt.plot(logged_time, w9, label='ch9')
        plt.legend()
        plt.show()
        
        """
        * Perform clean up and exit
        """

        #clear the VoltageRatioChange event handler 
        ch0.setOnVoltageRatioChangeHandler(None)
        ch1.setOnVoltageRatioChangeHandler(None)
        ch2.setOnVoltageRatioChangeHandler(None)
        ch3.setOnVoltageRatioChangeHandler(None)
        ch4.setOnVoltageRatioChangeHandler(None)
        ch5.setOnVoltageRatioChangeHandler(None)
        ch6.setOnVoltageRatioChangeHandler(None)
        ch7.setOnVoltageRatioChangeHandler(None)
        ch8.setOnVoltageRatioChangeHandler(None)
        ch9.setOnVoltageRatioChangeHandler(None)
           
        print("\nDone Sampling...")

        print("Cleaning up...")
        ch0.close()
        ch1.close()
        ch2.close()
        ch3.close()
        ch4.close()
        ch5.close()
        ch6.close()
        ch7.close()
        ch8.close()
        ch9.close()
        print("\nExiting...")
        return 0

    except PhidgetException as e:
        sys.stderr.write("\nExiting with error(s)...")
        DisplayError(e)
        traceback.print_exc()
        print("Cleaning up...")
        ch0.setOnVoltageRatioChangeHandler(None)
        ch1.setOnVoltageRatioChangeHandler(None)
        ch2.setOnVoltageRatioChangeHandler(None)
        ch3.setOnVoltageRatioChangeHandler(None)
        ch0.close()
        ch1.close()
        ch2.close()
        ch3.close()
        ch4.close()
        ch5.close()
        ch6.close()
        ch7.close()
        ch8.close()
        ch9.close()
        return 1
    except EndProgramSignal as e:
        print(e)
        print("Cleaning up...")
        ch0.setOnVoltageRatioChangeHandler(None)
        ch1.setOnVoltageRatioChangeHandler(None)
        ch2.setOnVoltageRatioChangeHandler(None)
        ch3.setOnVoltageRatioChangeHandler(None)
        ch0.close()
        ch1.close()
        ch2.close()
        ch3.close()
        ch4.close()
        ch5.close()
        ch6.close()
        ch7.close()
        ch8.close()
        ch9.close()
        return 1
    finally:
        print("Press ENTER to end program.")
        readin = sys.stdin.readline()

main()
