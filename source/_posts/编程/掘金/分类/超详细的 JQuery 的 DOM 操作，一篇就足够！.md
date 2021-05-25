
---
title: '超详细的 JQuery 的 DOM 操作，一篇就足够！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8377'
author: 掘金
comments: false
date: Mon, 24 May 2021 19:27:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=8377'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>​​​摘要：今天来和大家分享有关jQuery框架中DOM操作的相关技术，又是一个堪称DOM“全家桶”系列的讲解，建议收藏关注认真学习！</p>
</blockquote>
<p>本文分享自华为云社区<a href="https://bbs.huaweicloud.com/blogs/268474?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">《【JQuery框架】超详细DOM操作看这一篇就够了！》</a>，原文作者：灰小猿 。</p>
<p>今天来和大家分享有关jQuery框架中DOM操作的相关技术，<strong>又是一个堪称DOM“全家桶”系列的讲解，建议收藏关注认真学习！</strong></p>
<p>在进行内容操作时，对于设置和获取元素的内容使用同一个函数进行操作，设置元素内容时直接在函数中传入参数即可。</p>
<h1 data-id="heading-0">1. html()</h1>
<blockquote>
<p>作用：获取/设置元素的标签体内容</p>
</blockquote>
<pre><code class="copyable">// 获取mydiv的标签体内容
var divValue = $("#mydiv").html()

// 设置mydiv的标签体内容
var divValue = $("#mydiv").html(“你好”)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">2. text()</h1>
<blockquote>
<p>作用：获取/设置元素的标签体纯文本内容</p>
</blockquote>
<pre><code class="copyable">// 获取mydiv文本内容
var divText = $("#mydiv").text()

// 设置mydiv文本内容
var divText = $("#mydiv").text(“你好”)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">3. val()</h1>
<blockquote>
<p>作用：获取/设置元素的value属性值</p>
</blockquote>
<pre><code class="copyable">// 获取myinput 的value值
var value = $("#myinput").val()

// 设置myinput 的value值
var value = $("#myinput").val(“你好”)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>关于上述代码的实际演示如下：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title></title>
<script  src="../js/jquery-3.3.1.min.js"></script>
<script>

