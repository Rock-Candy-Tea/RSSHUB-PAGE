
---
title: 'JavaScript学习(3) - 聊聊原型链- 2. 对象与原型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a084df94ef4a4b1f8de27ae715c32998~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Apr 2021 00:00:10 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a084df94ef4a4b1f8de27ae715c32998~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>《JavaScript高级程序设计（第三版）》学习笔记</p>
<p>相关内容：</p>
<p><a href="https://juejin.cn/post/6954927427155935262" target="_blank">JavaScript学习(3)- 聊聊原型链- 1. 变量</a></p>
<p><a href="https://juejin.cn/post/6955002046504239134/" target="_blank">JavaScript学习(3)- 聊聊原型链- 2. 对象与原型</a></p>
<p><a href="https://juejin.cn/post/6955032858259882015/" target="_blank">JavaScript学习(3)- 聊聊原型链- 3. 原型链与继承</a></p>
</blockquote>
<hr>
<p><em><strong>关键词：对象的prototype属性；实例属性；创建对象的方式：原型模式、构造函数模式、寄生模式</strong></em></p>
<blockquote>
<p><strong>本章节学习路线：</strong></p>
<ol>
<li>
<p>什么是对象？对象的属性？</p>
</li>
<li>
<p>创建对象的模式：工厂模式、构造模式、 原型模式、动态原型模式 、寄生构造函数模式、稳妥构造函数模式</p>
</li>
<li>
<p>原型模式深入理解：</p>
</li>
</ol>
<ul>
<li>原型模式的优点与问题 - 共享</li>
<li>问题的解决方法：构造函数与原型模式的使用 - 构造函数存实例属性，原型对象存共享属性</li>
</ul>
</blockquote>
<h1 data-id="heading-0">1. 关于对象的理解</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建对象</span>
<span class="hljs-keyword">var</span> person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'kenny'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">29</span>,
  <span class="hljs-attr">sayName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.name) <span class="hljs-comment">// Object中可直接创建对象</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">1.1 属性类型</h2>
<h3 data-id="heading-2">1.1.1 数据属性</h3>
<blockquote>
<p>数据属性：包含一个数据值的位置。该位置可进行读取和写入</p>
</blockquote>






























