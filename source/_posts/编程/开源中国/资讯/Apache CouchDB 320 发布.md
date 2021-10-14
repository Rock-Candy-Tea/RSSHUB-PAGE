
---
title: 'Apache CouchDB 3.2.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9501'
author: 开源中国
comments: false
date: Thu, 14 Oct 2021 06:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9501'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CouchDB 是一个完全拥抱 Web 的数据库。用 JSON 文档存储你的数据。通过 HTTP 和网络浏览器访问你的文档。用 JavaScript 查询、组合和转换你的文档。CouchDB 与现代 Web 和移动应用程序配合得很好。你可以使用 CouchDB 的增量复制，有效地分发你的数据。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CouchDB 3.2.0 值得关注的更新包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>couch_sever 模块现在是分片的。尽管遵循高并发进程的架构，以前的版本中使用的 couch_server 模块是一个单一的 Erlang 进程，在繁忙的节点上，可能会成为一个瓶颈。CouchDB 3.2.0 引入了一个 couch_server_N 模块，有效地消除了瓶颈。</li> 
 <li>复制调度程序管理在任何时间运行哪些复制。这对于复制总量多于配置为并发运行的设置非常重要。以前，复制调度器会以轮流方式迭代所有的复制，并给它们同等的时间来运行。CouchDB 3.2.0 引入了一个公平分享的选项，允许你使用多个复制器数据库，每个都有不同的相对优先级。</li> 
 <li>支持 Erlang 23 和 24 版本，放弃对 19 版本的支持</li> 
 <li>支持 SpiderMonkey 78 和 86 版本</li> 
 <li>解决了 CVE-2021-2838295</li> 
 <li>支持通过 regex 指定密码要求</li> 
 <li>在几乎所有情况下，日志不再包括凭证</li> 
 <li>更加细化的 CSP 配置</li> 
 <li>通过 .devcontainer，更容易对 3.x 系列进行开发设置</li> 
 <li>使得自动压缩不那么激进，在繁忙的集群中节省了 CPU 和 I/O</li> 
 <li>包括用于高级诊断的 weatherreport 模块</li> 
 <li>包括一个专门的 Prometheus 端点，用于统计和度量</li> 
 <li>所有的 JS 测试都已经迁移到 Elixir</li> 
 <li>……</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.couchdb.org%2Fen%2Fstable%2Fwhatsnew%2F3.2.html" target="_blank">https://docs.couchdb.org/en/stable/whatsnew/3.2.html</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            