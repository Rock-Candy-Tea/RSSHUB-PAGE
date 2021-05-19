
---
title: 'JavaScript 系列七_ 对象'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5437'
author: 掘金
comments: false
date: Wed, 19 May 2021 00:48:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=5437'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>"Code tailor"，为前端开发者提供技术相关资讯以及系列基础文章，微信关注“小和山的菜鸟们”公众号，及时获取最新文章。</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>在开始学习之前，我们想要告诉您的是，本文章是对 <code>JavaScript</code> 语言知识中 <strong>"对象、类与面向对象编程"</strong> 部分的总结，如果您已掌握下面知识事项，则可跳过此环节直接进入题目练习</p>
<ul>
<li>对象的基本构造</li>
<li>对象声明及使用</li>
<li>类</li>
<li>对象的结构赋值</li>
<li>继承</li>
<li>包装对象</li>
</ul>
<p>如果您对某些部分有些遗忘，👇🏻 已经为您准备好了！</p>
<h2 data-id="heading-1">汇总总结</h2>
<p><code>ECMA-262</code> 将对象定义为一组属性的无序集合。严格来说，这意味着对象就是一组没有特定顺序的值。对象的每个属性或方法都由一个名称来标识，这个名称映射到一个值。正因为如此（以及其他还未讨论的原因），可以把<code>ECMAScript</code> 的对象想象成一张散列表，其中的内容就是一组名/值对，值可以是数据或者函数。</p>
<h3 data-id="heading-2">对象的基本构造</h3>
<p>创建自定义对象的通常方式是创建 Object 的一个新实例，然后再给它添加属性和方法，如下例 所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> person = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()
person.name = <span class="hljs-string">'XHS-rookies'</span>
person.age = <span class="hljs-number">18</span>
person.job = <span class="hljs-string">'Software Engineer'</span>
person.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子创建了一个名为 <code>person</code> 的对象，而且有三个属性（<code>name</code>、<code>age</code>和 <code>job</code>）和一个方法（<code>sayName()</code>）。<code>sayName()</code>方法会显示 <code>this.name</code> 的值，这个属性会解析为 <code>person.name</code>。早期<code>JavaScript</code> 开发者频繁使用这种方式创建新对象。几年后，对象字面量变成了更流行的方式。前面的例子如果使用对象字面量则可以这样写：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'XHS-rookies'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
  <span class="hljs-attr">job</span>: <span class="hljs-string">'Software Engineer'</span>,
  <span class="hljs-function"><span class="hljs-title">sayName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子中的 <code>person</code> 对象跟前面例子中的 <code>person</code> 对象是等价的，它们的属性和方法都一样。这些属性都有自己的特征，而这些特征决定了它们在 <code>JavaScript</code> 中的行为。</p>
