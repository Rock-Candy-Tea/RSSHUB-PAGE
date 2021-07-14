
---
title: '快乐Js之数组去重'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1788'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 01:51:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=1788'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">快乐Js之数组去重</h1>
<p>我们在写业务代码的时候，经常会碰到给复杂数组去重的需求，那么如何帅气的实现数组去重呢？请你看完这篇文。</p>
<h2 data-id="heading-1">简单数组去重</h2>
<p>饭要一口一口吃，先来看一个简单数组去重吧，鉴于网上数组去重的方法很多，这里只介绍几个我喜欢的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 一个简单数组，包含的每一项都是简单类型的值</span>
<span class="hljs-keyword">const</span> list = [<span class="hljs-number">11</span>,<span class="hljs-number">11</span>,<span class="hljs-number">33</span>,<span class="hljs-number">2</span>, <span class="hljs-string">'true'</span>, <span class="hljs-literal">true</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, <span class="hljs-literal">false</span>, <span class="hljs-string">'false'</span>, <span class="hljs-literal">false</span>, <span class="hljs-literal">NaN</span>, <span class="hljs-literal">NaN</span>]

<span class="hljs-comment">// 利用set数据结构去重的特性，大家用的最多的应该就是这种吧</span>
<span class="hljs-keyword">const</span> duplicateRemoval = <span class="hljs-function"><span class="hljs-params">list</span> =></span> <span class="hljs-built_in">Array</span>.from(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(list))

<span class="hljs-comment">// for循环去重</span>
<span class="hljs-keyword">const</span> duplicateRemoval = <span class="hljs-function"><span class="hljs-params">list</span> =></span> &#123;
  <span class="hljs-keyword">const</span> arr = []
  list.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> !arr.includes(item) && arr.push(item))
  <span class="hljs-keyword">return</span> arr
&#125;

