
---
title: 'Postcss了解一下'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/162788a67e2e458dae6b03ea068f0be4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 05:36:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/162788a67e2e458dae6b03ea068f0be4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>工作中用到的框架 css 处理有以下问题，需要用 postcss 做些自动处理。</p>
<ul>
<li>同名 class 后者会覆盖前者：<code>.a&#123;color: #fff&#125;</code> <code>.a&#123;background: #fff&#125;</code>，后者生效</li>
<li>最多嵌套两层：<code>.a .b .c &#123;&#125;</code>不生效</li>
</ul>
<p>通过本文学习了解什么是 postcss，以及如何通过 postcss 做一些工作。</p>
<h2 data-id="heading-0">简介</h2>
<blockquote>
<p>postcss：PostCSS is a tool for transforming styles with JS plugins. These plugins can lint your CSS, support variables and mixins, transpile future CSS syntax, inline images, and more.
postcss是使用用js插件转换样式的工具。这些插件可以校验css，支持variables和mixins，编译未来css语法，内联图片等等。</p>
</blockquote>
<p>从其名字 postcss 可以看出早期是被当做后处理器的。也就是处理less/sass 编译后的 css。最常用的插件就是 autoprefixer，根据浏览器版本添加兼容前缀。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/162788a67e2e458dae6b03ea068f0be4~tplv-k3u1fbpfcp-watermark.image" alt="流程图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>postcss 像 babel 一样会把 style 转成 ast，经过一系列插件转换，再将转换后的 as t生成新的 style。随着发展，用后处理器形容postcss 已经不合适了。目前可以使用 postcss-sass/postcss-less 对 less/sass 代码进行转化（将 less/sass 转化为 less/sass，而不是直接转化为 css），也可以使用 precss 代替 sass（感觉还不太成熟）。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92397fb502b1468ba30d43eee6f815ba~tplv-k3u1fbpfcp-watermark.image" alt="未命名文件 (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以目前推荐的还是 postcss 和 less/sass 结合使用，在 webpack 配置中，postcss-loader 要写在 sass-loader/less-loader 前面。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(css|less)$/i</span>,
                use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'postcss-loader'</span>, <span class="hljs-string">'less-loader'</span>],
            &#125;,
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于更多 postcss 的用途，可以参考 <a href="https://github.com/postcss/postcss" target="_blank" rel="nofollow noopener noreferrer">github.com/postcss/pos…</a></p>
<h2 data-id="heading-1">工作流程</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfbb840dcefd4cac9eeeb1f4606e54c4~tplv-k3u1fbpfcp-watermark.image" alt="未命名文件 (3).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大致步骤：</p>
<ul>
<li>将 CSS 字符串生成 Tokens</li>
<li>将 Tokens 通过规则生成 AST 树</li>
<li>将 AST 树传给插件进行处理</li>
<li>将处理后的 AST 树生成新的css资源（包括css字符串、sourceMap等）</li>
</ul>
<p>即如图所示的步骤：
CSS Input → Tokenizer → Parser → AST → Plugins → Stringifier
举个🌰：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@import</span> url(<span class="hljs-string">'./default.css'</span>);
<span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
  <span class="hljs-comment">/* margin: 0; */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1. input</h3>
<pre><code class="copyable">'@import url('./default.css');\nbody &#123;\n  padding: 0;\n  /* margin: 0; */\n&#125;\n'
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2. tokenizer</h3>
<p>tokenizer 包括以下几个方法:</p>
<ul>
<li>back：back方法会设置 nextToken 的下次调用的返回值。</li>
<li>nextToken：获取下一个 token。</li>
<li>endOfFile：判断文件是否结束。</li>
<li>position：获取当前 token 的位置。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// tokenize.js的nextToken方法 简化代码</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">nextToken</span>(<span class="hljs-params">opts</span>) </span>&#123;
    <span class="hljs-comment">// 如果之前调用了back方法，下一次调用nextToken将会返回back方法设置的token</span>
    <span class="hljs-keyword">if</span> (returned.length) <span class="hljs-keyword">return</span> returned.pop()
    code = css.charCodeAt(pos)
    <span class="hljs-comment">// 判断每一个字符</span>
    <span class="hljs-keyword">switch</span> (code) &#123; 
        <span class="hljs-keyword">case</span> xxx: 
        <span class="hljs-keyword">break</span>;
    &#125;

    pos++
    <span class="hljs-keyword">return</span> currentToken
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>nextToken 方法判断每一个字符，并生成如下类型的 token：</p>
<p><code>space: </code></p>
<ul>
<li>\n：换行</li>
<li>：空格</li>
<li>\f ：换页</li>
<li>\r：回车</li>
<li>\t：水平制表符</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 空格、换行、制表符、回车等，都被当做space类型token</span>
  <span class="hljs-keyword">case</span> NEWLINE:
  <span class="hljs-keyword">case</span> SPACE: 
  &#123;
    next = pos
    <span class="hljs-comment">// 循环，将连续的空格、换行、回车等作为一个token</span>
    <span class="hljs-keyword">do</span> &#123;
      next += <span class="hljs-number">1</span>
      code = css.charCodeAt(next)
    &#125; <span class="hljs-keyword">while</span> (
       <span class="hljs-comment">// 如果是</span>
    )
    <span class="hljs-comment">// 截取token的值</span>
    currentToken = [<span class="hljs-string">'space'</span>, css.slice(pos, next)]
    pos = next - <span class="hljs-number">1</span>
    <span class="hljs-keyword">break</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>string: </code></p>
