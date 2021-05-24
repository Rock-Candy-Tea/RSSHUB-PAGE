
---
title: 'Puma 5.3.2 发布，关注高并发的 Ruby HTTP 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1615'
author: 开源中国
comments: false
date: Mon, 24 May 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1615'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Puma 是一个简单、快速、线程化并且关注高并发的 HTTP 1.1 服务器，适用于开发和生产中的 Ruby/Rack 应用。</p> 
<p>Puma 5.3.2 正式发布，该版本更新内容如下：</p> 
<p>Bug 修复：</p> 
<ul> 
 <li>妥善处理 Rack 不接受 CLI 选项的情况；</li> 
 <li>修复 sigterm 错误行为；</li> 
 <li>改进 keepalive-connection shedding</li> 
</ul> 
<p>安全：</p> 
<ul> 
 <li>在快速内联请求达到最大数量后关闭 keepalive connections；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Freleases" target="_blank">https://github.com/puma/puma/releases</a></p>
                                        </div>
                                      
</div>
            