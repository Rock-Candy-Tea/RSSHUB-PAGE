
---
title: '从原型链出发，看看 Class 被编译成了什么样子'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4c37f0f37af4899943eeb58a20a7147~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 09:11:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4c37f0f37af4899943eeb58a20a7147~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文从 JavaScript 继承中，最核心的原型链出发，介绍了在 ES5 和 ES6 中一些实现继承的方式，及其背后的原理。
<a name="user-content-56SeP" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-0">原型链</h2>
<p><a name="user-content-9YKdH" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-1">基于原型的语言</h3>
<p>JavaScript 常被描述为一种<strong>基于原型的语言 (prototype-based language)</strong>——每个对象拥有一个<strong>原型对象</strong>，对象以其原型为模板、从原型继承方法和属性。原型对象也可能拥有原型，并从中继承方法和属性，一层一层、以此类推。这种关系常被称为<strong>原型链 (prototype chain)</strong>，它解释了为何一个对象会拥有定义在其他对象中的属性和方法。<br>准确地说，这些属性和方法定义在Object的构造器函数(constructor functions)之上的<code>prototype</code>属性上，而非对象实例本身。<br>在 JavaScript 中是在对象实例和它的构造器之间建立一个链接（它是<code>__proto__</code>属性，是从构造函数的<code>prototype</code>属性派生的），之后通过上溯原型链，在构造器中找到这些属性和方法。</p>
<blockquote>
<p>理解对象的原型（可以通过<code>Object.getPrototypeOf(obj)</code>或者已被弃用的<code>__proto__</code>属性获得）与构造函数的<code>prototype</code>属性之间的区别是很重要的。**前者是每个实例上都有的属性，后者是构造函数的属性。**也就是说，<code>Object.getPrototypeOf(new Foobar()) === Foobar.prototype</code></p>
</blockquote>
<p><a name="user-content-1gWBg" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-2">和基于类的语言的区别</h4>
<p>在传统的 OOP 中，首先定义“类”，此后创建对象实例时，类中定义的所有属性和方法都被<strong>复制</strong>到实例中。但是在 JavaScript 是如上文说的通过引用的方式在原型链上<strong>寻找</strong>对应的方法或属性，所以这种可能更应该被称为<strong>委托</strong>。
<a name="user-content-CzD3I" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-3">核心图解(基础)</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4c37f0f37af4899943eeb58a20a7147~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>我们先祭出简单版本的图，并以几个关键问题阐述</p>
<ul>
<li>函数的 <code>prototype</code> 属性指向了一个对象，这个对象是调用该 <strong>构造函数</strong> 创建的实例的 <strong>原型</strong>（所以叫实例原型）</li>
<li>实例对象有一个 <code>__proto__</code> 属性，指向他的<strong>原型</strong></li>
<li>每一个实例原型都有一个 <code>constructor</code> 属性指向关联的 <strong>构造函数</strong></li>
</ul>
<p><a name="user-content-uVi8B" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-4">为什么有的对象有 <code>prototype</code> 有的没有</h4>
<p>JavaScript 分为<strong>函数对象</strong>和<strong>普通对象</strong>，每个对象都有 <code>__proto__</code> 属性，但是只有函数对象才有 <code>prototype</code> 属性
<a name="user-content-ONXHR" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-5">JavaScript 是如何访问原型链上的属性或方法的</h4>
<p>在调用继承自 <code>Object</code> 的 <code>Person</code> 的 <code>person</code> 上的 <code>valueOf</code> 方法时(<code>person.valueOf()</code>)，会发生以下过程：</p>
<ul>
<li>浏览器首先检查，<code>person</code> 对象是否具有可用的 <code>valueOf()</code> 方法。</li>
<li>如果没有，则浏览器检查 <code>person</code> 对象的原型对象（即 <code>Person</code>构造函数的 <code>prototype</code> 属性所指向的对象）是否具有可用的 <code>valueof()</code> 方法。</li>
<li>如果也没有，则浏览器检查 <code>Person()</code> 构造函数的prototype属性所指向的对象的原型对象（即 <code>Object</code>构造函数的prototype属性所指向的对象）是否具有可用的 <code>valueOf()</code> 方法。这里有这个方法，于是该方法被调用。</li>
</ul>
<p><a name="user-content-kSwCN" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-6">为什么 <code>person.constructor === Person</code> ？</h4>
<p>首先，我们需要知道 实例原型（即 <code>Person.prototype</code> ）的 <code>constructor</code> 指向构造函数本身<br>从图里我们会发现， <code>person</code> 上并没有 <code>constructor</code> 属性，那为什么问题里的判等成立呢？——因为访问 <code>person.``constructor</code> 时，发现属性不存在， 则会从 <code>person</code> 的原型也就是 <code>Person.prototype</code> 中读取，这个时候能访问到，因此：<br><code>person.constructor === Person.prototype.constructor</code>
<a name="user-content-9ge9A" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-7">核心图解(进阶)</h3>
<p><br><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd1319d4ec6f4985b2f1539ae25cf720~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>接下来我们换一张复杂一些的，加上了 <code>Function</code> ，变得复杂了起来。
<a name="user-content-GGD83" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-8">原型链的顶端是什么</h4>
<ul>
<li><code>Object.prototype</code> 是原型链的 root ，它指向了 <code>null</code> （<code>Object.prototype === null</code>）</li>
</ul>
<p><a name="user-content-7onlZ" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-9">Object 和 Function</h4>
<ul>
<li>对于 Function 而言
<ul>
<li><code>Function.prototype.__proto__ === Object.prototype</code> 这里 Function 和 Object 的联系建立了起来 —— <strong>函数是一个对象</strong></li>
<li><code>Object.__proto__-> Function.prototype</code> <strong>Object 是一个函数（构造函数）</strong></li>
<li><code>Function.__proto__ === Function.prototype</code> 这里是 Function 和其他人都不一样的地方。而查找的时候，则会从 <code>Function.prototype</code> 查到 <code>Object.prototype</code> 走完原型链</li>
</ul>
</li>
<li>对于 Object
<ul>
<li>这里解释了为什么 <code>Object.prototype.valueOf === Object.valueOf</code> ，为什么 Object 上可以直接访问到 Object.prototype 上的属性，而当 Person 却不能直接访问 <code>Person.prototype</code> 上的属性 —— <code>Object.__proto__-> Function.prototype</code></li>
</ul>
</li>
</ul>
<p><code>Function.prototype.__proto__->Object.prototype</code>
<a name="user-content-dG1yy" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-10">鸡蛋问题</h4>
<ul>
<li>到底是先有鸡还是先有蛋？现有 <code>Object</code> 还是先有 <code>Function</code> ？
<ul>
<li><code>Object instanceof Function === true</code></li>
<li><code>Function instanceof Object === true</code></li>
</ul>
</li>
<li>核心：<code>Object.prototype.__proto__ === null</code>，人为规定了最开始的 <code>rootPrototype</code>，所以可以认为是先有 <code>Object</code></li>
</ul>
<p><a name="user-content-gjSgp" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-11">ES5 中的继承</h2>
<p>上文简单阐述了 JavaScript 中原型链的机制，下面我们来说说基于这种机制，如何实现继承
<a name="user-content-Ytw0l" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-12">原型链继承</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 父</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'foo'</span>;
&#125;
<span class="hljs-comment">// 在原型链上添加方法</span>
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
&#125;
<span class="hljs-comment">// 子</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params"></span>) </span>&#123;

&#125;
Child.prototype = <span class="hljs-keyword">new</span> Parent();

<span class="hljs-keyword">const</span> child1 = <span class="hljs-keyword">new</span> Child();
<span class="hljs-built_in">console</span>.log(child1.getName()) <span class="hljs-comment">// foo</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最简单的继承</p>
<ul>
<li>缺点：
<ul>
<li>引用类型的属性被所有实例共享
<ul>
<li>即，修改原型链上的引用类型属性时，会影响到所有 Child</li>
</ul>
</li>
<li>在创建 Child 的实例时，不能向 Parent 传参</li>
</ul>
</li>
</ul>
<p><a name="user-content-vRmKb" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-13">借用构造函数继承</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 父</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params">names</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.names = names;
&#125;
<span class="hljs-comment">// 子</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params">names</span>) </span>&#123;
  Parent.call(<span class="hljs-built_in">this</span>, names);
