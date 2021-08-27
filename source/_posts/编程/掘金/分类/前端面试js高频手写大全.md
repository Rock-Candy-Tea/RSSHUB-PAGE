
---
title: '前端面试js高频手写大全'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17b56147ef2244cb9211d5fc87fbd795~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 19:41:47 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17b56147ef2244cb9211d5fc87fbd795~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">介绍</h2>
<p>在前端面试中，手撕代码显然是不可避免的，并且占很大的一部分比重。</p>
<p>一般来说，如果代码写的好，即使理论知识答得不够清楚，也能有大概率通过面试。并且其实很多手写往往背后就考察了你对相关理论的认识。</p>
<p>编程题主要分为这几种类型:</p>
<pre><code class="copyable">* 算法题
* 涉及js原理的题以及ajax请求
* 业务场景题: 实现一个具有某种功能的组件
* 其他(进阶，对计算机综合知识的考察，考的相对较少)：实现订阅发布者模式；分别用面向对象编程，面向过程编程，函数式编程实现把大象放进冰箱等等
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中前两种类型所占比重最大。
算法题建议养成每天刷一道leetcode的习惯，重点刷数据结构(栈，链表，队列，树)，动态规划，DFS，BFS</p>
<p>本文主要涵盖了第二种类型的各种重点手写。</p>
<p><strong>建议优先掌握</strong>：</p>
<ul>
<li>instanceof (考察对原型链的理解)</li>
<li>new (对创建对象实例过程的理解)</li>
<li>call&apply&bind (对this指向的理解)</li>
<li>手写promise (对异步的理解)</li>
<li>手写原生ajax (对ajax原理和http请求方式的理解，重点是get和post请求的实现)</li>
<li>事件订阅发布 (高频考点)</li>
<li>其他：数组，字符串的api的实现，难度相对较低。只要了解数组，字符串的常用方法的用法，现场就能写出来个大概。(ps：笔者认为数组的reduce方法比较难，这块有余力可以单独看一些，即使面试没让你实现reduce，写其他题时用上它也是很加分的)</li>
</ul>
<hr>
<p>话不多说，直接开始</p>
<h2 data-id="heading-1">1. 手写instanceof</h2>
<p>instanceof作用:</p>
<p><strong>判断一个实例是否是其父类或者祖先类型的实例。</strong></p>
<p><strong>instanceof</strong> <strong>在查找的过程中会遍历左边变量的原型链，直到找到右边变量的 prototype</strong>查找失败，返回 false</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> myInstanceof = <span class="hljs-function">(<span class="hljs-params">target,origin</span>) =></span> &#123;
     <span class="hljs-keyword">while</span>(target) &#123;
         <span class="hljs-keyword">if</span>(target.__proto__===origin.prototype) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
         &#125;
         target = target.__proto__
     &#125;
     <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
 &#125;
 <span class="hljs-keyword">let</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]
 <span class="hljs-built_in">console</span>.log(myInstanceof(a,<span class="hljs-built_in">Array</span>));  <span class="hljs-comment">// true</span>
 <span class="hljs-built_in">console</span>.log(myInstanceof(a,<span class="hljs-built_in">Object</span>));  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">2. 实现数组的map方法</h2>
<p>数组的<strong>map()</strong> 方法会返回一个新的数组，这个新数组中的每个元素对应原数组中的对应位置元素调用一次提供的函数后的返回值。</p>
<p><strong>用法：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">const</span> b = array1.map(<span class="hljs-function"><span class="hljs-params">x</span> =></span> x * <span class="hljs-number">2</span>);
<span class="hljs-built_in">console</span>.log(b);   <span class="hljs-comment">// Array [2, 4, 6, 8]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现前，我们先看一下map方法的参数有哪些</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17b56147ef2244cb9211d5fc87fbd795~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
map方法有两个参数，一个是操作数组元素的方法fn，一个是this指向(可选)，其中使用fn时可以获取三个参数，实现时记得不要漏掉，这样才算完整实现嘛</p>
<p><strong>原生实现：</strong></p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 实现</span>
     <span class="hljs-built_in">Array</span>.prototype.myMap = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn, thisValue</span>) </span>&#123;
            <span class="hljs-keyword">let</span> res = []
            thisValue = thisValue||[]
            <span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">this</span>
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>; i<arr.length; i++) &#123;
                res.push(fn.call(thisValue, arr[i],i,arr))   <span class="hljs-comment">// 参数分别为this指向，当前数组项，当前索引，当前数组</span>
            &#125;
            <span class="hljs-keyword">return</span> res
        &#125;
        <span class="hljs-comment">// 使用</span>
        <span class="hljs-keyword">const</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
        <span class="hljs-keyword">const</span> b = a.myMap(<span class="hljs-function">(<span class="hljs-params">a,index</span>)=></span> &#123;
                <span class="hljs-keyword">return</span> a+<span class="hljs-number">1</span>; 
            &#125;
        )
        <span class="hljs-built_in">console</span>.log(b)   <span class="hljs-comment">// 输出 [2, 3, 4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">3. reduce实现数组的map方法</h2>
