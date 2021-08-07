
---
title: '深8️⃣Js从这里开始吧！__函数式编程__'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8225'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 19:04:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=8225'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>函数式编程（Function Programming，FP），FP是编程范式之一，我们常听的编程范式还有面向对象过程编程、面向对象编程。</p>
<ul>
<li>
<p>面向对象编程的思维方式</p>
<blockquote>
<p>把现实世界中的事物抽象成程序世界中的类和对象，通过封装、继承和多态来演示事物事件的联系</p>
</blockquote>
</li>
<li>
<p>函数式编程的思维方式</p>
<blockquote>
<p>把现实世界的事物和事物之间的联系抽象到程序世界（对运算过程进行抽象）</p>
</blockquote>
<ul>
<li>程序的本质：根据输入通过某种运算得到相应的输出，程序开发过程中会涉及很多有输入和输出的函数</li>
<li>函数式编程中的函数指的不是程序中的函数（方法），而是数学中的函数即映射关系，例如：y=sine(x),x和y的关系</li>
<li>相同的输入始终要得到相同的输出（纯函数）</li>
<li>函数式编程用来描述数据（函数）之间的映射</li>
</ul>
</li>
</ul>
<p>优点：</p>
<ul>
<li>可以让代码重用</li>
<li>在函数式的过程中，我们抽象出来的函数都是细粒度的函数，这些函数我们可以组合成功能更强大的函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//非函数式</span>
<span class="hljs-keyword">let</span> num1 = <span class="hljs-number">2</span>
<span class="hljs-keyword">let</span> num2 = <span class="hljs-number">3</span>
<span class="hljs-keyword">let</span> sum = num1 + num2
<span class="hljs-built_in">console</span>.log(sum)
<span class="hljs-comment">//函数式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">num1,num2</span>)</span>&#123;
    <span class="hljs-keyword">return</span> num1 + num2
&#125;
<span class="hljs-keyword">let</span> sum = add(<span class="hljs-number">2</span>,<span class="hljs-number">3</span>)
<span class="hljs-built_in">console</span>.log(sum)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">函数是一等公民 First-class Function</h2>
<ul>
<li>
<p>函数可以存储在变量中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//把函数赋值为变量</span>
<span class="hljs-comment">//函数表达式</span>
<span class="hljs-keyword">let</span> fn = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"hello 函数一等公民"</span>)
&#125;
fn()

<span class="hljs-comment">//一个示例</span>

<span class="hljs-keyword">const</span> BlogController = &#123;
    <span class="hljs-comment">/*
    如果一个函数包裹另一个函数，并且形式也相同时，我们可以认为是一个函数
    是把Views.index赋值给index，是一个函数赋值给index，是方法本身，而不是返回值所以要把方法调用去掉
    */</span>
    index (posts) &#123; <span class="hljs-keyword">return</span> Views.index(posts) &#125;,
    show (posts) &#123; <span class="hljs-keyword">return</span> Views.show(posts) &#125;,
    create (posts) &#123; <span class="hljs-keyword">return</span> Views.create(posts) &#125;,
    update (posts) &#123; <span class="hljs-keyword">return</span> Views.update(posts) &#125;,
    destroy (posts) &#123; <span class="hljs-keyword">return</span> Views.destroy(posts) &#125;,
&#125;

<span class="hljs-comment">//优化</span>
<span class="hljs-comment">//把一个方法赋值给另一个方法或者函数</span>
  <span class="hljs-keyword">const</span> BlogController = &#123;
    <span class="hljs-attr">index</span> : Views.index,
    <span class="hljs-attr">show</span> : Views.show,
    <span class="hljs-attr">create</span> : Views.create,
    <span class="hljs-attr">update</span> : Views.update,
    <span class="hljs-attr">destroy</span> : Views.destroy,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>函数可以作为参数</p>
</li>
<li>
<p>函数可以作为返回值</p>
</li>
</ul>
<p>在javaScript中函数就是一个普通的对象（可以通过new Funciton（）），我们可以把函数存储到变量/数组中，它还可以作为另一个函数的参数和返回值，甚至我们可以在程序运行的时候通过new Function('alert(1)')来构造一个新的函数</p>
<h2 data-id="heading-1">高阶函数 Hight-order Function</h2>
<ul>
<li>可以把函数作为参数传递给另一个函数
函数作为参数可以让函数更为灵活，调用foreach不用考虑内部的实现方式</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//foreach是遍历数组的每一个元素，然后对每一个元素进行处理</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEach</span>(<span class="hljs-params">array, fn</span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < array.length; i++) &#123;
        fn(array[i])
    &#125;
&#125;

<span class="hljs-comment">//测试</span>
<span class="hljs-keyword">let</span> arr =[<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">5</span>,<span class="hljs-number">4</span>,<span class="hljs-number">9</span>]
forEach(arr,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;)

<span class="hljs-comment">//filter过滤数组中满足条件的元素</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">filter</span>(<span class="hljs-params">array, fn</span>) </span>&#123;
    <span class="hljs-keyword">let</span> results = []
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < array.length; i++) &#123;
        <span class="hljs-keyword">if</span> (fn(array[i])) &#123;
            results.push(array[i])
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> results
&#125;
<span class="hljs-comment">//测试</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">4</span>, <span class="hljs-number">9</span>]
<span class="hljs-keyword">let</span> r = filter(arr, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">item</span>) </span>&#123;
    <span class="hljs-keyword">return</span> item % <span class="hljs-number">2</span> === <span class="hljs-number">0</span>
&#125;)
<span class="hljs-built_in">console</span>.log(r)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可以把函数作为另一个函数的返回结果</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeFn</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> msg = <span class="hljs-string">'make funciton'</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(msg)
    &#125;
&#125;
<span class="hljs-comment">// 用来接收makeFn返回的函数</span>
<span class="hljs-keyword">let</span> fn = makeFn()
fn()

<span class="hljs-comment">//第一个（）表示执行makeFn再加一个（）表示执行makeFn返回的函数</span>
makeFn()()

<span class="hljs-comment">//once</span>
<span class="hljs-comment">//支付的时候不管用户点击多少次，函数只执行一次</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">once</span>(<span class="hljs-params">fn</span>) </span>&#123;
    <span class="hljs-comment">//done来记录fn是否被执行</span>
    <span class="hljs-keyword">let</span> done = <span class="hljs-literal">false</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">//fn还未被执行</span>
        <span class="hljs-keyword">if</span> (!done) &#123;
            done = <span class="hljs-literal">true</span>
            <span class="hljs-comment">// 通过apply来调用fn,arguments表示调用当前函数的参数</span>
            <span class="hljs-comment">//apply使用会立即执行，这一点是和bind的区别</span>
            <span class="hljs-keyword">return</span> fn.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>)
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">let</span> pay = once(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">money</span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`支付：<span class="hljs-subst">$&#123;money&#125;</span>RMB`</span>)
&#125;)

