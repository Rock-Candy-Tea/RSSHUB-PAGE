
---
title: 'jQuery用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1700'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 03:25:53 GMT
thumbnail: 'https://picsum.photos/400/300?random=1700'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>jQuery的基本设计思想和主要用法，就是"选择某个网页元素，然后对其进行某种操作"。</p>
<h2 data-id="heading-0">如何使用jQuery</h2>
<p>将一个选择表达式放入jQuery构造函数</p>
<pre><code class="copyable">　$(document) //选择整个文档对象

　$('#myId') //选择ID为myId的网页元素

　$('div.myClass') // 选择class为myClass的div元素

　$('input[name=first]') // 选择name属性等于first的input元素
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">jQuery改变结果集</h2>
<p>根据结果集进行进一步筛选是jQuery的第二个设计思想</p>
<pre><code class="copyable">　$('div').has('p'); // 选择包含p元素的div元素

　$('div').not('.myClass'); //选择class不等于myClass的div元素

　$('div').filter('.myClass'); //选择class等于myClass的div元素

　$('div').first(); //选择第1个div元素

　$('div').eq(5); //选择第6个div元素
<span class="copy-code-btn">复制代码</span></code></pre>
<p>jQuery还提供了根据结果集移动或选择到附近元素的方法</p>
<pre><code class="copyable">　$('div').next('p'); //选择div元素后面的第一个p元素

　$('div').parent(); //选择div元素的父元素

　$('div').closest('form'); //选择离div最近的那个form父元素

　$('div').children(); //选择div的所有子元素

　$('div').siblings(); //选择div的同级元素
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">链式操作</h2>
<p>它的原理在于每一步的jQuery操作，返回的都是一个jQuery对象，所以不同操作可以连在一起。</p>
<pre><code class="copyable">$('div').find('h3').eq(2).html('Hello');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>jQuery还提供了.end()方法，使得结果集可以后退一步：</p>
<pre><code class="copyable">　　$('div')

　　　.find('h3')

　　　.eq(2)

　　　.html('Hello')

　　　.end() //退回到选中所有的h3元素的那一步

　　　.eq(0) //选中第一个h3元素

　　　.html('World'); //将它的内容改为World
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">元素的取值和赋值</h2>
<p>使用同一个函数，来完成取值和赋值，到底是取值还是赋值，由函数的参数决定。</p>
<pre><code class="copyable">　　$('h1').html(); //html()没有参数，表示取出h1的值

　　$('h1').html('Hello'); //html()有参数Hello，表示对h1进行赋值
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">元素的移动</h2>
<p>四种方法</p>
<pre><code class="copyable">　　.insertAfter()和.after()：在现存元素的外部，从后面插入元素

　　.insertBefore()和.before()：在现存元素的外部，从前面插入元素

　　.appendTo()和.append()：在现存元素的内部，从后面插入元素

　　.prependTo()和.prepend()：在现存元素的内部，从前面插入元素
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">元素的复制删除和创建</h2>
<p>复制元素使用.clone()<br>
删除元素：.remove()和.detach()<br>
清空元素内容但不删除元素：.empty()
创建新元素，把新元素直接传入jQuery的构造函数：</p>
<pre><code class="copyable">　　$('<p>Hello</p>');

　　$('<li class="new">new list item</li>');

　　$('ul').append('<li>list item</li>');
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            