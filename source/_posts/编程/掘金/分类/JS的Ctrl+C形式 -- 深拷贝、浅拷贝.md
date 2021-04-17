
---
title: 'JS的Ctrl+C形式 -- 深拷贝、浅拷贝'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22d9f544500d46fbaca283d944f6a31c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 16 Apr 2021 17:36:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22d9f544500d46fbaca283d944f6a31c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在讨论深拷贝和浅拷贝的之前，我们先来了解一下简单简单类型和复杂类型</p>
<h1 data-id="heading-0">1、简单类型和复杂类型</h1>
<p>简单类型又叫基本数据类型或值类型，复杂类型又叫做引用类型</p>
<ol>
<li>
<p>简单数据类型：<strong>在存储变量中存储的是值的本身</strong>，因此叫做值类型</p>
</li>
<li>
<p>引用类型：<strong>在存储变量中存储的仅仅是地址（引用）</strong>，因此叫做引用类型</p>
</li>
</ol>
<p>我们前面说过，js包括了6种基本类型（<code>Number</code>、<code>String</code>、<code>Boolean</code>、<code>Undefined</code>、<code>Null</code>、<code>Symbol</code>）和1种引用类型（<code>Object</code>）</p>
<ul>
<li><strong>基本类型没有属性</strong></li>
<li><strong>基本类型的初始化只能使用字面量形式</strong></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 虽然基本类型没有属性，但是为它添加属性并不会报错</span>
<span class="hljs-keyword">let</span> namer = <span class="hljs-string">'王五'</span>
namer.age = <span class="hljs-number">2</span>
<span class="hljs-built_in">console</span>.log(namer.age);  <span class="hljs-comment">// undefined</span>

<span class="hljs-comment">// 使用new就会创建一个对象</span>
<span class="hljs-keyword">let</span> namer1 = <span class="hljs-string">'张三'</span>
<span class="hljs-keyword">let</span> namer2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">'李四'</span>)

<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> namer1); <span class="hljs-comment">// string</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> namer2); <span class="hljs-comment">// object</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">堆和栈</h2>
<p>堆栈空间分配的区别：</p>
<ol>
<li>栈：<strong>基本数据类型就是存放在栈里面</strong>，由系统空间自动分配释放函数的参数值、局部变量的值等；</li>
<li>堆：<strong>引用类型就是存储在堆里面</strong>，一般由程序员分配释放或由垃圾收机制回收（js就是由垃圾会收器回收的）</li>
</ol>
<p>引用类型变量存储的是一个地址，真正的对象实例存储在堆空间中</p>
<p><img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22d9f544500d46fbaca283d944f6a31c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">2、深拷贝 和 浅拷贝</h1>
<p>我们都知道了，对象就是存储现在堆中，以变量-值这样的形式来存储，内容存储在堆中，通过引用进行访问，其中引用表示存储在栈中；而基本数据类型就存储在栈中</p>
<p><strong>深拷贝：复制对象的实例</strong>，相当于在内存开辟一个新的地址来存储这个变量，所以，修改某个对象，跟另一个变量半毛钱关系都没有，你走你的阳关道，我过我的独木桥</p>
<img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4be109a62ff4aa8a99f422620cfba85~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p><strong>浅拷贝：直接复制对象的地址</strong>，复制之后两个对象指向同一个地址。所以修改任何一个对象，由于他们指向同一个对象，所以另一个变量也会跟着改变</p>
<img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/592435e0f9b54b229effd38aed338356~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>我们可以使用 <code>===</code> 来判断深浅拷贝</p>
<ol>
<li>浅拷贝：由于来自同一个地址，返回 <code>true</code></li>
<li>深拷贝：来自不同的地址，返回<code>false</code></li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj1 = &#123; <span class="hljs-attr">namer</span>: <span class="hljs-string">'张三'</span> &#125;
<span class="hljs-keyword">let</span> obj2 = obj1
obj2.namer = <span class="hljs-string">'李四'</span>

<span class="hljs-built_in">console</span>.log(obj1); <span class="hljs-comment">// &#123; namer: '张三' &#125;</span>
<span class="hljs-built_in">console</span>.log(obj2); <span class="hljs-comment">// &#123; namer: '张三' &#125;</span>
<span class="hljs-built_in">console</span>.log(obj1 === obj2); <span class="hljs-comment">// true</span>


<span class="hljs-keyword">let</span> arr1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
<span class="hljs-keyword">let</span> arr2 = arr1
arr1[<span class="hljs-number">0</span>] = <span class="hljs-string">'张三'</span>

