
---
title: 'JavaScripts基础（10）DOM操作、DOM节点操作'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5da97989dc8c4a1f86cd36579e6fc229~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 18:08:41 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5da97989dc8c4a1f86cd36579e6fc229~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">DOM树(dom tree)：DOM结构</h2>
<blockquote>
<p>当浏览器加载HTML页面时，首先就是DOM结构计算，计算出来的DOM结构就是<code>DOM树</code>(把页面中的HTML标签像树状结构一样，分析出之间的层级关系)</p>
</blockquote>
<h3 data-id="heading-1">DOM树描述了标签和标签之间的关系（节点间的关系）</h3>
<blockquote>
<p>我们只要知道任何一个标签，都可以依据DOM中提供的属性和方法，获取到页面中任意一个标签或者节点</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5da97989dc8c4a1f86cd36579e6fc229~tplv-k3u1fbpfcp-watermark.image" alt="jsjc5.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">JS中获取DOM元素的方法</h2>
<ul>
<li><code>document.getElementById('id值')</code></li>
<li><code>document.documentElement</code>  获取html元素对象</li>
<li><code>document.body</code>  获取body元素对象</li>
<li><code>document.head</code>  获取head元素对象</li>
<li><code>document.getElementsByName('name属性值')</code></li>
<li><code>[context].getElementsByTagName('标签名')</code></li>
<li><code>[context].getElementsByClassName('class名')</code></li>
<li><code>[context].querySelector(css的选择器:'#aaa''.ddd''.ddd div')</code></li>
<li><code>[context].querySelectorAll(css的选择器:'#aaa''.ddd''.ddd div')</code></li>
</ul>
<h3 data-id="heading-3">document.getElementById('id值')</h3>
<blockquote>
<p>在整个文档中通过元素的id属性值，获取到这个对象</p>
<p>getElementById是获取元素的方法</p>
</blockquote>
<h4 data-id="heading-4">document限定了获取元素的范围，我们把这个范围称之为‘上下文【context】’</h4>
<h4 data-id="heading-5">获取到的是对象数据类型的值</h4>
<h4 data-id="heading-6">getElementById的上下文只能是document：</h4>
<blockquote>
<p>因为严格意义上，一个id是不能重复出现的，浏览器规定只能在整个文档中可以获取这个唯一id</p>
</blockquote>
<h4 data-id="heading-7">如果页面中的ID重复了，我们基于这个方法<code>只能获取到第一个元素</code>，后面相同ID元素无法获取</h4>
<h4 data-id="heading-8">IE6,7下 会把表单元素的name属性当做ID来使用，所以要注意id和表单元素name属性的重复问题</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> oBox=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'box'</span>)

<span class="hljs-keyword">typeof</span> oBox  => <span class="hljs-string">"object"</span>

<span class="hljs-comment">//分析包含的属性</span>
className：存储的是一个字符串，代表当前元素的样式类名

oBox.className=<span class="hljs-string">'aaa'</span>   会覆盖原有的<span class="hljs-class"><span class="hljs-keyword">class</span>
<span class="hljs-title">oBox</span>.<span class="hljs-title">className</span> +</span>=<span class="hljs-string">' aaa'</span>  不会覆盖原有<span class="hljs-class"><span class="hljs-keyword">class</span>  新的<span class="hljs-title">class</span>前边要有空格

<span class="hljs-title">id</span>：存储的是当前元素的<span class="hljs-title">id</span>值

<span class="hljs-title">innerHTML</span>：存储当前元素中所有的内容（包含<span class="hljs-title">HTML</span>标签）
<span class="hljs-title">innerText</span>：存储当前元素中所有的文本内容（不包含<span class="hljs-title">HTML</span>标签）

<span class="hljs-title">style</span>：存储当前元素所有的“行内样式”值（获取和操作的都只能是标签上的行内样式，写在样式表中的样式无法获取到）

