
---
title: '详细解析 JavaScript 闭包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://img-blog.csdnimg.cn/20200326095129142.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 23:17:29 GMT
thumbnail: 'https://img-blog.csdnimg.cn/20200326095129142.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>有的老师说JavaScript两大神兽：原型和闭包</p>
<p>有的老师说JavaScript两大难点：异步和闭包</p>
<p>反正不管哪一个都有闭包，可见真的是非常重要了。</p>
<p><strong>今天我就详细说一下闭包，看完你一定会有收获的。如果没看明白，一定是你没好好看。如果还没看明白，可以评论私信我给你讲。反正我自认为两大神兽已经攻克，我就是无敌的小萝莉</strong>。 ｡:.ﾟヽ(｡◕‿◕｡)ﾉﾟ.:｡+ﾟ</p>
<p>我看了两个老师的课，第一个老师讲的很深入，但是条理不太清晰，所以到最后我也感觉没听懂。直到第二个老师上来就仔细剖析了概念，我才恍然大悟。今天就结合起来写一下。</p>
<p>@[toc]</p>
<p> </p>
<hr>
<h1 data-id="heading-0">概念</h1>
<p>什么是闭包？要想了解闭包什么是闭包，先得从概念抓起来。</p>
<p> </p>
<blockquote>
<p>闭包（closure）是指有权访问另一个函数作用域中变量的函数     　　——《JavaScript高级程序设计》</p>
</blockquote>
<blockquote>
<p>（！！！记住这个英文单词，下边会有用）</p>
</blockquote>
<p> </p>
<p><strong>简单理解就是：</strong> 一个作用域可以访问另一个函数内部的局部变量。</p>
<p> </p>
<p>下图中三块作用域嵌套在一起：全局作用域中有一个<code>Fun</code>的函数作用域，<code>Fun</code>中有个局部变量<code>a</code>，还有一个函数<code>foo</code>，<code>foo</code>也有自己的函数作用域。<strong>不管是从<code>foo</code>中调用<code>Fun</code>的<code>a</code>变量，还是从全局作用域中调用<code>Fun</code>的<code>a</code>，都会形成闭包。</strong></p>
<p> </p>
<p><img src="https://img-blog.csdnimg.cn/20200326095129142.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h1 data-id="heading-1">如何产生闭包?</h1>
<ul>
<li>
<p><strong>当内部函数引用了外部函数的变量(函数)时, 就产生了闭包</strong></p>
</li>
<li>
<p><strong>当子函数引用了父函数的变量(函数)时, 就产生了闭包</strong></p>
</li>
</ul>
<p> </p>
<p>上面两种说法表达的是一个意思，拿概念中的图来说就是foo调用了Fun的变量或函数。</p>
<p> </p>
<h3 data-id="heading-2">解决问题1</h3>
<ul>
<li>
<p><s>当内部函数引用了外部函数的变量(函数)时, 就产生了闭包</s></p>
</li>
<li>
<p><s>当子函数引用了父函数的变量(函数)时, 就产生了闭包</s></p>
</li>
</ul>
<p> </p>
<p><kbd>你可能会说：“我听不懂。怎么内部引用外部变量就产生闭包了啊”</kbd></p>
<p> </p>
<p><strong>下边就举几个例子说明一下。</strong></p>
<h5 data-id="heading-3">举个栗子:chestnut: 不调用内部函数时已经产生闭包</h5>
<pre><code class="hljs language-js copyable" lang="js">
                     <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Fun</span>(<span class="hljs-params"></span>) </span>&#123;

                            <span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>

                            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;

                                   <span class="hljs-built_in">console</span>.log(a)

                            &#125;

                     &#125;

                     Fun()

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上边这段代码中，我们看一下控制台，我把断点打在<code>Fun()</code>这一句上。这个时候可以看到右边scope被我圈出来了，这时候下边只有一个global。</p>
<p>然后点击执行下一步。</p>
<p> </p>
<p><strong>如果不知道为什么打在这里，或者说我下边提到的匿看不懂，那你就需要回去学习<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_36667170%2Farticle%2Fdetails%2F105100870" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_36667170/article/details/105100870" ref="nofollow noopener noreferrer">变量提升、作用域、执行上下文</a>的内容。</strong></p>
<p><img src="https://img-blog.csdnimg.cn/20200326101104917.png" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个时候就到了<code>var a = 1</code>这一步上。右边的scope已经发生变化，出现一个local。local里边还有一个foo。看看上边红框框里我圈出来的调用栈，现在已经在调用Fun这个函数了。也就是说local现在指的是Fun这块作用域。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326101013998.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候你点开==local=>foo=>[[Scopes]]=>0==你就发现了新大陆，里边有closure，里边写的<code>a: undefined</code>也就是上边我让你记的闭包的英文单词。而这个<code>Closure(Fun)</code>意思就是Fun的闭包已经形成了。<strong>在变量提升的帮助下，只要内部函数被解析，内部函数不需要执行，就已经产生了闭包。</strong></p>
<p><img src="https://img-blog.csdnimg.cn/20200326101328691.png" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>为什么Fun的闭包已经形成了？</strong></p>
<p>看下图。因为这个时候foo已经被解析了，也就是说它已经调用a了，所以形成闭包了。但是a=1这句还没执行，所以a现在是undefined。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326104519857.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-4">举个反例:chestnut:加深理解不调用内部函数时已经产生闭包</h5>
<p>如果你代码写成下边这样他就不会形成闭包。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326103650618.png" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>查看一下控制台，确实没有闭包</p>
<p><img src="https://img-blog.csdnimg.cn/20200326104114126.png" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>知道为什么吧，再提醒一次，不知道就回去补习<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_36667170%2Farticle%2Fdetails%2F105100870" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_36667170/article/details/105100870" ref="nofollow noopener noreferrer">变量提升、作用域、执行上下文</a>。</strong></p>
<p>因为只有function声明的函数才会被提升。var声明的函数只会提升函数名。也就是说这时候函数体还没有解析，foo函数还没有调用到Fun的a变量。不信你可以继续往下自己试一试，当进入foo函数只会就会出现闭包的嗷(´,,•ω•,,`)</p>
<p><img src="https://img-blog.csdnimg.cn/20200326104409815.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-5">举个例子:chestnut:内部函数调用产生闭包</h5>
<p>看完上边两个例子，你当然那已经懂了，函数解析时候已经产生闭包了，调用的时候当然有闭包。 只不过区别是调用的时候a已经被赋值了。所以现在可以看到<code>a:1</code>了。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326105542327.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-6">再举个例子:chestnut:内部函数执行时不调用外部函数的变量，不产生闭包</h5>
<p>下图可以看出来，内部函数和外部函数的变量没有关系哦。所以内部函数即使执行了，右边scope那也没有显示产生闭包哦。(●′ω`●)</p>
<p><img src="https://img-blog.csdnimg.cn/20200326111846975.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">解决问题2</h3>
<ul>
<li>
<p>当内部函数引用了外部函数的<s>变量(函数)</s>时, 就产生了闭包</p>
</li>
<li>
<p>当子函数引用了父函数的<s>变量(函数)</s>时, 就产生了闭包</p>
</li>
</ul>
<p> </p>
<p><kbd>你可能会问：“你给出的概念那不是说调用变量吗，现在怎么加上（函数）了，<br>调用其他函数作用域中的函数也会形成闭包？”</kbd></p>
<p> </p>
<h5 data-id="heading-8">举个例子:chestnut:内部函数调用外部函数的其他子函数产生闭包</h5>
<p>不管是普通变量还是函数，只要内部的函数调用了外部函数的东西，就是闭包！！！</p>
<p><img src="https://img-blog.csdnimg.cn/20200326111523914.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">解决问题3</h3>
<ul>
<li>
<p><s>当内部函数</s>引用了外部函数的变量(函数)时, 就产生了闭包</p>
</li>
<li>
<p><s>当子函数</s>引用了父函数的变量(函数)时, 就产生了闭包</p>
</li>
</ul>
<p> </p>
<p><kbd>你可能还问：“你概念那不是说外部作用域调用Fun的变量也会产生闭包吗？我没<br>看到外部怎么调用啊。并且你这两条怎么都说的内部函数，没提全局作用域啊”</kbd></p>
<p> </p>
<p><strong>澄清一下，外部作用域的确可以调用某个函数的内部变量或函数，但也是借助该函数内部嵌套的子函数的。</strong></p>
<h5 data-id="heading-10">举个例子:chestnut:外部作用域如何调用内部变量产生闭包</h5>
<pre><code class="hljs language-js copyable" lang="js">
                     <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Fun</span>(<span class="hljs-params"></span>) </span>&#123;

                            <span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>

                            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;

                                   <span class="hljs-built_in">console</span>.log(a)

                            &#125;

                            <span class="hljs-keyword">return</span> foo;

                     &#125;

                     <span class="hljs-keyword">var</span> aa=Fun();

