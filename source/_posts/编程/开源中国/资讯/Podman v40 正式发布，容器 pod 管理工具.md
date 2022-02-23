
---
title: 'Podman v4.0 正式发布，容器 pod 管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0223/073303_Fm7l_2720166.png'
author: 开源中国
comments: false
date: Wed, 23 Feb 2022 07:58:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0223/073303_Fm7l_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>Podman 正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpodman.io%2Freleases%2F2022%2F02%2F22%2Fpodman-release-v4.0.0.html" target="_blank">发布</a>了全新的大版本——v4.0。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0223/073303_Fm7l_2720166.png" referrerpolicy="no-referrer"></p> 
<p>发布公告写道，Podman 4.0 是有史以来最重要的版本之一，增加了 60 多项新特性，主要更新内容是完全重写网络堆栈，以提升功能和性能。此外还有许多其他的变更，包括改进 Podman 对 Mac 和 Windows 的支持、改进 Pods、超过 50 个错误修复等。</p> 
<p>除了现有的 CNI 堆栈之外，Podman 现在还支持基于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcontainers%2Fnetavark" target="_blank">Netavark</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcontainers%2Faardvark-dns" target="_blank">Aardvark 的新网络堆栈。</a>新堆栈的特点是改进了对多个网络中容器的支持、改进 IPv6 支持，以及提升性能。为确保不会对现有用户产生影响，旧 CNI 堆栈将保持现有安装的默认值，而新安装将使用 Netvark。</p> 
<p>改进 Podman 对 Mac 和 Windows 的支持也是 Podman 4.0 的重要更新内容之一，其中最主要的变化是支持在主机系统上安装 Podman API 套接字，支持在主机系统上（不是在 podman machine VM 内）使用 Docker Compose 等工具。另外，podman machine 现在可以在 Windows 上使用 WSL2 作为后端，大大改进了 Podman 对 Windows 的支持。其他更多的功能包括支持从主机挂载卷，计划在 Podman v4.1 中提供。</p> 
<p>Podman Pods 也添加了许多新功能，以允许在 pod 中的容器之间共享资源。<code>podman pod create</code>命令的<code>--volume</code>和<code>--device</code>选项支持将卷和设备安装到 pod 中的每个容器，<code class="language-plaintext">--security-opt</code>和<code class="language-plaintext">--sysctl</code>选项支持为 pod 中的每个容器设置这些配置。按照开发团队的说法，这些更改只是他们计划的开始——最终，他们的目标是让<code class="language-plaintext">podman run</code>运行中的几乎所有选项对 pod 可用，以便在其中的容器之间轻松共享配置选项。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcontainers%2Fpodman%2Freleases%2Ftag%2Fv4.0.0" target="_blank">更多内容查看 release note</a>。</p>
                                        </div>
                                      
</div>
            