
---
title: 'PhpStorm 2022.1 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1e24bb111e193be330031c451efa1ad196b.gif'
author: 开源中国
comments: false
date: Sat, 16 Apr 2022 07:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1e24bb111e193be330031c451efa1ad196b.gif'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#27282c">PhpStorm 2022.1 正式发布啦！该版本包括改进的 Blade 和 Twig 支持、新的高级 PHP 元数据功能、@method 注解中的泛型以及对编辑器的一些改进等内容，下面摘录部分新特性作介绍：</span></p> 
<h2><span style="background-color:#ffffff; color:#27282c">增强对 Blade 模板的支持</span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">以前，PhpStorm 将 Blade 模板中的每个代码块视为一个独立的范围，这导致了一些问题，例如丢失代码完成：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-1e24bb111e193be330031c451efa1ad196b.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">PhpStorm 2022.1 对 IDE 处理 Blade 模板的方式进行了重大修改，现可在 .blade.php 文件中获得更好的代码完成方式：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-5f80bd44ee82fd65b4127eefd073c890bf0.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Blade 模板中代码完成和格式化的更多问题也得到了解决：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-37741" target="_blank">WI-37741</a> Blade 中 PHP 变量的自动完成</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-34830" target="_blank">WI-34830</a> Blade：支持 php 中的命名空间</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-64460" target="_blank">WI-64460</a> Blade：如果有 php block ()，则标签内的方法缺少完成</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-64463" target="_blank">WI-64463</a> Blade：两个连续的@php 片段合并在一起并产生“预期：表达式”警告</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-31196" target="_blank">WI-31196</a> Blade：html 注释格式错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-40358" target="_blank">WI-40358</a> Blade：@if 块内的@section 抛出“指令未关闭”</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-64594" target="_blank">WI-64594</a> Blade：支持@js 指令</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fyoutrack.jetbrains.com%2Fissues%2FWI%3Fq%3Dblade%2520%2523Verified%2520sort%2520by%3A%2520updated%2520" target="_blank"><span> </span>Bug 跟踪器</a>上的完整列表以获取更多信息。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"> </p> 
<h2>Twig 模板的改进</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>禁用关闭标签自动补全的新选项</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一些用户希望他们的 Twig 标签在输入 &#123;% 后不会自动关闭，这种行为现在是可配置的：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-da9cce582a6bfbc40d441e25bd13a577e37.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如果将开始和结束标记从 &#123;% 更新到 &#123;&#123; ，现在也将同时编辑开始和结束标记。</p> 
<h2>WordPress 的改进</h2> 
<p><strong>从 Hook 调用跳转到注册</strong></p> 
<p>在 PhpStorm 2022.1 中，调用左侧有一个装订线图标。单击它可以查看 hook 用法列表，包括注册和其他调用。</p> 
<p><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-d12ec63d49d592ad057f45514203d27a40f.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>使用 get_template_directory_uri() 支持动态路径</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span style="background-color:#ffffff; color:#27282c">在路径中添加了对 get_template_directory_uri() 函数的支持。</span></p> 
<p><span style="background-color:#ffffff; color:#27282c"><img alt src="https://oscimg.oschina.net/oscnet/up-7f0adc30fc49963ef5b6cfe1df75329725e.gif" width="700" referrerpolicy="no-referrer"></span></p> 
<h2><span style="background-color:#ffffff; color:#27282c">多行和嵌套数组形状</span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PhpStorm 2022.1  <strong>在 PHPDoc 和属性中添加了对多行和嵌套数组形状的完全支持：</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-66dd002dbec1a3b3b33952be444b286a44e.gif" width="700" referrerpolicy="no-referrer"></strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>     </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#27282c">在这种情况下，可以使用数组形状注释定义数组结构，以获得键的代码补全并推断值的类型。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#27282c">也可以在 PhpStorm 中使用 Booth PHPDoc 和 Attribute 语法，这些语法支持返回类型和参数类型定义：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#27282c"><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-1117b685ea73ad85bcb1573305f7777a317.gif" width="700" referrerpolicy="no-referrer"></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>除了多行和嵌套注释支持外，数组形状还有许多其他改进。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>@method 注解中的泛型</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PhpStorm 2022.1 支持 @method 定义中的泛型类型：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt src="https://oscimg.oschina.net/oscnet/up-941ecc75d236c6226d2b1f9762227586e9d.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的高级 PHP 元数据功能</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">除了内置的“代码感知”能力，PhpStorm 还依赖于外部的代码知识。这些知识以<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fphpstorm%2F2018%2F03%2Fhow-to-provide-stubs-for-phpstorm%2F" target="_blank">PHP 存根</a><span> </span>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fphpstorm%2Fide-advanced-metadata.html" target="_blank"><strong>.phpstorm.meta.php</strong></a>文件的形式出现。</p> 
<h3>支持 magic __call 和 __callStatic</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">之前如果你依赖<span> </span><span style="color:#27282c">magic 方法的<span> </span></span>__call 或者 __callStatic ，则可能失去其自动补全功能，因为这些方法未定义。在 2022.1 EAP 中，<span style="color:#27282c">可以添加相应的元数据条目，并获得此类调用的自动补全功能：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="363" src="https://static.oschina.net/uploads/space/2022/0130/072637_XuuB_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#27282c">甚至可以自动处理动态调用，从参数值接收特定的方法名称：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="286" src="https://static.oschina.net/uploads/space/2022/0130/073059_zdDJ_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>支持@|MyClass 类型</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#27282c">现在可以将联合类型指定为 @|MyClass ：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="420" src="https://static.oschina.net/uploads/space/2022/0130/073032_NAlY_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fphpstorm%2Fide-advanced-metadata.html" target="_blank">在文档</a>中了解有关其他元数据功能的更多信息。</p> 
<h3>新的 Composer 项目向导</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">增强<span> </span><em><strong>新建项目</strong><span> </span></em>向导：当创建一个新的空项目时您可以选择为其自动生成一个<code>composer.json</code>文件，并提供所需的依赖项。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="525" src="https://oscimg.oschina.net/oscnet/up-6ce477e7efe59c3056e41043f110ec27b4d.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">创建项目后，PhpStorm 会提示你安装它们：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="391" src="https://oscimg.oschina.net/oscnet/up-d1527791081f3a12feff9fb636386e05230.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>WebDAV 支持</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">该版本引入了对使用 WebDAV 服务器进行部署的支持。要配置新服务器，请转到<em>首选项 | 构建、执行、部署 | 部署</em>，然后添加一个新的<span> </span><em>WebDAV<span> </span></em>类型的服务器，并提供连接参数：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="544" src="https://oscimg.oschina.net/oscnet/up-cfcacfe5aa7912c57e753a0c9ddacaf2edd.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>覆盖 Rsync 命令行参数</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">PhpStorm 2021.3 为 SFTP 支持引入了 Rsync，以显着加快部署速度。Rsync 工具使用 <code>-zar</code> 命令行选项执行，它将压缩传输的数据 ( <code>z</code>)，保留传输文件和文件夹的权限、所有权和时间戳 ( <code>a</code>)，并递归到子目录 ( <code>r</code>)。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在此版本中，可以自定义选项集：转到 <em>设置 | 首选项 | 工具 | rsync </em>并提供所需的一组选项：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="544" src="https://oscimg.oschina.net/oscnet/up-1be5f0eabf2876022d6b0a5d8deb52a2f08.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>新的检查</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>添加了一些新的检查，旨在简化正则表达式的使用。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3>冗余修饰符</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>以下新检查将报告正则表达式模式中使用，但不影响匹配的修饰符：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li><code>/i</code>（不区分大小写）在不包含字母的模式中</li> 
 <li><code>/D</code>( <em>PCRE_DOLLAR_ENDONLY</em> ) 在不包含美元符号，或包含<code>\m</code>(PCRE_MULTILINE) 修饰符的模式中</li> 
 <li><code>/s</code>（点匹配换行符）在不包含点的模式中</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PhpStorm 提供<code>Alt+Enter</code>快速修复，可以快速删除这些修饰符。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="445" src="https://oscimg.oschina.net/oscnet/up-c01818c8d0f2d5fb7a469e990d16949568d.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>不支持的修饰符</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>该<code>/e</code>修饰符在 PHP 7.0 及更高版本中已弃用。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="191" src="https://oscimg.oschina.net/oscnet/up-17cfbb065f7b2f369c8154f789d4b360781.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"> </p> 
