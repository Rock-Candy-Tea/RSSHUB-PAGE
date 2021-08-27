
---
title: 'JavaScript 回顾（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bc2ebd3711f4575a7a5fa43d065b439~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 07:56:06 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bc2ebd3711f4575a7a5fa43d065b439~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第26天，活动详情查看: <a href="https://juejin.cn/post/6967194882926444557" target="_blank" title="https://juejin.cn/post/6967194882926444557">更文挑战</a></p>
<h4 data-id="heading-0">1, this指向</h4>
<p>解析器在调用函数每次都会向函数内部传递一个隐含的参数， 这个隐含的参数就是this</p>
<p>this指向的是一个对象，这个对象我们称为函数执行的上下文，根据函数的调用方式的不同，this会指向不同的对象</p>
<ul>
<li>以函数形式调用，this指的就是window</li>
<li>以方法的形式调用，this就是调用方法的那个对象</li>
<li>以构造函数的形式调用，this就是调用的那个对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> name = <span class="hljs-string">'全局'</span>
​
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun</span>(<span class="hljs-params"></span>) </span>&#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-keyword">var</span> obj = &#123;
   <span class="hljs-attr">name</span>: <span class="hljs-string">'a'</span>,
   <span class="hljs-attr">sayName</span>:fun
&#125;
<span class="hljs-keyword">var</span> obj2 = &#123;
   <span class="hljs-attr">name</span>: <span class="hljs-string">'b'</span>,
   <span class="hljs-attr">sayName</span>:fun
&#125;
obj.sayName()
obj2.sayName()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2, 工厂模式</h4>
<p>（1） 使用工厂模式创建对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createPerson</span>(<span class="hljs-params">name, age</span>) </span>&#123;
   <span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()
   obj.name = name;
   obj.age = age;
   obj.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
   &#125;
   <span class="hljs-keyword">return</span> obj
&#125;
<span class="hljs-keyword">var</span> obj = createPerson(<span class="hljs-string">'zlm'</span>, <span class="hljs-number">18</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：使用工厂模式创建的对象，使用的构造函数都是Object,所以创建的对象都是Object这个类型，无法具体区分对象类型</p>
<p>（2） 构造函数</p>
<p>对于上面的问题，我们可以创建一个构造函数。构造函数就是一个普通函数，创建方式和普通函数没有区别，不同的方式是构造函数习惯上首字母大写。</p>
<p>注意：不同点， 普通函数是直接调用，而构造函数需要使用new关键字来调用</p>
<pre><code class="copyable">function Person(name, age) &#123;
   this.name = name
    this.age = age
&#125;
var per = new Person('zlm', 19)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(3) 构造函数执行流程</p>
<p>1， 通过new 调用构造函数的时候，立即创建一个新的对象</p>
<p>2， 将新建的对象设置为函数中的this, 在构造函数中可以使用this来引用新建的 对象</p>
<p>3， 一行一行的执行函数中的代码</p>
<p>4， 将新建的对象作为返回值返回</p>
<p>综上： 使用同一个构造函数创建的对象，我们称为一类对象，也将一个构造函数称为一个类， 通过一个构造函数创建的对象，称为该类的实例</p>
<p>注意：可以使用<code>instanceof</code>检查一个对象是否是一个类的实例</p>
<pre><code class="copyable">per instanceof  Person
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>所有的对象都是Object的后代，所以任何对象通过instanceof 检查都是ture</strong></p>
<p>（4） 构造函数性能</p>
<p>构造函数每执行一次，里面的属性就会创建一次，这就导致，每执行100次，就回创建100遍，非常消耗性能, 如果提取出来，定义在全局，会污染了全局作用域的命名空间</p>
<pre><code class="copyable">function Person(name, age, gender) &#123;
   this.name = name;
   this.age = age;
   this.gender = gender
   this.sayName = fun
&#125;
function fun（）&#123;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3, 原型</h4>
<p>（1） 什么是原型</p>
<p>我们所创建的每一个函数，解析器都会向函数中添加一个属性prototype, 这个属性对应着一个对象，这个对象就是我们所谓的原型对象</p>
<ul>
<li>如果函数作为普通函数调用，prototype没有任何作用</li>
<li>当函数以构造函数的形式调用时，它所创建的对象中都会有一个隐含的属性，这个隐含的属性值指向该构造函数的原型对象，我们可以通过<strong>ptoto</strong> 来访问该属性</li>
<li>原型对象就相当于一个公共的区域，所有同一个类的实例都可以访问到这个原型对象，我们可以将对象中共有的内容，统一设置到原型对象中</li>
<li>当我们访问一个对象的属性或者方法时，它会先在对象自身中寻找，如果有则直接使用，如果没有则会去原型对象中寻找，如果找到直接使用</li>
</ul>
<pre><code class="copyable">function MyClass() &#123;
​
&#125;
var mc = new MyClass()
var mc2 = new MyClass()
console.log(MyClass.prototype)
console.log(mc2.__proto__ === MyClass.prototype)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>向原型对象中添加属性</p>
<pre><code class="copyable">MyClass.prototype.a = 123
MyClass.prototype.sayHello = function() &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：以后我们创建构造函数的时候，可以将这些对象共有的属性和方法，统一添加到构造函数的原型中，这样就不用分别为每一个对象添加，也不会影响到全局作用域，就可以使每一个对象都具有这些属性和方法了</p>
<p>（2）原型对象的对象</p>
<p>原型对象也是对象，所以它也是有原型。</p>
<ul>
<li>当我们使用一个对象的属性和方法时， 它会先在自身中寻找， 如果自身有，则直接使用。如果自身没有，则去原型对象中寻找，如果原型对象中又，则使用，如果没有则去原型的原型中寻找， 直到找到Object对象的原型，</li>
<li>Object对象的原型没有原型</li>
</ul>
<pre><code class="copyable">function MyClass() &#123;
 
&#125;
MyClass.prototype.name = '我是原型的对象'
var mc = new MyClass()
console.log(mc.name)
console.log('name' in mc)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意： 使用 in 检查对象中是否含有某个属性，如果对象中没有但是原型中有，也会返回ture， 如果只想检查自身中是否含有该属性，需要使用： <code>hasOwnProperty()</code></p>
<pre><code class="copyable">console.log(mc.hasOwnProperty("hasOwnProperty"))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原型的原型中寻找</p>
<pre><code class="copyable">mc.__proto__.proto__.hasOwnProperty("hasOwnProperty")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：最多两层, 儿子，——> 父亲——> 爷爷，一般这个时候就到Object</p>
<pre><code class="copyable">mc.__proto__.__proto__
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bc2ebd3711f4575a7a5fa43d065b439~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            