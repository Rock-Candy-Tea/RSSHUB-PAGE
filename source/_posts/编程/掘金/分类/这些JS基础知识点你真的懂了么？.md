
---
title: '这些JS基础知识点你真的懂了么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25dbd69468724dc987b68af7c5e3005a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 19:17:11 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25dbd69468724dc987b68af7c5e3005a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 9 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h2 data-id="heading-0">变量类型和计算</h2>
<h3 data-id="heading-1">typeof能判断哪些类型</h3>
<ul>
<li>识别所有值类型</li>
<li>识别函数</li>
<li>判断是否是引用类型（不可再细分）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//判断所有的值类型</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-literal">undefined</span> <span class="hljs-comment">// undefined</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-string">'abc'</span> <span class="hljs-comment">// string</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-number">123</span> <span class="hljs-comment">// number</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-literal">true</span> <span class="hljs-comment">// boolean</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'sdd'</span>)  <span class="hljs-comment">// symbol</span>

<span class="hljs-comment">//能判断函数</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">console</span>.log <span class="hljs-comment">// function</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125; <span class="hljs-comment">// function</span>

<span class="hljs-comment">//能识别引用类型（不能再细分）</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-literal">null</span> <span class="hljs-comment">// object</span>
<span class="hljs-keyword">typeof</span> [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>] <span class="hljs-comment">// object</span>
<span class="hljs-keyword">typeof</span> &#123;<span class="hljs-attr">a</span>:<span class="hljs-number">123</span>&#125; <span class="hljs-comment">// object</span>
 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">何时使用===，何时使用==</h3>
<ul>
<li><code>==</code> 抽象相等，比较时，会隐式进行类型转换，再进行值比较</li>
<li><code>===</code> 严格相等，会比较两个值的类型和值</li>
</ul>
<h3 data-id="heading-3">值类型和引用类型的区别</h3>
<ul>
<li><code>值类型</code>：基本类型，Number,String,Boolean,undefined,Null(指向空指针，特殊的引用类型),Symbol，BigInt</li>
<li><code>引用类型</code>: Object,Array,Function，Date,Map,Set,WeakSet,WeakMap</li>
</ul>



































<table><thead><tr><th align="left">区别</th><th align="left">值类型</th><th align="left">引用类型</th></tr></thead><tbody><tr><td align="left">存储位置</td><td align="left">栈中</td><td align="left">堆中（变量名在栈内存中，变量值在堆内存中）</td></tr><tr><td align="left">占用空间</td><td align="left">固定</td><td align="left">不固定</td></tr><tr><td align="left">赋值方式</td><td align="left">拷贝变量内容</td><td align="left">拷贝引用地址</td></tr><tr><td align="left">动态属性</td><td align="left">不能添加属性</td><td align="left">可动态添加属性</td></tr><tr><td align="left">检测方法</td><td align="left">typeof</td><td align="left">instanceof</td></tr></tbody></table>
<h3 data-id="heading-4">变量计算--强制类型转换</h3>
<ul>
<li>字符串拼接</li>
<li>==
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//除了 ==null  之外，其它都一律使用 === ，如</span>
<span class="hljs-keyword">let</span> obj = &#123;<span class="hljs-attr">x</span>:<span class="hljs-number">100</span>&#125;
<span class="hljs-keyword">if</span>(obj.a == <span class="hljs-literal">null</span>)&#123;&#125;
<span class="hljs-comment">//相当于:   if（obj.a == null || obj.a == undefined)&#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>if语句和逻辑运算</li>
<li>判断true/false
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//以下是falsely变量，除此之外都是truly变量</span>
!!<span class="hljs-number">0</span> === <span class="hljs-literal">false</span>
!!<span class="hljs-literal">NaN</span> === <span class="hljs-literal">false</span>
!!<span class="hljs-string">''</span> === <span class="hljs-literal">false</span>
!!<span class="hljs-literal">null</span> === <span class="hljs-literal">false</span>
!!<span class="hljs-literal">undefined</span> === <span class="hljs-literal">false</span>
!!<span class="hljs-literal">false</span> === <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 字符串拼接</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">100</span> + <span class="hljs-number">10</span> <span class="hljs-comment">//100</span>
<span class="hljs-keyword">var</span> b = <span class="hljs-number">100</span> + <span class="hljs-string">'10'</span> <span class="hljs-comment">//10010</span>
<span class="hljs-keyword">var</span> c = <span class="hljs-literal">true</span> + <span class="hljs-string">'10'</span> <span class="hljs-comment">// true10</span>