<h3 data-id="heading-3">对象声明及使用</h3>
<p>综观 <code>ECMAScript</code> 规范的历次发布，每个版本的特性似乎都出人意料。<code>ECMAScript 5.1</code> 并没有正式 支持面向对象的结构，比如类或继承。但是，正如接下来几节会介绍的，巧妙地运用原型式继承可以成 功地模拟同样的行为。<code>ECMAScript 6</code> 开始正式支持类和继承。<code>ES6</code>的类旨在完全涵盖之前规范设计的基于原型的继承模式。不过，无论从哪方面看，<code>ES6</code> 的类都仅仅是封装了<code>ES5.1</code> 构造函数加原型继承的语法糖而已。</p>
<h4 data-id="heading-4">工厂模式</h4>
<p>工厂模式是一种众所周知的设计模式，广泛应用于软件工程领域，用于抽象创建特定对象的过程。下面的例子展示了一种按照特定接口创建对象的方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createPerson</span>(<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-keyword">let</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()
  o.name = name
  o.age = age
  o.job = job
  o.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
  &#125;
  <span class="hljs-keyword">return</span> o
&#125;
<span class="hljs-keyword">let</span> person1 = createPerson(<span class="hljs-string">'XHS-rookies'</span>, <span class="hljs-number">18</span>, <span class="hljs-string">'Software Engineer'</span>)
<span class="hljs-keyword">let</span> person2 = createPerson(<span class="hljs-string">'XHS-boos'</span>, <span class="hljs-number">18</span>, <span class="hljs-string">'Teacher'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里，函数 <code>createPerson()</code> 接收 3 个参数，根据这几个参数构建了一个包含 <code>Person</code> 信息的对象。可以用不同的参数多次调用这个函数，每次都会返回包含 3 个属性和 1 个方法的对象。这种工厂模式虽然可以解决创建多个类似对象的问题，但没有解决对象标识问题（即新创建的对象是什么类型）。</p>
<h4 data-id="heading-5">构造函数模式</h4>
<p><code>ECMAScript</code> 中的构造函数是用于创建特定类型对象的。像 <code>Object</code> 和 <code>Array</code>这 样的原生构造函数，运行时可以直接在执行环境中使用。当然也可以自定义构造函数，以函数的形式为 自己的对象类型定义属性和方法。 比如，前面的例子使用构造函数模式可以这样写：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.age = age
  <span class="hljs-built_in">this</span>.job = job
  <span class="hljs-built_in">this</span>.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
  &#125;
&#125;
<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'XHS-rookies'</span>, <span class="hljs-number">18</span>, <span class="hljs-string">'Software Engineer'</span>)
<span class="hljs-keyword">let</span> person2 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'XHS-boos'</span>, <span class="hljs-number">18</span>, <span class="hljs-string">'Teacher'</span>)
person1.sayName() <span class="hljs-comment">// XHS-rookies</span>
person2.sayName() <span class="hljs-comment">// XHS-boos</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，<code>Person()</code> 构造函数代替了<code>createPerson()</code>工厂函数。实际上，<code>Person()</code> 内部 的代码跟 <code>createPerson()</code> 基本是一样的，只是有如下区别。</p>
<ul>
<li>
<p>没有显式地创建对象。</p>
</li>
<li>
<p>属性和方法直接赋值给了 <code>this</code>。</p>
</li>
<li>
<p>没有 <code>return</code>。</p>
</li>
</ul>
<p>另外，要注意函数名 <code>Person</code> 的首字母大写了。按照惯例，构造函数名称的首字母都是要大写的， 非构造函数则以小写字母开头。这是从面向对象编程语言那里借鉴的，有助于在 <code>ECMAScript</code> 中区分构 造函数和普通函数。毕竟 <code>ECMAScript</code> 的构造函数就是能创建对象的函数。</p>
<p>要创建 <code>Person</code> 的实例，应使用 <code>new</code> 操作符。以这种方式调用构造函数会执行如下操作。</p>
<p>（1）在内存中创建一个新对象。</p>
<p>（2）这个新对象内部的 <code>[[Prototype]]</code> 特性被赋值为构造函数的 <code>prototype</code> 属性。</p>
<p>（3）构造函数内部的 <code>this</code> 被赋值为这个新对象（即 <code>this</code> 指向新对象）。</p>
<p>（4）执行构造函数内部的代码（给新对象添加属性）。</p>
<p>（5）如果构造函数返回非空对象，则返回该对象；否则，返回刚创建的新对象。</p>
<p>上一个例子的最后，<code>person1</code> 和 <code>person2</code> 分别保存着 <code>Person</code> 的不同实例。这两个对象都有一个 <code>constructor</code> 属性指向 <code>Person</code>，如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(person1.constructor == Person) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(person2.constructor == Person) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>constructor</code> 本来是用于标识对象类型的。不过，一般认为 <code>instanceof</code> 操作符是确定对象类型更可靠的方式。前面例子中的每个对象都是 <code>Object</code> 的实例，同时也是 <code>Person</code> 的实例，如下面调用 <code>instanceof</code> 操作符的结果所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(person1 <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(person1 <span class="hljs-keyword">instanceof</span> Person) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(person2 <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(person2 <span class="hljs-keyword">instanceof</span> Person) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义自定义构造函数可以确保实例被标识为特定类型，相比于工厂模式，这是一个很大的好处。在 这个例子中，<code>person1</code> 和 <code>person2</code> 之所以也被认为是 <code>Object</code> 的实例，是因为所有自定义对象都继承自 <code>Object</code>（后面再详细讨论这一点）。构造函数不一定要写成函数声明的形式。赋值给变量的函数表达式也可以表示构造函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> Person = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.age = age
  <span class="hljs-built_in">this</span>.job = job
  <span class="hljs-built_in">this</span>.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
  &#125;
&#125;
<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'XHS-rookies'</span>, <span class="hljs-number">18</span>, <span class="hljs-string">'Software Engineer'</span>)
<span class="hljs-keyword">let</span> person2 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'XHS-boos'</span>, <span class="hljs-number">18</span>, <span class="hljs-string">'Teacher'</span>)
person1.sayName() <span class="hljs-comment">// XHS-rookies</span>
person2.sayName() <span class="hljs-comment">// XHS-boos</span>
<span class="hljs-built_in">console</span>.log(person1 <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(person1 <span class="hljs-keyword">instanceof</span> Person) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(person2 <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(person2 <span class="hljs-keyword">instanceof</span> Person) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在实例化时，如果不想传参数，那么构造函数后面的括号可加可不加。只要有 <code>new</code> 操作符，就可以调用相应的构造函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'rookies'</span>
  <span class="hljs-built_in">this</span>.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
  &#125;
&#125;
<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person()
<span class="hljs-keyword">let</span> person2 = <span class="hljs-keyword">new</span> Person()
person1.sayName() <span class="hljs-comment">// rookies</span>
person2.sayName() <span class="hljs-comment">// rookies</span>
<span class="hljs-built_in">console</span>.log(person1 <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(person1 <span class="hljs-keyword">instanceof</span> Person) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(person2 <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(person2 <span class="hljs-keyword">instanceof</span> Person) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1. 构造函数也是函数</strong></p>
<p>构造函数与普通函数唯一的区别就是调用方式不同。除此之外，构造函数也是函数。并没有把某个函数定义为构造函数的特殊语法。任何函数只要使用 <code>new</code> 操作符调用就是构造函数，而不使用 <code>new</code>操作符调用的函数就是普通函数。比如，前面的例子中定义的 <code>Person()</code>可以像下面这样调用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 作为构造函数</span>
<span class="hljs-keyword">let</span> person = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'XHS-rookies'</span>, <span class="hljs-number">18</span>, <span class="hljs-string">'Software Engineer'</span>)
person.sayName() <span class="hljs-comment">// "XHS-rookies"</span>
<span class="hljs-comment">// 作为函数调用</span>
Person(<span class="hljs-string">'XHS-boos'</span>, <span class="hljs-number">18</span>, <span class="hljs-string">'Teacher'</span>) <span class="hljs-comment">// 添加到 window 对象</span>
<span class="hljs-built_in">window</span>.sayName() <span class="hljs-comment">// "XHS-boos"</span>
<span class="hljs-comment">// 在另一个对象的作用域中调用</span>
<span class="hljs-keyword">let</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()
Person.call(o, <span class="hljs-string">'XHS-sunshineboy'</span>, <span class="hljs-number">25</span>, <span class="hljs-string">'Nurse'</span>)
o.sayName() <span class="hljs-comment">// "XHS-sunshineboy"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子一开始展示了典型的构造函数调用方式，即使用 <code>new</code> 操作符创建一个新对象。然后是普通函数的调用方式，这时候没有使用 <code>new</code>操作符调用 <code>Person()</code>，结果会将属性和方法添加到 <code>window</code> 对象。这里要记住，在调用一个函数而没有明确设置 <code>this</code> 值的情况下（即没有作为对象的方法调用，或 者没有使用 <code>call()/apply()</code>调用），<code>this</code> 始终指向 <code>Global</code> 对象（在浏览器中就是 <code>window</code> 对象）。 因此在上面的调用之后，<code>window</code> 对象上就有了一个 <code>sayName()</code> 方法，调用它会返回 <code>"Greg"</code>。最后展示的调用方式是通过 <code>call()</code>（或<code>apply()</code> ）调用函数，同时将特定对象指定为作用域。这里的调用将 对象 <code>o</code> 指定为 <code>Person()</code> 内部的 <code>this</code> 值，因此执行完函数代码后，所有属性和 <code>sayName()</code> 方法都会添加到对象 <code>o</code> 上面。</p>
<p><strong>2. 构造函数的问题</strong></p>
<p>构造函数虽然有用，但也不是没有问题。构造函数的主要问题在于，其定义的方法会在每个实例上都创建一遍。因此对前面的例子而言，<code>person1</code> 和 <code>person2</code> 为<code> sayName()</code> 的方法，但这两个方法不是同一个 <code>Function</code> 实例。我们知道，<code>ECMAScript</code>中的函数是对象，因此每次定义函数时，都会初始化一个对象。逻辑上讲，这个构造函数实际上是这样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.age = age
  <span class="hljs-built_in">this</span>.job = job
  <span class="hljs-built_in">this</span>.sayName = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">'console.log(this.name)'</span>) <span class="hljs-comment">// 逻辑等价</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样理解这个构造函数可以更清楚地知道，每个 <code>Person</code> 实例都会有自己的 <code>Function</code> 实例用于显 示 <code>name</code> 属性。当然了，以这种方式创建函数会带来不同的作用域链和标识符解析。但创建新 <code>Function</code> 实例的机制是一样的。因此不同实例上的函数虽然同名却不相等，如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(person1.sayName == person2.sayName) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为都是做一样的事，所以没必要定义两个不同的 <code>Function</code> 实例。况且，<code>this</code> 对象可以把函数 与对象的绑定推迟到运行时。 要解决这个问题，可以把函数定义转移到构造函数外部：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age, job</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name
  <span class="hljs-built_in">this</span>.age = age
  <span class="hljs-built_in">this</span>.job = job
  <span class="hljs-built_in">this</span>.sayName = sayName
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayName</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'XHS-rookies'</span>, <span class="hljs-number">18</span>, <span class="hljs-string">'Software Engineer'</span>)
<span class="hljs-keyword">let</span> person2 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'XHS-boos'</span>, <span class="hljs-number">18</span>, <span class="hljs-string">'Teacher'</span>)
person1.sayName() <span class="hljs-comment">// XHS-rookies</span>
person2.sayName() <span class="hljs-comment">// XHS-boos</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里，<code>sayName()</code>被定义在了构造函数外部。在构造函数内部，<code>sayName</code> 属性等于全局 <code>sayName()</code> 函数。因为这一次 <code>sayName</code> 属性中包含的只是一个指向外部函数的指针，所以 <code>person1</code> 和 <code>person2</code> 共享了定义在全局作用域上的 <code>sayName()</code> 函数。这样虽然解决了相同逻辑的函数重复定义的问题，但全局作用域也因此被搞乱了，因为那个函数实际上只能在一个对象上调用。如果这个对象需要多个方法， 那么就要在全局作用域中定义多个函数。这会导致自定义类型引用的代码不能很好地聚集一起。这个新问题可以通过原型模式来解决。</p>
<h4 data-id="heading-6">原型模式</h4>
<p>每个函数都会创建一个 <code>prototype</code> 属性，这个属性是一个对象，包含应该由特定引用类型的实例 共享的属性和方法。实际上，这个对象就是通过调用构造函数创建的对象的原型。使用原型对象的好处是，在它上面定义的属性和方法可以被对象实例共享。原来在构造函数中直接赋给对象实例的值，可以直接赋值给它们的原型，如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
Person.prototype.name = <span class="hljs-string">'XHS-rookies'</span>
Person.prototype.age = <span class="hljs-number">18</span>
Person.prototype.job = <span class="hljs-string">'Software Engineer'</span>
Person.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person()
person1.sayName() <span class="hljs-comment">// "XHS-rookies"</span>
<span class="hljs-keyword">let</span> person2 = <span class="hljs-keyword">new</span> Person()
person2.sayName() <span class="hljs-comment">// "XHS-rookies"</span>
<span class="hljs-built_in">console</span>.log(person1.sayName == person2.sayName) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用函数表达式也可以：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> Person = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;
Person.prototype.name = <span class="hljs-string">'XHS-rookies'</span>
Person.prototype.age = <span class="hljs-number">18</span>
Person.prototype.job = <span class="hljs-string">'Software Engineer'</span>
Person.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-keyword">let</span> person1 = <span class="hljs-keyword">new</span> Person()
person1.sayName() <span class="hljs-comment">// "XHS-rookies"</span>
<span class="hljs-keyword">let</span> person2 = <span class="hljs-keyword">new</span> Person()
person2.sayName() <span class="hljs-comment">// "XHS-rookies"</span>
<span class="hljs-built_in">console</span>.log(person1.sayName == person2.sayName) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里，所有属性和 <code>sayName() </code>方法都直接添加到了<code>Person</code> 的 <code>prototype</code> 属性上，构造函数体中什么也没有。但这样定义之后，调用构造函数创建的新对象仍然拥有相应的属性和方法。与构造函数模式不同，使用这种原型模式定义的属性和方法是由所有实例共享的。因此 <code>person1</code> 和 <code>person2</code> 访问的都是相同的属性和相同的 <code>sayName()</code> 函数。要理解这个过程，就必须理解 <code>ECMAScript</code> 中原型的本质。(详细学习 <code>ECMAScript</code>中的原型请见：<a href="https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Objects/Object_prototypes" target="_blank" rel="nofollow noopener noreferrer">对象原型</a>)</p>
<h4 data-id="heading-7">其他原型语法</h4>
<p>有读者可能注意到了，在前面的例子中，每次定义一个属性或方法都会把 <code>Person.prototype</code>重写一遍。为了减少代码冗余，也为了从视觉上更好地封装原型功能，直接通过一个包含所有属性和方法 的对象字面量来重写原型成为了一种常见的做法，如下面的例子所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
Person.prototype = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'XHS-rookies'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
  <span class="hljs-attr">job</span>: <span class="hljs-string">'Software Engineer'</span>,
  <span class="hljs-function"><span class="hljs-title">sayName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，<code>Person.prototype</code>被设置为等于一个通过对象字面量创建的新对象。最终结果是一样的，只有一个问题：这样重写之后，<code>Person.prototype</code> 的 <code>constructor</code> 属性就不指向 <code>Person</code> 了。在创建函数时，也会创建它的<code>prototype</code>对象，同时会自动给这个原型的 <code>constructor</code> 属性赋值。而上面的写法完全重写了默认的<code>prototype</code>对象，因此其 <code>constructor</code>属性也指向了完全不同的新对象（<code>Object</code>构造函数），不再指向原来的构造函数。虽然 <code>instanceof</code>操作符还能可靠地返回值，但我们不能再依靠 <code>constructor</code> 属性来识别类型了，如下面的例子所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> friend = <span class="hljs-keyword">new</span> Person()
<span class="hljs-built_in">console</span>.log(friend <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(friend <span class="hljs-keyword">instanceof</span> Person) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(friend.constructor == Person) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(friend.constructor == <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里，<code>instanceof</code> 仍然对 <code>Object</code> 和 <code>Person</code> 都返回 <code>true</code>。但 <code>constructor</code> 属性现在等于 <code>Object</code> 而不是 <code>Person</code> 了。如果<code>constructor</code>的值很重要，则可以像下面这样在重写原型对象时专门设置一 下它的值：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
Person.prototype = &#123;
  <span class="hljs-attr">constructor</span>: Person,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'XHS-rookies'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
  <span class="hljs-attr">job</span>: <span class="hljs-string">'Software Engineer'</span>,
  <span class="hljs-function"><span class="hljs-title">sayName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这次的代码中特意包含了 <code>constructor</code> 属性，并将它设置为 <code>Person</code>，保证了这个属性仍然包含恰当的值。 但要注意，以这种方式恢复 <code>constructor</code> 属性会创建一个 <code>[[Enumerable]]</code> 为 <code>true</code> 的属性。而原生 <code>constructor</code> 属性默认是不可枚举的。因此，如果你使用的是兼容 <code>ECMAScript</code> 的 <code>JavaScript</code> 引擎， 那可能会改为使用 <code>Object.defineProperty()</code> 方法来定义 <code>constructor</code>属性：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
Person.prototype = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'XHS-rookies'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
  <span class="hljs-attr">job</span>: <span class="hljs-string">'Software Engineer'</span>,
  <span class="hljs-function"><span class="hljs-title">sayName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
  &#125;,
&#125;
<span class="hljs-comment">// 恢复 constructor 属性</span>
<span class="hljs-built_in">Object</span>.defineProperty(Person.prototype, <span class="hljs-string">'constructor'</span>, &#123;
  <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">value</span>: Person,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">类</h3>
<p>前几节深入讲解了如何只使用 <code>ECMAScript 5</code> 的特性来模拟类似于类（<code>class-like</code>）的行为。不难看出，各种策略都有自己的问题，也有相应的妥协。正因为如此，实现继承的代码也显得非常冗长和混乱。</p>
<p>为解决这些问题，<code>ECMAScript 6</code> 新引入的<code>class</code> 关键字具有正式定义类的能力。类（<code>class</code>）是 <code>ECMAScript</code> 中新的基础性语法糖结构，因此刚开始接触时可能会不太习惯。虽然 <code>ECMAScript 6</code> 类表面 上看起来可以支持正式的面向对象编程，但实际上它背后使用的仍然是原型和构造函数的概念。</p>
<h4 data-id="heading-9">类定义</h4>
<p>与函数类型相似，定义类也有两种主要方式：类声明和类表达式。这两种方式都使用 <code>class</code> 关键 字加大括号：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 类声明</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;&#125;
<span class="hljs-comment">// 类表达式</span>
<span class="hljs-keyword">const</span> Animal = <span class="hljs-class"><span class="hljs-keyword">class</span> </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与函数表达式类似，类表达式在它们被求值前也不能引用。不过，与函数定义不同的是，虽然函数声明可以提升，但类定义不能：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(FunctionExpression) <span class="hljs-comment">// undefined</span>

<span class="hljs-keyword">var</span> FunctionExpression = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-built_in">console</span>.log(FunctionExpression) <span class="hljs-comment">// function() &#123;&#125;</span>
<span class="hljs-built_in">console</span>.log(FunctionDeclaration) <span class="hljs-comment">// FunctionDeclaration() &#123;&#125;</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FunctionDeclaration</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-built_in">console</span>.log(FunctionDeclaration) <span class="hljs-comment">// FunctionDeclaration() &#123;&#125;</span>
<span class="hljs-built_in">console</span>.log(ClassExpression) <span class="hljs-comment">// undefined</span>

<span class="hljs-keyword">var</span> ClassExpression = <span class="hljs-class"><span class="hljs-keyword">class</span> </span>&#123;&#125;
<span class="hljs-built_in">console</span>.log(ClassExpression) <span class="hljs-comment">// class &#123;&#125;</span>
<span class="hljs-built_in">console</span>.log(ClassDeclaration) <span class="hljs-comment">// ReferenceError: ClassDeclaration is not defined</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClassDeclaration</span> </span>&#123;&#125;
<span class="hljs-built_in">console</span>.log(ClassDeclaration) <span class="hljs-comment">// class ClassDeclaration &#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个跟函数声明不同的地方是，函数受函数作用域限制，而类受块作用域限制:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FunctionDeclaration</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClassDeclaration</span> </span>&#123;&#125;
&#125;
<span class="hljs-built_in">console</span>.log(FunctionDeclaration) <span class="hljs-comment">// FunctionDeclaration() &#123;&#125;</span>
<span class="hljs-built_in">console</span>.log(ClassDeclaration) <span class="hljs-comment">// ReferenceError: ClassDeclaration is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">类的构成</h4>
<p>类可以包含构造函数方法、实例方法、获取函数、设置函数和静态类方法，但这些都不是必需的。 空的类定义照样有效。默认情况下，类定义中的代码都在严格模式下执行。</p>
<p>与函数构造函数一样，多数编程风格都建议类名的首字母要大写，以区别于通过它创建的实例（比如，通过 <code>class Foo &#123;&#125; </code>创建实例 <code>foo</code>）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 空类定义，有效</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;&#125;
<span class="hljs-comment">// 有构造函数的类，有效</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bar</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="hljs-comment">// 有获取函数的类，有效</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Baz</span> </span>&#123;
  <span class="hljs-keyword">get</span> <span class="hljs-title">myBaz</span>() &#123;&#125;
&#125;
<span class="hljs-comment">// 有静态方法的类，有效</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Qux</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">myQux</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类表达式的名称是可选的。在把类表达式赋值给变量后，可以通过 <code>name</code> 属性取得类表达式的名称字符串。但不能在类表达式作用域外部访问这个标识符。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> Person = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PersonName</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">identify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(Person.name, PersonName.name)
  &#125;
&#125;
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person()
p.identify() <span class="hljs-comment">// PersonName PersonName</span>
<span class="hljs-built_in">console</span>.log(Person.name) <span class="hljs-comment">// PersonName</span>
<span class="hljs-built_in">console</span>.log(PersonName) <span class="hljs-comment">// ReferenceError: PersonName is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">类构造函数</h4>
<p><code>constructor </code>关键字用于在类定义块内部创建类的构造函数。方法名 <code>constructor</code> 会告诉解释器 在使用 <code>new</code> 操作符创建类的新实例时，应该调用这个函数。构造函数的定义不是必需的，不定义构造函 数相当于将构造函数定义为空函数。</p>
<p><strong>实例化</strong></p>
<p>使用 <code>new</code> 操作符实例化 Person 的操作等于使用 <code>new</code> 调用其构造函数。唯一可感知的不同之处就 是，<code>JavaScript</code> 解释器知道使用 <code>new</code> 和类意味着应该使用 <code>constructor</code> 函数进行实例化。 使用 <code>new</code> 调用类的构造函数会执行如下操作。</p>
<p>（1）在内存中创建一个新对象。</p>
<p>（2）这个新对象内部的 <code>[[Prototype]]</code>指针被赋值为构造函数的 <code>prototype</code> 属性。</p>
<p>（3）构造函数内部的 <code>this</code> 被赋值为这个新对象（即 <code>this</code> 指向新对象）。</p>
<p>（4）执行构造函数内部的代码（给新对象添加属性）。</p>
<p>（5）如果构造函数返回非空对象，则返回该对象；否则，返回刚创建的新对象。</p>
<p>来看下面的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'person ctor'</span>)
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vegetable</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.color = <span class="hljs-string">'orange'</span>
  &#125;
&#125;
<span class="hljs-keyword">let</span> a = <span class="hljs-keyword">new</span> Animal()
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person() <span class="hljs-comment">// person ctor</span>
<span class="hljs-keyword">let</span> v = <span class="hljs-keyword">new</span> Vegetable()
<span class="hljs-built_in">console</span>.log(v.color) <span class="hljs-comment">// orange</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类实例化时传入的参数会用作构造函数的参数。如果不需要参数，则类名后面的括号也是可选的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>.length)
    <span class="hljs-built_in">this</span>.name = name || <span class="hljs-literal">null</span>
  &#125;
&#125;
<span class="hljs-keyword">let</span> p1 = <span class="hljs-keyword">new</span> Person() <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">console</span>.log(p1.name) <span class="hljs-comment">// null</span>
<span class="hljs-keyword">let</span> p2 = <span class="hljs-keyword">new</span> Person() <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">console</span>.log(p2.name) <span class="hljs-comment">// null</span>
<span class="hljs-keyword">let</span> p3 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'Jake'</span>) <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(p3.name) <span class="hljs-comment">// Jake</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下，类构造函数会在执行之后返回 <code>this</code> 对象。构造函数返回的对象会被用作实例化的对 象，如果没有什么引用新创建的 <code>this</code> 对象，那么这个对象会被销毁。不过，如果返回的不是 <code>this</code> 对 象，而是其他对象，那么这个对象不会通过 <code>instanceof</code> 操作符检测出跟类有关联，因为这个对象的原型指针并没有被修改。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">override</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.foo = <span class="hljs-string">'foo'</span>
    <span class="hljs-keyword">if</span> (override) &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">bar</span>: <span class="hljs-string">'bar'</span>,
      &#125;
    &#125;
  &#125;
&#125;
<span class="hljs-keyword">let</span> p1 = <span class="hljs-keyword">new</span> Person(),
  p2 = <span class="hljs-keyword">new</span> Person(<span class="hljs-literal">true</span>)
<span class="hljs-built_in">console</span>.log(p1) <span class="hljs-comment">// Person&#123; foo: 'foo' &#125;</span>
<span class="hljs-built_in">console</span>.log(p1 <span class="hljs-keyword">instanceof</span> Person) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(p2) <span class="hljs-comment">// &#123; bar: 'bar' &#125;</span>
<span class="hljs-built_in">console</span>.log(p2 <span class="hljs-keyword">instanceof</span> Person) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类构造函数与构造函数的主要区别是，调用类构造函数必须使用 <code>new</code> 操作符。而普通构造函数如果不使用 <code>new</code> 调用，那么就会以全局的 <code>this</code>（通常是 <code>window</code>）作为内部对象。调用类构造函数时如果 忘了使用 <code>new</code>则会抛出错误：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;&#125;
<span class="hljs-comment">// 把 window 作为 this 来构建实例</span>
<span class="hljs-keyword">let</span> p = Person()
<span class="hljs-keyword">let</span> a = Animal()
<span class="hljs-comment">// TypeError: class constructor Animal cannot be invoked without 'new'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类构造函数没有什么特殊之处，实例化之后，它会成为普通的实例方法（但作为类构造函数，仍然要使用 <code>new</code>调用）。因此，实例化之后可以在实例上引用它：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;&#125;
<span class="hljs-comment">// 使用类创建一个新实例</span>
<span class="hljs-keyword">let</span> p1 = <span class="hljs-keyword">new</span> Person()
p1.constructor()
<span class="hljs-comment">// TypeError: Class constructor Person cannot be invoked without 'new'</span>
<span class="hljs-comment">// 使用对类构造函数的引用创建一个新实例</span>
<span class="hljs-keyword">let</span> p2 = <span class="hljs-keyword">new</span> p1.constructor()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">实例、原型和类成员</h4>
<p>类的语法可以非常方便地定义应该存在于实例上的成员、应该存在于原型上的成员，以及应该存在 于类本身的成员。</p>
<p><strong>1. 实例成员</strong></p>
<p>每次通过 <code>new</code>调用类标识符时，都会执行类构造函数。在这个函数内部，可以为新创建的实例（<code>this</code>） 添加“自有”属性。至于添加什么样的属性，则没有限制。另外，在构造函数执行完毕后，仍然可以给 实例继续添加新成员。</p>
<p>每个实例都对应一个唯一的成员对象，这意味着所有成员都不会在原型上共享：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 这个例子先使用对象包装类型定义一个字符串</span>
    <span class="hljs-comment">// 为的是在下面测试两个对象的相等性</span>
    <span class="hljs-built_in">this</span>.name = <span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">'xhs-rookies'</span>)
    <span class="hljs-built_in">this</span>.sayName = <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
    <span class="hljs-built_in">this</span>.nicknames = [<span class="hljs-string">'xhs-rookies'</span>, <span class="hljs-string">'J-Dog'</span>]
  &#125;
&#125;
<span class="hljs-keyword">let</span> p1 = <span class="hljs-keyword">new</span> Person(),
  p2 = <span class="hljs-keyword">new</span> Person()
p1.sayName() <span class="hljs-comment">// xhs-rookies</span>
p2.sayName() <span class="hljs-comment">// xhs-rookies</span>
<span class="hljs-built_in">console</span>.log(p1.name === p2.name) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(p1.sayName === p2.sayName) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(p1.nicknames === p2.nicknames) <span class="hljs-comment">// false</span>
p1.name = p1.nicknames[<span class="hljs-number">0</span>]
p2.name = p2.nicknames[<span class="hljs-number">1</span>]
p1.sayName() <span class="hljs-comment">// xhs-rookies</span>
p2.sayName() <span class="hljs-comment">// J-Dog</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. 原型方法与访问器</strong></p>
<p>为了在实例间共享方法，类定义语法把在类块中定义的方法作为原型方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 添加到 this 的所有内容都会存在于不同的实例上</span>
    <span class="hljs-built_in">this</span>.locate = <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'instance'</span>)
  &#125;

  <span class="hljs-comment">// 在类块中定义的所有内容都会定义在类的原型上</span>
  <span class="hljs-function"><span class="hljs-title">locate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'prototype'</span>)
  &#125;
