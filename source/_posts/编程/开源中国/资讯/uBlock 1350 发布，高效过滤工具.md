
---
title: 'uBlock 1.35.0 发布，高效过滤工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4392'
author: 开源中国
comments: false
date: Thu, 22 Apr 2021 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4392'
---

<div>   
<div class="content">
                                                                    
                                                        <p>uBlock 是一款支持多浏览器的高效过滤工具，快速、有效且简洁，它不仅过滤广告，屏蔽广告的功能是通过支持 Adblock Plus 过滤规则语法实现的，支持自定义过滤规则。uBlock 1.35.0 正式发布，此次更新内容如下：</p> 
<h4>新功能：</h4> 
<p>新增过滤功能，可以从文档资源中删除特定的响应 header，例如：</p> 
<pre><code>example.com##^responseheader(refresh)
</code></pre> 
<p>只允许删除以下响应 header，其他的都会导致过滤器无效并被丢弃：</p> 
<ul> 
 <li><code>location</code></li> 
 <li><code>refresh</code></li> 
 <li><code>report-to</code></li> 
 <li><code>set-cookie</code></li> 
</ul> 
<h4>基于 Chromium 的浏览器</h4> 
<p>更新 uBlock 后，网站能够使用 FLoC API，但将无法从中获得结果 —— uBlock 会导致 API 调用失败，就像没有 FLoC 数据一样。</p> 
<h4>已修复</h4> 
<ul> 
 <li>在 Chrome/uBO 中阻止 FLoC 检查；</li> 
 <li>json-prune 不能通过全通配符删除所有属性；</li> 
</ul> 
<h4>没有在问题跟踪器中列出的提交：</h4> 
<ul> 
 <li>删除高级设置 <code>ignoreScriptInjectFilters</code> ；</li> 
 <li>最终确定第三方脚本/框架的迷你过滤小工具；</li> 
 <li>删除高级设置 <code>ignoreRedirectFilters</code> ；</li> 
 <li>修复用于在元素选择器中提取属性名称的重码；</li> 
 <li>增加对删除响应 headers 的支持；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Freleases%2Ftag%2F1.35.0" target="_blank">https://github.com/gorhill/uBlock/releases/tag/1.35.0</a></p>
                                        </div>
                                      
</div>
            