
---
title: '「JavaScript进阶」一文吃透深浅拷贝'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c67131a878bd4f0c9a7136937386d489~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 02:37:18 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c67131a878bd4f0c9a7136937386d489~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<blockquote>
<p>文章里的每个案例都是我亲自编写并验证的，建议阅读文章时，可以在浏览器执行案例，会更有利于帮助理解。</p>
</blockquote>
<p>JavaScript 系列文章：<a href="https://juejin.cn/post/6940972802376171551#heading-1" target="_blank">JavaScript进阶</a></p>
<h2 data-id="heading-1">变量存储类型</h2>
<p>要理解深浅拷贝，先要熟悉变量存储类型，分为<code>基本数据类型</code>（值类型）和<code>引用数据类型</code>（复杂数据类型）。基本数据类型的值是直接存在栈内存的，而引用数据类型的栈内存保存的是内存地址，值保存在堆内存中。</p>























<table><thead><tr><th>变量存储类型</th><th>值</th><th>地址值</th><th>例子</th></tr></thead><tbody><tr><td>基本数据类型</td><td>存储在<code>栈</code>中</td><td></td><td>string、bool、number、undefined、null、symbol(ES6新增)</td></tr><tr><td>引用数据类型</td><td>存储在<code>堆</code>中</td><td>存储在<code>栈</code>中</td><td>数组、对象、函数、正则</td></tr></tbody></table>
<h3 data-id="heading-2">基本数据类型</h3>
<blockquote>
<p>直接把值存在 <strong>栈</strong> 中的数据。如<code>string、bool、number、undefined、null、symbol(ES6新增)</code></p>
</blockquote>
<ul>
<li>
<p>1、使用<code>typeof()</code>判断<code>null</code>，打印的是<code>object</code>，但是 <code>null</code> 是基本数据类型。基本数据类型存储的是值，是没有函数可以调用的，比如调用<code>null.toString()</code>就会报错</p>
</li>
<li>
<p>2、<code>null</code> 和 <code>undefined</code> 的区别</p>
<ul>
<li><code>null</code>：js 的关键字，是一个特殊的对象值，表示<code>空值</code>，typeof运算是<code>object</code></li>
<li><code>undefined</code>：预定义的全局变量，表示<code>未定义</code>，用typeof运算是<code>undefined</code></li>
</ul>
</li>
<li>
<p>3、关于 <code>Symbol</code>，可以去看文章 <a href="https://juejin.cn/post/6943906724390633502#heading-3" target="_blank">Symbol 是不是构造函数？</a></p>
</li>
</ul>
<h3 data-id="heading-3">引用数据类型</h3>
<blockquote>
<p>对象的引用地址存在 <strong>栈</strong> 中，对象的数据存在 <strong>堆</strong> 中。如<code>数组、对象、函数、正则</code></p>
</blockquote>
<p>引用类型用typeof运算后，会输出<code>object</code></p>
<h3 data-id="heading-4">检测数据类型的方法</h3>
<ul>
<li><strong>1.typeof</strong></li>
</ul>














