
---
title: 'Spring Shell 2.1 发布，基于 Spring 的交互式 shell'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202207/28072701_mHQU.gif'
author: 开源中国
comments: false
date: Thu, 28 Jul 2022 07:27:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202207/28072701_mHQU.gif'
---

<div>   
<div class="content">
                                                                                            <p>Spring Shell 2.1.x 完全依赖于 Spring Boot 2.x，并不试图与旧的 Spring Shell 1.x 或 Spring Boot 1.x 保持任何向后兼容。</p> 
<p>Spring Shell 2.1 发布，更新内容如下：</p> 
<h3>Command Registration</h3> 
<p><code>CommandRegistration</code> 是一种定义命令的新编程方式。现有的命令注解模型可以转化为场景背后的这些注册。这个新的注册模型现在允许我们动态地控制命令，这在旧的 shell 实现中是不可能的。</p> 
<h3>现有注解</h3> 
<p>对于 <code>@ShellMethod</code> 和 <code>@ShellOption</code>，我们试图保持它们的兼容性，未来的发展很可能会引入新的注解，与 <code>CommandRegistration</code> 更加一致。</p> 
<h3>主题化</h3> 
<p>现代终端的实现并不局限于显示一个简单的文本，而是允许不同类型的字体样式，并且可以使用颜色。在旧的 Spring Shell 中，这些大多是硬编码的，同时可以通过 JLine 使用 ANSI 序列将任何东西写进控制台。引入一个主题系统是有意义的，在这个系统中，所写的文本可以被样式化，这是创建漂亮的 shell UI 的基础。</p> 
<p><img alt="https://user-images.githubusercontent.com/50398/180449734-4186d36a-462e-4798-b9db-444aa4c5cb7e.gif" src="https://static.oschina.net/uploads/img/202207/28072701_mHQU.gif" referrerpolicy="no-referrer"></p> 
<p><img alt="https://user-images.githubusercontent.com/50398/180449857-2bcc06ac-1705-4934-8485-7f78bf7a6f76.gif" src="https://static.oschina.net/uploads/img/202207/28072701_W4TZ.gif" referrerpolicy="no-referrer"></p> 
<h3>UI 组件</h3> 
<p>你很可能使用过各种 CLI 工具，这些工具不仅仅是向用户询问一些文本，然后在此基础上做一些事情。例如，GitHub CLI 就是一个很好的例子，它的一些命令会进入交互模式，并使用各种技巧要求用户输入，如选择器列表和其他类型的 shell</p> 
<p>我们想在 Spring Shell 中完成的是创建这些组件，它们可以独立使用，也可以将这些组件组合成一个流程。</p> 
<p><img alt="https://user-images.githubusercontent.com/50398/180447680-8fa40f23-9ce6-4cd2-87b2-22c8ee09256f.svg" src="https://static.oschina.net/uploads/img/202207/28072702_Fvb2.svg" referrerpolicy="no-referrer"></p> 
<h3>Graal</h3> 
<p>在未来的 Spring Framework 版本中，一个重要的话题是用 GraalVM 进行本地编译。这显然对 CLI 有很大的影响，因为当你的现有代码被翻译成本地二进制时，那个小小的 jvm bootstrap 超时就会消失。</p> 
<p>在 2.1.x 版本中，我们用实验性的 Spring Native 项目证明了可以创建一个在 Linux、macOS 和 Windows 中以同样方式工作的 Spring Shell 应用程序。</p> 
<p><img alt="https://user-images.githubusercontent.com/50398/180446288-a1c3ed95-b20c-4cdb-924f-ab283c514e24.gif" src="https://static.oschina.net/uploads/img/202207/28072703_uehU.gif" referrerpolicy="no-referrer"></p> 
<p><img alt="https://user-images.githubusercontent.com/50398/180446731-9e08dc96-cfe1-4ca5-a978-2783c1cb4a52.gif" src="https://static.oschina.net/uploads/img/202207/28072704_gGDP.gif" referrerpolicy="no-referrer"></p> 
<p><img alt="https://user-images.githubusercontent.com/50398/180483578-89f0da8d-2773-46b8-aef8-70d1176a7f49.png" src="https://static.oschina.net/uploads/img/202207/28072704_5FUi.png" referrerpolicy="no-referrer"></p> 
<p>Spring Shell 对 GraalVM 的正式支持将在 3.x 版本中推出。</p> 
<h3>模板化</h3> 
<p>现在 Spring Shell 的一些默认输出是基于 ANTRL 项目的 ST4 的模板。这使得用户可以替换 Spring Shell 中使用的模板并修改默认行为。这些模板也集成到了主题框架中，这样就有可能为每个活动主题定义模板。</p> 
<h3>修复</h3> 
<p>本 GA 包含一些显着的变化：</p> 
<ul> 
 <li>基于 Spring Boot 2.7.2 构建</li> 
 <li>一些样式变化</li> 
 <li>Help 命令现在知道别名</li> 
 <li>MultiItemSelector 组件现在可以默认选择项目</li> 
 <li>@ShellOption 的一些修复</li> 
 <li>修复 using-shell-options-optional.adoc 中的拼写错误</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-shell%2Freleases%2Ftag%2Fv2.1.0" target="_blank">https://github.com/spring-projects/spring-shell/releases/tag/v2.1.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            