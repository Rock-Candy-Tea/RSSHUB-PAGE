
---
title: 'JDK 19 _ Java 19 正式 GA'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0921/073914_2JvW_2720166.png'
author: 开源中国
comments: false
date: Wed, 21 Sep 2022 07:47:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0921/073914_2JvW_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>JDK 19 / Java 19 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjdk.java.net%2F19%2F" target="_blank">已正式发布</a>。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0921/073914_2JvW_2720166.png" referrerpolicy="no-referrer"></p> 
<p>新版本总共包含 7 个新的 JEP：</p> 
<table cellspacing="0" class="jeps" style="-webkit-text-stroke-width:0px; border-collapse:collapse; color:#000000; font-family:"DejaVu Sans","Bitstream Vera Sans","Luxi Sans",Verdana,Arial,Helvetica; font-size:13.3333px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; orphans:2; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; word-spacing:0px" summary="jeps"> 
 <tbody> 
  <tr> 
   <td style="text-align:left; vertical-align:top; width:0px">405:</td> 
   <td style="text-align:left; vertical-align:top"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.org%2Fjeps%2F405" target="_blank">Record Patterns (Preview)</a></td> 
  </tr> 
  <tr> 
   <td style="text-align:left; vertical-align:top; width:0px">422:</td> 
   <td style="text-align:left; vertical-align:top"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.org%2Fjeps%2F422" target="_blank">Linux/RISC-V Port</a></td> 
  </tr> 
  <tr> 
   <td style="text-align:left; vertical-align:top; width:0px">424:</td> 
   <td style="text-align:left; vertical-align:top"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.org%2Fjeps%2F424" target="_blank">Foreign Function & Memory API (Preview)</a></td> 
  </tr> 
  <tr> 
   <td style="text-align:left; vertical-align:top; width:0px">425:</td> 
   <td style="text-align:left; vertical-align:top"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.org%2Fjeps%2F425" target="_blank">Virtual Threads (Preview)</a></td> 
  </tr> 
  <tr> 
   <td style="text-align:left; vertical-align:top; width:0px">426:</td> 
   <td style="text-align:left; vertical-align:top"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.org%2Fjeps%2F426" target="_blank">Vector API (Fourth Incubator)</a></td> 
  </tr> 
  <tr> 
   <td style="text-align:left; vertical-align:top; width:0px">427:</td> 
   <td style="text-align:left; vertical-align:top"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.org%2Fjeps%2F427" target="_blank">Pattern Matching for switch (Third Preview)</a></td> 
  </tr> 
  <tr> 
   <td style="text-align:left; vertical-align:top; width:0px">428:</td> 
   <td style="text-align:left; vertical-align:top"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.org%2Fjeps%2F428" target="_blank">Structured Concurrency (Incubator)</a></td> 
  </tr> 
 </tbody> 
</table> 
<ul> 
 <li><strong>405：记录模式 (Record Patterns) 进入预览阶段</strong></li> 
</ul> 
<p>Record Patterns 可对 record 的值进行解构，Record patterns 和 Type patterns 通过嵌套能够实现强大的、声明性的、可组合的数据导航和处理形式。</p> 
<p>该特性目前处于预览阶段。</p> 
<ul> 
 <li><strong>422：将 JDK 移植到 Linux/RISC-V 平台</strong></li> 
</ul> 
<p>目前只支持 RISC-V 的 RV64GV 配置，它是一个通用的 64 位 ISA。将来会考虑支持其他的 RISC-V 配置，例如通用的 32 位配置 (RV32G)。</p> 
<ul> 
 <li>424：<strong>外部函数和内存 API (Foreign Function & Memory API) 进入预览阶段</strong></li> 
</ul> 
<p>Java 程序可以通过该 API 与 Java 运行时之外的代码和数据进行互操作。通过高效地调用外部函数（即 JVM 之外的代码）和安全地访问外部内存（即不受 JVM 管理的内存），该 API 使 Java 程序能够调用本机库并处理本机数据，而不会像 JNI 那样危险和脆弱。</p> 
<p>一句话总结：该特性让 Java 调用普通 native 代码更加方便和高效。</p> 
<ul> 
 <li>425：<strong>虚拟线程 (Virtual Threads) 进入预览阶段</strong></li> 
</ul> 
<p>为 Java 引入虚拟线程，虚拟线程是 JDK 实现的轻量级线程，它在其他多线程语言中已经被证实是十分有用的，比如 Go 中的 Goroutine、Erlang 中的进程。虚拟线程避免了上下文切换的额外耗费，兼顾了多线程的优点，简化了高并发程序的复杂，可以有效减少编写、维护和观察高吞吐量并发应用程序的工作量。</p> 
<p>详情查看 <em><a href="https://www.oschina.net/news/190175/java-virtual-threads-preview" target="_blank">Java 引入预览版虚拟线程（协程）功能，大幅提高应用吞吐量</a></em></p> 
<ul> 
 <li><strong>426：向量 API (Vector API) 进入第 4 孵化阶段</strong></li> 
</ul> 
<p>向量计算由对向量的一系列操作组成。向量 API 用来表达向量计算，该计算可以在运行时可靠地编译为支持的 CPU 架构上的最佳向量指令，从而实现优于等效标量计算的性能。向量 API 的目标是为用户提供简洁易用且与平台无关的表达范围广泛的向量计算。</p> 
<ul> 
 <li><strong>427：switch 模式匹配 (Pattern Matching for switch) 进入第 3 预览阶段</strong></li> 
</ul> 
<p>用<code>switch</code>表达式和语句的模式匹配，以及对模式语言的扩展来增强 Java 编程语言。将模式匹配扩展到<code>switch</code>中，允许针对一些模式测试表达式，这样就可以简明而安全地表达复杂的面向数据的查询。</p> 
<ul> 
 <li>428：<strong>结构化并发 (Structured Concurrency) 进入孵化阶段</strong></li> 
</ul> 
<p>JDK 19 引入了结构化并发，这是一种多线程编程方法，目的是为了通过结构化并发 API 来简化多线程编程，并不是为了取代 java.util.concurrent，目前处于孵化阶段。</p> 
<p>结构化并发将不同线程中运行的多个任务视为单个工作单元，从而简化错误处理、提高可靠性并增强可观察性。也就是说，结构化并发保留了单线程代码的可读性、可维护性和可观察性。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjdk.java.net%2F19%2F" target="_blank">下载地址</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjdk.java.net%2F19%2Frelease-notes" target="_blank">Release Note</a></p>
                                        </div>
                                      
</div>
            