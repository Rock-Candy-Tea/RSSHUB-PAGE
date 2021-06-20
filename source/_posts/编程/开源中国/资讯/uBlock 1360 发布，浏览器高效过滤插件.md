
---
title: 'uBlock 1.36.0 发布，浏览器高效过滤插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5749'
author: 开源中国
comments: false
date: Sun, 20 Jun 2021 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5749'
---

<div>   
<div class="content">
                                                                    
                                                        <p>uBlock 是一款支持多浏览器的高效过滤工具，快速、有效且简洁，它不仅过滤广告，屏蔽广告的功能是通过支持 Adblock Plus 过滤规则语法实现的，支持自定义过滤规则。</p> 
<p>uBlock 1.36.0 正式发布，此次更新内容如下：</p> 
<h2>修复：</h2> 
<h3><strong>Chromium</strong></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FuBlockOrigin%2FuBlock-issues%2Fissues%2F1547" target="_blank">uBlock 在第一次运行时不加载 adminSettings</a></li> 
</ul> 
<h3><strong>Firefox</strong></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FuBlockOrigin%2FuBlock-issues%2Fissues%2F1620" target="_blank">在 React 组件中的 90,000 个 DOM 节点中进行 ajax 时出现奇怪的性能消耗</a></li> 
</ul> 
<h3><strong>Core</strong></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FuBlockOrigin%2FuBlock-issues%2Fissues%2F1629" target="_blank">Google Tag 管理器中的 eventCallback 在填充的 dataLayer 中没有被调用；</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FuBlockOrigin%2FuBlock-issues%2Fissues%2F1626" target="_blank">removeparam 过滤器会导致页面重定向问题</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FuBlockOrigin%2FuBlock-issues%2Fissues%2F1603" target="_blank">资产查看器在 !#endif 和 uBlock 列表中的注释行之间没有空格</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FuBlockOrigin%2FuBlock-issues%2Fissues%2F1570" target="_blank">管理扩展快捷方式中的文本包括转义 <code>&shy;</code></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FuBlockOrigin%2FuBlock-issues%2Fissues%2F1461" target="_blank">在弹出窗口中，如果过快地重新启用 Power 按钮，重新加载按钮会立即隐藏</a></li> 
</ul> 
<h3>其他</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2Fce801b952b5777775385efc00479405af54edbc9" target="_blank">将空数组、对象添加到 set-constant 脚本</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2F07d3c96261656e44f674550fbde50da8f6a15acc" target="_blank">修复转换为字符串时的潜在异常</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2F8cd2a1d263a96421487b39040c1d23eb01169484" target="_blank">使 googletagmanager_gtm.js 成为 google-analytics_analytics.js 的别名</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2Fe4b8f2ef2d0db2ef210e27b35849b0033809168d" target="_blank">确保使用适当的上下文调用 getter/setter</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2F001094580c0bd31ee007a301792f3e73c0ad48ab" target="_blank">允许通过上下文菜单订阅过滤器列表</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2Fd0e4c60f59201217cfa7c04d65f20af46f75da69" target="_blank">持续报告上次更新 "过时" 列表的时间</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Fcommit%2F1f8a67f40eb7293dcb8f4eba9a21cc122dc0d0eb" target="_blank">修复经典弹出面板中不正确的规则散列</a></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Freleases%2Ftag%2F1.36.0" target="_blank">https://github.com/gorhill/uBlock/releases/tag/1.36.0</a></p>
                                        </div>
                                      
</div>
            