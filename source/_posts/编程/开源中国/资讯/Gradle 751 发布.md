
---
title: 'Gradle 7.5.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8123'
author: 开源中国
comments: false
date: Sun, 07 Aug 2022 07:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8123'
---

<div>   
<div class="content">
                                                                                            <p>Gradle 7.5.1 现已发布。<span style="background-color:#ffffff; color:#333333">Gradle 是一个基于 Apache Ant 和 Apache Maven 概念的项目自动化构建工具，支持依赖管理和多项目，类似 Maven，但比之简单轻便。它使用一种基于 Groovy 的特定领域语言来声明项目设置，而不是传统的 XML。</span></p> 
<p><span style="background-color:#ffffff; color:#02303a">这是 Gradle 7.5 系列的第一个补丁版本</span><span style="background-color:#ffffff; color:#24292f">，官方建议用户进行升级。</span><span><span><span><span style="color:#02303a"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>它修复了以下问题：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul style="list-style-type:disc; margin-left:1.5em; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F21269" target="_blank">#21269</a> JavaVersion.VERSION_18 仍标记为 @Incubating</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F21301" target="_blank">#21301</a> 将某些类型的配置属性传递给 Checkstyle 时出现 NullPointerException</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F21346" target="_blank">#21346</a> 当上游任务失败时，finalizers 的 finalizers 不再执行</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F21353" target="_blank">#21353</a> CheckStyle 失败，因为它没有配置 javaLauncher</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F21365" target="_blank">#21365</a> 更新升级指南以警告 Checkstyle 工作目录中的更改</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F21374" target="_blank">#21374</a> 将设置为具有 ValueSourceParameters.None 参数类型的 ValueSource provider 的任务属性存储到配置缓存中失败</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F21399" target="_blank">#21399</a> Gradle 7.5 Javadoc 插件因多模块聚合而损坏（由于设置 --source-path）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F21400" target="_blank">#21400</a> Scala 编译失败，“不支持 rt.jar (class sbt.internal.inc.DummyVirtualFile)”</li> 
</ul> 
<p style="text-align:start"><span><span><span><span style="color:#02303a"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>此版本包括<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.5.1%2Frelease-notes.html%23java18" target="_blank">使用 Java 18 构建代码和运行 Gradle、</a>使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.5.1%2Frelease-notes.html%23groovy4" target="_blank">Groovy 4 构建代码、</a>响应速度<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.5.1%2Frelease-notes.html%23continuous-build" target="_blank">更快的持续构建</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.5.1%2Frelease-notes.html%23dependency-diagnostics" target="_blank">改进的依赖解析诊断</a>以及<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.5.1%2Frelease-notes.html%23configuration-cache-improvements" target="_blank">配置缓存改进</a>以提高性能、为 JVM <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.5.1%2Frelease-notes.html%23adoptium-provisioning" target="_blank">提供 Adoptium 工具链</a>等等。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start">详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2F7.5.1%2Frelease-notes.html" target="_blank">https://docs.gradle.org/7.5.1/release-notes.html</a></p>
                                        </div>
                                      
</div>
            