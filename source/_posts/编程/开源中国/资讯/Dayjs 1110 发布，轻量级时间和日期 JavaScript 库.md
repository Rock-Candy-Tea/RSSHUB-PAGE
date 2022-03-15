
---
title: 'Day.js 1.11.0 发布，轻量级时间和日期 JavaScript 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9532'
author: 开源中国
comments: false
date: Tue, 15 Mar 2022 07:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9532'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Day.js 是一个仅 2kb 大小的轻量级 JavaScript 时间日期处理库，目前发布了 1.11.0 版本，带来如下改动：</span></p> 
<h3><strong>Bug修复</strong></h3> 
<ul> 
 <li>添加 Kirundi (rn) 语言环境 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fissues%2F1793" target="_blank">#1793</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fcommit%2F74e5247227a779fffde39bdfcd1ee19911496709" target="_blank">74e5247</a> )</li> 
 <li>添加缺失日期速记 D 类型定义 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fissues%2F1752" target="_blank">#1752</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fcommit%2Fb045baf1646a81f7e4f446f355d02d5fb0ef4aa7" target="_blank">b045baf</a> )</li> 
 <li>将相对时间添加到加利西亚语 (gl) 并修复序数 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fissues%2F1800" target="_blank">#1800</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fcommit%2Fdcbf1708400624addfbddbc71e0f6a9ac15fa961" target="_blank">dcbf170</a> )</li> 
 <li>更新德语语言环境 (de-at, de-ch) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fissues%2F1775" target="_blank">#1775</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fcommit%2Ff9055a77bf3d84c575e5fcf99e21611138ba64d7" target="_blank">f9055a7</a> )</li> 
 <li>更新冰岛语 locale relativeTime 配置 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fissues%2F1796" target="_blank">#1796</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fcommit%2F76f9e1756de7e99c01e471dab30ea074b9ec9629" target="_blank">76f9e17</a> )</li> 
 <li>更新 index.d.ts 注释 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fissues%2F1716" target="_blank">#1716</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fcommit%2F5a108ff3159c53fd270ea7638f33c35c934d6457" target="_blank">5a108ff</a> )</li> 
 <li>更新语言环境德语 [de] monthsShort ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fissues%2F1746" target="_blank">#1746</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fcommit%2F4a7b7d07c885bb9338514c234dbb708e24e9863e" target="_blank">4a7b7d0</a> )</li> 
 <li>将 meridiem 函数更新为库尔德 (ku) 语言环境 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fissues%2F1725" target="_blank">#1725</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fcommit%2Fefd3904ff8cbf0a4fc064911dda76fc86b669f7b" target="_blank">efd3904</a> )</li> 
 <li>更新 updateLocal 插件类型 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fissues%2F1692" target="_blank">#1692</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fcommit%2Fc7a3f73064dbb63b4d365b2ad4c792f075f4d8d8" target="_blank">c7a3f73</a> )</li> 
</ul> 
<h3><strong>特性</strong></h3> 
<ul> 
 <li>回退到仅语言区域设置 + 支持大写区域设置 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Fissues%2F1524" target="_blank">#1524</a> )</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiamkun%2Fdayjs%2Freleases%2Ftag%2Fv1.11.0" target="_blank">https://github.com/iamkun/dayjs/releases/tag/v1.11.0</a></p>
                                        </div>
                                      
</div>
            