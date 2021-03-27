
---
title: '全面解析JavaScript中的构造函数、原型prototype、原型链'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/838a195079c84c129c63d714f33cc6b9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 26 Mar 2021 02:30:54 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/838a195079c84c129c63d714f33cc6b9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">构造函数</h2>
<h3 data-id="heading-1">什么是构造函数？</h3>
<blockquote>
<p>构造函数本身就是一个函数，与普通函数的区别在于，<code>用 new 创建实例的函数就是构造函数</code>，直接调用的就是普通函数。为了规范，构造函数的首字母一般大写。</p>
</blockquote>
<p>我们用一个事例来说说，如何用构造函数来创建一个对象。分两步：
1、定义一个构造函数（可包含属性和方法）
2、通过<code>new</code>调用构造函数创建实例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>)</span>&#123;
  <span class="hljs-comment">// 属性</span>
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-comment">// 方法</span>
  <span class="hljs-built_in">this</span>.getAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">18</span>;
  &#125;
&#125;
<span class="hljs-comment">// 通过 new 调用函数创建实例对象</span>
<span class="hljs-keyword">var</span> P = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'谷底飞龙'</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`my name is <span class="hljs-subst">$&#123;P.name&#125;</span>, my age is <span class="hljs-subst">$&#123;P.getAge()&#125;</span>`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的例子，我们会发现通过new创建的对象可以访问构造函数内部this指向的属性和方法。</p>
<h3 data-id="heading-2">new 调用构造函数发生了什么？</h3>
<p>调用<code>new Person('谷底飞龙')</code>的执行过程，经历4个阶段：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj  =&#123;&#125;;
obj.__proto__ = Person.prototype;
Person.call(obj);
<span class="hljs-keyword">return</span> obj;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>1、创建新的空对象<code>obj</code></li>
<li>2、将构造函数Person的原型<code>prototype</code>赋值给创建的新对象obj的<code>__proto__</code>，这是最关键的一步，具体细节将在下文描述。</li>
<li>3、通过<code>call</code>将新对象<code>obj</code>与构造函数内部的this进行硬绑定（可参考<a href="https://juejin.cn/post/6940963094948478990/#heading-1" target="_blank">call和apply的原理及区别</a>），因此，新对象obj能访问到函数内部this的属性和方法。</li>
<li>4、返回一个对象（默认返回this）<code>obj;</code></li>
</ul>
<h3 data-id="heading-3">Symbol 是不是构造函数？</h3>
<p>判断是否是构造函数，直接用new来调用执行试试</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Symbol</span>();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行后，会发现报错<code>Uncaught TypeError: Symbol is not a constructor</code>。因此，<code>Symbol</code>不支持使用new调用，所以不是构造函数，属于基本数据类型。</p>
<p>我们直接使用<code>Symbol()</code>试试，会打印出<code>Symbol()</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> sym = <span class="hljs-built_in">Symbol</span>()
<span class="hljs-built_in">console</span>.log(sym)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，Symbol虽然是基本数据类型，但是可以通过<code>Symbol()</code>来生成实例，且我们会发现实例<code>sym</code>有<code>constructor</code>属性值，值为<code>ƒ Symbol() &#123; [native code] &#125;</code>。这里的<code>constructor</code>属性值哪里来的呢？其实是Symbol原型<code>Symbol.prototype.constructor</code>上的，默认是<code>Symbol()</code>函数。</p>
<h3 data-id="heading-4">constructor 属性是否只读？</h3>
<blockquote>
<p>这个得分情况，对于引用类型来说 <code>constructor</code> 属性值是可以修改的，但是对于基本类型来说是只读的。</p>
</blockquote>
<ul>
<li>1、引用类型的<code>constructor</code>属性是可以修改的</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">案例正在补充中
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2、基本数据类型<code>number</code>、<code>string</code>、<code>bool</code>、<code>Symbol</code>等有constructor属性的，<code>constructor</code>属性是只读的。我们来运行代码试试：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;
<span class="hljs-built_in">console</span>.log(a.constructor);<span class="hljs-comment">//ƒ Number() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"谷底飞龙"</span>.constructor);<span class="hljs-comment">//ƒ String() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">true</span>.constructor);<span class="hljs-comment">//ƒ Boolean() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Symbol</span>().constructor);<span class="hljs-comment">//ƒ Symbol() &#123; [native code] &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3、基本数据类型<code>null</code>、<code>undefined</code>是没有constructor属性的</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-literal">null</span>.constructor);<span class="hljs-comment">//Uncaught TypeError: Cannot read property 'constructor' of null</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">undefined</span>.constructor);<span class="hljs-comment">//Uncaught TypeError: Cannot read property 'constructor' of undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">原型</h2>
<h3 data-id="heading-6">什么是原型 prototype？</h3>
<blockquote>
<p>JavaScript 是基于原型的语言。</p>
<p>JavaScript 中所有对象都是 Object 的实例，并继承自<code>Object.prototype</code>的属性和方法。
<code>每个 JavaScript 对象都拥有一个原型对象，对象以其原型为模板，从原型继承方法和属性</code>，这些属性和方法定义在对象的构造器函数的 prototype 属性上，而非对象实例本身。</p>
</blockquote>
<p>因此，给已存在的构造器添加属性和方法，需要通过原型来添加。我们先来试试不通过原型来添加属性，比如给下面的构造器 <code>Person</code> 增加新属性 <code>weight</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>)</span>&#123;
  <span class="hljs-comment">// 属性</span>
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-comment">// 方法</span>
  <span class="hljs-built_in">this</span>.getAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">18</span>;
  &#125;
