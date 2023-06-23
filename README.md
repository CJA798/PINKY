# Tiny-Forklift <img src="https://github.com/CJA798/Tiny-Forklift/blob/644d3fdcc407f6ff0c4a84dc8507e36112bb0a8a/IMAGES/Mini_Bot_V2.2.PNG" width="72" height="54">
Tiny forklift robot that uses computer vision to find objects, pick them up and place them in specific locations
<img src="https://github.com/CJA798/Tiny-Forklift/blob/644d3fdcc407f6ff0c4a84dc8507e36112bb0a8a/IMAGES/Mini_Bot_V2.2.PNG" width="720" height="540">

## Hardware:
- Arduino Nicla Vision
- Raspberry Pi Pico
- LM2596 DC to DC Buck Converter
- LM2596S DC to DC Buck Converter with Digital Voltmeter Display
- TATTU 650mAh 2S 7.4V 75C LiPo Battery Pack
- Switch
- Adafruit DRV8833 DC/Stepper Motor Driver Breakout Board
- 2x N20 DC Motor with Magnetic Encoder - 6V with 1:150 Gear Ratio
- 2x Technic Lego Wheel and Tire Set (Mindstorms nxt ev3 tyre)
- Future Upgrades:
   - Micro servos for forklift mechanism
   - Raspberry Pi 4B for tracking system
       - Power Bank
       - Coral USB Accelerator
       - Pi Camera Module V3  
- Chasis (See CAD folder for files)
# TODO:
- [ ] Train object detection model
- [ ] Figure out if reading data directly from ToF's I2C channel works on the Pico
- [ ] Write code to get sensor data
  - [ ] Nicla Vision ToF
  - [ ] Nicla Vision IMU
  - [ ] Nicla Vision camera
  - [ ] Pi 4B camera
  - [ ] Pico magnetic encoders
- [ ] Use a sensor fusion method to combine cameras, ToF, IMU, and encoder data for path planning
- [ ] Make a more compact chassis
- [ ] Simplify and clean wiring
   - [ ] Make custom PCB

