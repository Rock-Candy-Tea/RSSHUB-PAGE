
---
title: 'JS - Web APIs 应用js实现页面交互'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'images/link.jpg'
author: 掘金
comments: false
date: Fri, 28 May 2021 04:42:00 GMT
thumbnail: 'images/link.jpg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Web APIs 和 JS 基础关联性</h2>
<ol>
<li>JS的组成 ： js语法  DOM BOM</li>
<li>Web APIs：DOM  BOM</li>
</ol>
<h2 data-id="heading-1">API 和 Web API</h2>
<ol>
<li>
<p>API： 应用程序编程接口， 是一些预定义的函数</p>
<p>简单理解：是一种工具，以便实现想要完成的功能</p>
</li>
<li>
<p>Web API： 是浏览器提供的一套浏览器功能和页面元素的 API （BOM和 DOM）</p>
</li>
</ol>
<h2 data-id="heading-2">DOM（）</h2>
<h3 data-id="heading-3">一、DOM简介</h3>
<p>1.什么是DOM  文档对象模型，是接口
改变网页的内容，结构，样式
2.DOM树
文档：一个页面就是一个文档 document
元素：页面中的所有标签 element
节点：网页中所有内容都是节点 node
DOM 把以上内容都看做是对象</p>
<h3 data-id="heading-4">二、获取元素</h3>
<p>如何获取网页元素？</p>
<p>1.根据ID获取 <code>getElementByld()</code>方法</p>
<pre><code class="copyable"><div id="time">2020-11-25</div>
    <script>
        //1.因为文档页面从上往下加载 所以得先有标签  所有script写在标签下面
        //2.get获取element 元素 by通过 驼峰命名法
        //3.参数 id是大小写敏感的字符串
        //4.返回的是一个元素对象
        var timer = document.getElementById('time');
        console.log(timer);
        console.log(typeof timer);
        //5.console.dir(timer);  打印我们返回的元素对象 更好的查看里面的属性和方法
        console.dir(timer);
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.根据标签名获取 <code>getElementsByTagName()</code>方法  --返回带有指定标签名的对象的集合</p>
<ol>
<li>返回的是 获取过来元素对象的集合 以伪数组的形式存储的</li>
<li>如果页面中只有一个li 返回的还是伪数组形式</li>
<li>如果页面中没有这个元素 返回的是空的伪数组</li>
</ol>
<p>获取某个元素（父元素）内部所有指定标签名的子元素 <code>element.getElementsByTagName('标签名')</code></p>
<p>3.通过HTML5新增的方法获取</p>
<ol>
<li><code>document.querySelector('选择器')</code>   //根据指定选择器返回第一个元素对象</li>
<li><code>document.getElementsByClassName('类名')</code> //根据类名返回元素对象集合</li>
<li><code>document.querySelectorAll('选择器')</code>  //返回指定选择器的所有元素对象集合</li>
</ol>
<p>4.获取特殊元素(body,html)</p>
<ol>
<li>获取body  ： <code>document.body</code></li>
<li>获取html： <code>document.documentElement</code></li>
</ol>
<h3 data-id="heading-5">三、事件基础</h3>
<p>1.事件三要素： 事件源 事件类型  事件处理程序</p>
<ul>
<li>事件源： 事件被触发的对象 as:按钮</li>
<li>事件类型： 如何触发? 什么事件? 比如鼠标点击(onclick) 鼠标经过 键盘按下</li>
<li>事件处理程序： 通过一个函数赋值的方式 完成</li>
</ul>
<p>2.执行事件的步骤</p>
<ul>
<li>获取事件源</li>
<li>注册事件(绑定事件)</li>
<li>添加事件处理程序(采取函数赋值方法)</li>
</ul>
<h3 data-id="heading-6">四、操作元素</h3>
<p>1.改变元素的按钮</p>
<ol>
<li><code>element.innerText</code> //从起始位置到终点位置的内容，但它去除html标签 同时空格和换行也会去掉</li>
<li><code>element.innerHTML</code>  //起始位置到终点位置的全部内容 包括html标签 同时保留空格和换行</li>
</ol>
<p>区别：</p>
<ul>
<li>1.innerText 不识别html标签   非标准   去除空格和换行</li>
<li>2.innerHTML 识别html标签   W3C标准   保留空格和换行</li>
</ul>
<blockquote>
<pre><code class="copyable">     这两个属性是可读写的  可以获取元素里面的内容
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>2.常用元素的属性操作</p>
<pre><code class="copyable"><button id="ldh">刘德华</button>
    <button id="zxy">张学友</button><br>
    <img src="images/link.jpg" alt="" title="刘德华">
    <script>
        //修改元素属性 src
        //1.获取元素
        var ldh = document.getElementById('ldh');
        var zxy = document.getElementById('zxy');
        var img = document.querySelector('img');
        //2.注册事件
        zxy.onclick = function() &#123;
            img.src = 'images/zhang.jpg';
            img.title = '张学友';
        &#125;
        ldh.onclick = function() &#123;
            img.src = 'images/link.jpg';
            img.title = '刘德华';
        &#125;
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.表单元素的属性操作
4.样式属性操作
<code>element.style</code> 行内样式操作
<code>element.className</code>  类名样式操作</p>
<p>注意:</p>
<ol>
<li>JS里面的样式采取驼峰命名法 fontSize  backgroudColor</li>
<li>JS 修改 sytle 样式操作 产生的是行内样式 css 权重比较高</li>
<li>className 会直接更改元素的类名，会覆盖原先的类名</li>
</ol>
<p>5.排他思想
<code>干掉所有人，留下他自己</code></p>
<pre><code class="copyable"><body>
    <button>按钮1</button>
    <button>按钮2</button>
    <button>按钮3</button>
    <button>按钮4</button>
    <button>按钮5</button>
    <script>
        var btns = document.getElementsByTagName('button');
        for (var i = 0; i < btns.length; i++) &#123;
            btns[i].onclick = function() &#123;
                // 先把所有按钮的背景颜色去掉
                // 然后才变颜色
                for (var i = 0; i < btns.length; i++) &#123;
                    btns[i].style.backgroundColor = '';
                &#125;
                this.style.backgroundColor = 'pink';
            &#125;
        &#125;
    </script>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6.自定义属性的操作</p>
