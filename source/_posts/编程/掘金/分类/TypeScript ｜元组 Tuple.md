
---
title: 'TypeScript ｜元组 Tuple'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1327'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 17:34:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=1327'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>相同类型元素组成成为数组，不同类型元素组成了元组（Tuple）</p>
</blockquote>
<h2 data-id="heading-0">定义元组类型</h2>
<p>元组中规定的元素类型顺序必须是完全对照的，而且不能多、不能少：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> x: [string, number]; 
x = [<span class="hljs-string">'hello'</span>, <span class="hljs-number">10</span>]; <span class="hljs-comment">// OK</span>
x = [<span class="hljs-number">10</span>, <span class="hljs-string">'hello'</span>]; <span class="hljs-comment">// Error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当访问一个已知索引的元素，会得到正确的类型：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(x[<span class="hljs-number">0</span>].substr(<span class="hljs-number">1</span>)); <span class="hljs-comment">// OK</span>
<span class="hljs-built_in">console</span>.log(x[<span class="hljs-number">1</span>].substr(<span class="hljs-number">1</span>)); <span class="hljs-comment">// Property 'substr' does not exist on type 'number'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>元组越界</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//可以越界添加元素（不建议），但不可越界访问</span>
<span class="hljs-keyword">const</span> list: [string, number] = [<span class="hljs-string">'Sherlock'</span>, <span class="hljs-number">1887</span>]
list.push(<span class="hljs-string">'hello world'</span>)
<span class="hljs-built_in">console</span>.log(list)      <span class="hljs-comment">// [ 'Sherlock', 1887, 'hello world' ]</span>
<span class="hljs-built_in">console</span>.log(list[<span class="hljs-number">2</span>])   <span class="hljs-comment">// Tuple type '[string, number]' of length '2' has no element at index '2'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">可选元素类型</h2>
<p>元组类型允许在元素类型后缀一个 ? 来说明元素是可选的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> list: [number, string?, boolean?]
list = [<span class="hljs-number">10</span>, <span class="hljs-string">'Sherlock'</span>, <span class="hljs-literal">true</span>]
list = [<span class="hljs-number">10</span>, <span class="hljs-string">'Sherlock'</span>]
list = [<span class="hljs-number">10</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">应用</h2>
<ol>
<li>React Hook 的 useState</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">const</span> [loading, setLoading] = useState<boolean>(<span class="hljs-literal">false</span>); 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>数据源是CVS这种文件的时候，会使用元组</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">type Touple = [string, number, string];
<span class="hljs-keyword">let</span> csvData: Touple[] = [
    [<span class="hljs-string">'张三'</span>, <span class="hljs-number">18</span>, <span class="hljs-string">'男'</span>], 
    [<span class="hljs-string">'李四'</span>, <span class="hljs-number">14</span>, <span class="hljs-string">'男'</span>]
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">元组类型的 Rest 使用</h2>
<p>元组可以作为参数传递给函数，函数的 Rest 形参可以定义为元组类型：</p>
<pre><code class="hljs language-js copyable" lang="js">declare <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">rest</span>(<span class="hljs-params">...args: [number, string, boolean]</span>): <span class="hljs-title">void</span>
//等价
<span class="hljs-title">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">rest</span>(<span class="hljs-params">arg1: number, arg2: string, arg3: boolean</span>): <span class="hljs-title">void</span>
</span></span><span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在声明文件（.d.ts）中，关键字 declare 表示声明作用。声明文件用于编写第三方类库，通过配置 tsconfig.json 文件中的 declaration 为 true，在编译时可自行生成。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> list: [number, ...string[]] = [<span class="hljs-number">10</span>, <span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>]
<span class="hljs-keyword">const</span> list1: [string, ...number[]] = [<span class="hljs-string">'a'</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">学习链接</h2>
<ul>
<li><a href="http://www.imooc.com/wiki/typescriptlesson/tuple.html" target="_blank" rel="nofollow noopener noreferrer">www.imooc.com/wiki/typesc…</a></li>
<li><a href="https://www.runoob.com/typescript/ts-tuple.html" target="_blank" rel="nofollow noopener noreferrer">www.runoob.com/typescript/…</a></li>
</ul></div>  
</div>
            