&#125;
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person()
p.locate() <span class="hljs-comment">// instance</span>
Person.prototype.locate() <span class="hljs-comment">// prototype</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以把方法定义在类构造函数中或者类块中，但不能在类块中给原型添加原始值或对象作为成员数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'xhs-rookies'</span>
&#125;
<span class="hljs-comment">// Uncaught SyntaxError: Unexpected token</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类方法等同于对象属性，因此可以使用字符串、符号或计算的值作为键：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> symbolKey = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'symbolKey'</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">stringKey</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'invoked stringKey'</span>)
  &#125;
  [symbolKey]() &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'invoked symbolKey'</span>)
  &#125;
  [<span class="hljs-string">'computed'</span> + <span class="hljs-string">'Key'</span>]() &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'invoked computedKey'</span>)
  &#125;
&#125;
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person()
p.stringKey() <span class="hljs-comment">// invoked stringKey</span>
p[symbolKey]() <span class="hljs-comment">// invoked symbolKey</span>
p.computedKey() <span class="hljs-comment">// invoked computedKey</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类定义也支持获取和设置访问器。语法与行为跟普通对象一样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-keyword">set</span> <span class="hljs-title">name</span>(<span class="hljs-params">newName</span>) &#123;
    <span class="hljs-built_in">this</span>.name_ = newName
  &#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">name</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name_
  &#125;
