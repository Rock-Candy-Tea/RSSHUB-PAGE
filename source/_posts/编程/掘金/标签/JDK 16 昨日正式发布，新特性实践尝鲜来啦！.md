
---
title: 'JDK 16 昨日正式发布，新特性实践尝鲜来啦！'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd1be58f78ca4783b2be9c98261abd1c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 22 Mar 2021 00:07:53 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd1be58f78ca4783b2be9c98261abd1c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>JDK 16在2021年2月18日已完成最终候选版本，并于2021年3月16日正式发布。和JDK 15一样，JDK 16也会是一个短期版本，仅支持六个月。而计划在2021年9月发布的JDK 17将会是一个长期支持（LTS）版本，并获得数年的支持。虽然JDK 16是个短期版本，并且大部分的企业或者项目还依然停留在2018年9月发布的JDK 11（甚至更早的于2014年3月发布的JDK 8），但不妨碍Javaer对新版JDK的期待与持续学习的热情。
本文将与大家一起来玩一玩 JDK 16。</p>
</blockquote>
<h1 data-id="heading-0">新特性一览</h1>
<p>在开始之前，先让我们来一起浏览一下JDK 16版本所带来的17个新特性吧。</p>
<h2 data-id="heading-1">本文将解读的新特性</h2>
<p>357: OpenJDK源代码仓库从Mercurial迁移至Git。努力推动这一改变，将会在版本控制系统元数据大小、可用工具以及托管等方面体现优势。</p>
<p>369: 迁移到GitHub，这个变化是基于OpenJDK源码库迁移至Git的，JDK 16源代码仓库将出现在最流行的程序员社交网站上。</p>
<p>386: 在x64和AArch64架构上，将JDK移植到Alpine Linux和其他使用musl作为其主要C库的Linux发行版。Musl是 ISO C和Posix标准中描述的标准库功能的Linux实现。Alpine Linux由于其镜像小而被广泛应用于云部署、微服务以及容器环境中。Linux版本的Docker容器镜像小于6MB。让Java在此类设置中开箱即用地运行，并允许Tomcat、Jetty、Spring和其它流行的框架在这些环境中工作。通过使用jlink来减少Java运行时的大小，用户可以创建一个更小的镜像，以运行特定的应用程序。</p>
<p>394: instanceof操作符的模式匹配，在JDK 14和JDK 15中都已预览过，将于JDK 16最终确定。模式匹配使程序中的通用逻辑（即从对象中有条件的提取组件）可以更简洁、更安全的表达。</p>
<p>395: 提供Record记录类，作为不可变数据的透明载体。</p>
<h2 data-id="heading-2">其他的新特性</h2>
<p>347: 启用C++ 14语言功能，允许在JDK C++源代码中使用C++ 14功能，并提供有关在HotSpot代码中可以使用哪些功能的具体指导。</p>
<p>376: 将ZGC（可扩展低延迟垃圾收集器）线程堆栈处理从安全点移至并发阶段。ZGC垃圾收集器旨在使HotSpot中的GC暂停和可伸缩性问题成为过去。</p>
<p>380: 添加Unix-Domain Socket Channels，其中Unix-Domain（AF_UNIX）套接字的支持被添加到nio.channels包中的Socket Channel和Server Socket Channel API中。</p>
<p>387: 弹性Metaspace功能可将未使用的HotSpot虚拟机的Class Metadata(Metaspace)占用的内存更迅速的返回给操作系统，从而减少Metaspace的占用并简化Metaspace的代码以降低维护成本。</p>
<p>388: 将JDK移植到Windows/AArch64平台。</p>
<p>389: 孵化阶段的外部链接程序API，支持静态类型的纯Java方式访问本地代码。此计划的目的在于通过用更高级的纯Java开发模式来替换JNI（Java本机接口），以提供与C语言的交互。它的性能将会比JNI更加优越。</p>
<p>390: 基于值的类的警告建议：将原始包装类指定为基于值的类，弃用其构造函数以进行移除，并提示新的弃用警告。在Java平台中对于任何基于值的类的实例进行同步的错误尝试会予以警告。</p>
<p>392: 提供用于打包独立的Java应用程序的jpackage工具。</p>
<p>396: 默认情况下，JDK内部结构是强封装的，而关键内部API（例如misc.Unsafe）除外。此计划的目标包括提高JDK的安全性和可维护性，并鼓励开发人员从直接使用内部元素逐渐迁移为使用标准API，这样开发人员和最终用户都可以轻松地升级到 Java 的未来版本。</p>
<p>397: 之前在JDK 15中进行过预览，JDK 16中二次预览的密封类和接口限制了可以扩展或实现它们的类和接口。此计划的目标包括允许类或接口的创建者控制负责实现它的代码，提供比访问修饰符更声明性的方式来限制超类的使用，并通过提供模式分析基础来支持模式匹配的未来发展。</p>
<p>338: 孵化阶段的矢量API（JDK将配备一个孵化器模块），jdk.incubator.vector，以表达在可支持的CPU架构上编译为最佳硬件指令的矢量计算，以实现优于等效标量计算的性能。</p>
<p>393: 孵化阶段的外部存储器访问API，允许Java程序安全的访问Java堆外的外部存储器（包括本地、持久化介质以及托管堆存储器）。</p>
<p>如上新特性前编号为JDK Enhancement Process的标识符，详见文末参考资料</p>
<h1 data-id="heading-3">立即尝鲜</h1>
<p>浏览完17个新特性后，我都迫不及待的想尝试一下JDK 16，以及其中一些对工程上有所帮助的特性了。
那么先通过JDK官网进行JDK 16候选版下载（<a href="http://jdk.java.net/16/%EF%BC%89%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">jdk.java.net/16/）。</a></p>
<p>由于要方便的在系统中针对多个JDK版本进行切换，可以使用jenv（<a href="https://github.com/jenv/jenv%EF%BC%89%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">github.com/jenv/jenv）。</a></p>
<p>我们把下载好的JDK16路径添加到jenv，在做如下设置即可使用。</p>
<p>`jenv add $&#123;JDK16_Path&#125;</p>
<p>jenv global openjdk64-16`</p>
<p>如果一切顺利，那么查看JDK版本时，会有类似如下信息的返回。</p>
<p>`java -version</p>
<p>openjdk version "16"2021-03-16</p>
<p>OpenJDK Runtime Environment (build 16+36-2231)</p>
<p>OpenJDK 64-Bit Server VM (build 16+36-2231, mixed mode, sharing)`</p>
<p>如果你在使用较早的IDEA版本作为开发工具，那么使用JDK 16运行程序时，可能收到如下的错误：
<code>Cannot determine path to 'tools.jar' library for 16 (path/to/jdk-16) when running from IDEA, you should update to the latest version.</code></p>
<p>这是由于JDK9对Java运行时做了重构，已删除了rt.jar、tools.jar、dt.jar以及其它各种内部JAR包。而在较早的开发工具通常对这类JAR包有依赖，通过升级IDEA可以解决。
到官网获取一个IDEA 2021.1 EAP预发版本
（<a href="https://www.jetbrains.com/zh-cn/idea/nextversion/%EF%BC%89%E6%9D%A5%E6%8F%90%E5%89%8D%E4%BD%93%E9%AA%8C%EF%BC%88%E4%B9%9F%E5%8F%AF%E4%BB%A5%E7%AD%89%E5%BE%852021.3%E7%9A%84%E6%AD%A3%E5%BC%8F%E7%89%88%E6%9C%AC%EF%BC%89%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">www.jetbrains.com/zh-cn/idea/…</a></p>
<h1 data-id="heading-4">新特性解读</h1>
<h2 data-id="heading-5">迁移到GitHub</h2>
<p>早在2020年9月，OpenJDK已将Github上的jdk仓库作为JDK 16源码的主读取/写入仓库。随着JDK 16的正式发布，这将是OpenJDK在Github上开发完成的初代JDK版本。</p>
<p>而促使将OpenJDK源代码仓库从Mercurial迁移到Git的三个主要原因：版本控制系统元数据，可用工具和可用托管的大小。</p>
<p>版本控制元数据大小方面，转换后的存储库的初始原型已显示出版本控制元数据的大小显着减少。例如，使用Git的jdk仓库的.git目录大约为300MB，而使用Mercurial的.hg目录大约为1.2GB。减少元数据可保留本地磁盘空间并减少克隆时间，同时减少传输的数据。</p>
<p>可用工具方面，与Mercurial相比，Git可用的工具更多。所有的文本编辑器都可以本地或通过插件实现Git集成。此外，几乎所有的IDE都带有Git集成，包括Eclipse、Visual Studio、IDEA。</p>
<p>可用托管方面，有许多选项可用于托管Git仓库，无论是自托管还是作为服务托管。使用外部源码托管提供程序的原因包括性能、与开发人员进行交互的Web API的访问权限控制 以及 蓬勃发展的社区。</p>
<p>OpenJDK迁移到Github之后，对于Java开发者而言还是有不少的便利：
通过fork一份JDK 16源码仓库（<a href="https://github.com/openjdk/jdk%EF%BC%89%EF%BC%8C%E5%8F%AF%E4%BB%A5%E4%B8%80%E8%BE%B9%E9%98%85%E8%AF%BB%E6%BA%90%E4%BB%A3%E7%A0%81%EF%BC%8C%E4%B8%80%E8%BE%B9%E5%81%9A%E7%AC%94%E8%AE%B0%E5%B9%B6%E6%8F%90%E4%BA%A4%EF%BC%8C%E6%96%B9%E4%BE%BF%E6%8C%81%E7%BB%AD%E5%AD%A6%E4%B9%A0JDK%E6%BA%90%E7%A0%81%E3%80%82%E4%BD%BF%E7%94%A8Git%E7%9A%84upsteam%E4%BF%9D%E6%8C%81JDK%E6%BA%90%E7%A0%81%E7%9A%84%E6%9B%B4%E6%96%B0%EF%BC%8C%E5%90%8C%E6%97%B6%E4%B9%9F%E4%BF%9D%E6%8C%81%E8%87%AA%E6%88%91%E6%9B%B4%E6%96%B0%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">github.com/openjdk/jdk…</a></p>
<p>如网速够快，通过Github在线阅读代码的工具Github1s（<a href="https://github.com/conwnet/github1s%EF%BC%89%EF%BC%8C%E5%BF%AB%E9%80%9F%E5%9C%A8%E6%B5%8F%E8%A7%88%E5%99%A8%E4%B8%AD%E7%BF%BB%E9%98%85JDK" target="_blank" rel="nofollow noopener noreferrer">github.com/conwnet/git…</a> 16源码（<a href="https://github1s.com/openjdk/jdk/releases/tag/jdk-16%2B35%EF%BC%89%E4%B9%9F%E6%98%AF%E9%9D%9E%E5%B8%B8%E6%96%B9%E4%BE%BF%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">github1s.com/openjdk/jdk…</a></p>
<p>如果是在IDEA下工作与学习，clone好JDK 16源码，</p>
<p>打开Project Structure (command+;)，设置Project SDK为JDK 16，并设置Project language level到16。</p>
<p>之后就可以愉快的看JDK 16源码了。</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd1be58f78ca4783b2be9c98261abd1c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">将JDK移植到Alpine Linux</h2>
<p>在云原生时代，个人理解提升效率是第一原则：
更小的镜像体积分发时会更加迅速</p>
<p>应用程序/容器的启动要迅速</p>
<p>这样就能保障系统水平伸缩够快、问题出现时回滚处理够快。</p>
<p>另外，出于降低成本考虑，更小的镜像体积内存占用会更小，分发时耗用的资源也更小。</p>
<p>Alpine Linux就是与云原生的提升效率原则契合的一款独立的非商业性的通用Linux发行版。</p>
<p>其关注于安全性、简单性和资源效率，围绕musl libc和busybox构建。这使得它比传统的GNU/Linux发行版更小。</p>
<p>JDK移植到Alpine Linux后，将允许Tomcat、Jetty、Spring和其它流行的框架在其中工作。用户可以创建一个更小的镜像，以启动、运行特定的应用程序。</p>
<p>提前准备好Docker，我们先构建一个Alpine Linux镜像，然后添加JDK 16，最后运行一个简单的Spring Boot程序来演示一下。</p>
<h2 data-id="heading-7">构建Alpine Linux镜像</h2>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d7ff9cf72e541e89e587ee3cf9b4a7b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>通过docker images命令查看镜像大小会发现，alpine在截止本文完成时，镜像大小仅仅只有5.6MB。相对于debian、ubuntu、centos等系统动则几十甚至上百MB的镜像来说，alpine可是真的小！</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d08fd7adc4e14189ababcf6715cabc25~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">添加JDK 16</h2>
<p>OpenJDK通过使用jlink（JEP 282：<a href="https://openjdk.java.net/jeps/282%EF%BC%89%E6%9D%A5%E5%87%8F%E5%B0%91Java%E8%BF%90%E8%A1%8C%E6%97%B6%E7%9A%84%E5%A4%A7%E5%B0%8F%EF%BC%8C%E6%88%91%E4%BB%AC%E5%8F%AF%E4%BB%A5%E4%BB%8EDockerHub%E4%B8%8A%E8%8E%B7%E5%8F%96%E9%95%9C%E5%83%8F%EF%BC%9A" target="_blank" rel="nofollow noopener noreferrer">openjdk.java.net/jeps/282）来减…</a>
16-jdk-alpine（<a href="https://hub.docker.com/_/openjdk?tab=tags&page=1&name=16-jdk-alpine&ordering=last_updated%EF%BC%89%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">hub.docker.com/_/openjdk?t…</a>
或者如下Docker命令：
docker pull openjdk:16-jdk-alpine</p>
<h2 data-id="heading-9">运行Spring Boot</h2>
<p>先准备一个Spring Boot的FatJar程序，可以从Spring Boot官网获取Hello World！样例程序（<a href="https://spring.io/guides/gs/rest-service/%EF%BC%89%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">spring.io/guides/gs/r…</a>
创建一份Dockerfile，使用openjdk:16-jdk-alpine，并添加Spring Boot程序。</p>
<p>`FROM openjdk:16-jdk-alpine</p>
<p>VOLUME /tmp</p>
<p>ARG JAR_FILE</p>
<p>ADD $&#123;JAR_FILE&#125; app.jar</p>
<p>ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]`</p>
<h2 data-id="heading-10">构建并运行</h2>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1be8b6057d6b419d89a3453fe1edc3cd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a20fd7c0f6154e1e9c71e24c548ce194~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>至此，通过Alpine Linux系统带JDK 16运行时的Spring Boot已经启动并可以正常的访问了。</p>
<p>Alpine系统JDK 16镜像大小约为321MB。相比Oracle官方的Linux版本镜像的467MB，减少30%+。</p>
<h1 data-id="heading-11">记录类</h1>
<p>从JDK 14开始提供了Record记录类的预览特性，这一特性将成为JDK 16的一项永久性特性。Record记录类作为不可变数据的透明载体，其是为了回应有关Java过于冗长拘谨的抱怨。此计划的目标包括设计一个表示简单值集合的面向对象的构造函数，帮助开发人员专注于对不可变数据的建模而不是扩展行为，自动实现数据驱动的方法（例如 equals() 和 属性的访问器）。</p>
<p>通过较新版IDEA可以创建此类型：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/330ee5aacc8f403ab4145b9c0f5d101e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>声明Record记录类后，几乎不需要添加额外的代码，一组隐式声明让其代码书写很简洁：</p>
<p>隐式声明了属性</p>
<p>隐式声明了构造器</p>
<p>隐式声明了equals()、hashCode()、toString()</p>
<p>隐式声明了属性的访问器，访问器名称与属性同名</p>
<p><code>public record Point(int x, int y) &#123;&#125;</code></p>
<p>Record记录类支持Local Classes特性，那么当需要临时使用Record的时候，就可以非常方便的定义与使用：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7def1ac21919412bb6411fdaa868fdfe~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Record记录类将可以代替Tuple、Pair等之前在JDK之外的工具库提供的元组功能，在与下面将介绍的模式匹配特性配合，可使代码将变得非常简洁。</p>
<h2 data-id="heading-12">模式匹配</h2>
<p>从JDK 14开始引入了一种模式匹配的预览特性，这一特性也将成为JDK 16的一项永久性特性。因此虽然JDK 16是个短期版本，也不妨碍我们在未来的JDK版本中继续使用模式匹配特性。</p>
<p>模式匹配的现阶段仅限于一种模式（类型模式）和一种语言构造（instanceof），但这只是完整特性的一部分。即便如此，我们也已经获得了一个显著的好处：冗余的强制转换消失了，消除了冗余的代码，使更重要的代码得到了更清晰的关注，同时消除了隐藏bug的地方。</p>
<p>举个例子：
我们在开发中当需要解析对象会用到类似如下的方式</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87af605f3ee140108036bdd3c1ddced4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>使用模式匹配后的等价代码：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e60a37a7425f475db3f965fe6b6ddda2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>代码看起来是不是整洁了许多。</p>
<p>使用instanceof获取对象类型是一种条件提取形式，在获得到对象类型之后，总是要将对象强制转换为该类型。</p>
<p>以前在instanceof之后必须进行显式类型转换，这是一种繁琐的操作，而融合这些操作的好处不仅仅是为了简洁，它还消除了一个常见的错误来源：在剪切和粘贴instanceof及强制转换代码，容易在修改了 instanceof的类型之后忘记修改强制转换类型，这就给了漏洞一个藏身之处。通过instanceof的模式匹配消除了这个问题，我们还可以消灭所有这种类型的bug。</p>
<p>另一个需要经常的做此类“先检测后强制转换”的地方是equals方法。
再来看一个例子：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d958805faaa349c2a9d4b50faa5a7ccf~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>使用模式匹配后的等价代码：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45383d108e154a5aa34432451bbd55d7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这段代码起到同样的效果，但更简单直接，因为我们可以只使用一个复合布尔表达式来表达一个等价的条件，而不是使用控制流语句。</p>
<p>模式匹配的绑定变量（如上代码例子中 obj instanceof String s的s就是一个绑定变量）除了特殊的声明位置以外，其作用域也与"普通"局部变量有所不同。</p>
<p>比如我们可以这样写：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01f329617943414f9c46e5efb73623fc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这样特殊的作用域让我们能够在if-else的多分支情况下，自由的重新声明绑定变量，也考虑未来在switch中的case也是如此便利。如：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b151043dbc8422ba929487045717199~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果模式匹配可以消除Java代码中99%的强制类型转换操作，那么它肯定会很流行。但还不仅限于此，随着时间的推移，将会出现其他类型的模式，它们可以进行更复杂的条件提取，使用更复杂的方式来组合模式，以及提供其他可以使用模式的构造：比如switch，甚至是catch，再加上目前已永久支持的Record类以及在预览中的密封类等相关特性，模式匹配未来一定能够大大简化我们编写的代码。</p>
<h1 data-id="heading-13">尾声</h1>
<p>本文从JDK 16版本所带来的17个新特性中抽取对工程工作和学习比较有帮助的几个特性展开解读，快速了解了这些特性。</p>
<p>大部分的企业或者项目还在使用JDK 8（其依然占据JDK市场的80%，绝对的主流），源于JDK 8的超豪华新特性，如函数式接口、Lambda表达式、方法引用 / 构造器引用、更强的Steam API、接口的增强、Optional、JVM中Metaspace取代PermGen空间等等。</p>
<p>我们也能够看到Java为了跟上当下技术更迭的快节奏，不断的推陈出新。</p>
<p>从JDK 9开始，Java版本的发布改为每6个月一次，JDK 11是长期支持版本以及下半年将发布的JDK 17。</p>
<p>JDK 9~JDK15也不乏一些重要的新特性，如</p>
<ul>
<li>JDK 9 模块系统、JShell交互式命令行</li>
<li>JDK 10 局部变量类型推断</li>
<li>JDK 11 ZGC试用、HTTP Client API、Steam等增强</li>
<li>JDK 12 switch表达式扩展、增加基于JMH的一套微基准套件</li>
<li>JDK 13 Socket API 重构、文本块（多行文本）</li>
<li>JDK 14 更有价值的NPE错误信息、JDK 16特性的部分预览</li>
<li>JDK 15 密封类、Record类等JDK 16特性的预览</li>
</ul>
<p>希望这种快速版本迭代的策略能够让Java保持持续的活力，能够让开发者使用的更高效、更健壮！</p>
<h1 data-id="heading-14">参考资料</h1>
<p>JDK 16 的状态、发布计划与新特性</p>
<p>（<a href="http://openjdk.java.net/projects/jdk/16/%EF%BC%89" target="_blank" rel="nofollow noopener noreferrer">openjdk.java.net/projects/jd…</a></p>
<p>JDK 16: The new features in Java 16</p>
<p>（<a href="https://www.infoworld.com/article/3569150/jdk-16-the-new-features-in-java-16.html%EF%BC%89" target="_blank" rel="nofollow noopener noreferrer">www.infoworld.com/article/356…</a></p>
<p>Java源代码仓库迁移到Github</p>
<p>（<a href="https://www.infoworld.com/article/3569068/javas-move-to-github-set-for-september.html%EF%BC%89" target="_blank" rel="nofollow noopener noreferrer">www.infoworld.com/article/356…</a></p>
<p>在Alpine + OpenJDK镜像中运行Spring Boot</p>
<p>（<a href="https://blogs.oracle.com/developers/running-spring-boot-in-a-docker-container-on-openjdk,-oracle-jdk,-zulu-on-alpine-linux,-oracle-linux,-ubuntu%EF%BC%89" target="_blank" rel="nofollow noopener noreferrer">blogs.oracle.com/developers/…</a></p>
<p>JEP 394: Pattern Matching for instanceof</p>
<p>（<a href="https://openjdk.java.net/jeps/394%EF%BC%89" target="_blank" rel="nofollow noopener noreferrer">openjdk.java.net/jeps/394）</a></p>
<p>JEP 395: Records</p>
<p>（<a href="https://openjdk.java.net/jeps/395%EF%BC%89" target="_blank" rel="nofollow noopener noreferrer">openjdk.java.net/jeps/395）</a></p>
<p>JEP 397: Sealed Classes (Second Preview)</p>
<p>（<a href="https://openjdk.java.net/jeps/397%EF%BC%89" target="_blank" rel="nofollow noopener noreferrer">openjdk.java.net/jeps/397）</a></p>
<h2 data-id="heading-15">加入我们</h2>
<p>欢迎加入淘系架构团队，团队成员大牛云集，有阿里移动中间件的创始人员、Dubbo核心成员、更有一群热爱技术，期望用技术推动业务的小伙伴。</p>
<p>淘系架构团队，推进淘系（淘宝、天猫等）架构升级，致力于为淘系、整个集团提供基础核心能力、产品与解决方案：</p>
<p>业务高可用的解决方案与核心能力（精细化流量管控Marconi平台：为业务提供自适应流控、隔离与熔断的柔性高可用解决方案，站点高可用：故障自愈、多机房与异地容灾与快速切流恢复</p>
<p>新一代的业务研发模式FaaS（一站式函数研发Gaia平台）</p>
<p>下一代网络协议QUIC实现与落地</p>
<p>移动中间件（API网关MTop、接入层AServer、消息/推送、配置中心等等）</p>
<p>期待一起参与加入淘系基础平台的建设~</p>
<p>简历投递至📮：泽彬 <a href="mailto:zebin.xuzb@alibaba-inc.com">zebin.xuzb@alibaba-inc.com</a>
（淘系架构-应用架构Leader）</p>
<ul>
<li>作者：熊政(八风)</li>
<li>来源：淘系技术公众号</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            