<ul>
<li>'：单引号</li>
<li>"：双引号</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 单引号，双引号之间的内容会被当成string类型token</span>
  <span class="hljs-keyword">case</span> SINGLE_QUOTE:
  <span class="hljs-keyword">case</span> DOUBLE_QUOTE: &#123;
    quote = code === SINGLE_QUOTE ? <span class="hljs-string">"'"</span> : <span class="hljs-string">'"'</span>
    next = pos
    <span class="hljs-keyword">do</span> &#123;
      next = css.indexOf(quote, next + <span class="hljs-number">1</span>)
      <span class="hljs-keyword">if</span> (next === -<span class="hljs-number">1</span>) &#123;
        <span class="hljs-keyword">if</span> (ignore || ignoreUnclosed) &#123;
          next = pos + <span class="hljs-number">1</span>
          <span class="hljs-keyword">break</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
          unclosed(<span class="hljs-string">'string'</span>)
        &#125;
      &#125;
    &#125; <span class="hljs-keyword">while</span> (escaped)

    currentToken = [<span class="hljs-string">'string'</span>, css.slice(pos, next + <span class="hljs-number">1</span>), pos, next]
    pos = next
    <span class="hljs-keyword">break</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>at-word</code>：@ 和其后面连着的字符会被当成 at-wrod 类型 token
<code>@*</code>：at符</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">case</span> AT: &#123;
   currentToken = [<span class="hljs-string">'at-word'</span>, css.slice(pos, next + <span class="hljs-number">1</span>), pos, next]
   pos = next
   <span class="hljs-keyword">break</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>[和]</code>：中括号</p>
