
---
title: 'Thanos v0.27.0 发布，大规模 Prometheus 集群解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9190'
author: 开源中国
comments: false
date: Thu, 07 Jul 2022 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9190'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Thanos 是一组组件，可以组成一个具有无限存储容量的高可用度量系统，可以在现有的 Prometheus 部署之上无缝添加。Thanos 是一个 CNCF 孵化项目。Thanos 利用 Prometheus 2.0 的存储格式，在任何对象存储中低成本地存储历史度量数据，同时保留快速查询延迟。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Thanos 0.27 正式发布，更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">修复</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5339" target="_blank">#5339</a><span> </span>接收：在 routerOnly 模式下运行时，中断 (SIGINT) 现在将退出进程。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5357" target="_blank">#5357</a><span> </span>存储：确保缓存键中的斜杠不再被路由器解释，来修复组缓存处理。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5427" target="_blank">#5427</a><span> </span>接收：修复 Ketama 哈希环复制一致性。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">新增</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5337" target="_blank">#5337</a><span> </span>Thanos 对象存储：将<code>prefix</code><span> </span>选项添加到存储桶。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5409" target="_blank">#5409</a><span> </span>S3：添加选项，强制 DNS 样式查找。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5408" target="_blank">#5408</a><span> </span>接收：添加对一致哈希环的支持。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Fpull%2F5402" target="_blank">#5402</a><span> </span>接收：实施 api/v1/status/tsdb。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthanos-io%2Fthanos%2Freleases%2Ftag%2Fv0.27.0" target="_blank">https://github.com/thanos-io/thanos/releases/tag/v0.27.0</a></p>
                                        </div>
                                      
</div>
            