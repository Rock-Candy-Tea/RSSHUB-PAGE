
---
title: 'Eclipse OpenJ9 v0.27.0 发布，Java 虚拟机'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5118'
author: 开源中国
comments: false
date: Fri, 30 Jul 2021 07:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5118'
---

<div>   
<div class="content">
                                                                                            <p>Eclipse OpenJ9 v0.27.0 已发布，Eclipse OpenJ9 是 OpenJDK 的 JVM，由 IBM 创建并捐赠给 Eclipse 基金会。此 Java 虚拟机经过优化，具备占用空间小、启动速度快以及吞吐量高等优势。</p> 
<p>OpenJ9 0.27 提供了对 OpenJDK 8、11 和 16 的支持，并添加了一个新的 AdaptiveGCThreading 选项，可对自动调整的活跃并行 GC 线程的默认行为进行操作。此外还增加了新的扫描模式，可在平衡 GC 策略中使用。</p> 
<p>其他的主要变化：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Fopenj9%2Fdocs%2Fversion0.27%2F%23binaries-and-supported-environments" target="_blank">带来新的二进制文件，以及针对受支持的环境的变更</a></li> 
 <li>添加新的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Fopenj9%2Fdocs%2Fversion0.27%2F%23new-xx-adaptivegcthreading-option-added" target="_blank"><code>-XX:[+|-]AdaptiveGCThreading</code></a>选项</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Fopenj9%2Fdocs%2Fversion0.27%2F%23improved-time-zone-information-added-to-java-dump-files" target="_blank">改进时区信息，将其添加到 Java dump 文件</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Fopenj9%2Fdocs%2Fversion0.27%2F%23change-in-default-behavior-for-the-balanced-garbage-collection-gc-policy" target="_blank"><code>balanced</code></a>垃圾回收策略的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Fopenj9%2Fdocs%2Fversion0.27%2F%23change-in-default-behavior-for-the-balanced-garbage-collection-gc-policy" target="_blank">默认行为变更</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Fopenj9%2Fdocs%2Fversion0.27%2F%23stop-parsing-the-java_options-environment-variable" target="_blank">停止解析 JAVA_OPTIONS 环境变量</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Fopenj9%2Fdocs%2Fversion0.27%2F%23global-lock-reservation-enabled-by-default" target="_blank">默认启用全局 lock reservation</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Fopenj9%2Fdocs%2Fversion0.27%2F%23increase-in-default-operating-system-stack-size-on-ppc64-platforms" target="_blank">增加 PPC64 平台上默认操作系统的堆栈大小</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.eclipse.org%2Fopenj9%2Fdocs%2Fversion0.27%2F%23new-x-option-recognized-by-jpackcore-jextract" target="_blank">添加新的<code>-x</code>选项到<code>jpackcore</code> / <code>jextract</code></a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feclipse-openj9%2Fopenj9%2Freleases%2Ftag%2Fopenj9-0.27.0" target="_blank">源码下载</a></p> 
<p>完整的变更信息查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feclipse-openj9%2Fopenj9%2Fblob%2Fmaster%2Fdoc%2Frelease-notes%2F0.27%2F0.27.md" target="_blank">release note</a>。</p>
                                        </div>
                                      
</div>
            