<table><thead><tr><th>typeof是检测数据类型的运算符，输出的字符串就是对应的类型。有以下局限性1）</th></tr></thead><tbody><tr><td>1）<code>typeOf(null)</code>输出的是<code>object</code>，但 <code>null</code> 是基本数据类型</td></tr><tr><td>2）无法区分对象具体是什么类型，比如<code>typeof([1])</code>和<code>typeof(&#123;1&#125;)</code>输出的都是<code>object</code></td></tr></tbody></table>
<ul>
<li>
<p><strong>2.instanceOf</strong></p>
<p>检查某个实例是否属于某个类</p>
</li>
<li>
<p><strong>3.constructor</strong></p>
<p>获取当前实例的构造器，详见 <a href="https://juejin.cn/post/6943906724390633502#heading-4" target="_blank">constructor 属性是否只读？</a></p>
</li>
<li>
<p><strong>4.Object.prototype.toString.call</strong></p>
<p>获取当前实例所属类的信息，详见 <a href="https://juejin.cn/post/6940963094948478990#heading-3" target="_blank">通过 call 改变 this 指向来进行类型判断</a></p>
</li>
</ul>
<h2 data-id="heading-5">赋值、浅拷贝、深拷贝的区别</h2>
<p>从生成的<code>新对象与原数据是否指向同一对象</code>，以及<code>改变新对象是否会导致原数据发生改变行比较</code>（根据对象的第一层属性是 基本数据类型 和 引用数据类型分类）。</p>





























<table><thead><tr><th>操作类型</th><th>指向同一对象</th><th>第一层属性是基本类型</th><th>第一层属性是引用类型</th></tr></thead><tbody><tr><td>赋值</td><td>是</td><td>改变<code>会</code>导致原数据改变</td><td>改变<code>会</code>导致原数据改变</td></tr><tr><td>浅拷贝</td><td>是</td><td>改变<code>不会</code>导致原数据改变</td><td>改变<code>会</code>导致原数据改变</td></tr><tr><td>深拷贝</td><td>是</td><td>改变<code>不会</code>导致原数据改变</td><td>改变<code>不会</code>导致原数据改变</td></tr></tbody></table>
<h3 data-id="heading-6">赋值</h3>
<blockquote>
<p>符号<code>=</code>就是赋值操作。分为对<code>基本数据类型</code>和<code>引用数据类型赋值</code>两种情况</p>
</blockquote>
<ul>
<li>1.基本数据类型赋值</li>
</ul>
<p>基本数据类型的赋值操作是<code>值引用</code>，相互之间没有影响</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-string">'谷底飞龙'</span>;
<span class="hljs-keyword">var</span> b = a; <span class="hljs-comment">// 将 a 赋值给 b</span>
a = <span class="hljs-string">'天下无敌'</span>; <span class="hljs-comment">// 修改 a 的值为 '天下无敌'</span>
<span class="hljs-built_in">console</span>.log(b); <span class="hljs-comment">// 打印 b 的值，仍为 '谷底飞龙'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2.引用数据类型赋值</li>
</ul>
<p>引用数据类型的赋值是<code>地址引用</code>，两个变量指向同一个地址，相互之间有影响</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'谷底飞龙'</span> 
&#125;;
<span class="hljs-keyword">var</span> b = a; <span class="hljs-comment">// 将 a 赋值给 b</span>
a.name = <span class="hljs-string">'天下无敌'</span>; <span class="hljs-comment">// 修改 a.name 的值为 '天下无敌'</span>
<span class="hljs-built_in">console</span>.log(b.name); <span class="hljs-comment">// 打印 b.name 的值，变为 '天下无敌'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在开发过程中，我们有时候并不希望引用数据类型的赋值操作中的两个变量相互影响，这就需要<code>浅拷贝</code>和<code>深拷贝</code></p>
<h3 data-id="heading-7">浅拷贝</h3>
<blockquote>
<p>浅拷贝只拷贝原对象的第一层属性。即拷贝A对象里面的数据，但是不拷贝A对象里面的子对象。</p>
</blockquote>
<p>如果属性是基本数据类型，拷贝的就是基本类型的值。 如果属性是引用数据类型，拷贝的是引用类型的内存地址</p>
<h4 data-id="heading-8">如何实现一个浅拷贝？</h4>
<p>为了更直观的理解浅拷贝及其特点，我们来手动实现一个浅拷贝函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 对 obj 进行浅拷贝</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowCopy</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">'object'</span> && obj !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">let</span> copy = <span class="hljs-built_in">Array</span>.isArray(obj) ? [] : &#123;&#125;;
    <span class="hljs-comment">// 遍历原对象 obj，将第一层属性赋值给新对象</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> p <span class="hljs-keyword">in</span> obj) &#123;
      copy[p] = obj[p]
    &#125;
    <span class="hljs-comment">// 返回的新对象就是浅拷贝后的对象</span>
    <span class="hljs-keyword">return</span> copy
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 如果是基本类型，直接返回</span>
    <span class="hljs-keyword">return</span> obj
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到，浅拷贝只拷贝了原数据的第一层属性。现在来验证下前面表格中的内容：</p>
<ul>
<li>如果第一层属性是基本数据类型，改变新对象<code>不会</code>导致原数据发生改变；</li>
<li>如果第一层属性是引用数据类型，改变新对象<code>会</code>导致原数据发生改变</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 原数据是对象</span>
<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span>,
  <span class="hljs-attr">person</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'谷底飞龙'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">28</span>,
  &#125;,
&#125;
<span class="hljs-comment">// 浅拷贝</span>
<span class="hljs-keyword">var</span> copy = shallowCopy(obj);

<span class="hljs-comment">// 改变原数据第一层属性 color （基本数据类型）</span>
copy.color = <span class="hljs-string">'yellow'</span>;
<span class="hljs-comment">// 改变原数据第一层属性 person（引用数据类型）</span>
copy.person.name = <span class="hljs-string">'天下无敌'</span>;
<span class="hljs-comment">// 原数据中 color 仍为 “red“，但是 name 会被修改为 “天下无敌”</span>
<span class="hljs-built_in">console</span>.log(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行后的结果如下：
<img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c67131a878bd4f0c9a7136937386d489~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果把原数据换成数组，效果也是一样的，如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 原数据是数组</span>
<span class="hljs-keyword">var</span> obj = [
  <span class="hljs-string">'red'</span>,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'谷底飞龙'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">28</span>,
  &#125;,
]
<span class="hljs-comment">// 浅拷贝</span>
<span class="hljs-keyword">var</span> copy = shallowCopy(obj);

<span class="hljs-comment">// 改变原数据第一层属性 color （基本数据类型）</span>
copy[<span class="hljs-number">0</span>] = <span class="hljs-string">'yellow'</span>;
<span class="hljs-comment">// 改变原数据第一层属性 person（引用数据类型）</span>
copy[<span class="hljs-number">1</span>].name = <span class="hljs-string">'天下无敌'</span>;
<span class="hljs-comment">// 原数据中 color 仍为 “red“，但是 name 会被修改为 “天下无敌”</span>
<span class="hljs-built_in">console</span>.log(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行后的结果如下：
<img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24421f1040cb408e9d16bf68bba03af2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果原数据是基本数据类型呢？</p>
<ul>
<li>之前讲<code>赋值</code>的时候，提到<code>浅拷贝</code>和<code>深拷贝</code>是为了解决引用数据类型（复杂数据类型）赋值存在的问题才引入的。所以如果原数据是基本数据类型，一般只需要赋值操作就行。如果用上面实现的浅拷贝函数 <code>shallowCopy()</code>来拷贝基本数据类型，直接返回原数据。</li>
</ul>
<h4 data-id="heading-9">有哪些常用的浅拷贝?</h4>
<p>在实际开发中，我们很少需要自己去写一个浅拷贝函数，这里例举几个常用的浅拷贝</p>
<p><strong>1.对象 Object.assign()</strong></p>
<p>在 ES6 提供了<code>Object.assign(target, ...sources)</code> 来实现浅拷贝，第一个参数 <code>target</code>是目标对象，后面的参数<code>...sources</code>是原对象。我们现在来改造下前面的案例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 原数据是对象</span>
<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span>,
  <span class="hljs-attr">person</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'谷底飞龙'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">28</span>,
  &#125;,
&#125;

<span class="hljs-comment">// 改用 Object.assign() 实现浅拷贝</span>
<span class="hljs-keyword">var</span> copy = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;,obj);

<span class="hljs-comment">// 改变原数据第一层属性 color （基本数据类型）</span>
copy.color = <span class="hljs-string">'yellow'</span>;
<span class="hljs-comment">// 改变原数据第一层属性 person（引用数据类型）</span>
copy.person.name = <span class="hljs-string">'天下无敌'</span>;
<span class="hljs-comment">// 原数据中 color 仍为 “red“，但是 name 会被修改为 “天下无敌”</span>
<span class="hljs-built_in">console</span>.log(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果与<code>shallowCopy()</code>效果一样</p>
<p><code>注：</code> Object.assign() 一般用于对象的浅拷贝，用来处理数组时，会把数组视为对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Object.assign 把数组视为属性名为 0、1、2 的对象</span>
<span class="hljs-comment">// 源数组的 0 号属性 7 覆盖了目标数组的 0 号属性1，以此类推</span>
<span class="hljs-built_in">Object</span>.assign([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>], [<span class="hljs-number">7</span>,<span class="hljs-number">8</span>]); <span class="hljs-comment">// [7,8,3]</span>
<span class="hljs-built_in">Object</span>.assign([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>], [<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">8</span>]); <span class="hljs-comment">// [6,7,8]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.数组 Array.concat()</strong></p>
<p>对数组的浅拷贝，可以使用<code>Array.concat()</code>，这也是合并数组比较常用的方式。我们把之前的案例修改下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 原数据是数组</span>
<span class="hljs-keyword">var</span> obj = [
  <span class="hljs-string">'red'</span>,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'谷底飞龙'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">28</span>,
  &#125;,
]

<span class="hljs-comment">// 改用 [].concat() 实现浅拷贝</span>
<span class="hljs-keyword">var</span> copy = [].concat(obj);

<span class="hljs-comment">// 改变原数据第一层属性 color （基本数据类型）</span>
copy[<span class="hljs-number">0</span>] = <span class="hljs-string">'yellow'</span>;
<span class="hljs-comment">// 改变原数据第一层属性 person（引用数据类型）</span>
copy[<span class="hljs-number">1</span>].name = <span class="hljs-string">'天下无敌'</span>;
<span class="hljs-comment">// 原数据中 color 仍为 “red“，但是 name 会被修改为 “天下无敌”</span>
<span class="hljs-built_in">console</span>.log(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果与<code>shallowCopy()</code>效果一样</p>
<p><strong>3.扩展运算符 &#123; ...obj &#125;</strong></p>
<p>使用扩展运算符<code>&#123; ...obj &#125;</code>可以对数组和对象进行浅拷贝，我们这里用原数据是对象的情况来做案例，你也可以自己把原数据换成数组试试。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 原数据是对象</span>
<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span>,
  <span class="hljs-attr">person</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'谷底飞龙'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">28</span>,
  &#125;,
&#125;

<span class="hljs-comment">// 改用扩展运算符 &#123;...obj&#125; 实现浅拷贝</span>
<span class="hljs-keyword">var</span> copy = &#123;...obj&#125;;

<span class="hljs-comment">// 改变原数据第一层属性 color （基本数据类型）</span>
copy.color = <span class="hljs-string">'yellow'</span>;
<span class="hljs-comment">// 改变原数据第一层属性 person（引用数据类型）</span>
copy.person.name = <span class="hljs-string">'天下无敌'</span>;
<span class="hljs-comment">// 原数据中 color 仍为 “red“，但是 name 会被修改为 “天下无敌”</span>
<span class="hljs-built_in">console</span>.log(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行效果与其它浅拷贝方式的是一样的</p>
<h3 data-id="heading-10">深拷贝</h3>
<p>浅拷贝只对第一层属性进行拷贝，会存在一个问题：如果第一层属性是引用类型，拷贝的是地址，浅拷贝会导致原数据被修改。那怎么解决这个问题呢，这就需要<code>深拷贝</code>了。</p>
<blockquote>
<p>深拷贝是从内存中完整的拷贝一份出来，在堆内存中开一个新的内存空间，与原对象完全独立。修改新对象不会影响原对象。</p>
</blockquote>
<h4 data-id="heading-11">如何实现一个深拷贝？</h4>
<p><strong>1.浅拷贝+递归</strong></p>
<p>浅拷贝只对第一层属性进行拷贝，深拷贝需要拷贝到最后一层（直到属性是基本类型为止）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 递归浅拷贝</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">recursiveShallowCopy</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">var</span> copy = <span class="hljs-built_in">Array</span>.isArray(obj) ? [] : &#123;&#125;;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> p <span class="hljs-keyword">in</span> obj) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> obj[p] === <span class="hljs-string">'object'</span>) &#123;
      <span class="hljs-comment">// 对象类型，继续递归浅拷贝</span>
      copy[p] = recursiveShallowCopy(obj[p]);
    &#125; <span class="hljs-keyword">else</span> &#123;
      copy[p] = obj[p];
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> copy;
&#125;

<span class="hljs-comment">// 深拷贝</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepCopy</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">'object'</span> && obj !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-comment">// 如果是引用类型，进行递归浅拷贝</span>
    <span class="hljs-keyword">return</span> recursiveShallowCopy(obj);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 如果是基本类型，直接返回</span>
    <span class="hljs-keyword">return</span> obj;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们现在用上面创建的深拷贝函数 <code>deepCopy()</code>来验证下前面表格总结的内容：</p>
<ul>
<li>深拷贝时，无论第一层属性是基本类型还是引用类型，修改新对象都不会影响原数据。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 原数据是对象</span>
<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span>,
  <span class="hljs-attr">person</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'谷底飞龙'</span>,
  &#125;,
&#125;

<span class="hljs-comment">// 改用 deepCopy() 实现深拷贝</span>
<span class="hljs-keyword">var</span> copy = deepCopy(obj);

<span class="hljs-comment">// 改变原数据第一层属性 color （基本数据类型）</span>
copy.color = <span class="hljs-string">'yellow'</span>;
<span class="hljs-comment">// 改变原数据第一层属性 person（引用数据类型）</span>
copy.person.name = <span class="hljs-string">'天下无敌'</span>;
<span class="hljs-comment">// 原数据中 color 仍为 “red“，name 仍为 “谷底飞龙”</span>
<span class="hljs-built_in">console</span>.log(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行上面案例，打印结果如下：
<img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12fa289a623c49ed9cf16529ab7192ce~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>对数组的操作结果也是一样的，这里就不重复写了。</p>
<p><strong>2.JSON.parse(JSON.stringify())</strong></p>
<blockquote>
<p>先通过<code>JSON.stringify()</code>把原对象序列化成一个 JSON 字符串，再通过<code>JSON.parse()</code>生成一个新对象。</p>
</blockquote>
<p>这是目前比较常用的深拷贝方式。我们把之前的案例修改为用 <code>JSON.parse(JSON.stringify())</code>来实现深拷贝验证下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 原数据是对象</span>
<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span>,
  <span class="hljs-attr">person</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'谷底飞龙'</span>,
  &#125;,
&#125;

<span class="hljs-comment">// 改用 JSON.parse(JSON.stringify()) 实现深拷贝</span>
<span class="hljs-keyword">var</span> copy = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(obj));

<span class="hljs-comment">// 改变原数据第一层属性 color （基本数据类型）</span>
copy.color = <span class="hljs-string">'yellow'</span>;
<span class="hljs-comment">// 改变原数据第一层属性 person（引用数据类型）</span>
copy.person.name = <span class="hljs-string">'天下无敌'</span>;
<span class="hljs-comment">// 原数据中 color 仍为 “red“，name 仍为 “谷底飞龙”</span>
<span class="hljs-built_in">console</span>.log(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果与用<code>递归+浅拷贝</code>实现的<code>deepCopy()</code>效果是一样的</p>
<h4 data-id="heading-12">深拷贝的注意事项</h4>
<p>使用<code>JSON.parse(JSON.stringify()</code>实现深拷贝有一些缺陷：</p>
<blockquote>
<p>1.如果原对象中有<code>undefined、Symbol、函数</code>时，会导致该键值被丢失</p>
<p>2.如果原对象中有<code>正则</code>，会被转换为空对象<code>&#123;&#125;</code></p>
<p>3.如果原对象中有<code>Date</code>，会被转换成字符串</p>
<p>4.会抛弃原对象的<code>constructor</code>，都会被转换成<code>Object</code></p>
<p>5.如果对象中存在<code>循环引用</code>的情况，无法正确处理</p>
</blockquote>
<p>先来验证下前 3 个缺陷：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 原数据是对象</span>
<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span>,
  <span class="hljs-attr">person</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;, <span class="hljs-comment">// 被丢失</span>
    <span class="hljs-attr">country</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// 被丢失</span>
    <span class="hljs-attr">love</span>: <span class="hljs-built_in">Symbol</span>(), <span class="hljs-comment">// 被丢失</span>
    <span class="hljs-attr">time</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),<span class="hljs-comment">// 转换成 字符串</span>
    <span class="hljs-attr">height</span>: <span class="hljs-regexp">/[1-9][0-9]?/</span>, <span class="hljs-comment">// 转换成空对象 &#123;&#125;</span>
  &#125;,
&#125;

<span class="hljs-comment">// 使用 JSON.parse(JSON.stringify() 实现深拷贝</span>
<span class="hljs-keyword">var</span> copy = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(obj));
<span class="hljs-built_in">console</span>.log(copy)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行后，会发现原对象中的<code>属性 age（函数）、country（undefined）、love（Symbol）被丢失</code>，<code>time（Date）被转换成字符串</code>，<code>height（正则）被转换为空对象 &#123;&#125;</code>。打印结果如下
<img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5e59a05c5914241a1e3cfb52c715629~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们再来验证下使用<code>JSON.parse(JSON.stringify())</code>实现深拷贝，会抛弃原对象的<code>constructor</code>，都会被转换成<code>Object</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'谷底飞龙'</span>
&#125;

<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">person</span>: <span class="hljs-keyword">new</span> Person() 
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'原对象：'</span>)
<span class="hljs-built_in">console</span>.log(obj)

<span class="hljs-keyword">var</span> copy = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(obj))
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'新对象：'</span>)
<span class="hljs-built_in">console</span>.log(copy)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>深拷贝之后，不管这个对象原来的构造函数是什么，在深拷贝之后都会变成 <code>Object</code>。执行结果如下：</p>
<p>使用<code>JSON.parse(JSON.stringify()</code>实现深拷贝的前 4 个缺陷，可以通过<code>递归+浅拷贝</code>的深拷贝方式解决，但<code>递归+浅拷贝</code>不能解决第 5 点循环引用的问题。</p>
<p>参考</p>
<ul>
<li><a href="https://juejin.cn/post/6947249325994934302">详细解析赋值、浅拷贝和深拷贝的区别</a></li>
<li><a href="https://juejin.cn/post/6947249325994934302">javascript深拷贝、浅拷贝和循环引用深入理解</a></li>
</ul>
<hr>
<p><strong>结语</strong></p>
<p>写文章不易，花了我足足两天时间写的，如果你喜欢这篇文章，可以帮忙点个<code>赞</code>～</p>
<p>也可以关注我的公众号 「<strong>谷底飞龙</strong>」～</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            