<span class="hljs-comment">// == 运算符</span>
<span class="hljs-number">100</span> == <span class="hljs-string">'100'</span> <span class="hljs-comment">//true</span>
<span class="hljs-number">0</span> == <span class="hljs-string">''</span> <span class="hljs-comment">//true</span>
<span class="hljs-number">0</span> == <span class="hljs-literal">false</span> <span class="hljs-comment">// true</span>
<span class="hljs-literal">false</span> == <span class="hljs-string">''</span> <span class="hljs-comment">// true</span>
<span class="hljs-literal">null</span> == <span class="hljs-literal">undefined</span> <span class="hljs-comment">//true</span>
[<span class="hljs-number">10</span>] == <span class="hljs-number">10</span> <span class="hljs-comment">// true</span>
[] == <span class="hljs-number">0</span> <span class="hljs-comment">// true</span>
[] == <span class="hljs-literal">false</span> <span class="hljs-comment">// true</span>
![] == <span class="hljs-literal">false</span> <span class="hljs-comment">// true</span>
<span class="hljs-literal">null</span> == <span class="hljs-literal">false</span> <span class="hljs-comment">// false</span>

<span class="hljs-comment">//  语句</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-literal">true</span>
<span class="hljs-keyword">if</span>(a)&#123;&#125;
<span class="hljs-keyword">var</span> b = <span class="hljs-number">100</span>
<span class="hljs-keyword">if</span>(b)&#123;&#125; <span class="hljs-comment">// 把数字转换为true</span>
<span class="hljs-keyword">var</span> c = <span class="hljs-string">''</span>
<span class="hljs-keyword">if</span>(c)&#123;&#125; <span class="hljs-comment">// 把空字符串转换为false</span>

<span class="hljs-comment">// 逻辑运算</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>&&<span class="hljs-number">0</span>); <span class="hljs-comment">// 0 把10转换成true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">''</span> || <span class="hljs-string">'abc'</span>); <span class="hljs-comment">// 'abc' 把空字符串转换为false</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-built_in">window</span>.abc); <span class="hljs-comment">// window.abc是undefined 把非undefined转换成true</span>

<span class="hljs-comment">//判断一个变量会被当做true还是false</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">100</span>
<span class="hljs-built_in">console</span>.log(!!a); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">手写深拷贝</h3>
<p><a href="https://juejin.cn/post/6996828614465421343" target="_blank" title="https://juejin.cn/post/6996828614465421343">看了此文我就不信你还不懂浅拷贝、深拷贝</a></p>
<h2 data-id="heading-6">原型和原型链</h2>
<p><a href="https://juejin.cn/post/6994632915648774152" target="_blank" title="https://juejin.cn/post/6994632915648774152">彻底搞懂JS原型、原型链和继承</a></p>
<h2 data-id="heading-7">class和继承</h2>
<h3 data-id="heading-8">class</h3>
<ul>
<li>constructor</li>
<li>属性</li>
<li>方法</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span></span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name,age</span>)</span>&#123;
<span class="hljs-built_in">this</span>.name = name
<span class="hljs-built_in">this</span>.age = age
&#125;
<span class="hljs-function"><span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`姓名： <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>, 年龄： <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>`</span>)
&#125;
&#125;

<span class="hljs-comment">// 通过类new 对象/实例</span>
<span class="hljs-keyword">const</span> pp = <span class="hljs-keyword">new</span> Student(<span class="hljs-string">'小鱼'</span>,<span class="hljs-number">18</span>)
<span class="hljs-built_in">console</span>.log(pp.name,pp.age) <span class="hljs-comment">// 小鱼 18</span>
pp.sayHi()  <span class="hljs-comment">// 姓名： 小鱼, 年龄： 18</span>