&#125;


<span class="hljs-keyword">const</span> child1 = <span class="hljs-keyword">new</span> Child([]);
child1.names.push(<span class="hljs-string">'test'</span>);
<span class="hljs-built_in">console</span>.log(child1.names); <span class="hljs-comment">// ["test"]</span>

<span class="hljs-keyword">const</span> child2 = <span class="hljs-keyword">new</span> Child([]);
<span class="hljs-built_in">console</span>.log(child2.names); <span class="hljs-comment">// []</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>优点
<ul>
<li>避免了引用类型的属性被所有实例共享</li>
<li>可以在 Child 中向 Parent 传参</li>
</ul>
</li>
<li>缺点：
<ul>
<li>方法都在构造函数中定义，每次创建实例都会创建一遍方法。</li>
</ul>
</li>
</ul>
<p><a name="user-content-ijMXN" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-14">组合继承【常用】</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 父</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-built_in">this</span>.colors = [<span class="hljs-string">'red'</span>, <span class="hljs-string">'blue'</span>, <span class="hljs-string">'green'</span>];
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-comment">// 子</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params">name, age</span>) </span>&#123;
  <span class="hljs-comment">// 执行 Parent 的构造函数</span>
  Parent.call(<span class="hljs-built_in">this</span>, name);
  <span class="hljs-built_in">this</span>.age = age;
&#125;
<span class="hljs-comment">// 修改 prototype 到父元素实例。以便让子元素实例通过 __proto__ 使用父元素属性</span>
<span class="hljs-comment">// 但是多执行了一次 Parent 的构造函数</span>
Child.prototype = <span class="hljs-keyword">new</span> Parent();
<span class="hljs-comment">// 修正 constructor 以保证 child.constructor === Child</span>
Child.prototype.constructor = Child;

<span class="hljs-keyword">const</span> child1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'foo'</span>, <span class="hljs-string">'18'</span>);
child1.colors.push(<span class="hljs-string">'black'</span>);
<span class="hljs-built_in">console</span>.log(child1.name); <span class="hljs-comment">// foo</span>
<span class="hljs-built_in">console</span>.log(child1.age); <span class="hljs-comment">// 18</span>
<span class="hljs-built_in">console</span>.log(child1.colors); <span class="hljs-comment">// ["red", "blue", "green", "black"]</span>

<span class="hljs-keyword">const</span> child2 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'bar'</span>, <span class="hljs-string">'20'</span>);
<span class="hljs-built_in">console</span>.log(child2.name); <span class="hljs-comment">// bar</span>
<span class="hljs-built_in">console</span>.log(child2.age); <span class="hljs-comment">// 20</span>
<span class="hljs-built_in">console</span>.log(child2.colors); <span class="hljs-comment">// ["red", "blue", "green"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>缺点
<ul>
<li>会调用两次父构造函数，导致 <code>prototype</code> 和 实例上有重复的属性</li>
</ul>
</li>
</ul>
<p><a name="user-content-Ds4LO" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-15">原型式继承</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createObj</span>(<span class="hljs-params">o</span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
  F.prototype = o;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> F();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是 ES5 Object.create 的模拟实现，将传入的对象作为创建的对象的原型。</p>
<ul>
<li>缺点
<ul>
<li>包含引用类型的属性值始终都会共享相应的值，这点跟原型链继承一样</li>
</ul>
</li>
</ul>
<p><a name="user-content-br637" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-16">寄生式继承</h3>
<p>创建一个仅用于封装继承过程的函数，该函数在内部以某种形式来做增强对象，最后返回对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createObj</span> (<span class="hljs-params">o</span>) </span>&#123;
  <span class="hljs-keyword">const</span> clone = <span class="hljs-built_in">Object</span>.create(o);
  clone.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hi'</span>);
  &#125;
  <span class="hljs-keyword">return</span> clone;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>缺点
<ul>
<li>跟借用构造函数模式一样，每次创建对象都会创建一遍方法。</li>
</ul>
</li>
</ul>
<p><a name="user-content-N7gqA" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-17">寄生组合式继承【常用】</h3>
<p>核心：不使用 <code>Child.prototype = new Parent()</code> ，而是间接的让 <code>Child.prototype</code> 访问到 <code>Parent.prototype</code> ，少一次调用 <code>Child</code> 的构造函数<br>之前是通过构造函数，来创建 <code>__proto__</code> 的指向，而现在我们改进后，直接修改 Child 的 <code>prototype</code> 指向 Parent 的 <code>prototype </code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 代码封装</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">object</span>(<span class="hljs-params">o</span>) </span>&#123;
  <span class="hljs-comment">// 使用一个“干净”的函数，没有执行 Parent 的构造函数</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
  F.prototype = o;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> F();
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">prototype</span>(<span class="hljs-params">child, parent</span>) </span>&#123;
  <span class="hljs-keyword">const</span> prototype = object(parent.prototype);
  <span class="hljs-comment">// 修正 consturctor</span>
  prototype.constructor = child;
  <span class="hljs-comment">// 本质上约等于 child.prototype.__proto__ = parent.prototype</span>
  child.prototype = prototype;
&#125;

<span class="hljs-comment">// 业务代码</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-built_in">this</span>.colors = [<span class="hljs-string">'red'</span>, <span class="hljs-string">'blue'</span>, <span class="hljs-string">'green'</span>];
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params">name, age</span>) </span>&#123;
  Parent.call(<span class="hljs-built_in">this</span>, name);
  <span class="hljs-built_in">this</span>.age = age;
&#125;

<span class="hljs-comment">// 当我们使用的时候：</span>
prototype(Child, Parent);
<span class="hljs-keyword">const</span> child1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'foo'</span>, <span class="hljs-string">'18'</span>);
<span class="hljs-built_in">console</span>.log(child1);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>优点
<ul>
<li>只调用了一次 Parent 构造函数</li>
<li><code>prototype</code> 上没有有重复的属性</li>
<li>原型链还能保持不变，能够正常使用 instanceof 和 isPrototypeOf</li>
</ul>
</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d6eb0c8cad24af1a8bb72bc3ebb8448~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>上述代码关系如图
<a name="user-content-ossgV" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-18">继承静态方法</h3>
<p>我们前面讲的所有的继承方法，都没有实现构造函数上的静态方法继承，然而在ES6的 <code>class</code> 中，子类是可以继承父类的静态方法的。<br>
<br>我们可以通过 <code>Object.setPrototypeOf()</code> 方法实现静态方法的继承。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">prototype</span>(<span class="hljs-params">child, parent</span>) </span>&#123;
  <span class="hljs-keyword">const</span> prototype = <span class="hljs-built_in">Object</span>.create(parent.prototype);
  <span class="hljs-comment">// 修正 consturctor</span>
  prototype.constructor = child;
  <span class="hljs-comment">// 即 child.prototype.__proto__ = parent.prototype</span>
  child.prototype = prototype;
&#125;

<span class="hljs-comment">// 业务代码</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-built_in">this</span>.colors = [<span class="hljs-string">'red'</span>, <span class="hljs-string">'blue'</span>, <span class="hljs-string">'green'</span>];
&#125;
<span class="hljs-comment">// 静态方法</span>
Parent.staticFn = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"Parent"</span>;
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params">name, age</span>) </span>&#123;
  Parent.call(<span class="hljs-built_in">this</span>, name);
  <span class="hljs-built_in">this</span>.age = age;
&#125;
<span class="hljs-comment">// 继承静态方法</span>
<span class="hljs-built_in">Object</span>.setPrototypeOf(Child, Parent);

