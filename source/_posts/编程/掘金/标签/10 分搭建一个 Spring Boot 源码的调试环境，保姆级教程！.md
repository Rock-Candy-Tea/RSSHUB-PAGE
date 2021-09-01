
---
title: '10 分搭建一个 Spring Boot 源码的调试环境，保姆级教程！'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://www.iocoder.cn/images/Spring-Boot/2021-01-02/%E4%B8%8B%E8%BD%BD%20Gradle%20%E5%B7%A5%E5%85%B7.png'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 17:18:15 GMT
thumbnail: 'https://www.iocoder.cn/images/Spring-Boot/2021-01-02/%E4%B8%8B%E8%BD%BD%20Gradle%20%E5%B7%A5%E5%85%B7.png'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>友情提示：如果胖友对 Spring Boot 的使用不是很了解，可以看看艿艿写的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FYunaiV%2FSpringBoot-Labs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/YunaiV/SpringBoot-Labs" ref="nofollow noopener noreferrer">github.com/YunaiV/Spri…</a> 系列文章，大概有 <strong>100+</strong> 个 Spring Boot 使用案例。</p>
</blockquote>
<p>今儿，我们来搭建一个 Spring Boot 调试环境，目标是：<strong>启动 Spring Boot，成功调试它的启动过程</strong>。</p>
<p>视频可见 B 站：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1WA411P7Pz%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1WA411P7Pz/" ref="nofollow noopener noreferrer">www.bilibili.com/video/BV1WA…</a></p>
<p>😝 艿艿比较腼腆，大家给个三连支持一下，感恩 1024~</p>
<h1 data-id="heading-0">1. 依赖工具</h1>
<h2 data-id="heading-1">1.1 IDEA</h2>
<p>当然是 Jetbrains 出品的 IDEA 工具，相信绝大多数胖友都使用的它。</p>
<p>艿艿使用的是 <strong>2020.3</strong> 版本，胖友尽量保证不低于该版本哈。</p>
<h2 data-id="heading-2">1.2 JDK</h2>
<p>需要使用 JDK 编译 Spring Boot 的代码，这里艿艿使用的是 JDK <strong>1.8</strong> 版本</p>
<pre><code class="hljs language-Bash copyable" lang="Bash">$ java -version
java version <span class="hljs-string">"1.8.0_144"</span>
Java(TM) SE Runtime Environment (build 1.8.0_144-b01)
Java HotSpot(TM) 64-Bit Server VM (build 25.144-b01, mixed mode)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">2. 源码拉取</h1>
<p>使用 IDEA 从官方仓库 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/spring-projects/spring-boot" ref="nofollow noopener noreferrer">github.com/spring-proj…</a> 克隆项目。</p>
<blockquote>
<p>友情提示：如果网络不是很好的胖友，可以选择和艿艿一样，使用 Gitee 提供的镜像仓库 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fmirrors%2Fspring-boot" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/mirrors/spring-boot" ref="nofollow noopener noreferrer">gitee.com/mirrors/spr…</a></p>
</blockquote>
<p>这里，我们使用的 Spring Boot 版本是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fblob%2Fmain%2Fgradle.properties%23L1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/spring-projects/spring-boot/blob/main/gradle.properties#L1" ref="nofollow noopener noreferrer"><strong>2.6.0-SNAPSHOT</strong></a>。</p>
<blockquote>
<p>友情提示：胖友可以考虑 Fork 下<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/spring-projects/spring-boot" ref="nofollow noopener noreferrer">官方仓库</a>，为什么呢？</p>
<p>既然开始阅读、调试源码，我们可能会写一些注释，有了自己的仓库，可以进行自由的提交。😜</p>
</blockquote>
<h1 data-id="heading-4">3. 下载依赖</h1>
<p>① 克隆完成 Spring Boot 项目之后，IDEA 会自动下载需要的 Gradle 工具。如下图所示：</p>
<p><img src="https://www.iocoder.cn/images/Spring-Boot/2021-01-02/%E4%B8%8B%E8%BD%BD%20Gradle%20%E5%B7%A5%E5%85%B7.png" alt="下载 Gradle 工具" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里，我们使用的 Gradle 版本是 <strong>6.9</strong>。</p>
<blockquote>
<p>友情提示：由于是从国外的网址下载，所以需要耐心等待一会，艿艿花费了 2 分多钟。</p>
</blockquote>
<p>② 下载完 Gradle 工具之后，IDEA 就会使用它自动下载相关的依赖库。如下图所示：</p>
<p><img src="https://www.iocoder.cn/images/Spring-Boot/2021-01-02/%E4%B8%8B%E8%BD%BD%E4%BE%9D%E8%B5%96.png" alt="下载依赖" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为 Gradle 支持使用 Maven 依赖，所以我们可以使用阿里云的 Maven 镜像 <code>https://maven.aliyun.com/nexus/content/groups/public/</code>**。修改 <code>build.gradle</code> 文件，如下图所示：</p>
<p><img src="https://www.iocoder.cn/images/Spring-Boot/2021-01-02/%E4%B8%8B%E8%BD%BD%E4%BE%9D%E8%B5%962.png" alt="下载依赖" loading="lazy" referrerpolicy="no-referrer"></p>
<p>效果非常不错，不过艿艿还是花了 20 分钟才下载完了依赖。主要原因是，Spring Boot 内置了 50+ 个 Starter 的实现，导致引入了非常多的依赖。</p>
<p>ps：如果中间下载失败，点击【绿色刷新】按钮，继续下载依赖即可。</p>
<h1 data-id="heading-5">4. 调试 Spring Boot 示例</h1>
<p>依赖下载完后，我们通过调试 Spring Boot 提供的示例，了解 Spring Boot 的<strong>启动过程</strong>。在 <code>spring-boot-smoke-tests</code> 项目下，我们可以看到大量的示例，如下图所示：</p>
<p><img src="https://www.iocoder.cn/images/Spring-Boot/2021-01-02/Spring%20Boot%20%E7%A4%BA%E4%BE%8B.png" alt="Spring Boot 示例" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里，我们使用 <code>spring-boot-smoke-test-tomcat</code> 项目，最为熟悉的 Spring MVC + Tomcat 的组合。</p>
<p>① 在 SampleTomcatApplication 和 SpringApplication 分别打上断点，如下图所示：</p>
<p><img src="https://www.iocoder.cn/images/Spring-Boot/2021-01-02/%E6%89%93%E4%B8%8A%E6%96%AD%E7%82%B9.png" alt="打上断点" loading="lazy" referrerpolicy="no-referrer"></p>
<p>② Debug 运行 SampleTomcatApplication 类，首次构建会需要几秒钟，成功进入断点，可以愉快的调试 Spring Boot <strong>启动过程</strong>。如下图所示：</p>
<p><img src="https://www.iocoder.cn/images/Spring-Boot/2021-01-02/%E8%B0%83%E8%AF%95%20Spring%20Boot.gif" alt="调试 Spring Boot" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>更多 Spring 相关的文章，可以看看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.iocoder.cn%2FSpring%2Fgood-collection%2F%3Fjuejin" target="_blank" rel="nofollow noopener noreferrer" title="https://www.iocoder.cn/Spring/good-collection/?juejin" ref="nofollow noopener noreferrer">《Spring Framework 实现原理与源码解析》</a> 哟。</p>
<p>更多 Spring Boot 相关的文章，可以看看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.iocoder.cn%2FSpring-Boot%2Fgood-collection%2F%3Fjuejin" target="_blank" rel="nofollow noopener noreferrer" title="https://www.iocoder.cn/Spring-Boot/good-collection/?juejin" ref="nofollow noopener noreferrer">《Spring Boot 实现原理与源码解析》</a> 哟。</p>
<p>更多 Spring Cloud 相关的文章，可以看看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.iocoder.cn%2FSpring-Cloud%2Fgood-collection%2F%3Fjuejin" target="_blank" rel="nofollow noopener noreferrer" title="https://www.iocoder.cn/Spring-Cloud/good-collection/?juejin" ref="nofollow noopener noreferrer">《Spring Cloud 实现原理与源码解析》</a> 哟。</p>
</blockquote></div>  
</div>
            