<table><thead><tr><th>属性值</th><th>定义</th><th>默认值</th></tr></thead><tbody><tr><td><code>[[Configurable]]</code></td><td>能否修改属性的特性，一旦修改为false，则再也无法恢复</td><td>true</td></tr><tr><td><code>[[Enumerable]]</code></td><td>能否通过for-in循环返回属性</td><td>true</td></tr><tr><td><code>[[Writable]]</code></td><td>能否修改属性的值</td><td>true</td></tr><tr><td><code>[[Value]]</code></td><td>该属性的数据值</td><td>undefined</td></tr></tbody></table>
<p>用<code>Object.defineProperty()</code>可以对属性进行修改：（但是慎重使用）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> person = &#123;&#125;
<span class="hljs-built_in">Object</span>.defineProperty(person, <span class="hljs-string">'name'</span>, &#123;
  <span class="hljs-attr">writable</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">value</span>: <span class="hljs-string">'Teller'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.1.2 访问器属性</h3>
<blockquote>
<p>访问器属性：不包含数据值，包含getter和setter</p>
</blockquote>






























<table><thead><tr><th>属性值</th><th>定义</th><th>默认值</th></tr></thead><tbody><tr><td><code>[[Configurable]]</code></td><td>能否修改属性的特性，一旦修改为false，则再也无法恢复</td><td>true</td></tr><tr><td><code>[[Enumerable]]</code></td><td>能否通过for-in循环返回属性</td><td>True</td></tr><tr><td><code>[[Get]]</code></td><td>读取属性时调用</td><td>undefined</td></tr><tr><td><code>[[Set]]</code></td><td>写入属性时调用</td><td>undefined</td></tr></tbody></table>
<h2 data-id="heading-4">1.2 定义多个属性 - <code>Object.defineProperties()</code></h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> book = &#123;&#125;

<span class="hljs-built_in">Object</span>.defineProperties(book, &#123;
  <span class="hljs-attr">_year</span>: &#123;
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">value</span>: <span class="hljs-number">2004</span>
  &#125;,
  
  <span class="hljs-attr">edition</span>: &#123;
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>
  &#125;,
  
  <span class="hljs-attr">year</span>: &#123;
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._year
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">1.3 读取属性的特性 - <code>Object.getOwnPropertyDescriptior()</code></h2>
<p>任何DOM和BOM对象均可使用该方法，以获取对象属性</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> descriptor = <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptior(book,  <span class="hljs-string">'_year'</span>)

alert(descriptor.value) <span class="hljs-comment">// 2004</span>
alert(descriptor.configurable) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">2. 创建对象的方式</h1>
<p><strong>关键词：工厂模式、构造函数、原型模式、组合使用、动态原型、稳妥构造函数、寄生构造函数</strong></p>
<h2 data-id="heading-7">2.1 工厂模式</h2>
<ul>
<li><strong>工厂模式</strong>：用函数封装，构造整个对象，并在末尾return这个对象</li>
<li><strong>存在的问题</strong>：无法使用instanceof操作符判断对象类型（因该方法并非构造函数模式） - 用构造函数解决该问题</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createPerson</span> (<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-comment">// 1. 创建新对象</span>
  <span class="hljs-keyword">var</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()  
  
  <span class="hljs-comment">// 2. 为对象添加属性</span>
  o.name = name
  o.age = age
  o.job = job
  o.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.name)
  &#125;
  
  <span class="hljs-comment">// 3. 需要在末尾return这个对象</span>
  <span class="hljs-keyword">return</span> o 
&#125;

<span class="hljs-comment">// 调用函数构造实例 - 无需使用new操作符</span>
<span class="hljs-keyword">var</span> person1 = createPerson(<span class="hljs-string">'Greg'</span>, <span class="hljs-number">27</span>, <span class="hljs-string">'Doctor'</span>)

<span class="hljs-comment">// 存在的问题 - 无法使用instanceof判断person1是createPerson类型的对象</span>
alert(person1 <span class="hljs-keyword">instanceof</span> createPerson) <span class="hljs-comment">// false</span>
alert(person1 <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)       <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">2.2 构造函数模式</h2>
<ol>
<li>
<p><strong>构造函数</strong>：将属性和方法直接赋值给this对象，无需return</p>
</li>
<li>
<p><strong>与工厂模式的区别</strong>：</p>
<ol>
<li>没有显式的创造对象</li>
<li>直接将属性和方法给了this对象</li>
<li>没有return语句</li>
</ol>
</li>
<li>
<p><strong>解决了工厂模式的问题</strong>：用构造函数创建的对象，可以通过instanceof，获取到对象的类型</p>
</li>
<li>
<p><strong>构造函数的缺点</strong>：功能效果完全相同的属性无法共享，重复占据内存空间 - 用原型模式解决该问题</p>
</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 构造函数Person（一般为首字母大写）</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span> (<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.age = age
  <span class="hljs-built_in">this</span>.job = job
  <span class="hljs-built_in">this</span>.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.name)
  &#125;
&#125;

<span class="hljs-comment">// 调用构造函数的方式：</span>
<span class="hljs-comment">// 1. 用new方法，使用构造函数，创建person对象</span>
<span class="hljs-keyword">var</span> person1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'Greg'</span>, <span class="hljs-number">29</span>, <span class="hljs-string">'Doctor'</span>)
alert(person1 <span class="hljs-keyword">instanceof</span> Person) <span class="hljs-comment">// true - 可使用instanceof获得对象类型</span>

<span class="hljs-comment">// 2. 直接作为普通函数使用，则为给window创建创建对象 - 此时Person()中的this指向window</span>
Person(<span class="hljs-string">'Greg'</span>, <span class="hljs-number">29</span>, <span class="hljs-string">'Doctor'</span>)
<span class="hljs-built_in">window</span>.sayName() <span class="hljs-comment">// 'Greg'</span>


<span class="hljs-comment">// 存在的问题：构造函数创建的属性为实例属性，其中功能效果完全相同的属性无法共享，重复占据内存空间</span>
alert(person1.sayName == person2.sayName) <span class="hljs-comment">// false</span>

<span class="hljs-comment">/*
 * 例如：通过Person构造的两个对象的sayName()是不等价的，但两者执行的功能是一致的
 * 普通解决方法：将共享属性从构造函数中移出，作为全局属性
 * 产生的新的问题：如果一个对象需要有多个function，就要全局声明多个function，违反了封装性
 * 最佳解决方案：原型模式
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span> (<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.age = age
  <span class="hljs-built_in">this</span>.job = job
  <span class="hljs-built_in">this</span>.sayName = sayName
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayName</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// 全局function - 缺乏封装性</span>
  alert(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">2.3 原型模式 - prototype</h2>
<h3 data-id="heading-10">2.3.1 原型模式的创建方法与基本概念</h3>
<ol>
<li><strong>原型模式：每一个创建的函数、Object都有一个prototype属性</strong></li>
<li>prototype属性是一个指针，指向一个对象，包含由特定类型的所有实例共享的属性核方法</li>
<li><strong>优点</strong>：让所有对象实例均可共享其所包含的属性和方法，而无需在构造函数中定义对象实例的信息</li>
<li><strong>注意</strong>：实例中创建的同名属性，会覆盖掉原型中的属性</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-comment">// 构造函数Person</span>
  
<span class="hljs-comment">// 在Person的原型中添加属性,而非在构造函数中添加</span>
Person.prototype.name = <span class="hljs-string">'Nicholas'</span>
Person.prototype.name = <span class="hljs-number">29</span>
Person.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; alert(<span class="hljs-built_in">this</span>.name) &#125;
  
<span class="hljs-comment">// 创建对象 - 使用Person构造函数创建Person对象，该对象可以直接使用Person中的原型属性</span>
<span class="hljs-keyword">var</span> person1 = <span class="hljs-keyword">new</span> Person()
person1.sayName() <span class="hljs-comment">// 'Nicholas'</span>
  
<span class="hljs-keyword">var</span> person2 = <span class="hljs-keyword">new</span> Person()
person2.sayName() <span class="hljs-comment">// 'Nicholas'</span>
  
alert(person1.sayName == person2.sayName) <span class="hljs-comment">// true - 创建不同对象时，均指向同一个原型属性（同一个指针）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>另一种创建原型的方法：<strong>对象字面量法</strong></li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 对象字面量法</span>
Person.prototype = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Nicholas'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">29</span>,
  <span class="hljs-attr">job</span>: <span class="hljs-string">'Doctor'</span>,
  <span class="hljs-attr">sayName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.name)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>对象字面量法存在问题</strong>：prototype对象的constructor属性，不再指向Person</p>
<p><strong>原因</strong>：通过上述方法，完全重写了默认的prototype对象，所以constructor属性变成了新对象的constructor属性，指向Object构造函数，而非Person函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> person1 = <span class="hljs-keyword">new</span> Person()
alert(person1 <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>
alert(person1 <span class="hljs-keyword">instanceof</span> Person) <span class="hljs-comment">// true</span>
alert(person1.constructor == Person ) <span class="hljs-comment">// false - person1对象的构造函数因为重写prototype对象，所以直接指向了Object</span>
alert(person1.constructor == <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 处理上述问题的方法：在重写的对象中也把constructor进行赋值返回</span>
Person.prototype = &#123;
  <span class="hljs-attr">constructor</span>: Person, <span class="hljs-comment">// 在重写的原型对象中，把Person设置为constructor的值</span>
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Nicholas'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">29</span>,
  <span class="hljs-attr">job</span>: <span class="hljs-string">'Doctor'</span>,
  <span class="hljs-attr">sayName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.name)
  &#125;
&#125;
<span class="hljs-comment">// 但上述方法会导致constructor变成可枚举的值，实际上constructor是默认不可枚举的，所以需要用defineProperty方法进行设置</span>
<span class="hljs-built_in">Object</span>.defineProperty(Person.prototype, <span class="hljs-string">'constructor'</span>, &#123;
  <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 重置为false</span>
  <span class="hljs-attr">value</span>: Person
&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">2.3.2 原型对象的理解 - 共享属性</h3>
<ol>
<li>图解上述代码样例：</li>
</ol>
<p>图解说明如下：</p>
<pre><code class="copyable">1. Person Prototype - 原型对象：包含构造函数constructor和属性值：name、age、sayName
2. Person 构造函数：原型Prototype指向整个Person原型对象；原型对象中的构造函数指回了Person构造函数
3. 利用Person构造函数创建的Person1和Person2对象：包含一个[[Prototype]]属性，该属性指向的就是Person原型对象
所以，Person1和Person2对象，均指向的是同一个原型对象中的sayName属性
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a084df94ef4a4b1f8de27ae715c32998~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>A. 原型对象解析（根据上图总结）：</strong></p>
<pre><code class="copyable">1. 创建一个新函数function，就会为该函数创建一个prototype属性，该属性指向函数的原型对象
2. 所有的原型对象都会自动获得一个constructor属性，该属性是一个指向prototype属性所在函数的指针（注意：指针）
3. 通过构造函数创建一个对象后，该对象内部将包含一个`[[prototype]]`指针，指向构造函数的原型对象
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>B. 可以通过<code>isPrototype()</code>和<code>Object.getPrototypeOf()</code>方法确定对象是否指向构造函数（因为在常规实现中无法访问）：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1. 用isPrototype()方法确定对象和构造函数之间关于prototype的关系</span>
Person.prototype.isPrototypeOf(person1) <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 2. 用es5提出的Object.getPrototypeOf()来返回[[Prototype]]的值</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(person1).name <span class="hljs-comment">// 'Nicholas'</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(person1) == Person.prototype <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>C. 无法通过对象实例重写原型中的值，只能通过在实例中创建同名的该属性，以屏蔽原型中的属性</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1. 创建构造函数Person</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-comment">// 2. 创建Person的原型对象</span>
Person.prototype.name = <span class="hljs-string">'Nicholas'</span>
Person.prototype.age = <span class="hljs-number">29</span>
Person.prototype.job = <span class="hljs-string">'Doctor'</span>
Person.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; alert(<span class="hljs-built_in">this</span>.name) &#125;

<span class="hljs-comment">// 3. 创建Person的对象person1</span>
<span class="hljs-keyword">var</span> person1 = <span class="hljs-keyword">new</span> Person()

<span class="hljs-comment">// 4. 在实例（constructor）中创建name属性值</span>
person1.name = <span class="hljs-string">'Greg'</span>

<span class="hljs-comment">// 5. 实例中的name属性覆盖掉prototype中的name属性</span>
alert(person1.name) <span class="hljs-comment">// 'Greg'</span>

<span class="hljs-comment">// 6. 通过delete删除实例中的属性值</span>
<span class="hljs-keyword">delete</span> person1.name

<span class="hljs-comment">// 7. 由于删除了实例中的属性，所以调用时候会展示原型中的属性值</span>
alert(person1.name) <span class="hljs-comment">// 'Nicholas'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">2.3.3 判断属性在原型还是在实例中的方法</h3>
<p><strong>A. 判断属性是否来自于实例：<code>hasOwnProperty()</code> - 来自于实例中则返回true</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> person1 = <span class="hljs-keyword">new</span> Person()

<span class="hljs-comment">// 1. name属性来自于原型中，故返回false</span>
alert(person1.hasOwnProperty(<span class="hljs-string">'name'</span>)) <span class="hljs-comment">// false</span>

<span class="hljs-comment">// 2. 创建实例中的属性，则检测后返回true</span>
person1.name = <span class="hljs-string">'Greg'</span>
alert(person1.hasOwnProperty(<span class="hljs-string">'name'</span>)) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>B. 判断属性是否来自于实例或对象：<code>hasOwnProperty()</code>、单独使用in操作符、<code>hasPrototypeProperty()</code></strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> person1 = <span class="hljs-keyword">new</span> Person()

<span class="hljs-comment">// 1. 用in方法确认name属性是否存在于实例或原型中</span>
alert(<span class="hljs-string">'name'</span> <span class="hljs-keyword">in</span> person1) <span class="hljs-comment">// true --- name属性存在于实例或原型中</span>

<span class="hljs-comment">// 2. 用hasOwnProperty方法确认属性是否存在于实例中</span>
alert(person1.hasOwnProperty(<span class="hljs-string">'name'</span>)) <span class="hljs-comment">// false --- name属性不存在于实例中</span>

<span class="hljs-comment">// 3. 用hasOwnProperty和in结合的方法，判断属性是否存在于原型中</span>
alert(!Person.hasOwnProperty(<span class="hljs-string">'name'</span>) && (name <span class="hljs-keyword">in</span> Person)) <span class="hljs-comment">// true --- name属性存在于原型中</span>

<span class="hljs-comment">// 4. 利用上述方法，封装一个hasPrototypeProperty方法，判断属性是否存在于原型中</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hasPrototypeProperty</span>(<span class="hljs-params">object, name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> !object.hasPrototypeProperty(name) && (name <span class="hljs-keyword">in</span> object)
&#125;
alert(hasPrototypeProperty(person, <span class="hljs-string">'name'</span>)) <span class="hljs-comment">// true --- name属性存在于原型中</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>C. 通过for-in方法可访问Enumerated为true的属性值，但会屏蔽Enumerated为false的值</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 通过Object.keys()方法，返回包含所有可枚举属性的字符串数组</span>
<span class="hljs-keyword">var</span> keys = <span class="hljs-built_in">Object</span>.keys(Person.prototype)
alert(keys) <span class="hljs-comment">// 'name, age, job, sayName'</span>

<span class="hljs-comment">// 通过Object.getOwnPropertyNames()方法，返回所有实例属性（无论是否可枚举）</span>
<span class="hljs-keyword">var</span> keys2 = <span class="hljs-built_in">Object</span>.getOwnPropertyNames(Person.prototype)
alert(keys2) <span class="hljs-comment">// 'constructor, name, age, job, sayName' --- constructor不可枚举，但可以通过该方法获取</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">2.3.4 原型的动态性 - 动态修改原型</h3>
<p><strong>A. 动态修改原型：对原型对象所做的任何修改可立即在实例中反映出来</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1. 直接创建对象friend</span>
<span class="hljs-keyword">var</span> friend = <span class="hljs-keyword">new</span> Person()

<span class="hljs-comment">// 2. 然后为Person添加原型对象属性sayHi</span>
Person.prototype.sayHi = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  alert(<span class="hljs-string">'Hi'</span>)
&#125;

<span class="hljs-comment">// 3. 对象friend可以使用新添加的属性值</span>
friend.sayHi() <span class="hljs-comment">//'Hi'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>B. 注意：如果使用对象字面量法重写原型对象，会切断构造函数和最初原型对象的关系</strong></p>
<p>原因：实例中的指针是指向原型，而非构造函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1. 直接创建对象friend</span>
<span class="hljs-keyword">var</span> friend = <span class="hljs-keyword">new</span> Person()

<span class="hljs-comment">// 2. 然后为Person重写原型对象，包含属性sayHi</span>
Person.prototype = &#123;
  <span class="hljs-attr">constructor</span>: Person, <span class="hljs-comment">// 在重写的原型对象中，把Person设置为constructor的值</span>
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Nicholas'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">29</span>,
  <span class="hljs-attr">job</span>: <span class="hljs-string">'Doctor'</span>,
  <span class="hljs-attr">sayName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.name)
  &#125;
&#125;

<span class="hljs-comment">// 3. 对象friend不能使用通过重写原型对象而新添加的属性值，</span>
<span class="hljs-comment">// 原因：Person本身指向了一个全新的prototype对象，而非friend指向的原有的原型对象</span>
friend.sayHi() <span class="hljs-comment">//error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">2.3.5 原生对象也具备原型模式</h3>
<ol>
<li>原生对象：例如：Array、String等</li>
<li><strong>所有的原生的引用类型，都是上述模式创建的，具备原型模式。例如：<code>Array.prototype</code>中可以找到<code>sort()</code>方法；<code>String.prototype</code>中可以找到<code>substring()</code>方法</strong></li>
<li>可以随时给原生对象添加新的原型方法，但是不推荐使用</li>
</ol>
<h3 data-id="heading-15">2.3.6 成也原型，败也原型 - 浅析原型对象的问题：共享属性</h3>
<ol>
<li>prototype最优秀的特性，就是具备共享能力，可以把一些公有的方法、属性作为原型属性，让所有实例共享使用</li>
<li>但，prototype的缺点也来自于这种共享的特性：<strong>如果prototype中存在引用类型，则会使不同实例的该属性值相互干扰</strong></li>
<li>解决方案：<strong>共享属性放在原型中，非共享属性（需避免干扰的）放在构造函数中 ------------ 即为：构造函数模式和原型模式的组合使用（详见2.4节）</strong></li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建构造函数Person</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-comment">// 创建原型对象，其中包含引用类型friends（Array）</span>
Person.prototype = &#123;
  <span class="hljs-attr">constructor</span>: Person, <span class="hljs-comment">// 在重写的原型对象中，把Person设置为constructor的值</span>
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Nicholas'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">29</span>,
  <span class="hljs-attr">job</span>: <span class="hljs-string">'Doctor'</span>,
  <span class="hljs-attr">friends</span>: [<span class="hljs-string">'Sheldon'</span>, <span class="hljs-string">'Raj'</span>]
  <span class="hljs-attr">sayName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.name)
  &#125;
&#125;

<span class="hljs-keyword">var</span> person1 = <span class="hljs-keyword">new</span> Person()
<span class="hljs-keyword">var</span> person2 = <span class="hljs-keyword">new</span> Person()

<span class="hljs-comment">// person1对象中，为引用对象属性friends赋值</span>
person1.friends.push(<span class="hljs-string">'Penny'</span>)

<span class="hljs-comment">// 由于原型对象的共享性，所以所有通过Person()构造函数创建的对象，都具备相同的原型对象属性，原型对象中的引用对象会指向同一个值</span>
<span class="hljs-comment">// 问题：两个实例的共享属性互相干扰</span>
alert(person1.friends) <span class="hljs-comment">// 'Sheldon, Raj, Penny'</span>
alert(person1.friends) <span class="hljs-comment">// 'Sheldon, Raj, Penny'</span>
alert(person1.fiends === person2.friends) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">2.4 构造函数模式和原型模式的组合使用</h2>
<ol>
<li>用以解决上述原型模式共享属性带来的互相干扰的问题，并最大限度节省内存空间</li>
<li>充分结合利用构造函数模式与原型模式的特点：
<ol>
<li>构造函数模式：定义实例属性</li>
<li>原型模式：定义方法和共享的属性</li>
</ol>
</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建构造函数Person - 非共享属性，尤其是引用类型，作为实例属性</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.age = age
  <span class="hljs-built_in">this</span>.job = job
  <span class="hljs-built_in">this</span>.friends = [<span class="hljs-string">'Sheldon'</span>, <span class="hljs-string">'Raj'</span>]
&#125;

<span class="hljs-comment">// 创建Person的原型对象 - 将共享的属性，例如function，作为原型属性</span>
Person.prototype = &#123;
  <span class="hljs-attr">constructor</span>: Person, 
  <span class="hljs-attr">sayName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.name)
  &#125;
&#125;

<span class="hljs-keyword">var</span> person1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'Nicholas'</span>, <span class="hljs-number">29</span>, <span class="hljs-string">'Doctor'</span>)
<span class="hljs-keyword">var</span> person2 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'Cindy'</span>, <span class="hljs-number">28</span>, <span class="hljs-string">'Developer'</span>)
person1.friends.push(<span class="hljs-string">'Van'</span>)

<span class="hljs-comment">// 实例属性互不相同，但共享属性指向同一指针</span>
alert(person1.friends === person2.friends) <span class="hljs-comment">// false</span>
alert(person1.sayName === person2.sayName) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">2.5 动态原型模式</h2>
<ol>
<li><strong>动态原型模式</strong>：通过检查某个应该存在的方法是否有效，来决定是否需初始化原型</li>
<li><strong>优点</strong>：可以更进一步优化内存空间</li>
<li><strong>注意</strong>：使用动态原型模式时，不能使用对象字面量重写原型。因为已经创建了实例的情况下重写原型，会切换现有实例和新原型之间的关系</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.age = age
  <span class="hljs-built_in">this</span>.job = job
  <span class="hljs-built_in">this</span>.friends = [<span class="hljs-string">'Sheldon'</span>, <span class="hljs-string">'Raj'</span>]
&#125;

<span class="hljs-comment">// 仅在sayName不存在的情况下，才将其添加到原型中</span>
<span class="hljs-comment">// 添加方法不可使用对象字面量方法，</span>
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span>.sayName != <span class="hljs-string">'function'</span>) &#123;
  Person.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.sayName)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">2.6 寄生构造函数模式</h2>
<ol>
<li><strong>寄生构造函数模式</strong>：创建一个函数，该函数的作用仅为封装创建对象的代码，再返回新创建的对象</li>
<li><strong>用途</strong>：用于将原生对象（例如：Array）添加自定义属性方法而不修改原生对象的构造函数（对原生对象的增强）</li>
<li><strong>特点</strong>：
<ol>
<li>创建方法类似工厂模式，但工厂模式的函数不是构造函数，本模式的包装函数可以称为构造函数</li>
<li>可以使用new操作符</li>
<li>构造函数中的返回对象可以重写</li>
<li>构造函数返回的对象，与在构造函数外部创建的对象相同</li>
<li>无法通过instanceof来确定对象的类型</li>
</ol>
</li>
<li><em><strong>不推荐使用该模式！</strong></em></li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 样例1：</span>
<span class="hljs-comment">// 以类似工厂模式的方法，创建寄生构造函数模式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-keyword">var</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>() <span class="hljs-comment">// 创建对象</span>
  o.name = name
  o.age = age
  o.job = job
  o.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-built_in">this</span>.name)
  &#125;
  <span class="hljs-keyword">return</span> o <span class="hljs-comment">// 返回对象</span>
  <span class="hljs-comment">// 如果不设置返回值，则默认会返回新对象实例；故可以在寄生模式中重写返回值</span>
&#125;

<span class="hljs-comment">// 可以使用new操作符创建，因为上述方法可以被认为是构造函数</span>
<span class="hljs-keyword">var</span> friend = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'Nicholas'</span>, <span class="hljs-number">29</span>, <span class="hljs-string">'doctor'</span>)
friend.sayName() <span class="hljs-comment">// 'Nicholas'</span>



<span class="hljs-comment">// 样例2：重写并为Array方法添加属性</span>
<span class="hljs-comment">// 不能修改Array构造函数，但是可以使用寄生模式为对象添加构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SpecialArray</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> values = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>()              <span class="hljs-comment">// 创建数组对象</span>
  values.push.apply(values, <span class="hljs-built_in">arguments</span>)  <span class="hljs-comment">// 添加值</span>
  values.toPipedString = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;  <span class="hljs-comment">// 添加方法</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.join(<span class="hljs-string">'|'</span>)
  &#125;
  <span class="hljs-keyword">return</span> values                         <span class="hljs-comment">// 返回数组</span>
&#125;

<span class="hljs-keyword">var</span> colors = <span class="hljs-keyword">new</span> SpecialArray(<span class="hljs-string">'red'</span>, <span class="hljs-string">'blue'</span>, <span class="hljs-string">'green'</span>)
alert(colors.toPipedString())          <span class="hljs-comment">// 'red|blue|green'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">2.7 稳妥构造函数模式</h2>
<ol>
<li><strong>稳妥对象</strong>：没有公共属性，方法不引用this的对象，适合在安全环境中使用（安全模式下禁止this）</li>
<li><strong>与寄生模式创建方法相似，不同点如下</strong>：
<ol>
<li>新创建对象的实例方法不引用this</li>
<li>不使用new操作符调用构造函数</li>
</ol>
</li>
<li><strong>注意</strong>：稳妥模式下不能使用对象字面量重写原型，原因：对象字面量方法会切断与最初构造函数之间的关系</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-comment">// 创建对象</span>
  <span class="hljs-keyword">var</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>() 
  o.name = name
  o.age = age
  o.job = job
  
  <span class="hljs-comment">// 不使用this对象</span>
  o.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    alert(name) 
  &#125;
  
  <span class="hljs-comment">// 返回对象</span>
  <span class="hljs-keyword">return</span> o 
&#125;

<span class="hljs-keyword">var</span> friend = Person(<span class="hljs-string">'Nicholas'</span>, <span class="hljs-number">29</span>, <span class="hljs-string">'doctor'</span>)

<span class="hljs-comment">// 除了使用Person中的sayName，不能通过其他方法获取name，故适合安全环境</span>
friend.sayName() <span class="hljs-comment">// 'Nicholas'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">3. 小结</h1>
<ol>
<li>对象的基本属性：数据属性、访问器属性</li>
<li>创建对象的方式：</li>
</ol>

































<table><thead><tr><th>创建对象方式</th><th>简要说明</th></tr></thead><tbody><tr><td>工场模式</td><td>用函数封装，构造整个对象，并在末尾return这个对象<br>缺点：无法使用instanceof操作符判断对象类型（因该方法并非构造函数模式）<br>解决方案：用构造函数解决该问题</td></tr><tr><td>原型模式</td><td>直接使用prototype，利用prototype的共享特性；<br>缺点：引用对象存于prototype时，会导致创建的不同实例的该原型属性值互相干扰<br>解决方案：构造+原型组合模式</td></tr><tr><td>动态原型</td><td>通过检查某个应该存在的方法是否有效，来决定是否需初始化原型，以更进一步优化存储空间</td></tr><tr><td>构造+原型</td><td>构造部分存自身实例属性<br>原型部分存共享的属性（例如function）</td></tr><tr><td>寄生构造函数函数</td><td>可用于给原生对象（例如Array）增强添加一些自定义方法或属性而不破坏原有对象构造函数<br>缺点：不可用instanceof确定对象类型</td></tr><tr><td>稳妥构造函数</td><td>新创建对象的实例方法不引用this，在安全模式下稳妥运行<br>不使用new操作符调用构造函数</td></tr></tbody></table>
<ol start="3">
<li>原型的问题：引用对象放在prototype中，会因为共享导致一处改变、处处改变</li>
<li>寄生的本质：增强 - 在原有基础上添加自定义新属性</li>
</ol>
<hr>
<blockquote>
<p><strong>笔记目录：</strong></p>
<p><a href="https://juejin.cn/post/6954898562761097229" target="_blank">JavaScript学习(1) - JavaScript历史回顾</a></p>
<p><a href="https://juejin.cn/post/6954911303819345934" target="_blank">JavaScript学习(2) - 基础语法知识</a></p>
<p><a href="https://juejin.cn/post/6954927427155935262" target="_blank">JavaScript学习(3)- 聊聊原型链- 1. 变量</a></p>
<p><a href="https://juejin.cn/post/6955002046504239134/" target="_blank">JavaScript学习(3)- 聊聊原型链- 2. 对象与原型</a></p>
<p><a href="https://juejin.cn/post/6955032858259882015/" target="_blank">JavaScript学习(3)- 聊聊原型链- 3. 原型链与继承</a></p>
<p><a href="https://juejin.cn/post/6955309404207972360/" target="_blank">JavaScript学习(4)- 聊聊闭包那些事</a></p>
<p><strong>Github:</strong></p>
<p><a href="https://github.com/SHENLing0628/JavaScriptStudy" target="_blank" rel="nofollow noopener noreferrer">Github笔记链接（持续更新中，欢迎star，转载请标注来源）</a></p>
</blockquote></div>  
</div>
            