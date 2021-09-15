
---
title: 'JDK_Java 17 GA，新增「Free Java License」'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0915/062213_auj2_2720166.png'
author: 开源中国
comments: false
date: Wed, 15 Sep 2021 07:05:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0915/062213_auj2_2720166.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fprojects%2Fjdk%2F17%2F" target="_blank">JDK/Java 17 已正式 GA</a>。</p> 
 <p><img src="https://static.oschina.net/uploads/space/2021/0915/062213_auj2_2720166.png" referrerpolicy="no-referrer"></p> 
 <div> 
  <div> 
   <p>按照发布规划，JDK/Java 17 属于长期支持版本 (LTS)，将会获得 8 年的技术支持，直至 2029 年 9 年。</p> 
   <p><img alt src="https://oscimg.oschina.net/oscnet/up-8c99b5fc4a92ced93b9538f78e22fdee295.png" referrerpolicy="no-referrer"></p> 
   <p>JDK/Java 17 总共包含 14 个 JEP，具体如下：</p> 
  </div> 
 </div> 
 <div> 
  <div> 
   <table summary="jeps"> 
    <tbody> 
     <tr> 
      <td>306:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F306" target="_blank">Restore Always-Strict Floating-Point Semantics</a></td> 
     </tr> 
     <tr> 
      <td>356:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F356" target="_blank">Enhanced Pseudo-Random Number Generators</a></td> 
     </tr> 
     <tr> 
      <td>382:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F382" target="_blank">New macOS Rendering Pipeline</a></td> 
     </tr> 
     <tr> 
      <td>391:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F391" target="_blank">macOS/AArch64 Port</a></td> 
     </tr> 
     <tr> 
      <td>398:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F398" target="_blank">Deprecate the Applet API for Removal</a></td> 
     </tr> 
     <tr> 
      <td>403:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F403" target="_blank">Strongly Encapsulate JDK Internals</a></td> 
     </tr> 
     <tr> 
      <td>406:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F406" target="_blank">Pattern Matching for switch (Preview)</a></td> 
     </tr> 
     <tr> 
      <td>407:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F407" target="_blank">Remove RMI Activation</a></td> 
     </tr> 
     <tr> 
      <td>409:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F409" target="_blank">Sealed Classes</a></td> 
     </tr> 
     <tr> 
      <td>410:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F410" target="_blank">Remove the Experimental AOT and JIT Compiler</a></td> 
     </tr> 
     <tr> 
      <td>411:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F411" target="_blank">Deprecate the Security Manager for Removal</a></td> 
     </tr> 
     <tr> 
      <td>412:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F412" target="_blank">Foreign Function & Memory API (Incubator)</a></td> 
     </tr> 
     <tr> 
      <td>414:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F414" target="_blank">Vector API (Second Incubator)</a></td> 
     </tr> 
     <tr> 
      <td>415:</td> 
      <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F415" target="_blank">Context-Specific Deserialization Filters</a></td> 
     </tr> 
    </tbody> 
   </table> 
   <div> 
    <div> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F306" target="_blank">Restore Always-Strict Floating-Point Semantics</a></strong></h3> 
     <p>恢复始终执行严格模式 (Always-Strict) 的浮点定义</p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F356" target="_blank">Enhanced Pseudo-Random Number Generators</a></strong></h3> 
     <p>添加增强的伪随机数生成器</p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F382" target="_blank">New macOS Rendering Pipeline</a></strong></h3> 
     <p>为 macOS 引入新渲染管道</p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F391" target="_blank">macOS/AArch64 Port</a></strong></h3> 
     <p>支持将 JDK 移植到 macOS/AArch64 架构</p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F398" target="_blank">Deprecate the Applet API for Removal</a></strong></h3> 
     <p>弃用待移除的 Applet API</p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F403" target="_blank">Strongly Encapsulate JDK Internals</a></strong></h3> 
     <p>强封装的 JDK 内部 API，<span style="background-color:#ffffff; color:#333333">默认对 JDK 内部进行强封装</span></p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F406" target="_blank">Pattern Matching for switch (Preview)</a></strong></h3> 
     <p>switch 模式匹配进入预览 (Preview) 阶段</p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F407" target="_blank">Remove RMI Activation</a></strong></h3> 
     <p>移除 RMI（远程方法调用）激活机制</p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F409" target="_blank">Sealed Classes</a></strong></h3> 
     <p>密封类和接口正式可用，用于<span style="background-color:#ffffff; color:#333333">限制哪些类和接口可以继承或实现它们。</span></p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F410" target="_blank">Remove the Experimental AOT and JIT Compiler</a></strong></h3> 
     <p>移除实验性的 AOT 和 JIT 编译器</p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F411" target="_blank">Deprecate the Security Manager for Removal</a></strong></h3> 
     <p>弃用待移除的安全管理器 (Security Manager)</p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F412" target="_blank">Foreign Function & Memory API (Incubator)</a></strong></h3> 
     <p>外部函数和内存 API 进入孵化阶段，Java 应用程序通过该 API 能够与 Java 运行时之外的代码和数据进行互操作。</p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F414" target="_blank">Vector API (Second Incubator)</a></strong></h3> 
     <p>在 JDK/Java 17 中，<span style="background-color:#ffffff; color:#333333">Vector API 已进入孵化的第二阶段，Vector API 用于表达可在支持的 CPU 架构上编译为最佳矢量硬件指令的矢量计算，以实现优于等效标量计算的性能。</span></p> 
     <h3><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F415" target="_blank">Context-Specific Deserialization Filters</a></strong></h3> 
     <p>增加面向特定上下文的反序列化过滤器，此特性允许应用程序通过 JVM 的过滤器工厂配置特定于上下文和动态选择的反序列化过滤器。</p> 
     <p><a href="https://www.oschina.net/news/158012/jdk-17-new-features" target="_blank">详细介绍点此查看</a>。</p> 
     <p>值得一提的是，根据 Oracle 最新推出的<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.oracle.com%2Fjava%2Fpost%2Ffree-java-license" target="_blank">「Free Java License」</a></strong>，Oracle JDK 可免费用于生产环境。</p> 
     <p>Free Java License 摘要</p> 
     <div> 
      <ul> 
       <li>为 Oracle JDK <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.oracle.com%2Fjavadownload" target="_blank">免费提供</a>所有季度的安全更新，包括商业和生产用途。</li> 
       <li>新的许可证属于<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.oracle.com%2Fdownloads%2Flicenses%2Fno-fee-license.html" target="_blank">“Oracle 免费条款和条件”(NFTC) 许可证</a>。此许可证允许所有用户免费使用，甚至可以用于商业和生产用途。再分发同样不收取费用。</li> 
       <li>开发者和组织现可轻松<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.oracle.com%2Fjava%2Ftechnologies%2Fjdk-script-friendly-urls%2F" target="_blank">下载、使用、共享和重新分发 Oracle JDK</a>。</li> 
       <li>Oracle 将从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.oracle.com%2Fjavadownload" target="_blank">Oracle JDK 17</a> 开始提供这些免费版本和更新，并<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.oracle.com%2Fjava%2Fpost%2Fmoving-the-jdk-to-a-two-year-lts-cadence" target="_blank">在下一个 LTS 版本</a>发布之后继续提供整整一年。注意以前的版本不受此更改的影响。</li> 
       <li>Oracle 将继续按照自 Java 9 以来的相同版本和时间表提供 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Flegal%2Fgplv2%2Bce.html" target="_blank">GPL</a> 下的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjdk.java.net%2F" target="_blank">Oracle OpenJDK 版本</a>。</li> 
      </ul> 
      <p>此外，Oracle 还提议将 JDK LTS 的发布周期从每三年一次改为每两年一次。如果该提案被接受，这意味着 JDK 17 之后的下一个 JDK LTS 版本将是 JDK 21，而不是 JDK 23。</p> 
     </div> 
     <div>
      发布公告：
      <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmail.openjdk.java.net%2Fpipermail%2Fjdk-dev%2F2021-September%2F006037.html" target="_blank">https://mail.openjdk.java.net/</a>
      <br> 下载：
      <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjdk.java.net%2F17%2F" target="_blank">https://jdk.java.net/17/</a>
      <br> Release notes：
      <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjdk.java.net%2F17%2Frelease-notes" target="_blank">https://jdk.java.net/17/release-notes</a>
      <br> 文档：
      <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fjava%2Fjavase%2F17%2Findex.html" target="_blank">https://docs.oracle.com/en/java/javase/17/index.html</a>
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            