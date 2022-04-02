
---
title: 'IntelliJ IDEA 2022.1 Beta 2  发布，增强 Kotlin IDE 性能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a4fc07b3ac35df9f94ca99e9005ae347247.png'
author: 开源中国
comments: false
date: Sat, 02 Apr 2022 07:40:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a4fc07b3ac35df9f94ca99e9005ae347247.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#27282c">IntelliJ IDEA 2022.1 Beta 2 已发布，该 Beta 版本包含 EAP 版本中未介绍的一些新特性，比如更新 Java 版本支持、使用 Kotlin 时改进的 IDE 性能等。</span></p> 
<h3>Java 18 支持</h3> 
<p><span style="background-color:#ffffff; color:#27282c">IntelliJ IDEA 2022.1 支持 2022 年 3 月发布的<a href="https://www.oschina.net/news/187796/jdk-18-ga"> Java 18</a> 的新功能，IDE 现在支持代码片段、开关表达式的模式匹配更改等。</span>有关详细信息，请参阅此<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F03%2Fjava-18-features-support%2F" target="_blank">博客文章</a>。  </p> 
<h3>更好的 JUnit 5 支持</h3> 
<p>添加了对 JUnit 5.7 中引入的新功能的支持，包括对 <em>@EnabledIf/DisabledIf</em>、<em>@NullSource/EmptySource </em>和 <em>@TempDir </em>注释的支持。</p> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-a4fc07b3ac35df9f94ca99e9005ae347247.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#27282c">此外还引入了一些更新，确保与 Kotlin 的功能相同。</span></p> 
<h3>改进了 Kotlin 的 IDE 性能</h3> 
<p>优化了包索引，大大提高了 IDE 在执行代码完成、突出显示和与参考搜索等相关操作时的速度，在代码更改后发生的重新索引案例的数量和范围也有所减少。</p> 
<p><img alt height="540" src="https://oscimg.oschina.net/oscnet/up-760371713fc13766f75c8628e083e5b72c7.png" width="700" referrerpolicy="no-referrer"></p> 
<h3><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>调试器改进 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在调试 Kotlin 项目时对 <em>Smart Step Into </em>的功能进行了一些有用的改进和更新，还解决了一些涉及断点的问题。 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Kover 插件集成</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>为了确保更好的 Kotlin 代码覆盖率，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKotlin%2Fkotlinx-kover" target="_blank">Kover 插件</a>已与 IntelliJ IDEA 集成。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的 <em>不正确格式 </em>检查</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start">该版本实现了<strong>不正确的格式</strong>检查，如果文件的当前格式与代码样式设置不匹配，就会通知用户。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-b525a3cc46072ad5d8d14e8f487a0154943.png" width="700" referrerpolicy="no-referrer"></p> 
<h3><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><em>Inlay Hints </em></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>：新的设置 UI  </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>为 <em>Inlay Hints </em>设置实现了一个新的 UI，允许用户根据希望 IDE 提供的提示类型来配置首选项。 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-0226523ff426697aca273a57f1708f0867e.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="margin-left:0; margin-right:0; text-align:start">该 Beta 2 版本还包含其他更新项，完整更新列表请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FIDEA-A-147%2FIntelliJ-IDEA-2022.1-Beta-2-%28221.5080.93-build%29-Release-Notes" target="_blank">发行说明</a>。</p>
                                        </div>
                                      
</div>
            