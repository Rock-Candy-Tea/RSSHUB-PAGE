
---
title: 'Docker Desktop 3.3.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2913'
author: 开源中国
comments: false
date: Sat, 10 Apr 2021 07:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2913'
---

<div>   
<div class="content">
                                                                                            <p>Docker是一套平台即服务(PaaS)产品，它使用操作系统级别的虚拟化，以称为容器的包的形式交付软件。容器之间相互隔离，并捆绑自己的软件、库和配置文件；它们可以通过定义良好的渠道相互通信，因为所有的容器共享一个操作系统内核的服务，所以它们使用的资源比虚拟机少。</p> 
<h3>新特性：</h3> 
<p>用户现在可以指定何时下载和安装 Docker Desktop 更新。当更新可用时，Docker Desktop 会显示一个图标，表示有较新的版本。用户可以在方便的时候在后台下载更新。下载完成后，您只需点击更新并重新启动即可安装最新的更新。</p> 
<p>出于专业开发目的使用 Docker Desktop 的开发人员有时可能需要跳过特定的更新。为此，专业或团队的开发人员可以在出现提醒时跳过特定更新的通知。</p> 
<h3>升级</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcompose%2Freleases%2Ftag%2F1.29.0" target="_blank">Docker Compose 1.29.0</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcompose-cli%2Ftree%2Fv1.0.12" target="_blank">Compose CLI v1.0.12</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Flayers%2Fdocker%2Ffor-desktop-kernel%2F5.10.25-6594e668feec68f102a58011bb42bd5dc07a7a9b%2Fimages%2Fsha256-80e22cd9c9e6a188a785d0e23b4cefae76595abe1e4a535449627c2794b10871%3Fcontext%3Drepo" target="_blank">Linux kernel 5.10.25</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnyk%2Fsnyk%2Freleases%2Ftag%2Fv1.461.0" target="_blank">Snyk v1.461.0</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fhub-tool%2Freleases%2Ftag%2Fv0.3.1" target="_blank">Docker Hub Tool v0.3.1</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcontainerd%2Fcontainerd%2Freleases%2Ftag%2Fv1.4.4" target="_blank">containerd v1.4.4</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopencontainers%2Frunc%2Freleases%2Ftag%2Fv1.0.0-rc93" target="_blank">runc v1.0.0-rc93</a></li> 
</ul> 
<h3>错误修复和细微变化</h3> 
<ul> 
 <li>修正了查看以显式项目名启动的编译程序时的问题；</li> 
 <li>修复了 <code>--add-host host.docker.internal:host-gateway</code> 会导致 <code>host.docker.internal</code> 解析到错误 IP 地址的问题；</li> 
 <li>修正了一个导致容器间 HTTP 流量被错误地路由到外部 HTTP 代理的 bug；</li> 
 <li>修正了一个 Bug，当磁盘调整大小时，可能会导致虚拟机磁盘同一文件夹中的其他文件被删除；</li> 
 <li>修正了 delta 下载会导致 <code>Illegal instruction exception</code> 的问题；</li> 
 <li>为加密连接应用基于域的 HTTPS 代理 no_proxy 规则；</li> 
 <li>修正重设为出厂预设值对话框中缺失的文字；</li> 
 <li>修正了一个问题，即在主机上以随机端口运行容器会导致 Docker Desktop 仪表板错误地打开端口为 0 的浏览器，而不是使用分配的端口；</li> 
 <li>修正了一个问题，即使用 Docker Desktop 仪表板从 Docker Hub 拉取映像时操作失败而无提示；</li> 
 <li>删除了未使用的 DNS 名称 <code>docker.for.mac.http.internal</code> ；</li> 
 <li>启动 Linux 虚拟机时执行文件系统检查；</li> 
 <li>检测 Linux 内核崩溃并将其上报给用户。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.docker.com%2Fdocker-for-mac%2Frelease-notes%2F" target="_blank">https://docs.docker.com/docker-for-mac/release-notes/</a></p>
                                        </div>
                                      
</div>
            