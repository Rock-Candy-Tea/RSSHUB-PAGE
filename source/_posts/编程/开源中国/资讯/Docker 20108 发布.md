
---
title: 'Docker 20.10.8 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6722'
author: 开源中国
comments: false
date: Thu, 05 Aug 2021 06:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6722'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Docker 20.10.8 现已发布，具体更新内容如下：</p> 
<h4>弃用</h4> 
<ul> 
 <li>弃用对加密 TLS 私钥的支持。RFC 1423 中指定的传统 PEM 加密在设计上是不安全的。由于它不对密文进行身份验证，因此很容易受到可以让攻击者恢复 plaintext 的 padding oracle 攻击。对此功能的支持现已标记为已弃用，并将在即将发布的版本中删除。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcli%2Fpull%2F3219" target="_blank">docker/cli#3219</a></li> 
 <li>弃用 Kubernetes 堆栈支持。在 Kubernetes 上的 Compose 被弃用后，docker CLI 中的<code>stack</code>和<code>context</code>命令对 Kubernetes 的支持现在被标记为弃用，并将在即将发布的版本中移除。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcli%2Fpull%2F3174" target="_blank">docker/cli#3174</a></li> 
</ul> 
<h4>Client</h4> 
<ul> 
 <li>修复 Windows 上的“Invalid standard handle identifie”错误。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcli%2Fpull%2F3132" target="_blank">docker/cli#3132</a></li> 
</ul> 
<h4>Rootless</h4> 
<ul> 
 <li><code>dockerd-rootless.sh</code>：避免在 SELinux 主机上出现“无法打开 lock file /run/xtables.lock: Permission denied”错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42462" target="_blank">moby/moby#42462</a></li> 
 <li>在使用 SELinux 运行时禁用 overlay2 以防止出现权限拒绝的错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42462" target="_blank">moby/moby#42462</a></li> 
 <li>修复 openSUSE Tumbleweed 上的“509: certificate signed by unknown authority”错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42462" target="_blank">moby/moby#42462</a></li> 
</ul> 
<h4>Runtime</h4> 
<ul> 
 <li>当使用<code>--platform</code>选项拉出一个不符合主机原生架构的单架构镜像时，Print a warning。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42633" target="_blank">moby/moby#42633</a></li> 
 <li>修复使用 cgroups v2 运行时错误的“Your kernel does not support swap memory limit”警告。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42479" target="_blank">moby/moby#42479</a></li> 
 <li>Windows：修复了如果 HcsShutdownComputeSystem 返回<code>ERROR_PROC_NOT_FOUND</code>错误，容器未停止的情况。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42613" target="_blank">#42613</a> ]( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42613" target="_blank">#42613</a> )</li> 
</ul> 
<h4>Swarm</h4> 
<ul> 
 <li>修复了由于节点未能清理其旧的负载均衡器 IP 而可能存在重叠 IP 地址的可能性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42538" target="_blank">moby/moby#42538</a></li> 
 <li>修复日志代理中的死锁（“dispatcher is stopped”）。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42537" target="_blank">moby/moby#42537</a></li> 
</ul> 
<h4>Packaging</h4> 
<blockquote> 
 <p><strong>已知问题</strong></p> 
 <p>这个版本的静态包中的 ctr 二进制文件不是静态链接的，所以不能在使用 alpine 作为基础镜像的 Docker 镜像中运行。用户可以安装 libc6-compat 包，或者下载先前版本的 ctr 二进制文件作为解决方法。更多细节看参考与此问题相关的 containerd ticket：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcontainerd%2Fcontainerd%2Fissues%2F5824" target="_blank">containerd/containerd#5824</a>。</p> 
</blockquote> 
<ul> 
 <li>删除 Ubuntu 16.04 "Xenial" 和 Fedora 32 的 packaging，因为它们已达到 EOL <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fdocker-ce-packaging%2Fpull%2F560" target="_blank">docker/docker-ce-packaging#560</a></li> 
 <li>更新 Golang 运行时到 1.16.6</li> 
 <li>将 rpm 和 deb 软件包的捆绑 buildx 版本更新为 v0.6.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fdocker-ce-packaging%2Fpull%2F562" target="_blank">docker/docker-ce-packaging#562</a></li> 
 <li>将静态二进制文件和 containerd.io rpm 和 deb 包更新到 containerd v1.4.9 和 runc v1.0.1：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcontainerd-packaging%2Fpull%2F241" target="_blank">docker/containerd-packaging#241</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcontainerd-packaging%2Fpull%2F245" target="_blank">docker/containerd-packaging#245</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcontainerd-packaging%2Fpull%2F247" target="_blank">docker/containerd-packaging#247</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Freleases%2Ftag%2Fv20.10.8" target="_blank">https://github.com/moby/moby/releases/tag/v20.10.8</a> </p>
                                        </div>
                                      
</div>
            