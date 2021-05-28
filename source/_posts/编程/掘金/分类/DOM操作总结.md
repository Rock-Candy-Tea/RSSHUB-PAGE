
---
title: 'DOM操作总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4542fcdf65f6421e8ba715bc02c16521~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 27 May 2021 19:39:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4542fcdf65f6421e8ba715bc02c16521~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h6 data-id="heading-0">知识点</h6>
<ul>
<li>DOM 本质</li>
<li>DOM 节点操作</li>
<li>DOM 结构操作</li>
<li>DOM 性能</li>
</ul>
<h2 data-id="heading-1">前言</h2>
<p>各种框架层出不穷，但DOM操作一直都会是前端工程师的基础，必备知识。<br>
只会Vue和React等框架，而不懂DOM操作的前端程序员们。。。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4542fcdf65f6421e8ba715bc02c16521~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">DOM的本质？</h2>
<h4 data-id="heading-3">Do you know？</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae8484f65ad94724b5014e1dd75872e3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先，先了解一下什么是<code>xml</code> 。 上代码：</p>
<pre><code class="copyable"><?xml version="1.0" encoding="ISO-8859-1"?>
<note>
<to>George</to>
<from>John</from>
<heading>Reminder</heading>
<body>Don't forget the meeting!</body>
</note>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>XML （可扩展标记语言 EXtensible Markup Language）</p>
<p>XML 是一种标记语言， 被设计用来传输和存储数据，而非显示数据（HTML就被设计用来显示数据）</p>
<p>XML使用的标签没有被预定义，你需要自行定义标签。</p>
<p>SGML、HTML、XML、XHTML、HTML5 之间的关系，知道否？</p>
<p><strong>HTML是一种特殊的XML。它遵循W3C的规定，各种规定，必须先写什么，怎么写什么。</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div>
        <p>跟着W3C标准，有饭吃。。。ヽ(￣▽￣)ﾉ</p>
    </div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1236b40c76fa4ee7a8059cf6bd583dd5~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么如果是一个字符串对象（html一大坨）的话，让浏览器，js处理是非常不方便的。<br>