&#125;
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person()
p.name = <span class="hljs-string">'xhs-rookies'</span>
<span class="hljs-built_in">console</span>.log(p.name) <span class="hljs-comment">// xhs-rookies</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3. 静态类方法</strong></p>
<p>可以在类上定义静态方法。这些方法通常用于执行不特定于实例的操作，也不要求存在类的实例。与原型成员类似，静态成员每个类上只能有一个。 静态类成员在类定义中使用 <code>static</code> 关键字作为前缀。在静态成员中，<code>this</code> 引用类自身。其他所 有约定跟原型成员一样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 添加到 this 的所有内容都会存在于不同的实例上</span>
    <span class="hljs-built_in">this</span>.locate = <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'instance'</span>, <span class="hljs-built_in">this</span>)
  &#125;
  <span class="hljs-comment">// 定义在类的原型对象上</span>
  <span class="hljs-function"><span class="hljs-title">locate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'prototype'</span>, <span class="hljs-built_in">this</span>)
  &#125;
  <span class="hljs-comment">// 定义在类本身上</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">locate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'class'</span>, <span class="hljs-built_in">this</span>)
  &#125;
&#125;
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person()
p.locate() <span class="hljs-comment">// instance, Person &#123;&#125;</span>
Person.prototype.locate() <span class="hljs-comment">// prototype, &#123;constructor: ... &#125;</span>
Person.locate() <span class="hljs-comment">// class, class Person &#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>静态类方法非常适合作为实例工厂：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">age</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.age_ = age
  &#125;
  <span class="hljs-function"><span class="hljs-title">sayAge</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.age_)
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 使用随机年龄创建并返回一个 Person 实例</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Person(<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">100</span>))
  &#125;
&#125;
<span class="hljs-built_in">console</span>.log(Person.create()) <span class="hljs-comment">// Person &#123; age_: ... &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4. 非函数原型和类成员</strong></p>
<p>虽然类定义并不显式支持在原型或类上添加成员数据，但在类定义外部，可以手动添加：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">sayName</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;Person.greeting&#125;</span> <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>`</span>)
  &#125;
&#125;
<span class="hljs-comment">// 在类上定义数据成员</span>
Person.greeting = <span class="hljs-string">'My name is'</span>
<span class="hljs-comment">// 在原型上定义数据成员</span>
Person.prototype.name = <span class="hljs-string">'xhs-rookies'</span>
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person()
p.sayName() <span class="hljs-comment">// My name is xhs-rookies</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>注意</strong> 类定义中之所以没有显式支持添加数据成员，是因为在共享目标（原型和类）上添 加可变（可修改）数据成员是一种反模式。一般来说，对象实例应该独自拥有通过 <code>this</code> 引用的数据（注意在不同情况下使用 <code>this</code> 的情况会略有些不同，详细 <code>this</code> 学习请见<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/this" target="_blank" rel="nofollow noopener noreferrer">this-MDN</a>）。</p>
</blockquote>
<p><strong>5. 迭代器与生成器方法</strong></p>
<p>类定义语法支持在原型和类本身上定义生成器方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-comment">// 在原型上定义生成器方法</span>
  *<span class="hljs-function"><span class="hljs-title">createNicknameIterator</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">yield</span> <span class="hljs-string">'xhs-Jack'</span>
    <span class="hljs-keyword">yield</span> <span class="hljs-string">'xhs-Jake'</span>
    <span class="hljs-keyword">yield</span> <span class="hljs-string">'xhs-J-Dog'</span>
  &#125;
  <span class="hljs-comment">// 在类上定义生成器方法</span>
  <span class="hljs-keyword">static</span> *<span class="hljs-function"><span class="hljs-title">createJobIterator</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">yield</span> <span class="hljs-string">'xhs-Butcher'</span>
    <span class="hljs-keyword">yield</span> <span class="hljs-string">'xhs-Baker'</span>
    <span class="hljs-keyword">yield</span> <span class="hljs-string">'xhs-Candlestick maker'</span>
  &#125;
&#125;
<span class="hljs-keyword">let</span> jobIter = Person.createJobIterator()
<span class="hljs-built_in">console</span>.log(jobIter.next().value) <span class="hljs-comment">// xhs-Butcher</span>
<span class="hljs-built_in">console</span>.log(jobIter.next().value) <span class="hljs-comment">// xhs-Baker</span>
<span class="hljs-built_in">console</span>.log(jobIter.next().value) <span class="hljs-comment">// xhs-Candlestick maker</span>
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person()
<span class="hljs-keyword">let</span> nicknameIter = p.createNicknameIterator()
<span class="hljs-built_in">console</span>.log(nicknameIter.next().value) <span class="hljs-comment">// xhs-Jack</span>
<span class="hljs-built_in">console</span>.log(nicknameIter.next().value) <span class="hljs-comment">// xhs-Jake</span>
<span class="hljs-built_in">console</span>.log(nicknameIter.next().value) <span class="hljs-comment">// xhs-J-Dog</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为支持生成器方法，所以可以通过添加一个默认的迭代器，把类实例变成可迭代对象：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.nicknames = [<span class="hljs-string">'xhs-Jack'</span>, <span class="hljs-string">'xhs-Jake'</span>, <span class="hljs-string">'xhs-J-Dog'</span>]
  &#125;
  *[<span class="hljs-built_in">Symbol</span>.iterator]() &#123;
    <span class="hljs-keyword">yield</span>* <span class="hljs-built_in">this</span>.nicknames.entries()
  &#125;
&#125;
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person()
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [idx, nickname] <span class="hljs-keyword">of</span> p) &#123;
  <span class="hljs-built_in">console</span>.log(nickname)
