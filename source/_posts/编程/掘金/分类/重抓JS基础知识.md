
---
title: '重抓JS基础知识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=0'
author: 掘金
comments: false
date: Mon, 03 May 2021 19:49:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=0'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">初步了解JaveSctript</h1>
<ul>
<li>Web标准的构成</li>
</ul>

























<table><thead><tr><th>标题</th><th>内容</th><th>说明</th></tr></thead><tbody><tr><td>结构</td><td>HTML</td><td>网页元素的结构和内容</td></tr><tr><td>表现</td><td>CSS</td><td>网页元素的外观和位置，包括版式和颜色、大小</td></tr><tr><td>行为</td><td>js</td><td>网页模型的定义和交互</td></tr></tbody></table>
<ul>
<li>Javascript是一种编程语言，可以用来创建动态更新的内容，控制多媒体，制作图像动画等等实现人机交互效果，简单来说，可以通过简短的代码来实现神奇的功能。</li>
<li>JavaScript的书写方式，<strong>规范是script标签写在body上面</strong>
<ul>
<li>行内JavaScript</li>
<li>内部JavaScript</li>
<li>外部JavaScript</li>
</ul>
</li>
<li>结束符
<ul>
<li>代表语句的结束，用英文的<code>;</code>表示。</li>
<li>可写可不写。</li>
<li>换行符（回车） 会被识别成结束符，因此在实际开发中有许多人主张书写JavaScript代码时，省略结束符。</li>
<li>但是为了统一风格，要写结束符就每句都写，要么就每句都不写。</li>
</ul>
</li>
<li>JavaScript输入输出语句
<ul>
<li>输出和出入可以理解为人和计算机的交互，用户通过键盘、鼠标等向计算机输入信息，计算机处理后再展示给用户，这便是一个输入和输出的过程。</li>
<li>输出语句
<ul>
<li><code>ducoment.write("要输出的内容")</code>
<ul>
<li>向body内输出内容</li>
<li>如果输出的内容是标签，也会被解析成网页元素</li>
</ul>
</li>
<li><code>alert(要输出的内容)</code>
<ul>
<li>页面弹出框，输出对应的内容</li>
</ul>
</li>
<li>console.log(要输出的内容)
<ul>
<li>控制台输出对应的内容，通常帮助我们进行调试。</li>
</ul>
</li>
</ul>
</li>
<li>输入语句
<ul>
<li><code>prompt("请输入你的姓名")</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<h1 data-id="heading-1">变量</h1>
<ul>
<li>目标：理解变量是计算机存储数据的<strong>容器</strong>，掌握变量的<strong>声明方式</strong></li>
</ul>
<h2 data-id="heading-2">变量是什么</h2>
<ul>
<li>白话：变量就是一个盒子。</li>
<li>通俗：变量就是计算机存储数据的容器，它可以让计算机有记忆。</li>
</ul>
<h2 data-id="heading-3">变量的基本使用</h2>
<h3 data-id="heading-4">变量的声明方式</h3>
<ul>
<li>想要使用变量，首先要创建变量（专业的说法叫声明变量）</li>
<li>声明变量有两部分构成：声明关键字、变量名（标识）</li>
<li>let即为关键字，let(允许、许可、让、要)，所谓关键字就是系统提供的专门用来声明（定义）变量的词语</li>
<li>let语法
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//let声明一个变量,例如</span>
<span class="hljs-keyword">let</span> age
<span class="hljs-comment">//let声明变量并赋值</span>
<span class="hljs-keyword">let</span> age = <span class="hljs-number">18</span>
<span class="hljs-comment">//let同时声明多个变量并同时声明</span>
<span class="hljs-keyword">let</span> age = <span class="hljs-number">18</span>， name = <span class="hljs-string">"张三"</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>使用let时注意事项
<ul>
<li>允许声明和赋值同时进行。</li>
<li>不允许重复声明</li>
<li>JavaScript中内置的一些关键字不能被当作变量名</li>
<li>允许同时声明多个变量并赋值</li>
</ul>
</li>
<li>变量赋值
<ul>
<li>定义一个变量后，你就能够初始化它（赋值），在变量名之后加上一个=号，然后跟数值</li>
<li>语法</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> age
age = <span class="hljs-number">18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>更新变量
<ul>
<li>变量赋值后，还可以给它一个不同的值来更新它。</li>
<li>语法</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> age
age = <span class="hljs-number">18</span>
age = <span class="hljs-number">19</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注意
<ul>
<li>let能重新赋值但是不能被重复被定义（声明）</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-5">变量的本质</h2>
<ul>
<li>内存：计算机中存储数据的地方，相当于一个空间。</li>
<li>变量：是程序在内存中申请的一块拿来存放数据的小空间。</li>
</ul>
<h2 data-id="heading-6">变量的命名规则与规范</h2>
<h3 data-id="heading-7">规则：必须遵守，不遵守会爆错</h3>
<ul>
<li>不能使用关键字。
<ul>
<li>关键字：有特殊含义的字符，JavaScript内置的一些英语词汇。例如：let var if for等等。</li>
</ul>
</li>
<li>只能用下划线、字母、数字、$组成，且数字不能开头。</li>
<li>字母严格区分大小写，如Age和age是不同的变量。</li>
</ul>
<h3 data-id="heading-8">规范：建议，不遵守不会报错，但是不符合业内通识</h3>
<ul>
<li>起名要有意义。</li>
<li>遵守驼峰式命名
<ul>
<li>第一个单词的首字符小写，后面每个单词首字母大写。例如userName</li>
</ul>
</li>
</ul>
<h1 data-id="heading-9">数据类型</h1>
<ul>
<li>计算机世界完事成物都是数据。</li>
<li>计算机程序可以处理大量的数据，为了方便数据的管理（用途不同），将数据分成了不同的类型</li>
</ul>



























































