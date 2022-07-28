
---
title: 'GraalVM 社区版 22.2 发布：优化内存使用、减少 JDK 体积'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-09902b2bf3a2b7eba7b1b1b89d2988bb5cd.png'
author: 开源中国
comments: false
date: Thu, 28 Jul 2022 07:05:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-09902b2bf3a2b7eba7b1b1b89d2988bb5cd.png'
---

<div>   
<div class="content">
                                                                                            <p>GraalVM 社区版 22.2 已发布。</p> 
<blockquote> 
 <p>GraalVM 是一个高性能的 JDK 发行版。它旨在加速用 Java 和其他 JVM 语言编写的应用程序的执行，同时还为 JavaScript、Python、基于 LLVM 的语言（如 C 和 C++）以及许多其他流行编程语言提供运行时。此外，GraalVM 为编程语言之间提供了高效互操作性，并将 Java 应用程序提前编译为本机可执行文件，从而加快启动时间并降低内存开销。</p> 
</blockquote> 
<p><img src="https://oscimg.oschina.net/oscnet/up-09902b2bf3a2b7eba7b1b1b89d2988bb5cd.png" referrerpolicy="no-referrer"></p> 
<p><strong>主要变化</strong></p> 
<p><strong>减少 JDK 发行版体积</strong></p> 
<p>从 22.2 开始，<strong style="color:#292929">GraalVM JDK 更加模块化，并且不再包含 JavaScript runtime、LLVM runtime 和 VisualVM</strong>。开发者如需安装这些组件，请使用<code>gu install js</code>、<code>gu install llvm</code>和<code>gu install visualvm</code>命令进行安装。此举显著减少了 JDK 发行版体积。如果你使用 GraalVM 在 JVM 上运行 Java 应用程序或使用 Native Image，则设置 GraalVM 和运行应用程序的方式没有变化，除了 JDK 的下载体积显着减少。</p> 
<p>下面是 JDK 17 在 22.1 与 22.2 的对比：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-c137940cd501365bfd528bf30aaf4d05b02.png" referrerpolicy="no-referrer"></p> 
<p><strong>优化构建 Native Image 的内存占用率</strong></p> 
<p>由于内部数据结构的改进，目前 Native Image 在构建本地可执行文件时需要的内存明显减少。内存占用率降低在内存受限的环境中特别有利，比如云服务和 GitHub Action。从 22.2 开始，Native Image 工具支持成功构建许多较大的原生可执行文件，只需使用 2GB 的 Java heap 内存。</p> 
<p>例如，Spring PetClinic 应用程序现在只需使用 2GB 的内存即可构建。</p> 
<pre><code class="language-bash">========================================================================================================================
GraalVM Native Image: Generating 'petclinic-jpa' (executable)...
========================================================================================================================
[1/7] Initializing...                                                                                   (12.2s @ 0.47GB)
 Version info: 'GraalVM 22.2.0 Java 17 EE'
 Java version info: '17.0.4+11-LTS-jvmci-22.2-b05'
 C compiler: gcc (linux, x86_64, 9.4.0)
 Garbage collector: Serial GC
[2/7] Performing analysis...  [*********]                                                               (67.5s @ 1.92GB)
  26,184 (94.56%) of 27,689 classes reachable
  42,026 (68.44%) of 61,409 fields reachable
 140,935 (67.78%) of 207,928 methods reachable
   1,397 classes,   415 fields, and 7,894 methods registered for reflection
      65 classes,    74 fields, and    55 methods registered for JNI access
       4 native libraries: dl, pthread, rt, z
[3/7] Building universe...                                                                              (56.5s @ 1.95GB)
[4/7] Parsing methods...      [***]                                                                      (5.9s @ 1.48GB)
[5/7] Inlining methods...     [****]                                                                     (2.4s @ 1.55GB)
[6/7] Compiling methods...    [****]                                                                    (19.4s @ 1.74GB)
[7/7] Creating image...                                                                                  (8.4s @ 1.68GB)
  43.28MB (45.39%) for code area:    97,635 compilation units
  47.41MB (49.73%) for image heap:  579,002 objects and 835 resources
   4.65MB ( 4.87%) for other data
  95.34MB in total
------------------------------------------------------------------------------------------------------------------------
Top 10 packages in code area:                               Top 10 object types in image heap:
   3.21MB com.oracle.svm.core.code                             9.99MB byte[] for code metadata
   1.20MB jdk.proxy4                                           9.00MB byte[] for embedded resources
   1.06MB sun.security.ssl                                     5.83MB byte[] for java.lang.String
 878.77KB java.util                                            4.73MB java.lang.Class
 814.08KB com.mysql.cj.jdbc                                    4.22MB java.lang.String
 555.53KB org.hibernate.hql.internal.antlr                     3.53MB byte[] for general heap data
 488.76KB org.apache.coyote.http2                              1.65MB byte[] for reflection metadata
 476.47KB org.apache.catalina.core                             1.20MB com.oracle.svm.core.hub.DynamicHubCompanion
 465.88KB java.lang.invoke                                   725.72KB c.o.svm.core.hub.DynamicHub$ReflectionMetadata
 460.78KB com.sun.crypto.provider                            599.67KB java.lang.String[]
  33.08MB for 1101 more packages                               5.06MB for 4765 more object types
------------------------------------------------------------------------------------------------------------------------
                       77.2s (42.7% of total time) in 306 GCs | Peak RSS: 3.42GB | CPU load: 9.52
------------------------------------------------------------------------------------------------------------------------
Produced artifacts:
 /home/janedoe/demos/spring-native/samples/petclinic-jpa/target/petclinic-jpa (executable)
 /home/janedoe/demos/spring-native/samples/petclinic-jpa/target/petclinic-jpa.build_artifacts.txt (txt)
========================================================================================================================
Finished generating 'petclinic-jpa' in 3m 0s.</code></pre> 
<p><strong>改进 GraalJS 中的互操作性</strong></p> 
<p>从 22.2 开始，默认情况下为其他语言的对象分配适当的 JavaScript 原型。该功能处于实验性阶段，通过让外部对象作为 JavaScript 中的数组、函数和其他类型出现，增加了代码的可移植性。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgraalvm%2Fgraalvm-ce-builds%2Freleases%2Ftag%2Fvm-22.2.0" target="_blank">下载地址</a><span style="background-color:#ffffff; color:#333333"><span> </span>|<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fgraalvm%2Fgraalvm-22-2-smaller-jdk-size-improved-memory-usage-better-library-support-and-more-cb34b5b68ec0" target="_blank">发布公告</a></p>
                                        </div>
                                      
</div>
            