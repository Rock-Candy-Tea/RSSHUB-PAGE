
---
title: 'JavaScripts高阶（9）前端必须了解的函数的三种角色'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3786caa569514650b1b9b54e3bd7ba37~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 10 May 2021 18:49:32 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3786caa569514650b1b9b54e3bd7ba37~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1、普通函数</h2>
<ul>
<li>堆栈内存</li>
<li>作用域链</li>
</ul>
<h2 data-id="heading-1">2、类（构造函数）</h2>
<ul>
<li>prototype  原型</li>
<li><code>__proto__</code> 原型链</li>
<li>实例</li>
</ul>
<h2 data-id="heading-2">3、普通对象</h2>
<ul>
<li>和普通的obj没啥区别，就是对键值对的增删改查</li>
</ul>
<h2 data-id="heading-3">三种角色没有必然关系</h2>
<p>1、<code>私有变量只跟普通函数有关</code>，在作为类和普通对象情况下是没用的（获取不到）</p>
<p>2、<code>prototype是函数作为普通对象的一个属性，但是prototype里边放的东西就跟它就没关系了而是跟它的实例有关系；</code></p>
<p>3、<code>凡是Fn.prototype.xxx=xxx都是跟作为构造函数创建出来的实例有关</code></p>
<p>4、<code>在new Fn()的方式中，函数体中的this.xxx=xxx 都是跟作为构造函数创建出来的实例有关</code></p>
<p>5、<code>作为普通对象时，只有  Fn.属性名=属性值 这种才和它有关系</code></p>
<p>6、<code>函数体中的代码跟作为普通对象没关系，因为函数体中放的是字符串，不执行一点意义也没有，而作为对象不需要执行就能操作键值对</code></p>
<p>7、<code>new xxx也会使函数执行</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Fn</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">var</span> n=<span class="hljs-number">10</span>;
<span class="hljs-built_in">this</span>.m=<span class="hljs-number">100</span>;
&#125;
Fn.prototype.aa=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'aa'</span>)
&#125;
Fn.bb=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'bb'</span>)
&#125;

<span class="hljs-comment">//=>普通函数的执行</span>
Fn();     <span class="hljs-comment">//this：window     有一个私有变量 n  ； 和原型以及属性没有关系</span>

<span class="hljs-comment">//=>构造函数执行</span>
<span class="hljs-keyword">var</span> f=<span class="hljs-keyword">new</span> Fn();  <span class="hljs-comment">//this：f    </span>
<span class="hljs-built_in">console</span>.log(f.n)   <span class="hljs-comment">//undefined n为私有变量 和实例没有关系</span>
<span class="hljs-built_in">console</span>.log(f.m)   <span class="hljs-comment">//100  实例的私有属性</span>
f.aa();           <span class="hljs-comment">//'aa'   通过原型链找到了 Fn.prototype上的方法</span>
f.bb();           <span class="hljs-comment">//bb  is undefined  bb是把Fn当做一个普通对象设置的属性而已；和实例等没有半毛钱关系</span>

<span class="hljs-comment">//=>普通对象   只跟Fn.bb有关   prototype是函数对象的一个属性，但是prototype里边放的东西跟它就没关系了</span>
Fn.bb()       <span class="hljs-comment">//'bb'</span>



<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">以Number内置类为例：</h3>
<p>console.dir(Number)</p>
<h4 data-id="heading-5">把Number作为普通对象加入的方法，点前边必须为Number</h4>
<h4 data-id="heading-6">Number的prototype里存的方法是实例的方法，所以点前边必须是Number的具体实例才能调用（数字或者NaN）</h4>
<p>jQuery这个类库中提供了很多的方法，其中有一部分是写在原型上的，有一部分是把它当做普通对象来设置的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">~<span class="hljs-function"><span class="hljs-keyword">function</span>  (<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jQuery</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-comment">//...</span>
<span class="hljs-comment">//return  [jQuery实例]</span>
&#125;
jQuery.prototype.animate=<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;&#125;
jQuery.ajax=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;

<span class="hljs-built_in">window</span>.jQuery = <span class="hljs-built_in">window</span>.$ =jQuery;
&#125;();

$(); <span class="hljs-comment">//返回实例</span>
$().ajax()  <span class="hljs-comment">//不能调用，ajax是普通对象的键值对</span>
$.ajax()  <span class="hljs-comment">//可以  直接调取普通对象键值对</span>
$().animate()  <span class="hljs-comment">//可以   </span>

