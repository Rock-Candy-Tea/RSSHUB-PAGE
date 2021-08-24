
---
title: '一道统计题到reduce方法的学习'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8271'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 19:28:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=8271'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>题目：请输出当前页面出现最频繁的3个html标签及出现的次数！</p>
</blockquote>
<h2 data-id="heading-0">引出题目</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 我的解答</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'标签的数量： '</span>
+ <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([...document.getElementsByTagName(<span class="hljs-string">'*'</span>)].map(<span class="hljs-function"><span class="hljs-params">tag</span> =></span> tag.tagName)).size)
<span class="hljs-comment">/**
* num 统计的html数量
* arr 需要被统计的对象数组
*/</span>
<span class="hljs-keyword">let</span> htmlArr = [...document.getElementsByTagName(<span class="hljs-string">'*'</span>)].map(<span class="hljs-function"><span class="hljs-params">tag</span> =></span> tag.tagName)
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getHtmlInfo</span> (<span class="hljs-params">arr, num</span>) </span>&#123;
    <span class="hljs-keyword">let</span> len = arr.length
    <span class="hljs-keyword">let</span> obj = &#123;&#125;
    <span class="hljs-keyword">let</span> newArr = []
    <span class="hljs-keyword">let</span> tag
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
        tag = arr[i]
        <span class="hljs-keyword">if</span> (obj[tag]) &#123;
            obj[tag]++
        &#125; <span class="hljs-keyword">else</span> &#123;
            obj[tag] = <span class="hljs-number">1</span>
        &#125;
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> obj) &#123;
        newArr.push(&#123;
            <span class="hljs-attr">tag</span>: key,
            <span class="hljs-attr">count</span>: obj[key]
        &#125;)
    &#125;
    <span class="hljs-comment">// 降序</span>
    newArr.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> b.count - a.count
    &#125;)
    <span class="hljs-keyword">let</span> newNum = num || newArr.length
    <span class="hljs-keyword">return</span> newArr.slice(<span class="hljs-number">0</span>, newNum)
&#125;
<span class="hljs-keyword">let</span> newHtmlArr = getHtmlInfo(htmlArr, <span class="hljs-number">3</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`出现最多的是<span class="hljs-subst">$&#123;newHtmlArr[<span class="hljs-number">0</span>].tag&#125;</span>标签，共<span class="hljs-subst">$&#123;newHtmlArr[<span class="hljs-number">0</span>].count&#125;</span>次`</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`出现次数第二的是<span class="hljs-subst">$&#123;newHtmlArr[<span class="hljs-number">1</span>].tag&#125;</span>标签，共<span class="hljs-subst">$&#123;newHtmlArr[<span class="hljs-number">1</span>].count&#125;</span>次`</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`出现次数第三的是<span class="hljs-subst">$&#123;newHtmlArr[<span class="hljs-number">2</span>].tag&#125;</span>标签，共<span class="hljs-subst">$&#123;newHtmlArr[<span class="hljs-number">2</span>].count&#125;</span>次`</span>)
<span class="hljs-comment">// 比较low</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 大佬的解答</span>
<span class="hljs-built_in">Object</span>.entries([...document.querySelectorAll(<span class="hljs-string">"*"</span>)].map(<span class="hljs-function"><span class="hljs-params">tag</span>=></span>tag.tagName).reduce(<span class="hljs-function">(<span class="hljs-params">ret, i</span>)=></span>&#123;
  ret[i] = (ret[i] || <span class="hljs-number">0</span>) + <span class="hljs-number">1</span>;
  <span class="hljs-keyword">return</span> ret;
&#125;, &#123;&#125;)).sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>)=></span>(b[<span class="hljs-number">1</span>] - a[<span class="hljs-number">1</span>])).slice(<span class="hljs-number">0</span>, <span class="hljs-number">3</span>)
.map(<span class="hljs-function"><span class="hljs-params">a</span>=></span>(<span class="hljs-string">`<span class="hljs-subst">$&#123;a[<span class="hljs-number">0</span>]&#125;</span>: <span class="hljs-subst">$&#123;a[<span class="hljs-number">1</span>]&#125;</span>次`</span>)).join(<span class="hljs-string">', '</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Freduce" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce" ref="nofollow noopener noreferrer">Array.prototype.reduce()</a> 该方法对数组中的每个元素执行一个由您提供的<strong>reducer</strong>函数(升序执行)，将其结果汇总为单个返回值。 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Freduce" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce" ref="nofollow noopener noreferrer">MDN链接</a></p>
</blockquote>
<h2 data-id="heading-1">语法</h2>
<p><code>arr.reduce(callback(accumulator, currentValue[, currentIndex[, sourceArray]])[, initialValue])</code></p>
<ul>
<li><code>accumulator</code> 累计器累计回调的返回值</li>
<li><code>currentValue</code> 当前值</li>
<li><code>currentIndex</code> 可选当前索引</li>
<li><code>sourceArray</code> 可选源数组</li>
</ul>
<h3 data-id="heading-2">callback需要注意的点</h3>
<ul>
<li><code>accumulator</code> 默认值为<code>initialValue</code>,此时<code>currentValue</code>为数组的0号索引的值，<code>currentIndex</code>为0；如果<code>initialValue</code>没有提供，则<code>initialValue</code>取数组的0号索引位置的值,<code>currentValue</code>取1号索引的值，<code>currentIndex</code>为1。</li>
<li>如果数组为空数组且没有提供<code>initialValue</code>，则会报类型错误。</li>
<li>如果数组只有一个元素（任意位置），且没有提供<code>initialValue</code>，或提供了<code>initialValue</code>但数组为空，则callback不会被执行，该元素会被作为返回值。</li>
<li>值会被累计到<code>accumulator</code>，并最终与最后索引的值处理后合并为单一值返回。</li>
<li>建议，为安全着想，每次提供<code>initialValue</code>。</li>
</ul>
<h2 data-id="heading-3">使用场景</h2>
<h3 data-id="heading-4">计算数组中所有值的和</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> sum = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>].reduce(<span class="hljs-function">(<span class="hljs-params">acc, cur</span>) =></span> acc + cur, <span class="hljs-number">0</span>)
<span class="hljs-built_in">console</span>.log(sum) <span class="hljs-comment">// 10</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">累加对象数组中的值</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> sum = [&#123;<span class="hljs-attr">x</span>: <span class="hljs-number">1</span>&#125;, &#123;<span class="hljs-attr">x</span>: <span class="hljs-number">2</span>&#125;, &#123;<span class="hljs-attr">x</span>: <span class="hljs-number">3</span>&#125;].reduce(<span class="hljs-function">(<span class="hljs-params">acc, cur</span>) =></span> acc + cur.x, <span class="hljs-number">0</span>)
<span class="hljs-built_in">console</span>.log(sum) <span class="hljs-comment">// 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">将二维数组转化为一维数组</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [[<span class="hljs-number">0</span>, <span class="hljs-number">1</span>], [<span class="hljs-number">2</span>, <span class="hljs-number">3</span>], [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>]].reduce(<span class="hljs-function">(<span class="hljs-params">acc, cur</span>) =></span> acc.concat(cur), [])
<span class="hljs-built_in">console</span>.log(arr) <span class="hljs-comment">// [0, 1, 2, 3, 4, 5]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">计算数组中每个元素出现的次数</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">const</span> htmls = [<span class="hljs-string">'html'</span>, <span class="hljs-string">'span'</span>, <span class="hljs-string">'body'</span>, <span class="hljs-string">'div'</span>, <span class="hljs-string">'div'</span>]
 <span class="hljs-keyword">const</span> countedHtmls = htmls.reduce(<span class="hljs-function">(<span class="hljs-params">acc, cur</span>) =></span> &#123;
   <span class="hljs-keyword">if</span> (cur <span class="hljs-keyword">in</span> acc) &#123;
     acc[cur]++
   &#125; <span class="hljs-keyword">else</span> &#123;
     acc[cur] = <span class="hljs-number">1</span>
   &#125;
   <span class="hljs-keyword">return</span> acc
 &#125;, &#123;&#125;)
 <span class="hljs-built_in">console</span>.log(countedHtmls) <span class="hljs-comment">// &#123; html: 1, span: 1, body: 1, div: 2 &#125;</span>
 <span class="hljs-comment">// 计算当前页面出现次数最多的3个标签</span>
 <span class="hljs-built_in">Object</span>.entries([...document.querySelectorAll(<span class="hljs-string">'*'</span>)].map(<span class="hljs-function"><span class="hljs-params">tag</span> =></span> tag.tagName).reduce(<span class="hljs-function">(<span class="hljs-params">acc,cur</span>) =></span> &#123;
    acc[cur] = (acc[cur] || <span class="hljs-number">0</span>) + <span class="hljs-number">1</span>
    <span class="hljs-keyword">return</span> acc
&#125;, &#123;&#125;)).sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> b[<span class="hljs-number">1</span>] - a[<span class="hljs-number">1</span>]).slice(<span class="hljs-number">0</span>, <span class="hljs-number">3</span>).map(<span class="hljs-function"><span class="hljs-params">a</span> =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;a[<span class="hljs-number">0</span>]&#125;</span>: <span class="hljs-subst">$&#123;a[<span class="hljs-number">1</span>]&#125;</span>次`</span>).join(<span class="hljs-string">', '</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">按属性对object分类</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'css'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
  &#125;,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Javascript'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>
  &#125;,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'html'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
  &#125;
]
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">groupBy</span> (<span class="hljs-params">arr, property</span>) </span>&#123;
  <span class="hljs-keyword">return</span> arr.reduce(<span class="hljs-function">(<span class="hljs-params">acc, cur</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> key = cur[property]
    <span class="hljs-keyword">if</span> (!acc[key]) &#123;
      acc[key] = []
    &#125;
    acc[key].push(cur)
    <span class="hljs-keyword">return</span> acc
  &#125;, &#123;&#125;)
&#125;
<span class="hljs-built_in">console</span>.log(groupBy(arr, <span class="hljs-string">'age'</span>))
<span class="hljs-comment">// &#123;</span>
<span class="hljs-comment">//   '18': [ &#123; name: 'css', age: 18 &#125;, &#123; name: 'html', age: 18 &#125; ],</span>
<span class="hljs-comment">//   '20': [ &#123; name: 'Javascript', age: 20 &#125; ]</span>
<span class="hljs-comment">// &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">合并对象数组中的数组</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> friends = [
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'javascript'</span>,
    <span class="hljs-attr">books</span>: [<span class="hljs-string">'es6入门'</span>, <span class="hljs-string">'javascript高级程序设计'</span>, <span class="hljs-string">'你不知道的javascript'</span>, <span class="hljs-string">'Dom编程艺术'</span>, <span class="hljs-string">'Javascript设计模式'</span>]
  &#125;,
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'css'</span>,
    <span class="hljs-attr">books</span>: [<span class="hljs-string">'css世界'</span>]
  &#125;
]
<span class="hljs-keyword">const</span> allBooks = friends.reduce(<span class="hljs-function">(<span class="hljs-params">acc, cur</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> [...acc, ...cur.books]
&#125;, [])
<span class="hljs-built_in">console</span>.log(allBooks)
<span class="hljs-comment">// [</span>
<span class="hljs-comment">//   'es6入门',</span>
<span class="hljs-comment">//   'javascript高级程序设计',</span>
<span class="hljs-comment">//   '你不知道的javascript',</span>
<span class="hljs-comment">//   'Dom编程艺术',</span>
<span class="hljs-comment">//   'Javascript设计模式',</span>
<span class="hljs-comment">//   'css世界'</span>
<span class="hljs-comment">// ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">数组去重</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">5</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">4</span>,<span class="hljs-number">4</span>,<span class="hljs-number">4</span>]
<span class="hljs-keyword">const</span> result = arr.sort().reduce(<span class="hljs-function">(<span class="hljs-params">acc, cur</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (!acc.includes(cur)) &#123;
    acc.push(cur)
  &#125;
  <span class="hljs-keyword">return</span> acc
&#125;, [])
<span class="hljs-built_in">console</span>.log(result)
<span class="hljs-comment">// [ 1, 2, 3, 4, 5 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">按顺序运行promise</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runPromiseInSequence</span>(<span class="hljs-params">arr, input</span>) </span>&#123;
  <span class="hljs-keyword">return</span> arr.reduce(<span class="hljs-function">(<span class="hljs-params">promiseChain, currentFunction</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> promiseChain.then(currentFunction)
  &#125;, <span class="hljs-built_in">Promise</span>.resolve(input))
&#125;
<span class="hljs-comment">// function runPromiseInSequence(arr, input) &#123;</span>
<span class="hljs-comment">//   return arr.reduce((promiseChain, currentFunction) => &#123;</span>
<span class="hljs-comment">//     return promiseChain.then(currentFunction)</span>
<span class="hljs-comment">//   &#125;, new Promise(resolve => &#123;</span>
<span class="hljs-comment">//     resolve(input)</span>
<span class="hljs-comment">//   &#125;))</span>
<span class="hljs-comment">// &#125;</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">p1</span> (<span class="hljs-params">a</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(a * <span class="hljs-number">5</span>)
  &#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">p2</span> (<span class="hljs-params">a</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(a * <span class="hljs-number">2</span>)
  &#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f3</span> (<span class="hljs-params">a</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a * <span class="hljs-number">3</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">p4</span> (<span class="hljs-params">a</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(a * <span class="hljs-number">4</span>)
  &#125;)
&#125;
<span class="hljs-keyword">const</span> promiseArr = [p1, p2, f3, p4]
runPromiseInSequence(promiseArr, <span class="hljs-number">10</span>).then(<span class="hljs-built_in">console</span>.log)
<span class="hljs-comment">// 1200</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">管道机制/功能型函数管道</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 管道机制/功能型函数管道</span>
<span class="hljs-comment">// 定义：前一个函数的输出是后一个函数的输入</span>
<span class="hljs-comment">// const pipeLine = (...funcs) => input => &#123;</span>
<span class="hljs-comment">//   return funcs.reduce((acc, curFun) => curFun(acc), input)</span>
<span class="hljs-comment">// &#125;</span>
<span class="hljs-keyword">const</span> pipeLine = <span class="hljs-function">(<span class="hljs-params">...funcs</span>) =></span> <span class="hljs-function"><span class="hljs-params">input</span> =></span> funcs.reduce(<span class="hljs-function">(<span class="hljs-params">acc, curFn</span>) =></span> curFn(acc), input)

<span class="hljs-keyword">const</span> fun1 = <span class="hljs-function"><span class="hljs-params">num</span> =></span> num + num
<span class="hljs-keyword">const</span> fun2 = <span class="hljs-function"><span class="hljs-params">num</span> =></span> num * num
<span class="hljs-keyword">const</span> fun3 = <span class="hljs-function"><span class="hljs-params">num</span> =></span> num * <span class="hljs-number">10</span>

<span class="hljs-keyword">const</span> pipeResult = pipeLine(fun1, fun2, fun3)
<span class="hljs-built_in">console</span>.log(pipeResult(<span class="hljs-number">1</span>)) <span class="hljs-comment">// 40</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">实现map</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.prototype.mapUsingReduce) &#123;
  <span class="hljs-built_in">Array</span>.prototype.mapUsingReduce = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">callback, thisArg</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.reduce(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">mappedArray, currentValue, index, orignArray</span>) </span>&#123;
      mappedArray[index] = callback.call(thisArg, currentValue, index, orignArray)
      <span class="hljs-keyword">return</span> mappedArray
    &#125;, [])
  &#125;
&#125;
<span class="hljs-keyword">const</span> newArr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, , <span class="hljs-number">3</span>].mapUsingReduce(<span class="hljs-function">(<span class="hljs-params">currentValue, index, array</span>) =></span> currentValue + index + array.length)
<span class="hljs-built_in">console</span>.log(newArr)  <span class="hljs-comment">// [5, 7, , 10]</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            