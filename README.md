# WELCOME TO G.E.A.R. MK-1
FOLLOW THESE STEPS TO MAKE THE SYSTEM WORK:
1. Run the get_pi_requirements.sh file to get all the requirements
2. Run initial.sh to run the system (still finding a way to make it run after the system initialization)

**Can follow the operation manual to interact with the system**
*Need a Raspberry Pi 4 to run it due to the rpi.GPIO*

## Description
This is a robot I made for my Final Year Project in order to complete my Bachelor's Degree of IT. It is able to do the computer vision task and move around with the user control.

The picture below shows the whole robot &darr;
![GEARMK1](https://user-images.githubusercontent.com/49117926/151763814-4fca6ab5-f99f-424a-b6b0-eff80503a10e.jpg)


### Libraries Used: 
1. numpy
2. opencv-contrib-python==4.5.1.48
3. nltk
4. SpeechRecognition
5. pyttsx3
6. wolframalpha

### Hardware Components:
1. 1 Wheel Chassis (with 4 motors)
2. 1 L298N motor driver
3. 1 Raspberry Pi camera w/out stand
4. 1 Raspberry Pi 4 *(mine is 4GB RAM)*
5. 1 power source for Raspberry Pi 4 *(mine is powerbank with 5V output)*
6. at least 6V power source for L298N motor driver *(mine is a battery case with 6 AA batteries)*

### Functions Checklist
- [X] Simple Chat (NLTK)
- [X] Object Detection
- [X] Object Tracking
- [X] RC Driving
- [ ] Autonomous Driving (Object Following)
- [ ] Simple Chat (TF.Keras)
- [ ] Change built-in AI's gender/voice
