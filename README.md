# cityshaper
City Shaper - FLL code

Our code has many files that connect to each other in many ways. The **robot folder** has all of our classes and enumerations, which is the backbone of our code. This includes `robot.py`, which has all of our main functions, `pid.py`, which has the pid calculations, and `Line_edge.py and Line_sensor.py`, which are enumerations for our line follow. Our **mission files**, such as `crane.py`, `design_build.py`, and `ida.py` have th code to run our missions. Finally, `main.py` is the program running during the missions, which loads all the mission files and runs a specific one based on the button press. 
