# Python 3.9.4

''' You can go to https://earsketch.gatech.edu/landing/#/ to experiment with
your code.'''

from earsketch import *
 
init()
setTempo(130)
 
clip1 = EIGHT_BIT_ATARI_SFX_004
clip2 = EIGHT_BIT_ATARI_LEAD_011
clip3 = EIGHT_BIT_ATARI_LEAD_010
 
pointA = 4.75
repeat = 5
pointD = pointA + repeat 
 
#fitMedia(Clip,Track,StartMeasure,EndMeasure)
fitMedia(clip1,1,1,2)
for i in range(0,repeat):
  fitMedia(clip2,2,pointA + i,pointA + i + 1)
 
fitMedia(clip3,3,pointA,pointD + 50)
 
#setEffect(Track,effect,parmeter,value)
setEffect(173, VOLUME, GAIN, -20)
 
#setEffect(Track,effect,parmeter,value,start measure,value,end measure)
#Fade in
setEffect(1, VOLUME, GAIN, 3, 1, 5, 1.75)
#Delay Effect
setEffect(1, DELAY, DELAY_TIME, 250)
setEffect(2, DELAY, DELAY_TIME, 250)
#Fade Out
setEffect(3, VOLUME, GAIN, 4, pointD, 6, pointD+1)
 
finish()
