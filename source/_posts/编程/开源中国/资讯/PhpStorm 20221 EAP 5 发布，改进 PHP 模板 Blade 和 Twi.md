
---
title: 'PhpStorm 2022.1 EAP 5 发布，改进 PHP 模板 Blade 和 Twi'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1e24bb111e193be330031c451efa1ad196b.gif'
author: 开源中国
comments: false
date: Thu, 17 Mar 2022 07:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1e24bb111e193be330031c451efa1ad196b.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#27282c">PhpStorm 2022.1 的第五个尝鲜版本对流行的 PHP 模板引擎 Blade 和 Twig 进行了改进，与其他 EAP 版本一样，此版本可免费使用，但将在构建日期后 30 天到期。</span></p> 
<h2><span style="background-color:#ffffff; color:#27282c">增强对 Blade 模板的支持</span></h2> 
<p>以前，PhpStorm 将 Blade 模板中的每个代码块视为一个独立的范围，这导致了一些问题，例如丢失代码完成：</p> 
<p><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-1e24bb111e193be330031c451efa1ad196b.gif" width="700" referrerpolicy="no-referrer"></p> 
<p>PhpStorm 2022.1 对 IDE 处理 Blade 模板的方式进行了重大修改，现可在 .blade.php 文件中获得更好的代码完成方式：</p> 
<p><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-5f80bd44ee82fd65b4127eefd073c890bf0.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Blade 模板中代码完成和格式化的更多问题也得到了解决：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-37741" target="_blank">WI-37741</a> Blade 中 PHP 变量的自动完成</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-34830" target="_blank">WI-34830</a> Blade：支持 php 中的命名空间</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-64460" target="_blank">WI-64460</a> Blade：如果有 php block ()，则标签内的方法缺少完成</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-64463" target="_blank">WI-64463</a> Blade：两个连续的@php 片段合并在一起并产生“预期：表达式”警告</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-31196" target="_blank">WI-31196</a> Blade：html 注释格式错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-40358" target="_blank">WI-40358</a> Blade：@if 块内的@section 抛出“指令未关闭”</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWI-64594" target="_blank">WI-64594</a> Blade：支持@js 指令</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fyoutrack.jetbrains.com%2Fissues%2FWI%3Fq%3Dblade%2520%2523Verified%2520sort%2520by%3A%2520updated%2520" target="_blank"> Bug 跟踪器</a>上的完整列表以获取更多信息。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:start">Twig 模板的改进</h2> 
<p><strong>禁用关闭标签自动补全的新选项</strong></p> 
<p>一些用户希望他们的 Twig 标签在输入 &#123;% 后不会自动关闭，这种行为现在是可配置的：</p> 
<p><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-da9cce582a6bfbc40d441e25bd13a577e37.png" width="700" referrerpolicy="no-referrer"></p> 
<p>如果将开始和结束标记从 &#123;% 更新到 &#123;&#123; ，现在也将同时编辑开始和结束标记。</p> 
<p> </p> 
<p>有关此版本中 PhpStorm 的更改完整列表，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FWI-A-14%2FPhpStorm-2022.1-EAP-5-%28221.4994.43-build%29-Release-Notes" target="_blank"><strong>发行说明</strong></a>。</p>
                                        </div>
                                      
</div>
            