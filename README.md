# relay_control_for_octoprint

This script targets to **active low** relay modules. I uses 2 cheap modules that are active low and labeled 5V Vcc. But actually they can be used with 3v3 so it makes everything easier.  
My script uses pin 11 and 13 (physically pin number) to control relays. Remember to adjust them in the script (relay_pin0 and relay_pin1 variables) to fit your setup.  
After appropriately wiring hardware, copy the script somewhere and add these lines to config.yaml file of Octoprint ( if you're using OctoPi image, it's normally in ~/.octoprint/config.yaml).  
```
system:  
  actions:  
  - action: printer_on  
    command: python <your path>/control_pwr.py on  
    name: Turn on the printer  
  - action: printer_off  
    command: python <your path>/control_pwr.py off  
    confirm: You are about to turn off the printer. It's better to disconnect the printer first if you didn't.  
    name: Turn off the printer  
```
Below is my setup. I control both wires of AC power supplier.

            -------          
           |  RPI  |  
            -------  
               |  
               |  
      ---------------------------------  
     |2 channels relay module/2 modules|  
      ---------------------------------  
                  |      |  
         hot wire |      | cold wire   
                  |      |  
             -----------------   
            |AC power supplier|              
            |for my 3D printer|              
             -----------------  
       