<table><thead><tr><th>数据类型</th><th>作用</th><th>表示形式</th><th>例</th></tr></thead><tbody><tr><td>String（字符串）</td><td>表示文字内容</td><td>英文的单引号或者双引号包起来</td><td>'hello'、“world”</td></tr><tr><td>Number（数字）</td><td>表示数字内容</td><td>直接写数字</td><td>10，20</td></tr><tr><td>Boolean（布尔）</td><td>表示对立的两种状态，真或者假，对或者错等等</td><td>true 和 false</td><td>ture、false</td></tr><tr><td>undefined（未定义）</td><td>表示未定义</td><td>undefined</td><td>undefined</td></tr><tr><td>Object（对象）</td><td>表示普通对象</td><td>用大括号包起来的键值对</td><td>&#123;name:nihao&#125;</td></tr><tr><td>Null（空值）</td><td>表示空对象</td><td>null</td><td>null</td></tr><tr><td>Array（数组）</td><td>表示数组对象</td><td>用中括号包起来</td><td>[1,2,3]</td></tr><tr><td>Regex（正则）</td><td>表述正则对象</td><td>用反斜杠包起来</td><td>/^[+-]?/</td></tr></tbody></table>
<h2 data-id="heading-10">数字类型（Number）</h2>
<ul>
<li>即我们数学中学习到的数字，可以是整数、小数、正数、负数、NaN（非数字）。</li>
</ul>
<h3 data-id="heading-11">NaN</h3>
<ul>
<li>NaN:not a number;意思是不是一个数，但是它属于数字类型。</li>
<li>NaN和任何一个值都不相等，包括自己。</li>
</ul>
<h3 data-id="heading-12">isNaN()</h3>
<ul>
<li>检测一个值是否为有效数字，如果不是有效数字返回true，如果是有效数字返回false。</li>
<li>再使用isNaN这个方法时，首先会检测检测值是否为数字，如果不是，它会进行隐式转换，用<code>Number()</code>这个方法将值先转为数字类型然后在进行检测。</li>
</ul>
<h3 data-id="heading-13">Number()转化</h3>
<ul>
<li>将字符串转为数字，只要字符串中包含任意一个非有效数字字符结果都是<code>NAN</code>，空字符串会返回<strong>0</strong></li>
<li>把引用数据类型转为数字，是先把他基于<code>toString()</code>方法转换为字符串</li>
</ul>
<h3 data-id="heading-14">pareseInt()和parseFloat()</h3>
<ul>
<li>parseInt()将其他数据转为数字整数</li>
<li>parseFloat()将其他数据转为数字，取到小数点。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-string">'12px'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">parseInt</span>(a))<span class="hljs-comment">//12</span>
<span class="hljs-keyword">let</span> ary = [<span class="hljs-number">13</span>,<span class="hljs-number">14</span>]
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">parseInt</span>(ary))<span class="hljs-comment">//13</span>
<span class="hljs-comment">// 它会将其他数据类型先转化为字符串类型，ary.toString()后返回值为'13,14'。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">字符串类型（String）</h2>
<ul>
<li>通过单引号<code>''</code>、双引号<code>""</code>或者反引号``包裹的数据都叫字符串，单引号和双引号本质上没有区别，推荐使用单引号。</li>
<li>一个字符串是由零到多个字符组成，每一个字符都有自己位置的索引，由一个length存储字符串的长度。</li>
<li>注意
<ul>
<li>无论是单引号还是双引号都必须是成对的使用</li>
<li>单引号/双引号都可以互相嵌套，但是不能嵌套自己，外双内单或者外单内双都可以。</li>
<li>必要时可以使用转义符<code>\</code>输出单引号或者双引号</li>
</ul>
</li>
</ul>
<h3 data-id="heading-16">字符串拼接</h3>
<h4 data-id="heading-17">ES6新增的模板字符串</h4>
<ul>
<li><code>$&#123;&#125;</code>中存放的是js表达式，可以是变量以及变量运算，三元运算符等等。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> x = <span class="hljs-number">15</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;x&#125;</span>px`</span>)<span class="hljs-comment">//15px</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-number">3</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;x*b&#125;</span>px`</span>)<span class="hljs-comment">//45px</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">利用<code>+</code>拼接</h4>
<ul>
<li><code>+</code>号左右两边有一边出现字符串，结果就是字符串拼接</li>
<li><code>+</code>号左右两边有一个边出现对象（目的是把对象转为数字，进行数学运算）
<ul>
<li>系统首先会获取对象的<code>[Synbol.toPrimitive]</code>属性值</li>
<li>如果没有这个属性，其次获取他的<code>valueOf()</code>；原始值都是基本数据类型。</li>
<li>如果还没有原始值，最后就会把它转为字符串toString，最后就变成字符串拼接了。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">46</span>
<span class="hljs-built_in">console</span>.log(a+<span class="hljs-string">'岁'</span>)<span class="hljs-comment">//46岁</span>