如何查询，如何操作等等比较麻烦。所以浏览器拿到代码之后。。。</p>
<p><strong>DOM可以理解为浏览器把拿到的html代码，结构化一个浏览器能识别并且js可操作的一个模型而已（也就是DOM结构树）</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99089ba160a74b0b83d255855d6798c6~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>树结构什么的不要我讲了吧</p>
<h2 data-id="heading-4">DOM 节点操作</h2>
<h4 data-id="heading-5">获取 DOM 节点</h4>
<ul>
<li><strong>通过元素类型的方法来操作：</strong></li>
</ul>
<ol>
<li>**<code>document.getElementById();</code> //id名，在实际开发中较少使用，选择器中多用class id一般只用在顶级层存在 不能太过依赖id<br>
**</li>
<li>**<code>document.getElementsByTagName();</code> //标签名<br>
**</li>
<li>**<code>document.getElementsByClassName();</code> //类名<br>
**</li>
<li>**<code>document.getElementsByName();</code> //name属性值，一般不用<br>
**</li>
<li>**<code>document.querySelector();</code> //css选择符模式，返回与该模式匹配的第一个元素，结果为一个元素；如果没找到匹配的元素，则返回null<br>
**</li>
<li>**<code>document.querySelectorAll()</code> //css选择符模式，返回与该模式匹配的所有元素，结果为一个类数组<br>
**</li>
</ol>
<p><strong>注意：</strong></p>
<ul>
<li>前缀为document，意思是在document节点下调用这些方法，当然也可以在其他的元素节点下调用哦！</li>
<li><code>querySelector()</code>和<code>querySelectorAll()</code>两个方法为静态的，不是实时的，保存的是当时的状态，是一个副本，即：在以后的代码中通过方法使所选元素发生了变化，但该值依然不会改变，因此使用有局限性，一般不用，除非就想得到副本</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9b07779e00b4cb9ad544386859c4609~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>根据关系树来获取节点（遍历节点树）：</strong></li>
</ul>
<p>根据前面，我们已经知道：DOM（文档对象模型）可以将任何HTML、XML文档描绘成一个多层次的节点树。所有的页面都表现为以一个特定节点为根节点的树形结构。html文档中根节点为document节点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e5dafac0f2c48bfa0cc03d077407e9b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有节点都有<code>nodeType</code>属性，代表节点的不同类型，通过<code>nodeType</code>属性可以来判断节点的类型。</p>
<p><strong>经常使用的节点主要有以下几种类型：</strong></p>
<ol>
<li>Element类型（元素节点）：nodeType值为 1</li>
<li>Text类型（文本节点）：nodeType值为 3</li>
<li>Comment类型（注释节点）：nodeType值为 8</li>
<li>Document类型（document节点）：nodeType值为 9</li>
</ol>
<p><strong>其规定的一些常用的属性有:</strong></p>
<ul>
<li><code>document.body</code> <code>document.head</code> 分别为HTML中的 <code><body></code> <code><head></code></li>
<li><code>document.documentElement</code>为<code><html></code>标签</li>
</ul>
<p>所有的节点都有 <code>hasChildNodes()</code>方法，用来判断有无子节点 有一个或多个子节点时返回<code>true</code></p>
<p><strong>通过一些属性可以来遍历节点树：</strong></p>
<ol>
<li><code>parentNode</code> //获取所选节点的父节点，最顶层的节点为#document</li>
<li><code>childNodes</code> //获取所选节点的子节点们</li>
<li><code>firstChild</code> //获取所选节点的第一个子节点</li>
<li><code>lastChild</code> //获取所选节点的最后一个子节点</li>
<li><code>nextSibling</code> //获取所选节点的后一个兄弟节点 列表中最后一个节点的<code>nextSibling</code>属性值为<code>null</code></li>
<li><code>`previousSibling` //获取所选节点的前一兄弟节点 列表中第一个节点的`previousSibling`属性值为`null`</code></li>
</ol>
<p><strong>注意：</strong><br>
由于文档中的节点类型较多，遍历子节点的结果很多时候并不能得到我们想要的结果。<br>
小心哦！！空文本也是文本节点！<br>
使用遍历元素节点则很方便。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/258b616db5f349808ee04d1e4dbfc9ae~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>基于元素节点树的遍历（遍历元素节点树）：</strong></li>
</ul>
<ol>
<li><code>parentElement</code>　//返回当前元素的父元素节点（IE9以下不兼容）</li>
<li><code>children</code> // 返回当前元素的元素子节点</li>
<li><code>firstElementChild</code> //返回的是第一个元素子节点（IE9以下不兼容）</li>
<li><code>lastElementChild</code> //返回的是最后一个元素子节点（IE9以下不兼容）</li>
<li><code>nextElementSibling</code> //返回的是后一个兄弟元素节点（IE9以下不兼容）</li>
<li><code>previousElementSibling</code> //返回的是前一个兄弟元素节点（IE9以下不兼容）</li>
</ol>
<p><strong>注意：</strong><br>
这些获取节点的方式，返回值要么是一个特定的节点，要么是一个集合HTMLCollection,这个节点的集合是一个类数组。</p>
<p><strong>HTML中的 attribute 和 JavaScript中的 property</strong></p>
<p><strong>attribute</strong></p>
<p>**<code>attribute</code>是HTML标签中定义的属性(修改html属性，会改变html结构)，它的值只能是字符串。<br>
attribute 有三个方法：<code>setAttribute()</code> , <code>getAttribute()</code>, <code>removeAttribute()</code><br>
**</p>
<p><strong>property</strong></p>
<p><code>property</code>是JavaScript为元素对象定义的属性（修改对象属性，不会体现到html结构中）property 属性可以看作 DOM 对象的键值对，用点操作符修改。它也可以和其他的 JavaScript 对象一样添加自定义的属性以及方法。property 的值可以是任何的数据类型，对大小写敏感。</p>
<h5 data-id="heading-6">attribute 和 property 共同拥有的属性</h5>
<p>虽然Attribute和Property定义的属性分别在不同层面上，但是有以下几个属性是共享的：<br>
<code>id</code> <code>class</code> <code>lang</code> <code>dir</code> <code>title</code></p>
<pre><code class="copyable"><div id="div" class="class" lang="lang" dir="dir" title="title" user="user" >


 var ele = document.getElementById('id');
 
 console.log(ele.getAttribute('id'))    // id
 console.log(ele.getAttribute('class')) // class
 console.log(ele.getAttribute('lang'))  // lang
 console.log(ele.getAttribute('dir'))   // ltr
 console.log(ele.getAttribute('title')) // title
 console.log(ele.getAttribute('user'))  // user

 ele.user1= 'user1'
 console.log(ele.id)                    // id
 console.log(ele.className)             // class
 console.log(ele.lang)                  // lang
 console.log(ele.dir)                   // ltr
 console.log(ele.title)                 // title
 console.log(ele.user1)                 // user

 console.log(ele.user)                  // undefined
 console.log(ele.getAttribute('user1')) // null
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自定义的 property 不会出现在 html 代码中，只存在 js 中。因此，ele.getAttribute(‘user1’) 结果为：null</p>
<p>html 标签的5个标准特性：id，title，lang，dir，className（在DOM中以property方式操作这几个特性会同步到html标签中）。所以即使在html中没有指定id、title等，也会默认赋予一个空串，通过property属性（点操作符）可以访问。 而除此之外在html中设置的其他属性是不能通过Property访问到的（除了attribute特有的属性）。因此，ele.user 结果为：undefined</p>
<p><strong>注意：</strong><br>
有一些比较特殊的情况：</p>
<p><strong>- input 元素的 value</strong></p>
<pre><code class="copyable">var input1 = document.getElementById('input1'); // 获取id为'input1' 的input元素
input1.setAttribute('value', 'test');  // 用setAttribute()方法设置value属性为'test'
console.log(input1.value); // test

