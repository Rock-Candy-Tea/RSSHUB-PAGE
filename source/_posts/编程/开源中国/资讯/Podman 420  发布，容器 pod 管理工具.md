
---
title: 'Podman 4.2.0  发布，容器 pod 管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0812/151837_6rs4_2720166.png'
author: 开源中国
comments: false
date: Sat, 13 Aug 2022 07:30:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0812/151837_6rs4_2720166.png'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <p>Podman 4.2.0 已发布。</p> 
</div> 
<blockquote> 
 <p>Podman 是一个无守护进程的容器引擎，用于在 Linux 系统上开发、管理和运行 Open Container Initiative (OCI) 容器和容器镜像。Podman 提供了一个与 Docker 兼容的命令行前端，它可以作为 Docker CLI 使用，简单地说你可以直接添加别名：alias docker=podman 来使用 Podman。</p> 
 <p><img src="https://static.oschina.net/uploads/space/2022/0812/151837_6rs4_2720166.png" referrerpolicy="no-referrer"></p> 
</blockquote> 
<p><strong>更新亮点</strong></p> 
<ul> 
 <li style="text-align:start"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpodman-desktop.io%2F" target="_blank">Podman Desktop</a></strong></li> 
</ul> 
<p>团队表示，新项目 Podman Desktop 旨在将 Podman 更好地整合到 Linux、macOS 和 Windows，它提供了一个 GUI 来帮助开发者与 Podman 进行交互。Podman Desktop 目前处于早期阶段，功能包括：</p> 
<ul> 
 <li>列出所有镜像文件</li> 
 <li>与容器交互（访问日志、获取终端）</li> 
 <li>连接 registries（拉取私密镜像、推送镜像）</li> 
 <li>配置 Podman 设置项（例如代理）</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-45d71fabd344894f96375ff18fbf36bb128.png" referrerpolicy="no-referrer"></p> 
<p><strong>其他变化</strong></p> 
<ul> 
 <li>Podman 现在支持 Gitlab Runner（使用 Docker executor），允许在 Gitlab CI/CD 管道中使用它</li> 
 <li>添加新命令<code>podman pod clone</code>，用于创建现有 pod 的副本。它支持多个选项，包括<code>--start</code>启动新 pod、<code>--destroy</code>删除原始 pod 以及<code>--name</code>更改新 pod 的名称</li> 
 <li>添加新命令<code>podman volume reload</code>，用于在 Podman 的数据库和任何已配置的 volume 插件之间同步状态更改信息</li> 
 <li>添加新命令<code>podman machine info</code>，显示有关主机的信息和各种机器组件的版本</li> 
 <li>远程 Podman 客户端的<code>podman push</code>命令现在支持<code>--remove-signatures</code>选项</li> 
 <li>远程 Podman 客户端现在支持该<code>podman image scp</code>命令</li> 
 <li><code>podman image scp</code>命令现在支持使用新名称标记传输的镜像</li> 
 <li>……</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcontainers%2Fpodman%2Freleases%2Ftag%2Fv4.2.0" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            