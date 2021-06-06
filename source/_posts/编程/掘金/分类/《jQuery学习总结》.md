
---
title: '《jQuery学习总结》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7256'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 01:45:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=7256'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>jQuery</strong>是一个快速、简洁的<strong>JavaScript框架</strong>，是继Prototype之后又一个优秀的JavaScript代码库（框架）于<strong>2006年1月由John Resig</strong>发布。jQuery设计的宗旨是“write Less，Do More”，即倡导写更少的代码，做更多的事情。它<strong>封装JavaScript常用的功能代码</strong>，提供一种简便的JavaScript设计模式，<strong>优化HTML文档操作</strong>、<strong>事件处理</strong>、<strong>动画设计和Ajax交互</strong>。</p>
<hr>
<p>以下面的一坨简单的jQuery代码来对今天的<strong>jQuery如何获取元素</strong>.<strong>如何创建元素</strong>.<strong>链式操作是如何操作</strong>的进行一个简单的学习总结   <code>$  = jQuery()</code></p>
<pre><code class="copyable"><!DOCTYPE html>                       
<html>                               
 <head>
  <meta charset="utf-8">
  <title>jQuery</title>
 </head>
 <body>
  <div id="test">
  <div class="child">1</div>
  <div class="child">2</div>
  <div class="child">3</div>
 </div>
 </body>
</html>

window.$ = window.jQuery = function(selectorOrArray)&#123;
 let elements
if(typeof selectorOrArray === 'string')&#123;
     elements = document.querySelectorAll(selectorOrArray)
 &#125;else if(selectorOrArray instanceof Array)&#123;
     elements = selectorOrArray
 &#125;
 return &#123;
addClass(className)&#123;
    for(let i=0;i<elements.length;i++)&#123;
       elements[i].classList.add(className)
    &#125;
&#125;,
find(selector)&#123;
    let array = []
    for(let i=0;i<elements.length;i++)&#123;
     const x = Array.from(elements[i].querySelectorAll(selector))
     array = array.concat(x)
   &#125;
  return jQuery(array)
 &#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-0">元素获取</h5>
