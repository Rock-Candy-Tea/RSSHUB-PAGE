
---
title: 'Lemmy v0.15.2 发布，高性能自托管仿 Reddit 社区'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8133'
author: 开源中国
comments: false
date: Mon, 31 Jan 2022 07:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8133'
---

<div>   
<div class="content">
                                                                                            <p>Lemmy v0.15.2 现已发布。Lemmy 是一个 Rust 实现的类似于 Reddit、Lobste.rs、Raddle 与 Hacker News 等网站的项目，用户订阅感兴趣的论坛、发布链接和讨论，可以进行点赞/点踩，并对它们发表评论。基于 Fediverse 标准，所有服务器可以联合，这意味着在一台服务器上注册的用户可以订阅任何其它服务器上的论坛，并且可以与在其它地方注册的用户进行讨论。</p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>一些错误修复如下：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>查看社区/用户配置文件时不要发出 webfinger 请求（修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F1896" target="_blank">#1896</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2049" target="_blank">#2049</a>）</li> 
 <li>登录时不区分大小写的用户名（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2010" target="_blank">#2010</a>）</li> 
 <li>将社区放在 webfinger 响应的最后（修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2037" target="_blank">#2037</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2047" target="_blank">#2047</a>）</li> 
 <li>不要检查 MarkCommentAsRead 中的禁令（修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2045" target="_blank">#2045</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2054" target="_blank">#2054</a>）</li> 
 <li>空帖子正文（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2050" target="_blank">#2050</a>）</li> 
 <li>添加 tombstone 测试，更好的测试错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2046" target="_blank">#2046</a>）</li> 
 <li>对于数组也接受单个对象（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2048" target="_blank">#2048</a>）</li> 
 <li>清理可选的帖子。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2039" target="_blank">#2039</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2043" target="_blank">#2043</a> )</li> 
 <li>修复对被屏蔽者的点赞评论。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2033" target="_blank">#2033</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2042" target="_blank">#2042</a> )</li> 
 <li>为 lotide federation 添加测试，使 lotide 组可获取（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2035" target="_blank">#2035</a>）</li> 
 <li>删除对活动流的不必要依赖（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2034" target="_blank">#2034</a>）</li> 
 <li>修复私有实例检查。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2064" target="_blank">#2064</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Fissues%2F2065" target="_blank">#2065</a> )</li> 
</ul> 
<p>更新说明： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLemmyNet%2Flemmy%2Freleases%2Ftag%2F0.15.2" target="_blank">https://github.com/LemmyNet/lemmy/releases/tag/0.15.2</a></p>
                                        </div>
                                      
</div>
            