
---
title: 'Sentry 21.12.0 发布，跨平台实时应用监控工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=267'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=267'
---

<div>   
<div class="content">
                                                                                            <p>Sentry 从根本上是一项服务，可跨平台实时监控和修复应用程序崩溃，它重点关注于错误报告。服务器使用 Python，但它包含一个完整的 API，用于在任何应用程序中从任何语言发送事件。Sentry 可以帮助你将 Python 程序的所有 exception 自动记录下来，然后在一个好用的 UI 上呈现和搜索。处理 exception 是每个程序的必要部分，所以 Sentry 也几乎可以说是所有项目的必备组件。</p> 
<p>目前， Sentry 发布了 21.12.0 版本，此版本带来以下内容：</p> 
<h3><strong>前端部署（进行中）</strong>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F28878" target="_blank">#28878</a> )</h3> 
<h3><strong>Python：添加对 Apple arm64 开发的支持（进行中）</strong></h3> 
<p>Apple 开始从基于 Intel 的芯片组转向 arm64 芯片组（又名 Apple Silicon）。<br> 为了在这个新架构上进行 Sentry 开发，需要对 Sentry 的开发环境进行各种更改。其中一些更改包括使用不同的 Python 版本（在 Python 3.8.10 上添加了 arm64 支持）、升级 Python 包和托管第三方维护者尚未发布的一些 Python 轮子（<span style="color:#24292f">wheels</span>）。</p> 
<p>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F30071" target="_blank">#30071</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F29739" target="_blank">#29739</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F29449" target="_blank">#29449</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F29315" target="_blank">#29315</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F29013" target="_blank">#29013</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F28769" target="_blank">#28769</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F28607" target="_blank">#28607</a>）</p> 
<h3><strong>Docker：添加对 Apple arm64 开发的支持（正在进行中）</strong></h3> 
<p>Apple 正在从基于 Intel 的芯片组转向 arm64 芯片组（又名 Apple Silicon）。为了对 Sentry 进行开发，需要启动各种 Docker 容器。</p> 
<p>这个里程碑跟踪了确保可以在 Apple 的 arm64 架构上使用这些开发服务所需的所有工作。</p> 
<p>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F29494" target="_blank">#29494</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F29293" target="_blank">#29293</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F29284" target="_blank">#29284</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F29157" target="_blank">#29157</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F29081" target="_blank">#29081</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F29117" target="_blank">#29117</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F29084" target="_blank">#29084</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F28672" target="_blank">#28672</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F28724" target="_blank">#28724</a>）</p> 
<h3><strong>连接仪表板和发现（进行中）</strong></h3> 
<p><span style="color:#2e3033">向仪表板添加发现查询（</span><span style="color:#24292f">Discover Query</span><span style="color:#2e3033">）部件。</span></p> 
<p><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F28699" target="_blank">#28699</a><span style="color:#24292f">, </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F28827" target="_blank">#28827</a><span style="color:#24292f">, </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F28745" target="_blank">#28745</a><span style="color:#24292f">, </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Fpull%2F28637" target="_blank">#28637</a><span style="color:#24292f">)</span></p> 
<p> </p> 
<p>除了上述内容，此版本还带来了大量 bug 修复和体验改进，详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgetsentry%2Fsentry%2Freleases%2Ftag%2F21.12.0" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            