&#125;
<span class="hljs-comment">// xhs-Jack</span>
<span class="hljs-comment">// xhs-Jake</span>
<span class="hljs-comment">// xhs-J-Dog</span>
<span class="hljs-comment">//也可以只返回迭代器实例：</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.nicknames = [<span class="hljs-string">'xhs-Jack'</span>, <span class="hljs-string">'xhs-Jake'</span>, <span class="hljs-string">'xhs-J-Dog'</span>]
  &#125;
  [<span class="hljs-built_in">Symbol</span>.iterator]() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.nicknames.entries()
  &#125;
&#125;
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person()
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [idx, nickname] <span class="hljs-keyword">of</span> p) &#123;
  <span class="hljs-built_in">console</span>.log(nickname)
&#125;
<span class="hljs-comment">// xhs-Jack</span>
<span class="hljs-comment">// xhs-Jake</span>
<span class="hljs-comment">// xhs-J-Dog</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">对象的解构赋值</h3>
<p><code>ECMAScript 6</code> 新增了对象解构语法，可以在一条语句中使用嵌套数据实现一个或多个赋值操作。简单地说，对象解构就是使用与对象匹配的结构来实现对象属性赋值。 下面的例子展示了两段等价的代码，首先是不使用对象解构的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 不使用对象解构</span>
<span class="hljs-keyword">let</span> person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'xhs-Matt'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
&#125;
<span class="hljs-keyword">let</span> personName = person.name,
  personAge = person.age
