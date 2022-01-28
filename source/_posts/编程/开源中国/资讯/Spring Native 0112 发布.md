
---
title: 'Spring Native 0.11.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2761'
author: 开源中国
comments: false
date: Fri, 28 Jan 2022 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2761'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Spring Native 0.11.2 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F01%2F26%2Fspring-native-0-11-2-available-now" target="_blank">发布</a>，此版本共包括 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Freleases%2Ftag%2F0.11.2" target="_blank">30 个错误修复、文档改进和依赖项升级</a>。具体更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>New Features</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>跳过测试时跳过 Maven AOT 测试源生成 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1461" target="_blank">#1461</a></li> 
 <li>对“spring.factories”中的 factories 进行排序<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fpull%2F1424" target="_blank">#1424</a></li> 
 <li>修复“spring.factories”中带有空格的工厂名称<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fpull%2F1421" target="_blank">#1421</a></li> 
 <li>在 AOT 模式下正确禁用 devtools <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1419" target="_blank">#1419</a></li> 
 <li>检测到 logback.xml 时提供有意义的错误信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1415" target="_blank">#1415</a></li> 
 <li>提供一种使用常规代码路径（不是 AOT 路径）执行测试的方法<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1356" target="_blank">#1356</a></li> 
 <li>允许不使用 Gradle 调用测试 aot 任务 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1338" target="_blank">#1338</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Compatibility</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>data-jpa</code>示例原生图像不会在下<code>@EnableJpaRepositories</code>启动 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1405" target="_blank">#1405</a></li> 
 <li>抛出 AnnotationException 显示没有持久 id 属性<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1397" target="_blank">#1397</a></li> 
 <li>添加 Coroutines 反射推理<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F769" target="_blank">#769</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>Optimizations</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>查看 servlet 的 Spring Security 提示 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1392" target="_blank">#1392</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>Bug 修复</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>为 bootJar Gradle 任务预置 AOT jar 到 classpath <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fpull%2F1466" target="_blank">#1466</a></li> 
 <li>在 AOT 生成的 bean 注册中丢失了 dependsOn 属性<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1458" target="_blank">#1458</a></li> 
 <li>扫描带有交叉引用的 ConfigurationProperties 提示时出现 StackOverflowError <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fpull%2F1420" target="_blank">#1420</a></li> 
 <li>尽管该功能被明确禁用，但仍会创建 RefreshScope bean <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1413" target="_blank">#1413</a></li> 
 <li>ConstructorArgumentValues 仅应在存在索引参数值时分配<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1403" target="_blank">#1403</a></li> 
 <li>ResolvableType - java.lang.IllegalArgumentException：指定的泛型数量不匹配<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1401" target="_blank">#1401</a></li> 
 <li><code>@ConfigurationProperties</code>包含泛型属性时 AOT 生成期间的 NPE <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1396" target="_blank">#1396</a></li> 
 <li>细化 TypeModelProcessor 类过滤和错误处理<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1376" target="_blank">#1376</a></li> 
 <li>ClientHttpRequestFactoryHints 中的回归<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1370" target="_blank">#1370</a></li> 
 <li>在 ContextBootstrapInitializer 代码中导入的运行时依赖导致 IDE 编译问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1093" target="_blank">#1093</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Documentation </strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>改进 AOT 并构建设置文档结构<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1467" target="_blank">#1467</a></li> 
 <li>当委托给 Gradle 时，IDEA 中正在运行的应用程序被破坏的文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1465" target="_blank">#1465</a></li> 
 <li>java.lang.IllegalStateException: 多个特权包<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1414" target="_blank">#1414</a></li> 
 <li>说明 -parameters javac 标志对于本机是强制性的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1465" target="_blank">#1465</a></li> 
 <li>除非在 AOT 运行时启用了配置文件，否则不会在运行时选择配置文件中定义的 bean <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1411" target="_blank">#1411</a></li> 
 <li>改进 Windows 支持文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1319" target="_blank">#1319</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>依赖升级</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>升级 GRPC 到 1.43.2 和 protobuf 到 3.19.2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1433" target="_blank">#1433</a></li> 
 <li>升级到 Kotlin 1.6.10 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1437" target="_blank">#1437</a></li> 
 <li>升级到 Spring Boot 2.6.3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Fissues%2F1441" target="_blank">#1441</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects-experimental%2Fspring-native%2Freleases%2Ftag%2F0.11.2" target="_blank">https://github.com/spring-projects-experimental/spring-native/releases/tag/0.11.2</a> </p>
                                        </div>
                                      
</div>
            