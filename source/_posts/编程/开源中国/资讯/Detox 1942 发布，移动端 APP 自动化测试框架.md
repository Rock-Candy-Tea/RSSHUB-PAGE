
---
title: 'Detox 19.4.2 发布，移动端 APP 自动化测试框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3648'
author: 开源中国
comments: false
date: Sat, 15 Jan 2022 07:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3648'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Detox 是一个用于移动端 APP 灰盒测试（介于白盒测试和黑盒测试之间，既关注内部逻辑实现也关注软件最终效果，通常在集成测试阶段进行）的自动化测试框架。目前 Detox 发布了 19.4.2 版本，带来如下修复：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>iOS</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>AppleSimUtils：替换<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwix%2FDetox%2Freleases%2Ftag%2F19.4.0" target="_blank">v19.4.0</a><span> </span>版本中的解决方法，该解决方法在集成 Firebase-Performance 时解决了各种崩溃，并在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2FGoogleUtilities%2Fblob%2Fmain%2FCHANGELOG.md%23770" target="_blank">GoogleUtilities v7.7.0</a>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwix%2FDetox%2Fpull%2F3167" target="_blank">#3167</a>）中引入了指定修复程序- </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情请参阅：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffirebase%2Ffirebase-ios-sdk%2Fissues%2F9083" target="_blank">firebase/firebase-ios- sdk#9083</a><span> </span>.</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>安卓</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 RN66 解决方法（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwix%2FDetox%2Fpull%2F3169" target="_blank">#3169</a>）中的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjonathanmos" target="_blank"><strong>classCastException</strong></a><span> </span>- 详情请参阅：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwix%2FDetox%2Fissues%2F3168" target="_blank">#3168</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>JavaScript</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">修复端口分配竞争<span> </span></span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwix%2FDetox%2Fpull%2F3174" target="_blank">#3174</a><span style="color:#2e3033">) -应该会提高并发任务 >3 时的 Detox 稳定性。</span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwix%2FDetox%2Freleases%2Ftag%2F19.4.2" target="_blank">https://github.com/wix/Detox/releases/tag/19.4.2</a></p>
                                        </div>
                                      
</div>
            