<span class="hljs-built_in">console</span>.log(arr1);  <span class="hljs-comment">// [ '张三', 2, 3 ]</span>
<span class="hljs-built_in">console</span>.log(arr2);  <span class="hljs-comment">// [ '张三', 2, 3 ]</span>
<span class="hljs-built_in">console</span>.log(arr1 === arr2); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见对象之间直接赋值的方式就是浅拷贝</p>
<p>我们一般复制的语法有这几种：<code>...</code>、<code>slice</code>、<code>concat</code>、<code>Object.assign</code>、<code>JSON.stringify</code></p>
<h1 data-id="heading-3">3、数组拷贝 <code>slice</code>、<code>concat</code></h1>
<p>数组的两个方法：<code>slice</code>（截取）、<code>concat</code>（拼接），本质上就是一种复制</p>
<p><strong><code>slice</code></strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-string">'张三'</span>]
<span class="hljs-keyword">let</span> arr2 = arr1.slice()
arr2[<span class="hljs-number">2</span>] = <span class="hljs-string">'李四'</span>

<span class="hljs-built_in">console</span>.log(arr1); <span class="hljs-comment">//  [1, 2, '张三']</span>
<span class="hljs-built_in">console</span>.log(arr2); <span class="hljs-comment">//  [1, 2, '李四']</span>
<span class="hljs-built_in">console</span>.log(arr1 === arr2); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>concat()</code></strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-string">'张三'</span>]
<span class="hljs-comment">// 拼接，不传入参数的时候，返回原数组</span>
<span class="hljs-keyword">let</span> arr2 = arr1.concat();
arr2[<span class="hljs-number">2</span>] = <span class="hljs-string">'李四'</span>
<span class="hljs-built_in">console</span>.log(arr1); <span class="hljs-comment">//  [1, 2, '张三']</span>
<span class="hljs-built_in">console</span>.log(arr2); <span class="hljs-comment">//  [1, 2, '李四']</span>
<span class="hljs-built_in">console</span>.log(arr1 === arr2); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显这两种复制方式方式都是深复制</p>
<p>但是将它们还有另外一个特点，请看下面：</p>
<p><strong><code>slice</code></strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-string">'张三'</span>, [<span class="hljs-string">'1'</span>, <span class="hljs-string">'2'</span>]]
<span class="hljs-keyword">let</span> arr2 = arr1.slice()
arr2[<span class="hljs-number">3</span>][<span class="hljs-number">1</span>] = <span class="hljs-string">'李四'</span>

<span class="hljs-built_in">console</span>.log(arr1);  <span class="hljs-comment">// [ 1, 2, '张三', [ '1', '李四' ] ]</span>
<span class="hljs-built_in">console</span>.log(arr2);  <span class="hljs-comment">// [ 1, 2, '张三', [ '1', '李四' ] ]</span>
<span class="hljs-built_in">console</span>.log(arr1 === arr2); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>concat</code></strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-string">'张三'</span>, [<span class="hljs-string">'1'</span>, <span class="hljs-string">'2'</span>]]
<span class="hljs-keyword">let</span> arr2 = arr1.concat()
arr2[<span class="hljs-number">3</span>][<span class="hljs-number">1</span>] = <span class="hljs-string">'李四'</span>

<span class="hljs-built_in">console</span>.log(arr1); <span class="hljs-comment">// [ 1, 2, '张三', [ '1', '李四' ] ]</span>
<span class="hljs-built_in">console</span>.log(arr2); <span class="hljs-comment">// [ 1, 2, '张三', [ '1', '李四' ] ]</span>
<span class="hljs-built_in">console</span>.log(arr1 === arr2); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看出，当数组的属性为应用类型的时候，这两种复制方式对于引用类型其实是浅拷贝，拷贝之后，应用类型的指针还是指向同一个存储地址</p>
<h2 data-id="heading-4">总结：</h2>
<ol>
<li><strong><code>slice</code>、<code>concat</code> 可用于数组的拷贝</strong></li>
<li><strong>当拷贝的数组元素都是基本类型的时候，<code>slice</code>、<code>concat</code>进行的是深拷贝</strong></li>
<li><strong>当拷贝的数组元素有引用类型的时候，对引用类型的拷贝是浅拷贝，基本类型仍然是深拷贝</strong></li>
<li><strong>所以，<code>slice</code>、<code>concat</code>仅适用于拷贝不包含引用类型的数组</strong></li>
</ol>
<h1 data-id="heading-5">4、对象拷贝<code>...</code>、<code>Object.assign</code></h1>
<p><strong><code>...</code></strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 复制数组</span>
<span class="hljs-keyword">let</span> arr1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-string">'张三'</span>, [<span class="hljs-string">'1'</span>]]
<span class="hljs-keyword">let</span> arr2 = [...arr1]
arr1[<span class="hljs-number">2</span>] = <span class="hljs-string">'李四'</span>
arr1[<span class="hljs-number">3</span>][<span class="hljs-number">0</span>] = <span class="hljs-string">'张三不是李四'</span>

<span class="hljs-built_in">console</span>.log(arr1); <span class="hljs-comment">// [ 1, 2, '李四', [ '张三不是李四' ] ]</span>
<span class="hljs-built_in">console</span>.log(arr2); <span class="hljs-comment">// [ 1, 2, '张三', [ '张三不是李四' ] ]</span>
<span class="hljs-built_in">console</span>.log(arr1 === arr2); <span class="hljs-comment">// false</span>


