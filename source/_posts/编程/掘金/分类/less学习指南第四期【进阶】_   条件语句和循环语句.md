
---
title: 'less学习指南第四期【进阶】_   条件语句和循环语句'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/378098806c614752a7504e8f15a36b08~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 07:27:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/378098806c614752a7504e8f15a36b08~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<p>LESS是一个CSS预处理器，它在 CSS 的语法基础之上，引入了变量，Mixin（混入），运算以及函数等功能，大大简化了 CSS 的编写，并且降低了 CSS 的维护成本。这个系列主要就是学习并且巩固 Less 的基础知识，并且掌握一些更加高级的用法，用以提高开发效率。</p>
<p><strong>前期回顾</strong></p>
<p><a href="https://juejin.cn/post/6992236237922762759" target="_blank" title="https://juejin.cn/post/6992236237922762759">less学习指南第一期 | 嵌套和变量</a><br>
<a href="https://juejin.cn/post/6992615241037119525" target="_blank" title="https://juejin.cn/post/6992615241037119525">less学习指南第二期 | 运算和内置函数</a><br>
<a href="https://juejin.cn/post/6993332511149391908" target="_blank" title="https://juejin.cn/post/6993332511149391908">less学习指南第三期【重要】 | 混合和继承</a><br></p>
<h1 data-id="heading-0">条件表达式</h1>
<br>
<h2 data-id="heading-1">when关键字(if)（v1.5.0）</h2>
<p>条件表达式：就是我们在less中使用【比较运算符】或者【表达式的判断】来输入我们的值，根据不同的条件来输出不同的值。</p>
<p><code>用来模拟if</code></p>
<h3 data-id="heading-2">使用比较运算符</h3>
<p>比较运算符（共5种）：</p>
<ul>
<li>大于<code>> </code></li>
<li>小于<code>< </code></li>
<li>等于<code>=</code></li>
<li>大于等于<code>>=</code></li>
<li>小于等于<code>=<</code></li>
</ul>
<blockquote>
<p>注：（=）可用来比较【数字】，【字符串】、【标识符】等；其他的只能和【数字】一起使用；</p>
</blockquote>
<p><strong>示例：</strong></p>
<p>假如有这样一个需求：需要给标题设置不同颜色，要求主标题统一【黑色】、副标题统一【灰色】，已知主标题字号至少为20px；</p>
<p><code>代码实现</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/378098806c614752a7504e8f15a36b08~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807184337323" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">使用检查函数</h3>
<p><code>1）类型检查函数</code></p>
<p>可以基于值得类型来匹配函数</p>
<p>基本的类型检查函数有 <code>Iscolor(是否为颜色值) Isnumber(是否为数字) isstring(是否为字符) iskeyword(是否为关键字) isurl(是否为url)</code></p>
<blockquote>
<p>这些检查函数是👉<a href="https://link.juejin.cn/?target=https%3A%2F%2Fless.bootcss.com%2Ffunctions%2F%23type-functions" target="_blank" rel="nofollow noopener noreferrer" title="https://less.bootcss.com/functions/#type-functions" ref="nofollow noopener noreferrer">less的内置函数</a></p>
</blockquote>
<p>如以下判断</p>
<ul>
<li>如果传参是【字符串】，则背景是【黑色】；</li>
<li>如果参数是【数字】，则背景是【白色】；</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1a4d85736074233ad9b6e3ab6c23472~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807195347555" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>2）单位检查函数</code></p>
<p>检查一个值是否是一个特定的单位</p>
<p>基本的单位检查函数 <code>ispixel（是否为像素单位）、ispercentage（是否为百分比）、isem（是否为em单位）、isunit（是否为单位）</code></p>
<blockquote>
<p>这些函数是👉<a href="https://link.juejin.cn/?target=https%3A%2F%2Fless.bootcss.com%2Ffunctions%2F%23type-functions" target="_blank" rel="nofollow noopener noreferrer" title="https://less.bootcss.com/functions/#type-functions" ref="nofollow noopener noreferrer">less的内置函数</a></p>
</blockquote>
<p>如以下判断：</p>
<ul>
<li>如果单位是【px】，则背景是【黑色】</li>
<li>如果单位是【%】，则背景是【白色】</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73d90364c3b34a9d84f934b8338c8a0c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807203047595" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">逻辑运算符</h3>
<ul>
<li><code>(),() 相当 于JS中的 ||</code> ，只要有一个符合条件就会执行</li>
</ul>
<p><strong>如以下示例</strong>：当执行 .size的时候传入的第一个参数是100px【或者】第二个参数是100px才会执行</p>
<pre><code class="copyable">.size(@width,@height) when (@width = 100px),(@height = 100px)&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac5006ba8925499d808ef4e177947f64~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807205001615" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>()and() 相当于 JS中的 &&</code>，必须条件全部符合才会执行</li>
</ul>
<p><strong>如以下示例</strong>：当执行 .size的时候传入的第一个参数是100px【并且】第二个参数是100px才会执行</p>
<pre><code class="copyable">.size(@width,@height) when (@width = 100px) and (@height = 100px)&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35b7a7b2e1a94794a06e893d816adc37~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807205224394" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>not 运算符 相当于 非运算 !</code>，条件为 不符合才会执行</li>
</ul>
<p><strong>如以下示例</strong>：传给size的@width不为100px的都执行了；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85b12942279443e7a1747cef5104d43c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807212843636" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">变量和混合结合</h3>
<p>利用变量和混合结合，可以实现对【多个样式类】进行【条件判断】；</p>
<p><strong>如以下示例</strong>：设置了变量 <code>@variable</code>，混合<code>.demo()</code>里的两个类根据判断，最好只把符合条件<code>style2</code>编译了出来</p>
<blockquote>
<p>如果不知道为什么最后@variable取的是b，则去回顾一下👉<a href="https://juejin.cn/post/6992236237922762759" target="_blank" title="https://juejin.cn/post/6992236237922762759">【第一期—变量—变量的Lazy Evaluation和作用域】</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5e9a0004d904281be5ff52b7bfa5719~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807211131069" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">default函数(else)</h3>
<p>default() 函数可根据已创建的 Mixins 条件来形成该条件的补集。</p>
<p><code>可用于模拟else</code></p>
<p><strong>如以下示例</strong>：default()等价于 @width <= 10%</p>
<pre><code class="copyable">.size(@width) when (@width > 10%)&#123;color:red;&#125;
.size(@width) when (default())&#123;color:#333333;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffbbde311a4745d8ae38dda11ebed8ec~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807212819405" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">if关键字（v3.0.0）</h2>
<blockquote>
<p>在v3.0.0版本之前，less一直是用when来实现条件判断的。if关键字【发布于】v3.0.0 【更新于】v3.6.0</p>
</blockquote>
<p>根据条件返回两个值中的一个。</p>
<p>Parameters:</p>
<ul>
<li><code>condition</code> ：布尔表达式</li>
<li><code>value1</code> ：如果 <code>condition</code> 为true，则返回一个值。</li>
<li><code>value2</code> ：如果 <code>condition</code> 不为真，则返回一个值。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/654cfd9a98a24b8d85aa491cdbb8ad96~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807214311292" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意：支持作为 <code>conditional</code> 参数的布尔表达式与<code>Guard Statements</code>相同。</p>
<pre><code class="copyable">div &#123;
    margin: if(not (true), 30px, 10px);
    color: if((true) and (2 > 1), red, black);
    background:if((false) or (isstring("boo!")), red, black);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a991080c8fc465c8409b54d5f104c45~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807214615269" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注:在3.6版本之前，该条件需要一组括号，否则会报错。</p>
