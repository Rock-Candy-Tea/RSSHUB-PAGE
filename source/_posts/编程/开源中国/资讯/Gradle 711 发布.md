
---
title: 'Gradle 7.1.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4173'
author: 开源中国
comments: false
date: Sun, 04 Jul 2021 07:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4173'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Gradle 7.1.1 现已发布。Gradle 是一个基于 Apache Ant 和 Apache Maven 概念的项目自动化构建工具，支持依赖管理和多项目，类似 Maven，但比之简单轻便。它使用一种基于 Groovy 的特定领域语言来声明项目设置，而不是传统的 XML。</p> 
<p>v7.1.1 是 Gradle 7.1 的补丁版本，它修复了以下问题：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F17488" target="_blank">#17488</a>许多 Micronaut 构建在使用 Gradle 7.1 和 JDK 8 的 NPE 时失败</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F17548" target="_blank">#17548</a> [配置缓存] 任务不是最新的 SantaTracker</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F17542" target="_blank">#17542</a> [配置缓存] 过滤 FC，映射元素存储不正确</li> 
</ul> 
<p>官方建议用户升级到 7.1.1。</p> 
<p><strong>升级说明</strong></p> 
<p>通过更新包装器将构建切换为使用 Gradle 7.1.1：</p> 
<pre><code>./gradlew wrapper --gradle-version=7.1.1</code></pre> 
<p>参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.1.1%2Fuserguide%2Fupgrading_version_7.html%23changes_7.1" target="_blank">Gradle 7.x 升级指南</a>，了解升级到 Gradle 7.1.1 时的弃用、重大更改和其他注意事项。</p> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Freleases%2Ftag%2Fv7.1.1" target="_blank">https://github.com/gradle/gradle/releases/tag/v7.1.1</a></p>
                                        </div>
                                      
</div>
            