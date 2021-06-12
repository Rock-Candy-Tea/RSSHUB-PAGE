
---
title: 'Set与Map，它们你都了解吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8588'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 00:24:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=8588'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与更文挑战的第12天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557?utm_campaign=30day&utm_medium=Ccenter&utm_source=20210528" target="_blank">更文挑战</a> !</p>
<h2 data-id="heading-0">👽 概论</h2>
<p>提起JS中的数据类型，相信大家很容易就能联想到Number、String、Boolean、Object等等；没错，以上都属于JS中的两大数据类型。除此之外，JS中还有很多的内置对象。像大家耳熟能详的Array、Math、Function等，也有很多我们不怎么常用的，比如Set、Map、WeakSet、WeakMap。这些对象虽不常用，但也并非毫无用处，一起来看！</p>
<h2 data-id="heading-1">👽 Set</h2>
<h3 data-id="heading-2">👻 基本介绍</h3>
<p>Set其实与Aaary极为相似，也是一种有序的引用对象。其与Array的最大区别在于Set内的值不可重复，而Array则无此限制。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> myArray = [<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">2</span>]

<span class="hljs-keyword">const</span> mySet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(myArray)
<span class="hljs-built_in">console</span>.log(mySet2) <span class="hljs-comment">//输出 Set(2) &#123;1,2&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">👻 常用API</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//获取Set长度</span>
mySet.size()
<span class="hljs-comment">//向Set中增加值</span>
mySet.add(<span class="hljs-number">3</span>)
<span class="hljs-comment">//从Set中删除值</span>
mySet.delete(<span class="hljs-number">3</span>)
<span class="hljs-comment">//遍历Set</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> mySet)&#123;
 <span class="hljs-built_in">console</span>.log(item)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">👻 使用技巧</h3>
<p>既然Set有内部值唯一的特性，name用来去重再也合适不过了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//数组去重</span>
<span class="hljs-keyword">let</span> myArray = [<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">2</span>]

myArray = <span class="hljs-built_in">Array</span>.from(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(myArray))
<span class="hljs-built_in">console</span>.log(myArray) <span class="hljs-comment">//输出 [1,2]</span>

<span class="hljs-comment">//字符串去重</span>
<span class="hljs-keyword">let</span> myStr = <span class="hljs-string">'oovbyyu'</span>

myStr = <span class="hljs-built_in">Array</span>.from(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(myStr)).join(<span class="hljs-string">''</span>)
<span class="hljs-built_in">console</span>.log(myStr) <span class="hljs-comment">//输出"ovbyu"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">👽 Map</h2>
<h3 data-id="heading-6">👻 基本介绍</h3>
<p>Map与Object很像，他们都是键值对。主要的区别在于：
1. Map内部的值是有序的（与插入时的顺序一致）；
2. Map的键类型不受限制，可以是任意类型（包括函数，对象等等）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
<span class="hljs-keyword">let</span> arrayA = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>]

myMap.set(arrayA,<span class="hljs-number">2</span>)

<span class="hljs-built_in">console</span>.log(myMap) <span class="hljs-comment">//输出 Map(1) &#123;Array(2) => 2&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">👻 常用API</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//获取Map长度</span>
myMap.size
<span class="hljs-comment">//向Map中增加值</span>
myMap.set(<span class="hljs-string">'mapKey'</span>,<span class="hljs-string">'mapVal'</span>)
<span class="hljs-comment">//从Map中删除值</span>
myMap.delete(<span class="hljs-string">'mapKey'</span>)<span class="hljs-comment">//成功则返回true，失败则返回false</span>
<span class="hljs-comment">//获取Map中某键的值</span>
myMap.get(arrayA)
<span class="hljs-comment">//遍历Map</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> myMap)&#123;
 <span class="hljs-built_in">console</span>.log(item)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">👻 使用技巧</h3>
<p>Map内部值有序这一特性极为重要，如果存在需要在遍历Object时，确保遍历顺序一致，此时便可以使用Map。</p>
<h2 data-id="heading-9">👽 结语</h2>
<p>实践出真知，大家多多尝试~</p></div>  
</div>
            