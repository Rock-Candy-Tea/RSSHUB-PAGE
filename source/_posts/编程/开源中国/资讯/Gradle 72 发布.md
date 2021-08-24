
---
title: 'Gradle 7.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2259'
author: 开源中国
comments: false
date: Tue, 24 Aug 2021 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2259'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Gradle 7.2 现已发布。Gradle 是一个基于 Apache Ant 和 Apache Maven 概念的项目自动化构建工具，支持依赖管理和多项目，类似 Maven，但比之简单轻便。它使用一种基于 Groovy 的特定领域语言来声明项目设置，而不是传统的 XML。</p> 
<p>此版本增加了多项可用性改进，例如对 Scala 项目的工具链支持，并改进了操作系统之间的构建缓存命中率。当遇到问题和一些错误修复时，还有一些变更可以使远程 HTTP 构建缓存更具弹性。</p> 
<p>具体更新内容如下：</p> 
<p><strong>新功能和可用性改进</strong></p> 
<ul> 
 <li>对 Scala 项目的 Java 工具链支持</li> 
 <li>复制文件时保留转义序列</li> 
 <li>改进基于 HTTP header 的认证的凭证处理</li> 
 <li><code>dependencies</code> 和 <code>dependencyInsight</code> 支持配置名称缩写</li> 
 <li>版本目录改进</li> 
 <li>支持声明 sub-accessors</li> 
 <li>支持声明插件版本</li> 
</ul> 
<p><strong>性能优化</strong></p> 
<ul> 
 <li>改进操作系统之间的构建缓存命中率</li> 
 <li>对 Groovy 和 Scala 项目的配置缓存支持</li> 
</ul> 
<p><strong>远程构建缓存的可靠性改进</strong></p> 
<ul> 
 <li>出现临时网络错误时可自动重试上传</li> 
 <li>默认跟随重定向</li> 
 <li>使用 Expect-Continue 避免冗余上传</li> 
</ul> 
<p>此外，Gradle 7.2 还修复了共计 51 个 issue。</p> 
<p>更多详情可查看官方公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.2%2Frelease-notes.html" target="_blank">https://docs.gradle.org/7.2/release-notes.html</a></p>
                                        </div>
                                      
</div>
            