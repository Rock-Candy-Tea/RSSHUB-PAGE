
---
title: 'TypeScript的类型注解--(TypeScript 02)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad6e1a3274de426d92d9c0d8060aecc5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 00:31:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad6e1a3274de426d92d9c0d8060aecc5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">TS中的类型注解</h2>
<ul>
<li>基础类型：boolean string number null undefined symbol any never</li>
<li>对象：interface</li>
<li>数组：number[] string[] boolean[]</li>
<li>泛型的写法：Array<number></li>
</ul>
<h2 data-id="heading-1">TS带来的新的语法特性</h2>
<ol>
<li>as 断言</li>
<li>class(OOP面向对象的三大特性)：封装、继承、多态</li>
</ol>
<p>还有其他的，后续文章会进行详细的介绍。</p>
<h2 data-id="heading-2">创建tsconfig.json</h2>
<pre><code class="copyable">tsc --init
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">修改tsc的输出路径</h2>
<ol>
<li>在tsconfig.json中对下面两行进行修改。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad6e1a3274de426d92d9c0d8060aecc5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>直接运行tsc指令，系统将直接将编译好的js文件输出到dist目录下。</li>
</ol>
<h2 data-id="heading-4">原始数据的注解</h2>
<ol>
<li>布尔值的注解</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> isDone: boolean = <span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>数字类型的注解</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> decLiteral: <span class="hljs-built_in">number</span> = <span class="hljs-number">6</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>字符串类型的注解</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> name2: <span class="hljs-built_in">string</span> = <span class="hljs-string">"bob"</span>;
name2 = <span class="hljs-string">"smith"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>any类型的注解</li>
</ol>
<blockquote>
<p>any类型可以表示任意类型，通过此类型的注解，不会有相应的代码提示，但是可以赋值为不同类型的数据。</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> notSure: <span class="hljs-built_in">any</span> = <span class="hljs-number">4</span>;
notSure = <span class="hljs-string">"maybe a string instead"</span>;
notSure = <span class="hljs-literal">false</span>; <span class="hljs-comment">// okay, definitely a boolean</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>通过Object类型的注解可以赋值为任意类型，但是却只能调用真正的Object上的属性，也就是说只有你是真的对象才可以调用上面的方法。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> notSure: any = <span class="hljs-number">4</span>;
notSure.ifItExists(); <span class="hljs-comment">// okay, ifItExists might exist at runtime</span>
notSure.toFixed(); <span class="hljs-comment">// okay, toFixed exists (but the compiler doesn't check)</span>

<span class="hljs-keyword">let</span> prettySure: <span class="hljs-built_in">Object</span> = <span class="hljs-number">4</span>;
prettySure.toFixed(); <span class="hljs-comment">// Error: Property 'toFixed' doesn't exist on type 'Object'.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>未给初始值的变量，初始值是any.</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cc98bca0e6c48d0a72becc9a954fc9a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>void类型的注解</li>
</ol>
<blockquote>
<p>void类型的变量只能赋值为undefined和null,当一个函数没有返回值的时候，其注解类型为void.</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">warnUser</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"This is my warning message"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>undefined和null类型的注解</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Not much else we can assign to these variables!</span>
<span class="hljs-keyword">let</span> u: <span class="hljs-literal">undefined</span> = <span class="hljs-literal">undefined</span>;
<span class="hljs-keyword">let</span> n: <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在配置项中将"strictNullChecks"置为false的时候，undefined和null可以成为任何类型的子类型，所谓的子类型，就是说类型为number或其他的类型的值可以使undefined和null.</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a: number = <span class="hljs-literal">undefined</span>;
<span class="hljs-keyword">let</span> b: number = <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：在类型注解的时候，可以使用或运算符，同时注解多个类型</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> a: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">true</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>never类型的注解</li>
</ol>
<blockquote>
<p>返回never的函数必须存在无法达到的终点，never是任何类型的子类型，其他任何类型都不能赋值给never.</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 返回never的函数必须存在无法达到的终点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">error</span>(<span class="hljs-params">message: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">never</span> </span>&#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(message);
&#125;
<span class="hljs-comment">// 推断的返回值类型为never</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fail</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> error(<span class="hljs-string">"Something failed"</span>);
&#125;
<span class="hljs-comment">// 返回never的函数必须存在无法达到的终点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">infiniteLoop</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123;
    <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li>Object类型的注解</li>
</ol>
<blockquote>
<p>使用Object类型的注解，可以很好的表示非原始类型，也就是除<code>number</code>，<code>string</code>，<code>boolean</code>，<code>symbol</code>，<code>null</code>或<code>undefined</code>之外的类型。使用Object类型进行注解，可以很好的表示很多API。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">declare <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">o: object | <span class="hljs-literal">null</span></span>): <span class="hljs-title">void</span></span>;

create(&#123; <span class="hljs-attr">prop</span>: <span class="hljs-number">0</span> &#125;); <span class="hljs-comment">// OK</span>
create(<span class="hljs-literal">null</span>); <span class="hljs-comment">// OK</span>

create(<span class="hljs-number">42</span>); <span class="hljs-comment">// Error</span>
create(<span class="hljs-string">"string"</span>); <span class="hljs-comment">// Error</span>
create(<span class="hljs-literal">false</span>); <span class="hljs-comment">// Error</span>
create(<span class="hljs-literal">undefined</span>); <span class="hljs-comment">// Error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">类型断言</h2>
<blockquote>
<p>类型断言类似于其他语言中的类型转换。</p>
</blockquote>
<p><strong>尖括号语法</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> someValue: <span class="hljs-built_in">any</span> = <span class="hljs-string">"this is a string"</span>;

<span class="hljs-keyword">let</span> strLength: <span class="hljs-built_in">number</span> = (<<span class="hljs-built_in">string</span>>someValue).length;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>as语法</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> someValue: <span class="hljs-built_in">any</span> = <span class="hljs-string">"this is a string"</span>;

<span class="hljs-keyword">let</span> strLength: <span class="hljs-built_in">number</span> = (someValue <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>).length;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>推荐使用as语法，因为如果你使用JSX的时候，只有as语法是被允许的。</strong></p>
<h2 data-id="heading-6">欢迎大家关注我的专栏，一起学习TypeScript!</h2></div>  
</div>
            