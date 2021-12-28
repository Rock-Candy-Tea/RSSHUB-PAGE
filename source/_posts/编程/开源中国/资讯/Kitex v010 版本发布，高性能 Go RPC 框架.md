
---
title: 'Kitex v0.1.0 版本发布，高性能 Go RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1907'
author: 开源中国
comments: false
date: Tue, 28 Dec 2021 11:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1907'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">Kitex v0.1.0 版本已经发布，这是一个 <span style="background-color:#ffffff; color:#333333">Golang 微服务 RPC 框架，具有</span><strong style="color:#333333">高性能</strong><span style="background-color:#ffffff; color:#333333">、</span><strong style="color:#333333">强可扩展</strong><span style="background-color:#ffffff; color:#333333">的特点，在字节内部已广泛使用。如今越来越多的微服务选择使用 Golang，如果对微服务性能有要求，又希望定制扩展融入自己的治理体系，Kitex 会是一个不错的选择。</span></p> 
<p>此版本更新内容包括：</p> 
<h2 style="text-align:left">功能</h2> 
<h3 style="text-align:left">泛化调用</h3> 
<ul> 
 <li>IDL 解析支持多 Service</li> 
 <li>暴露 SetSeqID 方法便于二进制泛化场景 server 侧使用</li> 
 <li>泛化 client 支持关闭，规避内存泄漏问题</li> 
</ul> 
<h3 style="text-align:left">日志</h3> 
<ul> 
 <li>修改日志风格，使用 “key=value” 列出信息</li> 
 <li>使用 klog 作为全局的日志输出工具</li> 
 <li>使用全局的 default logger</li> 
 <li>日志打印更多 context 信息，例如 logId，方便问题排查</li> 
 <li>go func 传入服务信息用于 recover panic 后输出关键信息方便问题排查</li> 
</ul> 
<h3 style="text-align:left">Option</h3> 
<ul> 
 <li>增加 NewThriftCodecDisableFastMode 方法，来关闭 FastWrite 和 FastRead</li> 
 <li>Kitex server 支持端口复用</li> 
 <li>默认 RPC 超时设置为 0（在后续 PR 中，revert 了该变更）</li> 
</ul> 
<h3 style="text-align:left">Proxy</h3> 
<ul> 
 <li>Proxy 增加 ContextHandler 接口用于传递初始化ctx给 mwbuilder</li> 
 <li>注册 lbcache 的 Dump 给 diagnosis，用于问题诊断</li> 
 <li>将 PRCConfig 传递给 proxy.Config</li> 
</ul> 
<h2 style="text-align:left">优化</h2> 
<ul> 
 <li>减少了对象的堆分配</li> 
 <li>优化多路复用性能</li> 
 <li>优化 grpc 编解码性能，通过 Release 时释放(Close) LinkBuffer</li> 
 <li>在计算 backup request 的消耗(cost)时，区分 ErrRPCFinish</li> 
 <li>多路复用分片队列逻辑移动至 netpoll/mux，并重命名分片字典</li> 
 <li>优化Fast api中容器类型的长度编码逻辑</li> 
</ul> 
<h2 style="text-align:left">Bug 修复</h2> 
<ul> 
 <li>修复 server 端 WithErrorHandler 配置不生效问题</li> 
 <li>调整 lbcache 中的 Balancer 初始化逻辑</li> 
 <li>修复 TraceCtl 可能为 nil 的问题(仅影响单测)</li> 
 <li>设置默认的 rpc timeout, 并支持设置 WithRPCTimeout(0) 来关闭超时中间件</li> 
 <li>修复 default logger 使用错误的 call depth</li> 
 <li>重命名 BackwardProxy 为 ReverseProxy</li> 
 <li>修复 grpc 场景下的 panic</li> 
 <li>修复 grpc 场景下的潜在风险（keepalive 超时导致 panic）</li> 
 <li>修复 void 方法中的异常缺失</li> 
 <li>修复实例变更时 dump 信息不正确问题。</li> 
</ul> 
<h2 style="text-align:left">文档</h2> 
<ul> 
 <li>修复失效的中文链接</li> 
 <li>将全部 doc 移至官网 cloudwego.io</li> 
</ul> 
<h2 style="text-align:left">Netpoll API Change:</h2> 
<ul> 
 <li>适应 netpoll.Writer.Append 的 API 改动，返回值从 2个 变为 1个</li> 
</ul> 
<h2 style="text-align:left">依赖变化</h2> 
<ul> 
 <li>github.com/cloudwego/netpoll: v0.0.4 -> v0.1.2</li> 
</ul> 
<p>详情查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cloudwego.io%2Fzh%2Fblog%2F2021%2F12%2F13%2Fkitex-v0.1.0-%25E7%2589%2588%25E6%259C%25AC%25E5%258F%2591%25E5%25B8%2583%2F" target="_blank">https://www.cloudwego.io/zh/blog/2021/12/13/kitex-v0.1.0-%E7%89%88%E6%9C%AC%E5%8F%91%E5%B8%83</a></p>
                                        </div>
                                      
</div>
            