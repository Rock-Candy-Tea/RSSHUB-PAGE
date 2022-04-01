
---
title: 'Kitex v0.2.1 发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4443'
author: 开源中国
comments: false
date: Fri, 01 Apr 2022 02:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4443'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:left">Bugfix</h2> 
<ul> 
 <li> 修复(generic)：在泛化调用的时候检查 IDL 是否有循环依赖。</li> 
 <li> 修复(tool)：修复 protobuf CombineService 缺失 streaming 引用的问题。</li> 
 <li> 修复(client)：修复 oneway 请求的 sequence ID 没有被编码的问题以及降低 oneway 调用的丢包率。</li> 
 <li> 修复(generic/tool)：修复 CombineServices 可能存在多次加载同一个 service 问题。</li> 
</ul> 
<h2 style="text-align:left">Optimise</h2> 
<ul> 
 <li> 优化(diagnosis)：lbcaches 是全局的，无需为每个 client 注册 ProbeFunc 用于诊断查询。</li> 
 <li> 优化(rpcinfo)：RPCInfo.To().Tag() 优先使用服务发现的 instance tag 而不是 remoteinfo tag。</li> 
 <li> 优化(连接池)：修改默认的连接池最小空闲等待时间为 2s。</li> 
 <li> 优化(hook)：为<span> </span><code>onServerStart</code>和<span> </span><code>onShutdown</code>添加资源锁，当做一些如<code>RegisterStartHook</code>和<span> </span><code>server.Run</code>中的<span> </span><code>range</code>之类的读写操作时请求对应的资源锁。</li> 
 <li> 优化(discovery)：增加「实例不存在」错误定义。</li> 
</ul> 
<h2 style="text-align:left">Refactor</h2> 
<ul> 
 <li> 重构(event)：删除额外的原子操作并用普通赋值操作替换。</li> 
 <li> 重构(loadbalancer)：将 buildWeightedVirtualNodes 函数合入 buildVirtualNodes 函数中，成为一个函数。</li> 
</ul> 
<h2 style="text-align:left">Chore</h2> 
<ul> 
 <li> 升级依赖 choleraehyq/pid 以兼容 Go 1.18。</li> 
</ul> 
<h2 style="text-align:left">Docs</h2> 
<ul> 
 <li> 更新 README 到新博客的链接。</li> 
</ul> 
<p><strong>更多资讯</strong></p> 
<ul> 
 <li> <p>Kitex:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex" target="_blank">https://github.com/cloudwego/kitex</a></p> </li> 
 <li> <p>原文：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.cloudwego.io%2Fzh%2Fblog%2F2022%2F03%2F24%2Fkitex-v0.2.1-%25E7%2589%2588%25E6%259C%25AC%25E5%258F%2591%25E5%25B8%2583%2F" target="_blank">Kitex v0.2.1 版本发布 | CloudWeGo</a></p> <p> </p> </li> 
</ul> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            