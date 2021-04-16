
---
title: 'Docker 20.10.6 发布，正式支持 Apple M1'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8423'
author: 开源中国
comments: false
date: Fri, 16 Apr 2021 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8423'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Docker 20.10.6 现已发布，具体更新内容如下：</p> 
<p><strong>Client</strong></p> 
<ul> 
 <li>Apple Silicon (darwin/arm64) 对 Docker CLI 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcli%2Fpull%2F3042" target="_blank">docker/cli#3042</a></li> 
 <li>config：当退回到 v1.7.0 之前的配置文件<code>~/.dockercfg</code>时，print 弃用警告。对该文件的支持将在未来的版本中删除 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdocker%2Fcli%2Fpull%2F3000" target="_blank">docker/cli#3000</a></li> 
</ul> 
<p><strong>Builder</strong></p> 
<ul> 
 <li>修复 Classic builder silently ignoring 不支持的 Dockerfile 选项，并提示启用 BuildKit 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42197" target="_blank">moby/moby#42197</a></li> 
</ul> 
<p><strong>Logging</strong></p> 
<ul> 
 <li>json-file：修复偶发的意外 EOF 错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42174" target="_blank">moby/moby#42174</a></li> 
</ul> 
<p><strong>Networking</strong></p> 
<ul> 
 <li>修复了 docker 20.10 中的回归问题，导致 IPv6 地址在映射端口时不再被默认绑定 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42205" target="_blank">moby/moby#42205</a></li> 
 <li>修复 API 响应中不包含隐式 IPv6 端口映射的问题。在 docker 20.10 之前，默认情况下，发布的端口可以通过 IPv4 和 IPv6 访问，但 API 只包括 IPv4 (0.0.0.0) 映射的信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42205" target="_blank">moby/moby#42205</a></li> 
 <li>修复 docker 20.10 中的回归问题，导致 docker-proxy 在所有情况下都不会被终止  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42205" target="_blank">moby/moby#42205</a></li> 
 <li>修复 iptables 转发规则在容器 removal 后无法清理的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42205" target="_blank">moby/moby#42205</a></li> 
</ul> 
<p><strong>Plugins</strong></p> 
<ul> 
 <li>修复 docker 插件创建与旧版 Docker 不兼容的插件的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Fpull%2F42256" target="_blank">moby/moby#42256</a></li> 
</ul> 
<p>更多更新信息可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.docker.com%2Fengine%2Frelease-notes%2F%2320106" target="_blank">https://docs.docker.com/engine/release-notes/#20106</a></p>
                                        </div>
                                      
</div>
            