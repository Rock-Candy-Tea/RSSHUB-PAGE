
---
title: '快速入门kotlin-标准函数与静态方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8746'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 00:29:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=8746'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">标准函数</h1>
<p>首先我们介绍标准函数 with、run、apply，如果你了解javascript，那理解kotlin的标准函数width、run、apply那简直不要太轻松。with、run、apply与javascript中的with的意义基本一模一样，只是含有一些细微差别。</p>
<h2 data-id="heading-1">with</h2>
<p>with它接收两个参数，第一个参数可以是任意类型的对象，第二个参数是一个Lambda表达式。with函数会在Lambda表达式中提供第一个对象的上下文，可以直接使用对象的属性或方法，而不需要带上对象前缀。with函数会使用Lambda表达式中的最后一行代码作为返回值返回。</p>
<pre><code class="hljs language-kt copyable" lang="kt"><span class="hljs-keyword">val</span> result = with(obj) &#123;
<span class="hljs-comment">// 这里是obj的上下文环境</span>
doSomething() <span class="hljs-comment">// 调用obj的doSomething方法，无需 obj.doSomething() 这种形式调用</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">run</h2>
<p>run函数的用法与使用场景和with函数非常类似，只是做了些许改动。run函数无法直接调用，他需要在某个对象的基础上去调用它；其次run函数值接收一个Lambda表达式作为参数，并且会在Lambda表达中提供调用对象的上下文，同样将Lambda表达式中的最后一行代码作为返回值。</p>
<p>val result = obj.run &#123;
// 这里是obj的上下文环境
doSomething() // 调用obj的doSomething方法，无需 obj.doSomething() 这种形式调用
&#125;</p>
<h2 data-id="heading-3">apply</h2>
<p>apply函数和run函数在用法上基本一模一样，唯一区别是apply函数不会将Lambda表达式中的最后一行作为参数返回，而是会返回对象本身.</p>
<pre><code class="hljs language-kt copyable" lang="kt"><span class="hljs-keyword">val</span> result = obj.apply &#123;
<span class="hljs-comment">// 这里是obj的上下文环境</span>
doSomething() <span class="hljs-comment">// 调用obj的doSomething方法，无需 obj.doSomething() 这种形式调用</span>
&#125;
<span class="hljs-comment">// result == obj</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">静态方法</h1>
<p>在java中定义一个静态方法如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Util</span> </span>&#123;
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">doSome</span><span class="hljs-params">()</span> </span>&#123;
<span class="hljs-comment">// todo</span>
&#125;
&#125;

<span class="hljs-comment">// 使用静态方法</span>
Util.doSome()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而Kotlin提供了几种方式去实现类似java中的静态方法</p>
<ul>
<li>单例类实现静态方法</li>
</ul>
<pre><code class="hljs language-kt copyable" lang="kt"><span class="hljs-comment">// 声明一个单例类</span>
<span class="hljs-keyword">object</span> Util &#123;
<span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">doSome</span><span class="hljs-params">()</span></span> &#123;
<span class="hljs-comment">// todo</span>
&#125;
&#125;
<span class="hljs-comment">// 使用</span>
Util.doSome()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>伴生类实现静态方法</li>
</ul>
<p>单例类的写法会让类中的所有方法全部变成了类似静态方法的调用形式，如果我们只是希望类中的某些方法变成静态方法的调用形式怎么办呢？kotlin给我们提供了伴生类 companion object。</p>
<pre><code class="hljs language-kt copyable" lang="kt"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Utl</span> </span>&#123;
<span class="hljs-keyword">companion</span> obj &#123;
<span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">doSome</span><span class="hljs-params">()</span></span> &#123;
<span class="hljs-comment">// todo</span>
&#125;
&#125;
&#125;

<span class="hljs-comment">// 使用</span>
Util.doSome()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个关键字实际会在Util类的内部创建一个伴生类，Kotlin会保证一个类中只会存在一个伴生类对象,调用Util.doSome()实际上是调用Util类中的伴生类对象的doSome方法。</p>
<ul>
<li>注解实现静态方法</li>
</ul>
<p>如果我们确确实实需要定义真正的静态方法，我们可以给单例类或companion object伴生类中的方法加上 @JvmStatic注解，那么kotlin编译器就会将这些方法编译成真正的静态方法。注意这个注释一般加在单例类或伴生类的方法上，如果加在普通方法上，会直接提示语法错误。</p>
<pre><code class="hljs language-kt copyable" lang="kt"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Utl</span> </span>&#123;
<span class="hljs-keyword">companion</span> obj &#123;
<span class="hljs-meta">@JvmStatic</span>
<span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">doSome</span><span class="hljs-params">()</span></span> &#123;
<span class="hljs-comment">// todo</span>
&#125;
&#125;
&#125;

<span class="hljs-comment">// 使用</span>
Util.doSome()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>顶层方法实现静态方法</li>
</ul>
<p>顶层方法指的是哪些没有定义在任何类中的方法，比如我们编写的main()方法。kotlin编译器会将所有的顶层方法全部编译成静态方法。所有的顶层方法在任何位置可以直接被调用，不用管包名路径，也不用创建实例。但如果这个方法在Java代码中调用，需要加上该方法所在的文件名。</p>
<pre><code class="hljs language-kt copyable" lang="kt"><span class="hljs-comment">// 如我们在Tool.kt 文件中创建了一个顶层方法</span>
<span class="hljs-comment">// Tool.kt</span>
<span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">doSome</span><span class="hljs-params">()</span></span> &#123;
<span class="hljs-comment">// todo</span>
&#125;

<span class="hljs-comment">// 在java代码中使用</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">JavaTest</span> </span>&#123;
<span class="hljs-keyword">public</span> void invokeStaticFunc() &#123;
<span class="hljs-comment">// 文件名+方法形式调用顶层方法</span>
Tool.doSome()
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            