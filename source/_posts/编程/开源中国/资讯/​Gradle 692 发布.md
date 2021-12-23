
---
title: '​Gradle 6.9.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5903'
author: 开源中国
comments: false
date: Thu, 23 Dec 2021 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5903'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Gradle 6.9.2 现已发布。Gradle 是一个基于 Apache Ant 和 Apache Maven 概念的项目自动化构建工具，支持依赖管理和多项目，类似 Maven，但比之简单轻便。它使用一种基于 Groovy 的特定领域语言来声明项目设置，而不是传统的 XML。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f">这是 Gradle 6.9 的补丁版本，包含从 Gradle 7.2 向后移植到 Gradle 6.x 的错误修复；官方建议用户进行升级。它修复了以下问题：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F18163" target="_blank">#18163</a> 修复 excludes for substituted dependencies</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F18164" target="_blank">#18164</a> POSIX shell 脚本改进</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F18697" target="_blank">#18697</a> 修复由 replacement / capability conflict 导致的损坏 resolution result</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F19328" target="_blank">#19328</a> Gradle 构建中 log4j 漏洞的缓解措施</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F19372" target="_blank">#19372</a> 选择了多个转换的工件</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Log4Shell 漏洞相关的详情可查看此</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.gradle.org%2Flog4j-vulnerability" target="_blank">博客文章</a>。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>升级说明</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">通过更新包装器将构建切换为使用 Gradle<span> </span><span style="color:#24292f">6.9.2</span>：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start">./gradlew wrapper --gradle-version=6.9.2</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f">可参阅 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F6.9.2%2Fuserguide%2Fupgrading_version_6.html%23changes_6.9" target="_blank"><span style="color:#24292f">Gradle 6.x 升级指南</span></a><span style="color:#24292f">，了解升级到 Gradle 6.9.2 时的弃用、重大更改和其他注意事项。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Freleases%2Ftag%2Fv6.9.2" target="_blank">https://github.com/gradle/gradle/releases/tag/v6.9.2</a></p>
                                        </div>
                                      
</div>
            