<h2>新的通知工具窗口</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">用新的<em>通知<span> </span></em>工具窗口替换了<em>事件日志实例，</em>可以帮助用户更好地了解来自 IDE 的通知。默认情况下，新工具窗口位于 IDE 窗口的右下角，通知可以分为两类：<em>建议<span> </span></em>和<span> </span><em>时间线</em>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0130/072700_FIFO_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>Markdown 改进</h2> 
<ul> 
 <li>从 Markdown 文件运行命令</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#27282c">README 文件一般用来描述一个软件的运行步骤，</span>PhpStorm 2022.1 将允许直接从这类 Markdown 文件运行命令 —— 只需单击命令左侧装订线中的<span> </span><em>运行<span> </span></em>图标即可。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0130/072716_8ptv_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新选项可以通过<span> </span><em>Detect 命令进行管理，这些命令可以直接从 Preferences / Settings |<span> </span></em>中的 Markdown 文件运行。</p> 
<ul> 
 <li>复制 Markdown 的代码片段</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新版本向 Markdown 块添加了一个新的<em>复制代码片段<span> </span></em>操作，可以快速复制 Markdown 的代码到剪贴板。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0130/072730_2T9m_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>LightEdit 模式下的代码重新格式化</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fphpstorm%2Flightedit-mode.html" target="_blank"><em>LightEdit<span> </span></em>模式下</a>，无需创建或加载整个项目即可快速编辑文件。现在也可以在<span> </span><em>LightEdit<span> </span></em>模式下重新格式化代码。</p> 
<h2>对 Vue 的改进</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> JetBrains 的 IDE 2022.1 版本对 Vue 3 进行了多项改进，PhpStorm 整合了 WebStorm 对 HTML/CSS/JS 和其他 Web 技术的所有改进。在此版本中，如果你将组件定义为全局，IDE 将在你的 <em>.vue </em>文件中识别它们。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">PhpStorm 也正确支持 createApp 语法，它将正确匹配使用 createApp 相关元素创建的应用程序。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-ff83710389713b1bf7d6f0e7eccd7a5070b.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">该版本还包含一些 Git 操作改进和 Docker 功能增强，完整内容可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fphpstorm%2F2022%2F04%2Fphpstorm-2022-1-release%2F" target="_blank">官方发行公告博客</a>。</p>
                                        </div>
                                      
</div>
            