<span class="hljs-keyword">let</span> ary = [<span class="hljs-number">12</span>,<span class="hljs-number">13</span>]
ary[<span class="hljs-built_in">Symbol</span>.toPrimitive]<span class="hljs-comment">//undefined</span>
ary.valueOf()<span class="hljs-comment">//[12,13] //这个不是他的原始值，所有的原始值都是基本数据类型</span>

<span class="hljs-keyword">let</span> num = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">10</span>)<span class="hljs-comment">//这是一个对象</span>
<span class="hljs-built_in">console</span>.log(num[<span class="hljs-built_in">Symbol</span>.toPrimitive],num.valueOf) <span class="hljs-comment">//undefined  10</span>
<span class="hljs-built_in">console</span>.log(num+<span class="hljs-number">10</span>)  <span class="hljs-comment">//20</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>+</code>号只出现一边，这样这一边即使是字符串/对象,也是数字运算</li>
</ul>
<h3 data-id="heading-19">字符串的方法</h3>
<h4 data-id="heading-20">获取字符串中的字符</h4>
<ul>
<li>利用变量<code>[]</code>加索引获取</li>
<li>利用<code>charAt()</code>方法</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'fhcsj'</span>
<span class="hljs-built_in">console</span>.log(str[<span class="hljs-number">2</span>])<span class="hljs-comment">//c</span>
<span class="hljs-built_in">console</span>.log(str[str.legnth-<span class="hljs-number">1</span>])<span class="hljs-comment">//j</span>

<span class="hljs-built_in">console</span>.log(str.charAt(<span class="hljs-number">2</span>))<span class="hljs-comment">//c</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">把其他数据类型转化为字符串类型</h4>
<ul>
<li>利用<code>变量.toString()</code>方法</li>
<li>利用<code>String(变量)</code></li>
<li>注意：
<ul>
<li>数组转字符转，返回值是将数组中的每一项用逗号分隔</li>
<li>对于普通对象转为字符串，不论对象中包含的值是什么，最终的返回值都是<code>"[object Object]"</code></li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> num = <span class="hljs-number">15</span>,
ary = [<span class="hljs-number">11</span>,<span class="hljs-number">13</span>]
num.toString()<span class="hljs-comment">//'15'</span>
<span class="hljs-built_in">String</span>(num)<span class="hljs-comment">//'15'</span>

ary.toString()<span class="hljs-comment">//'11,13'</span>

