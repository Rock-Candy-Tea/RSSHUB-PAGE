
---
title: 'uBlock 1.34.0 发布，浏览器高效广告过滤插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3784'
author: 开源中国
comments: false
date: Wed, 17 Aug 2022 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3784'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">uBlock 是一款支持多浏览器的高效过滤工具，快速、有效且简洁，它不仅过滤广告，屏蔽广告的功能是通过支持 Adblock Plus 过滤规则语法实现的，因此它支持自定义过滤规则。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">uBlock 1.44.0 正式发布，此次更新内容如下：</p> 
<h3>新的程序修饰过滤器运算符：：matches-media()</h3> 
<p>参数必须是 MDN 上记录的有效媒体查询，即出现在 @media 规则和第一个左大括号之间的内容（包括需要时的括号）。</p> 
<p>最佳实践：</p> 
<p>在纯 CSS 选择器（如果有）之后使用 :matches-media()。</p> 
<ul> 
 <li>好：example.com###target-1 > .target-2:matches-media((min-width: 800px))</li> 
 <li>不好（尽管仍然有效）：example.com##:matches-media((min-width: 800px)) #target-1 > .target-2</li> 
</ul> 
<h3><strong>修复</strong></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2Fc521479ef9d9676e08fcd6751fde7330dce189e7" target="_blank">添加 0.5s mp3 可重定向资源</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2Fe62604f889a8bbe68a0dbbc09a5b946f35d417cb" target="_blank">将队列相关的初始化代码添加到 AMZN shim 脚本</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2Fb01d57ab631a7c5e39eadd6998382d1eaf0beae5" target="_blank">修复 DOM 检查器中的深色主题问题</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2F97befd116b75d1f768b8e663b90a15bb25fda4e9" target="_blank">更好地检测无效的化妆品过滤器</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2F019f3f1739b4292d4fc0e433cccebb6697319e7b" target="_blank">正确地将 3p 规则应用到 3p-script/3p-frame 单元格上</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2F9d81b7c4d9fedf16ba74493481c1136fde7b1f3e" target="_blank">acis scriptlet 中不存在时，跳过测试上下文</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2Fd00364860c0796ae4935b5b57634c991d6131bfe" target="_blank">忽略 ctrl keydown 事件处理程序中的自动重复事件</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2F2ff0abfb89390aec3efb68880aec3f92ce9ccade" target="_blank">修复 Thunderbird 的弹出面板</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2F6fbcfc51144bdc56cd87f3a621c9d60a57c70bb4" target="_blank">防止选取器大于视口</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2F798338e7fadc69fe6bd75428c9a8588840cbbe52" target="_blank">使用符合 WebAssembly-1.0 的函数名称</a></li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Freleases%2Ftag%2F1.44.0" target="_blank">https://github.com/gorhill/uBlock/releases/tag/1.44.0</a></p>
                                        </div>
                                      
</div>
            