
---
title: 'JS中的 if 语句、switch 语句与 && __'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3227'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 00:34:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=3227'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>最近在刷题过程中，遇到许多 if 语句可以改写成switch语句或&&运算符的。觉得很简洁，所以来综合总结一下。</p>
<h2 data-id="heading-0">if 语句</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">if</span> (ops[i] === <span class="hljs-string">"C"</span>) &#123;
      res.pop()
    &#125; <span class="hljs-keyword">else</span> 
    <span class="hljs-keyword">if</span> (ops[i] === <span class="hljs-string">"D"</span>) &#123;
      res.push(res[res.length-<span class="hljs-number">1</span>] * <span class="hljs-number">2</span>)
    &#125; <span class="hljs-keyword">else</span> 
    <span class="hljs-keyword">if</span> (ops[i] === <span class="hljs-string">"+"</span>) &#123;
      res.push(res[res.length - <span class="hljs-number">1</span>] + res[res.length -<span class="hljs-number">2</span>])
    &#125; <span class="hljs-keyword">else</span> 
    <span class="hljs-keyword">if</span> 
    (<span class="hljs-built_in">parseInt</span>(ops[i]) !== <span class="hljs-literal">NaN</span>) &#123;
      res.push(<span class="hljs-built_in">Math</span>.floor(ops[i]))
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>if 语句是最常见的写法，也是最为简单易懂的写法，但是代码太多，看着不是很清爽。可以改写成：</p>
<h2 data-id="heading-1">switch 语句</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">switch</span> (ops[i]) &#123;
  <span class="hljs-keyword">case</span> <span class="hljs-string">"C"</span>:
    res.pop()
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">case</span> <span class="hljs-string">"D"</span>:
    res.push(+res[res.length-<span class="hljs-number">1</span>] * <span class="hljs-number">2</span>)
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">case</span> <span class="hljs-string">"+"</span>:
    res.push(+res[res.length - <span class="hljs-number">1</span>] + +res[res.length -<span class="hljs-number">2</span>])
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">default</span>:
    res.push(+ops[i]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>switch 语句看起来清爽很多，但是在需要进行不等判断的情况下是无法实现的。因此可使用情况相对小一点。</p>
<h2 data-id="heading-2">&& || 语句</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript">(ops[i] === <span class="hljs-string">"C"</span> && res.pop()) || (ops[i] === <span class="hljs-string">"D"</span> && res.push(+res[res.length-<span class="hljs-number">1</span>] * <span class="hljs-number">2</span>)) || (ops[i] === <span class="hljs-string">"+"</span> && res.push(+res[res.length - <span class="hljs-number">1</span>] + +res[res.length -<span class="hljs-number">2</span>]) || (<span class="hljs-built_in">parseInt</span>(ops[i]) !== <span class="hljs-literal">NaN</span> && res.push(<span class="hljs-built_in">Math</span>.floor(ops[i]))))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只用一行代码就可以实现了。
&& || 语句，也称短路语句。即：如果 && 前面一个语句为 true，则这语句等于 && 后面的值（true / false）。如果 || 前面一个语句为 false，则这句语句等于 || 后面的值（true / false）。
一开始我的理解是，&& 约等于 if() ，|| 约等于else ，但 && || 运算符的本质是在进行与、或判断。
首先从左向右进行判断，如果 ops[i] === "C" 运行结果为 true，那就是 true && res.pop()，结果就是 res.pop() ，被判断为真。而后面接的又是 || 运算符，当前面被判断为真时就不会再向后进行运算。所以最后的结果就是 res.pop()。而如果运算结果为false，则 ops[i] === "C" && res.pop() 整个就是false，那么就会通过后面的 || 运算符 继续向后运算，向后面找。
因此这就给了人一种类似于 if…else 语句的错觉。其实这两种写法，只有最后的运算结果是一样的，但是运算的原理不同。
&& || 运算符写法，虽然非常的简洁，精炼。但是其中包含的逻辑却非常的复杂。一般不会大量的用来开发。维护性不佳。
下面这种情况例外：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> YAHOO = <span class="hljs-built_in">window</span>.YAHOO || &#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.name = name || <span class="hljs-string">'mama'</span>;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            