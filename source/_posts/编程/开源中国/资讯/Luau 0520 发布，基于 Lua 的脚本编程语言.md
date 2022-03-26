
---
title: 'Luau 0.520 发布，基于 Lua 的脚本编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1641'
author: 开源中国
comments: false
date: Sat, 26 Mar 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1641'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#333333">Luau（发音/ˈlu.aʊ/）是一门快速、轻量、安全、采用渐进式类型化且支持嵌入的脚本语言，派生自 Lua。，目前 Luau 0.520 发布了，该版本带来如下变更：</span></p> 
<h2><strong>Analysis changes</strong></h2> 
<ul> 
 <li><span style="color:#24292f">当来自不同模块的类型具有相同名称时，改进类型错误</span></li> 
 <li>当函数是可变参数时，改进参数计数不匹配的类型错误</li> 
 <li>改进表索引器类型不匹配的类型错误解释</li> 
 <li>从 UnknownType lint 中删除遗留的特定 Roblox 警告</li> 
 <li>提高具有复杂类型的类型错误的程序的类型检查性能</li> 
</ul> 
<h2><strong>Runtime Changes</strong></h2> 
<ul> 
 <li>通过默认排除指标收集来略微减少 GC 开销</li> 
 <li>使用 LUA_USE_LONGJMP 时，显著提高 macOS 上的 pcall/resume 性能 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRoblox%2Fluau%2Fissues%2F425" target="_blank">#425</a> )</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRoblox%2Fluau%2Freleases%2Ftag%2F0.520" target="_blank">https://github.com/Roblox/luau/releases/tag/0.520</a></p>
                                        </div>
                                      
</div>
            