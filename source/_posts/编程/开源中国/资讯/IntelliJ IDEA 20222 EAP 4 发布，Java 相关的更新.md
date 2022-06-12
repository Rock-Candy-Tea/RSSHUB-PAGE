
---
title: 'IntelliJ IDEA 2022.2 EAP 4 发布，Java 相关的更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8e6229d373ea2785d06f013474815678198.png'
author: 开源中国
comments: false
date: Sun, 12 Jun 2022 07:33:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8e6229d373ea2785d06f013474815678198.png'
---

<div>   
<div class="content">
                                                                                            <p>IntelliJ IDEA 2022.2 EAP 4 现已推出，此 EAP 构建具有与 Java 相关的更新，通过新的 inspections 和 quick-fixes 提供改进的<span style="background-color:#ffffff; color:#27282c"><span> </span>code completion</span> 和更好的 code analysis。<span style="background-color:#ffffff; color:#333333">开发者可以从</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fidea%2Fnextversion%2F" target="_blank">网站</a><span style="background-color:#ffffff; color:#333333">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Ftoolbox-app%2F" target="_blank">Toolbox App</a><span style="background-color:#ffffff; color:#333333">，或通过使用 Ubuntu 的 snaps 下载最新版本。</span></p> 
<p><strong>新的 Java inspections</strong></p> 
<p><span style="background-color:#ffffff; color:#27282c">Deep data flow analysis<span> </span></span>现在被用于不可转换类型的对象之间的"equals"检查。<span style="background-color:#ffffff; color:#27282c">即使声明的变量类型相同，这也可以检测到问题。</span></p> 
<p><img height="200" src="https://oscimg.oschina.net/oscnet/up-8e6229d373ea2785d06f013474815678198.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>当模式变量隐藏字段时，会有一个新的 inspection 向用户发出警告。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><img height="202" src="https://oscimg.oschina.net/oscnet/up-74f6abbf789548a4eb447532b51ce0c226e.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>可以使用 Standard ‘Charset’ object 的 inspection 已得到改进，现在可以识别 .name() 和 .toString()。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><img height="201" src="https://oscimg.oschina.net/oscnet/up-31e8e3653e863678dcc7f5309895caa3c4b.png" width="500" referrerpolicy="no-referrer"></p> 
<p>IDE 现在提供更好的报告，并在三元运算符中意外拆箱导致 NullPointerException 时建议 quick-fix。</p> 
<p><img height="201" src="https://oscimg.oschina.net/oscnet/up-da37de5680c82819f532369894791e51cec.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span>另一项新的检查可以捕获无意义的 Objects.requireNonNullElse 调用。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img height="200" src="https://oscimg.oschina.net/oscnet/up-44a99377f1e197c1e78e24aa0c9c7ab8f87.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>还升级了 Raw 使用参数化类检查的 quick-fix，在构造 raw types 时增加了一个 diamond operator。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="200" src="https://oscimg.oschina.net/oscnet/up-5c97113dec2084b9ce5d38fb9ccff0000e3.gif" width="500" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Javadoc 声明问题检查获得了新的 quick-fix，当 method 不提供 throws 部分时，可以从文档中删除多余的 @throws。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img height="199" src="https://oscimg.oschina.net/oscnet/up-85aed13e5f549853be9d6b07025fc1e1ad4.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>许多与 JUnit 相关的 Java 检查已转换为 JVM 检查，因此它们现在也可以在 Kotlin 中使用。包括 Unconstructable JUnit 测试类和 JUnit malformed declaration。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong>改进的 code completion</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start">Code completion 得到了改进，现在适用于 .class literals 的情况。</p> 
<p><img height="200" src="https://oscimg.oschina.net/oscnet/up-c6ede5dc74b1b9106659f54d20e07347bd4.png" width="500" referrerpolicy="no-referrer"></p> 
<p>详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F06%2Fintellij-idea-2022-2-eap-4%2F" target="_blank">查看官方博客</a>。</p>
                                        </div>
                                      
</div>
            