<span class="hljs-comment">// 当我们使用的时候：</span>
prototype(Child, Parent);
<span class="hljs-keyword">const</span> child1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'foo'</span>, <span class="hljs-string">'18'</span>);
<span class="hljs-built_in">console</span>.log(child1);
Child.staticFn()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-rpit8" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-19">扩展 - <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/create" target="_blank" rel="nofollow noopener noreferrer">Object.create()</a></h3>
<p><code>Object.create()</code> 方法创建一个新对象，使用现有的对象来提供新创建的对象的 <code>__proto__</code>。 也就是说，新创建一个对象，这个对象的 <code>__proto__</code> 指向了一个现有对象
<a name="user-content-hFtPZ" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-20">参数</h4>
<p><code>Object.create(proto，[propertiesObject])</code></p>
<ul>
<li><code>proto</code> 新创建对象的原型对象。</li>
<li><code>propertiesObject</code> 【可选】需要传入一个对象，该对象的属性类型参照<code>Object.defineProperties()</code>的第二个参数（即 数据描述符 - <code>configurable</code>、<code>enumerable</code>、<code>value</code>、<code>writable </code>和 访问器描述符 - <code>get</code>、<code>set</code>）。如果该参数被指定且不为 <code>undefined</code>，该传入对象的<strong>自有可枚举属性</strong>(即其自身定义的属性，而不是其原型链上的枚举属性)将为新创建的对象添加指定的属性值和对应的属性描述符。</li>
</ul>
<p><a name="user-content-ESbfU" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-21">使用场景</h4>
<ul>
<li>在需要实例原型，但不需要执行构造函数的时候（比如寄生组合继承）
<ul>
<li><code>o = new Constructor()</code> 和 <code>o = Object.create(Constructor.prototype)</code> 的区别就在于，后者没有执行构造函数</li>
</ul>
</li>
<li>创建一个纯净的对象
<ul>
<li>Object.create(null)</li>
</ul>
</li>
</ul>
<p><a name="user-content-cqoTZ" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-22">Polyfill</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Object</span>.create = <span class="hljs-function">(<span class="hljs-params">proto, propertiesObject</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> proto !== <span class="hljs-string">'object'</span> && <span class="hljs-keyword">typeof</span> proto !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Object prototype may only be an Object: '</span> + proto);
  &#125;
  <span class="hljs-keyword">if</span> (propertiesObject === <span class="hljs-literal">null</span>) <span class="hljs-keyword">throw</span> <span class="hljs-string">'TypeError'</span>
  
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span> (<span class="hljs-params"></span>) </span>&#123;&#125;
  F.prototype = proto
  <span class="hljs-keyword">const</span> o = <span class="hljs-keyword">new</span> F()
  
  <span class="hljs-comment">// 添加属性</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> propertiesObject !== <span class="hljs-string">'undefined'</span>) &#123;
    <span class="hljs-built_in">Object</span>.defineProperties(o, propertiesObject)
  &#125;
  <span class="hljs-comment">// 如果 proto 为 null,需要去除 __proto__</span>
  <span class="hljs-keyword">if</span> (proto === <span class="hljs-literal">null</span>) o.__proto__ = <span class="hljs-literal">null</span>
  <span class="hljs-comment">// 返回新的对象</span>
  <span class="hljs-keyword">return</span> o
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-oJc1u" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-23">扩展 - <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf" target="_blank" rel="nofollow noopener noreferrer">Object.setPrototypeOf()</a></h3>
<p>设置一个指定的对象的原型 ( 即, 内部<code>[[Prototype]]</code>属性，也就是 <code>__proto__</code>）到另一个对象或  <code>null</code>。<br>
<br>和 <code>Object.create</code> 的微小区别</p>
<ul>
<li><code>Object.create</code> 是新创建一个对象，这个对象的 <code>__proto__</code> 指向了一个现有对象</li>
<li><code>Object.setPrototypeOf()</code> 是 设置一个指定的对象的原型</li>
</ul>
<p>也就是说，<code>Object.create</code> 会多一层对象<br></p>
<p><a name="user-content-CEND6" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-24">参数</h4>
<p><code>Object.setPrototypeOf(obj, prototype)</code></p>
<ul>
<li><code>obj</code> 要设置其原型的对象。</li>
<li><code>prototype</code> 该对象的新原型(一个对象 或 <code>null</code>).</li>
</ul>
<p><a name="user-content-X6ipD" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-25">使用场景</h4>
<ol>
<li>继承静态方法
<ol>
<li>如上文</li>
</ol>
</li>
</ol>
<p><a name="user-content-859TF" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-26">Polyfill</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Object</span>.prototype.setPrototypeOf = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">obj, proto</span>) </span>&#123;
  <span class="hljs-keyword">if</span>(obj.__proto__) &#123;
    obj.__proto__ = proto;
    <span class="hljs-keyword">return</span> obj;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 如果你想返回 prototype of Object.create(null):</span>
    <span class="hljs-keyword">const</span> Fn = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> obj) &#123;
        <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">this</span>, key, &#123;
          <span class="hljs-attr">value</span>: obj[key],
        &#125;);
      &#125;
    &#125;;
    Fn.prototype = proto;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Fn();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-tchwf" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-27">ES6 中的继承 - Class 语法糖</h2>
<p>ES6 中新增了 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Classes" target="_blank" rel="nofollow noopener noreferrer">Class</a>，使得实现继承得到了简化。我们先来看简单看基础<br></p>
<p><a name="user-content-FpaUB" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-28">类表达式 和 类声明</h3>
<p>实际上，类是“特殊的函数”，就像你能够定义的函数表达式和函数声明一样，类语法有两个组成部分：<strong>类表达式</strong>和<strong>类声明</strong>。</p>
<ul>
<li>类声明：定义类的一种方法是使用类声明。要声明一个类，你可以使用带有class关键字的类名</li>
<li>类表达式：类表达式可以命名或不命名。命名类表达式的名称是该类体的局部名称。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 类声明</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Rectangle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">height, width</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.height = height;
    <span class="hljs-built_in">this</span>.width = width;
  &#125;
&#125;
<span class="hljs-comment">// 类表达式 - 匿名类</span>
<span class="hljs-keyword">let</span> Rectangle = <span class="hljs-class"><span class="hljs-keyword">class</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">height, width</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.height = height;
    <span class="hljs-built_in">this</span>.width = width;
  &#125;
&#125;;
<span class="hljs-comment">// 类表达式 - 命名类</span>
<span class="hljs-keyword">let</span> Rectangle = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Rectangle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">height, width</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.height = height;
    <span class="hljs-built_in">this</span>.width = width;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-QkzQW" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-29"><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Classes/Public_class_fields" target="_blank" rel="nofollow noopener noreferrer">类体和方法定义</a></h3>
<p>类元素拥有以下几种属性</p>
<ul>
<li>构造函数：<code>constructor</code> 方法是一个特殊的方法，这种方法用于创建和初始化一个由 <code>class</code> 创建的对象
<ul>
<li>注意：类的内部所有定义的方法，都是不可枚举的，也就是说</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// class</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
&#125;
<span class="hljs-comment">// ES5</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>原型方法
<ul>
<li>注意：类的内部所有定义的方法，都是不可枚举的</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// class</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'hello, I am '</span> + <span class="hljs-built_in">this</span>.name;
  &#125;
&#125;
<span class="hljs-built_in">Object</span>.keys(Person.prototype); <span class="hljs-comment">// []</span>
<span class="hljs-built_in">Object</span>.getOwnPropertyNames(Person.prototype); <span class="hljs-comment">// ["constructor", "sayHello"]</span>

<span class="hljs-comment">// ES5</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
&#125;
Person.prototype.sayHello = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">'hello, I am '</span> + <span class="hljs-built_in">this</span>.name;
&#125;;
<span class="hljs-built_in">Object</span>.keys(Person.prototype); <span class="hljs-comment">// ['sayHello']</span>
<span class="hljs-built_in">Object</span>.getOwnPropertyNames(Person.prototype); <span class="hljs-comment">// ["constructor", "sayHello"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>静态方法：<code>static</code> 关键字用来定义一个类的一个静态方法。调用静态方法不需要实例化该类，但不能通过一个类实例调用静态方法。类比 ES5 中定义在构造函数对象上的方法。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// class</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'hello'</span>;
  &#125;
&#125;
Person.sayHello() <span class="hljs-comment">// 'hello'</span>
<span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">new</span> Person();
foo.sayHello(); <span class="hljs-comment">// TypeError: foo.sayHello is not a function</span>