<span class="hljs-keyword">let</span> obj = &#123;&#125;
obj.toString()<span class="hljs-comment">//"[object Object]"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22"><code>charCodeAt()</code></h4>
<ul>
<li>返回字符串对应索引的编码</li>
</ul>
<h4 data-id="heading-23"><code>substr(start,end)</code></h4>
<ul>
<li>字符串截取</li>
</ul>
<h4 data-id="heading-24"><code>slice(start,end)</code></h4>
<ul>
<li>返回新的字符串，截取从start索引到end，但是不包括end索引。</li>
</ul>
<h4 data-id="heading-25"><code>split(separator,howmany)</code></h4>
<ul>
<li>利用指定的separator（必须）参数，将字符串分割成数组，howmany（可选）定义数组的长度，如果没写howmany参数，则对数组的长度没有限制。
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'fdkfhkds'</span>
<span class="hljs-built_in">console</span>.log(str.split(<span class="hljs-string">'k'</span>))<span class="hljs-comment">//[fd,fh,ds]</span>
<span class="hljs-built_in">console</span>.log(str.split(<span class="hljs-string">'k'</span>,<span class="hljs-number">2</span>))<span class="hljs-comment">//[fd,fh]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-26"><code>replace(regexp/substr,replacement)</code></h4>
<ul>
<li>用（replacement字符）替换 字符串中的（substr字符）或者替换一个与正则匹配的字符。
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'fsfsdhfsdfs'</span>
<span class="hljs-built_in">console</span>.log(str.replace(<span class="hljs-string">'fs'</span>,<span class="hljs-string">'i'</span>))<span class="hljs-comment">//ifsdhfsdfs,它只会替换第一个</span>

<span class="hljs-built_in">console</span>.log(str.replace(<span class="hljs-regexp">/fs/</span>),i)<span class="hljs-comment">//ifsdhfsdfs,这样写它也只会替换第一个</span>

<span class="hljs-built_in">console</span>.log(str.replace(<span class="hljs-regexp">/fs/g</span>),i)<span class="hljs-comment">//iidhidi,这样写是替换字符串中所有的fs</span>

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-27"><code>indexOf(searchValue,fromIndex)/lastIndexOf(searchValue,fromIndex)</code></h4>
<ul>
<li><code>indexOf()</code>
<ul>
<li>返回规定检索的字符串值（searchValue，必写）的索引，fromIndex(规定从哪个索引值开始检索,可选)</li>
<li>如果在字符串中没有检索到规定的字符串值，则会返回-1。</li>
</ul>
</li>
<li><code>lastIndexOf()</code>
<ul>
<li>返回规定检索的字符串值从右往左第一次出现的索引，fromIndex规定从第几个字符开始（其中这个字符是从后面往前数的）。注意：它的0索引还是最左边的第一个字符。</li>
<li>如果字符串中检索不到规定的字符值则返回-1</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'fsdhkhds'</span>
<span class="hljs-built_in">console</span>.log(str.indexOf(<span class="hljs-string">'d'</span>))<span class="hljs-comment">//2</span>
<span class="hljs-built_in">console</span>.log(str.indexOf(<span class="hljs-string">'d'</span>,<span class="hljs-number">3</span>))<span class="hljs-comment">//6</span>

<span class="hljs-built_in">console</span>.log(str.lastIndexOf(<span class="hljs-string">'d'</span>))<span class="hljs-comment">//6</span>
<span class="hljs-built_in">console</span>.log(str.lastIndexOf(<span class="hljs-string">'d'</span>,<span class="hljs-number">2</span>))<span class="hljs-comment">//2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28"><code>includes(searchValue,fromIndex)</code></h4>
<ul>
<li>判断字符串中是否包含规定的字符值（searchValue），从规定的索引开始（fromIndex）,返回值为true或者false</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'fdsds'</span>
<span class="hljs-built_in">console</span>.log(str.includes(<span class="hljs-string">'a'</span>))<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(str.includes(<span class="hljs-string">'s'</span>))<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">布尔类型（Boolean）</h2>
<ul>
<li>表示肯定或者否定时，在计算机中对应的就是布尔类型，它有两个固定的值true或者false。</li>
<li>把其他数据类型转化为布尔类型的两种方式
<ul>
<li><code>Boolean(value)</code></li>
<li><code>!!value</code></li>
</ul>
</li>
<li>注：只有0、NaN、空字符串、undefined变为布尔类型的值为false，其他的都是true。</li>
</ul>
<h2 data-id="heading-30">未定义类型（undefined）</h2>
<ul>
<li>未定义类型是一种比较特殊的类型，只有一个值undefined。</li>
<li>什么情况出现未定义类型？
<ul>
<li>只声明变量没有赋值的情况下，变量的默认值为undefined，一般很少为某个变量赋值undefined。</li>
</ul>
</li>
</ul>
<h2 data-id="heading-31">Symbol（表示唯一值，属于基本数据类型）</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-built_in">Symbol</span>(<span class="hljs-number">0</span>)
<span class="hljs-keyword">let</span> b = <span class="hljs-built_in">Symbol</span>(<span class="hljs-number">0</span>)
<span class="hljs-built_in">console</span>.log(a==b)<span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-32">对象数据类型</h2>
<h3 data-id="heading-33">普通对象</h3>
<ul>
<li>用<code>&#123;&#125;</code>包着键值对表示，类数组、实例、原型对象......</li>
</ul>
<h3 data-id="heading-34">数组对象</h3>
<ul>
<li>用<code>[]</code>包着表示</li>
</ul>
<h3 data-id="heading-35">正则对象</h3>
<ul>
<li>用<code>//</code>包着表示</li>
</ul>
<h3 data-id="heading-36">日期对象</h3>
<h2 data-id="heading-37">函数Function</h2>
<ul>
<li>函数：被设计为执行特定任务的代码块</li>
<li>说明：函数可以把具有相同或者类似逻辑的代码块包裹起来，通过函数调用执行这些代码逻辑，这么做的优势是有利于精简代码，方便复用。</li>
<li>语法
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> 函数名(<span class="hljs-params"></span>) </span>&#123;
    函数体
