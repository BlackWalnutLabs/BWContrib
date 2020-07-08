# BWContrib

一个基于 `python-periphery` 的简单控制领航者系列机器人的 `Python` 库。

[README](README.md) | [中文文档](README_zh.md)

## 安装

``` shell
pip3 install python-periphery
git clone https://github.com/BlackWalnutLabs/BWContrib
cd BWContrib
python3 setup.py build
python3 setup.py install --user
```

## 导入

``` python
import bwcontrib
```

## 初始化

``` python
# 默认使用 'ttyTHS1' 串口
bwcontrib.control.init()
```

## 简单控制

&emsp;&emsp;开发人员可以简单地发送方向命令来控制导航器，例如 “左”，“右”，“直” 和 “停止”。

&emsp;&emsp;一个命令对应一种行为，可以频繁发送命令，但命令之间有优先级，发送命令之间的间隔不能小于 `150ms`。

``` python
# 左转
bwcontrib.control.sendCommand('left')

# 左急转
bwcontrib.control.sendCommand('leftQuickly')

# 左平移
bwcontrib.control.sendCommand('leftParallel')

# 右转
bwcontrib.control.sendCommand('right')

# 右急转
bwcontrib.control.sendCommand('rightQuickly')

# 左平移
bwcontrib.control.sendCommand('leftParallel')

# 直行
bwcontrib.control.sendCommand('straight')

# 原地顺时针旋转 1 圈
bwcontrib.control.sendCommand('around')

# 停止
bwcontrib.control.sendCommand('stop')

# 直到下一个命令之前持续原地旋转
bwcontrib.control.sendCommand('keepAround')

# 顺时针旋转 90°
bwcontrib.control.sendCommand('turn90')
```

## 发送 API 命令

&emsp;&emsp;根据 [API 文档](docs/navigator_api_doc.md) 发送控制指令。

``` python
bwcontrib.control.sendCommandDirectly({'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0})
```

## 串口直接发送数据

&emsp;&emsp;直接往串口传数据，不经过预处理。

``` python
bwcontrib.control.sendCommandDirectlyWithoutJSON(bytes(json.dumps({'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0}), encoding="utf8"))
```

## 命令优先级

&emsp;&emsp;若存在 `A,B` 两个指令，当 `A` 指令下发，而车辆尚未完成 `A` 指令要求的动作时， `B` 指令下发，则此时车辆会根据 `AB` 指令优先级判断此时应该运行什么动作。若 `A` 指令优先级高于 `B` ，则会继续运行 `A` 的动作，永久抛弃 `B` 指令。若 `B` 指令优先级高于 `A` ，则终止 `A` 指令的动作，立即执行 `B` 指令的动作。若 `A,B` 优先级相同，则运行 `B` 指令的动作。

| 功能代码 | 功能描述                                       |
| -------- | ---------------------------------------------- |
| `F1`     | 自由平移：保持车头朝向不变，向任意角度平移行驶 |
| `F2`     | 定向旋转：以指定速率原地旋转指定度数           |
| `F3`     | 转速控制：控制小车原地自转速度与方向           |
| `F4`     | 混合运动：自由平移与原地旋转同时进行，互相叠加 |
| `F5`     | 刹车：车辆停止运动                             |

**F5 > F2 > F4 = F3 = F1**

## 更新日志

* 2020.07.08:
    * 可自由定制端口号和波特率
* 2020.03.18：
    * 增加领航者控制文档 `Modbus` 协议说明
* 2020.03.17：
    * `bwtricar` 项目更名为 `bwcontrib`
    * 删除样例
    * 删除速度档位
    * 删除 `v1` 系列控制指令
    * 更新领航者系列控制指令文档
* 2020.01.06:
    * 降低转弯速度
    * `3` 档速度添加 `平移` 指令
    * `3` 档速度添加 `右转 90` 指令
* 2019.12.26:
    * 更新引用。
* 2019.12.17:
    * 兼容 `2019.12.12` 前用法，默认使用 `ttyTHS1` 串口。
* 2019.12.12：
    * 新增 `USB` 转串口支持（`ttyUSB0`）。
    * 添加更新日志。
    * 支持直接往串口发数据。
* 2019.11.07：
    * 添加 `Navigator` 系列产品控制 `API` 文档。
* 2019.11.06：
    * 添加中文文档说明。
* 2019.08.26：
    * 支持 `Jetson Nano` 串口（`ttyTHS1`）。
    * 项目开源。
    * 添加英文文档说明。