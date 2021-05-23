
---
title: 'js中DOM 节点的一些操作方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b13ada6fa9db4401a0d2161b46ca0f8f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 21 May 2021 04:16:29 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b13ada6fa9db4401a0d2161b46ca0f8f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>js中DOM 节点的一些操作方法</p>
<h1 data-id="heading-0">DOM</h1>
<h2 data-id="heading-1">什么是DOM</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b13ada6fa9db4401a0d2161b46ca0f8f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>DOM：文档对象模型。DOM 为文档提供了结构化表示，并定义了如何通过脚本来访问文档结构。目的其实就是为了能让js操作html元素而制定的一个规范。</strong></p>
<p>DOM就是由节点组成的。</p>
<p><strong>解析过程</strong></p>
<p>HTML加载完毕，渲染引擎会在内存中把HTML文档，生成一个DOM树，getElementById是获取内中DOM上的元素节点。然后操作的时候修改的是该元素的属性。</p>
<p>DOM树（一切都是节点）</p>
<p>DOM的数据结构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cc831ae97cd41b586b6def281ad7f8e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>上图可知，在HTML当中，一切都是节点：（非常重要</strong>）<br>
<strong>元素节点：HMTL标签。</strong><br>
<strong>文本节点：标签中的文字（比如签之间的空格、换行）</strong><br>
<strong>属性节点：：标签的属性</strong><br>
<strong>整个html文档就是一个文档节点。所有的节点都是Object</strong></p>
<h2 data-id="heading-2">DOM可以做什么</h2>
<ul>
<li>找对象（元素节点）</li>
<li>设置元素的属性值</li>
<li>设置元素的样式</li>
<li>动态创建和删除元素</li>
<li>事件的触发响应：事件源、事件、事件的驱动程序</li>
</ul>
<h2 data-id="heading-3">DOM节点的获取</h2>
<p>DOM节点的获取方式其实就是获取事件源的方式</p>
<p>操作元素节点，必须首先找到该节点。有三种方式可以获取DOM节点：</p>
<pre><code class="copyable">var div1 = document.getElementById("box1");      //方式一：通过id获取单个标签

var arr1 = document.getElementsByTagName("div1");     //方式二：通过 标签名 获得 标签数组，所以有s

var arr2 = document.getElementsByClassName("hehe");  //方式三：通过 类名 获得 标签数组，所以有s
<span class="copy-code-btn">复制代码</span></code></pre>
<p>既然方式二、方式三获取的是标签数组，那么习惯性是先遍历之后再使用。</p>
<p>特殊情况：数组中的值只有1个。即便如此，这一个值也是包在数组里的。这个值的获取方式如下：</p>
<pre><code class="copyable">document.getElementsByTagName("div1")[0];    //取数组中的第一个元素

