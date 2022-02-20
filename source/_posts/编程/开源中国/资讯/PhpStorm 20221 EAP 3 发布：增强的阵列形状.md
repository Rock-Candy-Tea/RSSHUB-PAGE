
---
title: 'PhpStorm 2022.1 EAP #3 发布：增强的阵列形状'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-66dd002dbec1a3b3b33952be444b286a44e.gif'
author: 开源中国
comments: false
date: Sun, 20 Feb 2022 08:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-66dd002dbec1a3b3b33952be444b286a44e.gif'
---

<div>   
<div class="content">
                                                                                            <p>PhpStorm 2022.1 早期访问计划的第三个版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fphpstorm%2F2022%2F02%2Fphpstorm-2022-1-eap-3%2F" target="_blank">现已推出</a>，该版本聚焦于对数组形状和注释的增强支持，下面来介绍一下：</p> 
<h2>多行和嵌套数组形状</h2> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PhpStorm 2021.2 在 PHPDoc 块中引入了对数组形状的支持。但是，它有一个很大的限制——仅支持单行和单级注释。如果要</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>获得多行支持，可以选择使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJetBrains%2Fphpstorm-attributes%23arrayshape" target="_blank"><code>#[ArrayShape]</code></a>属性，但是它仍然不支持嵌套结构。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PhpStorm 2022.1 EAP 3 <strong>在 PHPDoc 和属性中添加了对多行和嵌套数组形状的完全支持：</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-66dd002dbec1a3b3b33952be444b286a44e.gif" width="700" referrerpolicy="no-referrer"></strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>     </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#27282c">在这种情况下，可以使用数组形状注释定义数组结构，以获得键的代码补全并推断值的类型。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#27282c">也可以在 PhpStorm 中使用 Booth PHPDoc 和 Attribute 语法，这些语法支持返回类型和参数类型定义：</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#27282c"><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-1117b685ea73ad85bcb1573305f7777a317.gif" width="700" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>除了多行和嵌套注释支持外，数组形状还有许多其他改进。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:start">支持带数字键的数组形状</h3> 
<p><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-95b3822d51559508a51dd6b6c39b7178574.gif" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3>支持类对象数组中的特定数组</h3> 
<p><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-a391cada4f43c1187e89678a20f301242d4.png" width="700" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">支持数组形状的列表</h4> 
<p><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-6492eef707940186b9549df03f1aafc8d74.gif" width="700" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>支持 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span><span><span><span><span><span><span style="color:#939393"><span style="background-color:#fafafa"><span><span><span><span><span><span><span><span><span style="color:#000000">@var</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> 变量用法的数组形状注释</h4> 
<p><img alt height="467" src="https://oscimg.oschina.net/oscnet/up-fea9c0fec8008806f44fa01a0dc5ec9404d.png" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:.5em; margin-right:0; text-align:start">对 Vue 的改进</h2> 
<p> JetBrains 的 IDE 2022.1 版本对 Vue 3 进行了多项改进，PhpStorm 整合了 WebStorm 对 HTML/CSS/JS 和其他 Web 技术的所有改进。在此版本中，如果你将组件定义为全局，IDE 将在你的 <em>.vue </em>文件中识别它们。</p> 
<p>PhpStorm 也正确支持 createApp 语法，它将正确匹配使用 createApp 相关元素创建的应用程序。</p> 
<p><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-ff83710389713b1bf7d6f0e7eccd7a5070b.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#27282c">此版本还包括对 Nuxt 3 的支持。</span></p> 
<p> </p> 
<p>PhpStorm 2022.1 EAP #3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FWI-A-12%2FPhpStorm-2022.1-EAP-3-%28221.4501.163-build%29-Release-Notes" target="_blank">发行说明</a>中提供了完整的更改列表，包括错误修复和改进。</p>
                                        </div>
                                      
</div>
            