<p><code>)</code>：右括号</p>
<p><code>&#123;和&#125;</code>：大括号</p>
<p><code>;</code>：分号</p>
<p><code>:</code>：冒号</p>
<p>都是独立的 token 类型。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// []&#123;&#125;:;)等都是独立的token类型</span>
<span class="hljs-keyword">case</span> OPEN_SQUARE:
<span class="hljs-keyword">case</span> CLOSE_SQUARE:
<span class="hljs-keyword">case</span> OPEN_CURLY:
<span class="hljs-keyword">case</span> CLOSE_CURLY:
<span class="hljs-keyword">case</span> COLON:
<span class="hljs-keyword">case</span> SEMICOLON:
<span class="hljs-keyword">case</span> CLOSE_PARENTHESES: &#123;
    <span class="hljs-keyword">let</span> controlChar = <span class="hljs-built_in">String</span>.fromCharCode(code)
    currentToken = [controlChar, controlChar, pos]
    <span class="hljs-keyword">break</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>(和brackets</code></p>
<ul>
<li>url()：url() 值没有单引号、双引号包裹的，当做brackets类型 token</li>
<li>url('')：如果没有右括号）,或者匹配到正则，当成（类型token，比如url('')</li>
<li>var(--main-color)：否则当成 brackets 类型 token，比如var(--main-color)</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 左括号特殊处理</span>
<span class="hljs-keyword">case</span> OPEN_PARENTHESES: &#123;
prev = buffer.length ? buffer.pop()[<span class="hljs-number">1</span>] : <span class="hljs-string">''</span>
n = css.charCodeAt(pos + <span class="hljs-number">1</span>)
    <span class="hljs-comment">// url()值没有单引号、双引号包裹的，当做brackets类型token</span>
    <span class="hljs-keyword">if</span> (
      prev === <span class="hljs-string">'url'</span> &&
      n !== SINGLE_QUOTE &&
      n !== DOUBLE_QUOTE &&
    ) &#123;
      next = pos
      <span class="hljs-keyword">do</span> &#123;
        escaped = <span class="hljs-literal">false</span>
        next = css.indexOf(<span class="hljs-string">')'</span>, next + <span class="hljs-number">1</span>)
        <span class="hljs-keyword">if</span> (next === -<span class="hljs-number">1</span>) &#123;
          <span class="hljs-keyword">if</span> (ignore || ignoreUnclosed) &#123;
            next = pos
            <span class="hljs-keyword">break</span>
          &#125; <span class="hljs-keyword">else</span> &#123;
            unclosed(<span class="hljs-string">'bracket'</span>)
          &#125;
        &#125;      
      &#125; <span class="hljs-keyword">while</span> (escaped)
      currentToken = [<span class="hljs-string">'brackets'</span>, css.slice(pos, next + <span class="hljs-number">1</span>), pos, next]
      pos = next
    &#125; <span class="hljs-keyword">else</span> &#123;
      next = css.indexOf(<span class="hljs-string">')'</span>, pos + <span class="hljs-number">1</span>)
      content = css.slice(pos, next + <span class="hljs-number">1</span>)
      <span class="hljs-comment">// 如果没有右括号）,或者匹配到正则，当成（类型token，比如url('')</span>
      <span class="hljs-keyword">if</span> (next === -<span class="hljs-number">1</span> || RE_BAD_BRACKET.test(content)) &#123;
        currentToken = [<span class="hljs-string">'('</span>, <span class="hljs-string">'('</span>, pos]
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 否则当成brackets类型token，比如var(--main-color)</span>
        currentToken = [<span class="hljs-string">'brackets'</span>, content, pos, next]
        pos = next
      &#125;
    &#125;
    <span class="hljs-keyword">break</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>comment</code>: 默认会被当成 comment 类型和 word 类型 token</p>
<ul>
<li>/：斜线</li>
<li>*：通配符</li>
</ul>
<p><code>word</code>:</p>
<ul>
<li>\：反斜线</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">default</span>: &#123;
    <span class="hljs-keyword">if</span> (code === SLASH && css.charCodeAt(pos + <span class="hljs-number">1</span>) === ASTERISK) &#123;
      next = css.indexOf(<span class="hljs-string">'*/'</span>, pos + <span class="hljs-number">2</span>) + <span class="hljs-number">1</span>
      <span class="hljs-keyword">if</span> (next === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">if</span> (ignore || ignoreUnclosed) &#123;
          next = css.length
        &#125; <span class="hljs-keyword">else</span> &#123;
          unclosed(<span class="hljs-string">'comment'</span>)
        &#125;
      &#125;

      currentToken = [<span class="hljs-string">'comment'</span>, css.slice(pos, next + <span class="hljs-number">1</span>), pos, next]
      pos = next
    &#125; <span class="hljs-keyword">else</span> &#123;
      RE_WORD_END.lastIndex = pos + <span class="hljs-number">1</span>
      RE_WORD_END.test(css)
      <span class="hljs-keyword">if</span> (RE_WORD_END.lastIndex === <span class="hljs-number">0</span>) &#123;
        next = css.length - <span class="hljs-number">1</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        next = RE_WORD_END.lastIndex - <span class="hljs-number">2</span>
      &#125;

      currentToken = [<span class="hljs-string">'word'</span>, css.slice(pos, next + <span class="hljs-number">1</span>), pos, next]
      buffer.push(currentToken)
      pos = next
    &#125;

    <span class="hljs-keyword">break</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过 tokenizer 处理成如下的 tokens：</p>
<pre><code class="copyable">[ 'at-word', '@import', 0, 6 ]
[ 'space', ' ' ]
[ 'word', 'url', 8, 10 ]
[ '(', '(', 11 ]
[ 'string', "'./default.css'", 12, 26 ]
[ ')', ')', 27 ]
[ ';', ';', 28 ]
[ 'space', '\n' ]
[ 'word', 'body', 30, 33 ]
[ 'space', ' ' ]
[ '&#123;', '&#123;', 35 ]
[ 'space', '\n  ' ]
[ 'word', 'padding', 39, 45 ]
[ ':', ':', 46 ]
[ 'space', ' ' ]
[ 'word', '0', 48, 48 ]
[ ';', ';', 49 ]
[ 'space', '\n  ' ]
[ 'comment', '/* margin: 0; */', 53, 68 ]
[ 'space', '\n' ]
[ '&#125;', '&#125;', 70 ]
[ 'space', '\n' ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，token是一个数组，以第一个token为例，数据结构如下</p>
<pre><code class="copyable">[
    'at-word', // 类型
    '@import', // 值
    0， // 起始位置
    6   // 终止位置
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3. parser</h3>
<p>parser 会循环调用 tokenizer 的 nextToken 方法，直到文件结束。在循环过程中使用一些算法和条件判断去创建节点然后构建 AST。上面例子生成的 AST 如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3803dd2240094f1d8bae9d5959d5da7d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">3.1 节点</h4>
<p>Node 和 Container 节点的基础类，其中 Container 继承自 Node。AST 由下面几种节点组成</p>
<ul>
<li>Root: 继承自 Container。AST 的根节点，代表整个 css 文件</li>
<li>AtRule: 继承自 Container。以 @ 开头的语句，核心属性为 params，例如：@import url('./default.css')，@keyframes shaking &#123;&#125;。params 为url('./default.css')</li>
<li>Rule: 继承自 Container。带有声明的选择器，核心属性为 selector，例如：body &#123;&#125;，selector为body</li>
<li>Declaration：继承自 Node。声明，是一个键值对，核心属性为 prop，value，例如：padding: 0，prop为padding，value为0</li>
<li>Comment: 继承自 Node。标准的注释/* 注释 */，如图所示 text 为margin: 0;</li>
</ul>
<p>节点包括一些通用属性</p>
<ul>
<li>
<p>type：节点类型</p>
</li>
<li>
<p>parent：父节点</p>
</li>
<li>
<p>source：存储节点的资源信息，计算 sourcemap</p>
<ul>
<li>input：输入</li>
<li>start：节点的起始位置</li>
<li>end：节点的终止位置</li>
</ul>
</li>
<li>
<p>raws：存储节点的附加符号，分号、空格、注释等，在 stringify 过程中会拼接这些附加符号</p>
<p>通用:</p>
<ul>
<li>before：The space symbols before the node. It also stores <code>*</code> and <code>_</code> symbols before the declaration (IE hack).</li>
</ul>
<p>作用于Rule:</p>
<ul>
<li>after：The space symbols after the last child of the node to the end of the node. 最后一个子节点和节点末尾之间的space符号</li>
<li>between：The symbols between the selector and <code>&#123;</code> for rules 。selector和&#123;之间的符号</li>
<li>semicolon：Contains <code>true</code> if the last child has an (optional) semicolon.最后一个子节点有；则为true</li>
<li>ownSemicolon: Contains <code>true</code> if there is semicolon after rule.如果rule后面有；则为true</li>
</ul>
<p>作用于Comment</p>
<ul>
<li>left：The space symbols between <code>/*</code> and the comment’s text. /* 和注释内容之间的space符号</li>
<li>right：The space symbols between the comment’s text. */和注释内容之间的space符号
作用于Declaration</li>
<li>important：The content of the important statement. 是否是important</li>
<li>value: Declaration value with comments. 带有注释的声明值。</li>
</ul>
</li>
</ul>
<p>节点有各自的API，具体可以看<a href="https://postcss.org/api/#container-remove" target="_blank" rel="nofollow noopener noreferrer">PostCSS API</a></p>
<h4 data-id="heading-6">3.2 生成过程</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parser</span> </span>&#123;  
  <span class="hljs-function"><span class="hljs-title">parse</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> token
    <span class="hljs-keyword">while</span> (!<span class="hljs-built_in">this</span>.tokenizer.endOfFile()) &#123;
      token = <span class="hljs-built_in">this</span>.tokenizer.nextToken()
      <span class="hljs-keyword">switch</span> (token[<span class="hljs-number">0</span>]) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'space'</span>:
          <span class="hljs-built_in">this</span>.spaces += token[<span class="hljs-number">1</span>]
          <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">';'</span>:
          <span class="hljs-built_in">this</span>.freeSemicolon(token)
          <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'&#125;'</span>:
          <span class="hljs-built_in">this</span>.end(token)
          <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'comment'</span>:
          <span class="hljs-built_in">this</span>.comment(token)
          <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'at-word'</span>:
          <span class="hljs-built_in">this</span>.atrule(token)
          <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'&#123;'</span>:
          <span class="hljs-built_in">this</span>.emptyRule(token)
          <span class="hljs-keyword">break</span>
        <span class="hljs-attr">default</span>:
          <span class="hljs-built_in">this</span>.other(token)
          <span class="hljs-keyword">break</span>
      &#125;
    &#125;
    <span class="hljs-built_in">this</span>.endFile()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先创建 root 节点，并将 current（当前节点）设置为 root，使用tokens 变量存储已经遍历但还未使用过的 token。</p>
<ul>
<li>遇到 <code>at-rule</code> token，创建 atRule 节点</li>
<li>遇到 <code>&#123;</code> token，创建 rule 节点
<ul>
<li>将 tokens 中存储的token生成 rule 的 selector 属性</li>
<li>将 current 设置为 rule 节点</li>
<li>将 rule 节点 push 到 current 的 nodes 中</li>
</ul>
</li>
<li>遇到 <code>;</code> token，创建 decl 节点。有一种特殊情况：declaration 是以；分隔的，如果是最后一条规则，可以不带；,比如.a&#123;color: blue&#125;，
<ul>
<li>将 decl 节点 push 到 current 的 nodes 中。</li>
</ul>
</li>
<li>遇到 <code>comment</code> token，就创建comment节点</li>
<li>遇到 <code>&#125;</code> token，认为当规则结束
<ul>
<li>将 current 设置为 current.parent（当前节点的父节点）</li>
</ul>
</li>
</ul>
<p>具体过程可以看源码: <a href="https://github.com/postcss/postcss/blob/main/lib/parser.js" target="_blank" rel="nofollow noopener noreferrer">github.com/postcss/pos…</a></p>
<p>用到的算法：</p>
<blockquote>
<ol>
<li>深度优先遍历</li>
<li>匹配的括号</li>
</ol>
</blockquote>
<h3 data-id="heading-7">4. plugins</h3>
<p>然后会调用plugins修改Parser得到的AST树。plugins的执行在lazy-result.js中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LazyResult</span> </span>&#123;
  get [<span class="hljs-built_in">Symbol</span>.toStringTag]() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'LazyResult'</span>
  &#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">processor</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.result.processor
  &#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">opts</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.result.opts
  &#125;
  <span class="hljs-comment">// 获取css</span>
  <span class="hljs-keyword">get</span> <span class="hljs-title">css</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.stringify().css
  &#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">content</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.stringify().content
  &#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">map</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.stringify().map
  &#125;
  <span class="hljs-comment">// 获取root</span>
  <span class="hljs-keyword">get</span> <span class="hljs-title">root</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.sync().root
  &#125;
  <span class="hljs-keyword">get</span> <span class="hljs-title">messages</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.sync().messages
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在访问result.css、result.map、result.root时均会执行对应的函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">stringify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.error) <span class="hljs-keyword">throw</span> <span class="hljs-built_in">this</span>.error
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.stringified) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.result
    <span class="hljs-built_in">this</span>.stringified = <span class="hljs-literal">true</span>
    <span class="hljs-comment">// 同步执行插件</span>
    <span class="hljs-built_in">this</span>.sync()

    <span class="hljs-keyword">let</span> opts = <span class="hljs-built_in">this</span>.result.opts
    <span class="hljs-keyword">let</span> str = stringify
    <span class="hljs-keyword">if</span> (opts.syntax) str = opts.syntax.stringify
    <span class="hljs-keyword">if</span> (opts.stringifier) str = opts.stringifier
    <span class="hljs-keyword">if</span> (str.stringify) str = str.stringify
    <span class="hljs-comment">// 生成map和css</span>
    <span class="hljs-keyword">let</span> map = <span class="hljs-keyword">new</span> MapGenerator(str, <span class="hljs-built_in">this</span>.result.root, <span class="hljs-built_in">this</span>.result.opts)
    <span class="hljs-keyword">let</span> data = map.generate()
    <span class="hljs-built_in">this</span>.result.css = data[<span class="hljs-number">0</span>]
    <span class="hljs-built_in">this</span>.result.map = data[<span class="hljs-number">1</span>]

    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.result
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在访问result.css时会先同步执行插件，然后用处理后的AST去生成css和sourcemap</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">sync</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.error) <span class="hljs-keyword">throw</span> <span class="hljs-built_in">this</span>.error
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.processed) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.result
    <span class="hljs-built_in">this</span>.processed = <span class="hljs-literal">true</span>

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.processing) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-built_in">this</span>.getAsyncError()
    &#125;

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> plugin <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.plugins) &#123;
      <span class="hljs-keyword">let</span> promise = <span class="hljs-built_in">this</span>.runOnRoot(plugin)
      <span class="hljs-keyword">if</span> (isPromise(promise)) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-built_in">this</span>.getAsyncError()
      &#125;
    &#125;
    <span class="hljs-comment">// 先收集访问器</span>
    <span class="hljs-built_in">this</span>.prepareVisitors()
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.hasListener) &#123;
      <span class="hljs-keyword">let</span> root = <span class="hljs-built_in">this</span>.result.root
      <span class="hljs-comment">// 如果root脏了，在root节点重新执行插件</span>
      <span class="hljs-keyword">while</span> (!root[isClean]) &#123;
        root[isClean] = <span class="hljs-literal">true</span>
        <span class="hljs-built_in">this</span>.walkSync(root)
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.listeners.OnceExit) &#123;
        <span class="hljs-built_in">this</span>.visitSync(<span class="hljs-built_in">this</span>.listeners.OnceExit, root)
      &#125;
    &#125;

    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.result
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新版插件支持访问器，访问器有两种类型：Enter 和 Exit。Once，Root，AtRule，Rule，Declaration，Comment等会在处理子节点之前调用，OnceExit，RootExit，AtRuleExit...等会在所有子节点处理完成后调用。其中 Declaration 和 AtRule 支持属性的监听，比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">opts = &#123;&#125;</span>) =></span> &#123;
    <span class="hljs-attr">Declaration</span>: &#123;
        <span class="hljs-attr">color</span>: <span class="hljs-function"><span class="hljs-params">decl</span> =></span> &#123;&#125;
        <span class="hljs-string">'*'</span>: <span class="hljs-function"><span class="hljs-params">decl</span> =></span> &#123;&#125;
    &#125;,
    <span class="hljs-attr">AtRule</span>: &#123;
        <span class="hljs-attr">media</span>: <span class="hljs-function"><span class="hljs-params">atRule</span> =></span> &#123;&#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">Rule</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>prepareVisitors 方法会搜集这些访问器，添加到 listeners 中，以上面的代码为例，会添加Declaration-color，Declaration*，AtRule-media，Rule等访问器。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">prepareVisitors</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.listeners = &#123;&#125;
    <span class="hljs-keyword">let</span> add = <span class="hljs-function">(<span class="hljs-params">plugin, type, cb</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.listeners[type]) <span class="hljs-built_in">this</span>.listeners[type] = []
      <span class="hljs-built_in">this</span>.listeners[type].push([plugin, cb])
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> plugin <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.plugins) &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> plugin === <span class="hljs-string">'object'</span>) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> event <span class="hljs-keyword">in</span> plugin) &#123;
          <span class="hljs-keyword">if</span> (!NOT_VISITORS[event]) &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> plugin[event] === <span class="hljs-string">'object'</span>) &#123;
              <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> filter <span class="hljs-keyword">in</span> plugin[event]) &#123;
                <span class="hljs-keyword">if</span> (filter === <span class="hljs-string">'*'</span>) &#123;
                  add(plugin, event, plugin[event][filter])
                &#125; <span class="hljs-keyword">else</span> &#123;
                  add(
                    plugin,
                    event + <span class="hljs-string">'-'</span> + filter.toLowerCase(),
                    plugin[event][filter]
                  )
                &#125;
              &#125;
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> plugin[event] === <span class="hljs-string">'function'</span>) &#123;
              add(plugin, event, plugin[event])
            &#125;
          &#125;
        &#125;
      &#125;
    &#125;
    <span class="hljs-built_in">this</span>.hasListener = <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">this</span>.listeners).length > <span class="hljs-number">0</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 walkSync 过程中，会判断该节点可以拥有的访问器类型，如果是 CHILDREN 则递归调用子节点，如果是其他可执行的访问器比如 Rule，则会执行访问器。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-title">walkSync</span>(<span class="hljs-params">node</span>)</span> &#123;
    node[isClean] = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">let</span> events = getEvents(node)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> event <span class="hljs-keyword">of</span> events) &#123;
      <span class="hljs-keyword">if</span> (event === CHILDREN) &#123;
        <span class="hljs-keyword">if</span> (node.nodes) &#123;
          node.each(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (!child[isClean]) <span class="hljs-built_in">this</span>.walkSync(child)
          &#125;)
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">let</span> visitors = <span class="hljs-built_in">this</span>.listeners[event]
        <span class="hljs-keyword">if</span> (visitors) &#123;
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.visitSync(visitors, node.toProxy())) <span class="hljs-keyword">return</span>
        &#125;
      &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在节点上执行一些有副作用的操作，比如append、prepend、remove、insertBefore、insertAfter等，会循环向上标记副作用<code>node[isClean] = false</code>，直到<code>root[isClean] = false</code>。会导致再次执行插件，甚至会导致死循环。</p>