document.getElementsByClassName("hehe")[0];  //取数组中的第一个元素
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">DOM访问关系的获取</h2>
<p>DOM的节点并不是孤立的，因此可以通过DOM节点之间的相对关系对它们进行访问。如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f028caab2454198a2e5913a4a74bc91~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>节点的访问关系，是以属性的方式存在的。</p>
<p>JS中的父子兄访问关系：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5030e7fce0c40b1a3948f68286e9582~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们要重点知道parentNode和children这两个属性的用法。下面分别介绍。</p>
<h2 data-id="heading-5">获取父节点</h2>
<p>调用者就是节点。一个节点只有一个父节点，调用方式就是</p>
<pre><code class="copyable">节点.parentNode
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">（1）nextSibling：</h3>
<pre><code class="copyable"> 指的是下一个节点（包括标签、空文档和换行节点）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>火狐、谷歌、IE9+版本：都指的是下一个节点（包括标签、空文档和换行节点）。</p>
<p>IE678版本：指下一个元素节点（标签）。</p>
<h3 data-id="heading-7">（2）nextElementSibling：</h3>
<p>火狐、谷歌、IE9+版本：都指的是下一个元素节点（标签）。
总结：为了获取下一个元素节点，我们可以这样做：在IE678中用nextSibling，在火狐谷歌IE9+以后用nextElementSibling，于是，综合这两个属性，可以这样写：</p>
<p><code>下一个兄弟节点 = 节点.nextElementSibling || 节点.nextSibling</code></p>
<p>previous的中文是: 前一个</p>
<h3 data-id="heading-8">（1）previousSibling：</h3>
<p>火狐、谷歌、IE9+版本：都指的是前一个节点（包括标签、空文档和换行节点）。
IE678版本：指前一个元素节点（标签）。</p>
<h3 data-id="heading-9">（2）previousElemntSibling：</h3>
<p>火狐、谷歌、IE9+版本：都指的是前一个元素节点（标签）。
总结：为了获取前一个元素节点，我们可以这样做：在IE678中用previousSibling，在火狐谷歌IE9+以后用previousElementSibling，于是，综合这两个属性，可以这样写：</p>
<p>前一个兄弟节点 = 节点.previousElementSibling || 节点.previousSibling</p>
<h3 data-id="heading-10">3、补充：获得任意一个兄弟节点：</h3>
<p>节点自己.parentNode.children[index];  //随意得到兄弟节点
获取单个的子节点</p>
<h3 data-id="heading-11">1、第一个子节点 | 第一个子元素节点：</h3>
<h2 data-id="heading-12">（1）firstChild：</h2>
<p>火狐、谷歌、IE9+版本：都指的是第一个子节点（包括标签、空文档和换行节点）。</p>
<p>IE678版本：指第一个子元素节点（标签）。</p>
<h2 data-id="heading-13">（2）firstElementChild：</h2>
<p>火狐、谷歌、IE9+版本：都指的是第一个子元素节点（标签）。
总结：为了获取第一个子元素节点，我们可以这样做：在IE678中用firstChild，在火狐谷歌IE9+以后用firstElementChild，于是，综合这两个属性，可以这样写：</p>
<p>第一个子元素节点 = 节点.firstElementChild || 节点.firstChild</p>
<h2 data-id="heading-14">2、最后一个子节点 | 最后一个子元素节点：</h2>
<h3 data-id="heading-15">（1）lastChild：</h3>
<p>火狐、谷歌、IE9+版本：都指的是最后一个子节点（包括标签、空文档和换行节点）。</p>
<p>IE678版本：指最后一个子元素节点（标签）。</p>
<h3 data-id="heading-16">（2）lastElementChild：</h3>
<p>火狐、谷歌、IE9+版本：都指的是最后一个子元素节点（标签）。
总结：为了获取最后一个子元素节点，我们可以这样做：在IE678中用lastChild，在火狐谷歌IE9+以后用lastElementChild，于是，综合这两个属性，可以这样写：</p>
<p>最后一个子元素节点 = 节点.lastElementChild || 节点.lastChild
获取所有的子节点</p>
<h3 data-id="heading-17">（1）childNodes：</h3>
<p>标准属性。返回的是指定元素的子节点的集合（包括元素节点、所有属性、文本节点）。是W3C的亲儿子。</p>
<p>火狐 谷歌等高本版会把换行也看做是子节点。（了解）
用法：</p>
<p>子节点数组 = 父节点.childNodes;   //获取所有节点。</p>
<h2 data-id="heading-18">（2）children：</h2>
<p>非标准属性。返回的是指定元素的子元素节点的集合。【重要】</p>
<p>它只返回HTML节点，甚至不返回文本节点。</p>
<p>在IE6/7/8中包含注释节点（在IE678中，注释节点不要写在里面）。</p>
<p>虽然不是标准的DOM属性，但它和innerHTML方法一样，得到了几乎所有浏览器的支持。</p>
<p>用法：（用的最多）</p>
<p>子节点数组 = 父节点.children;   //获取所有节点。用的最多。
nodeType</p>
<p>这里讲一下nodeType。</p>
<p>nodeType == 1 表示的是元素节点（标签） 。记住：元素就是标签。</p>
<p>nodeType == 2 表示是属性节点 了解</p>
<p>nodeType == 3 是文本节点 了解</p>
<p><strong>DOM节点操作（重要）</strong></p>
<p>上一段的内容：节点的访问关系都是属性。</p>
<p>节点的操作都是函数（方法）</p>
<p>创建节点</p>
<p>格式如下：</p>
<p>新的标签(元素节点) = document.createElement("标签名");</p>
<p>比如，如果我们想创建一个li标签，或者是创建一个不存在的adbc标签，可以这样做：</p>
<pre><code class="copyable"><script type="text/javascript">
    var a1 = document.createElement("li");   //创建一个li标签
    var a2 = document.createElement("adbc");   //创建一个不存在的标签

    console.log(a1);
    console.log(a2);

    console.log(typeof a1);
    console.log(typeof a2);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/872da7bec16b4d52bd98ce1ccade1982~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>插入节点</p>