<span class="hljs-keyword">const</span> cc = <span class="hljs-keyword">new</span> Student(<span class="hljs-string">'小C'</span>,<span class="hljs-number">16</span>)
<span class="hljs-built_in">console</span>.log(cc.name,cc.age)
cc.sayHi()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25dbd69468724dc987b68af7c5e3005a~tplv-k3u1fbpfcp-watermark.image" alt="原型链.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>每个class都有显示原型 prototype</li>
<li>每个实例都有隐式原型 <strong>proto</strong></li>
<li>实例的 <strong>proto</strong> 指向对应的class的prototype</li>
</ul>
<p><strong>执行规则</strong></p>
<ul>
<li>获取属性pp.name 或 执行方法 pp.sayHi()时</li>
<li>先在自身属性和方法寻找</li>
<li>如果找不到则 自动去 __proto__中查找</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// class 实际上是函数，是语法糖</span>
<span class="hljs-keyword">typeof</span> People <span class="hljs-comment">// function</span>
<span class="hljs-keyword">typeof</span> Student <span class="hljs-comment">// function</span>

<span class="hljs-comment">// 隐式原型和显示原型</span>
pp.__proto__   <span class="hljs-comment">//隐式原型 </span>
Student.prototype <span class="hljs-comment">// 显示原型</span>
pp.__proto__ === Student.prototype <span class="hljs-comment">// true</span>

Student.prototype.__proto__
People.prototype
People.prototype === Student.prototype.__proto__  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">继承</h3>
<ul>
<li>extends</li>
<li>super (父类)</li>
<li>扩展和重写</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">People</span></span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span>&#123;
<span class="hljs-built_in">this</span>.name =name
&#125;
<span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> eat something`</span>)
&#125;
&#125;
<span class="hljs-comment">// 子类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">People</span></span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name,age</span>)</span>&#123;
<span class="hljs-built_in">super</span>(name)
<span class="hljs-built_in">this</span>.age = age
&#125;
<span class="hljs-function"><span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`姓名： <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>, 年龄： <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>`</span>)
&#125;
&#125;
<span class="hljs-comment">// 子类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Teacher</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">People</span></span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name,major</span>)</span>&#123;
<span class="hljs-built_in">super</span>(name)
<span class="hljs-built_in">this</span>.major = major
&#125;
<span class="hljs-function"><span class="hljs-title">teach</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> 教授 <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.major&#125;</span>`</span>)
&#125;
&#125;

<span class="hljs-keyword">const</span> pp = <span class="hljs-keyword">new</span> Student(<span class="hljs-string">'小鱼'</span>,<span class="hljs-number">18</span>)
<span class="hljs-built_in">console</span>.log(pp.name,pp.age) <span class="hljs-comment">// 小鱼 18</span>
pp.sayHi()  <span class="hljs-comment">//姓名： 小鱼, 年龄： 18</span>
pp.eat() <span class="hljs-comment">// 小鱼 eat something</span>
<span class="hljs-comment">//实例</span>
<span class="hljs-keyword">const</span> lu = <span class="hljs-keyword">new</span> Teacher(<span class="hljs-string">'陆老师'</span>,<span class="hljs-string">'语文'</span>)
<span class="hljs-built_in">console</span>.log(lu.name,lu.major) <span class="hljs-comment">// 陆老师 语文</span>
lu.teach()  <span class="hljs-comment">// 陆老师 教授 语文</span>
pp.eat() <span class="hljs-comment">// 陆老师 eat something</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">instanceof</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 参照上面继承</span>
pp <span class="hljs-keyword">instanceof</span> Student <span class="hljs-comment">// true</span>
pp <span class="hljs-keyword">instanceof</span> People <span class="hljs-comment">// true</span>
pp <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span> <span class="hljs-comment">//true</span>

[] <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span> <span class="hljs-comment">// true</span>
[] <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span> <span class="hljs-comment">// true</span>