&#125;
<span class="hljs-comment">// 通过new调用函数创建实例对象</span>
<span class="hljs-keyword">var</span> P = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'谷底飞龙'</span>);

<span class="hljs-comment">// 给 Person 增加新属性 weight</span>
Person.weight = <span class="hljs-number">65</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`my weight is <span class="hljs-subst">$&#123;P.weight&#125;</span>`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加属性失败，会打印出<code>my weight is undefined</code>。如果要给构造器添加属性和方法，可以通过构造函数的原型 <code>prototype</code>来添加，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>)</span>&#123;
  <span class="hljs-comment">// 属性</span>
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-comment">// 方法</span>
  <span class="hljs-built_in">this</span>.getAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">18</span>;
  &#125;
&#125;
<span class="hljs-comment">// 通过 new 调用函数创建实例对象</span>
<span class="hljs-keyword">var</span> P = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'谷底飞龙'</span>);

<span class="hljs-comment">// 给 Person 增加新属性 weight 和方法 getHeight</span>
Person.prototype.weight = <span class="hljs-number">65</span>;
Person.prototype.getHeight = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
   <span class="hljs-keyword">return</span> <span class="hljs-number">165</span>;
&#125;;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`my weight is <span class="hljs-subst">$&#123;P.weight&#125;</span>, my height is <span class="hljs-subst">$&#123;P.getHeight()&#125;</span>`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过构造函数的原型可成功添加属性<code>weight</code>和方法 <code>getHeight()</code>, 打印出<code>my weight is 65, my height is 165</code></p>
<h3 data-id="heading-7">prototype、[[Prototype]]和__proto__的区别？</h3>
<blockquote>
<p>1、原型<code>prototype</code>是构造函数的属性，<code>__proto__</code>是 new 生成的对象的属性，<code>[[Prototype]]</code>是对象的内部属性。</p>
<p>2、构造函数的原型 <code>prototype</code> 和其对象的 <code>__proto__</code>指向同一个对象</p>
<p>3、<code>[[Prototype]]</code>指向它的构造函数的原型<code>prototype</code>，外部无法直接访问，可以通过<code>__proto__</code>来访问内部属性<code>[[Prototype]]</code>，</p>
</blockquote>
<p>从前面讲到的new调用构造函数的执行过程的第二步：<code>obj.__proto__ = Person.prototype</code>，我们可以看出</p>
<ul>
<li>1、原型<code>prototype</code>是构造函数的属性，<code>__proto__</code>是 new 生成的对象的属性</li>
<li>2、构造函数的原型 <code>prototype</code> 和其对象的 <code>__proto__</code>是赋值关系，因此指向同一个对象。如下面的例子，会打印出<code>true</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>)</span>&#123;
  <span class="hljs-comment">// 属性</span>
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-comment">// 方法</span>
  <span class="hljs-built_in">this</span>.getAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">18</span>;
  &#125;
