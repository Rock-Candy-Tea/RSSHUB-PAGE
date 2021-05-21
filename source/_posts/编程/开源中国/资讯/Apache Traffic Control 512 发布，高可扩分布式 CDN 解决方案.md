
---
title: 'Apache Traffic Control 5.1.2 发布，高可扩分布式 CDN 解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7849'
author: 开源中国
comments: false
date: Fri, 21 May 2021 07:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7849'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Traffic Control 5.1.2 现已发布。Apache Traffic Control 是一个分布式、可扩展的冗余解决方案，实现了现代 CDN 的所有核心功能，可用于构建、监视和配置大型内容交付网络。</p> 
<p>此版本更新内容如下：</p> 
<p><strong>Fixed</strong></p> 
<ul> 
 <li>修复了 GET api cdns/routing 的返回错误，以避免错误的 success response。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5712" target="_blank">＃5712-</a> 确保 5.x Traffic Stats 与 5.x Traffic Monitor 和 5.x Traffic Ops 兼容，并且不会 log all 0's for cache_stats</li> 
 <li>修复了 ORT 无法更新 Delivery Services 的 URLSIG 密钥的问题</li> 
 <li>修复了针对 mids 和拓扑结构的 ORT service category header 重写</li> 
 <li>修复了 Traffic Ops 不可用导致 Traffic Monitor 出现段故障和崩溃的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5754" target="_blank">＃5754-</a> 确保 Health Threshold Parameters 使用传统监测配置处理器的传统格式</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5695" target="_blank">＃5695-</a> 确保只针对受监控的接口计算 vitals</li> 
 <li>修复了 Traffic Monitor 以报告<code>ONLINE</code>缓存的可用性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5744" target="_blank">＃5744-</a> 按 DS 名称对 TM Delivery Service States 页面进行排序</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5724" target="_blank">＃</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5724" target="_blank">5724</a>- 如果服务器没有主机名，则将 XMPPID 设置为主机名，当 XMPPID 为空时，服务器更新时不会出错</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5739" target="_blank">＃5739-</a> 防止在尝试登录失败时循环</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Freleases%2Ftag%2Fv5.1.2" target="_blank">https://github.com/apache/trafficcontrol/releases/tag/v5.1.2</a></p>
                                        </div>
                                      
</div>
            