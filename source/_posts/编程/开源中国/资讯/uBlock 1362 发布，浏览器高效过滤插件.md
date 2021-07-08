
---
title: 'uBlock 1.36.2 发布，浏览器高效过滤插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7840'
author: 开源中国
comments: false
date: Thu, 08 Jul 2021 06:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7840'
---

<div>   
<div class="content">
                                                                    
                                                        <p>uBlock 是一款支持多浏览器的高效过滤工具，快速、有效且简洁，它不仅过滤广告，屏蔽广告的功能是通过支持 Adblock Plus 过滤规则语法实现的，支持自定义过滤规则。</p> 
<p>uBlock 1.36.2 正式发布，此次更新内容如下：</p> 
<p>Core：</p> 
<ul> 
 <li>修复带有严格拦截过滤器的 DoS</li> 
 <li>修复通过记录器创建的 csp_report 过滤器被标记为无效的问题；</li> 
 <li>修复来自 hosts 文件的 ipv6 fe80::1%lo0 localhost 被标记为错误行的问题；</li> 
 <li>Whitespaces 现在被从拦截规则的 URL 中剥离，导致针对 Whitespaces 的规则失效和/或引起非常广泛地拦截；</li> 
</ul> 
<p>值得注意的提交：</p> 
<ul> 
 <li>为 remove-attr 脚本添加 asap 行为；</li> 
 <li>确保挂起的回调只被调用一次；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorhill%2FuBlock%2Freleases" target="_blank">https://github.com/gorhill/uBlock/releases</a></p>
                                        </div>
                                      
</div>
            