pay(<span class="hljs-number">5</span>) <span class="hljs-comment">//支付：5RMB</span>
pay(<span class="hljs-number">5</span>)
pay(<span class="hljs-number">5</span>)
pay(<span class="hljs-number">5</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">使用高阶函数的意义</h3>
<ul>
<li>抽象可以帮我们屏蔽细节，只需要关注我们的目标</li>
<li>高阶函数是用来抽象通用的问题</li>
<li>使代码更简洁</li>
<li>可以使代码更灵活</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//面向过程的方式</span>
<span class="hljs-comment">//需要关注细节</span>
<span class="hljs-keyword">let</span> array =[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>]
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>; i<array.length;i++)&#123;
    <span class="hljs-built_in">console</span>.log(array[i])
&#125;

<span class="hljs-comment">//高阶函数</span>
<span class="hljs-keyword">let</span> array =[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>]
<span class="hljs-comment">//不需要关注循环变量的控制</span>
forEach( array,<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;

<span class="hljs-comment">//过滤数组中的元素，过滤的条件通过传入的条件来决定，不需要关注内部实现的细节，使代码更简洁</span>
<span class="hljs-keyword">let</span> r = filter(array,<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-keyword">return</span> item % <span class="hljs-number">2</span> === <span class="hljs-number">0</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">常用的高阶函数</h3>
<ul>
<li>forEach、filter</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//高阶函数-函数作为参数</span>
<span class="hljs-comment">//foreach是遍历数组的每一个元素，然后对每一个元素进行处理</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEach</span>(<span class="hljs-params">array, fn</span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < array.length; i++) &#123;
        fn(array[i])
    &#125;
&#125;

<span class="hljs-comment">//测试</span>
<span class="hljs-keyword">let</span> arr =[<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">5</span>,<span class="hljs-number">4</span>,<span class="hljs-number">9</span>]
forEach(arr,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(item)
&#125;)

<span class="hljs-comment">//filter过滤数组中满足条件的元素</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">filter</span>(<span class="hljs-params">array, fn</span>) </span>&#123;
    <span class="hljs-keyword">let</span> results = []
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < array.length; i++) &#123;
        <span class="hljs-keyword">if</span> (fn(array[i])) &#123;
            results.push(array[i])
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> results
&#125;
<span class="hljs-comment">//测试</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">4</span>, <span class="hljs-number">9</span>]
<span class="hljs-keyword">let</span> r = filter(arr, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">item</span>) </span>&#123;
    <span class="hljs-keyword">return</span> item % <span class="hljs-number">2</span> === <span class="hljs-number">0</span>
&#125;)
<span class="hljs-built_in">console</span>.log(r)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>map、every、some</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//map array some</span>

<span class="hljs-comment">/*map
是对数组中的每一个元素进行遍历，
并对每一个元素进行处理，并且把结果返回到一个新的数组中
*/</span>
<span class="hljs-keyword">const</span> map = <span class="hljs-function">(<span class="hljs-params">array, fn</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> results = []
    <span class="hljs-comment">// for of是对for的抽象</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> value <span class="hljs-keyword">of</span> array) &#123;
        results.push(fn(value))
    &#125;
    <span class="hljs-keyword">return</span> results
&#125;

<span class="hljs-comment">/*
总结：map函数的参数是一个函数，是一个高阶函数，
可以通过指定函数对数组中的元素进行任意的求值，
函数参数会让我们的map函数更灵活
*/</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">5</span>, <span class="hljs-number">7</span>, <span class="hljs-number">9</span>, <span class="hljs-number">12</span>]
arr = map(arr, <span class="hljs-function"><span class="hljs-params">v</span> =></span> v * v)
<span class="hljs-built_in">console</span>.log(arr)

<span class="hljs-comment">/*every
用来判断数组中的元素是否都匹配我们指定的一个条件
这个条件是灵活的，是变化的
*/</span>
<span class="hljs-keyword">const</span> every = <span class="hljs-function">(<span class="hljs-params">array, fn</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> result = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> value <span class="hljs-keyword">of</span> array) &#123;
        result = fn(value)
        <span class="hljs-keyword">if</span> (!result) &#123;
            <span class="hljs-keyword">break</span>
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> result
&#125;

<span class="hljs-comment">// 测试</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">5</span>, <span class="hljs-number">7</span>, <span class="hljs-number">9</span>, <span class="hljs-number">12</span>]
<span class="hljs-keyword">let</span> result = every(arr, <span class="hljs-function"><span class="hljs-params">v</span> =></span> v > <span class="hljs-number">0</span>)
<span class="hljs-built_in">console</span>.log(result)

<span class="hljs-comment">/*
some 与every类似，来检测我们数组中的元素是否有一个满足我们的条件
*/</span>
<span class="hljs-keyword">const</span> some = <span class="hljs-function">(<span class="hljs-params">array, fn</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> result = <span class="hljs-literal">false</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> value <span class="hljs-keyword">of</span> array) &#123;
        result = fn(value)
        <span class="hljs-keyword">if</span> (result) &#123;
            <span class="hljs-keyword">break</span>
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> result
&#125;

<span class="hljs-comment">// 测试</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">5</span>, <span class="hljs-number">7</span>, <span class="hljs-number">9</span>, <span class="hljs-number">11</span>]
<span class="hljs-keyword">let</span> r = some(arr, <span class="hljs-function"><span class="hljs-params">v</span> =></span> v % <span class="hljs-number">2</span> === <span class="hljs-number">0</span>)
<span class="hljs-built_in">console</span>.log(r)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">数组基础内容</h3>
<h4 data-id="heading-5">数组创建</h4>
<p>使用字面量表示法创建数组不会调用Array构造函数
Es6中新增的用于创建数组的静态方法：from（）和of（）</p>
<ul>
<li>from用于将类数组结构转换为数组实例</li>
<li>of用于将一组参数转换为数组实例</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*Array.from()
用于将类数组结构转换为数组实例
*/</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.from(<span class="hljs-string">'12345'</span>));

<span class="hljs-comment">//对数组进行浅复制</span>
<span class="hljs-keyword">const</span> a1 = [<span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">7</span>]
<span class="hljs-keyword">const</span> a2 = <span class="hljs-built_in">Array</span>.from(a1)
<span class="hljs-built_in">console</span>.log(a2)<span class="hljs-comment">//[1,4,5,7]</span>
<span class="hljs-built_in">console</span>.log(a1 == a2)<span class="hljs-comment">//false</span>

<span class="hljs-comment">//可以使用任务可迭代对象</span>

<span class="hljs-comment">//arguments可以轻松的被转为数组</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getArgsArray</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">arguments</span>)
&#125;
<span class="hljs-built_in">console</span>.log(getArgsArray(<span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>))<span class="hljs-comment">//[ 1, 3, 4, 5 ]</span>

<span class="hljs-comment">//也可用of来实现,用来替换es6之前常用的Array.prototype.slice.call(arguments)这种将参数转为数组的写法</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.of(<span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>))<span class="hljs-comment">//[ 1, 3, 4, 5 ]</span>

<span class="hljs-comment">//from也能转换带有必要属性的自定义对象</span>
<span class="hljs-keyword">const</span> arrayLikeObject = &#123;
    <span class="hljs-number">0</span>: <span class="hljs-number">1</span>,
    <span class="hljs-number">1</span>: <span class="hljs-number">5</span>,
    <span class="hljs-number">2</span>: <span class="hljs-number">7</span>,
    <span class="hljs-number">1</span>: <span class="hljs-number">0</span>,
    <span class="hljs-string">'length'</span>: <span class="hljs-number">6</span>
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.from(arrayLikeObject))
<span class="hljs-comment">/*[ 1, 0, 7, undefined, undefined, undefined ]*/</span>

<span class="hljs-comment">//from()还可以接受第二个可选的映射函数参数，这个函数可以增强新数组的值，还可以接受第三个可选参数，用于指定映射函数中的this，但这个重写的this值在箭头函数中不适应</span>
<span class="hljs-keyword">const</span> b1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>]
<span class="hljs-keyword">const</span> b2 = <span class="hljs-built_in">Array</span>.from(b1, <span class="hljs-function"><span class="hljs-params">x</span> =></span> x ** <span class="hljs-number">2</span>)
<span class="hljs-keyword">const</span> b3 = <span class="hljs-built_in">Array</span>.from(b1, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">x</span>) </span>&#123;
    <span class="hljs-keyword">return</span> x ** <span class="hljs-built_in">this</span>.exponent
&#125;, &#123;
    <span class="hljs-attr">exponent</span>: <span class="hljs-number">2</span>
&#125;)

<span class="hljs-built_in">console</span>.log(b2)<span class="hljs-comment">//[ 1, 4, 16, 25 ]</span>

<span class="hljs-built_in">console</span>.log(b3)<span class="hljs-comment">//[ 1, 4, 16, 25 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">数组空位</h4>
<p>es6与前期版本略有不同，es6新增方法普遍将这些空位当成存在的元素，只不过值为undefined</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> options = [<span class="hljs-number">1</span>,,,,<span class="hljs-number">5</span>]
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> i <span class="hljs-keyword">of</span> options)&#123;
    <span class="hljs-built_in">console</span>.log(option === <span class="hljs-literal">undefined</span> )
&#125;
<span class="hljs-comment">/*'
false
true
true
true
true
false
*/</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>es6之前的方法则会忽略这个空位，但具体方法也会因方法而异</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> options = [<span class="hljs-number">1</span>,,,,<span class="hljs-number">5</span>]
<span class="hljs-comment">//map会跳过这个空位</span>
<span class="hljs-built_in">console</span>.log(options.map(<span class="hljs-function">(<span class="hljs-params">item</span>)=></span><span class="hljs-number">6</span>))<span class="hljs-comment">//[6,,,,6]</span>
<span class="hljs-comment">//join视空位置为空字符串</span>
<span class="hljs-built_in">console</span>.log(options.join(<span class="hljs-string">'-'</span>))<span class="hljs-comment">//"1----5"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>由于行为不一致和存在性能隐患，因此实践中要避免使用数组空位，若确实需要，则可以显示的用undefined代替</p>
</blockquote>
<h4 data-id="heading-7">数组索引</h4>
<p>length属性不是只读的，通过修改可以从数组末尾删除或者添加元素</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> colors = [<span class="hljs-string">'red'</span>,<span class="hljs-string">'blue'</span>,<span class="hljs-string">'green'</span>]
colors.length = <span class="hljs-number">2</span>
<span class="hljs-built_in">console</span>.log(colors[<span class="hljs-number">2</span>])<span class="hljs-comment">//undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数组最多可以包含4 294 967 295个元素 约43亿</p>
<h4 data-id="heading-8">数组检测</h4>
<p>只有一个全局作用域的情况下使用instanceof操作符足以检测一个对象是不是数组，</p>
<p>不确定在哪个全局上下文中创建时可以使用Array.isArray()</p>
<h4 data-id="heading-9">数组迭代器方法</h4>
<p>Array数组原型暴露了3个用于检索数组内容的方法</p>
<ul>
<li>keys()</li>
<li>values()</li>
<li>entries()</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr1 = [<span class="hljs-string">'foo'</span>,<span class="hljs-string">'bar'</span>,<span class="hljs-string">'baz'</span>,<span class="hljs-string">'qux'</span>]
<span class="hljs-comment">/*
这些方法都返回迭代器，可以将他们的内容通过Arrayf.from()直接转化为数组实例
*/</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.from(arr1.keys()))<span class="hljs-comment">//[0, 1, 2, 3]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.from(arr1.values()))<span class="hljs-comment">//['foo','bar','baz','qux']</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.from(arr1.entries()))<span class="hljs-comment">//[[0,'foo'],[1,'bar'],[2,'baz'],[3,'qux']]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">闭包</h2>
<p>可以在另一个作用域中调用一个函数的内部函数并访问到该函数的作用域中的成员</p>
<p>核心作用：延长了外部函数的内部变量的作用范围</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//函数作为返回值</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makefn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> msg = <span class="hljs-string">`hello funciton`</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(msg)
    &#125;
&#125;
<span class="hljs-comment">/*

*/</span>
<span class="hljs-keyword">const</span> fn = makefn()
fn()


<span class="hljs-comment">/*
once
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">once</span>(<span class="hljs-params">fn</span>)</span>&#123;
    <span class="hljs-keyword">let</span> done =<span class="hljs-literal">false</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-title">funciton</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">if</span>(!done)&#123;
            done=<span class="hljs-literal">true</span>
            <span class="hljs-keyword">return</span> fn.apply(<span class="hljs-built_in">this</span>,<span class="hljs-built_in">arguments</span>)
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">let</span> pay = <span class="hljs-function"><span class="hljs-title">once</span>(<span class="hljs-params">funciton (money)</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`支付:<span class="hljs-subst">$&#123;money&#125;</span>RMB`</span>)&#125;

<span class="hljs-comment">//只会支付一次</span>
pay(<span class="hljs-number">5</span>)
pay(<span class="hljs-number">5</span>)
pay(<span class="hljs-number">5</span>)
pay(<span class="hljs-number">5</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>闭包的本质：函数执行的时候会放到一个执行栈上，当函数执行完毕之后会从执行栈上移除，但是堆上的作用域成员因为被外部引用不能被释放，因此内部函数依然可以访问外部函数的成员</p>
<h3 data-id="heading-11">纯函数</h3>
<p>相同的输入始终会得到相同的输出，没有任何可观察的副作用</p>
<ul>
<li>纯函数就是类似数学中的函数（用来描述输入和输出之间的关系），y=f(x)</li>
<li>lodash是一个纯函数的功能库，提供了对数组、数字、对象、字符串、函数等操作的一些方法</li>
<li>数组的slice和splice分别是：纯函数和不纯的函数
<ul>
<li>slice返回数组中的指定部分，不会改变原数组</li>
<li>splice对数组进行操作返回该数组，会改变原数组（包括删除、修改）</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//纯函数和不纯函数</span>

<span class="hljs-keyword">let</span> array = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">5</span>, <span class="hljs-number">8</span>, <span class="hljs-number">0</span>]

<span class="hljs-comment">//纯函数是指相同的输入始终有相同的输出</span>
<span class="hljs-built_in">console</span>.log(array.slice(<span class="hljs-number">0</span>, <span class="hljs-number">3</span>))
<span class="hljs-built_in">console</span>.log(array.slice(<span class="hljs-number">0</span>, <span class="hljs-number">3</span>))
<span class="hljs-built_in">console</span>.log(array.slice(<span class="hljs-number">0</span>, <span class="hljs-number">3</span>))
<span class="hljs-comment">//[1,2,5]</span>

<span class="hljs-comment">//splice是不纯的函数</span>
<span class="hljs-built_in">console</span>.log(array.splice(<span class="hljs-number">0</span>, <span class="hljs-number">3</span>))
<span class="hljs-built_in">console</span>.log(array.splice(<span class="hljs-number">0</span>, <span class="hljs-number">3</span>))
<span class="hljs-built_in">console</span>.log(array.splice(<span class="hljs-number">0</span>, <span class="hljs-number">3</span>))
<span class="hljs-comment">//[1,2,5] [8,0] []</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>函数式编程不会保留计算中间的结果，所以变量是不可变的（无状态的）</li>
<li>我们可以把一个函数的执行结果交给另一个函数去处理</li>
</ul>
<h3 data-id="heading-12">loadsh纯函数库</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//演示lodash</span>
<span class="hljs-comment">// first last toUpper reverse each </span>
<span class="hljs-comment">// es6中新的属性includes find findIndex</span>
<span class="hljs-keyword">const</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash'</span>)
<span class="hljs-keyword">const</span> array = [<span class="hljs-string">'jack'</span>, <span class="hljs-string">'tom'</span>, <span class="hljs-string">'lucy'</span>, <span class="hljs-string">'kate'</span>]
<span class="hljs-built_in">console</span>.log(_.first(array))
<span class="hljs-built_in">console</span>.log(_.last(array))

<span class="hljs-built_in">console</span>.log(_.toUpper(_.first(array)))

<span class="hljs-comment">//数组的reverse没有参数，不是一个纯函数</span>
<span class="hljs-built_in">console</span>.log(array.reverse(), <span class="hljs-string">'array.reverse'</span>)

<span class="hljs-built_in">console</span>.log(_.reverse(array))

<span class="hljs-comment">// each是forEach的别名</span>
<span class="hljs-keyword">const</span> r = _.each(array, <span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(item, index)
&#125;)
<span class="hljs-built_in">console</span>.log(r)

<span class="hljs-built_in">console</span>.log(array.includes(<span class="hljs-number">1</span>), <span class="hljs-string">'array.includes(1)'</span>)
<span class="hljs-built_in">console</span>.log(array.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.length > <span class="hljs-number">3</span>), <span class="hljs-string">'array.find(1)'</span>)
<span class="hljs-built_in">console</span>.log(array.findIndex(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.length > <span class="hljs-number">3</span>), <span class="hljs-string">'array.findIndex(1)'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的练习主要涉及了数组的搜索和位置方法
ECMAScript提供了两类搜索数组的方法：按严格相等搜索和按断言函数搜索</p>
<h4 data-id="heading-13">严格相等</h4>
<ul>
<li>indexOf()</li>
<li>lastIndexOf()</li>
<li>includes() 为es7中新增的</li>
</ul>
<p>这些方法都接收两个参数：要查找的元素和一个可选的起始搜索位置，lastIndexOf第二个参数表示最后一个元素的位置</p>
<blockquote>
<p>indexOf和incudes方法是从前往后搜索,lastIndexOf是从数组末尾开始向前搜索,但是lastIndexOf返回的位置与indexOf一致
indexof和indexLastOf都返回要查找的元素在数组中的位置，如果没有则返回-1
includes返回布尔值，表示是否找到一个与指定元素匹配的项</p>
</blockquote>
<p>在比较第一个参数跟数组每一个项时，会使用===比较，也就是说两项必须严格相等</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> num = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">4</span>, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">6</span>]

<span class="hljs-built_in">console</span>.log(num.indexOf(<span class="hljs-number">4</span>))<span class="hljs-comment">//3</span>
<span class="hljs-built_in">console</span>.log(num.lastIndexOf(<span class="hljs-number">6</span>))<span class="hljs-comment">//9</span>
<span class="hljs-built_in">console</span>.log(num.includes(<span class="hljs-number">4</span>))<span class="hljs-comment">//true</span>

<span class="hljs-built_in">console</span>.log(num.indexOf(<span class="hljs-number">3</span>,<span class="hljs-number">2</span>))<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(num.lastIndexOf(<span class="hljs-number">3</span>,<span class="hljs-number">4</span>))<span class="hljs-comment">//true</span>

<span class="hljs-keyword">let</span> person = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'nike'</span> &#125;
<span class="hljs-keyword">let</span> people = [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'nike'</span> &#125;]
<span class="hljs-keyword">let</span> morePeople = [person]

<span class="hljs-built_in">console</span>.log(people.indexOf(person))
<span class="hljs-built_in">console</span>.log(morePeople.indexOf(person))
<span class="hljs-built_in">console</span>.log(people.includes(person))
<span class="hljs-built_in">console</span>.log(morePeople.includes(person))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">断言函数</h4>
<p>断言函数接收三个参数：元素、索引和数组本身
find()和fineIndex()都从数组的最小索引开始，find返回第一个匹配的元素，findIndex返回第一个匹配元素的索引，都可接收第二个可选参数，用于指定内部this的值，找到匹配项后，这两个方法都不再继续思索。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//断言函数</span>
<span class="hljs-keyword">const</span> people = [
    &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Matt'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">28</span>
    &#125;, &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'nike'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">30</span>
    &#125;
]
<span class="hljs-comment">//find返回第一个匹配的元素，findIndex返回第一个匹配元素的索引</span>
<span class="hljs-built_in">console</span>.log(people.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.age > <span class="hljs-number">28</span>))
<span class="hljs-built_in">console</span>.log(people.findIndex(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.age > <span class="hljs-number">28</span>))

<span class="hljs-comment">//找到匹配项后，这两个方法都不再继续搜索。</span>
<span class="hljs-keyword">let</span> nums = [<span class="hljs-number">3</span>, <span class="hljs-number">6</span>, <span class="hljs-number">9</span>]
nums.find(<span class="hljs-function">(<span class="hljs-params">item, index, array</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(item)
    <span class="hljs-built_in">console</span>.log(index)
    <span class="hljs-built_in">console</span>.log(array)
    <span class="hljs-keyword">return</span> item > <span class="hljs-number">1</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">纯函数的好处</h3>
<ul>
<li>可缓存
<ul>
<li>因为纯函数对相同的输入始终有相同的结果，所以可以把纯函数的结果缓存起来,主要是用来提高性能</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//记忆函数</span>

<span class="hljs-keyword">const</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash'</span>)
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getArea</span>(<span class="hljs-params">r</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(r)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * r * r
&#125;
<span class="hljs-comment">// 会返回一个带有记忆功能的函数</span>
<span class="hljs-comment">// let getAreaWithMemory = _.memoize(getArea)</span>
<span class="hljs-comment">// console.log(getAreaWithMemory(4))</span>
<span class="hljs-comment">// console.log(getAreaWithMemory(4))</span>
<span class="hljs-comment">// console.log(getAreaWithMemory(4))</span>
<span class="hljs-comment">// console.log(getAreaWithMemory(4))</span>

<span class="hljs-comment">//模拟memoize实现</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">memoize</span>(<span class="hljs-params">fn</span>) </span>&#123;
    <span class="hljs-keyword">let</span> cache = &#123;&#125;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> key = <span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-built_in">arguments</span>)
        cache[key] = cache[key] || fn.apply(fn, <span class="hljs-built_in">arguments</span>)
        <span class="hljs-keyword">return</span> cache[key]
    &#125;
&#125;

<span class="hljs-keyword">let</span> getAreaWithMemory = memoize(getArea)
<span class="hljs-built_in">console</span>.log(getAreaWithMemory(<span class="hljs-number">4</span>))
<span class="hljs-built_in">console</span>.log(getAreaWithMemory(<span class="hljs-number">4</span>))
<span class="hljs-built_in">console</span>.log(getAreaWithMemory(<span class="hljs-number">4</span>))
<span class="hljs-built_in">console</span>.log(getAreaWithMemory(<span class="hljs-number">4</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可测试
纯函数让测试更方便</li>
<li>并行处理
<ul>
<li>在多线程环境下并行操作共享的内存数据很可能会出现意外情况</li>
<li>纯函数不需要访问共享的内存数据，所以在并行环境下可以任务运行纯函数（es6以后新增的web Worker，可以开启多个线程）</li>
</ul>
</li>
</ul>
<h3 data-id="heading-16">副作用</h3>
<p>纯函数：对于相同的输入永远会得到相同的输出，而且没有任何可观察的副作用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//不纯函数</span>
<span class="hljs-comment">//函数依赖于外部的状态就无法保证输出相同</span>
<span class="hljs-keyword">let</span> mini = <span class="hljs-number">18</span> <span class="hljs-comment">//带来了副作用</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkAge</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> age >= mini
&#125;

<span class="hljs-comment">//纯函数（有硬编码，后续可以通过柯里化解决）</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkAge</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> mini = <span class="hljs-number">18</span><span class="hljs-comment">//是一个具体的数字，硬编码，要尽量避免</span>
    <span class="hljs-keyword">return</span> age > = mini
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>副作用让一个函数变的不纯（如上例），纯函数根据相同的输入返回相同的输出，如果函数依赖于外部的状态就无法保证输出相同，就会带来副作用.</p>
<p>副作用来源：</p>
<ul>
<li>全局变量</li>
<li>配置文件</li>
<li>数据库</li>
<li>获取用户的输入</li>
<li>......</li>
</ul>
<p>所有的外部的交互都有可能产生副作用，副作用也使得方法通用性下降不适合扩展和可重用性，同时副作用会给程序中带来安全隐患（例如我们获取用户输入时可能会带来跨站脚本攻击），给程序带来不确定性，但是副作用不可能完全禁止，尽可能控制他们在可控范围内发生。</p>
<h3 data-id="heading-17">柯里化（Haskell Brooks Curry）</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//函数的柯里化</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkAgeB</span>(<span class="hljs-params">min</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">age</span>) </span>&#123;
        <span class="hljs-keyword">return</span> age >= min
    &#125;
&#125;
<span class="hljs-comment">//es6箭头函数</span>
<span class="hljs-keyword">let</span> checkAgeB = <span class="hljs-function"><span class="hljs-params">min</span> =></span> (<span class="hljs-function"><span class="hljs-params">age</span> =></span> age >= min)

<span class="hljs-keyword">let</span> checkAgeB18 = checkAgeB(<span class="hljs-number">18</span>)
<span class="hljs-keyword">let</span> checkAgeB20 = checkAgeB(<span class="hljs-number">20</span>)

<span class="hljs-built_in">console</span>.log(checkAgeB18(<span class="hljs-number">25</span>))
<span class="hljs-built_in">console</span>.log(checkAgeB18(<span class="hljs-number">20</span>))
<span class="hljs-built_in">console</span>.log(checkAgeB20(<span class="hljs-number">20</span>))
<span class="hljs-built_in">console</span>.log(checkAgeB20(<span class="hljs-number">24</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>柯里化：</p>
<ul>
<li>当一个函数有多个参数的时候先传递一部分参数调用它（这部分参数以后永远不变）</li>
<li>然后返回一个新的函数接收剩余的参数，返回结果</li>
</ul>
<h4 data-id="heading-18">lodash中的柯里化</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//lodash中的curry基本使用</span>
<span class="hljs-keyword">const</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash'</span>)

<span class="hljs-comment">//柯里化可以帮我们把任意多元函数转为一元函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSum</span>(<span class="hljs-params">a, b, c</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b + c
&#125;

<span class="hljs-keyword">const</span> curried = _.curry(getSum)
<span class="hljs-comment">//如果传入了getSum所需要的所有参数，则会被立即调用并返回结果</span>
<span class="hljs-built_in">console</span>.log(curried(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>))
<span class="hljs-comment">//如果传入参数为部分参数,它会返回一个函数，并且等待接收其他的参数</span>
<span class="hljs-built_in">console</span>.log(curried(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>,<span class="hljs-number">3</span>))
<span class="hljs-built_in">console</span>.log(curried(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">柯里化案例</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//柯里化案例</span>
<span class="hljs-keyword">const</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash'</span>)
<span class="hljs-comment">//匹配字符串中的所有字符</span>
<span class="hljs-comment">// ''.match(/\s+/g)</span>
<span class="hljs-comment">//匹配字符串中的所有数字</span>
<span class="hljs-comment">// ''.match(/\d+/g)</span>

<span class="hljs-comment">//函数式编程可以最大程度的重用函数</span>
<span class="hljs-comment">// function match(reg,str)&#123;</span>
<span class="hljs-comment">//   return str.match(reg)</span>
<span class="hljs-comment">// &#125;</span>

<span class="hljs-comment">//match柯里化处理</span>
<span class="hljs-keyword">let</span> match = _.curry(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">reg, str</span>) </span>&#123;
  <span class="hljs-keyword">return</span> str.match(reg)
&#125;)


<span class="hljs-keyword">const</span> haveSpace = match(<span class="hljs-regexp">/\s+/g</span>)
<span class="hljs-keyword">const</span> haveNum = match(<span class="hljs-regexp">/\d+/g</span>)

<span class="hljs-built_in">console</span>.log(haveSpace(<span class="hljs-string">'Hello Sine ya'</span>))
<span class="hljs-built_in">console</span>.log(haveNum(<span class="hljs-string">'Hello2 Sine4 ya1'</span>))

<span class="hljs-comment">//寻找数组中所有含有空格的字符串</span>
<span class="hljs-keyword">const</span> filter = _.curry(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn, arr</span>) </span>&#123;
  <span class="hljs-keyword">return</span> arr.filter(fn)
&#125;)
<span class="hljs-keyword">const</span> filter = _.curry(<span class="hljs-function">(<span class="hljs-params">fn, arr</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> arr.filter(fn)
&#125;)

<span class="hljs-keyword">const</span> findSpace = filter(haveSpace)

<span class="hljs-built_in">console</span>.log(filter(haveSpace, [<span class="hljs-string">'qw e'</span>, <span class="hljs-string">'rf p'</span>, <span class="hljs-string">'ert'</span>]))


<span class="hljs-built_in">console</span>.log(findSpace([<span class="hljs-string">'oi p'</span>, <span class="hljs-string">'ioj'</span>]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">柯里化的实现</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//模拟实现lodash中的curry方法</span>
<span class="hljs-keyword">const</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash'</span>)
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSum</span>(<span class="hljs-params">a,b,c</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b + c
&#125;

<span class="hljs-comment">/*
调用_.curry时我们要传入一个纯函数
返回一个柯里化后的函数
*/</span>
<span class="hljs-comment">// const curied = _.curry(getSum)</span>
<span class="hljs-keyword">const</span> curied = curry(getSum)

<span class="hljs-built_in">console</span>.log(curied(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>))
<span class="hljs-built_in">console</span>.log(curied(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>))
<span class="hljs-built_in">console</span>.log(curied(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>))

<span class="hljs-comment">//需要一个经过柯里化处理的函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curry</span>(<span class="hljs-params">fn</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curriedFn</span>(<span class="hljs-params">...args</span>)</span>&#123;
    <span class="hljs-comment">//第一种情况就是这个柯里化函数需要几个函数我们就传入几个函数</span>
    <span class="hljs-comment">//第二种，调用curry函数时只传入部分参数，返回一个等待接收其他参数的函数</span>
    <span class="hljs-comment">//我们要获取一下形参的个数是否与fn实参的个数</span>
    <span class="hljs-keyword">if</span>(args.length<fn.length)&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// arguments是伪数组所以要用Array.from进行处理</span>
        <span class="hljs-keyword">return</span> curriedFn(...args.concat(<span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">arguments</span>)))
      &#125;
    &#125;<span class="hljs-keyword">else</span>&#123;
      <span class="hljs-keyword">return</span> fn(...args)
    &#125;

  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">柯里化总结</h4>
<ul>
<li>柯里化可以让我们给一个函数传递较少的参数得到一个已经记住了某些固定参数的新函数</li>
<li>这是一种对函数参数的缓存</li>
<li>让函数变的更灵活，让函数的粒度更小</li>
<li>可以把多元函数转换成一元函数，可以组合使用函数产生从强大的功能</li>
</ul>
<h3 data-id="heading-22">函数的组合Compose</h3>
<ul>
<li>
<p>纯函数和柯里化很容易写出洋葱代码h(g(f(x)))</p>
<ul>
<li>获取数组的最后一个元素再转换成大写字母_.toUpper(<em>.first(</em>.reverse(arr)))</li>
<li>函数组合可以让我们把细粒度的函数重新组合成一个新的函数</li>
</ul>
</li>
<li>
<p>如果一个函数要经过多个函数处理才能得到最终值，这个时候可以把中间过程的函数合并成一个函数</p>
<ul>
<li>函数就像是数据的管道，函数组合就是把这些管道连接起来，让数据穿过多个管道形成最终结果</li>
<li>函数组合默认是从右到左执行</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//函数组合演示</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compose</span>(<span class="hljs-params">f,g</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>)</span>&#123;
        <span class="hljs-keyword">return</span> f(g(value))
    &#125;
&#125;
<span class="hljs-comment">//翻转</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reverse</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">return</span> arr.reverse()
&#125;
<span class="hljs-comment">//数组的第一个元素</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">first</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">return</span> arr[<span class="hljs-number">0</span>]
&#125;

<span class="hljs-keyword">const</span> last = compose(first,reverse)

<span class="hljs-built_in">console</span>.log(last([<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">lodash组合函数</h4>
<p>-flow（）从左到右执行
-flowRight() 从右到左执行，过程中用的比较多</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//lodash中的组合函数 _.flowRight</span>
<span class="hljs-keyword">const</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash'</span>)

<span class="hljs-keyword">const</span> reverse = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> arr.reverse()
<span class="hljs-keyword">const</span> first = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> arr[<span class="hljs-number">0</span>]
<span class="hljs-keyword">const</span> toUpper = <span class="hljs-function"><span class="hljs-params">s</span> =></span> s.toUpperCase()

<span class="hljs-keyword">const</span> f = _.flowRight(toUpper,first,reverse)
<span class="hljs-built_in">console</span>.log(f([<span class="hljs-string">'we'</span>,<span class="hljs-string">'rt4t'</span>,<span class="hljs-string">'rer'</span>]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">模拟lodash的flowRight</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//lodash中的组合函数 _.flowRight</span>
<span class="hljs-keyword">const</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash'</span>)
<span class="hljs-keyword">const</span> &#123; CodeNode &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'source-list-map'</span>)

<span class="hljs-keyword">const</span> reverse = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> arr.reverse()
<span class="hljs-keyword">const</span> first = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> arr[<span class="hljs-number">0</span>]
<span class="hljs-keyword">const</span> toUpper = <span class="hljs-function"><span class="hljs-params">s</span> =></span> s.toUpperCase()

<span class="hljs-comment">// const f = _.flowRight(toUpper,first,reverse)</span>


<span class="hljs-comment">// function compose(...args)&#123;</span>
<span class="hljs-comment">//     return function(value)&#123;</span>
<span class="hljs-comment">//         //对数组中的每一个元素去执行我们提供的一个函数，并将其汇总成一个单个的结果</span>
            <span class="hljs-comment">//acc 表示上一次的执行结果，fn表示当前管道</span>
<span class="hljs-comment">//         return args.reverse().reduce(function(acc,fn)&#123;</span>
<span class="hljs-comment">//             return fn(acc)</span>
<span class="hljs-comment">//         &#125;,value)</span>
<span class="hljs-comment">//     &#125;</span>
<span class="hljs-comment">// &#125;</span>

<span class="hljs-keyword">const</span> compose = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> <span class="hljs-function"><span class="hljs-params">value</span> =></span> args.reverse().reduce(<span class="hljs-function">(<span class="hljs-params">acc, fn</span>) =></span> fn(acc), value)
<span class="hljs-keyword">const</span> f = compose(toUpper, first, reverse)
<span class="hljs-built_in">console</span>.log(f([<span class="hljs-string">'we'</span>, <span class="hljs-string">'rt4t'</span>, <span class="hljs-string">'rer'</span>]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">函数的组合要满足结合律（associaltivity）</h4>
<ul>
<li>我们既可以把g和h组合，还可以把f和g组合，结果都是一样的</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> f = compose(f,g,h)
<span class="hljs-keyword">let</span> associaltive = compose(compose(f,g),h) == compose(f,compose(g,h))
<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//函数组合要满足结合律</span>
<span class="hljs-keyword">const</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash'</span>)
<span class="hljs-comment">// const f = _.flowRight(_.toUpper,_.first,_.reverse)</span>
<span class="hljs-comment">// const f = _.flowRight(_.flowRight(_.toUpper,_.first),_.reverse)</span>
<span class="hljs-keyword">const</span> f = _.flowRight(_.toUpper,_.flowRight(_.first,_.reverse))

<span class="hljs-built_in">console</span>.log(f([<span class="hljs-string">'we'</span>, <span class="hljs-string">'rt4t'</span>, <span class="hljs-string">'rer'</span>]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">如何调试组合函数</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> f = _.flowRight(_.toUpper,_.first,_.reverse)
<span class="hljs-comment">//函数组合调试</span>
<span class="hljs-comment">//NEVER SAY DIE --> never-say-die</span>

<span class="hljs-keyword">const</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash'</span>)

<span class="hljs-comment">// const log=(c)=>&#123;</span>
<span class="hljs-comment">//     console.log(c)</span>
<span class="hljs-comment">//     return c</span>
<span class="hljs-comment">// &#125;</span>
<span class="hljs-keyword">const</span> trace = _.curry(<span class="hljs-function">(<span class="hljs-params">tag, v</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(tag, v)
    <span class="hljs-keyword">return</span> v
&#125;)

<span class="hljs-comment">//_.split</span>
<span class="hljs-keyword">const</span> split = _.curry(<span class="hljs-function">(<span class="hljs-params">sep, str</span>) =></span> _.split(str, sep))
<span class="hljs-comment">//_.toLower</span>
<span class="hljs-keyword">const</span> map = _.curry(<span class="hljs-function">(<span class="hljs-params">fn, arr</span>) =></span> _.map(arr, fn))
<span class="hljs-comment">//_.join</span>
<span class="hljs-keyword">const</span> join = _.curry(<span class="hljs-function">(<span class="hljs-params">seq, arr</span>) =></span> _.join(arr, seq))

<span class="hljs-keyword">const</span> result = _.flowRight(join(<span class="hljs-string">'-'</span>),trace(<span class="hljs-string">'map之后打印'</span>), map(_.toLower),trace(<span class="hljs-string">'split之后打印'</span>), split(<span class="hljs-string">' '</span>))
<span class="hljs-built_in">console</span>.log(result(<span class="hljs-string">'NEVER SAY DIE'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">losash中的FP模块</h4>
<ul>
<li>lodash的fp模块提供了使用的对函数式编程友好的方法</li>
<li>提供了不可变auto-curried iteratee-first data-last的方法(是已经被柯里化的，如果是函数的话会要求函数优先，并且数据滞后)</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//lodash 模块</span>
<span class="hljs-comment">//数据优先，函数滞后</span>
_.map([<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>],_.toUpper)
<span class="hljs-comment">//=>["A","B","C"]</span>
_.map([<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>])
<span class="hljs-comment">//['a','b','c']</span>

_.split(<span class="hljs-string">"Hello World"</span>,<span class="hljs-string">' '</span>)

<span class="hljs-comment">//lodash/fp 模块</span>
<span class="hljs-comment">//函数优先数据滞后</span>
<span class="hljs-keyword">const</span> fp = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash/fp'</span>)
fp.map(fp.toUpper,[<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>])
fp.map(fp.toUpper)([<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>])

fp.split(<span class="hljs-string">' '</span>,<span class="hljs-string">"Hello World"</span>)
fp.split(<span class="hljs-string">' '</span>)(<span class="hljs-string">"Hello World"</span>)

<span class="hljs-comment">// NEVER SAY DIE  --> never-say-die</span>
<span class="hljs-keyword">const</span> fp = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash/fp'</span>)

<span class="hljs-keyword">let</span> f = fp.flowRight(fp.join(<span class="hljs-string">'-'</span>),fp.map(fp.toLower),fp.split(<span class="hljs-string">' '</span>))
<span class="hljs-built_in">console</span>.log(f(<span class="hljs-string">'NEVER SAY DIE'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">point Free 函数编码的风格</h3>
<p>我们可以把数据处理的过程定义成与数据无关的合成运算，不需要用到代表数据的那个参数，只要把简单的运算步骤合成到一起，在使用这种模式之前我们需要定义一些辅助的基本运算函数</p>
<ul>
<li>不需要指明处理的数据</li>
<li>只需要合成运算过程</li>
<li>需要定义一些辅助的基本运算函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// point free</span>
<span class="hljs-comment">// Hello     World => hello_world</span>
<span class="hljs-keyword">const</span> fp = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash/fp'</span>)

<span class="hljs-keyword">const</span> pf = fp.flowRight(fp.replace(<span class="hljs-regexp">/\s+/g</span>,<span class="hljs-string">"_"</span>),fp.toLower)
<span class="hljs-built_in">console</span>.log(pf(<span class="hljs-string">"Hello     World"</span>))
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            