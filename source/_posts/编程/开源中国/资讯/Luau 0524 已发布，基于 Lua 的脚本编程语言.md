
---
title: 'Luau 0.524 已发布，基于 Lua 的脚本编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2420'
author: 开源中国
comments: false
date: Sat, 23 Apr 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2420'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Luau（发音/ˈlu.aʊ/）是一门快速、轻量、安全、采用渐进式类型化且支持嵌入的脚本语言，派生自 Lua，目前 Luau 0.524 发布了，该版本带来如下变更：</span></p> 
<h2><strong>Analysis changes</strong></h2> 
<ul> 
 <li>改进不同模块中定义的类的类型不匹配错误</li> 
 <li>非严格类型推断现在自动推断函数返回类型，类似于严格模式</li> 
 <li>改进 <span style="color:#24292f">luau-analyze --annotate 数组和 for 循环的输出</span></li> 
 <li>修复 CMake 构建中的 GCC9 警告</li> 
</ul> 
<h2><strong>Runtime changes</strong></h2> 
<ul> 
 <li>通过减少临时分配，使字节码编译器速度提高约 5%</li> 
 <li><span style="color:#2e3033">当使用新的优化级别 2 (在 CLI 中是 -O2)，展开短 for 循环对字节码编译器是有利的</span></li> 
 <li>改进增量 GC 的节奏，以使 GC 工作量更加均匀</li> 
 <li>减少 GC 期间的扫描速度</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRoblox%2Fluau%2Freleases%2Ftag%2F0.524" target="_blank">https://github.com/Roblox/luau/releases/tag/0.524</a></p>
                                        </div>
                                      
</div>
            