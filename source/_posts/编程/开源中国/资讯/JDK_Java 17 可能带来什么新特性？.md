
---
title: 'JDK_Java 17 可能带来什么新特性？'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ebc589e48093918e78ea300ce6d55ea4bd7.png'
author: 开源中国
comments: false
date: Tue, 31 Aug 2021 05:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ebc589e48093918e78ea300ce6d55ea4bd7.png'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/news/133354/jdk-16-ga">JDK/Java 16</a> 已于今年 3 月份正式 GA，这是一个短期维护版本，仅有 6 个月的技术支持。下一个版本 JDK/Java 17 计划于今年 9 月 14 日发布，这是一个长期支持（LTS）版本，预计 Oracle 将提供数年的扩展支持。</p> 
<p>JDK 17 现在已经进入了第二个也是最后一个候选版本阶段（RC），目前最新版本是 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjdk.java.net%2F17%2F" target="_blank">Build 35</a>。</p> 
<p><img height="300" src="https://oscimg.oschina.net/oscnet/up-ebc589e48093918e78ea300ce6d55ea4bd7.png" width="390" referrerpolicy="no-referrer"></p> 
<p>按 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.infoworld.com%2Farticle%2F3606833%2Fjdk-17-the-new-features-in-java-17.html" target="_blank">InfoWorld </a>所述，OpenJDK JDK 17 的部分功能包括有：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F415" target="_blank">Context-specific 反序列化过滤器</a>允许应用程序通过调用 JVM-wide filter factory 为每个序列化操作选择过滤器，来配置 context-specific  和 dynamically selected 的反序列化过滤器。</li> 
 <li>随着 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F306" target="_blank">always-strict 浮点语义的</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F306" target="_blank">恢复</a>，浮点运算将保持一致的严格；而不是同时具有严格的浮点语义 ( <code>strictfp</code>) 和有着微妙出入的默认浮点语义。这就为语言和 VM 恢复了原始的浮点语义，与 Java Standard Edition 1.2 中引入严格和默认浮点模式之前的语义相匹配。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F411" target="_blank">弃用 Security Manager</a>，准备在未来版本中移除。追溯到 Java 1.0，Security Manager 一直是保护客户端 Java 代码的主要手段，很少用于保护服务器端代码。该提案的一个目标是评估是否需要新的 API 或机制来解决使用 Security Manager 的特定狭窄用例，例如阻塞<code>System::exit</code>。计划要求弃用 Security Manager 以与旧 Applet API 一起删除，该 API 也计划在 JDK 17 中弃用。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F406" target="_blank"><code>switch</code>模式匹配</a>预览版扩展了 Java 中的模式语言，允许<code>switch</code>表达式和语句可以针对多个模式进行测试，每个模式都有特定的操作。这使得复杂的面向数据的查询能够简洁而安全地表达。此功能的目标包括：通过使模式出现在案例标签中，来扩展<code>switch</code>表达式和语句的表现力和应用，在需要时放宽<code>switch</code>的 historical null-hostility，并引入两种模式：<code>guarded patterns</code>，允许用任意的布尔表达式来完善模式匹配逻辑，以及<code>parenthesized patterns</code>，解决了一些解析歧义。在 JDK 16 中，<code>instanceof</code>运算符被扩展为采用类型模式并执行模式匹配。提议的适度扩展允许简化熟悉的 instanceof-and-cast 习语。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F403" target="_blank">JDK 内部的强封装</a>，除了<code>sun.misc.Unsafe</code>等关键的内部 API 外，用户将不再可能通过单个命令行选项来 relax 对内部元素的强封装，这在 JDK 9 到 JDK 16 中是可行的。该计划的目标包括提高 JDK 的安全性和可维护性，并鼓励开发人员从内部元素迁移到标准 API。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F407" target="_blank">删除远程方法调用 (RMI) 激活机制，</a>同时保留 RMI 的其余部分。RMI 激活机制已过时和废弃，在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.infoworld.com%2Farticle%2F3534133%2Fjdk-15-the-new-features-in-java-15.html" target="_blank">JDK 15 中</a>不推荐使用。</li> 
 <li>在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftranslate.baiducontent.com%2Ftranspage%3Fcb%3DtranslateCallback%26ie%3Dutf8%26source%3Durl%26query%3Dhttps%253A%252F%252Fopenjdk.java.net%252Fjeps%252F412%26from%3Den%26to%3Dzh%26token%3D%26monLang%3Dzh" target="_blank">外部函数和 memory API </a>引入了一个孵化器阶段，允许 Java 程序与 Java 运行时之外的代码和数据进行互操作。API 计划的目标包括易用性、性能、通用性和安全性。</li> 
 <li>与平台无关的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F414" target="_blank">矢量 API</a> 作为孵化 API 集成到 JDK 16 中，将在 JDK 17 中再次孵化，提供一种机制来表达矢量计算，这些计算在运行时可靠地编译为支持的 CPU 架构上的最佳矢量指令。这比等效的标量计算获得了更好的性能。在 JDK 17 中，向量 API 已针对性能和实现进行了增强，包括在字节向量与布尔数组之间进行转换的增强功能。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F409" target="_blank">密封类和接口</a>限制哪些其他类或接口可以扩展或实现它们。该提案的目标包括允许类或接口的作者控制哪些代码负责实现它，提供比访问修饰符更具声明性的方式来限制超类的使用，并通过为模式的详尽分析提供基础来支持模式匹配的未来方向。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F410" target="_blank">删除实验性 AOT 和 JIT 编译器</a>，它们几乎没有使用，但需要大量维护工作。该计划要求维护 Java 级别的 JVM 编译器接口，以便开发人员可以继续使用外部构建的编译器版本进行 JIT 编译。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F391" target="_blank">将 JDK 移植到 MacOS/AArch64</a> 以响应 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.macworld.com%2Farticle%2F3563738%2Fyou-shouldnt-buy-a-new-mac-right-now.html" target="_blank">Apple 将其 Macintosh 计算机从 x64 转换到 AArch64 的计划</a>。针对 MacOS/AArch64 的更改有可能破坏现有的 Linux/AArch64、Windows/AArch64 和 MacOS/x64 port，但这种风险可通过预集成测试来降低。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F398" target="_blank">弃用 Applet API 以进行删除</a>。这个 API 本质上是无关紧要的，因为所有 Web 浏览器供应商要么已经取消了对 Java 浏览器插件的支持，要么已经宣布了这样做的计划。Applet API 之前在 2017 年 9 月的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.infoworld.com%2Farticle%2F3227244%2Fjava-9-is-here-everything-you-need-to-know.html" target="_blank">Java 9</a> 中已被弃用，但并未删除。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F382" target="_blank">用于 MacOS 的新渲染管道</a>，使用 Apple Metal API 作为使用已弃用 OpenGL API 的现有管道的替代方案。该提议旨在为使用 MacOS Metal 框架的 Java 2D API 提供一条功能齐全的渲染管道，为苹果从未来版本的 MacOS 中删除 OpenGL API 做好准备。该管道旨在功能上与现有的 OpenGL 管道相当，在某些应用程序和基准测试中具有相同或更好的性能。将创建适合当前 Java 2D 模型的干净架构。管道将与 OpenGL 管道共存，直到被淘汰。本提案的目的并不是添加任何新的 Java 或 JDK API。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F356" target="_blank">增强的伪随机数生成器</a>将为伪随机数生成器（PRNG）提供新的接口类型和实现，包括可跳转的 PRNG 和额外的一类可拆分 PRNG 算法 (LXM)。新接口<code>RandomGenerator</code>将为所有现有的和新的 PRNG 提供统一的 API；将提供四个专门的 RandomGenerator 接口。该计划的动机是关注 Java 中伪随机数生成领域的多个改进领域。这项工作不需要提供许多其他 PRNG 算法的实现。但是已经添加了三种常用算法，这些算法已经广泛部署在其他编程语言环境中。该计划的目标包括： 
  <ul> 
   <li>使在应用程序中交替使用各种 PRNG 算法变得更容易。</li> 
   <li>改进了对基于流的编程的支持，提供了 PRNG 对象流。</li> 
   <li>消除现有 PRNG 类中的代码重复。</li> 
   <li>保留类<code>java.util.Random</code>的现有行为。</li> 
  </ul> </li> 
</ul> 
<p>JDK 17 等 LTS 版本每三年发布一次，上一个LTS 版本 <a href="https://www.oschina.net/news/100305/java-11-released-sep-25">JDK 11</a> 于 2018 年 9 月发布。</p> 
<p>详情可查看： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjdk.java.net%2F17%2F" target="_blank">https://jdk.java.net/17/</a> </p>
                                        </div>
                                      
</div>
            