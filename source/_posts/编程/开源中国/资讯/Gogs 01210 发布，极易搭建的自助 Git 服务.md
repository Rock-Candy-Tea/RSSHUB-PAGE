
---
title: 'Gogs 0.12.10 发布，极易搭建的自助 Git 服务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3311'
author: 开源中国
comments: false
date: Wed, 03 Aug 2022 15:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3311'
---

<div>   
<div class="content">
                                                                                            <p>Gogs 0.12.10 已发布。</p> 
<blockquote> 
 <p>Gogs（<code>/gɑgz/</code>）项目旨在打造一个以最简便的方式搭建简单、稳定和可扩展的自助 Git 服务。使用 Go 语言开发使得 Gogs 能够通过独立的二进制分发，并且支持 Go 语言支持的<strong style="color:#24292f">所有平台</strong>，包括 Linux、macOS、Windows 和基于 ARM 的操作系统。</p> 
</blockquote> 
<p><strong>主要变化</strong></p> 
<ul> 
 <li>支持使用<code>[security] LOCAL_NETWORK_ALLOWLIST = *</code><span> 以允许所有主机名 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogs%2Fgogs%2Fpull%2F7111" target="_blank">#7111</a></li> 
</ul> 
<p style="text-align:start"><strong>Bugfix</strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">配置</span><code>[security] LOCAL_NETWORK_ALLOWLIST</code><span style="background-color:#ffffff; color:#24292f">后无法将 webhook 发送到本地网络地址</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogs%2Fgogs%2Fissues%2F7074" target="_blank">#7074</a></li> 
 <li>Security:<span> </span>在文件编辑器中发现系统命令行注入<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogs%2Fgogs%2Fissues%2F7000" target="_blank">#7000</a></li> 
 <li>Security:<span> </span>在仓库 issue 列表清理<code>DisplayName</code><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogs%2Fgogs%2Fpull%2F7009" target="_blank">#7009</a></li> 
 <li>Security:<span> </span>Windows 文件编辑器中的路径遍历问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogs%2Fgogs%2Fissues%2F7001" target="_blank">#7001</a></li> 
 <li>Security:<span> </span>Git HTTP 端点的路径遍历<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogs%2Fgogs%2Fissues%2F7002" target="_blank">#7002</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">在 Windows 上创建期间无法初始化仓库</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogs%2Fgogs%2Fissues%2F6967" target="_blank">#6967</a></li> 
 <li>Mysterious panic on<span> </span><code>Value not found for type *repo.HTTPContext</code>.<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogs%2Fgogs%2Fissues%2F6963" target="_blank">#6963</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogs%2Fgogs%2Freleases%2Ftag%2Fv0.12.10" target="_blank">Release Note</a></p>
                                        </div>
                                      
</div>
            