<span class="hljs-comment">// 复制对象</span>
<span class="hljs-keyword">let</span> obj1 = &#123; <span class="hljs-attr">namer</span>: <span class="hljs-string">'张三'</span>, <span class="hljs-attr">hobby</span>: [<span class="hljs-string">'螺蛳粉'</span>] &#125;
<span class="hljs-keyword">let</span> obj2 = &#123;...obj1 &#125;
obj2.namer = <span class="hljs-string">'李四'</span>
obj2.hobby[<span class="hljs-number">0</span>] = <span class="hljs-string">'牛肉果条'</span>

<span class="hljs-built_in">console</span>.log(obj1); <span class="hljs-comment">// &#123; namer: '张三', hobby: [ '牛肉果条' ] &#125;</span>
<span class="hljs-built_in">console</span>.log(obj2); <span class="hljs-comment">// &#123; namer: '李四', hobby: [ '牛肉果条' ] &#125;</span>
<span class="hljs-built_in">console</span>.log(obj1 === obj2); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>ES6新增的拷贝语法：<code>Object.assign</code></strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 拷贝数组</span>
<span class="hljs-keyword">let</span> arr1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-string">'张三'</span>, [<span class="hljs-string">'1'</span>]]
<span class="hljs-keyword">let</span> arr2 = []
<span class="hljs-built_in">Object</span>.assign(arr2, arr1)
arr1[<span class="hljs-number">2</span>] = <span class="hljs-string">'李四'</span>
arr1[<span class="hljs-number">3</span>][<span class="hljs-number">0</span>] = <span class="hljs-string">'张三不是李四'</span>

<span class="hljs-built_in">console</span>.log(arr1);  <span class="hljs-comment">// [ 1, 2, '李四', [ '张三不是李四' ] ]</span>
<span class="hljs-built_in">console</span>.log(arr2);  <span class="hljs-comment">// [ 1, 2, '张三', [ '张三不是李四' ] ]</span>
<span class="hljs-built_in">console</span>.log(arr1 === arr2); <span class="hljs-comment">// false</span>


<span class="hljs-comment">// 拷贝对象</span>
<span class="hljs-keyword">let</span> obj = &#123; <span class="hljs-attr">namer</span>: <span class="hljs-string">'张三'</span>, <span class="hljs-attr">hobby</span>: [<span class="hljs-string">'螺蛳粉'</span>] &#125;
<span class="hljs-keyword">let</span> copyObj = &#123;&#125;
<span class="hljs-comment">// 拷贝</span>
<span class="hljs-built_in">Object</span>.assign(copyObj, obj)
<span class="hljs-built_in">console</span>.log(copyObj); <span class="hljs-comment">// &#123; namer: '张三', hobby: ['螺蛳粉'] &#125;</span>

copyObj.namer = <span class="hljs-string">'李四'</span>
obj.hobby[<span class="hljs-number">0</span>] = <span class="hljs-string">'牛肉果条'</span>
<span class="hljs-built_in">console</span>.log(obj);  <span class="hljs-comment">// &#123; namer: '张三', hobby: [ '牛肉果条' ] &#125;</span>
<span class="hljs-built_in">console</span>.log(copyObj);  <span class="hljs-comment">// &#123; namer: '李四', hobby: [ '牛肉果条' ] &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<ol>
<li><strong><code>...</code> 和 <code>Object.assign</code> 可用于拷贝对象，，它们的拷贝特性还是跟<code>slice</code> 和 <code>concat</code> 一样</strong></li>
<li><strong>对象的值是基本类型，进行深拷贝；值是引用类型进行浅拷贝</strong></li>
</ol>
<h1 data-id="heading-6">5、<code>JSON.stringify</code></h1>
<p><code>JSON.stringify()</code> 就是目前开发中最常用的深拷贝方式，它的原理就是把对象转化成字符串保存在内存中，然后再利用 <code>JSON.parse()</code> 将字符串转化成一个新的对象</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123; <span class="hljs-attr">namer</span>: <span class="hljs-string">'张三'</span>, <span class="hljs-attr">hobby</span>: [<span class="hljs-string">'螺蛳粉'</span>] &#125;

<span class="hljs-keyword">let</span> obj1 = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(obj))
<span class="hljs-built_in">console</span>.log(obj1);  <span class="hljs-comment">//  &#123; namer: '张三', hobby: [ '螺蛳粉' ] &#125;</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> obj1); <span class="hljs-comment">// object</span>

obj1.hobby[<span class="hljs-number">0</span>] = <span class="hljs-string">'牛肉果条'</span>
<span class="hljs-built_in">console</span>.log(obj);  <span class="hljs-comment">// &#123; namer: '张三', hobby: [ '螺蛳粉' ] &#125;</span>
<span class="hljs-built_in">console</span>.log(obj1);  <span class="hljs-comment">// &#123; namer: '张三', hobby: [ '牛肉果条' ] &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            