&#125;
<span class="hljs-comment">// 通过new调用函数创建实例对象</span>
<span class="hljs-keyword">var</span> P = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'谷底飞龙'</span>)
<span class="hljs-comment">// 对象的 __proto__ 和构造函数的原型 prototype 指向同一个对象</span>
<span class="hljs-built_in">console</span>.log(P.__proto__ === Person.prototype)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>3、<code>[[Prototype]]</code>是对象的内部属性，指向它的构造函数的原型<code>prototype</code>，外部无法直接访问，可以通过<code>__proto__</code>来访问内部属性<code>[[Prototype]]</code>，值得注意的是，<code>__proto__</code>属性并非ECMAScript标准推荐使用的属性，并且是作为弃用的属性。</p>
</li>
<li>
<p>4、内部属性<code>[[Prototype]]</code>无法直接在代码中使用，要用函数<code>Object.getPrototypeOf</code>来获取它的值，用函数<code>Object.setPrototypeOf</code>来改变它的值。想了解的的更详细，可以看看这篇文章 <a href="https://www.jianshu.com/p/894bae1098a5" target="_blank" rel="nofollow noopener noreferrer">Javascript：内部属性[[Prototype]]</a></p>
</li>
</ul>
<h2 data-id="heading-8">原型链</h2>
<h3 data-id="heading-9">什么是原型链？</h3>
<blockquote>
<p>每个对象拥有一个原型对象 <code>__proto__</code>，<code>__proto__</code>指向上一个原型<code>prototype</code>，并继承其属性和方法，同时原型对象也有可能有原型，这样一层一层，最终指向<code>null</code>，这就是<code>原型链</code>。</p>
</blockquote>
<p>我们来看个例子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>)</span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
&#125;
<span class="hljs-keyword">var</span> P = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'谷底飞龙'</span>)
<span class="hljs-comment">// 打印对象</span>
<span class="hljs-built_in">console</span>.log(P)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印出对象<code>P</code>，如下：
<img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/838a195079c84c129c63d714f33cc6b9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
我们可以看到，对象<code>P</code>有一个原型对象<code>__proto__</code>，P的原型对象<code>__proto__</code>有两个属性<code>constructor</code>和自己的原型对象<code>__proto__</code>，依次下去，最终指向<code>null</code>。这个案例中的原型链关系：<code>P.__proto__ => P.__proto__.__proto__ => null</code></p>
<h3 data-id="heading-10">原型链继承</h3>
<blockquote>
<p>正在补充中</p>
</blockquote>
<h4 data-id="heading-11">instanceof 原理及实现</h4>
<blockquote>
<p>正在补充中</p>
</blockquote>
<h4 data-id="heading-12">运作机制及属性遮蔽</h4>
<blockquote>
<p>正在补充中</p>
</blockquote>
<h2 data-id="heading-13">参考文档</h2>
<ul>
<li><a href="https://blog.51cto.com/ycgit/2351230" target="_blank" rel="nofollow noopener noreferrer">深入理解js构造函数</a></li>
<li><a href="https://muyiy.cn/blog/5/5.1.html#%E5%BC%95%E8%A8%80" target="_blank" rel="nofollow noopener noreferrer">重新认识构造函数、原型和原型链</a></li>
<li><a href="https://www.runoob.com/js/js-object-prototype.html" target="_blank" rel="nofollow noopener noreferrer">JavaScript prototype（原型对象）</a></li>
<li><a href="https://www.jianshu.com/p/7d58f8f45557" target="_blank" rel="nofollow noopener noreferrer">一篇文章看懂_proto_和prototype的关系及区别</a></li>
<li><a href="https://www.jianshu.com/p/894bae1098a5" target="_blank" rel="nofollow noopener noreferrer">Javascript：内部属性[[Prototype]]</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            