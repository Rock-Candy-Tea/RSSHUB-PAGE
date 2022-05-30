
---
title: 'PhpStorm 2022.2 EAP 1 已发布，带来 Rector 支持、泛型改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-01bb900ffb0c24772ada2c3a4e8742420a1.png'
author: 开源中国
comments: false
date: Mon, 30 May 2022 07:46:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-01bb900ffb0c24772ada2c3a4e8742420a1.png'
---

<div>   
<div class="content">
                                                                                            <p>PhpStorm 2022.2 早期访问计划 (EAP) 正式发布！该版本带来泛型、Rector 支持和一系列质量改进的许多新功能。</p> 
<h2>Rector 支持</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frectorphp%2Frector" target="_blank">Rector</a> 可批量进行 PHP 自动升级和代码重构，现在<span style="background-color:#ffffff; color:#27282c">在 PhpStorm 中为它提供内置支持。</span></p> 
<p>使用 PhpStorm 的 Rector 支持，首先需要<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frectorphp%2Frector%23running-rector" target="_blank">安装 Rector 并对其进行配置</a>。接下来应专门为 Rector 创建一个新的运行配置。PhpStorm 可以自动执行此操作：只需右键单击您希望 Rector 修复的文件夹，然后选择 <strong style="color:#27282c">运行 | </strong><strong>Rector </strong>即可。</p> 
<p><img height="393" src="https://oscimg.oschina.net/oscnet/up-01bb900ffb0c24772ada2c3a4e8742420a1.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#27282c">也可以在编辑配置屏幕上手动创建新的 Rector 配置。</span></p> 
<h2><span style="background-color:#ffffff; color:#27282c">泛型</span></h2> 
<p>更新了对泛型的支持：</p> 
<ul> 
 <li><strong><span style="background-color:#ffffff; color:#27282c">Int<min, max></span></strong></li> 
</ul> 
<p>现在支持<code>int<min, max></code>类型</p> 
<p><img height="535" src="https://oscimg.oschina.net/oscnet/up-e8e8b5486d2550d9947fa7e444684548f20.png" width="700" referrerpolicy="no-referrer"></p> 
<div style="text-align:start"> 
 <ul> 
  <li><strong>对可迭代对象的通用支持</strong></li> 
 </ul> 
</div> 
<p style="margin-left:0; margin-right:0; text-align:start">PhpStorm 能够在循环遍历可迭代对象时推断类型：</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img height="451" src="https://oscimg.oschina.net/oscnet/up-de639582a07ecc8b17748283583c831282a.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li style="text-align:start"><strong><span style="background-color:#ffffff; color:#27282c">从闭包推断类型</span></strong></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#27282c">PhpStorm 现在能够从闭包返回值推断泛型类型。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img height="315" src="https://oscimg.oschina.net/oscnet/up-d0e5665ca3b7772362c98047f3050228ccd.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li style="text-align:start"><strong>支持绕过泛型类型</strong></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start">PhpStorm 现在可以更好地处理方法<code>Collection::lazy()</code>，其中泛型类型被代理到另一个对象中：</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img height="321" src="https://oscimg.oschina.net/oscnet/up-a1fcdd5807db3c81f50012df4c558d0a0ed.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>关于泛型的更多功能：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>改进了对嵌套泛型的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-66014%2FSupport-passing-template-parameter-into-static-for-different-fil" target="_blank">WI-66014</a> )。</li> 
 <li>翻转泛型类型 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-66015%2FSupport-switching-template-parameters-for-key-value-static-Tk-Tv" target="_blank">WI-66015</a> )。</li> 
 <li>支持迭代器中的泛型：<code>Iterator<Type></code> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-62323%2FGeneric-notation-for-iterator-generator-value-types" target="_blank">WI-62323</a> )。</li> 
 <li>在可迭代中支持泛型：<code>iterable<KeyType, ValueType></code>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-56037%2FSupport-iterable-type" target="_blank">WI-56037</a> )。</li> 
 <li><code>@extends \SplFixedArray<Token></code>现在按预期工作<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-65964%2FType-of-element-returned-by-current-method-of-SplFixedArray-cont" target="_blank">（WI-65964）</a>。</li> 
 <li>改进的泛型类型推断 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-60891%2FSupport-array-Tk-Tv-unwrapping-for-return-Tv-value-type" target="_blank">(WI-60891)</a>。</li> 
</ul> 
<h2>其他更新项</h2> 
<ul> 
 <li><span style="background-color:#ffffff; color:#27282c">添加了对在数组中自动插入箭头和逗号的支持。</span></li> 
 <li><span style="background-color:#ffffff; color:#27282c">可以将 PhpStorm 配置为在参数列表、闭包使用列表和函数调用中自动插入尾随逗号。</span></li> 
 <li>支持<span style="background-color:#ffffff; color:#27282c"><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flaravel.com%2Fdocs%2F9.x%2Fblade%23accessing-parent-data" target="_blank">blade<span> </span>组件</a>中的<code>@props</code>和<code>@aware</code>指令。</li> 
 <li style="text-align:start"><span style="background-color:#ffffff; color:#27282c">可以配置在运行 PHP CS Fixer 或 PHPUnit 等工具时要使用的 PHP 二进制文件。</span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#27282c">更多内容请在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fphpstorm%2F2022%2F05%2Fphpstorm-2022-2-early-access-program-is-open%2F" target="_blank">发行公告</a>中查阅。</span></p>
                                        </div>
                                      
</div>
            