<pre><code class="copyable">if(2 > 1, blue, green);   // Causes an error in 3.0-3.5.3
if((2 > 1), blue, green); // Ok 3.0+
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">boolean关键字（v3.0.0）</h2>
<blockquote>
<p>【发布于】v3.0.0 【更新于】v3.6.0</p>
</blockquote>
<p><code>评价为真或假</code></p>
<p>您可以将一个布尔表达式存在变量，以供以后在Guard或 <code>if()</code> 中进行判断。</p>
<p>Parameters:</p>
<ul>
<li><code>condition</code> ：布尔表达式</li>
</ul>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-variable">@bg:</span> rgb(<span class="hljs-number">10</span>, <span class="hljs-number">200</span>, <span class="hljs-number">30</span>);
<span class="hljs-variable">@bg-light:</span> boolean(luma(<span class="hljs-variable">@bg</span>) > <span class="hljs-number">50%</span>);
<span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">background</span>: <span class="hljs-variable">@bg</span>; 
  <span class="hljs-attribute">color</span>: if(<span class="hljs-variable">@bg-light</span>, black, white);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>luma从颜色值中提取亮度的百分比(@color)，返回值：百分比 0-100%</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9c483909f724ae28d5494689aa09a0c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807215517386" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">循环语句</h1>