a.value = 'change';   // property方式设置value
console.log(a.getAttribute('value')); // test
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>用点操作符修改 value 值，并不会同步到 attribute 上；但是通过 setAttribute 修改属性值，会同步到 property 上。</strong></p>
<p><strong>- 表单</strong></p>
<pre><code class="copyable"><input type='radio' checked='checked' id='radio'>
<script>
  var radio = document.getElementById('radio');
  console.log(radio.getAttribute('checked')); // 'check'
  console.log(radio.checked); // true
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>一些表单元素，对于这些特殊的 attribute 节点，只要存在该节点，对应的 property 就为true，disabled 类似</strong></p>
<p><strong>- href</strong></p>
<pre><code class="copyable"><a href='a.html' id='web'> </a>
<script>
  var radio = document.getElementById('web');
  console.log(web.getAttribute('href')); // 'a.html' 
  console.log(web.href); // 绝对路径
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>attribute 取得是相对路径；property 取得是绝对路径。</strong></p>
<p><strong>建议：</strong></p>
<p>尽量使用property,因为property可能会在js的一些机制中避免DOM的重新渲染，而attribute一旦改了html结构，则一定会引起DOM重新渲染。</p>
<p><strong>以下两种情况用attribute：</strong></p>
<ol>
<li>自定义 attribute 标签，因为它不能同步到 property 上。</li>
<li>访问内置的 html 标签的 attribute，如 input 的 value（可以用来检验 value 值是否改变）</li>
</ol>
<h2 data-id="heading-7">DOM 结构操作</h2>
<ul>
<li>新增/插入节点</li>
<li>获取子元素列表，获取父元素</li>
<li>删除子元素</li>
</ul>
<p>各种DOM操作，请读者自由发挥，耍起来哟~~<br>
<strong>一定要记得多敲敲！！！</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83b8ea991b6f43e39c6e5aa98801369c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>示例：主要代码如下</p>
<pre><code class="copyable"><div id="div1" class="container">
<p id="p1">一段文字 1</p>
    <p>一段文字 2</p>
    <p>一段文字 3</p>
</div>
<div id="div2">
    <img src="https://img-blog.csdnimg.cn/20200201200740869.jpg"/>
</div>

const div1 = document.getElementById('div1')
const div2 = document.getElementById('div2')

// 新建节点
const newP = document.createElement('p')
newP.innerHTML = 'this is newP'
// 插入节点
div1.appendChild(newP)

// 移动节点
const p1 = document.getElementById('p1')
div2.appendChild(p1)

// 获取父元素
console.log( p1.parentNode )

// 获取子元素列表
const div1ChildNodes = div1.childNodes
console.log( div1.childNodes )
const div1ChildNodesP = Array.prototype.slice.call(div1.childNodes).filter(child => &#123;
    if (child.nodeType === 1) &#123;
        return true
    &#125;
    return false
&#125;)
console.log('div1ChildNodesP', div1ChildNodesP)

// 删除子元素
div1.removeChild( div1ChildNodesP[0] )
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">DOM 性能</h2>
<p><strong>DOM 操作非常“昂贵”，避免频繁的DOM操作。</strong></p>
<ul>
<li>
<p><strong>对DOM 查询做缓存</strong></p>
<p>// 不缓存 DOM 查询结果
for (let = 0; i < document.getElementsByTagName('p').length; i++) &#123;
// 每次循环，都会计算 length, 频繁进行 DOM 查询
&#125;</p>
<p>// 缓存 DOM 查询结果
const pList = document.getElementsByTagName('p')
const length = pList.length
for (let i = 0; i < length; i++) &#123;
// 缓存 length, 只进行一次 DOM 查询
&#125;</p>
</li>
<li>
<p><strong>将频繁操作改为一次性操作</strong></p>
<p>const list = document.getElementById('list')</p>
<p>// 创建一个文档片段，此时还没有插入到 DOM 结构中
const frag = document.createDocumentFragment()</p>
<p>for (let i  = 0; i < 20; i++) &#123;
const li = document.createElement('li')
li.innerHTML = <code>List item $&#123;i&#125;</code></p>
<pre><code class="copyable">// 先插入文档片段中
frag.appendChild(li)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>// 都完成之后，再统一插入到 DOM 结构中
list.appendChild(frag)</p>
<p>console.log(list)</p>
</li>
</ul>
<p>复习回顾</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c4806345c234c8d80df85ae29d0f692~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>DOM 是哪种数据结构</strong></p>
<ul>
<li>树（DOM树）</li>
</ul>
<p><strong>DOM 操作的常用API</strong></p>
<ul>
<li>DOM 节点操作</li>
<li>DOM 结构操作</li>
<li>attribute 和 property 操作</li>
</ul>
<p><strong>attribute 和 property 的区别</strong></p>
<ul>
<li>attribute：修改html属性，会改变html结构</li>
<li>property：修改对象属性，不会体现到html结构中</li>
<li>两者都有可能引起DOM重新渲染</li>
</ul>
<p><strong>一次性插入多个DOM节点，考虑性能</strong></p>
<ul>
<li>你可以翻上去再瞧瞧</li>
</ul></div>  
</div>
            