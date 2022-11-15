import numpy as np
from tinytag import TinyTag

file = [None]*1000
for i in range(500):
    file[i] = TinyTag.get(r'dhwani'+str(i)+'.mp3')
for i in range(500,808):
    file[i] = TinyTag.get(r'dhwani'+str(i)+'.mp3')
for i in range(808, 1000):
    j = i - 808
    file[i] = TinyTag.get(r'video' + str(j)+'.mp4')

# We desire to have our data of features in array format

# X contains the features in order size/duration, samplerate, # y contains 1 for .mp3 files and 0 for .mp4 files

feature = [None]*1000
for i in range(1000):
    data1 = (file[i].filesize/file[i].duration)
    data2 = file[i].samplerate
    if file[i].audio_offset == None:
        data3 = 0
    else:
        data3 = file[i].audio_offset
    if file[i].bitrate == 'None':
        data4 = 0
    else:
        data4 = file[i].bitrate
    feature[i] = [data1, data2, data3, data4]
# Data1 = filesize vs time
# Data2 = Samplerate
# Data3 = audio_offset
# Data4 = bitrate
X = np.array(feature)
print("Feature of x:",feature)
output = [None]*1000
for i in range(808):
    output[i] = [1]
for i in range (808, 1000):
    output[i] = [0]
y = np.array(output)
print("y", output)