<h3 data-id="heading-8">5. stringifier</h3>
<p>stringifier 从 root 开始，层序遍历 AST 树，根据节点类型，拼接节点的数据为字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// stringifier.js 简化代码</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Stringifier</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">builder</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.builder = builder
  &#125;
  <span class="hljs-function"><span class="hljs-title">stringify</span>(<span class="hljs-params">node, semicolon</span>)</span> &#123;
    <span class="hljs-comment">// 调用对应类型节点</span>
    <span class="hljs-built_in">this</span>[node.type](node, semicolon)
  &#125;
  <span class="hljs-comment">// root节点处理</span>
  <span class="hljs-function"><span class="hljs-title">root</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.body(node)
    <span class="hljs-keyword">if</span> (node.raws.after) <span class="hljs-built_in">this</span>.builder(node.raws.after)
  &#125;
  <span class="hljs-comment">// root节点子节点处理</span>
   <span class="hljs-function"><span class="hljs-title">body</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-keyword">let</span> last = node.nodes.length - <span class="hljs-number">1</span>
    <span class="hljs-keyword">while</span> (last > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">if</span> (node.nodes[last].type !== <span class="hljs-string">'comment'</span>) <span class="hljs-keyword">break</span>
      last -= <span class="hljs-number">1</span>
    &#125;

    <span class="hljs-keyword">let</span> semicolon = <span class="hljs-built_in">this</span>.raw(node, <span class="hljs-string">'semicolon'</span>)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < node.nodes.length; i++) &#123;
      <span class="hljs-keyword">let</span> child = node.nodes[i]
      <span class="hljs-keyword">let</span> before = <span class="hljs-built_in">this</span>.raw(child, <span class="hljs-string">'before'</span>)
      <span class="hljs-keyword">if</span> (before) <span class="hljs-built_in">this</span>.builder(before)
      <span class="hljs-built_in">this</span>.stringify(child, last !== i || semicolon)
    &#125;
  &#125;
  <span class="hljs-comment">// comment类型节点拼接</span>
  <span class="hljs-function"><span class="hljs-title">comment</span>(<span class="hljs-params">node</span>)</span> &#123;&#125;
  <span class="hljs-comment">// decl类型节点拼接</span>
  <span class="hljs-function"><span class="hljs-title">decl</span>(<span class="hljs-params">node, semicolon</span>)</span> &#123;&#125;
  <span class="hljs-comment">// rule类型节点拼接</span>
  <span class="hljs-function"><span class="hljs-title">rule</span>(<span class="hljs-params">node</span>)</span> &#123;&#125;
  <span class="hljs-comment">// at-rule类型节点拼接</span>
  <span class="hljs-function"><span class="hljs-title">atrule</span>(<span class="hljs-params">node, semicolon</span>)</span> &#123;&#125;
  <span class="hljs-comment">// block节点处理，rule，at-rule(@media等)</span>
  <span class="hljs-function"><span class="hljs-title">block</span>(<span class="hljs-params">node, start</span>)</span>&#123;&#125;
  <span class="hljs-comment">// raw信息处理</span>
  <span class="hljs-function"><span class="hljs-title">raw</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>root、body、comment、decl、rule、atrule、block、raw等是不同类型节点、信息的字符串拼接函数。
