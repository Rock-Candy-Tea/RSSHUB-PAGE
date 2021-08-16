
---
title: 'Apache Maven 3.8.2 发布，项目管理和构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=20'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 07:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=20'
---

<div>   
<div class="content">
                                                                                            <p>Apache Maven 3.8.2 发布了。Apache Maven 是一个项目管理和构建工具。基于项目对象模型（POM）的概念， Maven 可以从中心位置管理项目的构建、报告和文档。</p> 
<p>此版本更新内容如下：</p> 
<p><strong>Bug</strong></p> 
<ul> 
 <li>[MNG-4706] - 多线程构建可以为本地存储库中下载的工件创建错误文件</li> 
 <li>[MNG-5307] - 依赖项解析期间的 NPE - parallel mode</li> 
 <li>[MNG-5315] - Artifact resolution 在并行模式下偶尔会失败 </li> 
</ul> 
<p><strong>New Feature</strong></p> 
<ul> 
 <li>[MNG-7149] - 在 mvnDebug 脚本中引入 MAVEN_DEBUG_ADDRESS。</li> 
</ul> 
<p><strong>Improvement</strong></p> 
<ul> 
 <li>[MNG-2802] - 并发- 安全访问本地 Maven 存储库</li> 
 <li>[MNG-6471] - 并行构建器应使用模块名称作为线程名称</li> 
 <li>[MNG-6754] - 在多模块构建中设置相同的时间戳</li> 
 <li>[MNG-6810] - 删除 maven-model 中的配置文件</li> 
 <li>[MNG-6811] - 移除不必要的 filtering 配置</li> 
 <li>[MNG-6816] - 优先选择 System.lineSeparator() 而不是系统属性</li> 
 <li>[MNG-6827] - 替换已废弃的 StringUtils#defaultString()。</li> 
</ul> 
<p><strong>Dependency upgrade</strong></p> 
<ul> 
 <li>[MNG-6872] - 在你的依赖中发现 CVE - plexus-utils（测试）</li> 
 <li>[MNG-6874] - 将 Maven Parent 升级到 34 </li> 
 <li>[MNG-6886] - 升级 plexus-cipher 1.8 </li> 
 <li>[MNG-6993] - 将 SLF4J 升级到 1.7.30 </li> 
 <li>[MNG-7152] - 将 Maven 解析器升级到 1.6.3 </li> 
 <li>[MNG-7177] - 将 Maven Shared Utils 升级到 3.3.4</li> 
 <li>[MNG-7179] - 将 Jansi 升级到 2.3.3 </li> 
 <li>[MNG-7186] - 将 Guice 升级到 4.2.2 </li> 
 <li>[MNG-7196] - 将 Jansi 升级到 2.3.4</li> 
 <li>[MNG-7198] - 将 SLF4J 升级到 1.7.32</li> 
</ul> 
<p>更多详情可查看更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaven.apache.org%2Fdocs%2F3.8.2%2Frelease-notes.html" target="_blank">https://maven.apache.org/docs/3.8.2/release-notes.html</a> </p>
                                        </div>
                                      
</div>
            