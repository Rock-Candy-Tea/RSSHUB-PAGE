
---
title: 'jQuery简介及入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2643'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 00:20:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=2643'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、什么是jQuery？</h2>
<p>1、jQuery是一个JavaScript库；也可以说jQuery是JavaScript框架，他还定义了自己的语法.<br>
2、jQuery的特点</p>
<p>（1）兼容性比较强，不必考虑firefox、IE6、IE7、IE8、Safari、Opera等不同浏览器的兼容问题<br>
（2）完善的Ajax应用，使Ajax变得简单<br>
（3）DOM操作简单化<br>
（4）丰富的插件支持，强大的易扩展性; 写的更少，但做的更多。</p>
<h2 data-id="heading-1">二、jQuery的引入</h2>
<p>1.1、<code><script src=“jquery.js”></script> </code><br>
无须加入“type=text/javascript”<br>
1.2、 <code><script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"> </script></code></p>
<h2 data-id="heading-2">三、开始jQuery</h2>
<p>1、首先在head标签内导入jQuery库</p>
<p>2、jQuery的简写形式：“$”美元符号</p>
<pre><code class="copyable">例一：$("#go") 等同于 jQuery("#go")    
例二：$.post 等同于 jQuery.post    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、$()构造函数</p>
<pre><code class="copyable">（1）$()即jQuery()函数，通常被当作jQuery的“选择器函数”。      
（2）圆括号中的为选择器，用来选取HTML元素。
（3）$()函数的作用：对圆括号中选取的HTML元素自动循环遍历，然后
   组装成一个jQuery对象返回。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、jQuery对象的写法</p>
<pre><code class="copyable">区分大小写：第一个字母“j”为小写，第二个字母“Q”为大写，后面的字母都为小写.

5、为了防止文档结构还没有完全加载就运行jQuery代码，都应当将jQuery代码包含在一个$(document).ready()函数之中
例如:
$(document).ready(function()&#123;
//---- 这里添加jQuery代码 ----
 &#125;);
简化版写法:
$(function()&#123;
 //---- 这里添加jQuery代码 ----
&#125;);
这两种写法就相当于JavaScript中的window.onload=function()&#123;&#125;
同时$(document).ready(function()&#123;&#125;)可以多个使用
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6、jQuery注释<br>
注释与JavaScript写法一样分为单行注释和多行注释<br>
单行注释为 //ctrl+/<br>
多行注释为/* */ctrl+shift+/</p>
<h2 data-id="heading-3">四、window.onload与$(document).ready(function()&#123;&#125;)的区别</h2>
<p>1、执行时机</p>
<p><code>window.onload====必须在网页中所有的内容加载完毕之后才可执行(包括图片img) $(document).ready(function()&#123;&#125;)====页面当中的DOM结构绘制加载完毕即可执行，可能与DOM元素关联的并未完全加载完</code></p>
<p>2、编写个数</p>
<p><code>window.onload====不可以编写多个   $(document).ready(function()&#123;&#125;)====可以编写多个，并且都会执行</code></p>
<p>3、简化写法</p>
<p><code>window.onload 无简化写法 $(document).ready(function()&#123;&#125;)可以简化为$(function()&#123;&#125;)</code></p>
<h2 data-id="heading-4">五、JavaScript DOM对象与jQuery对象的区别</h2>
<p>JavaScript通过js相关对象方法获取的对象<br>
例如:<br>
getElementById()、getElementsByClassName、<br>
getElementsByTagName、getElementsByName</p>
<p>jQuery对象:<br>
通过jQuery包装后产生的对象<br>
如:<br>
<code>var $aObj=$(“#one”).html()  //获取id名为one 的对象的html.         等同于:          var aObj=document.getElementById(“one”).innerHTML;</code></p>
<p>注：jquery对象中无法应用DOM 对象的任何方法，反之亦然</p>
<h2 data-id="heading-5">六、jQuery对象与JavaScript对象之间的相互转换</h2>
<p>1、jQuery对象转JavaScript对象<br>
1.1、[index]方法<br>
<code>var $cr = $(“#cr”);  var cr = $cr[0];  </code></p>
<p>1.2、get[index]方法<br>
<code>var $cr = $(“#cr”);var cr = $cr.get(0)</code></p>
<p>2、JavaScript对象转jQuery对象
<code>var cr = document.getElementById(“cr”);var $cr = $(cr);\</code></p>
<h2 data-id="heading-6">七、基本语法</h2>
<p>1、基本语法：$(selector).action()</p>
<p><code>（1）$：jQuery的简写形式      （2）$()：jQuery选择器函数 （3）selector：jQuery选择器，用来选择和查找HTML元素       例如：$("#go") —— 选择所有 id="go" 的元素 （4）action()：执行的方法或操作，可以是事件或动画效果       例如：hide() —— 执行隐藏操作 例如： $("#go").hide() —— 选择所有id="go"的元素，然后执行隐藏操作；                      也就是，隐藏所有id="go"的元素</code></p>
<pre><code class="copyable">2、链式语法：$(selector).action().action().action().....
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明：被选取的元素执行完第1个action()方法之后，紧接着执行第2个<br>
action()方法，然后是第3个action()方法，依此类推......
这就是jQuery特色的链式操作。</p></div>  
</div>
            