<p>利用数组内置的reduce方法实现map方法，考察对reduce原理的掌握</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.prototype.myMap = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn,thisValue</span>)</span>&#123;
     <span class="hljs-keyword">var</span> res = [];
     thisValue = thisValue||[];
     <span class="hljs-built_in">this</span>.reduce(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">pre,cur,index,arr</span>)</span>&#123;
         <span class="hljs-keyword">return</span> res.push(fn.call(thisValue,cur,index,arr));
     &#125;,[]);
     <span class="hljs-keyword">return</span> res;
&#125;
​
<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">1</span>,<span class="hljs-number">5</span>];
arr.myMap(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item,index,arr</span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(item,index,arr);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">4. 手写数组的reduce方法</h2>
<p>reduce() 方法接收一个函数作为累加器，数组中的每个值（从左到右）开始缩减，最终为一个值，是ES5中新增的又一个数组逐项处理方法</p>
<p><strong>参数：</strong></p>
<ul>
<li>
<p>callback（一个在数组中每一项上调用的函数，接受四个函数：）</p>
<ul>
<li>
<p>previousValue（上一次调用回调函数时的返回值，或者初始值）</p>
</li>
<li>
<p>currentValue（当前正在处理的数组元素）</p>
</li>
<li>
<p>currentIndex（当前正在处理的数组元素下标）</p>
</li>
<li>
<p>array（调用reduce()方法的数组）</p>
</li>
</ul>
</li>
<li>
<p>initialValue（可选的初始值。作为第一次调用回调函数时传给previousValue的值）</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reduce</span>(<span class="hljs-params">arr, cb, initialValue</span>)</span>&#123;
     <span class="hljs-keyword">var</span> num = initValue == <span class="hljs-literal">undefined</span>? num = arr[<span class="hljs-number">0</span>]: initValue;
     <span class="hljs-keyword">var</span> i = initValue == <span class="hljs-literal">undefined</span>? <span class="hljs-number">1</span>: <span class="hljs-number">0</span>
     <span class="hljs-keyword">for</span> (i; i< arr.length; i++)&#123;
        num = cb(num,arr[i],i)
     &#125;
     <span class="hljs-keyword">return</span> num
 &#125;
 
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">result, currentValue, index</span>)</span>&#123;
     <span class="hljs-keyword">return</span> result + currentValue
 &#125;
 
 <span class="hljs-keyword">var</span> arr = [<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>]
 <span class="hljs-keyword">var</span> b = reduce(arr, fn,<span class="hljs-number">10</span>) 
 <span class="hljs-keyword">var</span> c = reduce(arr, fn)
 <span class="hljs-built_in">console</span>.log(b)   <span class="hljs-comment">// 24</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">5. 数组扁平化</h2>
<p>数组扁平化就是把多维数组转化成一维数组</p>
<p><strong>1. es6提供的新方法 flat(depth)</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = [<span class="hljs-number">1</span>,[<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]]; 
a.flat(); <span class="hljs-comment">// [1,2,3] </span>
a.flat(<span class="hljs-number">1</span>); <span class="hljs-comment">//[1,2,3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实还有一种更简单的办法，无需知道数组的维度，直接将目标数组变成1维数组。 depth的值设置为Infinity。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = [<span class="hljs-number">1</span>,[<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,[<span class="hljs-number">4</span>,[<span class="hljs-number">5</span>]]]]; 
a.flat(<span class="hljs-literal">Infinity</span>); <span class="hljs-comment">// [1,2,3,4,5]  a是4维数组</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. 利用cancat</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flatten</span>(<span class="hljs-params">arr</span>) </span>&#123;
     <span class="hljs-keyword">var</span> res = [];
     <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, length = arr.length; i < length; i++) &#123;
     <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(arr[i])) &#123;
     res = res.concat(flatten(arr[i])); <span class="hljs-comment">//concat 并不会改变原数组</span>
     <span class="hljs-comment">//res.push(...flatten(arr[i])); //或者用扩展运算符 </span>
     &#125; <span class="hljs-keyword">else</span> &#123;
         res.push(arr[i]);
       &#125;
     &#125;
     <span class="hljs-keyword">return</span> res;
 &#125;
 <span class="hljs-keyword">let</span> arr1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>,[<span class="hljs-number">3</span>,<span class="hljs-number">1</span>],[<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,[<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]]]
flatten(arr1); <span class="hljs-comment">//[1, 2, 3, 1, 2, 3, 4, 2, 3, 4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">6. 函数柯里化</h2>
<p>这里用了这位大佬的方法 <a href="https://juejin.im/post/6844903882208837645" target="_blank" title="https://juejin.im/post/6844903882208837645">juejin.im/post/684490…</a></p>
<p>柯里化的定义：接收一部分参数，返回一个函数接收剩余参数，接收足够参数后，执行原函数。</p>
<p>当柯里化函数接收到足够参数后，就会执行原函数，如何去确定何时达到足够的参数呢？</p>
<p>有两种思路：</p>
<ol>
<li>
<p>通过函数的 length 属性，获取函数的形参个数，形参的个数就是所需的参数个数</p>
</li>
<li>
<p>在调用柯里化工具函数时，手动指定所需的参数个数</p>
</li>
</ol>
<p>将这两点结合一下，实现一个简单 curry 函数：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">/**
 * 将函数柯里化
 * <span class="hljs-doctag">@param </span>fn    待柯里化的原函数
 * <span class="hljs-doctag">@param </span>len   所需的参数个数，默认为原函数的形参个数
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curry</span>(<span class="hljs-params">fn,len = fn.length</span>) </span>&#123;
 <span class="hljs-keyword">return</span> _curry.call(<span class="hljs-built_in">this</span>,fn,len)