<ol>
<li>获取属性值</li>
</ol>
<ul>
<li><code>element.属性</code></li>
<li><code>element.getAttribute('属性')</code></li>
</ul>
<ol start="2">
<li>设置属性值</li>
</ol>
<ul>
<li><code>element.属性='值'</code></li>
<li><code>element.setAttribute('属性'，'值')</code></li>
</ul>
<ol start="3">
<li>移除属性</li>
</ol>
<ul>
<li><code>element.removeAttribute('属性')</code></li>
</ul>
<p>7.H5自定义属性</p>
<blockquote>
<p>自定义属性目的：是为了保存并使用数据，有些数据可以保存到页面中而不用保存到数据库中</p>
</blockquote>
<ol>
<li>
<p>设置H5自定义属性 规定自定义属性date- 开头 作为属性名并赋值</p>
<pre><code class="copyable"><div data-index="2" data-list-name="andy"></div>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>获取H5自定义属性</p>
</li>
</ol>
<p><code>element.getAttribute('属性')</code>
H5新增<code>element.dataset.index</code> 或者 <code>element.dataset['index']</code></p>
<p>注意：</p>
<ol>
<li>dataset 是一个集合 里面存放了所有以data开头的自定义属性</li>
<li>如果自定义属性有多个- 连接的单词 采取驼峰命名法
<code>console.log(div.dataset.listName)</code></li>
</ol>
<h3 data-id="heading-7">五、节点操作</h3>
<p>1.为什么学节点操作：逻辑性强，但兼容性稍差</p>
<ol>
<li>利用DOM提供的方法获取元素</li>
<li>利用节点层次关系获取元素</li>
</ol>
<p>2.节点概述 在DOM中 节点用node</p>
<ol>
<li>nodeType（节点类型） nodeName（节点名称） nodeValue(节点值)</li>
<li>元素节点 1 属性节点 2 文本节点 3</li>
<li>元素节点是主要操作</li>
</ol>
<p>3.节点层级  父子兄层级关系</p>
<ol>
<li>父级节点</li>
</ol>
<ul>
<li><code>node.parentNode</code>得到的是离元素最近的父级节点  如果找不到父节点 返回null</li>
</ul>
<ol start="2">
<li>子节点</li>
</ol>
<ul>
<li><code>parentNode.childNodes</code>（标准） 得到的是 文本节点 元素节点等等</li>
<li><code>parentNode.children</code> （非标准）是一个只读属性，返回所有的子元素节点</li>
<li><code> parentNode.firstChild</code>  返回第一个节点 不管是文本节点还是元素节点</li>
<li><code>parentNode.lastChild</code>  返回最后一个节点 不管是文本节点还是元素节点</li>
<li><code>parentNode.firstElementChild</code>  返回第一个子元素</li>
<li><code>parentNode.lastElementChild</code>  返回最后一个子元素 //兼任性问题 IE9以上
//实际开发中的写法</li>
<li><code>console.log(ol.children[0])</code> 第一个子元素</li>
<li><code>console.log(ol.children[ol.children.length - 1])</code>最后一个子元素</li>
</ul>
<p>3.兄弟节点</p>
<ul>
<li><code>node.nextSibling</code> 得到的是下一个兄弟节点 文本节点 元素节点等等</li>
<li><code>node.previousSibling</code>  得到的是上一个兄弟节点 文本节点 元素节点等等</li>
<li><code>node.nextElementSibling</code>  得到的是下一个兄弟元素节点</li>
<li><code>node.previousElementSibling</code>  得到的是上一个兄弟元素节点</li>
</ul>
<p>4.创建节点</p>
<ul>
<li><code>document.createElement('tagName')</code></li>
<li>添加节点 <code>node.appendChild(child)</code>  node 父级 child 子级  后面追加元素类似于push</li>
<li><code>node.insertBefore(child,指定元素)</code>  指定子元素前面插入元素</li>
</ul>
<blockquote>
<p>在页面中添加一个新的元素：1.创建元素 2.添加元素</p>
</blockquote>
<p>5.删除节点</p>
<ul>
<li><code>node.removeChild(child)</code></li>
</ul>
<p><code>阻止链接跳转：<a href='javascript:;'>删除</a></code></p>
<p>6.复制节点（克隆）
<code>node.cloneNode()</code>
注意：</p>
<ol>
<li>如果括号参数为空或者false  则浅拷贝 只复制标签不复制里面的内容</li>
<li>如果括号参数为 true  则深拷贝 全复制</li>
</ol>
<p>7.三种动态创建元素区别</p>
<ul>
<li><code>document.write()</code>           如果页面文档流加载完毕 会导致页面重绘</li>
<li><code>element.innerHTML</code>创建多个元素效率更高（不要拼接字符串，采取数组形式拼接）</li>
<li><code>document.createElement()</code>        创建多个元素效率稍微低一点点，但结构更清晰</li>
</ul>
<h2 data-id="heading-8">DOM重点核心---事件高级</h2>
<h3 data-id="heading-9">一、注册事件（绑定事件）</h3>
<ol>
<li>传统注册方式：具有唯一性，同一个元素同一个事件只能设置一个处理函数，最后注册的处理函数将会覆盖前面注册的处理函数</li>
<li>方法监听注册方式：<code>元素.addEventListener(type,listener[,useCapture])</code></li>
</ol>
<p><strong>特点：同一个元素同一个事件可以注册多个监听器</strong></p>
<ul>
<li>
<p>type:事件类型字符串 要加‘’ 比如click，mouseover  不要带on</p>
</li>
<li>
<p>listener：事件处理函数，事件发生时，会调用该监听函数</p>
</li>
<li>
<p>useCaoture:可选参数，是一个布尔值，默认false</p>
<p>ie9 以前版本：<code>attachEvent('onclick',回调函数)</code></p>
</li>
</ul>
<h3 data-id="heading-10">二、删除事件（解绑事件）</h3>
<p>删除事件的方式</p>
<ul>
<li>传统注册方式： <code>eventTarget.onclick=null</code></li>
<li>方法监听注册方式：<code>eventTarget.removeEventListener(type,listener[,useCapture])</code></li>
<li>ie9 以前版本：<code>detachEvent('onclick',回调函数)</code></li>
</ul>
<h3 data-id="heading-11">三、DOM事件流：事件传播的过程</h3>
<p>捕获阶段 目标阶段  冒泡阶段（石头扔水里）</p>
<h3 data-id="heading-12">四、事件对象</h3>
<ol>
<li>event 就是一个事件对象 写到我们侦听函数的小括号里面 当形参来看</li>
<li>事件对象只有有了事件才会存在 它是系统给我们创建的 不需要传递参数</li>
<li>事件对象是 我们是事件的一系列相关数据的集合 跟事件相关 比如鼠标点击里面就包含了鼠标的相关信息，鼠标坐标  如果是键盘事件里面就包含的键盘事件的信息 比如 判断用户按下了那个键</li>
<li>事件对象可以用别的命名 比如event evt  e</li>
<li>兼容问题 ie678 通过 <code>window.event</code></li>
</ol>
<p>事件对象的常见属性和方法</p>
<p><code>e.target</code> 返回的是触发事件的对象(元素)  <code>this</code>返回的是绑定事件的对象(元素)</p>
<p>区别：<code>e.target</code>点击了哪个元素，就返回哪个元素 <code>this</code> 哪个元素绑定这个点击事件 那么就返回谁</p>
<p>兼容性：</p>
<ul>
<li>ie 用<code>e.srcElement</code>获取触发事件的对象</li>
<li><code>e.type</code> 返回事件对象类型</li>
<li>阻止默认行为（事件）让链接不跳转 或者让提交按钮不提交 <code>e.preventDefault()</code></li>
<li>低版本浏览器<code>e.returnValue</code>--属性 或者利用<code>return false</code>也能阻止注意后面代码不执行 而且只限于传统的注册方式</li>
</ul>
<h3 data-id="heading-13">五、阻止事件冒泡</h3>
<p>1.阻止事件冒泡的两种方式</p>
<ol>
<li>e.stopPropagation(); //标准</li>
<li>e.cancelBubble=true;  //ei678</li>
</ol>
<p>2.阻止事件冒泡的兼容性解决方案</p>
<pre><code class="copyable">if(e && e.stopPropagation)&#123;
           e.stopPropagation();