$(function ()&#123;
// 获取myinput 的value值
var value = $("#myinput").val()
// alert(value);

// 获取mydiv的标签体内容
var divValue = $("#mydiv").html()
alert(divValue);

// 获取mydiv文本内容
var divText = $("#mydiv").text()
// alert(divText)
&#125;);
</script>

</head>
<body>
<input id="myinput" type="text" name="username" value="张三" /><br />
<div id="mydiv"><p><a href="#">标题标签</a></p></div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">二、属性操作</h1>
<h1 data-id="heading-4">（1）通用属性操作</h1>
<h1 data-id="heading-5">1. attr():</h1>
<blockquote>
<p>作用：获取/设置元素的属性</p>
</blockquote>
<pre><code class="copyable">//获取北京节点的name属性值
var bj = $("#bj").attr("name");
alert(bj);
//设置北京节点的name属性的值为dabeijing
$("#bj").attr("name", "dabeijing");
//新增北京节点的discription属性 属性值是didu
$("#bj").attr("discription", "didu");
//删除北京节点的name属性并检验name属性是否存在
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">2. removeAttr()</h1>
<blockquote>
<p>作用：删除属性</p>
</blockquote>
<pre><code class="copyable">//删除北京节点的name属性并检验name属性是否存在
$("#bj").removeAttr("name");
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">3. prop()</h1>
<blockquote>
<p>作用：获取/设置元素的属性</p>
</blockquote>
<pre><code class="copyable">//获得hobby的的选中状态
var hobby_type = $("#hobby").prop("checkbox");
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">4. removeProp()</h1>
<blockquote>
<p>作用：删除属性</p>
</blockquote>
<pre><code class="copyable">//删除hobby的CheckBox属性
var hobby_type = $("#hobby").removeProp("checkbox");
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">5.attr和prop区别</h1>
<ol>
<li>如果操作的是元素的固有属性，则建议使用prop</li>
<li>如果操作的是元素自定义的属性，则建议使用attr</li>
</ol>
<h1 data-id="heading-10">（2）对class属性操作</h1>
<h1 data-id="heading-11">1. addClass()</h1>
<blockquote>
<p>作用：添加class属性值</p>
</blockquote>
<pre><code class="copyable">//<input type="button" value=" addClass"  id="b2"/>
//给one标签增加属性
$("#b2").click(function () &#123;
   $("#one").addClass("second");
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">2. removeClass()</h1>
<blockquote>
<p>作用：删除class属性值//<input type=</p>
</blockquote>
<pre><code class="copyable">//<input type="button" value="removeClass"  id="b3"/>
//删除one标签的class属性
$("#b3").click(function () &#123;
    $("#one").removeClass("second");
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">3. toggleClass()</h1>
<blockquote>
<p>作用：切换class属性</p>
</blockquote>
<pre><code class="copyable">//<input type="button" value=" 切换样式"  id="b4"/>
//为one标签的class样式进行切换，有class属性就删除，没有就添加
$("#b4").click(function () &#123;
   $("#one").toggleClass("second");
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在这里对该函数做一个详细的介绍：</strong></p>
<p>如toggleClass("one"):</p>
<p>* 判断如果元素对象上存在class="one"，则将属性值one删除掉。 如果元素对象上不存在class="one"，则添加</p>
<h1 data-id="heading-14">4. css()</h1>
<blockquote>
<p>作用，修改元素属性</p>
</blockquote>
<pre><code class="copyable">//<input type="button" value=" 通过css()获得id为one背景颜色"  id="b5"/>
$("#b5").click(function () &#123;
   var backgroundColor = $("#one").css("backgroundColor");
   alert(backgroundColor);
&#125;);

//<input type="button" value=" 通过css()设置id为one背景颜色为绿色"  id="b6"/>
$("#b6").click(function () &#123;
   $("#one").css("backgroundColor","green")
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-15">三、CRUD操作</h1>
<h1 data-id="heading-16">1. append()</h1>
<blockquote>
<p>作用：父元素将子元素追加到末尾</p>
</blockquote>
<blockquote>
<p>样例：对象1.append(对象2): 将对象2添加到对象1元素内部，并且在末尾</p>
</blockquote>
<h1 data-id="heading-17">2. prepend()</h1>
<blockquote>
<p>作用：父元素将子元素追加到开头</p>
</blockquote>
<blockquote>
<p>样例：对象1.prepend(对象2):将对象2添加到对象1元素内部，并且在开头</p>
</blockquote>
<h1 data-id="heading-18">3. appendTo()</h1>
<blockquote>
<p>样例：对象1.appendTo(对象2):将对象1添加到对象2内部，并且在末尾</p>
</blockquote>
<h1 data-id="heading-19">4. prependTo()</h1>
<blockquote>
<p>样例：对象1.prependTo(对象2):将对象1添加到对象2内部，并且在开头</p>
</blockquote>
<h1 data-id="heading-20">5. after()</h1>
<blockquote>
<p>作用：添加元素到元素后边</p>
</blockquote>
<blockquote>
<p>样例：对象1.after(对象2)： 将对象2添加到对象1后边。对象1和对象2是兄弟关系</p>
</blockquote>
<h1 data-id="heading-21">6. before()</h1>
<blockquote>
<p>作用：添加元素到元素前边</p>
</blockquote>
<blockquote>
<p>样例：对象1.before(对象2)： 将对象2添加到对象1前边。对象1和对象2是兄弟关系</p>
</blockquote>
<h1 data-id="heading-22">7. insertAfter()</h1>
<blockquote>
<p>样例：对象1.insertAfter(对象2)：将对象1添加到对象2后边。对象1和对象2是兄弟关系</p>
</blockquote>
<h1 data-id="heading-23">8. insertBefore()</h1>
<blockquote>
<p>样例：对象1.insertBefore(对象2)： 将对象1添加到对象2前边。对象1和对象2是兄弟关系</p>
</blockquote>
<h1 data-id="heading-24">9. remove()</h1>
<blockquote>
<p>作用：移除元素</p>
</blockquote>
<blockquote>
<p>样例：对象.remove():将对象删除掉</p>
</blockquote>
<h1 data-id="heading-25">10. empty()</h1>
<blockquote>
<p>作用：清空元素的所有后代元素。</p>
</blockquote>
<blockquote>
<p>样例：对象.empty():将对象的后代元素全部清空，但是保留当前对象以及其属性节点</p>
</blockquote>
<p><strong><a href="https://bbs.huaweicloud.com/blogs?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">点击关注，第一时间了解华为云新鲜技术~</a></strong></p></div>  
</div>
            