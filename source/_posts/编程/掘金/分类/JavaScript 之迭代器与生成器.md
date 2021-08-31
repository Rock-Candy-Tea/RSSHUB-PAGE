
---
title: 'JavaScript 之迭代器与生成器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1217'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 08:32:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=1217'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>因为前一篇文章在写 <a href="https://juejin.cn/post/6998176775930904607" target="_blank" title="https://juejin.cn/post/6998176775930904607">React 学习之常用 Redux Middleware</a>，写到 <code>redux-saga</code> 中间件时，发现需要复习的迭代器与生成器的内容有点太多了，干脆单独作为一篇文章得了</p>
<p>既然被小姐姐吸引进来了，好歹看一眼再走？！🤫 哈哈，废话不多说，进入正文辣～</p>
<h2 data-id="heading-0">迭代器与可迭代协议</h2>
<p>迭代：按某种逻辑，依次取出下一个数据进行处理 (不需要依赖集合数据结构)；它类似于 <code>遍历</code> (而遍历则是从有多个数据组成的集合数据结构 <code>(map、set、array 等数组或类数组)</code> 中依次取出数据进行处理的过程)</p>
<p><strong>迭代器 (<code>iterator</code>)</strong> ：用我们的话来说就是 JavaScript 语言规定，如果一个对象具有 <code>next 方法</code>，且 next 方法被调用后会返回一个至少具有 <code>value (数据的值，done 为 true 则置为 undefined)</code> 和 <code>done (boolean 是否迭代完毕)</code> 属性的对象，那么我们可以称这个对象为迭代器对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 比如，最简结果：</span>
<span class="hljs-comment">// 以产生随机数为例：</span>
<span class="hljs-keyword">const</span> iterator = &#123;
    <span class="hljs-function"><span class="hljs-title">next</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">value</span>: <span class="hljs-built_in">Math</span>.rondom(),
            <span class="hljs-attr">done</span>: <span class="hljs-literal">false</span>
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// 再比如，可迭代三次的迭代器：</span>
<span class="hljs-keyword">const</span> iteratorObj = &#123;
    <span class="hljs-attr">total</span>: <span class="hljs-number">3</span>,
    <span class="hljs-attr">idx</span>: <span class="hljs-number">0</span>,
    <span class="hljs-function"><span class="hljs-title">next</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> res = &#123;
            <span class="hljs-attr">value</span>: <span class="hljs-built_in">this</span>.idx > <span class="hljs-built_in">this</span>.total ? <span class="hljs-literal">undefined</span> : <span class="hljs-built_in">this</span>.idx,
            <span class="hljs-attr">done</span>: <span class="hljs-built_in">this</span>.idx > <span class="hljs-built_in">this</span>.total
        &#125;
        <span class="hljs-built_in">this</span>.idx++
        <span class="hljs-keyword">return</span> res
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>又比如，我在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsuressk.com%2Farticle%2Fc1802cd1-4e97-42e1-926c-92d7fbae8063_1016" target="_blank" rel="nofollow noopener noreferrer" title="https://suressk.com/article/c1802cd1-4e97-42e1-926c-92d7fbae8063_1016" ref="nofollow noopener noreferrer">《Summary of Interview Algorithm》</a> 一文中第 4 点有写到另外几种方案的 <code>斐波那契数列</code> 实现以及一些优化方案，使用迭代器实现斐波那契数列的方案如下 (那么当然，它是正向取值，其结果是不可逆的，除非去另外控制)：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fibo = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">b</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">curIdx</span>: <span class="hljs-number">1</span>,
    <span class="hljs-function"><span class="hljs-title">next</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.curIdx === <span class="hljs-number">1</span> || <span class="hljs-built_in">this</span>.curIdx === <span class="hljs-number">2</span>) &#123;
            <span class="hljs-built_in">this</span>.curIdx ++
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>,
                <span class="hljs-attr">done</span>: <span class="hljs-literal">false</span>
            &#125;
        &#125;
        <span class="hljs-keyword">const</span> c = <span class="hljs-built_in">this</span>.a + <span class="hljs-built_in">this</span>.b
        <span class="hljs-built_in">this</span>.curIdx++
        [<span class="hljs-built_in">this</span>.a, <span class="hljs-built_in">this</span>.b] = [<span class="hljs-built_in">this</span>.b, c]
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">value</span>: c,
            <span class="hljs-attr">done</span>: <span class="hljs-literal">false</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以通过调用 next 方法依次取出数据，并可根据返回对象的 done 属性判定是否迭代结束</p>
