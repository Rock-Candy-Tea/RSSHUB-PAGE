
---
title: 'Kong 2.8.0 发布，云原生 API 网关'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8120'
author: 开源中国
comments: false
date: Thu, 03 Mar 2022 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8120'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Kong 是一款可扩展、快速且开源的微服务 API 网关，用于管理、保护与连接混合及云原生架构。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前 Kong 发布了 2.8.0 版本，带来如下变更：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>弃用</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>外部<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fgo-pluginserver" target="_blank"><span> </span>go-plugin server<span> </span></a>项目默认被弃用，更倾向于<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.konghq.com%2Fgateway%2F2.7.x%2Freference%2Fexternal-plugins%2F" target="_blank">文档</a>中描述的嵌入式服务器方法。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">依赖项</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>OpenSSL 升级到 1.1.1m<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8191" target="_blank">#8191</a></li> 
 <li>将 resty.session 从 3.8 升级到 3.10<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8294" target="_blank">#8294</a></li> 
 <li>将 lua-resty-openssl 升级到 0.8.5<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8368" target="_blank">#8368</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新增</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>核心</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>可自定义的透明动态 TLS SNI 名称<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8196" target="_blank">#8196</a></li> 
 <li>路由支持使用正则表达式匹配标头<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F6079" target="_blank">#6079</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Beta</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Secrets Management 和 Vault 支持作为 Beta 功能引入，正在测试中<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8403" target="_blank">#8403</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>性能</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>改进了用于大型配置的声明式哈希配置的计算，新方法速度更快，使用的内存更少<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8204" target="_blank">#8204</a></li> 
 <li>路由器的多项改进：构建速度提高了一倍、更快地缓存和丢弃故障<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8087" target="_blank">#8087<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8010" target="_blank">#8010</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>插件</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>Response-ratelimiting</strong>：Redis ACL 支持，以及对用户名的通用 Redis 连接支持。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8213" target="_blank">#8213</a></li> 
 <li><strong>ACME</strong>：添加 rsa_key_size 配置选项  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8114" target="_blank">#8114</a></li> 
 <li><strong>Prometheus</strong><span> </span>: 添加了仪表来跟踪<span> </span><code>ngx.timer.running_count()</code><span> </span>和<span> </span><code>ngx.timer.pending_count()</code><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8387" target="_blank">#8387</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>管理 API</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">当 Kong 节点在 dbless 或数据平面模式下运行时，状态端点返回当前的声明性配置哈希。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8214" target="_blank">#8214</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8425" target="_blank">#8425</a> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fblob%2F2.8.0%2FCHANGELOG.md%23280" target="_blank">https://github.com/Kong/kong/blob/2.8.0/CHANGELOG.md#280</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            