<span class="hljs-comment">// ES5</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-comment">// 不在原型链上</span>
Person.sayHello = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'hello'</span>;
&#125;;
Person.sayHello(); <span class="hljs-comment">// 'hello'</span>
<span class="hljs-keyword">var</span> foo = <span class="hljs-keyword">new</span> Person();
kevin.sayHello(); <span class="hljs-comment">// TypeError: foo.sayHello is not a function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>实例属性
<ul>
<li>实例的属性必须定义在类的方法里。（但是有一个 <a href="https://github.com/tc39/proposal-class-fields#field-declarations" target="_blank" rel="nofollow noopener noreferrer">Stag 3的提案</a> 可以直接写在类里面）</li>
<li>静态的或原型的数据属性必须定义在类定义的外面。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// class</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;;
  &#125;
&#125;
<span class="hljs-comment">// 新的 Field declarations</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  state = &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
  &#125;;
&#125;
<span class="hljs-comment">// ES5</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.state = &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>静态属性
<ul>
<li>静态公有字段在你想要创建一个只在每个类里面只存在一份，而不会存在于你创建的每个类的实例中的属性时可以用到。静态公有字段不会在子类里重复初始化</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// class</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-keyword">static</span> name = <span class="hljs-string">'foo'</span>;
&#125;

<span class="hljs-comment">// ES5</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;;
Person.name = <span class="hljs-string">'foo'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>getter</code> 和 <code>setter</code>
<ul>
<li>与 ES5 一样，在“类”的内部可以使用 get 和 set 关键字，对某个属性设置存值函数和取值函数，拦截该属性的存取行为</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// class</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-keyword">get</span> <span class="hljs-title">name</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'bar'</span>;
  &#125;
  <span class="hljs-keyword">set</span> <span class="hljs-title">name</span>(<span class="hljs-params">newName</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'new name 为：'</span> + newName)
  &#125;
&#125;
<span class="hljs-keyword">let</span> person = <span class="hljs-keyword">new</span> Person();
person.name = <span class="hljs-string">'foo'</span>;
<span class="hljs-comment">// new name 为：foo</span>
<span class="hljs-built_in">console</span>.log(person.name);
<span class="hljs-comment">// bar</span>

<span class="hljs-comment">// ES5</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;&#125;
Person.prototype = &#123;
  <span class="hljs-keyword">get</span> <span class="hljs-title">name</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'bar'</span>;
  &#125;,
  <span class="hljs-keyword">set</span> <span class="hljs-title">name</span>(<span class="hljs-params">newName</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'new name 为：'</span> + newName)
  &#125;
&#125;
<span class="hljs-keyword">let</span> person = <span class="hljs-keyword">new</span> Person();
person.name = <span class="hljs-string">'foo'</span>;
<span class="hljs-comment">// new name 为：foo</span>
<span class="hljs-built_in">console</span>.log(person.name);
<span class="hljs-comment">// bar</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>私有属性/方法
<ul>
<li>在属性/方法前加上 <code>#</code> 即可让其成为私有的，<code>#</code>是名称的一部分，也用于访问和声明。</li>
<li>私有字段仅能在字段声明中预先定义，不能通过在之后赋值来创建它们</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Rectangle</span> </span>&#123;
  #height = <span class="hljs-number">0</span>;
  #width;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">height, width</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.#height = height;
    <span class="hljs-built_in">this</span>.#width = width;
  &#125;
<span class="hljs-keyword">static</span> #<span class="hljs-function"><span class="hljs-title">privateStaticMethod</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">42</span>;
  &#125;
&#125;
<span class="hljs-comment">// 这个在自己实现起来很恶心，可以使用 闭包/Symbol/WeakMap 实现，暂且不详细叙述</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-srvTw" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-30">Babel是如何编译你的 Class 的</h3>
<p>下文编译均来自 <a href="https://babeljs.io/repl" target="_blank" rel="nofollow noopener noreferrer">babel try it out</a>
<a name="user-content-qyf9d" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-31">只有构造函数</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Input</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
&#125;
<span class="hljs-comment">// Output</span>
<span class="hljs-meta">"use strict"</span>;
<span class="hljs-comment">// 在环境支持与不支持Symbol的情况做了区分</span>
<span class="hljs-comment">// 在 Symbol 存在的环境下，left instanceof right 实际上是 right[Symbol.hasInstance](left)，同时可以在类的内部去覆写这个方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_instanceof</span>(<span class="hljs-params">left, right</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (right != <span class="hljs-literal">null</span> && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> !== <span class="hljs-string">"undefined"</span> && right[<span class="hljs-built_in">Symbol</span>.hasInstance]) &#123;
    <span class="hljs-keyword">return</span> !!right[<span class="hljs-built_in">Symbol</span>.hasInstance](left);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> left <span class="hljs-keyword">instanceof</span> right;
  &#125;
&#125;
<span class="hljs-comment">// _classCallCheck 的作用是检查 Person 是否是通过 new 的方式调用，类必须使用 new 调用，否则会报错。</span>
<span class="hljs-comment">// 当我们使用 var person = Person() 的形式调用的时候，this 指向 window，所以 instance instanceof Constructor 就会为 false，与 ES6 的要求一致。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_classCallCheck</span>(<span class="hljs-params">instance, Constructor</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!_instanceof(instance, Constructor)) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Cannot call a class as a function"</span>);
  &#125;
&#125;
<span class="hljs-keyword">var</span> Person = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
  _classCallCheck(<span class="hljs-built_in">this</span>, Person);
  <span class="hljs-built_in">this</span>.name = name;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-Zz52z" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-32">实例属性，静态属性，私有属性</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Input</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-comment">// 实例属性</span>
  foo = <span class="hljs-string">'foo'</span>;
<span class="hljs-comment">// 静态属性</span>
<span class="hljs-keyword">static</span> bar = <span class="hljs-string">'bar'</span>;
<span class="hljs-comment">// 私有属性</span>
#test = <span class="hljs-string">'test'</span>;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
&#125;
<span class="hljs-comment">// Output</span>
<span class="hljs-meta">"use strict"</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_instanceof</span>(<span class="hljs-params">left, right</span>) </span>&#123; <span class="hljs-keyword">if</span> (right != <span class="hljs-literal">null</span> && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> !== <span class="hljs-string">"undefined"</span> && right[<span class="hljs-built_in">Symbol</span>.hasInstance]) &#123; <span class="hljs-keyword">return</span> !!right[<span class="hljs-built_in">Symbol</span>.hasInstance](left); &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-keyword">return</span> left <span class="hljs-keyword">instanceof</span> right; &#125; &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_classCallCheck</span>(<span class="hljs-params">instance, Constructor</span>) </span>&#123; <span class="hljs-keyword">if</span> (!_instanceof(instance, Constructor)) &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Cannot call a class as a function"</span>); &#125; &#125;
<span class="hljs-comment">// defineProperty 修改/设置属性</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_defineProperty</span>(<span class="hljs-params">obj, key, value</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> obj) &#123;
    <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
      <span class="hljs-attr">value</span>: value,
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>
    &#125;);
  &#125; <span class="hljs-keyword">else</span> &#123;
    obj[key] = value;
  &#125;
  <span class="hljs-keyword">return</span> obj;
