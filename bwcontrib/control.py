# coding=utf-8

#
# Copyright (c) 2019, BlackWalnut Labs.  All rights reserved.
#
# BlackWalnut Labs. and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from BlackWalnut Labs. is strictly prohibited.
#

from periphery import Serial
import json

serial = None

currentAbsSpeed = {
    'left': {'o': 0, 'v': 15, 'c': 0, 'd': 0, 'r': 15000, 'a': 0},
    'leftQuickly': {'o': 0, 'v': 10, 'c': 0, 'd': 0, 'r': 7000, 'a': 0},
    'leftParallel': {'o': 0, 'v': 10, 'c': 270, 'd': 0, 'r': 0, 'a': 0},
    'right': {'o': 0, 'v': 15, 'c': 0, 'd': 1, 'r': 15000, 'a': 0},
    'rightQuickly': {'o': 0, 'v': 10, 'c': 0, 'd': 1, 'r': 7000, 'a': 0},
    'rightParallel': {'o': 0, 'v': 10, 'c': 90, 'd': 0, 'r': 0, 'a': 0},
    'straight': {'o': 0, 'v': 21, 'c': 0, 'd': 0, 'r': 0, 'a': 0},
    'around': {'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 5000, 'a': 180},
    'stop': {'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0},
    'keepAround': {'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 15000, 'a': 0},
    'turn90': {'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 8000, 'a': 90}
}

interfaceDict = {
    'UART': '/dev/ttyTHS',
    'USB': '/dev/ttyUSB'
}


def init(interfaceType='UART', number=0, baud = 115200):
    global serial

    if(interfaceDict.get(interfaceType) != None):
        serial = Serial(interfaceDict[interfaceType] + str(number), baud)
    else:
        print('Interface type not exist, please concat us.')


def sendCommand(command):
    serial.write(bytes(json.dumps(currentAbsSpeed[command]), encoding="utf8"))


def sendCommandDirectly(command):
    serial.write(bytes(json.dumps(command), encoding="utf8"))


def sendCommandDirectlyWithoutJSON(command):
    serial.write(command)
