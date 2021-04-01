
---
title: 'javascript学习（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9612'
author: 掘金
comments: false
date: Tue, 30 Mar 2021 23:49:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=9612'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">JS正则</h1>
<p><code>alert(str.match(re));</code>
<code>match</code> 把所有匹配的东西全部提取出来</p>
<p><code>var re = /\d+/g;</code></p>
<p>+：若干（多少都可以）
g global 找到全部</p>
<h2 data-id="heading-1">转译</h2>
<p>\d 数字 [0-9]
\w 英文 数字 下划线
\s 空白字符</p>
<h1 data-id="heading-2">获取元素方式</h1>
<ul>
<li>getElementsByClassName('box') 根据类名获得某些元素集合</li>
<li>querySelector('.box') 返回指定选择器的<strong>第一个</strong>元素对象 里面的选择器需要加符号 .box #nav</li>
<li>querySelectorAll('.box') 返回指定选择器的所有元素对象集合</li>
</ul>
<h1 data-id="heading-3">事件</h1>
<h2 data-id="heading-4">步骤</h2>
<p>触发相应的一种机制。</p>
<ul>
<li>获取事件源：事件被处罚的对象</li>
<li>绑定事件</li>
<li>添加事件处理程序</li>
</ul>
<h2 data-id="heading-5">innerText&innerHTML</h2>
<p>均 可读写，可以获取元素里面的内容</p>
<h3 data-id="heading-6">innerText</h3>
<ul>
<li>不识别html标签</li>
<li>去除空格和换行</li>
</ul>
<h3 data-id="heading-7">innerHTML</h3>
<ul>
<li>识别html标签</li>
<li>保留空格和换行</li>
<li>W3C标准</li>
</ul>
<h1 data-id="heading-8">获取元素属性值</h1>
<h2 data-id="heading-9">1.element.属性</h2>
<h2 data-id="heading-10">2.element.getAttribute('属性')</h2>
<p>我们自己添加的属性——自定义属性
eg.
div.getAttribute('index')</p>
<h1 data-id="heading-11">设置元素属性值</h1>
<h2 data-id="heading-12">1.element.属性 = '值'</h2>
<h2 data-id="heading-13">2.element.setAttribute("属性","值");   （主要针对自定义属性</h2>
<h1 data-id="heading-14">H5自定义属性</h1>
<h2 data-id="heading-15">设置H5自定义属性</h2>
<p>H5规定自定义属性以<code>data-</code>开头做属性名。</p>
<pre><code class="copyable">element.setAttribute("data-index",2)
div.getAttribute("data-index")
div.dataset
div.dataset.index
div.dataset["index"]
div.dataset.listName
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li><code>element.setAttribute(name, value);</code></li>
</ol>
<p>设置指定元素上的某个属性值。如果属性已经存在，则更新该值；否则，使用指定的名称和值添加一个新的属性。</p>
<ol>
<li><code>let attribute = element.getAttribute(attributeName);</code></li>
</ol>
<p><code>getAttribute()</code>返回元素上一个指定的属性值。如果指定的属性不存在，则返回<code>null</code>或 ""（空字符串）</p>
<ol>
<li><code>element.removeAttribute(attrName);</code></li>
</ol>
<p>元素方法<code>removeAttribute()</code>从指定的元素中删除一个属性</p>
<pre><code class="copyable"><div getTime="10" data-index="2" data-list-name="gloucester"></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>#节点操作</p>
<h2 data-id="heading-16">1.节点概述</h2>
<p>一般的，节点至少拥有nodeType（节点类型），nodeName（节点名称）和nodeValue（节点值）这三个基本属性。</p>
<ul>
<li>元素节点nodeType为1</li>
<li>属性节点nodeType为2</li>
<li>文本节点nodeType为3（文本节点不包括文字/空格/换行等）</li>
</ul>
<h2 data-id="heading-17">2.节点层级</h2>
<h3 data-id="heading-18">子节点</h3>
<h4 data-id="heading-19">（标准）<code>parentNode.childNodes</code>返回值里包含所有子节点，如果需要获得某一特定节点，如元素节点，则需要专门处理。</h4>
<h4 data-id="heading-20">（非标准）<code>parentNode.children</code>只返回子元素节点，其余节点不返回。</h4>
<blockquote>
<p>虽为非标准，但得到了各个浏览器支持，可以放心使用。</p>
</blockquote>
<h4 data-id="heading-21"><code>firstChild</code> 第一个子节点</h4>
<h4 data-id="heading-22"><code>firstElementChild</code> 第一个元素节点</h4>
<p><strong>(IE9以上才支持</strong></p>
<h4 data-id="heading-23">parentNode.children[0]</h4>
<h4 data-id="heading-24">parentNode.children[parentNode.children.length - 1]</h4>
<h3 data-id="heading-25">兄弟节点</h3>
<ul>
<li><code>node.nextSibling</code>返回当前元素的下一个兄弟节点。</li>
<li><code>node.nextElementSibling</code>返回当前元素的下一个兄弟元素节点，找不到则返回null。</li>
<li><code>node.previousElementSibling</code></li>
</ul>
<h3 data-id="heading-26">添加节点</h3>
<p><code>node.appendChild(child)</code>
<code>node.appendChild()</code>方法将一个节点添加到指定父节点的子节点列表<strong>末尾</strong>。类似于css里的after伪元素。</p>
<p><code>node.insertBefore(child,指定元素)</code></p>
<h3 data-id="heading-27">复制节点</h3>
<p>node.cloneNode()</p>
<ul>
<li>如果括号参数为空/false，则是浅拷贝，即只克隆节点本身，不克隆里面的子节点。</li>
<li>如果括号参数为true，则是深拷贝，克隆节点本身，并且克隆里面的子节点。</li>
</ul>
<h3 data-id="heading-28">三种动态创建元素区别</h3>
<ul>
<li>document.write()</li>
<li>element.innerHTML</li>
<li>document.createElement()</li>
</ul>
<p><strong>区别：</strong></p>
<ol>
<li><code>document.write</code>是直接将内容写入页面的内容流，但是文档流执行完毕，则它会导致页面全部重绘。</li>
<li><code>innerHTML</code>是将内容写入某个DOM节点，不会导致页面全部重绘。</li>
<li><code>innerHTML</code>创建多个元素效率更高（不要拼接字符串，采取数组形式拼接），结构稍微复杂。</li>
<li></li>
</ol>
<p><code>createElement()</code>创建多个元素效率稍低一点，但是结构更清晰。</p>
<h1 data-id="heading-29">注册事件</h1>
<h2 data-id="heading-30">注册事件概述：给元素添加事件</h2>
<h3 data-id="heading-31">1.传统注册方式</h3>
<ul>
<li>利用on开头的事件</li>
<li>特点：注册事件的唯一性</li>
<li>同一个元素同一个事件只能设置一个处理函数，最后注册的处理函数将会覆盖前面注册的处理函数。</li>
</ul>
<h3 data-id="heading-32">2.方法监听注册方式</h3>
<ul>
<li><code>addEventListener()</code></li>
<li>IE9以前：<code>attachEvent()</code></li>
<li>特点：同一个元素同一个事件可以注册多个监听器，按注册顺序依次执行。</li>
</ul>
<h1 data-id="heading-33">删除事件</h1>
<h2 data-id="heading-34">删除事件的方式</h2>
<h3 data-id="heading-35">1.传统注册方式</h3>
<p><code>eventTarget.onclick = null;</code></p>
<h3 data-id="heading-36">2.方法监听注册方式</h3>
<p><code>eventTarget.removeEventListener(type, listener[, useCapture]);</code></p>
<h1 data-id="heading-37">DOM事件流：事件传播过程</h1>
<h3 data-id="heading-38">DOM事件流分为三个阶段：</h3>
<h4 data-id="heading-39">1.捕获阶段</h4>
<h4 data-id="heading-40">2.当前目标阶段</h4>
<h4 data-id="heading-41">3.冒泡阶段</h4>
<p><strong>注意：</strong></p>
<ol>
<li>JS代码中只能执行捕获/冒泡其中的一个阶段</li>
<li><code>onclick</code>,<code>attachEvent</code>只能得到冒泡阶段</li>
<li><code>addEventListener(type, listener[, useCapture])</code>第三个参数如果是<code>ture</code>，表示在事件捕获阶段调用事件处理程序；如果是<code>false</code>/不写，表示在事件冒泡阶段调用事件处理程序。</li>
<li>实际开发中我们很少使用事件捕获，我们更关注事件冒泡。</li>
<li>有些事件是没有冒泡的，比如<code>onblur</code>,<code>onfocus</code>,<code>onmouseover</code>,<code>onmouseleave</code>。</li>
<li>事件冒泡有时候会带来麻烦，有时候又会帮助很巧妙地做某些事情。</li>
</ol>
<h1 data-id="heading-42">事件对象</h1>
<ol>
<li><code>event</code>就是一个事件对象，写到侦听函数的小括号里面，当形参来看。</li>
<li>事件对象只有有了事件才会存在，它是<strong>系统给自动创建</strong>的，不需要我们传递参数。</li>
<li>事件对象是事件的一系列相关数据的集合。如鼠标点击里面就包含了鼠标的相关信息：鼠标坐标等。</li>
<li>事件对象可以自己命名，如<code>event,evt,e</code></li>
<li>事件对象也有兼容性问题，ie678通过 <code>window.event</code>兼容性的写法<code>e = e || window.event;</code></li>
</ol>
<h2 data-id="heading-43">事件对象常见属性和方法</h2>
<ul>
<li><code>e.target</code>:返回<strong>触发事件</strong>的对象（即我们点击的那个对象</li>
</ul>
<blockquote>
<p>区别：this返回的是绑定事件的对象（元素）</p>
</blockquote>
<ul>
<li>
<p><code>e.srcElement</code>：返回触发事件的对象，非标准，ie6-8使用。</p>
</li>
<li>
<p><code>e.type</code>: 返回事件的类型，比如<code>click</code>,<code>mouseover</code>,不带on。</p>
</li>
<li>
<p><code>e.returnValue</code>：阻止默认行为（事件），非标准，ie678，如让链接不跳转。</p>
</li>
<li>
<p><code>e.preventDefault()</code>：阻止默认行为（事件），标准。</p>
</li>
<li>
<p><code>e.stopPropagation</code></p>
</li>
</ul>
<h2 data-id="heading-44">事件对象阻止默认行为</h2>
<p>阻止默认行为（事件），比如不让链接跳转，或者让提交按钮不提交。</p>
<h3 data-id="heading-45">1. 方法监听注册方式</h3>
<p><strong>dom标准写法：</strong>
<code>event.preventDefault();</code></p>
<pre><code class="copyable">var a = document.querySelector("a");
a.addEventListener("click", function(e) &#123;
e.preventDefault();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-46">2. 传统注册方式</h3>
<ul>
<li>普通浏览器：<code>e.preventDefault();</code></li>
<li>低版本浏览器（ie678）：<code>return false;</code></li>
</ul>
<p>没有兼容性问题，但return 后面的代码不执行了，而且只限于传统的注册方式。</p>
<h2 data-id="heading-47">事件委托</h2>
<h3 data-id="heading-48">原理：不是每个子节点单独设置事件监听器，而是事件监听器设置在其父节点上，然后利用事件冒泡影响每一个子节点。</h3>
<h2 data-id="heading-49">常用的鼠标事件</h2>
<h3 data-id="heading-50">鼠标事件对象</h3>
<ul>
<li><code>e.clientX</code>/<code>e.clientY</code>：返回鼠标相对于可视区的x和y坐标。</li>
<li><code>e.pageX</code>/<code>e.pageY</code>：返回鼠标相对于文档页面的x和y坐标。</li>
</ul>
<h2 data-id="heading-51">常用的键盘事件</h2>
<ul>
<li><code>onkeyup</code>：按键弹起的时候触发。</li>
<li><code>onkeypress</code>：按键按下的时候触发，不能识别功能键，如ctrl，shift，左右箭头。</li>
<li><code>keydown</code>：按键按下的时候触发，能识别功能键，如ctrl，shift，左右箭头。</li>
</ul>
<h3 data-id="heading-52">三个事件的执行顺序：keydown -- keypress -- keyup</h3>
<blockquote>
<p>注意：
<code>keydown``keypress</code>在文本框里的特点：他们两个事件触发的时候，文字还没落入文本框。
<code>keyup</code>事件触发的时候，文字已经落入文本框中。</p>
</blockquote>
<h2 data-id="heading-53">JS执行机制</h2>
<ol>
<li>先执行执行栈中的同步任务。</li>
<li>异步任务（回调函数）放入任务队列中。</li>
<li>一旦执行栈中的所有同步任务执行完毕，系统就会按次序读取任务队列中的异步任务，于是被读取的异步任务结束等待状态，进入执行栈，开始执行。</li>
</ol>
<h2 data-id="heading-54">location对象</h2>
<p><code>location.href</code>：获取或设置整个URL。
<code>location.search</code>：返回参数。
<code>location.hash</code>：返回片段#后面的内容，常见于链接/锚点</p>
<h2 data-id="heading-55">offset系列</h2>
<h2 data-id="heading-56">offset与style区别</h2>
<h3 data-id="heading-57">offset</h3>
<ul>
<li>可以得到任意样式表中的样式值</li>
<li>获得的数值无单位</li>
<li><code>offsetWidth</code>包含padding+border+width</li>
<li><code>offsetWidth</code>只读属性，不能赋值。</li>
</ul>
<h3 data-id="heading-58">style</h3>
<ul>
<li>只能得到行内样式表中的样式值</li>
<li><code>style.width</code>获得的是带有单位的字符串</li>
<li><code>style.width</code>获得不包含padding, border的值</li>
<li><code>style.width</code>是可读写属性，既可以获取也可以赋值</li>
</ul>
<h2 data-id="heading-59">三大系列总结</h2>
<ul>
<li><code>element.offsetWidth</code></li>
<li><code>element.clientWidth</code>：返回padding，内容区宽度，不含border，返回数值不带单位。</li>
<li><code>element.scrollWidth</code>：返回自身实际宽度，不含border，返回数值不带单位。</li>
<li>页面滚动的距离通过<code>window.pageXOffset</code>获得</li>
</ul>
<h2 data-id="heading-60">立即执行函数</h2>
<h3 data-id="heading-61">1.立即执行函数：不需要调用，立马能够自己执行的函数</h3>
<h3 data-id="heading-62">2.写法</h3>
<p><code>(function()&#123;&#125;)()</code>
<code>(function()&#123;&#125;())</code>
也可以传递参数进来，第二个小括号可以看作是调用函数。</p>
<h3 data-id="heading-63">3.立即执行函数的作用</h3>
<p>独立创建了一个作用域，不存在命名冲突。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            