<span class="hljs-built_in">console</span>.log(personName) <span class="hljs-comment">// xhs-Matt</span>
<span class="hljs-built_in">console</span>.log(personAge) <span class="hljs-comment">// 18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，是使用对象解构的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 使用对象解构</span>
<span class="hljs-keyword">let</span> person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'xhs-Matt'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
&#125;
<span class="hljs-keyword">let</span> &#123; <span class="hljs-attr">name</span>: personName, <span class="hljs-attr">age</span>: personAge &#125; = person
<span class="hljs-built_in">console</span>.log(personName) <span class="hljs-comment">// xhs-Matt</span>
<span class="hljs-built_in">console</span>.log(personAge) <span class="hljs-comment">// 18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用解构，可以在一个类似对象字面量的结构中，声明多个变量，同时执行多个赋值操作。如果想让变量直接使用属性的名称，那么可以使用简写语法，比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'xhs-Matt'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
&#125;
<span class="hljs-keyword">let</span> &#123; name, age &#125; = person
<span class="hljs-built_in">console</span>.log(name) <span class="hljs-comment">// xhs-Matt</span>
<span class="hljs-built_in">console</span>.log(age) <span class="hljs-comment">// 18</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解构不成功以及对象解构可以指定一些默认值的情况，这些详细内容可以见我们的<a href="https://xhs-rookies.com/docs/ECMAScript%206/2.%20%E5%8F%98%E9%87%8F%E7%9A%84%E8%A7%A3%E6%9E%84%E8%B5%8B%E5%80%BC" target="_blank" rel="nofollow noopener noreferrer">解构赋值</a>文章，在对象中我们不过多赘述。</p>
<h3 data-id="heading-14">继承</h3>
<p>本章前面花了大量篇幅讨论如何使用 <code>ES5</code> 的机制实现继承。<code>ECMAScript 6 </code> 新增特性中最出色的一 个就是原生支持了类继承机制。虽然类继承使用的是新语法，但背后依旧使用的是原型链。</p>
<h4 data-id="heading-15">继承基础</h4>
<p><code>ES6</code>类支持单继承。使用 <code>extends</code> 关键字，就可以继承任何拥有 <code>[[Construct]]</code> 和原型的对象。 很大程度上，这意味着不仅可以继承一个类，也可以继承普通的构造函数（保持向后兼容）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span> </span>&#123;&#125;
<span class="hljs-comment">// 继承类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bus</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vehicle</span> </span>&#123;&#125;
<span class="hljs-keyword">let</span> b = <span class="hljs-keyword">new</span> Bus()
<span class="hljs-built_in">console</span>.log(b <span class="hljs-keyword">instanceof</span> Bus) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(b <span class="hljs-keyword">instanceof</span> Vehicle) <span class="hljs-comment">// true</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-comment">// 继承普通构造函数</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Engineer</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;&#125;
<span class="hljs-keyword">let</span> e = <span class="hljs-keyword">new</span> Engineer()
<span class="hljs-built_in">console</span>.log(e <span class="hljs-keyword">instanceof</span> Engineer) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(e <span class="hljs-keyword">instanceof</span> Person) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>派生类都会通过原型链访问到类和原型上定义的方法。<code>this</code> 的值会反映调用相应方法的实例或者类：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">identifyPrototype</span>(<span class="hljs-params">id</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(id, <span class="hljs-built_in">this</span>)
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">identifyClass</span>(<span class="hljs-params">id</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(id, <span class="hljs-built_in">this</span>)
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bus</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vehicle</span> </span>&#123;&#125;
<span class="hljs-keyword">let</span> v = <span class="hljs-keyword">new</span> Vehicle()
<span class="hljs-keyword">let</span> b = <span class="hljs-keyword">new</span> Bus()
b.identifyPrototype(<span class="hljs-string">'bus'</span>) <span class="hljs-comment">// bus, Bus &#123;&#125;</span>
v.identifyPrototype(<span class="hljs-string">'vehicle'</span>) <span class="hljs-comment">// vehicle, Vehicle &#123;&#125;</span>
Bus.identifyClass(<span class="hljs-string">'bus'</span>) <span class="hljs-comment">// bus, class Bus &#123;&#125;</span>
Vehicle.identifyClass(<span class="hljs-string">'vehicle'</span>) <span class="hljs-comment">// vehicle, class Vehicle &#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意:</strong> <code>extends</code>关键字也可以在类表达式中使用，因此 <code>let Bar = class extends Foo &#123;&#125;</code> 是有效的语法。</p>
<h4 data-id="heading-16">构造函数、HomeObject 和 super()</h4>
<p>派生类的方法可以通过 <code>super</code>关键字引用它们的原型。这个关键字只能在派生类中使用，而且仅限于类构造函数、实例方法和静态方法内部。在类构造函数中使用 <code>super</code>可以调用父类构造函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.hasEngine = <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bus</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 不要在调用 super()之前引用 this，否则会抛出 ReferenceError</span>
    <span class="hljs-built_in">super</span>() <span class="hljs-comment">// 相当于 super.constructor()</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span> <span class="hljs-keyword">instanceof</span> Vehicle) <span class="hljs-comment">// true</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>) <span class="hljs-comment">// Bus &#123; hasEngine: true &#125;</span>
  &#125;
