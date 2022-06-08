
---
title: 'PhpStorm 2022.2 EAP 2 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ba802ec3a2afe667c445ed7cfb51bfd2b19.png'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 07:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ba802ec3a2afe667c445ed7cfb51bfd2b19.png'
---

<div>   
<div class="content">
                                                                                            <p>PhpStorm 2022.2 第二个抢先体验版本（EAP 2）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fphpstorm%2F2022%2F06%2Fphpstorm-2022-2-eap-2%2F" target="_blank">上线</a>啦！该版本依旧带来了一些新功能，下面对这些功能作介绍~</p> 
<ul> 
 <li><strong>将多个<code>isset()</code>调用合并为一个</strong></li> 
</ul> 
<p>PHP 允许将多个参数传递到一个 isset() 调用中。</p> 
<p><img height="353" src="https://oscimg.oschina.net/oscnet/up-ba802ec3a2afe667c445ed7cfb51bfd2b19.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>尽可能使用 <code>in_array()</code>和<code>array_key_exists()</code></strong></li> 
</ul> 
<p>PhpStorm 能够检测可以优化<code>in_array()</code>或<code>array_key_exists()</code>调用的 for 循环。</p> 
<p><img height="394" src="https://oscimg.oschina.net/oscnet/up-1785dec01505c2c4c7d37c31b1bc4d3ab5d.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>不明确时，将变量名称添加到 @var 和 @param 文档块</strong></li> 
</ul> 
<p>有时 PhpStorm 无法确定 @var 或 @param docblock 引用哪个变量，该版本添加了一个检查功能，以轻松地指向正确的变量。</p> 
<p><img height="332" src="https://oscimg.oschina.net/oscnet/up-2d3cf8b29e487007dddf757126f4aa02d44.png" width="700" referrerpolicy="no-referrer"></p> 
<div style="text-align:start"> 
 <ul> 
  <li><strong>转换 array|Traversable 为 iterable</strong></li> 
 </ul> 
</div> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在 PHP 中，<code>array|Traversable</code>联合等于内置<code>iterable</code>类型。PhpStorm 现在建议用后者替换前者，从而使代码更清晰。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img height="316" src="https://oscimg.oschina.net/oscnet/up-3f85dcf82fd349fa2f53bc922065fbf094a.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>转换<code><?php echo …; ?></code>为<code><?=</code></strong></li> 
</ul> 
<p>允许在 <strong><code><?php echo …; ?></code></strong>和<strong><code><?=</code></strong>在整个文件中互相切换。</p> 
<p><img height="458" src="https://oscimg.oschina.net/oscnet/up-3c2bdc04bdf8a2e035e718c072d86a6321d.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>用 explode 替换简单的<code>preg_split</code>()调用</strong></li> 
</ul> 
<p>PhpStorm 现在将检测简单的<code>preg_split</code>() 调用并建议使用<code>explode</code>() 代替。</p> 
<p><img height="339" src="https://oscimg.oschina.net/oscnet/up-179e891177c881d35b50f7676389fa12a06.png" width="700" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>以上为该版本<strong style="color:#27282c">部分内容</strong>，<strong style="color:#27282c"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FWI-A-231735989%2FPhpStorm-20222-EAP-2-22228899-build-Release-Notes" target="_blank">发行说明</a></strong>中提供了此版本中更改的完整列表。</p>
                                        </div>
                                      
</div>
            