<p>插入节点有两种方式，它们的含义是不同的。</p>
<p>方式1：</p>
<p>父节点.appendChild(新的子节点);
解释：父节点的最后插入一个新的子节点。</p>
<p>方式2：</p>
<p>父节点.insertBefore(新的子节点,作为参考的子节点);
解释：</p>
<p>在参考节点前插入一个新的节点。
如果参考节点为null，那么他将在父节点最后插入一个子节点。
删除节点</p>
<p>格式如下：</p>
<p>父节点.removeChild(子节点);</p>
<p>解释：用父节点删除子节点。必须要指定是删除哪个子节点。</p>
<p>如果我想删除自己这个节点，可以这么做：</p>
<p>node1.parentNode.removeChild(node1);
复制节点（克隆节点）</p>
<p>格式如下：</p>
<p><code> 要复制的节点.cloneNode();       //括号里不带参数和带参数false，效果是一样的。</code></p>
<p>要复制的节点.cloneNode(true);</p>
<p>括号里带不带参数，效果是不同的。解释如下：</p>
<p>不带参数/带参数false：只复制节点本身，不复制子节点。</p>
<p>带参数true：既复制节点本身，也复制其所有的子节点。</p>
<p>设置节点的属性
我们可以获取节点的属性值、设置节点的属性值、删除节点的属性。</p>
<p>我们就统一拿下面这个标签来举例：</p>
<pre><code class="copyable"><img src="images/1.jpg" class="image-box" title="美女图片" alt="地铁一瞥" id="a1">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面分别介绍。</p>
<p>1、获取节点的属性值</p>
<p>方式1：</p>
<pre><code class="copyable">元素节点.属性;
元素节点[属性];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举例：（获取节点的属性值）</p>
<pre><code class="copyable"><body>
<img src="images/1.jpg" class="image-box" title="美女图片" alt="地铁一瞥" id="a1">

<script type="text/javascript">
    var myNode = document.getElementsByTagName("img")[0];

    console.log(myNode.src);
    console.log(myNode.className);    //注意，是className，不是class
    console.log(myNode.title);

    console.log("------------");

    console.log(myNode["src"]);
    console.log(myNode["className"]); //注意，是className，不是class
    console.log(myNode["title"]);
</script>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方式2：（推荐）</p>
<p>素节点.getAttribute("属性名称");
例子：</p>
<pre><code class="copyable">console.log(myNode.getAttribute("src"));
console.log(myNode.getAttribute("class"));   //注意是class，不是className
console.log(myNode.getAttribute("title"));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方式1和方式2的区别在于：前者是直接操作标签，后者是把标签作为DOM节点。推荐方式2。</p>
<p>2、设置节点的属性值</p>
<p>方式1举例：（设置节点的属性值）</p>
<pre><code class="copyable">myNode.src = "images/2.jpg"   //修改src的属性值
myNode.className = "image2-box";  //修改class的name
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方式2：（推荐）</p>
<p>元素节点.setAttribute(属性名, 新的属性值);
方式2举例：（设置节点的属性值）</p>
<pre><code class="copyable">myNode.setAttribute("src","images/3.jpg");
myNode.setAttribute("class","image3-box");
myNode.setAttribute("id","你好");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、删除节点的属性</p>
<p>格式：</p>
<pre><code class="copyable">元素节点.removeAttribute(属性名);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举例：（删除节点的属性）</p>
<pre><code class="copyable">myNode.removeAttribute("class");
myNode.removeAttribute("id");
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://juejin.cn/post/url">原文链接</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75cb99115d414d9689c1e2c8f629bea2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            