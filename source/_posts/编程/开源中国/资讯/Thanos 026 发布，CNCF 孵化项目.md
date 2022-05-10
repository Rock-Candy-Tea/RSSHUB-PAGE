
---
title: 'Thanos 0.26 发布，CNCF 孵化项目'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6912'
author: 开源中国
comments: false
date: Tue, 10 May 2022 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6912'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Thanos 是一组组件，可以组成一个具有无限存储容量的高可用度量系统，可以在现有的 Prometheus 部署之上无缝添加。Thanos 是一个 CNCF 孵化项目。Thanos 利用 Prometheus 2.0 的存储格式，在任何对象存储中低成本地存储历史度量数据，同时保留快速查询延迟。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Thanos 0.26 正式发布，更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5281" target="_blank">#5281</a><span> </span>Blocks: 对文件系统路径和对象存储路径分别使用正确的分隔符</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5300" target="_blank">#5300</a><span> </span>Query: 在重复数据删除功能关闭的情况下，忽略查询的缓存。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新增</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5220" target="_blank">#5220</a><span> </span>Query Frontend: 增加<span> </span><code>--query-frontend.forward-header</code><span> </span>标志，将 headers 信息转发到下游查询器。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5250%2Ffiles" target="_blank">#5250</a><span> </span>Querier: 通过 GRPC 公开 Query 和 QueryRange API</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5290" target="_blank">#5290</a><span> </span>添加对 ppc64le 的支持</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">变化</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F4838" target="_blank">#4838</a><span> </span>Tracing: 偶然发现 Stackdriver 的客户端在跟踪 YAML 配置时废弃了<span> </span><code>type: STACKDRIVER</code><span> </span>，使用<span> </span><code>type: GOOGLE_CLOUD</code><span> </span>代替（为向后兼容保留<span> </span><code>STACKDRIVER</code><span> </span>类型）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5170" target="_blank">#5170</a><span> </span>All: 将 TLS 版本从 TLS1.2 升级到 TLS1.3</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5206" target="_blank">#5206</a><span> </span>Cache: 为 groupcache 的获取操作增加超时</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5231" target="_blank">#5231</a><span> </span>Tools: Bucket 验证工具忽略了带有删除标记的 blocks</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5255" target="_blank">#5255</a><span> </span>InfoAPI: 当 stores 还没有准备好时，设置 store API 不可用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5256" target="_blank">#5256</a><span> </span>更新 Prometheus 依赖至 v2.33.5</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5271" target="_blank">#5271</a><span> </span>DNS: 修复 miekgdns 解析器，使其也能使用 CNAME 记录</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">移除</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5145" target="_blank">#5145</a><span> </span>UI: 移除旧的 Prometheus UI.</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Freleases%2Ftag%2Fv0.26.0" target="_blank">https://github.com/thanos-io/thanos/releases/tag/v0.26.0</a></p>
                                        </div>
                                      
</div>
            