<span class="hljs-comment">// filter 函数去重</span>
<span class="hljs-keyword">const</span> duplicateRemoval = <span class="hljs-function"><span class="hljs-params">list</span> =></span> &#123;
  <span class="hljs-keyword">return</span> list.filter(<span class="hljs-function">(<span class="hljs-params">item, index, arr</span>) =></span> &#123;
    <span class="hljs-comment">//当前元素，在原始数组中的第一个索引==当前索引值，否则返回当前元素</span>
    <span class="hljs-keyword">return</span> arr.indexOf(item) === index;
  &#125;);
&#125;
<span class="hljs-comment">// 让我们精简一下上面这个函数，很好，非常的完美</span>
<span class="hljs-keyword">const</span> duplicateRemoval = <span class="hljs-function"><span class="hljs-params">list</span> =></span> list.filter(<span class="hljs-function">(<span class="hljs-params">item, index, arr</span>) =></span> arr.indexOf(item) === index)

<span class="hljs-comment">// 使用reduce函数去重</span>
<span class="hljs-keyword">const</span> duplicateRemoval = <span class="hljs-function"><span class="hljs-params">list</span> =></span> list.reduce(<span class="hljs-function">(<span class="hljs-params">accumulator, currentValue</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (accumulator.indexOf(currentValue) === -<span class="hljs-number">1</span>) &#123;
    accumulator.push(currentValue)
  &#125;
  <span class="hljs-keyword">return</span> accumulator
&#125;, [])
<span class="hljs-comment">// 好的，按照惯例精简一下</span>
<span class="hljs-keyword">const</span> duplicateRemoval = <span class="hljs-function"><span class="hljs-params">list</span> =></span> list.reduce(<span class="hljs-function">(<span class="hljs-params">acc, cur</span>) =></span> (!acc.includes(cur) && acc.push(cur), acc),[])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单数组去重的写法太多啦，随便一搜就是十种八种的，鉴于我们的主题并不是简单数组去重，所以暂时就写到这吧～</p>
<h2 data-id="heading-2">复杂数组按条件去重</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 一个我们经常会碰到的对象数组，我们需要按照某个特定条件去除重复项</span>
<span class="hljs-keyword">const</span> list = [&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'lily1'</span>, <span class="hljs-attr">code</span>: <span class="hljs-string">'133'</span>&#125;,&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'lily1'</span>, <span class="hljs-attr">code</span>: <span class="hljs-string">'323'</span>&#125;,&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'lily2'</span>, <span class="hljs-attr">code</span>: <span class="hljs-string">'333'</span>&#125;,&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'lily3'</span>, <span class="hljs-attr">code</span>: <span class="hljs-string">'333'</span>&#125;,&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'lily4'</span>, <span class="hljs-attr">code</span>: <span class="hljs-string">'332'</span>&#125;,&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'lily4'</span>, <span class="hljs-attr">code</span>: <span class="hljs-string">'333'</span>&#125;]

<span class="hljs-comment">// 由于复杂数据结构的特性，我们无法再简单的使用set进行去重了</span>

<span class="hljs-comment">// 利用filter函数去重</span>
<span class="hljs-keyword">const</span> duplicateRemovalByFilter = <span class="hljs-function">(<span class="hljs-params">list, key</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> map = &#123;&#125;
  <span class="hljs-keyword">return</span> list.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-keyword">let</span> value = item[key]
    <span class="hljs-comment">// 还是比较好理解的，写一个map来记录筛选项出现的次数，然后当次数为1时返回true,这样筛选出来的就是在数组中只出现过一次的项了</span>
    <span class="hljs-keyword">if</span>(!map[value]) &#123;
      map[value] = <span class="hljs-number">1</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      map[value] += <span class="hljs-number">1</span>
    &#125;
    <span class="hljs-keyword">return</span> map[value] === <span class="hljs-number">1</span>
  &#125;)
&#125;
<span class="hljs-comment">// 按照惯例精简一下</span>
<span class="hljs-keyword">const</span> duplicateRemovalByFilter = <span class="hljs-function">(<span class="hljs-params">list, key</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> map = &#123;&#125;
  <span class="hljs-comment">// 小知识 赋值语句的返回值等于被赋予的那个值</span>
  <span class="hljs-comment">// let a; // 返回undefined</span>
  <span class="hljs-comment">// a = 688; // 返回688</span>
  <span class="hljs-keyword">return</span> list.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> !map[item[key]] && (map[item[key]] = <span class="hljs-literal">true</span>))
&#125;

<span class="hljs-comment">// 利用reduce函数去重</span>
<span class="hljs-keyword">const</span> duplicateRemovalByReduce = <span class="hljs-function">(<span class="hljs-params">list,key</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> obj = list.reduce(<span class="hljs-function">(<span class="hljs-params">pre, cur</span>) =></span> &#123;
    <span class="hljs-comment">// 判断一下 累加器中对应的值是否为undefined，是的话赋上当前的值，不是的话，就保持现状</span>
    pre[cur[key]] = pre[cur[key]] || cur
    <span class="hljs-keyword">return</span> pre
  &#125;, &#123;&#125;)
  <span class="hljs-comment">// 返回obj中可迭代的值数组</span>
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.values(obj)
&#125;
<span class="hljs-comment">// 同样，我们的精简环节来了</span>
<span class="hljs-keyword">const</span> duplicateRemovalByReduce = <span class="hljs-function">(<span class="hljs-params">list,key</span>) =></span> &#123;
  <span class="hljs-comment">// 一位朋友在vue源码中看到的逗号运算符的应用，虽然比较难理解，但是真帅！</span>
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.values(list.reduce(<span class="hljs-function">(<span class="hljs-params">pre, cur</span>) =></span> (pre[cur[key]] = pre[cur[key]] || cur, pre), &#123;&#125;))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于我比较懒，复杂数组按条件去重就写这两样了。还有更多的写法，欢迎交流～</p>
<h2 data-id="heading-3">一个值得注意的点</h2>
<p>精简写法虽然代码量少，看起来非常舒服。但是如果不写注释突然在你的某个业务功能函数里来上这么一段，分分钟能气死你的同事和过了很久之后再看代码的自己。所以我有两点建议：</p>
<ol>
<li>一个函数只做一件事，去重函数就只用来去重，把去重函数单独抽出来写成独立的函数，而不是混在业务逻辑里。</li>
<li>多写注释</li>
</ol>
<h2 data-id="heading-4">感谢阅读，mua～</h2></div>  
</div>
            