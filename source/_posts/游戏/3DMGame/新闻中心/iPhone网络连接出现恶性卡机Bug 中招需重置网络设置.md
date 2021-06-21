
---
title: 'iPhone网络连接出现恶性卡机Bug 中招需重置网络设置'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20210621/1624271602_189477.gif'
author: 3DMGame
comments: false
date: Mon, 21 Jun 2021 10:45:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20210621/1624271602_189477.gif'
---

<div>   
<p style="text-indent:2em;">
BleepingComputer网站报道称iPhone在进行WiFi连接时中会出现一个恶性卡机Bug，该Bug将使的全球数百万台苹果设备受到攻击。此外，该bug一旦触发iPhone将无法再连接到任何无线网络。
</p>
<p style="text-indent:2em;">
该Bug是逆向工程师CarlSchou在尝试将iPhone连接到SSID为'%p%s%s%s%s%n'的个人WiFi后偶然发现的。Schou发推文称“iPhone拒绝连接并且禁用其WiFi连接，重新启动或更改SSID都无法修复该Bug。相反，iPhone还会陷入如下卡机循环中。”
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210621/1624271602_189477.gif" alt="iPhone网络连接出现恶性卡机Bug 中招需重置网络设置" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
Schou所使用操作系统是iOS14.4.2版本，但BleepingComputer证实该bug也会影响运行装有iOS14.6系统的iPhone。iPad目前还没有经过测试，但估计iPad也会受到攻击，Android设备不受影响。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210621/1624272072_131954.jpg" alt="iPhone网络连接出现恶性卡机Bug 中招需重置网络设置" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
根据网络安全博主CodeColorist的分析，该Bug是一个字符串<span>格式错误，WiFi名字中某些字符可能被操作系统误读为命令而不是简单的名称（在本例中为“%”）。这会导致设备出现故障，黑客可以利用该Bug来入侵设备或者恶意破坏。该Bug类似去年年底引起广泛关注的SMS Bug。</span>
</p>
<p style="text-indent:2em;">
目前，短期唯一的解决方案是用户重置其iPhone的网络设置（设置>通用>重置>重置网络设置），这将会清除手机中所有的WiFi密码，并且这套操作治标不治本，设备如果再次受到攻击，用户还必须重新这样操作。
</p>
<p style="text-indent:2em;">
预计苹果官方将会发布紧急iOS更新来解决此问题（可能是iOS12到iOS14.6.1的更新），目前苹果官方未对此事作出回应。
</p>          
</div>
            