&#125;else&#123;
           window.event.cancelBubble = true;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">六、事件委托(代理，委派)</h3>
<p>事件委托原理：不要给每个子节点单独设置事件监听器，而是事件监听器设置在其父节点上，然后利用冒泡原理影响设置每个子节点</p>
<p>事件委托的作用：只操作了一次DOM，提升了程序的性能</p>
<h3 data-id="heading-15">七、常用的鼠标事件</h3>
<ol>
<li>禁止鼠标右键菜单： <code>contextmenu</code></li>
<li>禁止鼠标选中：<code>selectstart</code></li>
</ol>
<p>2.鼠标事件对象：<code>MouseEvent</code>  键盘事件对象：<code>KeyboardEvent</code></p>
<ol>
<li><code>e.clientX/Y</code> 返回的是可视区的x y 坐标</li>
<li><code>e.pageX/Y</code> 返回的是相对于文档页面的x y坐标</li>
<li><code>e.screenX/Y</code> 返回的是相对于电脑屏幕的x y坐标</li>
<li><code>mousemove</code> 鼠标移动</li>
<li><code>mousedown</code> 鼠标按下</li>
<li><code>mouseup</code> 鼠标松开</li>
</ol>
<h3 data-id="heading-16">八、常用的键盘事件</h3>
<ol>
<li>键盘事件对象：<code>KeyboardEvent</code></li>
</ol>
<ul>
<li>onkeyup 某个键盘按键被松开的时候触发</li>
<li>onkeydown 某个键盘按键被按下时触发</li>
<li>onkeypress 某个键盘按键被按下时触发 但是它不识别功能键 比如ctrl shift 箭头等</li>
</ul>
<blockquote>
<p>三个事件的执行顺序 down>press>up</p>
</blockquote>
<p>2.<code>keyCode属性</code> 返回该键的ASCII码值 判断用户按下了哪个键</p>
<p>keydown 和 keypress 在文本框里面的特点: 事件触发的时候 文字还没有落入文本框中</p>
<h2 data-id="heading-17">BOM</h2>
<h3 data-id="heading-18">一、BOM概述</h3>
<ol>
<li>什么时BOM  浏览器对象模型  与浏览器进行交互的对象</li>
<li>BOM的构成 window对象 是浏览器的顶级对象  全局变量，函数都会变成window对象的属性的方法</li>
</ol>
<blockquote>
<p>BOM>DOM</p>
</blockquote>
<h3 data-id="heading-19">二、window对象常见的事件</h3>
<p>1.窗口加载事件</p>
<ol>
<li><code>window.onload=function()&#123;&#125;</code></li>
<li><code>window.addEventListener('load',function()&#123;&#125;)</code> 最提倡的写法</li>
<li><code>document.addEventListener('DOMContentLoaded',function()&#123;&#125;)</code>DOM元素加载完就能执行 不包含图片 falsh css</li>
</ol>
<p>load 等页面内容全部加载完毕 包含页面dom元素 图片 flash css 等</p>
<p>2.调整窗口大小事件</p>
<ol>
<li><code>window.onresize=function()&#123;&#125;</code></li>
<li><code>window.addEventListerner('resize',function()&#123;&#125;)</code></li>
<li><code>window.innerWidth</code> 获取当前屏幕的宽度</li>
</ol>
<h3 data-id="heading-20">三、定时器</h3>
<p>1.两种定时器</p>
<ul>
<li><code>setTimeout()</code></li>
<li><code>setInterval()</code></li>
</ul>
<p>2.<code>setTimeout()</code>  定时器   -----回调函数 callback</p>
<ul>
<li><code>window.setTimeout(调用函数，延时时间)</code>window可省略  延时时间是毫秒</li>
</ul>
<p>3.停止<code>setTimeout()</code>  定时器   <code>clearTimeout()</code></p>
<p>4.<code>setInterval()</code> 定时器  每间隔一段时间 调用一次函数</p>
<p>5.停止<code>setInterval()</code> 定时器   <code>clearInterval()</code></p>
<p>6.this</p>
<ul>
<li>全局作用域和普通函数中<code>this</code>指向window  （计时器里面的<code>this</code>指向window）</li>
<li>方法调用中谁调用<code>this</code>指向谁</li>
<li>构造函数中<code>this</code>指向构造函数的实例</li>
</ul>
<h3 data-id="heading-21">四、js执行队列（事件循环 event loop）</h3>
<p>1.js是单线程</p>
<p>2.同步（执行栈/主车道）和异步（任务队列/应急车道）</p>
<ul>
<li>同步是一个一个执行 异步是多个任务同时执行</li>
<li>回调函数为异步任务</li>
</ul>
<p>3.js执行机制 :先执行同步任务 ,遇到回调函数 ,放到任务队列 ,同步任务执行完成, 再执行异步任务</p>
<h3 data-id="heading-22">五、location对象</h3>
<p>1.什么是location对象</p>
<p>location属性用于获取或设置窗体的url  并且用于解析url ----返回的是一个对象</p>
<p>2.url 统一资源定位符</p>
<p>3.location 对象属性</p>
<ul>
<li><code>location.href</code>  获取或者设置整个url</li>
<li><code>location.search</code> 返回参数</li>
</ul>
<p>4.location.assign() 重定向  （可后退）</p>
<ul>
<li><code>location.replace()</code> 替换当前页面（不能后退）</li>
<li><code>location.reload()</code> 重新加载页面  如果强制刷新（true）；ctrl+f5</li>
</ul>
<h3 data-id="heading-23">六、navigator对象</h3>
<p>常用的属性<code>userAgent</code>  用来判断用户用pc端还是移动端打开该页面</p>
<h3 data-id="heading-24">七、history对象</h3>
<ol>
<li><code>back()</code> 后退</li>
<li><code>forward()</code> 前进</li>
<li><code>go(参数)</code> 前进后退功能 参数如果是1 前进1个页面 如果是-1 后退一个页面</li>
</ol></div>  
</div>
            