&#125;
<span class="hljs-comment">//函数调用,函数体内的代码逻辑会被执行</span>
函数名()
<span class="hljs-comment">// 可重复调用，次数不限。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>函数的命名规范
<ul>
<li>和变量命名基本一致</li>
<li>尽量使用驼峰式命名</li>
<li>前缀一般为动词</li>
<li>命名建议：常用动词约定。</li>
</ul>
</li>
</ul>
</li>
</ul>

































<table><thead><tr><th>常用的动词</th><th>含义</th></tr></thead><tbody><tr><td>can</td><td>判断是否可执行某个动作</td></tr><tr><td>has</td><td>判断是否含义某个值</td></tr><tr><td>is</td><td>判断是否为某个值</td></tr><tr><td>get</td><td>获取某个值</td></tr><tr><td>set</td><td>设置某个值</td></tr><tr><td>load</td><td>加载某些数据</td></tr></tbody></table>
<h1 data-id="heading-38">检测数据类型</h1>
<h2 data-id="heading-39">typeof</h2>
<ul>
<li>语法<code>let age = 18;console.log(type age)</code></li>
<li>注意
<ul>
<li>typeof能能检测基本数据类型。</li>
<li><code>typeof undefined</code>的返回值是undefined。</li>
<li><code>type null</code>的返回值是一个object。</li>
</ul>
</li>
</ul>
<h1 data-id="heading-40">JS算数运算符</h1>
<ul>
<li>数学运算符也叫运算符，主要包括假、减、乘、除、取余（求模）。</li>
</ul>





























<table><thead><tr><th>描述</th><th>符号</th></tr></thead><tbody><tr><td>求和</td><td>+</td></tr><tr><td>求差</td><td>-</td></tr><tr><td>求积</td><td>*</td></tr><tr><td>求商</td><td>/</td></tr><tr><td>取余数（求模）</td><td>%</td></tr></tbody></table>
<ul>
<li>
<ul>
<li>运算符比较特殊
<ul>
<li>+运算符在数字型中是求和运算</li>
<li>+运算符在字符串型中是拼接。</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-41">数据类型转换</h2>
<h3 data-id="heading-42">隐式转换</h3>
<ul>
<li>某些运算符被执行时，系统内部自动将数据类型进行转换，这种类型称为隐式转换。</li>
<li>规则
<ul>
<li>+号两边只要有一个是字符串类型，就会自动把另一个转为字符串。</li>
<li>除了+号以外的所有算术运算符都会把数据转成数值类型。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-43">显式转换</h3>
<ul>
<li>编写程序时过度依靠系统内部的隐式转换是不严谨的，最好是通过显式转换比较好。</li>
<li>Number(数据)
<ul>
<li>转成数字类型</li>
<li>如果字符串内容里有非数字，转换失败时结果为NaN(Not a Number)即不是一个数字。</li>
<li>NaN也是number类型的数据，代表非数字</li>
</ul>
</li>
<li>Boolean(数据)
<ul>
<li>转成布尔类型</li>
<li>0、空字符串、NaN、undefined、null转成false，其他的都是true。</li>
</ul>
</li>
<li>变量.toString()</li>
</ul>
<h1 data-id="heading-44">ES6知识点</h1>
<h2 data-id="heading-45">解构赋值</h2>
<ul>
<li>ES6中的解构赋值，主要是针对对象和数组，左侧定义和右侧值类似的结构，这样声明几个变量，快速获取到每一部分的信息。</li>
</ul>
<h3 data-id="heading-46">数组结构赋值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]
<span class="hljs-keyword">let</span> [x, y] = arr
<span class="hljs-built_in">console</span>.log(x, y)<span class="hljs-comment">//1, 2</span>