&#125;
​
<span class="hljs-comment">/**
 * 中转函数
 * <span class="hljs-doctag">@param </span>fn    待柯里化的原函数
 * <span class="hljs-doctag">@param </span>len   所需的参数个数
 * <span class="hljs-doctag">@param </span>args  已接收的参数列表
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_curry</span>(<span class="hljs-params">fn,len,...args</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...params</span>) </span>&#123;
         <span class="hljs-keyword">let</span> _args = [...args,...params];
         <span class="hljs-keyword">if</span>(_args.length >= len)&#123;
             <span class="hljs-keyword">return</span> fn.apply(<span class="hljs-built_in">this</span>,_args);
         &#125;<span class="hljs-keyword">else</span>&#123;
          <span class="hljs-keyword">return</span> _curry.call(<span class="hljs-built_in">this</span>,fn,len,..._args)
         &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来验证一下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> _fn = curry(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a,b,c,d,e</span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(a,b,c,d,e)
&#125;);
​
_fn(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>);     <span class="hljs-comment">// print: 1,2,3,4,5</span>
_fn(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>);   <span class="hljs-comment">// print: 1,2,3,4,5</span>
_fn(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>,<span class="hljs-number">4</span>)(<span class="hljs-number">5</span>);   <span class="hljs-comment">// print: 1,2,3,4,5</span>
_fn(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>)(<span class="hljs-number">4</span>)(<span class="hljs-number">5</span>); <span class="hljs-comment">// print: 1,2,3,4,5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们常用的工具库 lodash 也提供了 curry 方法，并且增加了非常好玩的 placeholder 功能，通过占位符的方式来改变传入参数的顺序。</p>
<p>比如说，我们传入一个占位符，本次调用传递的参数略过占位符， 占位符所在的位置由下次调用的参数来填充，比如这样：</p>
<p>直接看一下官网的例子：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d4f8885dde64cfb872389d7b20f19d2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们来思考，如何实现占位符的功能。</p>
<p>对于 lodash 的 curry 函数来说，curry 函数挂载在 lodash 对象上，所以将 lodash 对象当做默认占位符来使用。</p>
<p>而我们的自己实现的 curry 函数，本身并没有挂载在任何对象上，所以将 curry 函数当做默认占位符</p>
<p>使用占位符，目的是改变参数传递的顺序，所以在 curry 函数实现中，每次需要记录是否使用了占位符，并且记录占位符所代表的参数位置。</p>
<p>直接上代码：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@param  </span>fn           待柯里化的函数
 * <span class="hljs-doctag">@param  </span>length       需要的参数个数，默认为函数的形参个数
 * <span class="hljs-doctag">@param  </span>holder       占位符，默认当前柯里化函数
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;Function&#125;</span>   </span>柯里化后的函数
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curry</span>(<span class="hljs-params">fn,length = fn.length,holder = curry</span>)</span>&#123;
 <span class="hljs-keyword">return</span> _curry.call(<span class="hljs-built_in">this</span>,fn,length,holder,[],[])
&#125;
<span class="hljs-comment">/**
 * 中转函数
 * <span class="hljs-doctag">@param </span>fn            柯里化的原函数
 * <span class="hljs-doctag">@param </span>length        原函数需要的参数个数
 * <span class="hljs-doctag">@param </span>holder        接收的占位符
 * <span class="hljs-doctag">@param </span>args          已接收的参数列表
 * <span class="hljs-doctag">@param </span>holders       已接收的占位符位置列表
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;Function&#125;</span>   </span>继续柯里化的函数 或 最终结果
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_curry</span>(<span class="hljs-params">fn,length,holder,args,holders</span>)</span>&#123;
 <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">..._args</span>)</span>&#123;
 <span class="hljs-comment">//将参数复制一份，避免多次操作同一函数导致参数混乱</span>
 <span class="hljs-keyword">let</span> params = args.slice();
 <span class="hljs-comment">//将占位符位置列表复制一份，新增加的占位符增加至此</span>
 <span class="hljs-keyword">let</span> _holders = holders.slice();
 <span class="hljs-comment">//循环入参，追加参数 或 替换占位符</span>
 _args.forEach(<span class="hljs-function">(<span class="hljs-params">arg,i</span>)=></span>&#123;
 <span class="hljs-comment">//真实参数 之前存在占位符 将占位符替换为真实参数</span>
 <span class="hljs-keyword">if</span> (arg !== holder && holders.length) &#123;
     <span class="hljs-keyword">let</span> index = holders.shift();
     _holders.splice(_holders.indexOf(index),<span class="hljs-number">1</span>);
     params[index] = arg;
 &#125;
 <span class="hljs-comment">//真实参数 之前不存在占位符 将参数追加到参数列表中</span>
 <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(arg !== holder && !holders.length)&#123;
     params.push(arg);
 &#125;
 <span class="hljs-comment">//传入的是占位符,之前不存在占位符 记录占位符的位置</span>
 <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(arg === holder && !holders.length)&#123;
     params.push(arg);
     _holders.push(params.length - <span class="hljs-number">1</span>);
 &#125;
 <span class="hljs-comment">//传入的是占位符,之前存在占位符 删除原占位符位置</span>
 <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(arg === holder && holders.length)&#123;
    holders.shift();
 &#125;
 &#125;);
 <span class="hljs-comment">// params 中前 length 条记录中不包含占位符，执行函数</span>
 <span class="hljs-keyword">if</span>(params.length >= length && params.slice(<span class="hljs-number">0</span>,length).every(<span class="hljs-function"><span class="hljs-params">i</span>=></span>i!==holder))&#123;
 <span class="hljs-keyword">return</span> fn.apply(<span class="hljs-built_in">this</span>,params);
 &#125;<span class="hljs-keyword">else</span>&#123;
 <span class="hljs-keyword">return</span> _curry.call(<span class="hljs-built_in">this</span>,fn,length,holder,params,_holders)
 &#125;
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>验证一下：；</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> fn = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a, b, c, d, e</span>) </span>&#123;
 <span class="hljs-built_in">console</span>.log([a, b, c, d, e]);
&#125;
​
<span class="hljs-keyword">let</span> _ = &#123;&#125;; <span class="hljs-comment">// 定义占位符</span>
<span class="hljs-keyword">let</span> _fn = curry(fn,<span class="hljs-number">5</span>,_);  <span class="hljs-comment">// 将函数柯里化，指定所需的参数个数，指定所需的占位符</span>
​
_fn(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>);                 <span class="hljs-comment">// print: 1,2,3,4,5</span>
_fn(_, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>)(<span class="hljs-number">1</span>);              <span class="hljs-comment">// print: 1,2,3,4,5</span>
_fn(<span class="hljs-number">1</span>, _, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>)(<span class="hljs-number">2</span>);              <span class="hljs-comment">// print: 1,2,3,4,5</span>
_fn(<span class="hljs-number">1</span>, _, <span class="hljs-number">3</span>)(_, <span class="hljs-number">4</span>,_)(<span class="hljs-number">2</span>)(<span class="hljs-number">5</span>);         <span class="hljs-comment">// print: 1,2,3,4,5</span>
_fn(<span class="hljs-number">1</span>, _, _, <span class="hljs-number">4</span>)(_, <span class="hljs-number">3</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">5</span>);        <span class="hljs-comment">// print: 1,2,3,4,5</span>
_fn(_, <span class="hljs-number">2</span>)(_, _, <span class="hljs-number">4</span>)(<span class="hljs-number">1</span>)(<span class="hljs-number">3</span>)(<span class="hljs-number">5</span>);        <span class="hljs-comment">// print: 1,2,3,4,5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，我们已经完整实现了一个 curry 函数~~</p>
<h2 data-id="heading-7">7. 浅拷贝和深拷贝的实现</h2>
<p>深拷贝和浅拷贝是只针对Object和Array这样的引用数据类型的。</p>
<p><strong>浅拷贝和深拷贝的区别：</strong></p>
<p>浅拷贝：创建一个新对象，这个对象有着原始对象属性值的一份精确拷贝。如果属性是基本类型，拷贝的就是基本类型的值，如果属性是引用类型，拷贝的就是内存地址，如果其中一个对象改变了引用类型的属性，就会影响到另一个对象。</p>
<p>深拷贝：将一个对象从内存中完整的复制一份出来,从堆内存中开辟一个新区域存放。这样更改拷贝值就不影响旧的对象</p>
<h4 data-id="heading-8">浅拷贝实现：</h4>
<p>方法一：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shallowCopy</span>(<span class="hljs-params">target, origin</span>)</span>&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">in</span> origin) target[item] = origin[item];
    <span class="hljs-keyword">return</span> target;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他方法(内置api)：</p>
<ol>
<li>Object.assign</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj=&#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>,<span class="hljs-attr">b</span>:[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>],<span class="hljs-attr">c</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i am c'</span>)&#125;&#125;
<span class="hljs-keyword">var</span> tar=&#123;&#125;;
<span class="hljs-built_in">Object</span>.assign(tar,obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然这个方法只适合于对象类型，如果是数组可以使用slice和concat方法</p>
<ol start="2">
<li>Array.prototype.slice</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]];
<span class="hljs-keyword">var</span> newArr=arr.slice(<span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>Array.prototype.concat</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]];
<span class="hljs-keyword">var</span> newArr=arr.concat();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试同上(assign用对象测试、slice concat用数组测试)，结合浅拷贝深拷贝的概念来理解效果更佳</p>
<h4 data-id="heading-9">深拷贝实现：</h4>
<p><strong>方法一：</strong></p>
<p>转为json格式再解析
<code>const a = JSON.parse(JSON.stringify(b))</code></p>
<p><strong>方法二：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 实现深拷贝  递归</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepCopy</span>(<span class="hljs-params">newObj,oldObj</span>)</span>&#123;
     <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> k <span class="hljs-keyword">in</span> oldObj)&#123;
         <span class="hljs-keyword">let</span> item=oldObj[k]
         <span class="hljs-comment">// 判断是数组、对象、简单类型？</span>
         <span class="hljs-keyword">if</span>(item <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>)&#123;
             newObj[k]=[]
             deepCopy(newObj[k],item)
         &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(item <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)&#123;
             newObj[k]=&#123;&#125;
             deepCopy(newObj[k],item)
         &#125;<span class="hljs-keyword">else</span>&#123;  <span class="hljs-comment">//简单数据类型，直接赋值</span>
             newObj[k]=item
         &#125;
     &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">8. 手写call, apply, bind</h2>
<p><strong>手写call</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.myCall=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">context=<span class="hljs-built_in">window</span></span>)</span>&#123;  <span class="hljs-comment">// 函数的方法，所以写在Fuction原型对象上</span>
 <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span> !==<span class="hljs-string">"function"</span>)&#123;   <span class="hljs-comment">// 这里if其实没必要，会自动抛出错误</span>
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"不是函数"</span>)
 &#125;
 <span class="hljs-keyword">const</span> obj=context||<span class="hljs-built_in">window</span>   <span class="hljs-comment">//这里可用ES6方法，为参数添加默认值，js严格模式全局作用域this为undefined</span>
 obj.fn=<span class="hljs-built_in">this</span>      <span class="hljs-comment">//this为调用的上下文,this此处为函数，将这个函数作为obj的方法</span>
 <span class="hljs-keyword">const</span> arg=[...arguments].slice(<span class="hljs-number">1</span>)   <span class="hljs-comment">//第一个为obj所以删除,伪数组转为数组</span>
 res=obj.fn(...arg)
 <span class="hljs-keyword">delete</span> obj.fn   <span class="hljs-comment">// 不删除会导致context属性越来越多</span>
 <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//用法：f.call(obj,arg1)</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">a,b</span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(a+b)
 <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-keyword">let</span> obj=&#123;
 <span class="hljs-attr">name</span>:<span class="hljs-number">1</span>
&#125;
f.myCall(obj,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>) <span class="hljs-comment">//否则this指向window</span>

obj.greet.call(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'Spike'</span>&#125;) <span class="hljs-comment">//打出来的是 Spike</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>手写apply</strong>(arguments[this, [参数1，参数2.....] ])</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.myApply=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">context</span>)</span>&#123;  <span class="hljs-comment">// 箭头函数从不具有参数对象！！！！！这里不能写成箭头函数</span>
 <span class="hljs-keyword">let</span> obj=context||<span class="hljs-built_in">window</span>
 obj.fn=<span class="hljs-built_in">this</span>
 <span class="hljs-keyword">const</span> arg=<span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>]||[]    <span class="hljs-comment">//若有参数，得到的是数组</span>
 <span class="hljs-keyword">let</span> res=obj.fn(...arg)
 <span class="hljs-keyword">delete</span> obj.fn
 <span class="hljs-keyword">return</span> res
&#125; 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">a,b</span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(a,b)
 <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-keyword">let</span> obj=&#123;
 <span class="hljs-attr">name</span>:<span class="hljs-string">'张三'</span>
&#125;
f.myApply(obj,[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>])  <span class="hljs-comment">//arguments[1]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>手写bind</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.value = <span class="hljs-number">2</span>
<span class="hljs-keyword">var</span> foo = &#123;
 <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>
&#125;;
<span class="hljs-keyword">var</span> bar = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name, age, school</span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(name) <span class="hljs-comment">// 'An'</span>
 <span class="hljs-built_in">console</span>.log(age) <span class="hljs-comment">// 22</span>
 <span class="hljs-built_in">console</span>.log(school) <span class="hljs-comment">// '家里蹲大学'</span>
&#125;
<span class="hljs-keyword">var</span> result = bar.bind(foo, <span class="hljs-string">'An'</span>) <span class="hljs-comment">//预置了部分参数'An'</span>
result(<span class="hljs-number">22</span>, <span class="hljs-string">'家里蹲大学'</span>) <span class="hljs-comment">//这个参数会和预置的参数合并到一起放入bar中</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单版本</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.bind = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">context, ...outerArgs</span>) </span>&#123;
 <span class="hljs-keyword">var</span> fn = <span class="hljs-built_in">this</span>;
 <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...innerArgs</span>) </span>&#123;   <span class="hljs-comment">//返回了一个函数，...rest为实际调用时传入的参数</span>
 <span class="hljs-keyword">return</span> fn.apply(context,[...outerArgs, ...innerArgs]);  <span class="hljs-comment">//返回改变了this的函数，</span>
 <span class="hljs-comment">//参数合并</span>
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>new失败的原因：</p>
<p>例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 声明一个上下文</span>
<span class="hljs-keyword">let</span> thovino = &#123;
 <span class="hljs-attr">name</span>: <span class="hljs-string">'thovino'</span>
&#125;
​
<span class="hljs-comment">// 声明一个构造函数</span>
<span class="hljs-keyword">let</span> eat = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">food</span>) </span>&#123;
 <span class="hljs-built_in">this</span>.food = food
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> eat <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.food&#125;</span>`</span>)
&#125;
eat.prototype.sayFuncName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'func name : eat'</span>)
&#125;
​
<span class="hljs-comment">// bind一下</span>
<span class="hljs-keyword">let</span> thovinoEat = eat.bind(thovino)
<span class="hljs-keyword">let</span> instance = <span class="hljs-keyword">new</span> thovinoEat(<span class="hljs-string">'orange'</span>)  <span class="hljs-comment">//实际上orange放到了thovino里面</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'instance:'</span>, instance) <span class="hljs-comment">// &#123;&#125;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成的实例是个空对象</p>
<p>在<code>new</code>操作符执行时，我们的<code>thovinoEat</code>函数可以看作是这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">thovinoEat</span> (<span class="hljs-params">...innerArgs</span>) </span>&#123;
 eat.call(thovino, ...outerArgs, ...innerArgs)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在new操作符进行到第三步的操作<code>thovinoEat.call(obj, ...args)</code>时，这里的<code>obj</code>是new操作符自己创建的那个简单空对象<code>&#123;&#125;</code>，但它其实并没有替换掉<code>thovinoEat</code>函数内部的那个上下文对象<code>thovino</code>。这已经超出了<code>call</code>的能力范围，因为这个时候要替换的已经不是<code>thovinoEat</code>函数内部的<code>this</code>指向，而应该是<code>thovino</code>对象。</p>
<p><strong>换句话说，我们希望的是<code>new</code>操作符将<code>eat</code>内的<code>this</code>指向操作符自己创建的那个空对象。但是实际上指向了<code>thovino</code>，<code>new</code>操作符的第三步动作并没有成功</strong>！</p>
<p>可new可继承版本</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.bind = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context, ...outerArgs</span>) </span>&#123;
 <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span>;
​
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">res</span> (<span class="hljs-params">...innerArgs</span>) </span>&#123;
     <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span> <span class="hljs-keyword">instanceof</span> res) &#123;
         <span class="hljs-comment">// new操作符执行时</span>
         <span class="hljs-comment">// 这里的this在new操作符第三步操作时，会指向new自身创建的那个简单空对象&#123;&#125;</span>
         that.call(<span class="hljs-built_in">this</span>, ...outerArgs, ...innerArgs)
     &#125; <span class="hljs-keyword">else</span> &#123;
         <span class="hljs-comment">// 普通bind</span>
         that.call(context, ...outerArgs, ...innerArgs)
     &#125;
     &#125;
     res.prototype = <span class="hljs-built_in">this</span>.prototype <span class="hljs-comment">//！！！</span>
     <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">9. 手动实现new</h2>
<p>new的过程文字描述：</p>
<ol>
<li>
<p>创建一个空对象 obj;</p>
</li>
<li>
<p>将空对象的隐式原型（<strong>proto</strong>）指向构造函数的prototype。</p>
</li>
<li>
<p>使用 call 改变 this 的指向</p>
</li>
<li>
<p>如果无返回值或者返回一个非对象值，则将 obj 返回作为新对象；如果返回值是一个新对象的话那么直接直接返回该对象。</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name,age</span>)</span>&#123;
 <span class="hljs-built_in">this</span>.name=name
 <span class="hljs-built_in">this</span>.age=age
&#125;
Person.prototype.sayHi=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hi！我是'</span>+<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-keyword">let</span> p1=<span class="hljs-keyword">new</span> Person(<span class="hljs-string">'张三'</span>,<span class="hljs-number">18</span>)
​
<span class="hljs-comment">////手动实现new</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params"></span>)</span>&#123;
 <span class="hljs-keyword">let</span> obj=&#123;&#125;
 <span class="hljs-comment">//获取构造函数</span>
 <span class="hljs-keyword">let</span> fn=[].shift.call(<span class="hljs-built_in">arguments</span>)  <span class="hljs-comment">//将arguments对象提出来转化为数组，arguments并不是数组而是对象    ！！！这种方法删除了arguments数组的第一个元素，！！这里的空数组里面填不填元素都没关系，不影响arguments的结果      或者let arg = [].slice.call(arguments,1)</span>
 obj.__proto__=fn.prototype
 <span class="hljs-keyword">let</span> res=fn.apply(obj,<span class="hljs-built_in">arguments</span>)    <span class="hljs-comment">//改变this指向，为实例添加方法和属性</span>
 <span class="hljs-comment">//确保返回的是一个对象(万一fn不是构造函数)</span>
 <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> res===<span class="hljs-string">'object'</span>?res:obj
&#125;
​
<span class="hljs-keyword">let</span> p2=create(Person,<span class="hljs-string">'李四'</span>,<span class="hljs-number">19</span>)
p2.sayHi()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>细节：</p>
<pre><code class="hljs language-js copyable" lang="js">[].shift.call(<span class="hljs-built_in">arguments</span>)  也可写成：
 <span class="hljs-keyword">let</span> arg=[...arguments]
 <span class="hljs-keyword">let</span> fn=arg.shift()  <span class="hljs-comment">//使得arguments能调用数组方法,第一个参数为构造函数</span>
 obj.__proto__=fn.prototype
 <span class="hljs-comment">//改变this指向，为实例添加方法和属性</span>
 <span class="hljs-keyword">let</span> res=fn.apply(obj,arg)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">10. 手写promise(常考promise.all, promise.race)</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Promise/A+ 规范规定的三种状态</span>
<span class="hljs-keyword">const</span> STATUS = &#123;
 <span class="hljs-attr">PENDING</span>: <span class="hljs-string">'pending'</span>,
 <span class="hljs-attr">FULFILLED</span>: <span class="hljs-string">'fulfilled'</span>,
 <span class="hljs-attr">REJECTED</span>: <span class="hljs-string">'rejected'</span>
&#125;
​
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
 <span class="hljs-comment">// 构造函数接收一个执行回调</span>
 <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
     <span class="hljs-built_in">this</span>._status = STATUS.PENDING <span class="hljs-comment">// Promise初始状态</span>
     <span class="hljs-built_in">this</span>._value = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// then回调的值</span>
     <span class="hljs-built_in">this</span>._resolveQueue = [] <span class="hljs-comment">// resolve时触发的成功队列</span>
     <span class="hljs-built_in">this</span>._rejectQueue = [] <span class="hljs-comment">// reject时触发的失败队列</span>
    ​
 <span class="hljs-comment">// 使用箭头函数固定this（resolve函数在executor中触发，不然找不到this）</span>
 <span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
     <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
         <span class="hljs-comment">// Promise/A+ 规范规定的Promise状态只能从pending触发，变成fulfilled</span>
         <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._status === STATUS.PENDING) &#123;
             <span class="hljs-built_in">this</span>._status = STATUS.FULFILLED <span class="hljs-comment">// 更改状态</span>
             <span class="hljs-built_in">this</span>._value = value <span class="hljs-comment">// 储存当前值，用于then回调</span>
            ​
             <span class="hljs-comment">// 执行resolve回调</span>
             <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>._resolveQueue.length) &#123;
                 <span class="hljs-keyword">const</span> callback = <span class="hljs-built_in">this</span>._resolveQueue.shift()
                 callback(value)
             &#125;
         &#125;
     &#125;
     <span class="hljs-comment">//把resolve执行回调的操作封装成一个函数,放进setTimeout里,以实现promise异步调用的特性（规范上是微任务，这里是宏任务）</span>
     <span class="hljs-built_in">setTimeout</span>(run)
 &#125;
​
 <span class="hljs-comment">// 同 resolve</span>
 <span class="hljs-keyword">const</span> reject = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
     <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
         <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._status === STATUS.PENDING) &#123;
         <span class="hljs-built_in">this</span>._status = STATUS.REJECTED
         <span class="hljs-built_in">this</span>._value = value
        ​
         <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>._rejectQueue.length) &#123;
             <span class="hljs-keyword">const</span> callback = <span class="hljs-built_in">this</span>._rejectQueue.shift()
             callback(value)
         &#125;
     &#125;
 &#125;
     <span class="hljs-built_in">setTimeout</span>(run)
 &#125;

     <span class="hljs-comment">// new Promise()时立即执行executor,并传入resolve和reject</span>
     executor(resolve, reject)
 &#125;
​
 <span class="hljs-comment">// then方法,接收一个成功的回调和一个失败的回调</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>) </span>&#123;
  <span class="hljs-comment">// 根据规范，如果then的参数不是function，则忽略它, 让值继续往下传递，链式调用继续往下执行</span>
  <span class="hljs-keyword">typeof</span> onFulfilled !== <span class="hljs-string">'function'</span> ? onFulfilled = <span class="hljs-function"><span class="hljs-params">value</span> =></span> value : <span class="hljs-literal">null</span>
  <span class="hljs-keyword">typeof</span> onRejected !== <span class="hljs-string">'function'</span> ? onRejected = <span class="hljs-function"><span class="hljs-params">error</span> =></span> error : <span class="hljs-literal">null</span>

  <span class="hljs-comment">// then 返回一个新的promise</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> resolveFn = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> x = onFulfilled(value)
        <span class="hljs-comment">// 分类讨论返回值,如果是Promise,那么等待Promise状态变更,否则直接resolve</span>
        x <span class="hljs-keyword">instanceof</span> MyPromise ? x.then(resolve, reject) : resolve(x)
      &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        reject(error)
      &#125;
    &#125;
  &#125;
&#125;
​
  <span class="hljs-keyword">const</span> rejectFn = <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> x = onRejected(error)
        x <span class="hljs-keyword">instanceof</span> MyPromise ? x.then(resolve, reject) : resolve(x)
      &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        reject(error)
      &#125;
    &#125;

    <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>._status) &#123;
      <span class="hljs-keyword">case</span> STATUS.PENDING:
        <span class="hljs-built_in">this</span>._resolveQueue.push(resolveFn)
        <span class="hljs-built_in">this</span>._rejectQueue.push(rejectFn)
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> STATUS.FULFILLED:
        resolveFn(<span class="hljs-built_in">this</span>._value)
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> STATUS.REJECTED:
        rejectFn(<span class="hljs-built_in">this</span>._value)
        <span class="hljs-keyword">break</span>;
    &#125;
 &#125;)
 &#125;
 <span class="hljs-keyword">catch</span> (rejectFn) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">undefined</span>, rejectFn)
&#125;
<span class="hljs-comment">// promise.finally方法</span>
<span class="hljs-function"><span class="hljs-title">finally</span>(<span class="hljs-params">callback</span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> MyPromise.resolve(callback()).then(<span class="hljs-function">() =></span> value), <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    MyPromise.resolve(callback()).then(<span class="hljs-function">() =></span> error)
  &#125;)
&#125;

 <span class="hljs-comment">// 静态resolve方法</span>
 <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
      <span class="hljs-keyword">return</span> value <span class="hljs-keyword">instanceof</span> MyPromise ? value : <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> resolve(value))
  &#125;

 <span class="hljs-comment">// 静态reject方法</span>
 <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">error</span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> reject(error))
    &#125;

 <span class="hljs-comment">// 静态all方法</span>
 <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">promiseArr</span>)</span> &#123;
      <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>
      <span class="hljs-keyword">let</span> result = []
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span>       &#123;
        <span class="hljs-keyword">if</span> (!promiseArr.length) &#123;
          <span class="hljs-keyword">return</span> resolve(result)
        &#125;
        promiseArr.forEach(<span class="hljs-function">(<span class="hljs-params">p, i</span>) =></span> &#123;
          MyPromise.resolve(p).then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
            count++
            result[i] = value
            <span class="hljs-keyword">if</span> (count === promiseArr.length) &#123;
              resolve(result)
            &#125;
          &#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
            reject(error)
          &#125;)
        &#125;)
      &#125;)
    &#125;

 <span class="hljs-comment">// 静态race方法</span>
 <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promiseArr</span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        promiseArr.forEach(<span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
          MyPromise.resolve(p).then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
            resolve(value)
          &#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
            reject(error)
          &#125;)
        &#125;)
      &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">11. 手写原生AJAX</h2>
<p><strong>步骤</strong></p>
<ol>
<li>
<p>创建 XMLHttpRequest 实例</p>
</li>
<li>
<p>发出 HTTP 请求</p>
</li>
<li>
<p>服务器返回 XML 格式的字符串</p>
</li>
<li>
<p>JS 解析 XML，并更新局部页面</p>
</li>
</ol>
<p>不过随着历史进程的推进，XML 已经被淘汰，取而代之的是 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.json.org%2Fjson-zh.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.json.org/json-zh.html" ref="nofollow noopener noreferrer">JSON</a>。</strong></p>
<p>了解了属性和方法之后，根据 AJAX 的步骤，手写最简单的 GET 请求。</p>
<p>version 1.0：</p>
<pre><code class="hljs language-js copyable" lang="js">myButton.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  ajax()
&#125;)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajax</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest() <span class="hljs-comment">//实例化，以调用方法</span>
  xhr.open(<span class="hljs-string">'get'</span>, <span class="hljs-string">'https://www.google.com'</span>)  <span class="hljs-comment">//参数2，url。参数三：异步</span>
  xhr.onreadystatechange = <span class="hljs-function">() =></span> &#123;  <span class="hljs-comment">//每当 readyState 属性改变时，就会调用该函数。</span>
    <span class="hljs-keyword">if</span> (xhr.readyState === <span class="hljs-number">4</span>) &#123;  <span class="hljs-comment">//XMLHttpRequest 代理当前所处状态。</span>
      <span class="hljs-keyword">if</span> (xhr.status >= <span class="hljs-number">200</span> && xhr.status < <span class="hljs-number">300</span>) &#123;  <span class="hljs-comment">//200-300请求成功</span>
        <span class="hljs-keyword">let</span> string = request.responseText
        <span class="hljs-comment">//JSON.parse() 方法用来解析JSON字符串，构造由字符串描述的JavaScript值或对象</span>
        <span class="hljs-keyword">let</span> object = <span class="hljs-built_in">JSON</span>.parse(string)
      &#125;
    &#125;
  &#125;
  request.send() <span class="hljs-comment">//用于实际发出 HTTP 请求。不带参数为GET请求</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>promise实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajax</span>(<span class="hljs-params">url</span>) </span>&#123;
  <span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest()
    xhr.open(<span class="hljs-string">'get'</span>, url)
    xhr.onreadystatechange = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (xhr.readyState == <span class="hljs-number">4</span>) &#123;
        <span class="hljs-keyword">if</span> (xhr.status >= <span class="hljs-number">200</span> && xhr.status <= <span class="hljs-number">300</span>) &#123;
          resolve(<span class="hljs-built_in">JSON</span>.parse(xhr.responseText))
        &#125; <span class="hljs-keyword">else</span> &#123;
          reject(<span class="hljs-string">'请求出错'</span>)
        &#125;
      &#125;
    &#125;
    xhr.send()  <span class="hljs-comment">//发送hppt请求</span>
  &#125;)
  <span class="hljs-keyword">return</span> p
&#125;
<span class="hljs-keyword">let</span> url = <span class="hljs-string">'/data.json'</span>
ajax(url).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res))
  .catch(<span class="hljs-function"><span class="hljs-params">reason</span> =></span> <span class="hljs-built_in">console</span>.log(reason))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">12. 手写节流防抖函数</h2>
<pre><code class="hljs language-dart copyable" lang="dart">函数节流与函数防抖都是为了限制函数的执行频次，是一种性能优化的方案，比如应用于<span class="hljs-built_in">window</span>对象的resize、scroll事件，拖拽时的mousemove事件，文字输入、自动完成的keyup事件。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>节流</strong>：连续触发事件但是在 n 秒中只执行一次函数</p>
<p>例:（连续不断动都需要调用时用，设一时间间隔），像dom的拖拽，如果用消抖的话，就会出现卡顿的感觉，因为只在停止的时候执行了一次，这个时候就应该用节流，在一定时间内多次执行，会流畅很多。</p>
<p><strong>防抖</strong>：指触发事件后在 n 秒内函数只能执行一次，如果在 n 秒内又触发了事件，则会重新计算函数执行时间。</p>
<p>例:（连续不断触发时不调用，触发完后过一段时间调用），像仿百度搜索，就应该用防抖，当我连续不断输入时，不会发送请求；当我一段时间内不输入了，才会发送一次请求；如果小于这段时间继续输入的话，时间会重新计算，也不会发送请求。</p>
<p>防抖的实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">fn, delay</span>) </span>&#123;
     <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> fn!==<span class="hljs-string">'function'</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'fn不是函数'</span>)
     &#125;
     <span class="hljs-keyword">let</span> timer; <span class="hljs-comment">// 维护一个 timer</span>
     <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
         <span class="hljs-keyword">var</span> _this = <span class="hljs-built_in">this</span>; <span class="hljs-comment">// 取debounce执行作用域的this(原函数挂载到的对象)</span>
         <span class="hljs-keyword">var</span> args = <span class="hljs-built_in">arguments</span>;
         <span class="hljs-keyword">if</span> (timer) &#123;
            <span class="hljs-built_in">clearTimeout</span>(timer);
         &#125;
         timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            fn.apply(_this, args); <span class="hljs-comment">// 用apply指向调用debounce的对象，相当于_this.fn(args);</span>
         &#125;, delay);
     &#125;;
&#125;

<span class="hljs-comment">// 调用​</span>
input1.addEventListener(<span class="hljs-string">'keyup'</span>, debounce(<span class="hljs-function">() =></span> &#123;
 <span class="hljs-built_in">console</span>.log(input1.value)
&#125;), <span class="hljs-number">600</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>节流的实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">fn, delay</span>) </span>&#123;
  <span class="hljs-keyword">let</span> timer;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> _this = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">var</span> args = <span class="hljs-built_in">arguments</span>;
    <span class="hljs-keyword">if</span> (timer) &#123;
      <span class="hljs-keyword">return</span>;
    &#125;
    timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      fn.apply(_this, args); <span class="hljs-comment">// 这里args接收的是外边返回的函数的参数，不能用arguments</span>
      <span class="hljs-comment">// fn.apply(_this, arguments); 需要注意：Chrome 14 以及 Internet Explorer 9 仍然不接受类数组对象。如果传入类数组对象，它们会抛出异常。</span>
      timer = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 在delay后执行完fn之后清空timer，此时timer为假，throttle触发可以进入计时器</span>
    &#125;, delay)
  &#125;
&#125;

div1.addEventListener(<span class="hljs-string">'drag'</span>, throttle(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(e.offsetX, e.offsetY)
&#125;, <span class="hljs-number">100</span>))

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">13. 手写Promise加载图片</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getData</span>(<span class="hljs-params">url</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    $.ajax(&#123;
      url,
      <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params">data</span>)</span> &#123;
        resolve(data)
      &#125;,
      <span class="hljs-function"><span class="hljs-title">error</span>(<span class="hljs-params">err</span>)</span> &#123;
        reject(err)
      &#125;
    &#125;)
  &#125;)
&#125;
<span class="hljs-keyword">const</span> url1 = <span class="hljs-string">'./data1.json'</span>
<span class="hljs-keyword">const</span> url2 = <span class="hljs-string">'./data2.json'</span>
<span class="hljs-keyword">const</span> url3 = <span class="hljs-string">'./data3.json'</span>
getData(url1).then(<span class="hljs-function"><span class="hljs-params">data1</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data1)
  <span class="hljs-keyword">return</span> getData(url2)
&#125;).then(<span class="hljs-function"><span class="hljs-params">data2</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data2)
  <span class="hljs-keyword">return</span> getData(url3)
&#125;).then(<span class="hljs-function"><span class="hljs-params">data3</span> =></span>
  <span class="hljs-built_in">console</span>.log(data3)
).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span>
  <span class="hljs-built_in">console</span>.error(err)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">14. 函数实现一秒钟输出一个数</h2>
<p>(!!!这个题这两天字节校招面试被问到了，问var打印的什么，改为let为什么可以？
有没有其他方法实现？我自己博客里都写了不用let的写法第二种方法,居然给忘了~~~白学了)</p>
<p><strong>ES6</strong>：用let块级作用域的原理实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<=<span class="hljs-number">10</span>;i++)&#123;   <span class="hljs-comment">//用var打印的都是11</span>
 <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(i);
 &#125;,<span class="hljs-number">1000</span>*i)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>不用let的写法</strong>： 原理是用立即执行函数创造一个块级作用域</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">10</span>; i++)&#123;
    (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">i</span>) </span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(i);
        &#125;, <span class="hljs-number">1000</span> * i)
    &#125;)(i);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">15. 创建10个标签，点击的时候弹出来对应的序号？</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-number">10</span>;i++)&#123;
 a=<span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'a'</span>)
 a.innerHTML=i+<span class="hljs-string">'<br>'</span>
 a.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>)</span>&#123;
     <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)  <span class="hljs-comment">//this为当前点击的<a></span>
     e.preventDefault()  <span class="hljs-comment">//如果调用这个方法，默认事件行为将不再触发。</span>
     <span class="hljs-comment">//例如，在执行这个方法后，如果点击一个链接（a标签），浏览器不会跳转到新的 URL 去了。我们可以用 event.isDefaultPrevented() 来确定这个方法是否(在那个事件对象上)被调用过了。</span>
     alert(i)
 &#125;)
 <span class="hljs-keyword">const</span> d=<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'div'</span>)
 d.appendChild(a)  <span class="hljs-comment">//append向一个已存在的元素追加该元素。</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">16. 实现事件订阅发布(eventBus)</h2>
<p>实现EventBus类，有 on off once trigger功能，分别对应绑定事件监听器，解绑，执行一次后解除事件绑定，触发事件监听器。 这个题目面字节和快手都问到了，最近忙，答案会在后续更新</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventBus</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">on</span>(<span class="hljs-params">eventName, listener</span>)</span> &#123;&#125;
    <span class="hljs-function"><span class="hljs-title">off</span>(<span class="hljs-params">eventName, listener</span>)</span> &#123;&#125;
    <span class="hljs-function"><span class="hljs-title">once</span>(<span class="hljs-params">eventName, listener</span>)</span> &#123;&#125;
    <span class="hljs-function"><span class="hljs-title">trigger</span>(<span class="hljs-params">eventName</span>)</span> &#123;&#125;
&#125;

<span class="hljs-keyword">const</span> e = <span class="hljs-keyword">new</span> EventBus();
<span class="hljs-comment">// fn1 fn2</span>
e.on(<span class="hljs-string">'e1'</span>, fn1)
e.once(<span class="hljs-string">'e1'</span>, fn2)
e.trigger(<span class="hljs-string">'e1'</span>) <span class="hljs-comment">// fn1() fn2()</span>
e.trigger(<span class="hljs-string">'e1'</span>) <span class="hljs-comment">// fn1()</span>
e.off(<span class="hljs-string">'e1'</span>, fn1)
e.trigger(<span class="hljs-string">'e1'</span>) <span class="hljs-comment">// null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现：</p>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-comment">//声明类</span>
      <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventBus</span> </span>&#123;
        <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-built_in">this</span>.eventList = &#123;&#125; <span class="hljs-comment">//创建对象收集事件</span>
        &#125;
        <span class="hljs-comment">//发布事件</span>
        $on(eventName, fn) &#123;
          <span class="hljs-comment">//判断是否发布过事件名称? 添加发布 : 创建并添加发布</span>
          <span class="hljs-built_in">this</span>.eventList[eventName]
            ? <span class="hljs-built_in">this</span>.eventList[eventName].push(fn)
            : (<span class="hljs-built_in">this</span>.eventList[eventName] = [fn])
        &#125;
        <span class="hljs-comment">//订阅事件</span>
        $emit(eventName) &#123;
          <span class="hljs-keyword">if</span> (!eventName) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请传入事件名'</span>)
          <span class="hljs-comment">//获取订阅传参</span>
          <span class="hljs-keyword">const</span> data = [...arguments].slice(<span class="hljs-number">1</span>)
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.eventList[eventName]) &#123;
            <span class="hljs-built_in">this</span>.eventList[eventName].forEach(<span class="hljs-function">(<span class="hljs-params">i</span>) =></span> &#123;
              <span class="hljs-keyword">try</span> &#123;
                i(...data) <span class="hljs-comment">//轮询事件</span>
              &#125; <span class="hljs-keyword">catch</span> (e) &#123;
                <span class="hljs-built_in">console</span>.error(e + <span class="hljs-string">'eventName:'</span> + eventName) <span class="hljs-comment">//收集执行时的报错</span>
              &#125;
            &#125;)
          &#125;
        &#125;
        <span class="hljs-comment">//执行一次</span>
        $once(eventName, fn) &#123;
          <span class="hljs-keyword">const</span> _this = <span class="hljs-built_in">this</span>
          <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onceHandle</span>(<span class="hljs-params"></span>) </span>&#123;
            fn.apply(<span class="hljs-literal">null</span>, <span class="hljs-built_in">arguments</span>)
            _this.$off(eventName, onceHandle) <span class="hljs-comment">//执行成功后取消监听</span>
          &#125;
          <span class="hljs-built_in">this</span>.$on(eventName, onceHandle)
        &#125;
        <span class="hljs-comment">//取消订阅</span>
        $off(eventName, fn) &#123;
          <span class="hljs-comment">//不传入参数时取消全部订阅</span>
          <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">arguments</span>.length) &#123;
            <span class="hljs-keyword">return</span> (<span class="hljs-built_in">this</span>.eventList = &#123;&#125;)
          &#125;
          <span class="hljs-comment">//eventName传入的是数组时,取消多个订阅</span>
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(eventName)) &#123;
            <span class="hljs-keyword">return</span> eventName.forEach(<span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
              <span class="hljs-built_in">this</span>.$off(event, fn)
            &#125;)
          &#125;
          <span class="hljs-comment">//不传入fn时取消事件名下的所有队列</span>
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length === <span class="hljs-number">1</span> || !fn) &#123;
            <span class="hljs-built_in">this</span>.eventList[eventName] = []
          &#125;
          <span class="hljs-comment">//取消事件名下的fn</span>
          <span class="hljs-built_in">this</span>.eventList[eventName] = <span class="hljs-built_in">this</span>.eventList[eventName].filter(
            <span class="hljs-function">(<span class="hljs-params">f</span>) =></span> f !== fn
          )
        &#125;
      &#125;
      <span class="hljs-keyword">const</span> event = <span class="hljs-keyword">new</span> EventBus()

      <span class="hljs-keyword">let</span> b = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">v1, v2, v3</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b'</span>, v1, v2, v3)
      &#125;
      <span class="hljs-keyword">let</span> a = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>)
      &#125;
      event.$once(<span class="hljs-string">'test'</span>, a)
      event.$on(<span class="hljs-string">'test'</span>, b)
      event.$emit(<span class="hljs-string">'test'</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">45</span>, <span class="hljs-number">123</span>)

      event.$off([<span class="hljs-string">'test'</span>], b)

      event.$emit(<span class="hljs-string">'test'</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">45</span>, <span class="hljs-number">123</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>参考：</strong></p>
<p>数组扁平化 <a href="https://juejin.im/post/5c971ee16fb9a070ce31b64e#heading-3" target="_blank" title="https://juejin.im/post/5c971ee16fb9a070ce31b64e#heading-3">juejin.im/post/5c971e…</a></p>
<p>函数柯里化 <a href="https://juejin.im/post/6844903882208837645" target="_blank" title="https://juejin.im/post/6844903882208837645">juejin.im/post/684490…</a></p>
<p>节流防抖 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fc8b86b09daf0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/c8b86b09daf0" ref="nofollow noopener noreferrer">www.jianshu.com/p/c8b86b09d…</a></p>
<p>事件订阅发布实现 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fheznb.com%2Farchives%2Fjs-shi-xian-eventbuss-shi-jian-zong-xian--fa-bu-ding-yue-mo-shi-" target="_blank" rel="nofollow noopener noreferrer" title="https://heznb.com/archives/js-shi-xian-eventbuss-shi-jian-zong-xian--fa-bu-ding-yue-mo-shi-" ref="nofollow noopener noreferrer">heznb.com/archives/js…</a></p>
<p>浅拷贝深拷贝 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000014234116" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000014234116" ref="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p></div>  
</div>
            