<p><strong>迭代器创建函数 (iterator creator)</strong>：它是指一个函数，调用该函数，会返回一个迭代器，也可简称为 <code>迭代器函数</code></p>
<p><strong>可迭代协议</strong></p>
<p>ES6 新增了 <code>for...of</code> 循环，该循环就是用于迭代某个对象的，因此 <code>for...of</code> 循环要求该对象必须是可迭代的 (该对象必须满足可迭代协议)</p>
<p>可迭代协议：一个对象必须拥有 <code>知名符号属性 Symbol.iterator</code>，该属性必须是一个 <code>无参的迭代器创建函数</code></p>
<p><strong>for...of 循环原理</strong>：调用对象的 <code>[Symbol.iterator]</code> 方法得到一个迭代器，并调用它的 next 方法，循环判断是否迭代结束，否则取出结果的 value 属性值，执行我们写在 <code>for...of</code> 内部的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 比如：</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> obj) &#123;
    <span class="hljs-built_in">console</span>.log(item) <span class="hljs-comment">// 遍历打印每一项</span>
&#125;

<span class="hljs-comment">// 大概原理：</span>
<span class="hljs-keyword">const</span> iterator = obj[<span class="hljs-built_in">Symbol</span>.iterator]() <span class="hljs-comment">// 得到迭代器</span>
<span class="hljs-keyword">let</span> result = iterator.next()
<span class="hljs-keyword">while</span> (!result.done) &#123;
    <span class="hljs-keyword">const</span> item = result.value
    
    <span class="hljs-built_in">console</span>.log(item) <span class="hljs-comment">// 我们写的打印每一项的代码</span>
    
    result = iterator.next()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">生成器</h2>
<h3 data-id="heading-2">generator</h3>
<p>由构造函数 <code>Generator</code> 创建的对象，该对象是一个迭代器，同时又是一个可迭代对象（满足上面的可迭代协议）</p>
<p><strong>伪代码</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> generator = <span class="hljs-keyword">new</span> Generator()
generator.next() <span class="hljs-comment">// 拥有 next 方法</span>
generator[<span class="hljs-built_in">Symbol</span>.iterator] <span class="hljs-comment">// Function 可迭代</span>

<span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> generator) &#123;
    <span class="hljs-comment">// 可迭代对象，可被 for...of 循环</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>Generator</code> 函数是 JS 引擎内部使用的构造函数，不提供给开发者</strong></p>
<h3 data-id="heading-3">generator function</h3>
<p>生成器函数（生成器创建函数），用于创建一个生成器。语法上为 <code>function*</code> 来声明函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">createGenerator</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// other code...</span>
&#125;
<span class="hljs-comment">// 或是</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">createGenerator</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// other code...</span>
&#125;

<span class="hljs-keyword">const</span> generator = createGenerator() <span class="hljs-comment">// 得到一个生成器</span>

<span class="hljs-comment">// 所以：</span>
generator.next <span class="hljs-comment">// => native code Function</span>
generator[<span class="hljs-built_in">Symbol</span>.iterator] <span class="hljs-comment">// => native code Function</span>

generator.next === generator[<span class="hljs-built_in">Symbol</span>.iterator]().next <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">生成器函数的特点</h3>
<ol>
<li>
<p>生成器函数调用，不会执行函数体中的函数体，而是返回一个生成器（因为生成器函数内部函数体的执行，受返回的生成器控制）</p>
</li>
<li>
<p>每当调用了返回的生成器的 <code>next</code> 方法，生成器函数的函数体 会从上一次 <code>yield</code> 语句的位置（或函数体开始的位置）运行到下一个 <code>yield</code> 语句的位置（或函数结尾）</p>
<blockquote>
<p><code>yield</code> 关键字只能在生成器函数中使用，它表示暂停函数内部代码的执行，并返回一个当前迭代的数据；<br>
若无下一个 <code>yield</code>，next 方法返回对象的 done 则会置为 true</p>
</blockquote>
</li>
<li>
<p><code>yield</code> 关键字后表达式的结果会作为 <code>next 方法</code> 返回对象的 <code>value 值</code></p>
</li>
<li>
<p>生成器函数最后的返回值 <code>return "any data..."</code> 会作为迭代器首次迭代结束时的 <code>value</code> 值（done 初次为 true 时），后续再调用 next 方法，返回结果恒为 <code>&#123;value: undefined, done: true&#125;</code></p>
</li>
<li>
<p>生成器调用 <code>next</code> 方法的时候，可以传递参数，这个参数会作为生成器函数函数体上一次 <code>yield</code> 表达式的值（生成器第一次调用 next 方法传递参数无意义，直接被忽略），如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">createGenerator</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'function start...'</span>)
    <span class="hljs-keyword">let</span> res = <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>
    <span class="hljs-comment">// 第一次迭代 <next() 调用> 卡在 yield 语句，未完成赋值操作</span>
    <span class="hljs-comment">// 第二次迭代新传的参数值会赋给 res 变量（不传则为 undefined）</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger - 1'</span>, res)
    res = <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger - 2'</span>, res)
    res = <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger - 3'</span>, res)
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">desc</span>: <span class="hljs-string">'function end...'</span>
    &#125;
