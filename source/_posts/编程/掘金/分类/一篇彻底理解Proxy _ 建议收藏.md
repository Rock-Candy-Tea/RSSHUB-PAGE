
---
title: '一篇彻底理解Proxy _ 建议收藏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b834c2fe9ec3469f952cb4649fd3f675~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 05:00:23 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b834c2fe9ec3469f952cb4649fd3f675~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第20天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>没有前言，咱们直接单刀直入，直奔主题！</p>
<p>首先从字面意思得知，<code>Proxy</code>是代理的意思</p>
<p>那它是什么呢？通过<code>typeof </code>来检测一下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Proxy</span>)<span class="hljs-comment">//function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由上可以得知：</p>
<ol>
<li><code>Proxy</code>是定义在<code>window</code>上的全局变量</li>
<li>它的类型是<code>function</code></li>
</ol>
<p>并且首字母大写了，我们可以猜测，它并不是一个普通的function，它应该是一个构造函数或者说是一个类。</p>
<p>那来试试看，万一可以直接执行呢！</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> proxy = <span class="hljs-built_in">Proxy</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果让你失望了，以上代码会报错：<code>Uncaught TypeError: Constructor Proxy requires 'new'</code></p>
<p>所以我们来试试正儿八经的试试<code>new Proxy()</code>,如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码执行也会抛出错误：<code>Uncaught TypeError: Cannot create proxy with a non-object as target or handler</code>,意思是创建<code>proxy</code>对象时，不能使用不是对象的东西作为<code>target</code>或者<code>handler</code>传入，什么意思呢？<strong>答案是要按照它的要求来传递参数</strong></p>
<p>从以上报错信息，我们可以得出两个重要信息：</p>
<ol>
<li><code>Proxy</code>在构造对象时接受两个参数：<code>target</code>和<code>handler</code></li>
<li>两个参数的类型必须是<code>object</code></li>
</ol>
<p>那问题来了，这两个参数<code>target</code>和<code>handler</code>分别表示什么呢？</p>
<p>在最开始，我说过<code>Proxy </code>的本意是代理意思，表示由它来“代理”某些操作；网上还有另外一种理解：</p>
<blockquote>
<p>可以将<code>Proxy</code>理解成“拦截”，在目标对象之前架设一层“拦截”，当外界对该对象的访问，都必须先通过这层拦截，正因为有了一种拦截机制，当外界的访问我们可以对进行一些操作（过滤或改写）</p>
</blockquote>
<p>所以我们可以很好的理解，<code>target</code>表示的就是要拦截（代理）的目标对象；而<code>handler</code>是用来定制拦截行为</p>
<p><code>target</code>很容易理解，关键就在<code>handler</code>里头到底可以填什么呢？分别用于拦截对象的什么操作呢？</p>
<p>于是乎，我们猜测：handler中肯定存在与对象操作一一对应的方法？</p>
<p>那我们先回顾我们是怎么操作对象？为了方便，我这里列举出操作对象的所有方式</p>
<p>例如：js</p>
<pre><code class="copyable">let obj = &#123;
name: 'alice',
showName() &#123;
console.log(`my name is $&#123;this.name&#125;`)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>获取对象属性</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(obj.name)<span class="hljs-comment">//alice</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>给对象添加属性</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">obj.age = <span class="hljs-number">12</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>判断属性是否在对象中</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'age'</span> <span class="hljs-keyword">in</span> obj)<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>删除对象属性</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">delete</span> obj.age
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>通过各种方法遍历对象的所有属性</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.getOwnPropertyNames(obj));<span class="hljs-comment">//["name", "showName"]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.getOwnPropertySymbols(obj));<span class="hljs-comment">//[]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.keys(obj))<span class="hljs-comment">//["name", "showName"]</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> obj)&#123;
<span class="hljs-built_in">console</span>.log(key)
&#125;<span class="hljs-comment">//分别打印name showName</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>获取对象的某个属性的描述对象</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> d = <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(obj,<span class="hljs-string">'name'</span>)
<span class="hljs-built_in">console</span>.log(d)
<span class="hljs-comment">//&#123;value: "alice", writable: true, enumerable: true, configurable: true&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>使用Object身上的方法，为某个对象添加一个或多个属性</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.defineProperty(obj,<span class="hljs-string">'age'</span>,&#123;
<span class="hljs-attr">value</span>:<span class="hljs-number">12</span>,
<span class="hljs-attr">writable</span>:<span class="hljs-literal">true</span>,
<span class="hljs-attr">enumerable</span>:<span class="hljs-literal">true</span>,
<span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>
&#125;)
<span class="hljs-built_in">Object</span>.defineProperties(obj,&#123;
<span class="hljs-attr">showAge</span>:&#123;
<span class="hljs-attr">value</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`我今年<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>岁了`</span>)&#125;,
<span class="hljs-attr">writable</span>:<span class="hljs-literal">true</span>,
<span class="hljs-attr">enumerable</span>:<span class="hljs-literal">true</span>,
<span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>,
&#125;,
<span class="hljs-attr">showInfo</span>:&#123;
<span class="hljs-attr">value</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`我叫<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>,我今年<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>岁了`</span>)&#125;,
<span class="hljs-attr">writable</span>:<span class="hljs-literal">true</span>,
<span class="hljs-attr">enumerable</span>:<span class="hljs-literal">true</span>,
<span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>,
&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li>获取一个对象的原型对象</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.getPrototypeOf(obj)
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.getPrototypeOf(obj) === obj.__proto__)<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="9">
<li>设置某个对象的原型属性对象</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.setPrototypeOf(obj,<span class="hljs-literal">null</span>);
<span class="hljs-comment">//表示设置对象的原型为null，也可以传入其他对象作为其原型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="10">
<li>让一个对象变得不可扩展，即不能添加新的属性</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.preventExtensions(obj)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="11">
<li>查看一个对象是不是可扩展的</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.isExtensible(obj));<span class="hljs-comment">//false，因为上面设置了该对象为不可扩展对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="12">
<li>如果对象为function类型，function类型的对象可以执行被执行符号()以及.call()和.apply()执行</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">...args</span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>,args) 
&#125;
fn(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>);
fn.call(obj,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>);
fn.apply(obj,[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="13">
<li>一切皆是对象。如果对象作为构造函数时，则该对象可以用new生成出新的对象</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-keyword">let</span> p1 = <span class="hljs-keyword">new</span> Person();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上都是对对象的一些操作！</p>
<p>那回到我们的<code>new Proxy(target,handler)</code>中的<code>handler</code>，我们之前说了，<code>handler</code>是用于设置拦截行为的，其实拦截的内容就是上面这一系列的对象操作，当对象执行某个操作时，就会触发<code>handler</code>里面定义的东西，而这些东西本质是一个个函数。</p>
<p>于是，我们对<code>Proxy</code>有了比较全面的认知，知道它其实是构造函数，它可以构造出代理对象，这个代理对象可以代理目标对象target做一些事，当执行某个操作时，它会执行该操作所对应的函数。那问题来了，<code>handler</code>中都有哪些函数呢？分别对应什么操作呢？</p>
<p>为了看上去不乱，我这里先画个图</p>
<p>补画图处...............................................</p>
<p>下面我们一个个来讲</p>
<ol>
<li><code>get方法</code></li>
</ol>
<p>get方法可自动接受3个参数target, propKey, receiver，分别表示要代理的目标对象、对象上的属性以及代理对象，该方法用于拦截某个属性的读取操作，比如<code>proxy.foo</code>和<code>proxy['foo']</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Alice"</span>
&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
  <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">target, propKey</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (propKey <span class="hljs-keyword">in</span> target) &#123;
      <span class="hljs-keyword">return</span> target[propKey];
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">ReferenceError</span>(<span class="hljs-string">`Prop name <span class="hljs-subst">$&#123;propKey&#125;</span> does not exist.`</span>);
    &#125;
  &#125;
&#125;);
proxy.name <span class="hljs-comment">// "Alice"</span>
proxy.age <span class="hljs-comment">// 抛出错误:Uncaught ReferenceError: Prop name age does not exist.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，上面我访问了不存在属性，正常情况下如果没有这个拦截函数，访问不存在的属性，只会返回undefined，这里由于被代理了，所以抛出错误了！</p>
<p>而且<code>console.log(proxy === receiver)</code>返回<code>true</code></p>
<ol start="2">
<li><code>set方法</code></li>
</ol>
<p>set方法可自动接受4个参数：target, propKey, value, receiver，分别表示要代理的目标对象、对象上的属性、属性对应的值以及代理对象。</p>
<p>该方法用于拦截对象属性操作，像<code>proxy.foo = xxx</code>或<code>proxy['foo'] = xxx</code>，例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Alice"</span>
&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, propKey, value, receiver</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`设置 <span class="hljs-subst">$&#123;target&#125;</span> 的<span class="hljs-subst">$&#123;propKey&#125;</span> 属性，值为<span class="hljs-subst">$&#123;value&#125;</span>`</span>);
        target[propKey] = value
    &#125;
&#125;);
proxy.name = <span class="hljs-string">'Tom'</span>
proxy.age = <span class="hljs-number">18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b834c2fe9ec3469f952cb4649fd3f675~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li><code>has方法</code></li>
</ol>
<p>has方法接受target, propKey，用于拦截<code>propKey in proxy</code>的操作，返回一个布尔值，表示属性是否存在。如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Alice"</span>
&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
    <span class="hljs-function"><span class="hljs-title">has</span>(<span class="hljs-params">target, propKey</span>)</span> &#123;
        <span class="hljs-keyword">return</span> propKey <span class="hljs-keyword">in</span> target
    &#125;
&#125;);
<span class="hljs-keyword">if</span>(<span class="hljs-string">'name'</span> <span class="hljs-keyword">in</span> proxy)&#123;
    <span class="hljs-built_in">console</span>.log(proxy.name)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上结果返回Alice</p>
<ol start="4">
<li><code>deleteProperty方法</code></li>
</ol>
<p>可接收target, propKey，用于拦截delete操作，返回一个布尔值，表示是否删除成功。例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Alice"</span>
&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
    <span class="hljs-function"><span class="hljs-title">deleteProperty</span>(<span class="hljs-params">target, propKey</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">delete</span> target[propKey]
    &#125;
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">delete</span> proxy.name)<span class="hljs-comment">//ture</span>
<span class="hljs-built_in">console</span>.log(proxy.name)<span class="hljs-comment">//undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li><code>ownKeys方法</code></li>
</ol>
<p>可接收target，用于拦截<code>Object.getOwnPropertyNames(proxy)</code>、<code>Object.getOwnPropertySymbols(proxy)</code>、<code>Object.keys(proxy)</code>、<code>for...in</code>循环等类似操作，返回一个数组，表示对象所拥有的keys，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Alice"</span>
&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
    <span class="hljs-function"><span class="hljs-title">ownKeys</span>(<span class="hljs-params">target</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.getOwnPropertyNames(target)<span class="hljs-comment">//为了省事</span>
    &#125;
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.getOwnPropertyNames(proxy))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回["name"]</p>
<ol start="6">
<li><code>getOwnPropertyDescriptor方法</code></li>
</ol>
<p>接收target和propKey，用于拦截<code>Object.getOwnPropertyDescriptor(proxy, propKey)</code>，返回属性的描述对象。如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Alice"</span>
&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
    <span class="hljs-function"><span class="hljs-title">getOwnPropertyDescriptor</span>(<span class="hljs-params">target,propKey</span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(target, propKey)
    &#125;
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(proxy, <span class="hljs-string">'name'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71e3b23a1b234fcd88637641e07fe6c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="7">
<li><code>defineProperty方法</code></li>
</ol>
<p>接收target, propKey, propDesc，分别表示目标对象、目标对象的属性，以及属性描述配置，用于拦截<code>Object.defineProperty(proxy, propKey, propDesc）</code>和<code>Object.defineProperties(proxy, propDescs)</code>的操作，例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
    <span class="hljs-function"><span class="hljs-title">defineProperty</span>(<span class="hljs-params">target,propKey,propKeypropDesc</span>)</span>&#123;        
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.defineProperty(target, propKey, propKeypropDesc)        
    &#125;
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.defineProperty(proxy, <span class="hljs-string">'name'</span>, &#123;<span class="hljs-attr">value</span>:<span class="hljs-string">'Tom'</span>&#125;))
<span class="hljs-built_in">console</span>.log(person.name)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li><code>preventExtensions方法</code></li>
</ol>
<p>可接收target，用于拦截<code>Object.preventExtensions(proxy)</code>操作，补充说明一下preventExtensions的作用是将一个对象变成不可扩展，也就是永远不能再添加新的属性。例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Alice"</span>
&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
    <span class="hljs-function"><span class="hljs-title">preventExtensions</span>(<span class="hljs-params">target</span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.preventExtensions(target)
    &#125;
&#125;);
<span class="hljs-built_in">Object</span>.preventExtensions(proxy)
proxy.age = <span class="hljs-number">11</span>;
<span class="hljs-built_in">console</span>.log(person)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后面添加的age，并没有成功添加</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60090b27a5714ce6a78d38ee4b9a96e7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="9">
<li><code>getPrototypeOf(target)</code></li>
</ol>
<p>在使用<code>Object.getPrototypeOf(proxy)</code>会触发调用，返回一个对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Alice"</span>
&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
    <span class="hljs-function"><span class="hljs-title">getPrototypeOf</span>(<span class="hljs-params">target</span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.getPrototypeOf(target)
    &#125;
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.getPrototypeOf(proxy))
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="10">
<li><code>isExtensible(target)</code></li>
</ol>
<p>当使用<code>Object.isExtensible(proxy)</code>时会触发调用，返回一个布尔值，表示是否可扩展，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Alice"</span>
&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
    <span class="hljs-function"><span class="hljs-title">isExtensible</span>(<span class="hljs-params">target</span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.isExtensible(target)
    &#125;
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.isExtensible(proxy))<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="11">
<li><code>setPrototypeOf(target, proto)</code></li>
</ol>
<p>当调用<code>Object.setPrototypeOf(proxy, proto)</code>会触发该函数调用，例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Alice"</span>
&#125;;
<span class="hljs-keyword">let</span> proto = &#123;&#125;
<span class="hljs-keyword">let</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person,&#123;
    <span class="hljs-function"><span class="hljs-title">setPrototypeOf</span>(<span class="hljs-params">target,proto</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`设置<span class="hljs-subst">$&#123;target&#125;</span>的原型为<span class="hljs-subst">$&#123;proto&#125;</span>`</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.setPrototypeOf(target,proto)
    &#125;
&#125;);
<span class="hljs-built_in">Object</span>.setPrototypeOf(proxy,proto)
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.getPrototypeOf(person) === proto)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1dc2395b17041a2bf67cf94570b0b8e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="12">
<li><code>apply(target, object, args)</code></li>
</ol>
<p>接收三个参数target, object, args，分别表示目标对象、调用函数是的this指向以及参数列表，当<code>Proxy</code>实例作为函数调用时触发，比如<code>proxy(...args)</code>、<code>proxy.call(object, ...args)</code>、<code>proxy.apply(...)</code>，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span> (<span class="hljs-params">x,y</span>)</span>&#123; <span class="hljs-keyword">return</span> x + y&#125;
<span class="hljs-keyword">let</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(f,&#123;
    <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">target, object, args</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`调用了f`</span>);
        <span class="hljs-keyword">return</span> f.call(object,...args)
    &#125;
&#125;)
<span class="hljs-built_in">console</span>.log(proxy(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90805d8284b3477db317f1563da5be53~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="13">
<li><code>construct(target, args)</code></li>
</ol>
<p>接收target和args，表示目标函数即参数列表，当<code> Proxy</code> 实例作为构造函数时触发该函数调用，比如<code>new proxy(...args)</code>，例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>)</span>&#123; &#125;
<span class="hljs-keyword">let</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(F,&#123;
    <span class="hljs-function"><span class="hljs-title">construct</span>(<span class="hljs-params">target,  args</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`调用了construct`</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> target(...args)
    &#125;
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> proxy())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47b81541087c43a59133ecc4d0f0b02a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上这些方法都被称为捕获器，这些捕获器分别捕获对象不同的操作行为。</p>
<p>下面我们通过一个简单例子，来进一步搞清楚目标对象和代理对象之间的关系。</p>
<p>如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Alice"</span>
&#125;;
<span class="hljs-keyword">var</span> proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(person, &#123;
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, propKey, value, receiver</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`设置 <span class="hljs-subst">$&#123;target&#125;</span> 的<span class="hljs-subst">$&#123;propKey&#125;</span> 属性，值为<span class="hljs-subst">$&#123;value&#125;</span>`</span>);
        target[propKey] = value
    &#125;
&#125;);        
proxy.age = <span class="hljs-number">18</span>
person.sex = <span class="hljs-string">'female'</span>
<span class="hljs-built_in">console</span>.log(person,proxy)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05a6e977ad564b8db6fbbf66a4e78447~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上述例子，我们可以得出以下4点结论：</p>
<ol>
<li>代理对象不等于目标对象，他是目标对象的包装品</li>
<li>目标对象既可以直接操作，也可以被代理对象操作，且两者相互关联</li>
<li>如果直接操作目标对象，则会绕过代理定义的各种拦截行为</li>
<li>如果用了代理，那肯定是希望给对象的操作嵌入我们定义的特殊行为，所以一般就操作代理对象就好</li>
</ol>
<p>如果你还模糊，那我来给你看看Proxy真面目。....也没啥好说的，其实就是一个构造函数,并且接受两个参数target和handler，返回代理对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Proxy</span>(<span class="hljs-params">target,handler</span>)</span>&#123;
    <span class="hljs-comment">//...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这下彻底理解了Proxy，那我们来看看它的应用吧。由于代理模式是非常典型的编程模式，会在很多地方被应用，我们以Vue3数据响应式系统为例来简单讲讲！</p>
<p>Vue3定义了一系列的响应式API，比如reactive、ref等等，它们的特点是：当时数据发生变化时，页面会对应更新UI，而底层用的就是Proxy！我以reactive为例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key</span>)</span> &#123;
            <span class="hljs-keyword">return</span> target[key]
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, val</span>)</span> &#123;
            target[key] = val
            <span class="hljs-comment">// 这里当数据变化时，更新界面，于是我们考虑到这里需要update方法用户更新</span>
            <span class="hljs-comment">// 执行updata操作...</span>
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，数据对象obj通过reactive包装成了代理对象，当数据发生变化时，会调用set方法，在更新数据的同时，同时执行一些update的操作</p>
<p>这就是典型的代理模式应用~</p>
<p>到这里应该没有什么问题了吧，有问题欢迎下方留言告知，谢谢！</p>
<p>END~</p></div>  
</div>
            