&#125;
<span class="hljs-keyword">new</span> Bus()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在静态方法中可以通过 <code>super</code> 调用继承的类上定义的静态方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">identify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'vehicle'</span>)
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bus</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">identify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>.identify()
  &#125;
&#125;
Bus.identify() <span class="hljs-comment">// vehicle</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意:</strong> <code>ES6</code>给类构造函数和静态方法添加了内部特性 <code>[[HomeObject]]</code>，这个特性是一个指针，指向定义该方法的对象。这个指针是自动赋值的，而且只能在 JavaScript 引擎内部访问。<code>super</code> 始终会定义为<code>[[HomeObject]]</code> 的原型。</p>
<h4 data-id="heading-17">使用 super 时要注意几个问题</h4>
<ul>
<li><code>super</code> 只能在派生类构造函数和静态方法中使用。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>()
    <span class="hljs-comment">// SyntaxError: 'super' keyword unexpected</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>不能单独引用 <code>super</code> 关键字，要么用它调用构造函数，要么用它引用静态方法。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span> </span>&#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bus</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">super</span>)
    <span class="hljs-comment">// SyntaxError: 'super' keyword unexpected here</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>调用 <code>super()</code>会调用父类构造函数，并将返回的实例赋值给 <code>this</code>。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span> </span>&#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bus</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>()
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span> <span class="hljs-keyword">instanceof</span> Vehicle)
  &#125;
&#125;
<span class="hljs-keyword">new</span> Bus() <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>super()</code>的行为如同调用构造函数，如果需要给父类构造函数传参，则需要手动传入。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">licensePlate</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.licensePlate = licensePlate
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bus</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">licensePlate</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(licensePlate)
  &#125;
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> Bus(<span class="hljs-string">'1337H4X'</span>)) <span class="hljs-comment">// Bus &#123; licensePlate: '1337H4X' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果没有定义类构造函数，在实例化派生类时会调用 <code>super()</code>，而且会传入所有传给派生类的 参数。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">licensePlate</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.licensePlate = licensePlate
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bus</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vehicle</span> </span>&#123;&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> Bus(<span class="hljs-string">'1337H4X'</span>)) <span class="hljs-comment">// Bus &#123; licensePlate: '1337H4X' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在类构造函数中，不能在调用 <code>super()</code> 之前引用<code>this</code>。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span> </span>&#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bus</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
  &#125;