&#125;
<span class="hljs-keyword">const</span> generator = createGenerator() <span class="hljs-comment">// 得到生成器</span>
generator.next(<span class="hljs-number">111</span>)
<span class="hljs-comment">/*
print: ‘function start...’
returns: &#123; value: 1, done: false &#125;
*/</span>

generator.next(<span class="hljs-number">222</span>)
<span class="hljs-comment">/*
print: ‘logger - 1’ 222
returns: &#123; value: 2, done: false &#125;
*/</span>

generator.next()
<span class="hljs-comment">/*
print: ‘logger - 2’ undefined
returns: &#123; value: 3, done: false &#125;
*/</span>

generator.next(<span class="hljs-number">444</span>)
<span class="hljs-comment">/*
print: ‘logger - 3’ 444
returns: &#123;
    value: &#123;
        desc: 'function end...'
    &#125;,
    done: true
&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，在迭代过程中，下次迭代需要上次迭代返回的结果，就可以这样处理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 以上面的 createGenerator 函数为例</span>
<span class="hljs-keyword">const</span> generator = createGenerator() <span class="hljs-comment">// 得到生成器</span>
<span class="hljs-keyword">let</span> result = generator.next() <span class="hljs-comment">// 初次调用才会有返回值</span>
<span class="hljs-keyword">while</span> (!result.done) &#123;
    <span class="hljs-comment">// 未迭代结束，上次迭代的返回结果传递给下一次迭代</span>
    result = generator.next(result.value)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 ES7 <code>async</code>、<code>await</code> 出现之前，我们需要 <code>pro.then() => .then => .then</code> 去进行一系列的异步操作，那么我们也可以借助生成器去完成每一步的操作：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 模拟数据请求</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getData</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            resolve(&#123;
                <span class="hljs-attr">name</span>: <span class="hljs-string">'suressk'</span>,
                <span class="hljs-attr">age</span>: <span class="hljs-number">25</span>,
                <span class="hljs-attr">province</span>: <span class="hljs-string">'Hubei'</span>
            &#125;)
        &#125;, <span class="hljs-number">2000</span>)
    &#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">task</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'get data...'</span>)
    <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">yield</span> getData() <span class="hljs-comment">// value => Promise</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'got data: '</span>, data)
&#125;

<span class="hljs-keyword">const</span> generator = task()
<span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">value</span>: pro &#125; = generator.next()
<span class="hljs-comment">// print: 'get data...'</span>

<span class="hljs-comment">// 2 seconds later</span>
pro.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> generator.next(data))
<span class="hljs-comment">// print: 'got data: ' &#123; name: 'suressk', ... &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 封装一个 生成器任务的运行函数：</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span>(<span class="hljs-params">generatorFunc</span>) </span>&#123;
    <span class="hljs-keyword">const</span> generator = generatorFunc() <span class="hljs-comment">// 得到生成器</span>
    next()

    <span class="hljs-comment">/**
    * 封装 generator 的 next 方法
    * 调用则进行下一次迭代
    */</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params">nextVal</span>) </span>&#123;
        <span class="hljs-keyword">const</span> &#123; value, done &#125; = generator.next(nextVal)
        <span class="hljs-keyword">if</span> (done) <span class="hljs-keyword">return</span> <span class="hljs-comment">// 迭代结束</span>
        <span class="hljs-keyword">if</span> (isPromise(value)) &#123;
            value.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> next(data))
        &#125; <span class="hljs-keyword">else</span> &#123;
            next(value)
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// 辅助函数，判定 obj 是不是 Promise</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isPromise</span>(<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-keyword">return</span> !!obj &&
        (<span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">'object'</span> || <span class="hljs-keyword">typeof</span> obj === <span class="hljs-string">'function'</span>) &&
        <span class="hljs-keyword">typeof</span> obj.then === <span class="hljs-string">'function'</span>
&#125;

<span class="hljs-comment">// 上面代码的 task 生成器函数则可以直接调用</span>
run(task) <span class="hljs-comment">// 如果 task 内部有多步 yield 截断的异步方法一样可以运行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>生成器带有一个 <code>throw 方法</code>，该方法与 next 的效果相同，唯一的区别在于：next 方法传递的参数会被返回成一个正常的值；throw 方法传递的参数是一个错误对象，而且会将此迭代器状态置为 <code>迭代结束</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">generatorFunc</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'function start...'</span>)
    <span class="hljs-keyword">let</span> res = <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger - 1'</span>, res)
    res = <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger - 2'</span>, res)
    res = <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'logger - 3'</span>, res)
    <span class="hljs-keyword">return</span> <span class="hljs-string">'function end...'</span>
&#125;