<pre><code class="copyable">$('#test') ：上述代码中可以通过$('#test')代码获取到id为test的元素
$('#test').find('.child').addClass('red')也可以是找到test元素里面的所有child元素，然后在child元素里添加上red。
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-1">除此之外一些非以上代码的获取</h6>
<pre><code class="copyable">$(document) //选择整个文档对象
$('div.myClass') // 选择class为myClass的div元素
$('input[name=first]') // 选择name属性等于first的input元素
$('a:first') //选择网页中第一个a元素
$('#myForm :input') // 选择表单中的input元素
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-2">jQuery设计思想之二，就是提供各种强大的过滤器，对结果集进行筛选，缩小选择结果。</h6>
<pre><code class="copyable">$('div').has('p'); // 选择包含p元素的div元素
$('div').not('.myClass'); //选择class不等于myClass的div元素
$('div').filter('.myClass'); //选择class等于myClass的div元素
$('div').first(); //选择第1个div元素
$('div').eq(5); //选择第6个div元素
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-3">还可以移动到其他相关的元素上</h6>
<pre><code class="copyable">$('div').next('p'); //选择div元素后面的第一个p元素
$('div').parent(); //选择div元素的父元素
$('div').closest('form'); //选择离div最近的那个form父元素
$('div').children(); //选择div的所有子元素
$('div').siblings(); //选择div的同级元素
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h5 data-id="heading-4">jQuery的链式操作</h5>
<p>jQuery设计思想之三，就是最终选中网页元素以后，可以对它进行一系列操作，并且所有操作可以连接在一起，<strong>以链条的形式写出来</strong>。</p>
<pre><code class="copyable">$('#test').addClass('glue').addClass('red')通过此代码可以在最上面那坨代码中找到test元素，在上面添加上glue，然后在后面再此添加上red。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是jQuery最令人称道、最方便的特点。它的原理在于每一步的jQuery操作，返回的都是一个jQuery对象，所以不同操作可以连在一起。</p>
<hr>
<h5 data-id="heading-5">创建元素</h5>
<h6 data-id="heading-6">可以直接把需要创建的新元素添加到jQuery的构造函数里</h6>
<pre><code class="copyable">$('<p>Hello</p>');
$('<li class="new">new list item</li>');
$('ul').append('<li>list item</li>');
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h5 data-id="heading-7">如何移动元素</h5>
<p>jQuery设计思想之五，就是提供两组方法，来操作元素在网页中的位置移动。一组方法是直接移动该元素，另一组方法是移动其他元素，使得目标元素达到我们想要的位置。</p>
<p>假定我们选中了一个div元素，需要把它移动到p元素后面。</p>
<p>第一种方法是使用<code>.insertAfter()</code>，把div元素移动p元素后面：</p>
<pre><code class="copyable">$('div').insertAfter($('p'));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二种方法是使用<code>.after()</code>，把p元素加到div元素前面：</p>
<pre><code class="copyable">$('p').after($('div'));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>表面上看，这两种方法的效果是一样的，唯一的不同似乎只是操作视角的不同。但是实际上，它们有一个重大差别，那就是<strong>返回的元素不一样</strong>。<strong>第一种方法返回div元素</strong>，<strong>第二种方法返回p元素</strong>。
还有其他这种操作方法</p>
<pre><code class="copyable">.insertAfter()和.after()：在现存元素的外部，从后面插入元素
.insertBefore()和.before()：在现存元素的外部，从前面插入元素
.appendTo()和.append()：在现存元素的内部，从后面插入元素
.prependTo()和.prepend()：在现存元素的内部，从前面插入元素
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h5 data-id="heading-8">修改元素属性</h5>
<p>操作网页元素，最常见的需求是取得它们的值，或者对它们进行赋值。</p>
<p>jQuery设计思想之四，就是使用同一个函数，来完成取值（getter）和赋值（setter），即"取值器"与"赋值器"合一。到底是取值还是赋值，由函数的参数决定。</p>
<pre><code class="copyable">$('h1').html(); //html()没有参数，表示取出h1的值
$('h1').html('Hello'); //html()有参数Hello，表示对h1进行赋值
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他常见取值和赋值函数（读，写）</p>
<h6 data-id="heading-9">div大部分时候对应了多个div元素</h6>
<pre><code class="copyable">$div.html() 读写html内容
$div.text() 读写text内容
$div.attr('title',?) 读写某个属性的值
$div.css(&#123;color:'red'&#125;)读写style
$div.addClass('blue')
$div.on('clicl',fn)
$div.off('click',fn)
$div.width() 读写某个元素的宽度
$div.height() 读写某个元素的高度
$div.val() 读某个表单元素的值
<span class="copy-code-btn">复制代码</span></code></pre>
<p>attr() 方法设置或返回被选元素的属性和值。</p>
<p>当该方法用于返回属性值，则返回第一个匹配元素的值。</p>
<p>当该方法用于设置属性值，则为匹配元素设置一个或多个属性/值对。</p>
<p>返回属性的值：</p>
<pre><code class="copyable">$(selector).attr(attribute)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置属性和值：</p>
<pre><code class="copyable">$(selector).attr(attribute,value)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用函数设置属性和值：</p>
<pre><code class="copyable">$(selector).attr(attribute,function(index,currentvalue))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置多个属性和值：</p>
<pre><code class="copyable">$(selector).attr(&#123;attribute:value, attribute:value,...&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h5 data-id="heading-10">一些常用的工具方法</h5>
<pre><code class="copyable">$.trim() 去除字符串两端的空格。
$.each() 遍历一个数组或对象。
$.inArray() 返回一个值在数组中的索引位置。如果该值不在数组中，则返回-1。
$.grep() 返回数组中符合某种标准的元素。
$.extend() 将多个对象，合并到第一个对象。
$.makeArray() 将对象转化为数组。
$.type() 判断对象的类别（函数对象、日期对象、数组对象、正则对象等等）。
$.isArray() 判断某个参数是否为数组。
$.isEmptyObject() 判断某个对象是否为空（不含有任何属性）。
$.isFunction() 判断某个参数是否为函数。
$.isPlainObject() 判断某个参数是否为用"&#123;&#125;"或"new Object"建立的对象。
$.support() 判断浏览器是否支持某个特性
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h6 data-id="heading-11">日常学习记录，有错误请指正，本文借鉴了<a href="http://www.ruanyifeng.com/blog/2011/07/jquery_fundamentals.html" target="_blank" rel="nofollow noopener noreferrer">阮一峰jQuery设计思想</a></h6></div>  
</div>
            