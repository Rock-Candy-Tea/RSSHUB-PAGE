
---
title: 'Docker 20.10.7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4931'
author: 开源中国
comments: false
date: Fri, 04 Jun 2021 07:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4931'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Docker 20.10.7 现已发布，具体更新内容如下：</p> 
<p><strong>Client</strong></p> 
<ul> 
 <li>禁止对已弃用的 cgroup 发出警告 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcli%2Fpull%2F3099" target="_blank">docker/cli#3099</a>。</li> 
 <li>防止在 Linux 和 macOS 上向容器发送<code>SIGURG</code>。Go 运行时（从 Go 1.14 开始）在内部使用<code>SIGURG</code>信号作为 interrupt 来支持可抢占的系统调用。在 Docker CLI 连接到容器的情况下，这些 interrupt 被转发给容器。此项修复改变了 Docker CLI，使其忽略了<code>SIGURG</code>信号 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcli%2Fpull%2F3107" target="_blank">docker/cli#3107</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42421" target="_blank">moby/moby#42421</a>。</li> 
</ul> 
<p><strong>Builder</strong></p> 
<ul> 
 <li>将 BuildKit 更新到 v0.8.3-3-g244e8cde 版本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42448" target="_blank">moby/moby#42448 </a>： 
  <ul> 
   <li>转换执行程序中 exec 挂载的相对挂载点，以解决 runc v1.0.0-rc94 及更高版本中的 breaking change。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fbuildkit%2Fpull%2F2137" target="_blank">moby/buildkit#2137</a>。</li> 
   <li>添加图像推送 5xx errors 时的重试。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fbuildkit%2Fpull%2F2043" target="_blank">moby/buildkit#2043</a>。</li> 
   <li>修复在重命名使用通配符复制的文件时，build-cache 不会失效的问题。请注意，此更改会使使用通配符的复制命令的现有构建缓存无效。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fbuildkit%2Fpull%2F2018" target="_blank">moby/buildkit#2018</a>。</li> 
   <li>修复使用 mounts 时 build-cache 不会失效的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fbuildkit%2Fpull%2F2076" target="_blank">moby/buildkit#2076</a>。</li> 
  </ul> </li> 
 <li>修复使用 legacy schema 1 images 时，<code>FROM</code>图像未被缓存的构建失败 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42382" target="_blank">moby/moby#42382</a>。</li> 
</ul> 
<p><strong>Logging</strong></p> 
<ul> 
 <li>更新 hcsshim SDK 以减少 Windows 上的守护进程日志 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42292" target="_blank">moby/moby#42292</a>。</li> 
</ul> 
<p><strong>Rootless</strong></p> 
<ul> 
 <li>修复了在启用了用户命名空间的守护进程上构建映像时不支持的功能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42352" target="_blank">moby/moby#42352</a>。</li> 
</ul> 
<p><strong>Networking</strong></p> 
<ul> 
 <li>更新 libnetwork 以修复在内核启动参数 ipv6.disable=1 的环境下发布端口的问题，并修复导致内部 DNS 查询失败的死锁问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42413" target="_blank">moby/moby#42413</a>。</li> 
</ul> 
<p><strong>Contrib</strong></p> 
<ul> 
 <li>将 rootlesskit 更新到 v0.14.2 以修复使用<code>slirp4netns</code>端口驱动程序启动用户态代理时的超时问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42294" target="_blank">moby/moby#42294</a>。</li> 
 <li>修复了在 rootless daemon 上运行 docker-in-docker 时出现的“设备或资源繁忙”错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42342" target="_blank">moby/moby#42342</a>。</li> 
</ul> 
<p><strong>Packaging</strong></p> 
<ul> 
 <li> <p>将 containerd 更新到 v1.4.6，runc v1.0.0-rc95 以解决 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-30465" target="_blank">CVE-2021-30465</a> 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42398" target="_blank">moby/moby#42398</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42395" target="_blank">moby/moby#42395</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcontainerd-packaging%2Fpull%2F234" target="_blank">ocker/containerd-packaging#234</a></p> </li> 
 <li>将 containerd 更新为 v1.4.5、runc v1.0.0-rc94 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42372" target="_blank">moby/moby#42372</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42388" target="_blank">moby/moby#42388</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42388" target="_blank">docker </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcontainerd-packaging%2Fpull%2F232" target="_blank">/containerd-packaging#232</a>。</li> 
 <li>将 Docker Scan 插件包 ( <code>docker-scan-plugin</code>)更新到 v0.8 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fdocker-ce-packaging%2Fpull%2F545" target="_blank">docker/docker-ce-packaging#545</a>。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Freleases%2Ftag%2Fv20.10.7" target="_blank">https://github.com/moby/moby/releases/tag/v20.10.7</a></p>
                                        </div>
                                      
</div>
            