<span class="hljs-keyword">const</span> generator = generatorFunc()
generator.next() <span class="hljs-comment">// 执行到 yield 1 语句停止</span>
<span class="hljs-comment">/**
* print: 'function start...'
* returns: &#123; value: 1, done: false &#125;
*/</span>
<span class="hljs-comment">// 若传递一个错误对象</span>
generator.next(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'报错啦～'</span>)) <span class="hljs-comment">// 执行到 yield 2 语句停止</span>
<span class="hljs-comment">/**
* print: 'logger - 1' [错误对象('报错啦～')]
* returns: &#123; value: 2, done: false &#125;
*/</span>
generator.throw(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'报错啦～'</span>)) <span class="hljs-comment">// 抛出错误，迭代结束</span>
<span class="hljs-comment">/**
* print: [错误对象('报错啦～')]
* returns: nothing...
*/</span>
<span class="hljs-comment">// 后续再调用 next() ➡️ 返回 &#123;value: undefined, done: true&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>生成器带有一个 <code>return 方法</code>，用于直接结束生成器函数，它可以接受一个参数，作为调用它得到返回值对象的 value 属性 (不传则为 undefined)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 借用上面的生成器函数 generatorFunc</span>
<span class="hljs-keyword">const</span> generator = generatorFunc()

generator.next() <span class="hljs-comment">// 执行到 yield 1 语句停止</span>
generator.return() <span class="hljs-comment">// 迭代结束</span>
<span class="hljs-comment">/**
* returns: &#123;value: undefined, done: true&#125;
*/</span>
generator.return(<span class="hljs-string">'abc'</span>)
<span class="hljs-comment">/**
* returns: &#123;value: 'abc', done: true&#125;
*/</span>
<span class="hljs-comment">// 继续调用 return 方法</span>
generator.return(<span class="hljs-string">'上面已经提前迭代结束了吖～'</span>)
<span class="hljs-comment">/**
* returns: &#123;value: '上面已经提前迭代结束了吖～', done: true&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>若需要在生成器内部调用其他生成器，若直接调用，则只是在调用的位置创建了一个生成器对象；若使用 <code>yield 加 *</code> 号调用，则会进入其生成器内部逐步执行</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">g1</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'g1 start...'</span>)
    <span class="hljs-keyword">let</span> res = <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'g1 logger - 1'</span>, res)
    res = <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'g1 logger - 2'</span>, res)
    res = <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'g1 logger - 3'</span>, res)
    <span class="hljs-keyword">return</span> <span class="hljs-string">'g1 end...'</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">g2</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'g2 start...'</span>)
    <span class="hljs-keyword">let</span> res = <span class="hljs-keyword">yield</span> <span class="hljs-number">4</span>
    <span class="hljs-comment">// 直接调用另一个生成器函数，这里只是得到一个生成器</span>
    <span class="hljs-comment">// 相当于直接写了个对象在这里，无实际效果</span>
    g1()
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'g2 logger - 1'</span>, res)
    res = <span class="hljs-keyword">yield</span> <span class="hljs-number">5</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'g2 logger - 2'</span>, res)
    res = <span class="hljs-keyword">yield</span> <span class="hljs-number">6</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'g2 logger - 3'</span>, res)
    <span class="hljs-keyword">return</span> <span class="hljs-string">'g2 end...'</span>
&#125;

<span class="hljs-keyword">const</span> g = g2()
g.next() <span class="hljs-comment">// 后续调用 next，表现上看相当于 g1() 语句被直接被忽略</span>
<span class="hljs-comment">// ...</span>
g.next() <span class="hljs-comment">// 后续调用 next，表现上看相当于 g1() 语句被直接被忽略</span>

<span class="hljs-comment">// 若在 g2 函数内部这样调用 yield* g1()</span>
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">g2</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'g2 start...'</span>)
    <span class="hljs-keyword">let</span> res = <span class="hljs-keyword">yield</span> <span class="hljs-number">4</span>
    <span class="hljs-comment">// 如果这样调用，运行到这一步时会进入此生成器函数内部</span>
    <span class="hljs-comment">// 去依次执行 g1 函数具体的代码</span>
    res = <span class="hljs-keyword">yield</span>* g1()
    <span class="hljs-comment">// g1 运行结束，这里 res 的结果为 g1 函数的返回值</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'g2 logger - 1'</span>, res)
    res = <span class="hljs-keyword">yield</span> <span class="hljs-number">5</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'g2 logger - 2'</span>, res)
    res = <span class="hljs-keyword">yield</span> <span class="hljs-number">6</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'g2 logger - 3'</span>, res)
    <span class="hljs-keyword">return</span> <span class="hljs-string">'g2 end...'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>至此，迭代器与生成器的相关内容及注意点就写到这里了，这些内容又多又绕的...</p></div>  
</div>
            