
---
title: 'Dart 2.17 正式发布：提升生产力、实验性支持 RISC-V'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f7b03daab8aa9c2768ffa6a4a50c856d6e0.png'
author: 开源中国
comments: false
date: Mon, 16 May 2022 14:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f7b03daab8aa9c2768ffa6a4a50c856d6e0.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Dart 2.17 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fdartlang%2Fdart-2-17-b216bfc80c5d" target="_blank">发布</a>。</p> 
<p><strong>重要新特性</strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#494949">枚举已支持成员变量</span></li> 
 <li><span style="background-color:#ffffff; color:#494949">改进对超类的参数转发</span></li> 
 <li><span style="background-color:#ffffff; color:#494949">为命名参数提供更大灵活性</span></li> 
 <li><span style="background-color:#ffffff; color:#494949">在 Flutter 插件提供新模板，通过使用</span><code>dart:ffi</code><span style="background-color:#ffffff; color:#292929"><span> </span>（与 C 进行原生互操作），改进了平台集成</span></li> 
 <li><span style="background-color:#ffffff; color:#494949">实验性支持 RISC-V 处理器</span></li> 
 <li><span style="background-color:#ffffff; color:#494949">对 macOS 和 Windows 可执行文件的签名支持</span></li> 
</ul> 
<p><img src="https://oscimg.oschina.net/oscnet/up-f7b03daab8aa9c2768ffa6a4a50c856d6e0.png" referrerpolicy="no-referrer"></p> 
<p><strong><span style="background-color:#ffffff; color:#494949">支持成员变量的枚举</span></strong></p> 
<p><span style="background-color:#ffffff; color:#1b1b1d">Dart 2.17 现已支持枚举类型的成员变量。这意味着开发者可以添加保存状态的字段、设置状态的构造函数、具有功能的方法，甚至重载现有的方法。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1e46b07250ba22bf97d235d164662bfb72a.png" referrerpolicy="no-referrer"></p> 
<p><strong>超类的初始化构造</strong></p> 
<p>对于类型继承关系，常见的处理是将一些构造函数参数传递给超类的构造函数。为此，子类需要</p> 
<ol> 
 <li>在其构造函数中列出每个参数</li> 
 <li>使用这些参数调用超类的构造函数，这导致开发者要编写大量重复代码，降低代码阅读性，且不易维护</li> 
</ol> 
<p>Dart 2.17 通过引入一个新结构来表示在超类中指定了一个参数来解决此问题。官方称将此特性应用到 Flutter 框架时，总共<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fpull%2F100905%2Ffiles" target="_blank">减少了近 2000 行代码</a>。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b7bd2f0e703618a2bdd0a989af44cc44ae6.png" referrerpolicy="no-referrer"></p> 
<p>向 Flutter 插件添加<code>dart:ffi</code><span style="background-color:#ffffff; color:#494949">模板</span></p> 
<p>在 Flutter 中，<span style="background-color:#ffffff; color:#1b1b1d">FFI 是构建使用宿主平台原生 API（例如 Windows win32 API）插件的主流方法。在 Dart 2.17 和 Flutter 3 中，官方向</span><code>flutter</code><span style="background-color:#ffffff; color:#1b1b1d">工具添加了 FFI 模板，开发者现在可以轻松地创建 FFI 插件，这些插件具有通过</span><code>dart:ffi</code><span style="background-color:#ffffff; color:#1b1b1d">调用原生代码支持的 Dart API。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.flutter.dev%2Fdevelopment%2Fpackages-and-plugins%2Fdeveloping-packages%23dart-only-platform-implementations" target="_blank">详情信息</a></span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fdartlang%2Fdart-2-17-b216bfc80c5d" target="_blank">更多内容查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            