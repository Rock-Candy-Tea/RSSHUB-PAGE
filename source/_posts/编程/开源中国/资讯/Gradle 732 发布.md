
---
title: 'Gradle 7.3.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9457'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9457'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Gradle 7.3.2 现已发布。Gradle 是一个基于 Apache Ant 和 Apache Maven 概念的项目自动化构建工具，支持依赖管理和多项目，类似 Maven，但比之简单轻便。它使用一种基于 Groovy 的特定领域语言来声明项目设置，而不是传统的 XML。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>这是 Gradle 7.3 的补丁版本，官方建议用户进行升级。它修复了以下问题：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F19300" target="_blank">#19300</a> Gradle 构建中 log4j 漏洞的缓解措施</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F19257" target="_blank">#19257</a> 使用 $ 字符重命名类名时增量 java 编译失败</li> 
</ul> 
<p>Log4Shell 漏洞相关的详情可查看此<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.gradle.org%2Flog4j-vulnerability" target="_blank">博客</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>升级说明</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">通过更新包装器将构建切换为使用 Gradle 7.3.2：</p> 
<div> 
 <pre><code>./gradlew wrapper --gradle-version=7.3.2</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.3.2%2Fuserguide%2Fupgrading_version_7.html%23changes_7.3" target="_blank">Gradle 7.x 升级指南</a>，了解升级到 Gradle 7.3.2 时的弃用、突破性变化和其他注意事项。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Freleases%2Ftag%2Fv7.3.2" target="_blank">https://github.com/gradle/gradle/releases/tag/v7.3.2</a></p>
                                        </div>
                                      
</div>
            