</span><span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">兼容处理</h4>
<h5 data-id="heading-10">在ID重复时获取所有ID为‘aaa’的标签(兼容所有浏览器):获取所有标签，判断id</h5>
<blockquote>
<p><code>在JS中，默认会把元素的ID设置为变量，不需要再进行获取设置，而且ID重复，获取的结果就是一个集合，包含所有ID元素，不重复就是一个元素对象（类似于ById的结果）</code></p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">queryAllById</span>(<span class="hljs-params">id</span>)</span>&#123;
<span class="hljs-keyword">var</span> nodeList=<span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'*'</span>);
<span class="hljs-keyword">var</span> arr=[];
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<nodeList.length;i++)&#123;
 nodeList[i].id=== id?arr.push(nodeList[i]):<span class="hljs-literal">null</span>;
&#125;
<span class="hljs-keyword">return</span> arr;
&#125;
queryAllById(<span class="hljs-string">'aaa'</span>)
<span class="hljs-comment">//直接用  aaa也行</span>
<span class="hljs-built_in">console</span>.log(aaa)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">获取元素集合（获取多个元素）：</h2>
<h3 data-id="heading-12">[context].getElementsByTagName('标签名')获取一组元素集合</h3>
<blockquote>
<p>在指定的上下文中，通过元素的标签名<code>获取一组**元素集合**(HTMLCollection)</code></p>
<p>上下文是我们自己来指定的</p>
</blockquote>
<ul>
<li>
<p>1、获取的结果是一组元素集合(HTMLCollection，<code>__proto__</code>指向<code>HTMLCollection</code>)（<code>是一个类数组，不能直接使用数组的方法</code>），</p>
</li>
<li>
<p>2、集合中的每一个值又是一个<code>元素对象</code>（<code>对象数据类型</code>，包含很多内置属性，例如：id、className）</p>
</li>
<li>
<p>3、它会把当前上下文中，子子孙孙（后代）层级内的该标签都获取到（<code>并不是只获取到子级</code>）</p>
</li>
<li>
<p>4、基于这个方法<code>获取到的结果永远都是一个集合</code>，不管里边是否有内容，也不管有几项；如果想操作集合中具体的某一项，需要基于索引获取到才可以</p>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> liList=oBox.getElementsByTagName(<span class="hljs-string">'li'</span>);
liList[<span class="hljs-number">0</span>]  <span class="hljs-comment">//就是第一个li(通过索引获取具体某一个li)</span>
liList.length  <span class="hljs-comment">//集合中li的数量</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">[context].getElementsByClassName('class名')获取到一组元素集合</h3>
<blockquote>
<p>在指定的上下文中通过元素的样式类名（class）<code>获取到一组**元素集合**</code></p>
<p>真实项目中，我们经常是基于样式类给元素设置样式，所以JS中经常通过样式类获取元素，<code>不兼容IE6~8</code></p>
</blockquote>
<h4 data-id="heading-14">解决兼容问题：</h4>
<p>获取所有标签，筛选他们的class</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Node.prototype.queryElementsByClassName=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">arguments</span>.length === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> [];
<span class="hljs-keyword">var</span> className=<span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>];
<span class="hljs-comment">//Array.prototype.slice.call  类数组转化为数组，要不然nodeList.splice不能用</span>
<span class="hljs-keyword">var</span> nodeList=<span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">this</span>.getElementsByTagName(<span class="hljs-string">'*'</span>));
className=className.replace(<span class="hljs-regexp">/^| +$/g</span>,<span class="hljs-string">''</span>).split(<span class="hljs-regexp">/ +/</span>);
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<className.length;i++)&#123;
<span class="hljs-keyword">var</span> reg = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">'(^| +)'</span>+className[i]+<span class="hljs-string">'( +|$)'</span>);
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> j=<span class="hljs-number">0</span>;j<nodeList.length;j++)&#123;
 <span class="hljs-keyword">if</span>(!reg.test(nodeList[j].className))&#123;
 nodeList.splice(j,<span class="hljs-number">1</span>);
 j--;
 &#125;