&#123;&#125; <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span> <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">题目</h2>
<h3 data-id="heading-12">如何判断数组</h3>
<ol>
<li><code>Object.prototype.toString.call()</code></li>
<li><code>Array.isArrray()</code></li>
<li><code>instanceof</code>: 判断一个变量是否某个对象的实例</li>
<li><code>Array.prototype.isPrototypeOf</code>: 利用isPrototypeOf()方法，判定Array是不是在obj的原型链中</li>
<li><code>constructor</code>: 返回对创建此对象的数组函数的引用，就是返回对象相对应的构造函数</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isArray</span>(<span class="hljs-params">obj</span>)</span>&#123;
　 <span class="hljs-comment">// return Object.prototype.toString.call(obj).slice(8,-1) === 'Array';</span>
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(obj) === <span class="hljs-string">'[object Array]'</span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isArray</span>(<span class="hljs-params">obj</span>)</span>&#123;
　　<span class="hljs-keyword">return</span>  <span class="hljs-built_in">Array</span>.isArrray(obj);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isArray</span>(<span class="hljs-params">obj</span>)</span>&#123;
　　<span class="hljs-keyword">return</span> obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isArray</span>(<span class="hljs-params">obj</span>)</span>&#123;
　　<span class="hljs-keyword">return</span> obj.constructor === <span class="hljs-built_in">Array</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isArray</span>(<span class="hljs-params">obj</span>)</span>&#123;
　　<span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>.prototype.isPrototypeOf(obj)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">手写jquery</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">jQuery</span></span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">selector</span>)</span>&#123;
<span class="hljs-keyword">const</span> result = <span class="hljs-built_in">document</span>.querySelectorAll(selector)
<span class="hljs-keyword">const</span> length = result.length
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>; i<length;i++)&#123;
<span class="hljs-built_in">this</span>[i] = result[i]
&#125;
<span class="hljs-built_in">this</span>.length = length
<span class="hljs-built_in">this</span>.selector = selector
&#125;
<span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">index</span>)</span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>[index]
&#125;
<span class="hljs-function"><span class="hljs-title">each</span>(<span class="hljs-params">fn</span>)</span>&#123;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>; i<<span class="hljs-built_in">this</span>.length;i++)&#123;
<span class="hljs-keyword">const</span> elem = <span class="hljs-built_in">this</span>[i]
fn(elem)
&#125;
&#125;
<span class="hljs-function"><span class="hljs-title">on</span>(<span class="hljs-params">type,fn</span>)</span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.each(<span class="hljs-function"><span class="hljs-params">elem</span>=></span>&#123;
elem.addEventListener(type,fn,<span class="hljs-literal">false</span>)
&#125;)
&#125;
<span class="hljs-comment">//扩展很多DOM API</span>
&#125;

<span class="hljs-comment">// 插件</span>
jQuery.prototype.dialog = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">info</span>)</span>&#123;
alert(info)
&#125;
<span class="hljs-comment">//造轮子</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">myJQuery</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">jQuery</span></span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">selector</span>)</span>&#123;
<span class="hljs-built_in">super</span>(selector)
&#125;
<span class="hljs-comment">//扩展自己的方法</span>
<span class="hljs-function"><span class="hljs-title">addClass</span>(<span class="hljs-params">className</span>)</span>&#123;

&#125;
&#125;

<span class="hljs-comment">//调用demo</span>
<span class="hljs-keyword">const</span> $p = <span class="hljs-keyword">new</span> jQuery(<span class="hljs-string">'p'</span>)
$p.get(<span class="hljs-number">1</span>)
$p.each(<span class="hljs-function"><span class="hljs-params">elem</span>=></span><span class="hljs-built_in">console</span>.log(elem.nodeName))
$p.on(<span class="hljs-string">'click'</span>,<span class="hljs-function">()=></span>alert(<span class="hljs-string">'clicked'</span>))
$p.dialog(<span class="hljs-string">'test'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">作用域和闭包</h2>
<p><strong>作用域</strong></p>
<ul>
<li>全局作用域</li>
<li>函数作用域</li>
<li>块级作用域</li>
</ul>
<p><strong>自由变量</strong></p>
<ul>
<li>一个变量在当前作用域没有定义，但被使用了</li>
<li>向上级作用域，一层一层依次寻找，直到找到为止</li>
<li>如果到全局作用域都没有找到，则报错 XX is not defined</li>
</ul>
<p><strong>闭包</strong>
作用域应用的特殊情况，有2种表现：</p>
<ul>
<li>函数作为参数被传递</li>
<li>函数作为返回值被返回</li>
</ul>
<blockquote>
<p>自由变量的查找: 是在<code>函数定义</code>的地方，向上级作用域查找； 不是在执行的地方！！！</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//函数作为返回值</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">let</span> a = <span class="hljs-number">100</span>
<span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(a)
&#125;
&#125;
<span class="hljs-keyword">const</span> fn = create()
<span class="hljs-keyword">let</span> a = <span class="hljs-number">200</span>
fn()  <span class="hljs-comment">// 100</span>

<span class="hljs-comment">//函数作为参数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">print</span>(<span class="hljs-params">fn</span>)</span>&#123;
<span class="hljs-keyword">let</span> a = <span class="hljs-number">200</span>
fn()
&#125;
<span class="hljs-keyword">let</span> a = <span class="hljs-number">100</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(a)
&#125;
print(fn) <span class="hljs-comment">//100</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">this在不同场景，如何取值</h3>
<blockquote>
<p>this取值，是在<code>函数执行的时候确认</code>，不是在函数定义时确认</p>
</blockquote>
<ul>
<li>作为普通函数</li>
<li>使用 call apply bind</li>
<li>作为对象方法调用</li>
<li>在class方法中调用</li>
<li>箭头函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
&#125;
fn1() <span class="hljs-comment">// window</span>

fn1.call(&#123;<span class="hljs-attr">x</span>:<span class="hljs-number">100</span>&#125;) <span class="hljs-comment">// &#123;x:100&#125;</span>

<span class="hljs-keyword">let</span> fn2 = fn1.bind(x:<span class="hljs-number">200</span>)
fn2() <span class="hljs-comment">// &#123;x:200&#125;</span>

<span class="hljs-keyword">const</span> pp = &#123;
<span class="hljs-attr">name</span>:<span class="hljs-string">'pp'</span>,
<span class="hljs-function"><span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-comment">//this 即当前对象</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
&#125;,
<span class="hljs-function"><span class="hljs-title">wait</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-comment">// this === window</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
&#125;)
&#125;,
<span class="hljs-function"><span class="hljs-title">wait2</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
<span class="hljs-comment">// this 即当前对象</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
&#125;)
&#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">People</span></span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span>&#123;
<span class="hljs-built_in">this</span>.name = name
&#125;
<span class="hljs-function"><span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
&#125;
&#125;
<span class="hljs-keyword">const</span> pp = <span class="hljs-keyword">new</span> People(<span class="hljs-string">'小玉儿'</span>)
pp.sayHi() <span class="hljs-comment">// 指向 pp对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">手写bind函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params">a,b,c</span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'this'</span>,<span class="hljs-built_in">this</span>) <span class="hljs-comment">// this &#123; x:100&#125;</span>
<span class="hljs-built_in">console</span>.log(a,b,c)  <span class="hljs-comment">// 10 20 30</span>
<span class="hljs-keyword">return</span> <span class="hljs-string">'this is fn1'</span>
&#125;
<span class="hljs-keyword">const</span> fn2 = fn1.bind(&#123;<span class="hljs-attr">x</span>:<span class="hljs-number">100</span>&#125;,<span class="hljs-number">10</span>,<span class="hljs-number">20</span>,<span class="hljs-number">30</span>)
<span class="hljs-keyword">const</span> res = fn2()
<span class="hljs-built_in">console</span>.log(res) <span class="hljs-comment">// this is fn1</span>

<span class="hljs-comment">//模拟bind</span>
<span class="hljs-built_in">Function</span>.prototype.bind1 = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-comment">//将参数拆解为数组</span>
<span class="hljs-keyword">const</span> args = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>)

<span class="hljs-comment">//获取 this（数组第一项）</span>
<span class="hljs-keyword">const</span> t = args.shift()
 
 <span class="hljs-comment">//fn1.bind(...)中的fn1</span>
<span class="hljs-keyword">const</span> self = <span class="hljs-built_in">this</span>

<span class="hljs-comment">//返回一个函数</span>
<span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">return</span> self.apply(t,args)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">实际开发中闭包应用场景</h3>
<ul>
<li>隐藏数据</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 闭包隐藏数据，只提供API</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createCache</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">const</span> data = &#123;&#125; <span class="hljs-comment">// 闭包中的数据，被隐藏，不被外界访问</span>
<span class="hljs-keyword">return</span> &#123;
<span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">key,value</span>)</span>&#123;
data[key] = value 
&#125;,
<span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">key</span>)</span>&#123;
<span class="hljs-keyword">return</span> data[key]
&#125;
&#125;
&#125;
<span class="hljs-keyword">const</span> a = createCache()
a.set(<span class="hljs-string">'a1'</span>,<span class="hljs-number">100</span>)
<span class="hljs-built_in">console</span>.log(a.get(a1))
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            