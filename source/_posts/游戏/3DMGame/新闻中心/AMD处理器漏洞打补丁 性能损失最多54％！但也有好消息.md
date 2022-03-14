
---
title: 'AMD处理器漏洞打补丁 性能损失最多54％！但也有好消息'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20220313/1647182311_565174.jpg'
author: 3DMGame
comments: false
date: Sun, 13 Mar 2022 14:39:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20220313/1647182311_565174.jpg'
---

<div>   
<p style="text-indent:2em;">
近几年，Meltdown熔断、Spectre幽灵两大安全漏洞不但冲击整个CPU处理器行业，尤其是幽灵漏洞，版本众多，不断出现新变种。
</p>
<p style="text-indent:2em;">
近日，Intel、荷兰大学研究人员又发现了一个Spectre V2幽灵漏洞版本，为分支历史注入(BHI)，可以绕过部分补丁，Intel 4-12代酷睿、ARM Cortex/Neoverse架构无一幸免。
</p>
<p style="text-indent:2em;">
根据实测，Intel处理器打上相应的补丁后，性能会损失最多35％。
</p>
<p style="text-indent:2em;">
AMD完全免疫？倒也不是。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220313/1647182311_565174.jpg" alt="AMD处理器漏洞打补丁 性能损失最多54％！但也有好消息" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
Intel研究发现，AMD处理器的补丁存在缺陷，后者的修复方式也从LEFENCE/JMP变成了常规的Retpoline，也不可避免地影响了性能。
</p>
<p style="text-indent:2em;">
Phoronix对锐龙9 5950X、锐龙9 5900HX、霄龙7F23三颗处理器在Linux下进行了补丁前后的性能实测对比，都基于Zen3架构，分别用于桌面、笔记本、服务器。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220313/1647182333_659079.png" alt="AMD处理器漏洞打补丁 性能损失最多54％！但也有好消息" referrerpolicy="no-referrer"> 
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220313/1647182333_285362.png" alt="AMD处理器漏洞打补丁 性能损失最多54％！但也有好消息" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
锐龙9 5950X打补丁后，Stess-NG(Context Switching)测试性能居然丢了多达54％，直接腰斩，但幸运的是，除此之外其他项目影响不大，最多不过6.4％，平均还不到1.5％，甚至有三个项目不降反升。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220313/1647182354_190711.png" alt="AMD处理器漏洞打补丁 性能损失最多54％！但也有好消息" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
锐龙9 5900HX也是Stress-NG(Context Switching)项目影响最大，损失了22％，另外有三个项目超过9％。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220313/1647182362_387337.png" alt="AMD处理器漏洞打补丁 性能损失最多54％！但也有好消息" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
霄龙7F23的情况最好，Stress-NG(Context Switching)也只下滑了8.9％，还有多达8个项目性能更好了，最多增加了近4％。
</p>          
</div>
            