&#125;
&#125;
<span class="hljs-keyword">return</span> nodeList;
&#125;

<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'J_focus'</span>).queryElementsByClassName(<span class="hljs-string">'slider_item'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">document.getElementsByName('name属性值')获取一组节点集合</h3>
<blockquote>
<p><code>上下文也只能是document</code></p>
<p>在整个文档中通过元素的name属性值<code>获取一组**节点集合**（类数组）</code>（<code>__proto__</code>指向<code>NodeList</code>）</p>
<p>在IE9及以下浏览器中，只对表单元素的name属性起作用（正常来说：我们只会给表单元素设置name；给非表单元素设置name是一个不太符合规范的操作）</p>
</blockquote>
<h3 data-id="heading-16">[context].querySelector(css的选择器:'#aaa''.ddd''.ddd div')获取的是一个元素对象哪怕选择器匹配了多个，也只获取第一个</h3>
<blockquote>
<p>在指定的上下文当中基于选择器（类似于css选择器）获取到指定的**<code>元素对象</code>**（获取的是一个对象<code>哪怕选择器匹配了多个</code>，也<code>只获取第一个</code>）</p>
</blockquote>
<h3 data-id="heading-17">[context].querySelectorAll(css的选择器:'#aaa''.ddd''.ddd div')获取到选择器匹配到的所有元素，结果是一个节点集合</h3>
<blockquote>
<p>在querySelector的基础上，我们获取到选择器<code>匹配到的所有元素</code>，结果是一个<code>节点集合</code>（<code>__proto__</code>指向<code>NodeList</code>）（类数组）</p>
</blockquote>
<p><code>querySelector</code>、<code>querySelectorAll</code>都<code>不兼容</code> <code>IE6~8</code>，不考虑兼容的情况下，我们<code>能用别的方法获取尽量不要用这两个</code>，这两个方法消耗性能较大</p>
<h2 data-id="heading-18">获取浏览器一屏幕的宽高（兼容所有浏览器）</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">document</span>.documentElement.clientWidth || <span class="hljs-built_in">document</span>.body.clientWidth;

<span class="hljs-built_in">document</span>.documentElement.clientHeight || <span class="hljs-built_in">document</span>.body.clientHeight;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">DOM中的节点(node)：<code>元本注档1389</code></h2>
<blockquote>
<p>在html文档中出现的所有东西都是节点</p>
<blockquote>
<p>元素节点：html标签；</p>
<p>文本节点：文字内容；</p>
<p>注释节点：注释内容；</p>
<p>文档节点：document；</p>
</blockquote>
</blockquote>
<h3 data-id="heading-20">每一种类型的节点都会有一些属性区分自己的特性和特征：</h3>
<ul>
<li><code>nodeType</code>：节点类型；</li>
<li><code>nodeName</code>：节点名称；</li>
<li><code>nodeValue</code>：节点值；</li>
</ul>
<h3 data-id="heading-21">元素节点 1</h3>
<ul>
<li><code>nodeType</code>：1；</li>
<li><code>nodeName</code>：大写标签名；</li>
<li><code>nodeValue</code>：null；</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">oBox.nodeType  <span class="hljs-comment">//1</span>
oBox.nodeName  <span class="hljs-comment">//"DIV"</span>
oBox.nodeValue  <span class="hljs-comment">//null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">文本节点 3</h3>
<ul>
<li><code>nodeType</code>：3；</li>
<li><code>nodeName</code>：'#text'；</li>
<li><code>nodeValue</code>：文本内容；</li>
<li>在标准浏览器中，会把<code>空格和换行都当做文本节点来处理</code></li>
</ul>
<h3 data-id="heading-23">注释节点 8</h3>
<ul>
<li><code>nodeType</code>：8；</li>
<li><code>nodeName</code>：'#common'；</li>
<li><code>nodeValue</code>：注释内容；</li>
</ul>
<h3 data-id="heading-24">文档节点 9</h3>
<ul>
<li><code>nodeType</code>：9；</li>
<li><code>nodeName</code>：'#document'；</li>
<li><code>nodeValue</code>：null；</li>
</ul>
<h2 data-id="heading-25">描述节点之间关系的属性</h2>
<h3 data-id="heading-26">parentNode，获取当前节点唯一的父亲节点</h3>
<h3 data-id="heading-27">childNodes，获取当前元素的所有子节点</h3>
<ul>
<li>1、子节点：只获取到<code>儿子级别</code>，不能获取到孙子级及以后</li>
<li>2、所有：<code>包含元素节点，文本节点等</code></li>
</ul>
<h3 data-id="heading-28">children，获取当前元素的所有元素子节点</h3>
<ul>
<li>在I<code>E6~8</code>中会把注释节点也当做元素节点获取到，所以兼容性不好</li>
<li>元素节点</li>
</ul>
<h3 data-id="heading-29">previousSibling，获取当前节点的上一个哥哥节点（获取的哥哥可能是元素也可能是文本等）</h3>
<h3 data-id="heading-30">previousElementSibling：获取上一个哥哥 元素 节点（不兼容IE6~8）</h3>
<h3 data-id="heading-31">nextSibling，获取当前节点的下一个弟弟节点（紧跟的节点）（获取的弟弟可能是元素也可能是文本等）</h3>
<h3 data-id="heading-32">nextElementSibling：获取下一个弟弟 元素 节点（不兼容IE6~8）</h3>
<h3 data-id="heading-33">firstChild，获取当前元素的第一个子节点（可能是元素也可能是文本等）</h3>
<h3 data-id="heading-34">firstElmentChild：获取第一个 元素 子节点（不兼容IE6~8）</h3>
<h3 data-id="heading-35">lastChild，获取当前元素的最后一个子节点（可能是元素也可能是文本等）</h3>
<h3 data-id="heading-36">lastElmentChild：获取最后一个 元素 子节点（不兼容IE6~8）`</h3>
<h3 data-id="heading-37">兼容处理</h3>
<h4 data-id="heading-38">获取当前元素的所有元素子节点</h4>
<blockquote>
<p>解决<code>children</code>在<code>IE6~8</code>中会<code>把注释节点也当做元素节点</code>获取到的问题</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">children</span>(<span class="hljs-params">curEle</span>)</span>&#123;
<span class="hljs-comment">//1、获取当前元素下的所有子节点</span>
<span class="hljs-comment">//2、筛选出来所有的元素子节点（nodeType===1）</span>
<span class="hljs-keyword">var</span> nodeList=curEle.children;
<span class="hljs-keyword">var</span> res=[];
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<nodeList.length;i++)&#123;
 <span class="hljs-keyword">var</span> item=nodeList[i];
 <span class="hljs-keyword">if</span>(item.nodeType === <span class="hljs-number">1</span>)&#123;
  res.push(item)
 &#125; 
&#125;
<span class="hljs-keyword">return</span> res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-39">获取当前元素的上一个哥哥元素节点</h4>
<blockquote>
<p><code>previousSibling</code>:上一个哥哥节点</p>
<p><code>previousElementSibling</code>：上一个哥哥元素子节点</p>
<p>解决<code>previousElementSibling</code>不兼容IE6~8的问题</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">prevElement</span>(<span class="hljs-params">curEle</span>)</span>&#123;
<span class="hljs-comment">//1、获取上一个哥哥节点</span>
<span class="hljs-comment">//2、判断上一个各个节点是不是元素节点（nodeType===1）</span>
<span class="hljs-comment">//不是再往前找</span>
<span class="hljs-keyword">var</span> node=curEle.previousSibling;
<span class="hljs-comment">//node存在 并且  不是元素节点   才往前找</span>
<span class="hljs-keyword">while</span>(node && node.nodeType !== <span class="hljs-number">1</span>)&#123;
node=node.previousSibling;
&#125;
<span class="hljs-keyword">return</span> node;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-40">DOM的增删改</h2>
<h3 data-id="heading-41">document.createElement('标签名')</h3>
<blockquote>
<p>创建一个元素标签（元素对象）</p>
</blockquote>
<h3 data-id="heading-42">createTextNode，创建一个文本节点</h3>
<h3 data-id="heading-43">[container].appendChild(创建的元素对象或已有的元素对象)，把一个元素对象插入到指定容器【末尾】</h3>
<blockquote>
<p>如果文档树中已经存在了 <code>newchild</code>，它将从文档树中删除，然后重新插入它的新位置（<code>如果是dom树中已有的元素对象，会把原有的删除，然后再添加到新的地方</code>）</p>
</blockquote>
<h3 data-id="heading-44">[container].insertBefore(创建的元素对象，要插入其前面的元素)</h3>
<ul>
<li>1、把一个元素对象插入到<code>指定容器中</code>某一个元素标签之前</li>
<li>2、如果<code>未规定</code> 要插入其前面的元素，则 insertBefore 方法会在<code>结尾插入 newnode</code></li>
<li>3、如果给定的子节点是对文档中现有节点的引用，insertBefore() 会将其从当前位置移动到新位置（在将节点附加到其他节点之前，不需要从其父节点删除该节点）</li>
</ul>
<h3 data-id="heading-45">[curEle要克隆的元素].cloneNode()，把一个节点进行克隆</h3>
<ul>
<li>1、[curEle要克隆的元素].cloneNode()：浅克隆（只克隆当前的标签，标签的样式也有，只是没有innerHTML）</li>
<li>2、[curEle要克隆的元素].cloneNode(true)：深克隆，当前标签及里面的内容都一起克隆了</li>
</ul>
<blockquote>
<p>克隆一个元素节点会拷贝它<code>所有的属性以及属性值</code>,当然也就<code>包括了属性上绑定的事件</code>(比如onclick="alert(1)"),但<code>不会拷贝那些使用addEventListener()方法或者node.onclick = fn</code>这种用<code>JavaScript动态绑定的事件</code></p>
</blockquote>
<blockquote>
<p>在使用Node.appendChild()或其他类似的方法将拷贝的节点<code>添加到文档中之前</code>,那个拷贝节点并不属于当前文档树的一部分,也就是说,它<code>没有父节点</code>.</p>
</blockquote>
<h3 data-id="heading-46">[container].removeChild(要删除的元素)，在指定容器当中删除某一个元素</h3>
<h3 data-id="heading-47">[curEle要操作的元素].set/get/removeAttribute(属性名,属性值)</h3>
<blockquote>
<p>设置、获取、删除当前元素的某一个<code>自定义属性</code>;</p>
<p>[curEle要操作的元素].setAttribute(属性名,属性值)</p>
<p>[curEle要操作的元素].getAttribute(属性名)</p>
<p>[curEle要操作的元素].removeAttribute(属性名)</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> oBox=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'box'</span>);
<span class="hljs-comment">//=>1、把当前元素作为一个对象，在对象对应的堆内存中新增一个自定义的属性</span>
oBox.myIndex=<span class="hljs-number">10</span>;                <span class="hljs-comment">//设置</span>
<span class="hljs-built_in">console</span>.log(oBox.myIndex)       <span class="hljs-comment">//获取</span>
<span class="hljs-keyword">delete</span> oBox.myIndex；           <span class="hljs-comment">//删除</span>

<span class="hljs-comment">//2、基于Attribute等dom方法完成自定义属性的设置</span>
oBox.setAttribute(<span class="hljs-string">'myHahaha'</span>,<span class="hljs-string">'123456'</span>)         <span class="hljs-comment">//设置</span>
oBox.getAttribute(<span class="hljs-string">'myHahaha'</span>)                  <span class="hljs-comment">//获取</span>
oBox.removeAttribute(<span class="hljs-string">'myHahaha'</span>)               <span class="hljs-comment">//删除</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong><code>上边两种方法属于独立的运作体制，不能相互混淆使用 </code></strong></p>
</blockquote>
<ul>
<li>
<p>第一种是<code>基于对象键值对操作方式</code> ，修改当前元素对象的堆内存空间来完成（<code>不存在时</code>获取到的是<code>undefined</code>）</p>
</li>
<li>
<p>第二种是<code>直接修改页面中HTML标签的结构来完成的</code>,此种办法设置的自定义属性<code>可以在结构上呈现出来</code>（<code>不存在时</code>获取到的是<code>null</code>）</p>
</li>
<li>
<p>第一种方法设置的属性在elements控制台是<code>看不到的</code>，第二种设置的<code>能看到</code>（<code>myIndex看不到，myHahaha看得到</code>）</p>
</li>
<li>
<p>基于setAttribute设置的自定义属性值<code>都是字符串</code></p>
</li>
<li>
<p>能用第一种不要用第二种，第二种结构上可见易被攻击，而且第二种操作的是dom耗费性能</p>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> oBox=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'box'</span>);
<span class="hljs-comment">//=>1、把当前元素作为一个对象，在对象对应的堆内存中新增一个自定义的属性</span>
oBox.myIndex=<span class="hljs-number">10</span>;                <span class="hljs-comment">//设置</span>
<span class="hljs-built_in">console</span>.log(oBox.getAttribute(<span class="hljs-string">'myIndex'</span>))       <span class="hljs-comment">//null</span>

oBox.setAttribute(<span class="hljs-string">'m'</span>,<span class="hljs-string">'123456'</span>)         <span class="hljs-comment">//设置</span>
<span class="hljs-built_in">console</span>.log(oBox.m)       <span class="hljs-comment">//undefined</span>


<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-48">node.attributes，获取指定节点的属性集合</h3>
<blockquote>
<p>用法：document.getElementsByTagName("BUTTON")[0].attributes;</p>
<p>可以使用 length 属性来确定属性的数量，能够遍历所有的属性节点并提取需要的信息</p>
</blockquote>
<h3 data-id="heading-49"><code>解析一个URL字符串问号传参和HASH值部分</code>：a元素对象的hash/search两个属性分别存储了哈希值和参数值</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str=<span class="hljs-string">"http://www.baidu.com/stu?lx=1&name=AA&age=20#haha"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">queryURLParametr</span>(<span class="hljs-params">str</span>)</span>&#123;
<span class="hljs-comment">//1、创建一个A标签，把需要解析的地址当做a标签的href赋值</span>
<span class="hljs-keyword">var</span> newA=<span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'a'</span>);
newA.href=str;
<span class="hljs-comment">//页面不需要展示newA，我们只是利用他的属性而已，所以不需要添加到页面中</span>
<span class="hljs-comment">//2、a元素对象的hash/search两个属性分别存储了哈希值和参数值</span>
<span class="hljs-keyword">var</span> search=newA.search.substr(<span class="hljs-number">1</span>);
<span class="hljs-keyword">var</span> hash=newA.hash.substr(<span class="hljs-number">1</span>);

<span class="hljs-comment">//3、分别解析出hash和参数即可</span>
<span class="hljs-keyword">var</span> obj=&#123;&#125;;
hash?obj.HASH=hash:<span class="hljs-literal">null</span>;

<span class="hljs-keyword">if</span>(search)&#123;
<span class="hljs-keyword">var</span> search=search.split(<span class="hljs-string">'&'</span>);   <span class="hljs-comment">//["lx=1","name=AA","age=20"]</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<search.length;i++)&#123;
<span class="hljs-keyword">var</span> itemArr=search[i].split(<span class="hljs-string">'='</span>);   <span class="hljs-comment">//["lx","1"]</span>
obj[itemArr[<span class="hljs-number">0</span>]]=itemArr[<span class="hljs-number">1</span>]
&#125;
&#125;
<span class="hljs-keyword">return</span> obj;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            