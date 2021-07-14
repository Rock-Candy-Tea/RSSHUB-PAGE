
---
title: 'JS原型和原型链'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/553bd3d594a244dc8e0de29e2e03150a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 20:48:16 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/553bd3d594a244dc8e0de29e2e03150a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>原型是JavaScript中一个比较难理解的概念， 为深入理解JavaScript 中的原型、原型链，整理下思路。</p>
</blockquote>
<p>原型是 JavaScript 中一个比较难理解的概念，原型相关的属性也比较多，对象有 <code>prototype</code> 属性，函数对象有 <code>prototype</code> 属性，原型对象有 <code>constructor</code> 属性。</p>
<h3 data-id="heading-0">一、初识原型</h3>
<p>在 JavaScript 中，原型也是一个对象，通过原型可以实现对象的属性继承，JavaScript 的对象中都包含了一个 <code>prototype</code> 内部属性，这个属性所对应的就是该对象的原型。
  prototype 作为对象的内部属性，是不能被直接访问的。所以为了方便查看一个对象的原型，Firefox和Chrome中提供了<code>__proto__</code>这个非标准（不是所有浏览器都支持）的访问器（ECMA引入了标准对象原型访问器 Object.getPrototype(object)）。在 JavaScript 的原型对象中，还包含一个 <code>constructor</code> 属性，这个属性对应创建所有指向该原型的实例的构造函数。</p>
<h3 data-id="heading-1">二、规则</h3>
<p>在 JavaScript 中，每个函数都有一个 <code>prototype</code> 属性，当一个函数被用作构造函数来创建实例时，这个函数的 <code>prototype</code> 属性值会被作为原型赋值给所有对象实例（也就是设置 实例的<code>__proto__</code>属性），也就是说，所有实例的原型引用的是函数的 prototype 属性。(只有函数对象才会有这个属性!)</p>
<blockquote>
<p>上面说这么多，大家肯定还不了解什么是原型、原型链。原型（prototype）既然是对象的一个属性，那我们就从对象开始理解。</p>
</blockquote>
<h3 data-id="heading-2">三、Object 与 Function</h3>
<p>先来看 Object 到底是什么，在浏览器的控制台输出</p>
<pre><code class="copyable">console.log(Object);
console.log(Object(&#123;&#125;));
console.log(new Object);
//输出的结果
//function Object() &#123; [native code] &#125;
//Object &#123;&#125;
//Object &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  Object 对象本身是一个函数对象。既然是Object函数，就肯定会有 <code>prototype</code> 属性，所以可以看到 Object.prototype 的值就是 Object &#123;&#125; 这个原型对象。反过来，当访问 Object.prototype 对象的 <code>constructor</code> 这个属性的时候，就得到了Obejct函数。
<br>  另外，当通过 Object.prototype.__ proto__ 获取Object原型的原型的时候，将会得到 null，也就是说 Object &#123;&#125; 原型对象就是原型链的终点了。<br>
  然后我们来看 Object.prototype 的输出结果，可以看到 Object &#123;&#125; 原型对象里并没有 __ proto __ 这个属性。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/553bd3d594a244dc8e0de29e2e03150a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>  Function — JavaScript 中函数也是对象，所以就可以通过__proto__查找到构造函数对象的原型。<br>
  Object 对象本身是一个已经定义好的函数对象。那我们自己定义一个 people 对象，看看它的原型（people.prototype）输出结果有何不同。</p>
<pre><code class="copyable">var people=function(name,age)&#123;
  this.name=name,
  this.age=age
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2dcd1e47f5b443d38a79399c11682439~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有 constructor 属性说明 people 对象是原型对象，people.<strong>proto</strong> 获取到的就是 Object 对象。<br>
  然后我们为 people 构建一个实例化对象 student ，进行一些输出。</p>
<pre><code class="copyable">var student=new people;
console.log(people.prototype);
console.log(student.__proto__);
console.log(student.__proto__.__proto__);
console.log(student.prototype);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e029f7465424b84a945ce2cf28e492e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>people.prototype</code> 和 <code>student.__proto__</code> 的输出结果相同可以得出 —— <code>people.prototype</code> === <code>student.__proto__</code>。
  函数对象可以通过 函数对象.prototype 得到它的原型对象，实例化对象.__ proto__ 也可以得到它的原型对象。
  <code>prototype</code> 作为对象的内部属性，是不能被直接访问的，因此我们可以通过对象的 __ proto__ 属性得到对应的对象原型。</p>
<h3 data-id="heading-3">四、原型链</h3>
<p>理解原型链：<br>
  原型链的基本思想是利用原型让一个引用类型继承另一个引用类型的属性和方法。
  因为每个对象和原型都有原型，对象的原型指向原型对象，而父的原型又指向父的父，这种原型层层连接起来的就构成了原型链。</p>
<p>简单回顾下构造函数、原型和实例的关系：<br>
  每个构造函数都有一个原型对象，原型对象包含一个指向构造函数的指针（prototype），而实例则包含一个指向原型对象的内部指针（__ proto__）。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62ba806acdab49abba797b680bd87a3f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
原型链的问题：<br>
  虽然很强大，可以用它来实现继承，但它也存在一些问题。最主要的问题来自包含引用类型值的原型。在通过原型来实现继承时，原型实际上会变成一个类型的实例。于是，原先的实例属性也顺理成章的变成了现在的原型的属性了。</p>
<p>例如</p>
<pre><code class="copyable">student.__proto__.add=function()&#123;
    return sex="女"
&#125;
console.log(student.__proto__);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c413b70caa024cc9b3d15f75a7686b14~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>  原先的原型对象并中没有 add 这个函数，但是通过 __ proto__ 给 student 对象添加 add 函数后，people 对象的原型中就有了add 函数。</p>
<h3 data-id="heading-4">总结：</h3>
<ol>
<li>所有的对象都有 __ proto__ 属性，该属性对应该对象的原型；</li>
<li>所有的函数对象都有 prototype 属性，该属性的值会被赋值给该函数创建的对 象的 __ proto__属性；</li>
<li>所有的对象可以通过不断使用 __ proto__ 属性找到 Object.prototype ；</li>
<li>所有的原型对象都有<code>constructor</code>属性，该属性对应创建所有指向该原型的实例的构造函数；</li>
<li>函数对象和原型对象通过<code>prototype</code>和<code>constructor</code>属性进行相互关联。</li>
</ol></div>  
</div>
            