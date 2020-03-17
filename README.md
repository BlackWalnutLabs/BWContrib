# BWContrib

A Python library based on `python-periphery` for simple control of the Navigator series robots.

[README](README.md) | [中文文档](README_zh.md)

## Installation

``` shell
pip3 install python-periphery
git clone https://github.com/BlackWalnutLabs/BWContrib
cd BWContrib
python3 setup.py build
python3 setup.py install --user
```

## Import

``` python
import bwcontrib
```

## Initialization

``` python
# 默认使用 'ttyTHS1' 串口
bwcontrib.control.init()
```

## Simple control

&emsp;&emsp;Developers can simply send directional commands to control the navigator, such as `Left`, `Right`, `Straight` and `Stop`.

&emsp;&emsp;A command corresponds to a behavior and can be sent frequently, but there is a priority between commands, and the interval between sending commands cannot be less than `150ms`.

``` python
# Turn left
bwcontrib.control.sendCommand('left')

# Sharp left
bwcontrib.control.sendCommand('leftQuickly')

# Pan left
bwcontrib.control.sendCommand('leftParallel')

# Turn right
bwcontrib.control.sendCommand('right')

# Sharp right
bwcontrib.control.sendCommand('rightQuickly')

# Pan right
bwcontrib.control.sendCommand('rightParallel')

# Straight
bwcontrib.control.sendCommand('straight')

# Rotate clockwise 1 circle in place
bwcontrib.control.sendCommand('around')

# Stop
bwcontrib.control.sendCommand('stop')

# Rotate in place until the next command
bwcontrib.control.sendCommand('keepAround')

# Rotate 90° clockwise
bwcontrib.control.sendCommand('turn90')
```

## Sending API commands

&emsp;&emsp;Send control instructions according to [API Documentation](docs/navigator_api_doc.md).

``` python
bwcontrib.control.sendCommandDirectly({'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0})
```

## Send data directly through the serial port

&emsp;&emsp;Send data directly to the serial port without preprocessing.

``` python
bwcontrib.control.sendCommandDirectlyWithoutJSON(bytes(json.dumps({'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0}), encoding="utf8"))
```

## Command priority

&emsp;&emsp;If there are two commands A and B, when the A command is issued and the vehicle has not completed the action required by the A command, the B command is issued, then the vehicle will judge what action should be run according to the priority of the AB command. If the A command has a higher priority than B, it will continue to run the A action and permanently discard the B command. If the priority of the B command is higher than A, the action of the A command is terminated, and the action of the B command is immediately executed. If A and B have the same priority, the action of the B command is executed.

|  Function Code   | Function Description  |
|  ----  | ----  |
| F1  | Free panning: keep the head facing unchanged and pan at any angle |
| F2  | Directional rotation: Rotate the specified degree in situ at the specified rate |
| F3  | Speed ​​control: control the speed and direction of the Navigator's in-situ rotation |
| F4  | Mixed motion: Free translation and simultaneous rotation, superimposed on each other. |
| F5  | Brake: Navigator stops moving |

**F5 > F2 > F4 = F3 = F1**

## Change log

* 2020.03.17:
    * Changed `bwtricar` project  to `bwcontrib`
    * Delete example
    * Delete speed gear
    * Remove `v1` series control instructions
    * Updated the navigator's series control instruction document
* 2020.01.06:
    * Turn slower.
    * Add `pan` command to `3rd` speed.
    * Add `turn` command to `3rd` speed.
* 2019.12.26:
    * Update reference.
* 2019.12.17:
    * Compatible with the previous usage of `2019.12.12`, the` ttyTHS1` serial port is used by default.
* 2019.12.12:
    * Added `USB` to serial port support (`ttyUSB0`).
    * Add change log.
    * Support sending data directly to serial port.
* 2019.11.07:
    * Add `Navigator` series product control `API` document.
* 2019.11.06:
    * Added Chinese documentation.
* 2019.08.26:
    * Supports `Jetson Nano` dock (`ttyTHS1`).
    * Open source the project.
    * Added English documentation.