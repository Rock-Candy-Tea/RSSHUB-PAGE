
---
title: 'Jina 3.8.0 发布，云原生神经搜索框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2025'
author: 开源中国
comments: false
date: Wed, 31 Aug 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2025'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Jina 是一个神经搜索框架，它使任何人都可以在几分钟内</span>在云上构建可扩展且可持续的神经搜索系统<span style="color:#333333">。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Jina 3.8.0 正式发布，本期主要更新如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>新的功能</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F527beb85a62eef9ec239406b986e43fcec28c2e7" target="_blank"><code>527beb85</code></a>] -升级 protobuf 版本 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5082" target="_blank">#5082</a>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2Fc47cb71637a9f72dd0f8710a7f93b3e6c6e9b238" target="_blank"><code>c47cb716</code></a>]<span> </span><strong>-</strong>添加失败和成功的请求数指标 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5079" target="_blank">#5079</a>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bug 修复</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2Fc81252aca7ba0c52650f7e915febe367a5e4828f" target="_blank"><code>c81252ac</code></a>]<span> </span><strong>-</strong>更新到 protobuf 4.21 的新类型 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5098" target="_blank">#5098</a>) </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>代码重构</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F6e51e815e534a8bf54d6629dc828fd50ace21bc0" target="_blank"><code>6e51e815</code></a>]<span> </span><strong>-</strong>重构数据请求处理程序监控 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5088" target="_blank">#5088</a>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>文档</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2Fb3fdb49cf4946796bc8b5fb8e5bc360f6f32bd0c" target="_blank"><code>b3fdb49c</code></a>]<span> </span><strong>-</strong>修正 jcloud 保留天数 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5096" target="_blank">#5096</a>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F98fb71f188fb71600db18ebd77809a36bfa9909c" target="_blank"><code>98fb71f1</code></a>]<span> </span><strong>-</strong>jcloud：调整 jcloud监控文档（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5081" target="_blank">#5081</a>）</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2Fdbea43f3f36fda3e111a7c0d58ea3b56b0146337" target="_blank"><code>dbea43f3</code></a>]<span> </span><strong>-</strong>从 jcloud 文档中删除 kong/alb (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5080" target="_blank">#5080</a>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>单元测试和 CICD</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F27ec3b41f8b49507aa5694db2ef020a9161576e7" target="_blank"><code>27ec3b41</code></a>]<span> </span><strong>-<span> </span></strong>清理 pip 安装 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5094" target="_blank">#5094</a>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2Fc0c3bf9a58cf59d6eea0cacabdb479b00d147b99" target="_blank"><code>c0c3bf9a</code></a>]<span> </span><strong>-</strong><span> </span>CI 中的降级 linkerd 版本 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5090" target="_blank">#5090</a>) </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Freleases%2Ftag%2Fv3.8.0" target="_blank">https://github.com/jina-ai/jina/releases/tag/v3.8.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            