<span class="hljs-comment">//如果在下面接着用x，y变量结构赋值，则会报错，说x，y已存在</span>
<span class="hljs-keyword">let</span>[y,...x] = arr<span class="hljs-comment">//报错</span>

<span class="hljs-comment">//...代表剩余运算符，意思是剩下的数组都拿到并放到b中</span>
<span class="hljs-keyword">let</span> [a,...b] = arr
<span class="hljs-built_in">console</span>.log(a, b)<span class="hljs-comment">//1, [2, 3, 4]</span>

<span class="hljs-comment">//逗号代表前面的每一项</span>
<span class="hljs-keyword">let</span>[, , , x, y] = arr
<span class="hljs-built_in">console</span>.log(x, y) <span class="hljs-comment">// 40 undefined</span>

<span class="hljs-comment">//也可以给结构赋值的变量赋予一个默认值，如果没有值就等于默认值</span>
<span class="hljs-keyword">let</span> [, , , , b = <span class="hljs-number">0</span>] = arr
<span class="hljs-built_in">console</span>.log(b)<span class="hljs-comment">//0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-47">对象的解构赋值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//默认情况下声明的"变量"需要和"属性名一致"，这样对象才可以获取到指定成员的值</span>
<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'珠峰培训'</span>,
    <span class="hljs-attr">age</span>:<span class="hljs-number">11</span>,
    <span class="hljs-attr">teacher</span>:<span class="hljs-string">'fc'</span>,
    <span class="hljs-number">0</span>:<span class="hljs-number">100</span>
&#125;
<span class="hljs-keyword">let</span> &#123;name,age&#125; = obj
<span class="hljs-built_in">console</span>.log(name, age) <span class="hljs-comment">// '珠峰培训' 11</span>

<span class="hljs-comment">//声明一个x变量，并将obj.name 赋值给x</span>
<span class="hljs-keyword">let</span> &#123;<span class="hljs-attr">name</span>: x&#125; = obj

<span class="hljs-comment">//解构赋值时，可以给变量设置默认值</span>
<span class="hljs-keyword">let</span> &#123; x = <span class="hljs-number">0</span> &#125; = obj
<span class="hljs-comment">//如果不存在这个属性值，则给赋值默认值0</span>
<span class="hljs-built_in">console</span>.log(x)<span class="hljs-comment">//0</span>

<span class="hljs-comment">//对与数字属性名，我们则重新命名一个新的变量接收值即可</span>
<span class="hljs-comment">//如果直接写会报错，下面两种方式都会报错</span>
<span class="hljs-keyword">let</span> &#123;<span class="hljs-number">0</span>&#125; = obj
<span class="hljs-keyword">let</span> &#123;[<span class="hljs-number">0</span>]&#125; = obj
<span class="hljs-comment">//正确写法</span>
<span class="hljs-keyword">let</span>&#123;<span class="hljs-number">0</span>: x&#125; = obj
<span class="hljs-built_in">console</span>.log(x)<span class="hljs-comment">//100</span>

<span class="hljs-comment">//快速获取网站的域名和网址</span>
<span class="hljs-keyword">let</span> &#123;<span class="hljs-attr">hostname</span>:domain, <span class="hljs-attr">pathname</span>:path&#125; = location;

<span class="hljs-comment">//数组结构赋值和对象结构赋值的合并使用</span>
<span class="hljs-keyword">let</span> ary  = [<span class="hljs-number">100</span>,<span class="hljs-string">'你好'</span>,&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'hello'</span>,<span class="hljs-attr">score</span>:[<span class="hljs-number">12</span>, <span class="hljs-number">13</span>]&#125;]
<span class="hljs-keyword">let</span> [, y, &#123;<span class="hljs-attr">score</span>:[, math]&#125;]
<span class="hljs-built_in">console</span>.log(y,math)<span class="hljs-comment">//'你好',13</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            