&#125;
<span class="hljs-comment">// 通过 weakMap 实现私有变量，详见下文扩展</span>
<span class="hljs-keyword">var</span> _test = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();
<span class="hljs-keyword">var</span> Person = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
  _classCallCheck(<span class="hljs-built_in">this</span>, Person);
  _defineProperty(<span class="hljs-built_in">this</span>, <span class="hljs-string">"foo"</span>, <span class="hljs-string">'foo'</span>);
  _test.set(<span class="hljs-built_in">this</span>, &#123;
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">value</span>: <span class="hljs-string">'test'</span>
  &#125;);
  <span class="hljs-built_in">this</span>.name = name;
&#125;;
_defineProperty(Person, <span class="hljs-string">"bar"</span>, <span class="hljs-string">'bar'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以清楚的发现：</p>
<ul>
<li>实例属性通过 <code>defineProperty</code> 在构造函数中设置到了实例上</li>
<li>静态属性 <code>defineProperty</code>  在构造函数外设置到了构造函数上</li>
<li>私有属性 和 实例属性/静态属性 是独立的，通过 weakMap 实现</li>
</ul>
<p><a name="user-content-SNXBg" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-33">实例方法，静态方法，私有方法，getter/setter</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Input</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  #hello = <span class="hljs-string">'hello'</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'hello, I am '</span> + <span class="hljs-built_in">this</span>.#privateSayHello();
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">onlySayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'hello'</span>;
  &#125;
  #<span class="hljs-function"><span class="hljs-title">privateSayHello</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.#hello;
  &#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">name</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'foo'</span>;
  &#125;
  <span class="hljs-keyword">set</span> <span class="hljs-title">name</span>(<span class="hljs-params">newName</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'new name 为：'</span> + newName);
  &#125;
&#125;
<span class="hljs-comment">// Output</span>
<span class="hljs-meta">"use strict"</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_instanceof</span>(<span class="hljs-params">left, right</span>) </span>&#123; <span class="hljs-keyword">if</span> (right != <span class="hljs-literal">null</span> && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> !== <span class="hljs-string">"undefined"</span> && right[<span class="hljs-built_in">Symbol</span>.hasInstance]) &#123; <span class="hljs-keyword">return</span> !!right[<span class="hljs-built_in">Symbol</span>.hasInstance](left); &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-keyword">return</span> left <span class="hljs-keyword">instanceof</span> right; &#125; &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_classCallCheck</span>(<span class="hljs-params">instance, Constructor</span>) </span>&#123; <span class="hljs-keyword">if</span> (!_instanceof(instance, Constructor)) &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Cannot call a class as a function"</span>); &#125; &#125;
<span class="hljs-comment">// 1. 会把设置的值变成不可枚举的，符合上文规范中要求的【类的内部所有定义的方法，都是不可枚举的】</span>
<span class="hljs-comment">// 2. 对于 getter setter，需要设置成不可写的，进来就是没有 value 字段</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_defineProperties</span>(<span class="hljs-params">target, props</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < props.length; i++) &#123;
    <span class="hljs-keyword">var</span> descriptor = props[i];
    descriptor.enumerable = descriptor.enumerable || <span class="hljs-literal">false</span>;
    descriptor.configurable = <span class="hljs-literal">true</span>;
    <span class="hljs-keyword">if</span> (<span class="hljs-string">"value"</span> <span class="hljs-keyword">in</span> descriptor) descriptor.writable = <span class="hljs-literal">true</span>;
    <span class="hljs-built_in">Object</span>.defineProperty(target, descriptor.key, descriptor);
  &#125;
&#125;
<span class="hljs-comment">// 将实例方法添加到原型链上，将静态方法添加到构造函数上</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_createClass</span>(<span class="hljs-params">Constructor, protoProps, staticProps</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (protoProps) _defineProperties(Constructor.prototype, protoProps);
    <span class="hljs-keyword">if</span> (staticProps) _defineProperties(Constructor, staticProps);
    <span class="hljs-keyword">return</span> Constructor;
&#125;

<span class="hljs-comment">// 以下三个为获取私有属性用</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_classPrivateFieldGet</span>(<span class="hljs-params">receiver, privateMap</span>) </span>&#123;
    <span class="hljs-keyword">var</span> descriptor = _classExtractFieldDescriptor(receiver, privateMap, <span class="hljs-string">"get"</span>);
    <span class="hljs-keyword">return</span> _classApplyDescriptorGet(receiver, descriptor);
&#125;
<span class="hljs-comment">// 保护调用，获得 weakMap 里通过构造函数绑定的方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_classExtractFieldDescriptor</span>(<span class="hljs-params">receiver, privateMap, action</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!privateMap.has(receiver)) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"attempted to "</span> + action + <span class="hljs-string">" private field on non-instance"</span>);
    &#125;
    <span class="hljs-keyword">return</span> privateMap.get(receiver);
&#125;
<span class="hljs-comment">// 调用方法，获得私有属性的值</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_classApplyDescriptorGet</span>(<span class="hljs-params">receiver, descriptor</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (descriptor.get) &#123;
        <span class="hljs-keyword">return</span> descriptor.get.call(receiver);
    &#125;
    <span class="hljs-keyword">return</span> descriptor.value;
&#125;

<span class="hljs-comment">// 调用私有方法用</span>
<span class="hljs-comment">// 调用时，检查是否有这个 weakmap 在实例上，有则执行对应方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_classPrivateMethodGet</span>(<span class="hljs-params">receiver, privateSet, fn</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!privateSet.has(receiver)) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"attempted to get private field on non-instance"</span>);
    &#125;
    <span class="hljs-keyword">return</span> fn;
&#125;

<span class="hljs-keyword">var</span> _hello = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();
<span class="hljs-keyword">var</span> _privateSayHello = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakSet</span>();
<span class="hljs-keyword">var</span> Person = <span class="hljs-comment">/*#__PURE__*/</span><span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
    _classCallCheck(<span class="hljs-built_in">this</span>, Person);
    _privateSayHello.add(<span class="hljs-built_in">this</span>);
    <span class="hljs-comment">// 设置私有属性的值</span>
    _hello.set(<span class="hljs-built_in">this</span>, &#123;
      <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">value</span>: <span class="hljs-string">'hello'</span>
    &#125;);
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
  <span class="hljs-comment">// 第一个参数是构造函数，二个参数是实例方法，第三个参数是静态方法</span>
  _createClass(Person, [&#123;
    <span class="hljs-attr">key</span>: <span class="hljs-string">"sayHello"</span>,
    <span class="hljs-attr">value</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'hello, I am '</span> + _classPrivateMethodGet(<span class="hljs-built_in">this</span>, _privateSayHello, _privateSayHello2).call(<span class="hljs-built_in">this</span>);
    &#125;
  &#125;, &#123;
    <span class="hljs-attr">key</span>: <span class="hljs-string">"name"</span>,
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'foo'</span>;
    &#125;,
    <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">set</span>(<span class="hljs-params">newName</span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'new name 为：'</span> + newName);
    &#125;
  &#125;], [&#123;
    <span class="hljs-attr">key</span>: <span class="hljs-string">"onlySayHello"</span>,
    <span class="hljs-attr">value</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onlySayHello</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'hello'</span>;
    &#125;
  &#125;]);
  <span class="hljs-keyword">return</span> Person;
&#125;();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_privateSayHello2</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> _classPrivateFieldGet(<span class="hljs-built_in">this</span>, _hello);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意的几点</p>
<ul>
<li>在设置方法时，会把设置的值变成不可枚举的，符合上文规范中要求的【类的内部所有定义的方法，都是不可枚举的】</li>
<li>对于 <code>getter/setter</code> ，是不可写的</li>
<li>私有方法也是靠 <code>weakMap</code> 实现，不过方法被定义到了构造函数外，通过构造函数和 <code>weakMap</code> 链接，同时需要注意私有方法和私有变量取值不一样之处</li>
</ul>
<p><a name="user-content-pYUIn" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-34">Babel是如何让你通过 Class 继承的</h3>
<p>上面我们看了一下 Class 中各种各样的属性、方法会被编译成什么样子，接下来我们看看是如何用他们实现继承的
<a name="user-content-tCUQv" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-35">只有构造函数</h4>
<p>注意，在子类的 <code>constructor</code> 里要使用 <code>this</code> 的话，必须调用一次父类的构造函数，也就是 <code>super()</code> （类似 ES5 中的 <code>Parent.call(this)</code> ）。这是因为子类没有自己的 <code>this</code> 对象，而是继承父类的 <code>this</code> 对象，然后对其进行加工。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Input - 寄生组合式继承</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name);
    <span class="hljs-built_in">this</span>.age = age;
  &#125;
&#125;
<span class="hljs-keyword">const</span> child1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'foo'</span>, <span class="hljs-string">'18'</span>);

<span class="hljs-comment">// Output</span>
<span class="hljs-meta">"use strict"</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_typeof</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-string">"@babel/helpers - typeof"</span>;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> === <span class="hljs-string">"function"</span> && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span>.iterator === <span class="hljs-string">"symbol"</span>) &#123;
    _typeof = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_typeof</span>(<span class="hljs-params">obj</span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> obj;
    &#125;;
  &#125; <span class="hljs-keyword">else</span> &#123;
    _typeof = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_typeof</span>(<span class="hljs-params">obj</span>) </span>&#123;
      <span class="hljs-keyword">return</span> obj && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> === <span class="hljs-string">"function"</span> && obj.constructor === <span class="hljs-built_in">Symbol</span> && obj !== <span class="hljs-built_in">Symbol</span>.prototype ? <span class="hljs-string">"symbol"</span> : <span class="hljs-keyword">typeof</span> obj;
    &#125;;
  &#125;
  <span class="hljs-keyword">return</span> _typeof(obj);
&#125;
<span class="hljs-comment">// 重点，继承的核心</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_inherits</span>(<span class="hljs-params">subClass, superClass</span>) </span>&#123;
  <span class="hljs-comment">// extend 的继承目标必须是函数或者是 null</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> superClass !== <span class="hljs-string">"function"</span> && superClass !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Super expression must either be null or a function"</span>);
  &#125;
  <span class="hljs-comment">// 类似于 ES5 的寄生组合式继承，使用 Object.create，设置子类 prototype 属性的 __proto__ 属性指向父类的 prototype 属性</span>
  subClass.prototype = <span class="hljs-built_in">Object</span>.create(superClass && superClass.prototype, &#123;
    <span class="hljs-attr">constructor</span>: &#123;
      <span class="hljs-attr">value</span>: subClass,
      <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;);
  <span class="hljs-comment">// 设置子类的 __proto__ 属性指向父类，这样能让子类访问到父类上的静态方法</span>
  <span class="hljs-keyword">if</span> (superClass) _setPrototypeOf(subClass, superClass);
&#125;
<span class="hljs-comment">// 工具方法，设置一个对象的 __proto__</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_setPrototypeOf</span>(<span class="hljs-params">o, p</span>) </span>&#123;
  _setPrototypeOf = <span class="hljs-built_in">Object</span>.setPrototypeOf || <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_setPrototypeOf</span>(<span class="hljs-params">o, p</span>) </span>&#123;
    o.__proto__ = p;
    <span class="hljs-keyword">return</span> o;
  &#125;;
  <span class="hljs-keyword">return</span> _setPrototypeOf(o, p);
&#125;
<span class="hljs-comment">// 创建一个 super，来调用父元素构造函数，主要是处理其返回类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_createSuper</span>(<span class="hljs-params">Derived</span>) </span>&#123;
  <span class="hljs-keyword">var</span> hasNativeReflectConstruct = _isNativeReflectConstruct();
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_createSuperInternal</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 获取原型，也就是Parent（在之前已经完成了继承）</span>
    <span class="hljs-keyword">var</span> Super = _getPrototypeOf(Derived),
        result;
    <span class="hljs-keyword">if</span> (hasNativeReflectConstruct) &#123;
      <span class="hljs-comment">// 有 Reflect 就走高端方案</span>
      <span class="hljs-comment">// 作为新创建对象的原型对象的 constructor 属性</span>
      <span class="hljs-keyword">var</span> NewTarget = _getPrototypeOf(<span class="hljs-built_in">this</span>).constructor;
      result = <span class="hljs-built_in">Reflect</span>.construct(Super, <span class="hljs-built_in">arguments</span>, NewTarget);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 没有 Reflect 的环境就当成构造函数调用一下</span>
      result = Super.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
    &#125;
    <span class="hljs-comment">// 检查返回值</span>
    <span class="hljs-keyword">return</span> _possibleConstructorReturn(<span class="hljs-built_in">this</span>, result);
  &#125;;
&#125;
<span class="hljs-comment">// 用于处理构造函数返回值——规范允许在构造函数内主动返回一个 对象、方法，否则则返回构造函数内的 this</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_possibleConstructorReturn</span>(<span class="hljs-params">self, call</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (call && (_typeof(call) === <span class="hljs-string">"object"</span> || <span class="hljs-keyword">typeof</span> call === <span class="hljs-string">"function"</span>)) &#123;
    <span class="hljs-keyword">return</span> call;
  &#125;
  <span class="hljs-keyword">return</span> _assertThisInitialized(self);
&#125;
<span class="hljs-comment">// 工具方法，判断 this 是不是存在</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_assertThisInitialized</span>(<span class="hljs-params">self</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (self === <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">ReferenceError</span>(<span class="hljs-string">"this hasn't been initialised - super() hasn't been called"</span>);
  &#125;
  <span class="hljs-keyword">return</span> self;
&#125;
<span class="hljs-comment">// 工具方法，是否支持原生的 Reflect</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_isNativeReflectConstruct</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Reflect</span> === <span class="hljs-string">"undefined"</span> || !<span class="hljs-built_in">Reflect</span>.construct) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Reflect</span>.construct.sham) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Proxy</span> === <span class="hljs-string">"function"</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-built_in">Boolean</span>.prototype.valueOf.call(<span class="hljs-built_in">Reflect</span>.construct(<span class="hljs-built_in">Boolean</span>, [], <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;));
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
&#125;
<span class="hljs-comment">// 工具方法，返回指定对象的原型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_getPrototypeOf</span>(<span class="hljs-params">o</span>) </span>&#123;
  _getPrototypeOf = <span class="hljs-built_in">Object</span>.setPrototypeOf ? <span class="hljs-built_in">Object</span>.getPrototypeOf : <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_getPrototypeOf</span>(<span class="hljs-params">o</span>) </span>&#123;
    <span class="hljs-keyword">return</span> o.__proto__ || <span class="hljs-built_in">Object</span>.getPrototypeOf(o);
  &#125;;
  <span class="hljs-keyword">return</span> _getPrototypeOf(o);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_instanceof</span>(<span class="hljs-params">left, right</span>) </span>&#123; <span class="hljs-keyword">if</span> (right != <span class="hljs-literal">null</span> && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> !== <span class="hljs-string">"undefined"</span> && right[<span class="hljs-built_in">Symbol</span>.hasInstance]) &#123; <span class="hljs-keyword">return</span> !!right[<span class="hljs-built_in">Symbol</span>.hasInstance](left); &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-keyword">return</span> left <span class="hljs-keyword">instanceof</span> right; &#125; &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_classCallCheck</span>(<span class="hljs-params">instance, Constructor</span>) </span>&#123; <span class="hljs-keyword">if</span> (!_instanceof(instance, Constructor)) &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Cannot call a class as a function"</span>); &#125; &#125;

<span class="hljs-keyword">var</span> Parent = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">name</span>) </span>&#123;
  _classCallCheck(<span class="hljs-built_in">this</span>, Parent);
  <span class="hljs-built_in">this</span>.name = name;
&#125;;

<span class="hljs-keyword">var</span> Child = <span class="hljs-comment">/*#__PURE__*/</span><span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_Parent</span>) </span>&#123;
  <span class="hljs-comment">// 继承原型链</span>
  _inherits(Child, _Parent);
  <span class="hljs-comment">// 创建一个super</span>
  <span class="hljs-keyword">var</span> _super = _createSuper(Child);
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">name, age</span>) </span>&#123;
    <span class="hljs-keyword">var</span> _this;
    _classCallCheck(<span class="hljs-built_in">this</span>, Child);
    <span class="hljs-comment">// 调用 super，拿到 this</span>
    _this = _super.call(<span class="hljs-built_in">this</span>, name);
    _this.age = age;
    <span class="hljs-keyword">return</span> _this;
  &#125;
  <span class="hljs-keyword">return</span> Child;
&#125;(Parent);

<span class="hljs-keyword">var</span> child1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'foo'</span>, <span class="hljs-string">'18'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这块最核心的其实就两个：如何处理 <code>super</code> 和如何处理继承：</p>
<ul>
<li>如何处理继承
<ul>
<li>防御性处理，extend 的继承目标必须是函数或者是 null</li>
<li>继承的核心和 ES5 的寄生组合式继承类似，使用 <code>create</code> 完成</li>
<li>ES6中基于 Class 的继承，子类能继承父类的静态方法，所以需要让子类的 <code>__proto__</code> 指向父类</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 重点，继承的核心</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_inherits</span>(<span class="hljs-params">subClass, superClass</span>) </span>&#123;
  <span class="hljs-comment">// extend 的继承目标必须是函数或者是 null</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> superClass !== <span class="hljs-string">"function"</span> && superClass !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Super expression must either be null or a function"</span>);
  &#125;
  <span class="hljs-comment">// 类似于 ES5 的寄生组合式继承，使用 Object.create，设置子类 prototype 属性的 __proto__ 属性指向父类的 prototype 属性</span>
  subClass.prototype = <span class="hljs-built_in">Object</span>.create(superClass && superClass.prototype, &#123;
    <span class="hljs-attr">constructor</span>: &#123;
      <span class="hljs-attr">value</span>: subClass,
      <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;);
  <span class="hljs-comment">// 设置子类的 __proto__ 属性指向父类，这样能让子类访问到父类上的静态方法</span>
  <span class="hljs-keyword">if</span> (superClass) _setPrototypeOf(subClass, superClass);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如何处理 <code>super</code>
<ul>
<li>本质上，<code>super</code> 类似于  <code>Parent.call(this)</code></li>
<li>需要注意的是额外处理了返回值</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建一个 super，来调用父元素构造函数，主要是处理其返回类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_createSuper</span>(<span class="hljs-params">Derived</span>) </span>&#123;
  <span class="hljs-keyword">var</span> hasNativeReflectConstruct = _isNativeReflectConstruct();
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_createSuperInternal</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 获取原型，也就是Parent（在之前已经完成了继承）</span>
    <span class="hljs-keyword">var</span> Super = _getPrototypeOf(Derived),
        result;
    <span class="hljs-keyword">if</span> (hasNativeReflectConstruct) &#123;
      <span class="hljs-comment">// 有 Reflect 就走高端方案</span>
      <span class="hljs-comment">// 作为新创建对象的原型对象的 constructor 属性</span>
      <span class="hljs-keyword">var</span> NewTarget = _getPrototypeOf(<span class="hljs-built_in">this</span>).constructor;
      result = <span class="hljs-built_in">Reflect</span>.construct(Super, <span class="hljs-built_in">arguments</span>, NewTarget);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 没有 Reflect 的环境就当成构造函数调用一下</span>
      result = Super.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
    &#125;
    <span class="hljs-comment">// 检查返回值</span>
    <span class="hljs-keyword">return</span> _possibleConstructorReturn(<span class="hljs-built_in">this</span>, result);
  &#125;;
&#125;
<span class="hljs-comment">// 用于处理构造函数返回值——规范允许在构造函数内主动返回一个 对象、方法，否则则返回构造函数内的 this</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_possibleConstructorReturn</span>(<span class="hljs-params">self, call</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (call && (_typeof(call) === <span class="hljs-string">"object"</span> || <span class="hljs-keyword">typeof</span> call === <span class="hljs-string">"function"</span>)) &#123;
    <span class="hljs-keyword">return</span> call;
  &#125;
  <span class="hljs-keyword">return</span> _assertThisInitialized(self);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-QGsn6" href="https://juejin.cn/post/undefined"></a></p>
<h4 data-id="heading-36">继承自内建对象</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Input</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Array</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(value);
  &#125;
&#125;
<span class="hljs-keyword">const</span> child1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-number">1</span>);
<span class="hljs-comment">// Output</span>
<span class="hljs-meta">"use strict"</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_instanceof</span>(<span class="hljs-params">left, right</span>) </span>&#123; <span class="hljs-keyword">if</span> (right != <span class="hljs-literal">null</span> && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> !== <span class="hljs-string">"undefined"</span> && right[<span class="hljs-built_in">Symbol</span>.hasInstance]) &#123; <span class="hljs-keyword">return</span> !!right[<span class="hljs-built_in">Symbol</span>.hasInstance](left); &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-keyword">return</span> left <span class="hljs-keyword">instanceof</span> right; &#125; &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_typeof</span>(<span class="hljs-params">obj</span>) </span>&#123; <span class="hljs-string">"@babel/helpers - typeof"</span>; <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> === <span class="hljs-string">"function"</span> && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span>.iterator === <span class="hljs-string">"symbol"</span>) &#123; _typeof = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_typeof</span>(<span class="hljs-params">obj</span>) </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> obj; &#125;; &#125; <span class="hljs-keyword">else</span> &#123; _typeof = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_typeof</span>(<span class="hljs-params">obj</span>) </span>&#123; <span class="hljs-keyword">return</span> obj && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> === <span class="hljs-string">"function"</span> && obj.constructor === <span class="hljs-built_in">Symbol</span> && obj !== <span class="hljs-built_in">Symbol</span>.prototype ? <span class="hljs-string">"symbol"</span> : <span class="hljs-keyword">typeof</span> obj; &#125;; &#125; <span class="hljs-keyword">return</span> _typeof(obj); &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_classCallCheck</span>(<span class="hljs-params">instance, Constructor</span>) </span>&#123; <span class="hljs-keyword">if</span> (!_instanceof(instance, Constructor)) &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Cannot call a class as a function"</span>); &#125; &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_inherits</span>(<span class="hljs-params">subClass, superClass</span>) </span>&#123; <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> superClass !== <span class="hljs-string">"function"</span> && superClass !== <span class="hljs-literal">null</span>) &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Super expression must either be null or a function"</span>); &#125; subClass.prototype = <span class="hljs-built_in">Object</span>.create(superClass && superClass.prototype, &#123; <span class="hljs-attr">constructor</span>: &#123; <span class="hljs-attr">value</span>: subClass, <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span> &#125; &#125;); <span class="hljs-keyword">if</span> (superClass) _setPrototypeOf(subClass, superClass); &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_createSuper</span>(<span class="hljs-params">Derived</span>) </span>&#123; <span class="hljs-keyword">var</span> hasNativeReflectConstruct = _isNativeReflectConstruct(); <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_createSuperInternal</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">var</span> Super = _getPrototypeOf(Derived), result; <span class="hljs-keyword">if</span> (hasNativeReflectConstruct) &#123; <span class="hljs-keyword">var</span> NewTarget = _getPrototypeOf(<span class="hljs-built_in">this</span>).constructor; result = <span class="hljs-built_in">Reflect</span>.construct(Super, <span class="hljs-built_in">arguments</span>, NewTarget); &#125; <span class="hljs-keyword">else</span> &#123; result = Super.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>); &#125; <span class="hljs-keyword">return</span> _possibleConstructorReturn(<span class="hljs-built_in">this</span>, result); &#125;; &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_possibleConstructorReturn</span>(<span class="hljs-params">self, call</span>) </span>&#123; <span class="hljs-keyword">if</span> (call && (_typeof(call) === <span class="hljs-string">"object"</span> || <span class="hljs-keyword">typeof</span> call === <span class="hljs-string">"function"</span>)) &#123; <span class="hljs-keyword">return</span> call; &#125; <span class="hljs-keyword">return</span> _assertThisInitialized(self); &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_assertThisInitialized</span>(<span class="hljs-params">self</span>) </span>&#123; <span class="hljs-keyword">if</span> (self === <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>) &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">ReferenceError</span>(<span class="hljs-string">"this hasn't been initialised - super() hasn't been called"</span>); &#125; <span class="hljs-keyword">return</span> self; &#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_wrapNativeSuper</span>(<span class="hljs-params">Class</span>) </span>&#123;
  <span class="hljs-comment">// 基于 Map 的缓存</span>
  <span class="hljs-keyword">var</span> _cache = <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Map</span> === <span class="hljs-string">"function"</span> ? <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>() : <span class="hljs-literal">undefined</span>;
  _wrapNativeSuper = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_wrapNativeSuper</span>(<span class="hljs-params">Class</span>) </span>&#123;
    <span class="hljs-comment">// 保护，如果没有，或者不是原生的 function 则直接返回</span>
    <span class="hljs-keyword">if</span> (Class === <span class="hljs-literal">null</span> || !_isNativeFunction(Class)) <span class="hljs-keyword">return</span> Class;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> Class !== <span class="hljs-string">"function"</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Super expression must either be null or a function"</span>);
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> _cache !== <span class="hljs-string">"undefined"</span>) &#123;
      <span class="hljs-keyword">if</span> (_cache.has(Class)) <span class="hljs-keyword">return</span> _cache.get(Class);
      _cache.set(Class, Wrapper);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Wrapper</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 用父类构造函数生成了新的实例</span>
      <span class="hljs-keyword">return</span> _construct(Class, <span class="hljs-built_in">arguments</span>, _getPrototypeOf(<span class="hljs-built_in">this</span>).constructor);
    &#125;
    <span class="hljs-comment">// 把父类的原型方法挂上去</span>
    Wrapper.prototype = <span class="hljs-built_in">Object</span>.create(Class.prototype, &#123;
      <span class="hljs-attr">constructor</span>: &#123;
        <span class="hljs-attr">value</span>: Wrapper,
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;);
    <span class="hljs-comment">// 修正 __proto__ 指向</span>
    <span class="hljs-keyword">return</span> _setPrototypeOf(Wrapper, Class);
  &#125;;
  <span class="hljs-comment">// 所以这里返回的是父类的一个实例</span>
  <span class="hljs-keyword">return</span> _wrapNativeSuper(Class);
&#125;
<span class="hljs-comment">// 工具函数，Reflect.construct 的 polyfill</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_construct</span>(<span class="hljs-params">Parent, args, Class</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (_isNativeReflectConstruct()) &#123;
        _construct = <span class="hljs-built_in">Reflect</span>.construct;
    &#125; <span class="hljs-keyword">else</span> &#123;
        _construct = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_construct</span>(<span class="hljs-params">Parent, args, Class</span>) </span>&#123;
            <span class="hljs-keyword">var</span> a = [<span class="hljs-literal">null</span>];
            a.push.apply(a, args);
            <span class="hljs-keyword">var</span> Constructor = <span class="hljs-built_in">Function</span>.bind.apply(Parent, a);
            <span class="hljs-keyword">var</span> instance = <span class="hljs-keyword">new</span> Constructor();
            <span class="hljs-keyword">if</span> (Class) _setPrototypeOf(instance, Class.prototype);
            <span class="hljs-keyword">return</span> instance;
        &#125;;
    &#125;
    <span class="hljs-keyword">return</span> _construct.apply(<span class="hljs-literal">null</span>, <span class="hljs-built_in">arguments</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_isNativeReflectConstruct</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Reflect</span> === <span class="hljs-string">"undefined"</span> || !<span class="hljs-built_in">Reflect</span>.construct) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>; <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Reflect</span>.construct.sham) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>; <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Proxy</span> === <span class="hljs-string">"function"</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>; <span class="hljs-keyword">try</span> &#123; <span class="hljs-built_in">Boolean</span>.prototype.valueOf.call(<span class="hljs-built_in">Reflect</span>.construct(<span class="hljs-built_in">Boolean</span>, [], <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;)); <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>; &#125; <span class="hljs-keyword">catch</span> (e) &#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>; &#125; &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_isNativeFunction</span>(<span class="hljs-params">fn</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Function</span>.toString.call(fn).indexOf(<span class="hljs-string">"[native code]"</span>) !== -<span class="hljs-number">1</span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_setPrototypeOf</span>(<span class="hljs-params">o, p</span>) </span>&#123; _setPrototypeOf = <span class="hljs-built_in">Object</span>.setPrototypeOf || <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_setPrototypeOf</span>(<span class="hljs-params">o, p</span>) </span>&#123; o.__proto__ = p; <span class="hljs-keyword">return</span> o; &#125;; <span class="hljs-keyword">return</span> _setPrototypeOf(o, p); &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_getPrototypeOf</span>(<span class="hljs-params">o</span>) </span>&#123; _getPrototypeOf = <span class="hljs-built_in">Object</span>.setPrototypeOf ? <span class="hljs-built_in">Object</span>.getPrototypeOf : <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_getPrototypeOf</span>(<span class="hljs-params">o</span>) </span>&#123; <span class="hljs-keyword">return</span> o.__proto__ || <span class="hljs-built_in">Object</span>.getPrototypeOf(o); &#125;; <span class="hljs-keyword">return</span> _getPrototypeOf(o); &#125;

<span class="hljs-keyword">var</span> Child = <span class="hljs-comment">/*#__PURE__*/</span><span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_Array</span>) </span>&#123;
  _inherits(Child, _Array);
  <span class="hljs-keyword">var</span> _super = _createSuper(Child);
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">value</span>) </span>&#123;
    _classCallCheck(<span class="hljs-built_in">this</span>, Child);
    <span class="hljs-keyword">return</span> _super.call(<span class="hljs-built_in">this</span>, value);
  &#125;
  <span class="hljs-keyword">return</span> Child;