<p>在其他的编程语言中我们都是通过 for 循环的结构去实现的循环结构。</p>
<p>但是在 Less 中并没有这么一种语法，而是通过【自身调用】从而实现的【循环递归】。</p>
<p>同时我们需要运用之前我们学习到的【条件判断】从而【跳出循环】。</p>
<h2 data-id="heading-10">递归调用自己</h2>
<p><strong>简单示例</strong></p>
<pre><code class="copyable">.w(@counter) when (@counter > 0)&#123;
    //递归调用自身
.w((@counter - 1)); 
     //每次调用时产生的样式代码
width:(10px * @counter);
&#125;

div&#123;
     /*调用循环*/
.w(5);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdba702b8486481e9e3898a73b4005a1~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807220605511" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>实用示例</strong>：利用递归循环创建一个CSS网格;</p>
<pre><code class="copyable">.loop-columns(@n, @i: 1) when (@i =< @n) &#123;
  .column-@&#123;i&#125; &#123;
    width: (@i * 100% / @n);
  &#125;
  .loop-columns(@n, (@i + 1));
&#125;
.loop-columns(4);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>示例分析</strong></p>
<ul>
<li>混合loop-columns设了两个参数@n，@i。并且给@i设置了默认值1</li>
<li>第一次执行，只传了一个参数4，则@n=4，@i=默认值1</li>
<li>在自身调用自己，让@i自增</li>
<li>通过when判断，当@i<=@n时，停止执行</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bd2a34b30394302824e946bceaedc8e~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807221005839" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>实用示例2</strong>：可以设置一些css的预设值，如设置一些padding（可以按上面的思路自行分析一下）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd49750fe8ae4bbca943de2e347973ba~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807221940794" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">使用 <code>range</code> 和 <code>each</code> 创建一个 <code>for</code> 循环(v3.9.0)</h2>
<blockquote>
<p>至少需要Less v3.9.0</p>
</blockquote>
<p>你可以简单地通过生成数字列表并使用 <code>each</code> 数字列表将其扩展为规则集来模拟 <code>for</code> 循环</p>
<pre><code class="copyable">each(range(4), &#123;
  .col-@&#123;value&#125; &#123;
    height: (@value * 50px);
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d491fd6b60b84303a6cf2d4e2dd4c85a~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807222327444" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-12">each(v3.7.0)</h1>
<p>将规则集的值绑定到列表的每个成员。</p>
<p><strong>Parameters</strong></p>
<ul>
<li><code>list</code> -用逗号或空格分隔的值列表。</li>
<li><code>rules</code> -匿名规则集/混合</li>
</ul>
<p>每个列表成员可以被默认绑定<code>@value</code>, <code>@key</code>, <code>@index</code>三个变量，对大部分的列表而言， <code>@key</code>和 <code>@index</code>会被定义为相同的值（比如以1开始的有序列表）。然而，你也可以使用规则自定义列表中的<code>@key</code>值。</p>
<h2 data-id="heading-13">官网示例</h2>
<pre><code class="copyable">@set: &#123;
  one: blue;
  two: green;
  three: red;
&#125;
.set &#123;
  each(@set, &#123;
    @&#123;key&#125;-@&#123;index&#125;: @value;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b066f584e57c4be7bd3696bad356153c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807223225325" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">批量设置class名称</h2>
<pre><code class="copyable">@selectors: div, span, p;

each(@selectors, &#123;
  .sel-@&#123;value&#125; &#123;
    background: #cccccc;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c40a13a6c372470face4f1a4d5ddb064~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807222822883" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">批量设置font-size</h2>
<pre><code class="copyable">/** 定义需要遍历的对象 */
@List: &#123;
    4: 4px;
    5: 5px;
    8: 8px;
    10: 10px;
    12: 12px;
&#125;
each(@List, &#123;
    .fs-@&#123;key&#125; &#123;
        font-size: @value;
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39706b3397bf4b8ea6d3f2f0bdbc9d0d~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807224604905" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">批量设置color</h2>
<pre><code class="copyable">@colors: &#123;
  info: #eee;
  danger: #f00;
&#125;

each(@colors, &#123;
   .text-@&#123;key&#125;&#123;
        color: @value;
  &#125;
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7c3207403e744ab804b85d371bf5cb8~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807224013542" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">在 <code>each()</code> 中设置变量名称</h2>
<p>在 每个<code>each()</code>函数中你不必都使用<code>@value</code>, <code>@key</code>, <code>@index</code>作为变量名。</p>
<p>在Less 3.7版本中，Less通过 <code>each()</code> 函数引入了匿名混入的概念，该混入可能会在以后扩展到语法的其他部分。</p>
<blockquote>
<p>匿名混入使用 <code>#()</code> 或 <code>.()</code> 的形式（以开头） <code>.</code> 或 <code>#</code> 就像常规的mixin一样</p>
</blockquote>
<blockquote>
<p><code>each()</code>函数会获取不定参数中的变量的名字并按顺序把它们赋给到<code>@value</code>、<code>@key</code>、<code>@index</code>的value值。如果你只是写了<code>each(@list, .(@value)&#123;&#125;)</code>,则<code>@key</code>和<code>@index</code>都会变成未定义</p>
</blockquote>
<pre><code class="copyable">@colors: &#123;
  info: #eee;
  danger: #f00;
&#125;

each(@colors,.(@v,@k,@i) &#123;
   .text-@&#123;k&#125;&#123;
        color: @v;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37c221482a384d52aca823286dc4074e~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807224335547" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-18">range(v3.9.0)</h1>
<p>生成一个跨越一系列数值的列表。</p>
<p><strong>Parameters</strong></p>
<ul>
<li><code>start</code> -（可选）起始值，<em>例如1或1px</em></li>
<li><code>end</code> -端值<em>例如5像素</em></li>
<li><code>step</code> -（可选）要增加的数量</li>
</ul>
<p>示例：此示例只是为了把值打印出来看一下，无任何实际意义</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f65c10141d634a508fe088c18c5ce152~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807230119535" loading="lazy" referrerpolicy="no-referrer"></p>
<p>范围内每个值的输出将与 <code>end</code> 值使用相同的单位</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d237ceb8c6a84c6d913bbccd01207b09~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807230330093" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-19">结语</h1>
<p>下期预告：less学习指南第五期 | *****</p>
<p>参考：<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flesscss.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://lesscss.org/" ref="nofollow noopener noreferrer">less官网</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fless.bootcss.com%2Ffunctions%2F%23misc-functions-default" target="_blank" rel="nofollow noopener noreferrer" title="https://less.bootcss.com/functions/#misc-functions-default" ref="nofollow noopener noreferrer">less default</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fless.bootcss.com%2Ffunctions%2F%23logical-functions-if" target="_blank" rel="nofollow noopener noreferrer" title="https://less.bootcss.com/functions/#logical-functions-if" ref="nofollow noopener noreferrer">less if</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fless.bootcss.com%2Ffunctions%2F%23logical-functions-boolean" target="_blank" rel="nofollow noopener noreferrer" title="https://less.bootcss.com/functions/#logical-functions-boolean" ref="nofollow noopener noreferrer">less booleane</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fless.bootcss.com%2Ffunctions%2F%23list-functions-each" target="_blank" rel="nofollow noopener noreferrer" title="https://less.bootcss.com/functions/#list-functions-each" ref="nofollow noopener noreferrer">less each</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fless.bootcss.com%2Ffunctions%2F%23list-functions-range" target="_blank" rel="nofollow noopener noreferrer" title="https://less.bootcss.com/functions/#list-functions-range" ref="nofollow noopener noreferrer">less range</a><br></p>
<hr>
<p>🏃‍♀️🏃‍♀️🏃‍♀️点赞召唤下一期！🏃‍♀️🏃‍♀️🏃‍♀️</p></div>  
</div>
            