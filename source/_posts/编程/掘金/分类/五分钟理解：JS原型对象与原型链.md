
---
title: '五分钟理解：JS原型对象与原型链'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37bb8c05529549feaa1600a6708c067f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 02:13:17 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37bb8c05529549feaa1600a6708c067f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、原型对象和原型链到底是什么？</h1>
<p>要知道原型对象就得先了解在JS中什么是对象：<strong>JavaScript 对象是被命名值的容器</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 这段代码将一个单一值vehicle赋给car这个变量</span>
<span class="hljs-keyword">let</span> car = <span class="hljs-string">"vehicle"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象也是变量。但是对象包含很多值：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 这段代码把多个值（vehicle, hongqi, black）赋给名为 car 的变量：</span>
<span class="hljs-keyword">let</span> car = &#123;<span class="hljs-attr">type</span>:<span class="hljs-string">"vehicle"</span>, <span class="hljs-attr">model</span>:<span class="hljs-string">"hongqi"</span>, <span class="hljs-attr">color</span>:<span class="hljs-string">"black"</span>&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>搞清楚什么是对象之后我们继续聊，在此处我想引用一段<strong>MDN文档</strong>里的定义：<br>
JavaScript 常被描述为一种基于原型的语言 (prototype-based language)——<strong>每个对象拥有一个原型对象</strong>，对象以其原型为模板、从原型继承方法和属性。原型对象也可能拥有原型，并从中继承方法和属性，一层一层、以此类推。这种<strong>关系</strong>常被称为<strong>原型链 (prototype chain)</strong>，它解释了为何一个对象会拥有定义在其他对象中的属性和方法。</p>
<h1 data-id="heading-1">二、通过一个简单的小栗子来说明它们的关系</h1>
<p><strong>首先应该理解两个概念</strong>：</p>
<ol>
<li>JS中的对象都内置了__proto__属性，但是只有函数对象内置了prototype属性</li>
<li>以下包含Object和Function以及Data、Math、Array、String、Number、Boolean、RegExp在内的函数都是<strong>JS的内置函数</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Animal</span>(<span class="hljs-params">name, age</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.age = age;
  &#125;;
  <span class="hljs-built_in">console</span>.log(Animal.prototype);
  <span class="hljs-comment">// 在原型对象上定义公共方法say</span>
  Animal.prototype.say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'say'</span>);
  &#125;
  <span class="hljs-comment">// 实例化一个对象ani</span>
  <span class="hljs-keyword">let</span> ani = <span class="hljs-keyword">new</span> Animal(<span class="hljs-string">'xiaobai'</span>, <span class="hljs-number">8</span>);
  <span class="hljs-keyword">let</span> ani1 = <span class="hljs-keyword">new</span> Animal();
  <span class="hljs-keyword">let</span> ani2 = <span class="hljs-keyword">new</span> Animal();
  <span class="hljs-built_in">console</span>.log(ani);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37bb8c05529549feaa1600a6708c067f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到：对象Animal的原型对象Animal.prototype内置的prototype属性内<strong>包含</strong>constructor属性和__proto__属性</p>
<ul>
<li>值得注意的是constructor指向定义的函数对象Animal</li>
<li>函数对象也通过prototype与它的原型对象关联起来了</li>
</ul>
<p>那么现在读者可能有一个疑问：实例化出来的对象ani怎么与函数原型对象来进行关联呢，还记得刚才说的__proto__吧，那么就是通过它来找到函数原型对象了。我们当然可以不止实例化一个对象，如果有需要，我们可以实例化1个、2个甚至100个对象。这么多对象都可以通过__proto__来找到函数原型对象，这也就可以理解为所谓的原型链了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b932ec94cc94841bfddc873579f26b7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里就是我们ani打印出来的结果了</p>
<hr>
<p>至此，我们可以通过一张图来小小地总结一下原型对象和原型链的概念与联系<br>
在这里还有一个点是我刚才没说的，原型链的终点就是Object.prototype,原型对象一层一层地指向直至指到它为止，而Object.prototype指向Null</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fac5e53a4d6417b94e367ad43f93c4c~tplv-k3u1fbpfcp-watermark.image" alt="原型链.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">三、结语</h1>
<p>本文也只是简略地谈了一下原型对象和原型链相关的概念，里面还有很多内容无法一次说完，本人也是前端小白，如有不妥希望大佬给予指导，感谢！</p></div>  
</div>
            