<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下上边这段代码，我帮你理一下。</p>
<p>上面这个代码运行的时候，先进行全局上下文的处理，进行变量提升。然后执行<code>aa=Fun()</code>赋值语句，调用Fun函数。此时进入Fun，Fun进行函数中的执行上下文处理。此时代码逻辑上会变成下图的样子：</p>
<p><img src="https://img-blog.csdnimg.cn/20200326122333474.png" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p>进入Fun函数的时候，变量提升的时候就已经产生了闭包了。因为下图中断点打在<code>a=1</code>上。此时这句还没执行，也就是说还没给a复制，右边已经有闭包了。并且显示<code>a:undefined</code></p>
<p><img src="https://img-blog.csdnimg.cn/20200326122454968.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击执行下一句，就会到<code>return foo</code>，此时a已经赋值了，右边闭包可以看到<code>a:1</code></p>
<p><img src="https://img-blog.csdnimg.cn/20200326122626782.png" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>到这里我们可以知道，在全局中给aa赋值时候，Fun中就产生闭包了</strong>，全局作用于就是Fun的玩不作用域，现在就完成了外部作用域访问函数内部变量而产生闭包了吧。</p>
<h3 data-id="heading-11">综上所述产生闭包的条件</h3>
<ul>
<li>
<p>函数嵌套</p>
</li>
<li>
<p>内部函数引用了外部函数的数据(变量/函数)</p>
</li>
</ul>
<hr>
<h1 data-id="heading-12">闭包的生命周期</h1>
<h3 data-id="heading-13">产生</h3>
<p><strong>产生：在嵌套内部函数定义执行完时就产生了(不是在调用)</strong></p>
<p>经过上面的几个例子我们已经可以知道闭包是什么时候产生的了。</p>
<p><strong>内部函数定义执行完时</strong>有下边几层含义</p>
<ul>
<li>
<p>不需要执行内部函数就可以产生</p>
</li>
<li>
<p>内部函数解析的时候产生</p>
</li>
</ul>
<p> </p>
<p>上边的第一个、第二个、最后一个例子都能看出来，function声明的函数在变量提升的时候解析了，那时候就已经产生了。如果不使用function声明的，用var声明的，那么在给var变量赋值函数的时候，函数解析也会产生闭包。<strong>不需要执行内部函数就可以产生</strong>。</p>
<h3 data-id="heading-14">死亡</h3>
<p><strong>死亡：在嵌套的内部函数成为垃圾对象时</strong></p>
<p>什么叫<strong>内部函数成为垃圾对象时</strong></p>
<ul>
<li>调用内部函数的变量被销毁时。</li>
</ul>
<p> </p>
<p>借用上边最后一个例子继续来看。上边我已经提到了，执行<code>var aa=Fun();</code>的时候已经产生闭包了。那么现在把断点打在下边的<code>aa()</code>上看一下。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326124041942.png" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行<code>aa()</code>就相当于调用了foo函数，点击下一步查看<code>aa()</code>执行的情况。这时候发现右边会显示存在闭包，因为你调用aa，aa引用了Fun的变量。也就是说aa执行的时候闭包是存在的。第一个aa执行完之后闭包依然存在，因为还有第二个aa，虽然我下面没写了，但是你怎么知道实际写程序的时候下边不会继续用到呢。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326124248901.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p>所以只要你赋值之后不管执行不执行，闭包是一直都存在的。如果想让他消失，就要销毁<strong>调用内部函数的变量</strong>，也就是使<code>aa=null</code>，执行之后闭包就消失了。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326124628543.png" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h1 data-id="heading-15">闭包的作用</h1>
<ul>
<li>让函数外部可以操作(读写)到函数内部的数据(变量/函数)</li>
</ul>
<p>这个在<strong>解决问题3</strong>上已经说明了。忘了的上去看。</p>
<ul>
<li>使用函数内部的变量在函数执行完后, 仍然存活在内存中(延长了局部变量的生命周期)</li>
</ul>
<p>这个在<strong>闭包的生命周期 死亡</strong>上边刚解释了。忘了的上去看。</p>
<p> </p>
<h3 data-id="heading-16">问题</h3>
<p>  1. <strong>函数执行完后, 函数内部声明的局部变量是否还存在?</strong></p>
<p>       一般来说是不存在了。但是使用闭包的情况下可以使它继续存在（实例见<strong>闭包的生命周期</strong>）</p>
<p>  2. <strong>在函数外部能直接访问函数内部的局部变量吗?</strong></p>
<p>       一般来说不能，但是可以通过闭包来操作，使内部的变量对外部可见。</p>
<p> </p>
<p> ***</p>
<h1 data-id="heading-17">常见的闭包</h1>
<ul>
<li>将函数作为另一个函数的返回值</li>
</ul>
<p><img src="https://img-blog.csdnimg.cn/20200326125716164.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>将函数作为实参传递给另一个函数调用</li>
</ul>
<p><img src="https://img-blog.csdnimg.cn/20200326130006769.png" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h1 data-id="heading-18">闭包的应用——定义JS模块</h1>
<p><strong>JS模块是什么</strong></p>
<p>  * 具有特定功能的js文件</p>
<p>  * 将所有的数据和功能都封装在一个函数内部(私有的)</p>
<p>  * 只向外暴露一个或n个方法的对象或函数</p>
<p>  * 模块的使用者, 只需要通过模块暴露的对象调用方法来实现对应的功能</p>
<p> </p>
<h3 data-id="heading-19">两种写法</h3>
<h5 data-id="heading-20">使用外部函数返回值</h5>
<p>下图中将内部的两个函数作为返回值，外部声明变量之后即可使用。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326133923926.png" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-21">使用匿名函数自调用</h5>
<p>使用匿名函数自调用向外暴露方法，就可以直接调用不用声明变量了。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326134325115.png" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h1 data-id="heading-22">闭包的缺点和解决方法</h1>
<p>###  缺点</p>
<p>  * 函数执行完后, 函数内的局部变量没有释放, 占用内存时间会变长</p>
<p>  * 容易造成内存泄露</p>
<p> </p>
<p>比如下图中，我创建了一个超大数组。现在外部aa赋值之后产生闭包了。如果我忘了释放，那就会导致占用内存时间边长，并且泄露内存。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326134840172.png" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">解决</h3>
<p>  * 能不用闭包就不用</p>
<p>  * 及时释放</p>
<p>       就是<code>var aa = Fun()</code>使用完之后及时<code>aa=null</code></p>
<p> </p>
<h3 data-id="heading-24">补充</h3>
<p><strong>内存溢出：</strong></p>
<ul>
<li>
<p>一种程序运行出现的错误</p>
</li>
<li>
<p>当程序运行时候需要的内存超过了剩余内存，就抛出内存溢出的错误。</p>
</li>
</ul>
<p> </p>
<p><strong>内存泄漏：</strong></p>
<ul>
<li>占用的内存没有及实释放</li>
</ul>
<p>-  内存泄漏积累多了就会导致内存溢出</p>
<ul>
<li>常见的内存泄漏</li>
</ul>
<p>       - 闭包</p>
<p>       - 意外的全局变量</p>
<p>       - 没有及时清理的计时器或回调函数</p>
<p> </p>
<hr>
<h1 data-id="heading-25">搞几个例题？</h1>
<p><strong>例题1：</strong> 输出什么？</p>
<pre><code class="hljs language-js copyable" lang="js">
                     <span class="hljs-keyword">var</span> name = <span class="hljs-string">"The Window"</span>;

                     <span class="hljs-keyword">var</span> object = &#123;

                            <span class="hljs-attr">name</span>: <span class="hljs-string">"My Object"</span>,

                            <span class="hljs-attr">getNameFunc</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;

                                   <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;

                                          <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;

                                   &#125;;

                                  

                            &#125;

                     &#125;;

                     <span class="hljs-built_in">console</span>.log(object.getNameFunc()());

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://img-blog.csdnimg.cn/20200326140830981.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为你是直接调用getNameFunc的，所以getNameFunc的this指针是指向全局的，<strong>输出The Window</strong></p>
<p> </p>
<p><strong>例题2</strong>：输出什么？</p>
<pre><code class="hljs language-js copyable" lang="js">
                     <span class="hljs-keyword">var</span> name2 = <span class="hljs-string">"The Window"</span>;

                     <span class="hljs-keyword">var</span> object2 = &#123;

                            <span class="hljs-attr">name2</span>: <span class="hljs-string">"My Object"</span>,

                            <span class="hljs-attr">getNameFunc</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;

                                   <span class="hljs-keyword">var</span> that = <span class="hljs-built_in">this</span>;

                                   <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;

                                          <span class="hljs-keyword">return</span> that.name2;

                                   &#125;;

                            &#125;

                     &#125;;

                     <span class="hljs-built_in">console</span>.log(object2.getNameFunc()());

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://img-blog.csdnimg.cn/20200326141334903.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你是直接调用getNameFunc的，所以getNameFunc的this指针是指向全局的。</p>
<p>但是在定义的时候，有个<code>var that = this</code>，定义的时候函数是作为object2的一个方法，所以那时候this指向object2。用that存储了那个时候的this指向。即使之后在全局中调用，this的指向改变了，也不会影响that，所以<strong>输出My Object</strong></p>
<p> </p>
<p><strong>例题3</strong>：输出什么？ （建议不要看，我感觉我解释了你可能也看不懂。只会徒增纠结。当然如果看了不懂可以留言。）</p>
<pre><code class="hljs language-js copyable" lang="js">
                     <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun</span>(<span class="hljs-params">n, o</span>) </span>&#123;

                            <span class="hljs-built_in">console</span>.log(o)

                            <span class="hljs-keyword">return</span> &#123;

                                   <span class="hljs-attr">fun</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">m</span>) </span>&#123;

                                          <span class="hljs-keyword">return</span> fun(m, n)

                                   &#125;

                            &#125;

                     &#125;

                     <span class="hljs-keyword">var</span> a = fun(<span class="hljs-number">0</span>)

                     a.fun(<span class="hljs-number">1</span>)

                     a.fun(<span class="hljs-number">2</span>)

                     a.fun(<span class="hljs-number">3</span>)

                     <span class="hljs-keyword">var</span> b = fun(<span class="hljs-number">0</span>).fun(<span class="hljs-number">1</span>).fun(<span class="hljs-number">2</span>).fun(<span class="hljs-number">3</span>)

                     <span class="hljs-keyword">var</span> c = fun(<span class="hljs-number">0</span>).fun(<span class="hljs-number">1</span>)

                     c.fun(<span class="hljs-number">2</span>)

                     c.fun(<span class="hljs-number">3</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://img-blog.csdnimg.cn/20200326143805570.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://img-blog.csdnimg.cn/20200326145410741.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看一下执行<code>a.fun(1)</code> 的时候，调用栈显示两个fun，也就是确实又回到了function fun(n,x)。这个fun是由于最里边的返回值调用的，所以这时候又产生了新的闭包。然后<code>a.fun(1)</code> 又传入一个1，这时候原来的闭包还存在，那就相当于传入两个参数fun(1,0)。所以<strong>输出0</strong>。执行完毕后，由于全局中并没有一个变量存储<code>a.fun(1)</code> ，因此执行完后刚才新产生的那个闭包就死亡了。但是变量a存储的<code>fun(0)</code>这个闭包还是存在的。因此执行<code>a.fun(2)</code> <code>a.fun(3)</code>的时候同理，新产生的闭包传入新的参数，和原来闭包传入的参数一起。所以都会<strong>输出0</strong> 。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326145505309.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>变量b是生成四层闭包并且保存了下来。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326150432365.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://img-blog.csdnimg.cn/20200326150600894.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到变量c这里就好理解多了，是c存储了两层闭包。剩下的c.fun(2)，c.fun(3)生成的闭包都不会保存下来，因此执行的时候都是在两层闭包的基础上执行的。</p>
<p><img src="https://img-blog.csdnimg.cn/20200326150923692.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以之后执行的都是会将1变为x，仅在执行的时候传入n的新值2或3。</p>
<hr>
<p> </p>
<p>╭(●｀∀´●)╯怎么样看懂了吧！我可真是小机智。</p>
<p>我是萝莉安，还没当程序媛的小机智。</p></div>  
</div>
            