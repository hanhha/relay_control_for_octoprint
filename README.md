# relay_control_for_octoprint

This script targets to #active low# relay modules. I uses 2 cheap modules that are active low and labeled 5V Vcc. But actually they can be used with 3v3 so it makes everything easier.

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
       
