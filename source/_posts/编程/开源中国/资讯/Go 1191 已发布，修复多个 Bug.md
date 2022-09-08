
---
title: 'Go 1.19.1 已发布，修复多个 Bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9363'
author: 开源中国
comments: false
date: Thu, 08 Sep 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9363'
---

<div>   
<div class="content">
                                                                                            <p>Go1.19.1 已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fgo%2Freleases%2Ftag%2Fgo1.19.1" target="_blank">发布</a>，此版本包含对<code>net/http</code> 和 <code>net/url</code> 包的安全修复，以及对编译器、<code>go</code>命令、<code>pprof</code>命令、链接器、运行时和 <code>crypto/tls</code> / <code>crypto/x509</code>包的错误修复。</p> 
<p>下面是该版本修复的部分 Bug：</p> 
<ul> 
 <li>cmd/go:使用 <code>unix</code> 构建约束导入依赖项时出现 <code>cannot find package</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fgo%2Fissues%2F54736" target="_blank"><span style="color:var(--color-fg-muted)!important">#54736</span></a></li> 
 <li>cmd/compile:  "Value live at entry" 编译失败问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fgo%2Fissues%2F54726" target="_blank"><span style="color:var(--color-fg-muted)!important">#54736</span></a><span style="color:var(--color-fg-muted)!important"> </span></li> 
 <li>cmd/compile: 使用泛型类型的未绑定方法编译代码时，出现内部编译器错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fgo%2Fissues%2F54243" target="_blank"><span style="color:var(--color-fg-muted)!important">#54243</span></a></li> 
 <li>cmd/go: 为提交生成 pseudo-versions 时，git fetch 错误被丢弃的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fgo%2Fissues%2F54734" target="_blank">#54734</a> </li> 
 <li>cmd/go: TestScript 中的数据竞争 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fgo%2Fissues%2F54637" target="_blank"><span style="color:var(--color-fg-muted)!important">#54637</span></a></li> 
 <li>runtime：使用 Linux 内核 5.18 运行 ppc64/linux 二进制文件会出现<span style="color:var(--color-fg-muted)!important">段错误 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fgo%2Fissues%2F54665" target="_blank"><span style="color:var(--color-fg-muted)!important">#54665</span></a></li> 
 <li>net/http: 发送 GOAWAY 后，出现处理服务器错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fgo%2Fissues%2F54376" target="_blank"><span style="color:var(--color-fg-muted)!important">#54376</span></a><span style="color:var(--color-fg-muted)!important"> </span></li> 
 <li>misc/cgo: TestSignalForwardingExternal 有时会因错误的信号 SIGINT<span style="color:var(--color-fg-muted)!important"> 而失败 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fgo%2Fissues%2F54239" target="_blank"><span style="color:var(--color-fg-muted)!important">#54239</span></a></li> 
</ul> 
<p>更多内容可以查看 Go1.19.1 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fgo%2Fissues%3Fq%3Dmilestone%253AGo1.19.1%2Blabel%253ACherryPickApproved" target="_blank">milestone</a>。</p>
                                        </div>
                                      
</div>
            