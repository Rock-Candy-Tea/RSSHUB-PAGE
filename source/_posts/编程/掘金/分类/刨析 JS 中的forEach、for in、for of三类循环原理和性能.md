
---
title: '刨析 JS 中的forEach、for in、for of三类循环原理和性能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1805'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 17:12:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=1805'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><strong>大家好，我是林一一，这是一篇比较 JS 中三类循环的原理和性能的文章，希望能给你带来点帮助 😁</strong></p>
</blockquote>
<h2 data-id="heading-0">性能比较</h2>
<h2 data-id="heading-1">for 循环和 while 循环的性能对比</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">999999</span>).fill(<span class="hljs-number">1</span>)

<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'forTime'</span>)
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i< arr.length; i++)&#123;&#125;
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'forTime'</span>)

<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'whileTime'</span>)
<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
<span class="hljs-keyword">while</span>(i< arr.length)&#123;
    i ++ 
&#125;
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'whileTime'</span>)
<span class="hljs-comment">/* 输出
* forTime: 4.864990234375 ms
* whileTime: 8.35107421875 ms
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用 <code>let</code> 声明下的循环，由于 <code>for</code> 中块级作用域的影响，内存得到释放，运行的运行的速度会更快一些。</li>
<li>使用 <code>var</code> 声明时因为<code>for while</code> 的循环都不存在块级作用域的影响，两者运行的速度基本一致。</li>
</ul>
<h2 data-id="heading-2">forEach(callback, thisArg) 循环数组</h2>
<blockquote>
<p><code>callback</code> 函数每一轮循环都会执行一次，且还可以接收三个参数<code>(currentValue, index, array)</code>，<code>index, array</code> 也是可选的，<code>thisArg</code>(可选) 是回调函数的 <code>this</code> 指向。</p>
</blockquote>
<ul>
<li>遍历可枚举的属性</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">999999</span>).fill(<span class="hljs-number">1</span>)
<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'forEachTime'</span>)
arr.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span>&#123;&#125; )
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'forEachTime'</span>)
<span class="hljs-comment">// forEachTime: 25.3291015625 ms</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>函数式编程的 <code>forEach</code> 性能消耗要更大一些。</li>
</ul>
<h3 data-id="heading-3">思考：在 forEach 中使用 return 能中断循环吗？</h3>
<pre><code class="hljs language-js copyable" lang="js">[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>].forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(item, index)
    <span class="hljs-keyword">return</span>
&#125;)
<span class="hljs-comment">// 1 0</span>
<span class="hljs-comment">// 2 1</span>
<span class="hljs-comment">// 4 2</span>
<span class="hljs-comment">// 5 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>从上面看出 forEach 中使用 return 是不能跳出循环的。</p>
</blockquote>
<p><strong>那么如何中断 forEach 的循环</strong>、</p>
<ul>
<li>可以使用 try catch</li>
<li>或使用其他循环来代替，比如 用 every 和some 替代 forEach，every 中内部返回 false是跳出，some 中内部是 true 时 跳出</li>
</ul>
<h3 data-id="heading-4">模拟实现 forEach</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.prototype.myForEach = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">callback, context</span>) </span>&#123;
    <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>,
        than = <span class="hljs-built_in">this</span>,
        len = <span class="hljs-built_in">this</span>.length;
    context = context ? <span class="hljs-built_in">window</span> : context;
    <span class="hljs-keyword">for</span> (; i < len; i++) &#123;
        <span class="hljs-keyword">typeof</span> callback === <span class="hljs-string">'function'</span> ? callback.call(context, than[i], i, than) : <span class="hljs-literal">null</span>
    &#125;
&#125;

<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">5</span>, <span class="hljs-number">9</span>]
arr.myForEach(<span class="hljs-function">(<span class="hljs-params">item, index, arr</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(item, index, arr)
&#125;)

<span class="hljs-comment">//0 0 (4) [0, 1, 5, 9]</span>
<span class="hljs-comment">// 1 1 (4) [0, 1, 5, 9]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>结果准确无误。关于 this 指向或 call 的使用的可以看看 <a href="https://juejin.cn/post/6942697803709677582" target="_blank">JS this 指向</a>  和  <a href="https://juejin.cn/post/6945219696429891597" target="_blank">call, apply, bind的模拟实现</a></p>
</blockquote>
<h2 data-id="heading-5">for in 循环</h2>
<blockquote>
<p><code>for in</code> 的循环性能循环很差。性能差的原因是因为：<code>for in</code> 会迭代对象原型链上一切 <code>可以枚举</code>的属性。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">999999</span>).fill(<span class="hljs-number">1</span>)
<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'forInTime'</span>)
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> arr)&#123;&#125;
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'forInTime'</span>)
<span class="hljs-comment">// forInTime: 323.08984375 ms</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>for in</code> 循环主要用于对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'林一一'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
    <span class="hljs-number">0</span>: <span class="hljs-string">'number0'</span>,
    <span class="hljs-number">1</span>: <span class="hljs-string">'number1'</span>,
    [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'a'</span>)]: <span class="hljs-number">10</span>
&#125;

<span class="hljs-built_in">Object</span>.prototype.fn = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;

<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> obj)&#123;
<span class="hljs-comment">//    if(!obj.hasOwnProperty(key)) break 阻止获取原型链上的公有属性 fn</span>
    <span class="hljs-built_in">console</span>.log(key)
&#125;
<span class="hljs-comment">/* 输出
 0
 1
 name
 age
 fn
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>(缺点) <code>for in</code> 循环主要遍历数字优先，由小到大遍历</li>
<li>(缺点) <code>for in</code> 无法遍历 <code>Symbol</code>属性（不可枚举）。</li>
<li>(缺点) <code>for in</code> 会将公有(prototype) 中可枚举的属性也遍历了。可以使用 <code>hasOwnProperty</code>来阻止遍历公有属性。</li>
</ul>
<h3 data-id="heading-6">思考</h3>
<h4 data-id="heading-7">1. 怎么获取 Symbol 属性</h4>
<blockquote>
<p>使用 <code>Object.getOwnPropertySymbols()</code>，获取所有 Symbol 属性。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'林一一'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
    <span class="hljs-number">0</span>: <span class="hljs-string">'number0'</span>,
    <span class="hljs-number">1</span>: <span class="hljs-string">'number1'</span>,
    [<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'a'</span>)]:  <span class="hljs-number">10</span>
&#125;

<span class="hljs-built_in">Object</span>.prototype.fn = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;

<span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">Object</span>.keys(obj).concat(<span class="hljs-built_in">Object</span>.getOwnPropertySymbols(obj))
<span class="hljs-built_in">console</span>.log(arr)    <span class="hljs-comment">//["0", "1", "name", "age", Symbol(a)]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">for of 循环</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">999999</span>).fill(<span class="hljs-number">1</span>)
<span class="hljs-built_in">console</span>.time(<span class="hljs-string">'forOfTime'</span>)
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> value <span class="hljs-keyword">of</span> arr)&#123;&#125;
<span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'forOfTime'</span>)
<span class="hljs-comment">// forOfTime: 33.513916015625 ms</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>for of 循环的原理是<code>按照是否有迭代器规范来循环的</code>，所有带有 <code>Symbol.iterator</code> 的都是实现了迭代器规范，比如数组一部分类数组，<code>Set,Map...</code>，<code>对象没有实现 Symbol.iterator 规范</code>，所以不能使用<code>for of</code>循环。</p>
</blockquote>
<ul>
<li>使用 <code>for of</code> 循环，首先会先执行 <code>Symbol.iterator</code> 属性对应的函数且返回一个对象</li>
<li>对象内包含一个函数 <code>next()</code> 循环一次执行一次 <code>next()</code>，<code>next()</code> 中又返回一个对象</li>
<li>这个对象内包含两个值分别是 <code>done：代表循环是否结束，true 代表结束；value：代表每次返回的值</code>。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Symbol.iterator 内部机制如下</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">12</span>, <span class="hljs-number">23</span>, <span class="hljs-number">34</span>]
arr[<span class="hljs-built_in">Symbol</span>.iterator] = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> self = <span class="hljs-built_in">this</span>,
        index = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-function"><span class="hljs-title">next</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">if</span>(index > self.length-<span class="hljs-number">1</span>)&#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-attr">done</span>: <span class="hljs-literal">true</span>,
                    <span class="hljs-attr">value</span>: <span class="hljs-literal">undefined</span>
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">done</span>: <span class="hljs-literal">false</span>,
                <span class="hljs-attr">value</span>: self[index++]
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">思考，如何让普通的类数组可以使用 for of 循环</h3>
<blockquote>
<p>类数组被需具备和数组类试的结果属性名从<code>0, 1, 2...</code>开始，且必须具备<code>length</code> 属性</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-number">0</span>: <span class="hljs-number">12</span>,
    <span class="hljs-number">1</span>: <span class="hljs-string">'林一一'</span>,
    <span class="hljs-number">2</span>: <span class="hljs-string">'age18'</span>,
    <span class="hljs-attr">length</span>: <span class="hljs-number">3</span>
&#125;
<span class="hljs-comment">// </span>
obj[<span class="hljs-built_in">Symbol</span>.iterator] = <span class="hljs-built_in">Array</span>.prototype[<span class="hljs-built_in">Symbol</span>.iterator]
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> value <span class="hljs-keyword">of</span> obj) &#123;
    <span class="hljs-built_in">console</span>.log(value)   
&#125;
<span class="hljs-comment">/* 属性
*   12
*   林一一
*   age18
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>只需要给类数组对象添加<code>Symbol.iterator</code>接口规范就可以了。</p>
</blockquote>
<h2 data-id="heading-10">(附加)将argument实参集合变成真正的数组</h2>
<p><strong><code>arguments</code> 为什么不是数组？</strong></p>
<ul>
<li><code>arguments</code> 是类数组(其实是一个对象)属性从0开始排，依次为0，1，2... 最后还有 <code>callee和length</code> 属性，<code>arguments</code> 的 <code>__proto__</code> 直接指向基类的 <code>object</code>，不具备数组的方法。</li>
</ul>
<h3 data-id="heading-11">方式一 使用 call()，[].slice/Array.prototype.slice()</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> array = [<span class="hljs-number">12</span>, <span class="hljs-number">23</span>, <span class="hljs-number">45</span>, <span class="hljs-number">65</span>, <span class="hljs-number">32</span>]
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">array</span>)</span>&#123;
    <span class="hljs-keyword">var</span> args = [].slice.call(<span class="hljs-built_in">arguments</span>)
    <span class="hljs-keyword">return</span> args[<span class="hljs-number">0</span>]
&#125;
fn(array)   <span class="hljs-comment">// [12, 23, 45, 65, 32]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>上面的 <code>slice</code> 结合 <code>call</code> 为什么可以在改变 <code>this</code> 后可以将 <code>arguments</code> 转化成数组？我们来模拟手写实现一下 <code>slice</code>，就知道里面的原理了</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.prototype.mySlice = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">startIndex=<span class="hljs-number">0</span>, endIndex</span>)</span>&#123;
    <span class="hljs-keyword">let</span> array = <span class="hljs-built_in">this</span>    <span class="hljs-comment">// 通过 this 获取调用的数组</span>
    <span class="hljs-keyword">let</span> thisArray = []
    endIndex === <span class="hljs-literal">undefined</span> ? (endIndex = array.length) : <span class="hljs-literal">null</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = startIndex; i< endIndex; i++)&#123;      <span class="hljs-comment">// 通过 `length` 属性遍历</span>
        thisArray.push(array[i])
    &#125;
    <span class="hljs-keyword">return</span> thisArray
&#125;

<span class="hljs-comment">// 测试一下没有问题</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">23</span>]
<span class="hljs-keyword">let</span> a 
a = arr.mySlice()   <span class="hljs-comment">// [1, 3, 5, 6, 7, 23]</span>
a = arr.mySlice(<span class="hljs-number">2</span>, <span class="hljs-number">6</span>)   <span class="hljs-comment">// [5, 6, 7, 23]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>通过 <code>this</code> 获取调用 <code>mySlice</code> 的数组，再通过 <code>length</code> 属性遍历形成一个新的数组返回。所以改变<code>this</code> 指向 <code>arguments</code> 再通过 <code>arguments.length</code> 遍历返回一个新的数组，便实现了将类数组转化成数组了。</p>
</blockquote>
<p><strong><strong>来思考一下字符串可以转化成数组吗？</strong></strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = [].slice.call(<span class="hljs-string">'stringToArray'</span>)
<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">// ["s", "t", "r", "i", "n", "g", "T", "o", "A", "r", "r", "a", "y"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>同样也是可以的，理由同上。至于字符串(值类型)为什么被 <code>this</code> 指定，可以来看看这篇文章 <a href="https://juejin.cn/post/6976419561067249672">面试 | call,apply,bind 的实现原理和面试题</a></p>
</blockquote>
<h3 data-id="heading-12">方式二 使用 ES6 的扩展运算符 <code>...</code></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">array</span>)</span>&#123;
    <span class="hljs-keyword">var</span> args = [...arguments]
    <span class="hljs-keyword">return</span> args
&#125;
fn(<span class="hljs-number">12</span>, <span class="hljs-number">23</span>, <span class="hljs-number">45</span>, <span class="hljs-number">65</span>, <span class="hljs-number">32</span>)   <span class="hljs-comment">// [12, 23, 45, 65, 32]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">方式三 Array.from()</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">array</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">arguments</span>)
&#125;
fn(<span class="hljs-number">12</span>, <span class="hljs-number">23</span>, <span class="hljs-number">45</span>, <span class="hljs-number">65</span>, <span class="hljs-number">32</span>)   <span class="hljs-comment">// [12, 23, 45, 65, 32]</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            