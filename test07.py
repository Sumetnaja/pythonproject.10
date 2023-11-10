import os

if os.path.exists('iot1.txt') :
    os.remove('iotxxx.txt')
else :
    print('File not found....^_^')