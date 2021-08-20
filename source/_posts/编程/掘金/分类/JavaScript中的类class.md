
---
title: 'JavaScript中的类class'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9669'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 01:51:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=9669'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI4MDYyNjQ1OA%3D%3D%26mid%3D2247483956%26idx%3D1%26sn%3Dadc1ec7ae4cd3f01728fdcb43a38690f%26chksm%3Debb4d641dcc35f57cd2bf66ba9819874cf300108884700bf3d6a1410c18c0ed4ff3d90d10a8f%23rd" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzI4MDYyNjQ1OA==&mid=2247483956&idx=1&sn=adc1ec7ae4cd3f01728fdcb43a38690f&chksm=ebb4d641dcc35f57cd2bf66ba9819874cf300108884700bf3d6a1410c18c0ed4ff3d90d10a8f#rd" ref="nofollow noopener noreferrer">参考文献</a></p>
</blockquote>
<h2 data-id="heading-0">1. ES5中的近类结构</h2>
<p>ES5中创建类的方法：</p>
<p>新建一个构造函数，定义一个方法并且赋值给构造函数的原型。</p>
<blockquote>
<p>proto、prototype参考p21</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//新建构造函数，大写字母开头</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
&#125;
<span class="hljs-comment">//定义一个方法并赋值给构造函数的原型</span>
Person.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;
<span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'Tom'</span>);
<span class="hljs-built_in">console</span>.log(p.sayName());
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. ES6中的class</h2>
<blockquote>
<p>ES6实现类很简单，只需要类声明。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
    <span class="hljs-comment">//新建构造函数</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.name = name;<span class="hljs-comment">//私有属性</span>
    &#125;
    <span class="hljs-comment">//定义一个方法并赋值给构造函数的原型</span>
    <span class="hljs-function"><span class="hljs-title">sayName</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
    &#125;
&#125;
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'Tom'</span>)
<span class="hljs-built_in">console</span>.log(p.sayName())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与ES5中使用构造函数不同的是，<strong>私有属性是实例中的属性，不会出现在原型上</strong>。</p>
<p>类声明和函数声明的区别和特点：</p>
<p>1、函数声明可以被提升，<strong>类声明不能提升</strong>(与let声明类似)。</p>
<p>2、类声明中的代码自动强行运行在<strong>严格模式</strong>下。</p>
<p>3、类中的所有方法都是不可枚举的，而自定义类型中，可以通过Object.defineProperty()手工指定不可枚举属性。</p>
<p>4、每个类都有一个[[construct]]的方法。</p>
<p>5、<strong>只能使用new来调用类的构造函数。</strong></p>
<p>6、不能在类中修改类名。</p>
<h3 data-id="heading-2">类表达式</h3>
<p>类有声明式和表达式两种表现形式：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//声明式</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
&#125;
<span class="hljs-comment">//匿名表达式</span>
<span class="hljs-keyword">let</span> A = <span class="hljs-class"><span class="hljs-keyword">class</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">construnctor</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
&#125;
<span class="hljs-comment">//命名表达式，B可以在外部使用，B1只能在内部使用</span>
<span class="hljs-keyword">let</span> B = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B1</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">3. 类的应用场景</h2>
<p>JavaScript函数是一等公民，类也设计成一等公民。</p>
<h3 data-id="heading-4">(1) 类作为参数传入函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> A = <span class="hljs-class"><span class="hljs-keyword">class</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">sayName</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'Tom'</span>
    &#125;
&#125;
<span class="hljs-comment">//该函数返回一个类的实例</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params">classA</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> classA()
&#125;
<span class="hljs-comment">//给test函数传A</span>
<span class="hljs-keyword">let</span> t = test(A)
<span class="hljs-built_in">console</span>.log(t.sayName)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">(2) 通过立即执行函数，调用类构造函数创建单例</h3>
<p>用new调用类的表达式，接着()调用表达式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-keyword">new</span> <span class="hljs-class"><span class="hljs-keyword">class</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.name = name
    &#125;
    <span class="hljs-function"><span class="hljs-title">sayName</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name
    &#125;
&#125;(<span class="hljs-string">'Tom'</span>)
<span class="hljs-built_in">console</span>.log(a.sayName())
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">4. 类的静态成员</h2>
<p>静态成员是指在方法名或属性名前面加上static关键字，和普通方法不一样的是，static修饰的方法不能在实例中访问，只能用类名直接访问。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.name = name
    &#125;
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params">name</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> A(name)
    &#125;
&#125;
<span class="hljs-keyword">let</span> a = A.create(<span class="hljs-string">'TOM'</span>)
<span class="hljs-built_in">console</span>.log(a.name)<span class="hljs-comment">//TOM</span>
<span class="hljs-keyword">let</span> t = <span class="hljs-keyword">new</span> A()
<span class="hljs-built_in">console</span>.log(t.create(<span class="hljs-string">'Tom'</span>))<span class="hljs-comment">//t.create is not a function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">5. 继承与派生</h2>
<p>比如自定义react组件要继承React.Component</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span>&#123;
        <span class="hljs-built_in">super</span>(props)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>A是派生类，在派生类中使用构造方法必须使用super.</p>
<p>关于super使用的几点要求：</p>
<ul>
<li>1、只可以在派生类中使用super。派生类是指继承自其它类的新类。</li>
<li>2、在构造函数中访问this之前要调用super()，负责初始化this。</li>
</ul>
<h3 data-id="heading-8">(1)在继承的类中重写父类方法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">[a,b] = props</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.a = a
        <span class="hljs-built_in">this</span>.b = b
    &#125;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.a + <span class="hljs-built_in">this</span>.b
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">T</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span>&#123;
        <span class="hljs-built_in">super</span>(props)
    &#125;
    <span class="hljs-comment">//重写父类方法add</span>
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.a * <span class="hljs-built_in">this</span>.b
    &#125;
&#125;
<span class="hljs-keyword">let</span> t = <span class="hljs-keyword">new</span> T([<span class="hljs-number">2</span>,<span class="hljs-number">3</span>])
<span class="hljs-built_in">console</span>.log(t.add())<span class="hljs-comment">//6</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            