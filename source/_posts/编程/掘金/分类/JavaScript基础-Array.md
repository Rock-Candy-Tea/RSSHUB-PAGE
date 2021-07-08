
---
title: 'JavaScript基础-Array'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8270'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 22:36:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=8270'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与新手入门的第2篇文章</p>
<h2 data-id="heading-0">前言</h2>
<p>每天一题算法，生活都充实了！正当我开心的沉醉在算法中，突然发现<code>JavaScript</code>不支持真正的多维数组，只能使用数组的数组来模拟。让我感受到自己才疏学浅，于是乎，开始重温<code>Array</code>吧。</p>
<p>大致分为以下几类：</p>
<blockquote>
<p>数组的方法</p>
<p>稀疏数组</p>
<p>多维数组</p>
<p>类数组</p>
</blockquote>
<p>数组的方法这里就不多说了，直接参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array" ref="nofollow noopener noreferrer">MDN</a>，里面的帮助文档写的详细。</p>
<p>（数组的长度是0到2<sup>32</sup>-1之间的整数）</p>
<h2 data-id="heading-1">稀疏数组</h2>
<p>所谓稀疏数组，指的是元素没有连续索引的数组，<code>length</code>属性的值大于元素数，例如：[0,,2]。通俗的来讲就是数组中有间隙。</p>
<p>可以用Array()构造函数，或者给大于元素长度的索引赋值来创建<strong>稀疏数组</strong>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> sparseArr1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">10</span>); <span class="hljs-comment">//数组长度为10且没有元素</span>

<span class="hljs-keyword">var</span> sparseArr2 = [];
sparseArr2[<span class="hljs-number">9</span>] = <span class="hljs-number">0</span>; <span class="hljs-comment">//元素为0,数组的长度为10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以通过字面量来创建</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> sparseArr1 = [<span class="hljs-number">1</span>,,<span class="hljs-number">3</span>]; <span class="hljs-comment">//有两个元素,但数组长度为3</span>

<span class="hljs-keyword">var</span> sparseArr2 = [,]; <span class="hljs-comment">//没有元素,数组长度为1</span>
<span class="hljs-keyword">var</span> sparseArr2 = [,,]; <span class="hljs-comment">//没有元素,数组长度为2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">多维数组</h2>
<p>说到多维数组，不是很简单嘛，先来个二维数组：<code>[[1],[2]]</code>。深受Java的影响，为了申明一个二维数组的变量，于是我便大胆猜测<code>var arr = new [][];</code>然而，console里<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mrow><mi>U</mi><mi>n</mi><mi>c</mi><mi>a</mi><mi>u</mi><mi>g</mi><mi>h</mi><mi>t</mi><mi>S</mi><mi>y</mi><mi>n</mi><mi>t</mi><mi>a</mi><mi>x</mi><mi>E</mi><mi>r</mi><mi>r</mi><mi>o</mi><mi>r</mi><mo>:</mo><mi>U</mi><mi>n</mi><mi>e</mi><mi>x</mi><mi>p</mi><mi>e</mi><mi>c</mi><mi>t</mi><mi>e</mi><mi>d</mi><mi>t</mi><mi>o</mi><mi>k</mi><mi>e</mi><msup><mi>n</mi><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><msup><mo stretchy="false">]</mo><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;Uncaught SyntaxError: Unexpected token ']'&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="mord" style="color:red;"><span class="mord mathnormal" style="margin-right:0.10903em;color:red;">U</span><span class="mord mathnormal" style="color:red;">n</span><span class="mord mathnormal" style="color:red;">c</span><span class="mord mathnormal" style="color:red;">a</span><span class="mord mathnormal" style="color:red;">u</span><span class="mord mathnormal" style="margin-right:0.03588em;color:red;">g</span><span class="mord mathnormal" style="color:red;">h</span><span class="mord mathnormal" style="color:red;">t</span><span class="mord mathnormal" style="margin-right:0.05764em;color:red;">S</span><span class="mord mathnormal" style="margin-right:0.03588em;color:red;">y</span><span class="mord mathnormal" style="color:red;">n</span><span class="mord mathnormal" style="color:red;">t</span><span class="mord mathnormal" style="color:red;">a</span><span class="mord mathnormal" style="color:red;">x</span><span class="mord mathnormal" style="margin-right:0.05764em;color:red;">E</span><span class="mord mathnormal" style="margin-right:0.02778em;color:red;">r</span><span class="mord mathnormal" style="margin-right:0.02778em;color:red;">r</span><span class="mord mathnormal" style="color:red;">o</span><span class="mord mathnormal" style="margin-right:0.02778em;color:red;">r</span><span class="mspace" style="color:red;margin-right:0.2777777777777778em;"></span><span class="mrel" style="color:red;">:</span><span class="mspace" style="color:red;margin-right:0.2777777777777778em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;color:red;">U</span><span class="mord mathnormal" style="color:red;">n</span><span class="mord mathnormal" style="color:red;">e</span><span class="mord mathnormal" style="color:red;">x</span><span class="mord mathnormal" style="color:red;">p</span><span class="mord mathnormal" style="color:red;">e</span><span class="mord mathnormal" style="color:red;">c</span><span class="mord mathnormal" style="color:red;">t</span><span class="mord mathnormal" style="color:red;">e</span><span class="mord mathnormal" style="color:red;">d</span><span class="mord mathnormal" style="color:red;">t</span><span class="mord mathnormal" style="color:red;">o</span><span class="mord mathnormal" style="margin-right:0.03148em;color:red;">k</span><span class="mord mathnormal" style="color:red;">e</span><span class="mord" style="color:red;"><span class="mord mathnormal" style="color:red;">n</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight" style="color:red;"><span class="mord mtight" style="color:red;"><span class="mord mtight" style="color:red;">′</span></span></span></span></span></span></span></span></span><span class="mclose" style="color:red;"><span class="mclose" style="color:red;">]</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight" style="color:red;"><span class="mord mtight" style="color:red;"><span class="mord mtight" style="color:red;">′</span></span></span></span></span></span></span></span></span></span></span></span></span></span>亮闪闪的红色字体映入眼帘。</p>
<p>怎么回事呢，<code>JavaScript</code>不支持真正的多维数组，可以使用数组的数组来模拟。以下才是常规操作：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">5</span>);
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++)&#123;
    arr[i] = [<span class="hljs-number">1</span>];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先定义一个数组<code>arr</code>，遍历<code>arr</code>数组中每一项并且赋值为数组<code>[1]</code>，<code>arr</code>就变成<code>[[1],[1],[1],[1],[1]]</code>这样的二维数组啦。</p>
