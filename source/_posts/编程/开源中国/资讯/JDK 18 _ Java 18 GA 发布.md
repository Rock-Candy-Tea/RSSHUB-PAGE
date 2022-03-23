
---
title: 'JDK 18 _ Java 18 GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3039'
author: 开源中国
comments: false
date: Wed, 23 Mar 2022 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3039'
---

<div>   
<div class="content">
                                                                    
                                                        <p>JDK 18 / Java 18 GA 发布。JDK 18 是一个短期维护版本，将获得六个月的支持。尽管如此，但它仍然可用于生产环境中。根据开发计划，JDK 19 将于今年 9 月发布，而下一个 LTS 版本 JDK 21 将于 2023 年 9 月发布。</p> 
<p>JDK 18 共包括 9 个 JEP，以及数百个较小的增强功能和一千多个错误修复。</p> 
<table class="jeps" style="width:100%" summary="jeps"> 
 <tbody> 
  <tr> 
   <td>400:</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F400" target="_blank">UTF-8 by Default</a></td> 
  </tr> 
  <tr> 
   <td>408:</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F408" target="_blank">Simple Web Server</a></td> 
  </tr> 
  <tr> 
   <td>413:</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F413" target="_blank">Code Snippets in Java API Documentation</a></td> 
  </tr> 
  <tr> 
   <td>416:</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F416" target="_blank">Reimplement Core Reflection with Method Handles</a></td> 
  </tr> 
  <tr> 
   <td>417:</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F417" target="_blank">Vector API (Third Incubator)</a></td> 
  </tr> 
  <tr> 
   <td>418:</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F418" target="_blank">Internet-Address Resolution SPI</a></td> 
  </tr> 
  <tr> 
   <td>419:</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F419" target="_blank">Foreign Function & Memory API (Second Incubator)</a></td> 
  </tr> 
  <tr> 
   <td>420:</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F420" target="_blank">Pattern Matching for switch (Second Preview)</a></td> 
  </tr> 
  <tr> 
   <td>421:</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fjeps%2F421" target="_blank">Deprecate Finalization for Removal</a></td> 
  </tr> 
 </tbody> 
</table> 
<h3><strong>默认编码为 UTF-8</strong></h3> 
<p>将 UTF-8 指定为标准 Java API 的默认字符集。 通过此更改，依赖于默认字符集的 API 将在所有实现、操作系统、语言环境和配置中保持一致。</p> 
<h3><strong>简易 HTTP 服务器</strong></h3> 
<p>提供命令行工具来启动一个仅提供静态文件的最小 Web 服务器。没有可用的 CGI 或类似 servlet 的功能。该工具可用于原型设计、临时编码和测试目的，尤其是在教育环境中。</p> 
<h3><strong>Java API 文档中的代码片段</strong></h3> 
<p>为 JavaDoc 的 Standard Doclet 引入一个 @snippet 标签，以简化 API 文档中的示例源代码。</p> 
<h3><strong>用方法句柄（Method Handles）重新实现 Java 核心反射</strong></h3> 
<p>在 java.lang.invoke 方法句柄的基础上重新实现 java.lang.reflect.Method、Constructor 和 Field。让方法句柄成为反射的底层机制将减少 java.lang.reflect 和 java.lang.invoke API 的维护和开发成本。</p> 
<h3><strong>Vector API （第三次进行孵化）</strong></h3> 
<p>引入一个 API 来表达在运行时能够可靠编译的向量计算，在支持的 CPU 架构上优化向量指令，从而实现优于标量计算的性能。</p> 
<h3><strong>互联网地址解析 SPI</strong></h3> 
<p>定义一个用于主机名称和地址解析的服务供给接口（SPI），以便 java.net.InetAddress 可以使用平台内置解析器以外的解析器。</p> 
<h3><strong>外部函数和内存 API（第二次进行孵化）</strong></h3> 
<p>引入一个 API，通过它，Java 程序可以与 Java 运行时之外的代码和数据进行互操作。通过有效地调用外部函数，以及安全地访问外部内存，该 API 使 Java 程序能够调用本地库并处理本地数据，而没有 JNI 的脆弱性和危险。</p> 
<h3><strong>Switch 模式匹配（第二次进行预览）</strong></h3> 
<p>用 <code>switch</code> 表达式和语句的模式匹配，以及对模式语言的扩展来增强 Java 编程语言。将模式匹配扩展到 <code>switch</code> 中，允许针对一些模式测试表达式，这样就可以简明而安全地表达复杂的面向数据的查询。这是 JDK 18 中的一个预览的语言功能。</p> 
<h3><strong>弃用 Finalization，以便在未来删除</strong></h3> 
<p>弃用 Finalization，以便在未来的版本中删除它。目前 Finalization 仍然是默认启用的，但可以禁用它以便进行早期测试。在之后的版本中，它将率先被默认禁用，并在未来的版本中将其彻底删除。依赖于 Finalization 的库和应用程序的维护者应该考虑迁移到其他资源管理技术，如 <code>try-with-resources</code> 语句。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenjdk.java.net%2Fprojects%2Fjdk%2F18%2F" target="_blank">https://openjdk.java.net/projects/jdk/18/</a></p> 
<p>下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjdk.java.net%2F18%2F" target="_blank">https://jdk.java.net/18/</a></p>
                                        </div>
                                      
</div>
            