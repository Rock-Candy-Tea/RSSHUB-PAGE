
---
title: '诡异的JS知识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7542'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 05:43:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=7542'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h4 data-id="heading-0">前言</h4>
<p>在日常开发和学习中，我总能遇到一些奇怪的问题，所以记录了下来！</p>
<h4 data-id="heading-1">基本语法和变量</h4>
<h5 data-id="heading-2">连续定义变量</h5>
<p>在日常开发中，我们经常会使用到定义多个变量的场景</p>
<pre><code class="copyable">  var a=b=3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这到了JS解释器眼里就会变成</p>
<pre><code class="copyable">  b=3
  var a=b
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 <code>=</code>运算符是自右向左运算的，所以会先执行<code>b=3</code>，再执行<code>var a=b</code></p>
<p>眨眼看去也没什么错呀，也只是在定义<code>b</code>时未使用<code>var</code>，熟悉全局作用域的人应该知道在JS中未用<code>var</code>、 <code>let</code>、<code>count</code>定义变量，那么变量默认是定义到全局的。</p>
<p>来看看例子:</p>
<pre><code class="copyable">  function test()&#123;
      var a=b=2
      console.log(a)  //2
      console.log(b)  //2
  &#125;
  test()
  console.log(a)  // ReferenceError: a is not defined
  console.log("a" in window)  //false
  
  console.log(b)  // 2
  console.log("b" in window)  //true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>明显看到，b定义到了全局，这样就会造成全局污染了，而且这种错是很难找的。如果要定义多个变量可以<code>,</code>隔开。</p>
<pre><code class="copyable">  var a = 2,b = a;   //正确写法
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这要注意<code>,</code>号运算符是自左向右运算的，先从左边开始定义变量的，先执行<code>var a = 2</code>，再执行<code>var b=a</code>。JS解释器如下：</p>
<pre><code class="copyable">  var a = 2;
  var b = a; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">常见的诡异比较和运算</h5>
<pre><code class="copyable">  null >= 0 //true
  null <= 0 //true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合上面两个表达式，我们可以推出<strong>null==0</strong>,但是放到控制台上面才发现不是这样的结果</p>
<pre><code class="copyable">  null == null  //false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样是比较运算符，为什么推理出来结果不同？</p>
<p>这是因为JS<code>==</code>运算符的隐式转换和<code>>=</code>、<code><=</code>是不一样，所以才会出现后面的效果，所以有的时候不能用数学的方式去思考代码</p>
<pre><code class="copyable">  [] == []  //false
  [] == ![] //false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这样的题在面试中可以说是层出不穷的，因为刁钻而且不容易理解，但是我们正要克服这些（隐式转换的知识点）</p>
<h5 data-id="heading-4">逗号运算符</h5>
<p><code>,</code>运算符是我们最常用的，也是最容易被忽略的，因为不会不会有人把<code>,</code>运算符的语句直接参与运算，比如：</p>
<pre><code class="copyable"> let a = (1,2,3)  // a=3
 (1,2) + (6,2)    // 4
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实也很简单，<strong>逗号表达式</strong>的值就是最后一个逗号后面的值。比如：<code>(1,2)</code>表达式，那么它的值就是2</p>
<p>虽然不常用，但是还是要了解，这种类型的语句一般会出现的压缩源码和面试中</p>
<h5 data-id="heading-5">基本类型的包装类</h5>
<p>什么是包装类我就不讲了，直接看看下面的例子</p>
<pre><code class="copyable"> var str="abc"
 console.log(str.length)  //3
 str.length = 6
 console.log(str.length)  //3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发现了什么，明明修改了<code>str</code>的<code>length</code>属性，再次访问却还是原来的值！！！</p>
<p>我们可以将语句拆开来看，其实JS解释器会进行的是如下操作</p>
<pre><code class="copyable"> var str="abc"
 console.log(new String(str).length)  //3
 new String(str).length = 6
 console.log(new String(str).length)  //3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样是不是就很容易就可以看出问题了喃，因为每次访问<code>length</code>属性都是新定义一个对象，所以你就算修改了对象的<code>length</code>属性，下次访问还是访问的一个新的对象，所以<code>length</code></p>
<h4 data-id="heading-6">函数</h4>
<h5 data-id="heading-7">自执行函数常见考点</h5>
<pre><code class="copyable">  function test()&#123;
      console.log(1)
  &#125;()  //SyntaxError: Unexpected token ')'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面书写自执行函数的方式肯定会报错，这里我也就不解释了（知识点：函数表达式和函数声明的区别）。</p>
<p>那再来看看如下的方式会不会报错喃</p>
<pre><code class="copyable">  function()&#123;
      console.log(1)
  &#125;(1)      //1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到只是添加了一个函数形参，却不会产生报错了。老规矩看看JS解释器如何解释这串代码的吧</p>
<pre><code class="copyable">  function()&#123;
      console.log(1)
  &#125;
  (1)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样是不是就很清晰了呀，因为<code>()</code>运算符的很高，并且里面还有数据，所以就没有把<code>()</code>当作函数执行符号了</p>
<h4 data-id="heading-8">作用域</h4>
<h5 data-id="heading-9">没有块级作用域</h5>
<pre><code class="copyable">   function test()&#123;
       if(true)&#123;
          var a=2
      &#125;
      console.log(a)  //2
   &#125;
  test()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>做过其他语言开发的程序员在初次接触这段代码就很奇怪，为什么可以访问到<code>a变量</code>，<code>if</code>语句块里面定义的变量为什么外面可以访问？</p>
<p>这也算的上JS都有的特性吧，语言本身只存在函数作用域和全局作用域（个人认为全局作用域也可以称为全局匿名函数作用域），故语言本身就没有块级作用域，也就理解为什么<code>if</code>语句块里面定义的变量在外面可以访问喃，因为<code>a变量</code>属于 <code>test函数</code>所产生的函数作用域里面，所以可以在<code>test函数</code>内部任何位置访问。同理<code>for</code>、<code>while</code>等其他语言生成块级作用域的地方，JS都不会生成块级作用域。</p>
<p>在ES6 出来之后就改变这样的规则，但是仅次于是<code>let</code>、 <code>count</code>定义的变量才能产生块级作用域，<code>var</code>定义变量作用域的规则还是照旧。</p>
<p>持续更新中...</p></div>  
</div>
            