&#125;
<span class="hljs-keyword">new</span> Bus()
<span class="hljs-comment">// ReferenceError: Must call super constructor in derived class</span>
<span class="hljs-comment">// before accessing 'this' or returning from derived constructor</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果在派生类中显式定义了构造函数，则要么必须在其中调用 <code>super()</code>，要么必须在其中返回 一个对象。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span> </span>&#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vehicle</span> </span>&#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bus</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>()
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Van</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vehicle</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;&#125;
  &#125;
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> Car()) <span class="hljs-comment">// Car &#123;&#125;</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> Bus()) <span class="hljs-comment">// Bus &#123;&#125;</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> Van()) <span class="hljs-comment">// &#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">包装对象</h3>
<h4 data-id="heading-19">原始值包装类型</h4>
<p>为了方便操作原始值，<code>ECMAScript</code> 提供了 3 种特殊的引用类型：<code>Boolean</code>、<code>Number</code> 和 <code>String</code>。 这些类型具有本章介绍的其他引用类型一样的特点，但也具有与各自原始类型对应的特殊行为。每当用到某个原始值的方法或属性时，后台都会创建一个相应原始包装类型的对象，从而暴露出操作原始值的 各种方法。来看下面的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> s1 = <span class="hljs-string">'xhs-rookies'</span>
<span class="hljs-keyword">let</span> s2 = s1.substring(<span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里，<code>s1</code> 是一个包含字符串的变量，它是一个原始值。第二行紧接着在 <code>s1</code> 上调用了 <code>substring()</code> 方法，并把结果保存在 <code>s2</code> 中。我们知道，原始值本身不是对象，因此逻辑上不应该有方法。而实际上 这个例子又确实按照预期运行了。这是因为后台进行了很多处理，从而实现了上述操作。具体来说，当 第二行访问 <code>s1</code> 时，是以读模式访问的，也就是要从内存中读取变量保存的值。在以读模式访问字符串 值的任何时候，后台都会执行以下 3 步：</p>
<p>（1）创建一个 <code>String</code> 类型的实例；</p>
<p>（2）调用实例上的特定方法；</p>
<p>（3）销毁实例。</p>
<p>可以把这 3 步想象成执行了如下 3 行 <code>ECMAScript</code> 代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> s1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">'xhs-rookies'</span>)
<span class="hljs-keyword">let</span> s2 = s1.substring(<span class="hljs-number">2</span>)
s1 = <span class="hljs-literal">null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种行为可以让原始值拥有对象的行为。对布尔值和数值而言，以上 3 步也会在后台发生，只不过 使用的是 <code>Boolean</code>和 <code>Number</code> 包装类型而已。 引用类型与原始值包装类型的主要区别在于对象的生命周期。在通过 <code>new</code> 实例化引用类型后，得到 的实例会在离开作用域时被销毁，而自动创建的原始值包装对象则只存在于访问它的那行代码执行期 间。这意味着不能在运行时给原始值添加属性和方法。比如下面的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> s1 = <span class="hljs-string">'xhs-rookies'</span>
s1.color = <span class="hljs-string">'red'</span>
<span class="hljs-built_in">console</span>.log(s1.color) <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的第二行代码尝试给字符串 s1 添加了一个 <code>color</code> 属性。可是，第三行代码访问 <code>color</code> 属性时， 它却不见了。原因就是第二行代码运行时会临时创建一个 <code>String</code>对象，而当第三行代码执行时，这个对象已经被销毁了。实际上，第三行代码在这里创建了自己的 <code>String</code> 对象，但这个对象没有 <code>color</code> 属性。</p>
<p>可以显式地使用 <code>Boolean</code>、<code>Number</code> 和<code>String</code> 构造函数创建原始值包装对象。不过应该在确实必 要时再这么做，否则容易让开发者疑惑，分不清它们到底是原始值还是引用值。在原始值包装类型的实 例上调用 <code>typeof</code>会返回 <code>"object"</code>，所有原始值包装对象都会转换为布尔值<code>true</code>。</p>
<p>另外，<code>Object</code> 构造函数作为一个工厂方法，能够根据传入值的类型返回相应原始值包装类型的实 例。比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>(<span class="hljs-string">'xhs-rookies'</span>)
<span class="hljs-built_in">console</span>.log(obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">String</span>) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果传给 <code>Object</code> 的是字符串，则会创建一个 <code>String</code> 的实例。如果是数值，则会创建 <code>Number</code> 的 实例。布尔值则会得到 <code>Boolean</code> 的实例。</p>
<p>注意，使用 <code>new</code> 调用原始值包装类型的构造函数，与调用同名的转型函数并不一样。例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> value = <span class="hljs-string">'18'</span>
<span class="hljs-keyword">let</span> number = <span class="hljs-built_in">Number</span>(value) <span class="hljs-comment">// 转型函数</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> number) <span class="hljs-comment">// "number"</span>
<span class="hljs-keyword">let</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(value) <span class="hljs-comment">// 构造函数</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> obj) <span class="hljs-comment">// "object"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，变量 <code>number</code> 中保存的是一个值为 25 的原始数值，而变量 <code>obj</code>中保存的是一个 <code>Number</code> 的实例。</p>
<p>虽然不推荐显式创建原始值包装类型的实例，但它们对于操作原始值的功能是很重要的。每个原始值包装类型都有相应的一套方法来方便数据操作。</p>
<h2 data-id="heading-20">题目自测</h2>
<p><strong>一：所有对象都有原型。</strong></p>
<ul>
<li>A: 对</li>
<li>B: 错</li>
</ul>
<details>
<summary>Answer</summary>
**Answer：B**
<p>除了基本对象（<code>base object</code>），所有对象都有原型。基本对象可以访问一些方法和属性，比如 <code>.toString</code>。这就是为什么你可以使用内置的 <code>JavaScript</code> 方法！所有这些方法在原型上都是可用的。虽然<code>JavaScript</code>不能直接在对象上找到这些方法，但 <code>JavaScript </code>会沿着原型链找到它们，以便于你使用。</p>
</details>
<hr>
<p><strong>二：以下哪一项会对对象 person 有副作用？</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Lydia Hallie'</span>,
  <span class="hljs-attr">address</span>: &#123;
    <span class="hljs-attr">street</span>: <span class="hljs-string">'100 Main St'</span>,
  &#125;,
&#125;

<span class="hljs-built_in">Object</span>.freeze(person)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>A: <code>person.name = "Evan Bacon"</code></li>
<li>B: <code>delete person.address</code></li>
<li>C: <code>person.address.street = "101 Main St"</code></li>
<li>D: <code>person.pet = &#123; name: "Mara" &#125;</code></li>
</ul>
<details>
<summary>Answer</summary>
<p><strong>Answer：C</strong></p>
<p>使用方法 <code>Object.freeze</code> 对一个对象进行 冻结。不能对属性进行添加，修改，删除。</p>
<p>然而，它仅对对象进行浅冻结，意味着只有 对象中的 直接 属性被冻结。如果属性是另一个 <code>object</code>，像案例中的 <code>address</code>，<code>address</code> 中的属性没有被冻结，仍然可以被修改。</p>
</details>
<hr>
<p><strong>三：使用哪个构造函数可以成功继承<code>Dog</code>类?</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Labrador</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Dog</span> </span>&#123;
  <span class="hljs-comment">// 1</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, size</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.size = size
  &#125;
  <span class="hljs-comment">// 2</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, size</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name)
    <span class="hljs-built_in">this</span>.size = size
  &#125;
  <span class="hljs-comment">// 3</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">size</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(name)
    <span class="hljs-built_in">this</span>.size = size
  &#125;
  <span class="hljs-comment">// 4</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, size</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name
    <span class="hljs-built_in">this</span>.size = size
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>A: 1</li>
<li>B: 2</li>
<li>C: 3</li>
<li>D: 4</li>
</ul>
<details>
<summary>Answer</summary>
<p><strong>Answer：B</strong></p>
<p>在子类中，在调用 <code>super</code> 之前不能访问到 <code>this</code> 关键字。 如果这样做，它将抛出一个 <code>ReferenceError：1</code> 和 4 将引发一个引用错误。</p>
<p>使用 <code>super</code> 关键字，需要用给定的参数来调用父类的构造函数。 父类的构造函数接收 <code>name</code> 参数，因此我们需要将 <code>name</code> 传递给 <code>super</code>。</p>
<p><code>Labrador</code> 类接收两个参数，<code>name</code> 参数是由于它继承了 <code>Dog</code>，<code>size</code> 作为 <code>Labrador</code> 类的额外属性，它们都需要传递给 <code>Labrador</code> 的构造函数，因此使用构造函数 2 正确完成。</p>
</details>
<pre><code class="hljs language-mdx-code-block copyable" lang="mdx-code-block">import DocFooter from "../../src/components/doc-footer"

<DocFooter/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>JavaScript 系列的对象，我们到这里结束啦，谢谢各位对作者的支持！你们的关注和点赞，将会是我们前进的最强动力！谢谢大家！</strong></p></div>  
</div>
            