
---
title: 'Gradle 7.2 RC2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5146'
author: 开源中国
comments: false
date: Sun, 08 Aug 2021 07:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5146'
---

<div>   
<div class="content">
                                                                                            <p>Gradle 7.2 RC2<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Freleases%2Ftag%2Fv7.2.0-RC2" target="_blank"> 已发布</a>。</p> 
<p>此版本增加了多项可用性方面的改进，例如对 Scala 项目的工具链支持，并改进了操作系统之间的构建缓存命中率。此外，当遇到问题和一些错误修复时，还有部分变更可以使<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.2-rc-2%2Frelease-notes.html%23http-build-cache" target="_blank">远程 HTTP 构建缓存更具弹性</a>。</p> 
<p><strong>新功能和可用性改进</strong></p> 
<ul> 
 <li><span style="color:#02303a"><span style="background-color:#ffffff">对 Scala 项目的 Java 工具链支持</span></span></li> 
 <li><span style="color:#02303a"><span style="background-color:#ffffff">复制文件时保留转义序列</span></span></li> 
 <li><span style="color:#02303a"><span style="background-color:#ffffff">改进基于 HTTP header 的认证的凭证处理</span></span></li> 
 <li><code>dependencies</code> 和 <code>dependencyInsight</code> 支持配置名称缩写</li> 
 <li><span style="color:#02303a"><span style="background-color:#ffffff">版本目录改进</span></span></li> 
 <li>支持声明 sub-accessors</li> 
 <li>支持声明插件版本</li> 
</ul> 
<p><strong>性能优化</strong></p> 
<ul> 
 <li>改进操作系统之间的构建缓存命中率</li> 
 <li>对 Groovy 和 Scala 项目的配置缓存支持</li> 
</ul> 
<p style="text-align: start;"><strong><span style="color:null">远程构建缓存的可靠性改进</span></strong></p> 
<ul> 
 <li>出现临时网络错误时可自动重试上传</li> 
 <li>默认跟随重定向</li> 
 <li>使用 Expect-Continue 避免冗余上传</li> 
</ul> 
<p>除了以上这些变更，Gradle 7.2 还修复了共计 49 个 issue，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.2-rc-2%2Frelease-notes.html" target="_blank">详情查看 release notes</a>。</p>
                                        </div>
                                      
</div>
            