整个过程从root开始，做层序遍历，root→body→rule/atrule/comment/decl，然后通过 builder 拼接字符串。builder 是一个拼接函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> builder = <span class="hljs-function">(<span class="hljs-params">str, node, type</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.css += str
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">插件plugins</h2>
<h3 data-id="heading-10">1. 老写法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> postcss = <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss'</span>);

<span class="hljs-built_in">module</span>.exports = postcss.plugin(<span class="hljs-string">'postcss-plugin-old'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">opts</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">root</span>) </span>&#123;
    root.walkRules(<span class="hljs-function">(<span class="hljs-params">rule</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (rule.selector === <span class="hljs-string">'body'</span>) &#123;
        rule.append(postcss.decl(&#123; <span class="hljs-attr">prop</span>: <span class="hljs-string">'margin'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'0'</span> &#125;));
        rule.append(postcss.decl(&#123; <span class="hljs-attr">prop</span>: <span class="hljs-string">'font-size'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'14px'</span> &#125;));
      &#125;
    &#125;);
  &#125;;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>老写法需要引入 postcss，所以插件需要将 postcss 设置为 peerDependence，然后使用 postcss 的 api 去操作 AST。</p>
<h3 data-id="heading-11">2. 新写法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 使用symbol标记处理过的节点</span>
<span class="hljs-keyword">const</span> processd = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'processed'</span>);
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">opts = &#123;&#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">postcssPlugin</span>: <span class="hljs-string">'postcss-plugin-new'</span>,  
    <span class="hljs-function"><span class="hljs-title">Once</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
    <span class="hljs-function"><span class="hljs-title">OnceExit</span>(<span class="hljs-params">root</span>)</span> &#123;
      root.walkDecls(<span class="hljs-function">(<span class="hljs-params">decl</span>) =></span> &#123;
        <span class="hljs-comment">// 删除节点</span>
        <span class="hljs-keyword">if</span> (decl.prop === <span class="hljs-string">'color'</span>) &#123;
          decl.value = <span class="hljs-string">'#ee3'</span>;
        &#125;
      &#125;);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">Rule</span>(<span class="hljs-params">rule, &#123; Declaration &#125;</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!rule[processd]) &#123;
        <span class="hljs-keyword">if</span> (rule.selector === <span class="hljs-string">'body'</span>) &#123;
          rule.append(<span class="hljs-keyword">new</span> Declaration(&#123; <span class="hljs-attr">prop</span>: <span class="hljs-string">'color'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'#333'</span> &#125;));
        &#125;
        rule[processd] = <span class="hljs-literal">true</span>;
      &#125;
    &#125;,
    <span class="hljs-attr">Declaration</span>: &#123;
      <span class="hljs-attr">padding</span>: <span class="hljs-function">(<span class="hljs-params">decl</span>) =></span> &#123;&#125;,
      <span class="hljs-attr">margin</span>: <span class="hljs-function">(<span class="hljs-params">decl</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (decl.value === <span class="hljs-string">'0'</span>) &#123;
          decl.value = <span class="hljs-string">'10px'</span>;
        &#125;
      &#125;,
    &#125;,
    <span class="hljs-function"><span class="hljs-title">DeclarationExit</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
    <span class="hljs-function"><span class="hljs-title">prepare</span>(<span class="hljs-params">result</span>)</span>&#123;
        <span class="hljs-keyword">const</span> variables = &#123;&#125;;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-function"><span class="hljs-title">Declaration</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
            <span class="hljs-function"><span class="hljs-title">OnceExit</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
        &#125;
    &#125;
  &#125;;
&#125;;
<span class="hljs-built_in">module</span>.exports.postcss = <span class="hljs-literal">true</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新写法不再需要引入 postcss，而且新增了访问器（Visitor）。</p>
<ul>
<li>访问器有 Enter 和 Exit 两种，比如 Declaration 会在访问 decl 节点时执行，DeclarationExit 会在所有 Declaration 访问器处理完之后再处理。</li>
<li>可以利用 prepare() 动态生成访问器。</li>
<li>访问器的第一个参数是访问的节点 node，可以直接调用 node 的方法进行操作。</li>
<li>访问器的第二个参数是&#123; ...postcss, result: this.result, postcss &#125;，方便调用 postcss 上的方法。</li>
</ul>
<p>更多可以参考官方文档 <a href="https://github.com/postcss/postcss/blob/main/docs/writing-a-plugin.md" target="_blank" rel="nofollow noopener noreferrer">write-a-plugin</a></p>
<h2 data-id="heading-12">语法syntax</h2>
<p>postcss-less 和 postcss-scss 都属于 syntax，只能识别这种语法，然后进行转换，并不会编译生成css</p>
<p>内部实现也都是继承 Tokenizer 和 Parser 类，并重写内部部分方法。</p>
<p>比如 css 是不支持//注释得，如果我们不指定 syntax 为 postcss-scss，postcss会因为不识别//而报错CssSyntaxError: Unknown word，如果写一个 syntax 支持这种语法呢？</p>
<ol>
<li>首先 tokenizer 需要识别//为 comment 类型 token</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">nextToken</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-comment">// ...</span>
     <span class="hljs-keyword">if</span>()&#123;
     &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (code === SLASH && n === SLASH) &#123;
      RE_NEW_LINE.lastIndex = pos + <span class="hljs-number">1</span>
      RE_NEW_LINE.test(css)
      <span class="hljs-keyword">if</span> (RE_NEW_LINE.lastIndex === <span class="hljs-number">0</span>) &#123;
        next = css.length - <span class="hljs-number">1</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        next = RE_NEW_LINE.lastIndex - <span class="hljs-number">2</span>
      &#125;
    
      content = css.slice(pos, next + <span class="hljs-number">1</span>)
      <span class="hljs-comment">// inline表示是//注释</span>
      currentToken = [<span class="hljs-string">'comment'</span>, content, pos, next, <span class="hljs-string">'inline'</span>]
    
      pos = next
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>然后 parser 需要将其构建为 node 节点，并存储 source，raws 等信息。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ProParser</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parser</span></span>&#123;
    comment (token) &#123;
        <span class="hljs-keyword">if</span> (token[<span class="hljs-number">4</span>] === <span class="hljs-string">'inline'</span>) &#123;
            <span class="hljs-keyword">let</span> node = <span class="hljs-keyword">new</span> Comment()
            <span class="hljs-built_in">this</span>.init(node, token[<span class="hljs-number">2</span>])
            node.raws.inline = <span class="hljs-literal">true</span>
            <span class="hljs-keyword">let</span> pos = <span class="hljs-built_in">this</span>.input.fromOffset(token[<span class="hljs-number">3</span>])
            node.source.end = &#123; <span class="hljs-attr">offset</span>: token[<span class="hljs-number">3</span>], <span class="hljs-attr">line</span>: pos.line, <span class="hljs-attr">column</span>: pos.col       &#125;
            
            <span class="hljs-keyword">let</span> text = token[<span class="hljs-number">1</span>].slice(<span class="hljs-number">2</span>)
            <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/^\s*$/</span>.test(text)) &#123;
                node.text = <span class="hljs-string">''</span>
                node.raws.left = text
                node.raws.right = <span class="hljs-string">''</span>
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">let</span> match = text.match(<span class="hljs-regexp">/^(\s*)([^]*\S)(\s*)$/</span>)
                <span class="hljs-keyword">let</span> fixed = match[<span class="hljs-number">2</span>].replace(<span class="hljs-regexp">/(\*\/|\/\*)/g</span>, <span class="hljs-string">'*//*'</span>)
                node.text = fixed
                node.raws.left = match[<span class="hljs-number">1</span>]
                node.raws.right = match[<span class="hljs-number">3</span>]
                node.raws.text = match[<span class="hljs-number">2</span>]
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">super</span>.comment(token)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>最后 stringifier 需要将其拼接为字符串</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ProStringifier</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Stringifier</span> </span>&#123;
     comment (node) &#123;
        <span class="hljs-keyword">let</span> left = <span class="hljs-built_in">this</span>.raw(node, <span class="hljs-string">'left'</span>, <span class="hljs-string">'commentLeft'</span>)
        <span class="hljs-keyword">let</span> right = <span class="hljs-built_in">this</span>.raw(node, <span class="hljs-string">'right'</span>, <span class="hljs-string">'commentRight'</span>)
    
        <span class="hljs-keyword">if</span> (node.raws.inline) &#123;
          <span class="hljs-keyword">let</span> text = node.raws.text || node.text
          <span class="hljs-built_in">this</span>.builder(<span class="hljs-string">'//'</span> + left + text + right, node)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">this</span>.builder(<span class="hljs-string">'/*'</span> + left + node.text + right + <span class="hljs-string">'*/'</span>, node)
        &#125;
     &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">解决开篇</h2>
<p>针对开篇的场景，思路是：</p>
<ol>
<li>根据 selector 拆分，比如<code>.a .b&#123;&#125;</code>拆分成<code>.a&#123;&#125;，.b&#123;&#125;</code>，并将前后同名 selector 的 rule 的 declaration 进行合并。</li>
<li>对 selector 进行 <code>split(' ')</code>，<code>length>2</code> 的进行裁剪处理</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">options = &#123;&#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">postcssPlugin</span>: <span class="hljs-string">'postcss-plugin-crop-css'</span>,
    Once (root, &#123; postcss &#125;) &#123;
      <span class="hljs-keyword">const</span> selectorRuleMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
      root.walkRules(<span class="hljs-function">(<span class="hljs-params">rule</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> &#123; selector &#125; = rule
        <span class="hljs-keyword">const</span> selectorUnits = selector.split(<span class="hljs-string">','</span>)
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> selectorUnit <span class="hljs-keyword">of</span> selectorUnits) &#123;
          <span class="hljs-keyword">let</span> selectorUnitArr = selectorUnit.split(<span class="hljs-string">' '</span>)
          <span class="hljs-comment">// 选择器超过两层，报错</span>
          <span class="hljs-keyword">if</span> (selectorUnitArr.length > <span class="hljs-number">2</span>) &#123;
            <span class="hljs-keyword">throw</span> rule.error(<span class="hljs-string">'no more than two nested levels'</span>)
          &#125;
          <span class="hljs-keyword">const</span> selectorCrop = selectorUnitArr.join(<span class="hljs-string">' '</span>).replace(<span class="hljs-string">'\n'</span>, <span class="hljs-string">''</span>)
          <span class="hljs-keyword">const</span> existSelectorRule = selectorRuleMap.get(selectorCrop)
          <span class="hljs-keyword">const</span> nodes = existSelectorRule ? [existSelectorRule.nodes, rule.nodes] : rule.nodes
          <span class="hljs-keyword">const</span> newRule = <span class="hljs-keyword">new</span> postcss.Rule(&#123;
            <span class="hljs-attr">selector</span>: selectorCrop,
            <span class="hljs-attr">source</span>: rule.source,
            nodes
          &#125;)
          selectorRuleMap.set(selectorCrop, newRule)
        &#125;
        rule.remove()
      &#125;)
      selectorRuleMap.forEach(<span class="hljs-function"><span class="hljs-params">selectorRule</span> =></span> &#123;
        root.append(selectorRule)
      &#125;)
    &#125;
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports.postcss = <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">参考</h2>
<ol>
<li><a href="https://github.com/postcss/postcss" target="_blank" rel="nofollow noopener noreferrer">postcss</a></li>
</ol>
<h2 data-id="heading-15">广告</h2>
<p>字节跳动游戏发行&小游戏前端组有坑位，简历请发到<a href="mailto:wangyichen.33@bytedance.com">wangyichen.33@bytedance.com</a></p></div>  
</div>
            