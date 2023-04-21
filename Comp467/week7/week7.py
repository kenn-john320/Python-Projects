# Write a script that takes a frame and turns it into
# a working timecode at 24fps.

# Use frame examples: 35, 1569, 14000


#Lesson Question Answer: MAGNETO

# from timecode import TimeCode

def convertTimeCode(frames):
    fps = 24 # frames per second
    totalSec = frames/fps


    hours = int( totalSec / 3600 )
    minutes = int((totalSec % 3600) / 60)
    seconds = int(totalSec % 60)

    frames = frames % fps

    return f'Timecode: {int(hours) if int(hours) > 9 else "0" + str(hours) }:{int(minutes) if int(minutes) > 9 else "0" + str(minutes)}:{int(seconds) if int(seconds) > 9 else "0" + str(seconds)}:{int(frames) if int(frames) > 9 else "0" + str(frames)}'


print(convertTimeCode(14000))