&#125;( <span class="hljs-comment">/*#__PURE__*/</span>_wrapNativeSuper(<span class="hljs-built_in">Array</span>));

<span class="hljs-keyword">var</span> child1 = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'foo'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里很好的解决了一个问题，你会发现在之前 ES5 的处理中，我们没有处理继承内建对象，比如：<code>Array</code>，<code>Date</code>等。这是因为之前都是调用父类构造函数并使用 <code>call</code> 改变 <code>this</code> 指向子类实例实现的（<code>Parent.call(this, foo)</code>）。但是对于原生构造函数来说，会有几种情况：</p>
<ul>
<li>一些会忽略 <code>apply/call</code> 方法传入的 <code>this</code>，也就是说原生构造函数 <code>this</code> 无法绑定，导致子类实例拿不到内部属性。</li>
<li>一些在底层有限制，如 <code>Date</code> ，如果调用对象的 <code>[[Class]]</code> 不是 <code>Date</code>，则抛出错误</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02d51c8774984a79a87676287565f2c8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>而现在则通过包装，调用时会返回 new 父类出来的实例，从而借助其获得内建对象上的方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_wrapNativeSuper</span>(<span class="hljs-params">Class</span>) </span>&#123;
  <span class="hljs-comment">// 基于 Map 的缓存</span>
  <span class="hljs-keyword">var</span> _cache = <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Map</span> === <span class="hljs-string">"function"</span> ? <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>() : <span class="hljs-literal">undefined</span>;
  _wrapNativeSuper = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_wrapNativeSuper</span>(<span class="hljs-params">Class</span>) </span>&#123;
    <span class="hljs-comment">// 保护，如果没有，或者不是原生的 function 则直接返回</span>
    <span class="hljs-keyword">if</span> (Class === <span class="hljs-literal">null</span> || !_isNativeFunction(Class)) <span class="hljs-keyword">return</span> Class;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> Class !== <span class="hljs-string">"function"</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Super expression must either be null or a function"</span>);
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> _cache !== <span class="hljs-string">"undefined"</span>) &#123;
      <span class="hljs-keyword">if</span> (_cache.has(Class)) <span class="hljs-keyword">return</span> _cache.get(Class);
      _cache.set(Class, Wrapper);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Wrapper</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 用父类构造函数生成了新的实例</span>
      <span class="hljs-keyword">return</span> _construct(Class, <span class="hljs-built_in">arguments</span>, _getPrototypeOf(<span class="hljs-built_in">this</span>).constructor);
    &#125;
    <span class="hljs-comment">// 把父类的原型方法挂上去</span>
    Wrapper.prototype = <span class="hljs-built_in">Object</span>.create(Class.prototype, &#123;
      <span class="hljs-attr">constructor</span>: &#123;
        <span class="hljs-attr">value</span>: Wrapper,
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;);
    <span class="hljs-comment">// 修正 __proto__ 指向</span>
    <span class="hljs-keyword">return</span> _setPrototypeOf(Wrapper, Class);
  &#125;;
  <span class="hljs-comment">// 所以这里返回的是父类的一个实例</span>
  <span class="hljs-keyword">return</span> _wrapNativeSuper(Class);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><a name="user-content-V00Tz" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-37">小结</h2>
<p>本文从原型链讲起，主要针对 JavaScript 中基于原型链继承的原理，ES5中各种继承的优缺点，以及 Class 语法糖本身的样子 进行了一定介绍。主要还是偏向于基础知识层面，后续会结合设计模式、TypeScript 以及有关 polyfill 进行学习</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            