<p>亦或是直接字面量：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [[<span class="hljs-number">1</span>],[<span class="hljs-number">1</span>]];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>高级一点的写法：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = <span class="hljs-built_in">Array</span>.apply(<span class="hljs-literal">null</span>,&#123;<span class="hljs-attr">length</span>:<span class="hljs-number">2</span>&#125;).map(<span class="hljs-function"><span class="hljs-params">value</span> =></span> value = [<span class="hljs-number">1</span>]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此处<code>arr</code>的值为[1,1]。<code>Array.apply(null,&#123;length:2&#125;)</code>是用来创建有初始化的数组，其结果为<code>[undefined,undefined]</code>；与<code>Array(2)</code>没有初始化的结果<code>[,]</code>有所不同。</p>
<p>需要注意的是：</p>
<blockquote>
<p><code>apply</code>的第二个参数除了数组外，还可以是类数组对象。</p>
<p><code>map</code>不会遍历数组中没有初始化的或被删除的元素。</p>
</blockquote>
<h2 data-id="heading-3">类数组</h2>
<p>类数组，顾名思义：类似数组但不是数组的对象，不能够全部使用数组的方法。满足类数组的条件：</p>
<blockquote>
<p>有<code>length</code>属性</p>
<p>使用数字作为属性名</p>
</blockquote>
<p>例1：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-number">0</span> : <span class="hljs-string">'STA'</span>,
    <span class="hljs-number">1</span> : <span class="hljs-string">'SUN'</span>,
    <span class="hljs-attr">length</span> : <span class="hljs-number">2</span>
&#125;
<span class="hljs-keyword">var</span> arr = <span class="hljs-built_in">Array</span>.from(obj); <span class="hljs-comment">//['STA','SUN']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>obj</code>以数字作为属性名并且有<code>length</code>属性，因此<code>obj</code>是一个类数组对象。当然可以通过<code>Array.from()</code>来将类数组转成数组。</p>
<p>例2：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str = <span class="hljs-string">'123'</span>;
<span class="hljs-keyword">var</span> arr = <span class="hljs-built_in">Array</span>.from(str); <span class="hljs-comment">//['1','2','3']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串也可以看作类数组。</p>
<p>例3：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>);
    <span class="hljs-comment">//Arguments(2) [1, 2, callee: ƒ, Symbol(Symbol.iterator): ƒ]</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>.length); <span class="hljs-comment">//2</span>
&#125;
foo(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样<code>arguments</code>也是一个类数组，<code>arguments</code>作为函数外部传入实参的集合，如果对参数进行处理，需要用到数组的方法，直接调用方法是不可取的。那么有办法让类数组中的数据使用数组的某些方法呢？当然是可以的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">Array</span>.prototype.map.call(<span class="hljs-built_in">arguments</span>,<span class="hljs-function"><span class="hljs-params">value</span> =></span> value + <span class="hljs-number">1</span>);
    <span class="hljs-built_in">console</span>.log(arr);  <span class="hljs-comment">//[2,3]</span>
&#125;
foo(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上例可以看到，我们可以通过<code>call</code>改变数组map的执行环境，从而使类数组中的数据使用<code>map</code>方法；也可以先将类数组通过<code>Array.from()</code>转变成数组再进行<code>map</code>操作。</p>
<h2 data-id="heading-4">总结</h2>
<p>稀疏数组是元素没有连续索引的数组；<code>JavaScript</code>不支持真正的多维数组，可以使用数组的数组来模拟；类数组需要有<code>length</code>属性以及数字属性名。</p>
<p>当然，写的可能不是很详细，或是错误的地方，欢迎大家补充、指正。</p></div>  
</div>
            