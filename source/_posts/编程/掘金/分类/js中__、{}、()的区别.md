
---
title: 'js中__、&#123;&#125;、()的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a21f36e536e0464e8690afeda900884d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 00:33:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a21f36e536e0464e8690afeda900884d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><ul>
<li><code>&#123;&#125;</code>：表示对象</li>
<li><code>[]</code>：表示对象的属性、方法</li>
<li><code>()</code>：如果用在方法名后面，代表调用</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a21f36e536e0464e8690afeda900884d~tplv-k3u1fbpfcp-zoom-1.image" alt="0Uybp6.png" loading="lazy" referrerpolicy="no-referrer"></p>

<p>一、<code>&#123; &#125;</code> 大括号，表示<strong>定义一个对象</strong>，大部分情况下要有成对的属性和值，或是函数体。</p>
<pre><code class="hljs language-js copyable" lang="js">如：<span class="hljs-keyword">var</span> LangShen = &#123;<span class="hljs-string">"Name"</span>:<span class="hljs-string">"Langshen"</span>,<span class="hljs-string">"AGE"</span>:”<span class="hljs-number">28</span>”&#125;; 
上面声明了一个名为“LangShen”的对象，多个属性或函数用,（逗号）隔开，因为是对象的属性， 
所以访问时，应该用.（点）来层层访问：LangShen.Name、LangShen.AGE，
当然我们也可以用数组的方式来访问，如：LangShen[<span class="hljs-string">"Name"</span>]、LangShen[<span class="hljs-string">"AGE"</span>]，结果是一样的。
<span class="hljs-keyword">var</span> LangShen = &#123; 
    <span class="hljs-attr">Name</span> : <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123; 
        <span class="hljs-keyword">return</span> <span class="hljs-string">"LangShen"</span>; 
    &#125;, 
    <span class="hljs-attr">Age</span> : <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123; 
        <span class="hljs-keyword">return</span> <span class="hljs-string">"28"</span>; 
    &#125; 
&#125; 
调用 LangShen.Name()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>二、<code>[ ]</code>中括号，表示<strong>一个数组，也可以理解为一个数组对象</strong>。</p>
<pre><code class="hljs language-js copyable" lang="js">如：<span class="hljs-keyword">var</span> LangShen = [ <span class="hljs-string">"Name"</span>,<span class="hljs-string">"LangShen"</span>,<span class="hljs-string">"AGE"</span>,<span class="hljs-string">"28"</span> ]; 
很明显，每个值或函数，都是独立的，多个值之间只用,（逗号）隔开，因为是数组对象，所以它等于： 
<span class="hljs-keyword">var</span> LangShen = <span class="hljs-built_in">Array</span>( <span class="hljs-string">"Name"</span>,<span class="hljs-string">"LangShen"</span>,<span class="hljs-string">"AGE"</span>,<span class="hljs-string">"28"</span> ); 
访问时，也是和数组一样，alert( LangShen[<span class="hljs-number">0</span>] )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>三、<code>&#123; &#125;</code> 和<code>[ ] </code>一起使用，<code>&#123; &#125;</code> 是一个对象，<code>[ ]</code> 是一个数组，我们可以组成一个对象数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> LangShen = &#123; 
    <span class="hljs-string">"Name"</span>:<span class="hljs-string">"Langshen"</span>, 
    <span class="hljs-string">"MyWife"</span>:[ <span class="hljs-string">"LuLu"</span>,<span class="hljs-string">"26"</span> ], 
    <span class="hljs-string">"MySon"</span>:[&#123;<span class="hljs-string">"Name"</span>:<span class="hljs-string">"Son1"</span>&#125;,&#123;<span class="hljs-string">"Name"</span>:<span class="hljs-string">"Son2"</span>&#125;,&#123;<span class="hljs-string">"Name"</span>:<span class="hljs-string">"Son3"</span>&#125;] 
&#125; 
从上面的结构来看，是一个对象里面的第一项是个属性，第二项是一个数组，第三个是包含有多个对象的数组。
调用起来，也是一层一层访问，对象的属性用.（点）叠加，数组用 [下标] 来访问。

如：alert( LangShen.MySon[<span class="hljs-number">1</span>].Name ) ；
<span class="hljs-keyword">var</span> LangShen=[
    &#123;“name”：“wangwu”&#125;,
    &#123;“name”：“lieu”&#125;
];
这是一个对象数组
<span class="copy-code-btn">复制代码</span></code></pre>
<p>四、()多表示参数、&#123;&#125;表示函数体 ()要看它放在什么位置才能知道它起什么作用，因为它有多种用法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">show</span>(<span class="hljs-params">name</span>)</span>&#123;
    Alert(name);
&#125;
es6中，
<span class="hljs-keyword">let</span> show=<span class="hljs-function">(<span class="hljs-params">name</span>)=></span>&#123;
    alert(name);
&#125;
在es6中如果参数只有一个，或者函数体只有一个话，可以省略（）、&#123;&#125;,如
<span class="hljs-keyword">let</span> show=<span class="hljs-function"><span class="hljs-params">name</span>=></span>alert(name);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            