$.animate()  <span class="hljs-comment">//不可以   对象上没有animate这个属性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>var getName=function()&#123;&#125;，在全局变量提升中只是定义 没赋值，getName为undefined,在代码执行的时候才赋值；function getName 声明并赋值全局 getName  为‘console.log（5）’ 代码执行的时候就不再进行任何操作  <strong><code>重要注意点</code></strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span>(<span class="hljs-params"></span>)</span>&#123;
getName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
&#125;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
&#125;
Foo.getName=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)
&#125;
Foo.prototype.getName=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)
&#125;
<span class="hljs-keyword">var</span> getName=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;     <span class="hljs-comment">//全局变量提升阶段只声明不定义    在代码执行的时候给变量赋值 会把console.log(5)的函数顶掉</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">4</span>)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getName</span>(<span class="hljs-params"></span>)</span>&#123;         <span class="hljs-comment">//全局变量提升阶段声明并定义 代码执行的时候就不再进行任何操作</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>)
&#125;
Foo.getName();               <span class="hljs-comment">//  2</span>
getName();                   <span class="hljs-comment">//4</span>
Foo().getName();             <span class="hljs-comment">//  1</span>
getName(); <span class="hljs-comment">//1</span>
<span class="hljs-keyword">new</span> Foo.getName();           <span class="hljs-comment">//=>A:(Foo.getName) =>new A;   2</span>
<span class="hljs-keyword">new</span> Foo().getName()          <span class="hljs-comment">//=>B:new Foo() =>B.getName()  3</span>
<span class="hljs-keyword">new</span> <span class="hljs-keyword">new</span> Foo().getName();     <span class="hljs-comment">//=>C:new Foo() =>把C.getName作为一个整体new（C是Foo的实例） D：C.getName  =>  new D()  3</span>

<span class="hljs-comment">//=>全局作用域  </span>
<span class="hljs-comment">//变量提升 Foo,getName</span>
<span class="hljs-comment">//Foo=AAAFFF111(1、开辟堆内存2、存字符串3、建立联系)天生自带 prototype</span>
<span class="hljs-comment">//getName=AAAFFF222(1、开辟堆内存2、存字符串3、建立联系)天生自带 prototype</span>
<span class="hljs-comment">//var getName=，在全局变量提升中只是定义 没赋值；function getName 声明并赋值全局 getName  为‘console.log（5）’  **重要注意点**</span>

<span class="hljs-comment">//=>代码执行</span>
<span class="hljs-comment">//AAAFFF111.getName=bbbFFF111   console.log(2)  Foo作为普通对象添加键值对</span>
<span class="hljs-comment">//AAAFFF111.prototype.getName=bbbFFF222   console.log(3)</span>
<span class="hljs-comment">//var getName=， 因为在变量提升中声明过所以只赋值；所以全局getName为‘console.log（4）’</span>
<span class="hljs-comment">//Foo作为普通对象的getName执行  2</span>
<span class="hljs-comment">//全局getName（window.getName）执行 4</span>
<span class="hljs-comment">//Foo作为普通函数执行，把返回值的getName执行</span>
<span class="hljs-comment">//Foo作为普通函数执行形成私有作用域  </span>
<span class="hljs-comment">//形参赋值  变量提升没有</span>
<span class="hljs-comment">//代码执行</span>
<span class="hljs-comment">//全局getName  console.log（1）</span>
<span class="hljs-comment">//return this  为 window</span>
<span class="hljs-comment">//window.getName执行  1</span>
<span class="hljs-comment">//全局getName（window.getName）执行   1</span>
<span class="hljs-comment">//(new (Foo.getName))()  Foo作为普通对象的getName属性 执行  2</span>
<span class="hljs-comment">//(new Foo()).getName()  实例.getName执行    3</span>
<span class="hljs-comment">//(new ((new Foo()).getName))()     (实例.getName)的实例  执行  3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>在Foo后面没有东西的时候，new Foo和new Foo()是一样的；但是在Foo后面有东西时就不一样了：new Foo.getName()  是把new Foo.getName作为一个整体new的 相当于A:（Foo.getName） new A；new Foo().getName() 先new Foo() 让实例的getName执行</code></p>
<h3 data-id="heading-7">js中的运算符优先级 (数值越大优先级越高)</h3>
<p>从左到右：同级别 从左到右先写谁，谁的优先级高</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3786caa569514650b1b9b54e3bd7ba37~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/331a89ca4162437f944b3f4a7ca4cfde~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5549a88bfa246ad8749f61703d25a1e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            