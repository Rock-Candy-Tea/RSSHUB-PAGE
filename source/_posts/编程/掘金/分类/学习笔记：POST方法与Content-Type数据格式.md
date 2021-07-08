
---
title: '学习笔记：POST方法与Content-Type数据格式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecaf6ed325d74fa4b606f5d7929df329~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 07:23:05 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecaf6ed325d74fa4b606f5d7929df329~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">序言</h1>
<p>之所以写下此篇笔记，是因为前几天在与后端联调的时候，双方对数据传递的格式出现了分歧，正当我想为自己辩护时，却发现自己竟然连几种常见的content-type都搞不清，进而被后端嘲讽自己连传什么格式都搞不清。</p>
<p>希望通过这篇笔记，能让自己牢记不爱总结、思考的下场。</p>
<h1 data-id="heading-1">POST</h1>
<p>HTTP <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTTP%2FMethods%2FPOST" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Methods/POST" ref="nofollow noopener noreferrer">POST</a> 方法 发送数据给服务器. 请求主体的类型由 Content-Type 首部指定。post请求除了使用html表单发送，还可以通过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequest" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest" ref="nofollow noopener noreferrer">AJAX</a>的方式发送。</p>
<pre><code class="copyable">POST / HTTP/1.1
Host: foo.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 13

say=Hi&to=Mom
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">Content-Type</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTTP%2FHeaders%2FContent-Type" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Content-Type" ref="nofollow noopener noreferrer">Content-Type</a>实体头部用于指示资源的MIME类型。在响应中，Content-Type标头告诉客户端实际返回的内容的内容类型。</p>
<p>在原生的form表单中，可以通过enctype这个字段指定content-type类型。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">action</span>=<span class="hljs-string">"/"</span> <span class="hljs-attr">method</span>=<span class="hljs-string">"post"</span> <span class="hljs-attr">enctype</span>=<span class="hljs-string">"multipart/form-data"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"description"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"some text"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"file"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"myFile"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span>></span>Submit<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在前后端的通信中，我们通常通过以下三种content-type类型定义数据格式，分别是application/x-www-form-urlencoded、multipart/form-data和application/json，下面我来分别介绍一下。</p>
<h2 data-id="heading-3">application/x-www-form-urlencoded</h2>
<pre><code class="hljs language-http copyable" lang="http"><span class="hljs-attribute">content-type</span><span class="hljs-punctuation">: </span>application/x-www-form-urlencoded; charset=UTF-8
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从urlencoded这个单词就可以看出，它的编码规则和url编码规则是一样的。在原生的form标签中，如果不显式的指定enctype属性，默认发送的数据就是application/x-www-form-urlencoded。如果你查看通过这种编码规则发送的请求，数据是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js">productId=<span class="hljs-number">94608</span>&folderId=5fa00a2ce4b01e990ecee97b&skuId=<span class="hljs-number">440535</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在经过url编码过后，会变成这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">encodeURIComponent</span>(<span class="hljs-string">"productId=94608&folderId=5fa00a2ce4b01e990ecee97b&skuId=440535"</span>)
<span class="hljs-comment">// "productId%3D94608%26folderId%3D5fa00a2ce4b01e990ecee97b%26skuId%3D440535"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是感觉很眼熟？因为他和get方法在url中传参是一样的，每组key/val通过&连接。这种数据格式和直接使用url的区别，只是把数据放在body里。</p>
<p>关于url编码，阮一峰大佬写过一篇博客，感兴趣的可以看一下<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2010%2F02%2Furl_encoding.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.ruanyifeng.com/blog/2010/02/url_encoding.html" ref="nofollow noopener noreferrer">关于URL编码</a></p>
<h2 data-id="heading-4">multipart/form-data</h2>
<pre><code class="hljs language-http copyable" lang="http"><span class="hljs-attribute">content-type</span><span class="hljs-punctuation">: </span>multipart/form-data; boundary=----WebKitFormBoundaryllpanFebLMmhdFGN
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你想要上传图片这种二进制文件，就必须用multipart/form-data格式传输数据，body通过boundary字段封装消息的多个部分的边界。</p>
<p>关于为什么上传二进制文件一定要通过multipart/form-data而不是application/x-www-form-urlencoded，是因为后者针对非字母或者数字的字符会使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FGlossary%2Fpercent-encoding" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Glossary/percent-encoding" ref="nofollow noopener noreferrer">Percent-encoding</a>，直接导致没法对二进制数据编码。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecaf6ed325d74fa4b606f5d7929df329~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当你在js中使用new <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFormData%2FFormData" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/FormData/FormData" ref="nofollow noopener noreferrer">FormData()</a>的时候，最终传输的数据就是multipart/form-data这种格式</p>
<h2 data-id="heading-5">application/json</h2>
<pre><code class="hljs language-http copyable" lang="http"><span class="hljs-attribute">content-type</span><span class="hljs-punctuation">: </span>application/json; charset=UTF-8
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最简单也最常见的格式，适合结构化数据，尤其是数据层级较深的时候。由于前后端针对json格式的序列化与反序列化都是十分便捷，因此有大量数据交互场景是通过json格式传递数据的。</p>
<p>提交表单的场景中，除非涉及到文件上传，否则基本都是通过application/json这种数据提交表单信息。</p>
<p>值得注意的是，application/json会触发<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTTP%2FCORS" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS" ref="nofollow noopener noreferrer">CORS预检请求</a>，而上面提到的两种并不会。</p>
<pre><code class="hljs language-js copyable" lang="js">networkService.post(&#123;
  <span class="hljs-attr">url</span>: <span class="hljs-string">'xxx/yyy'</span>,
  <span class="hljs-attr">data</span>: <span class="hljs-built_in">JSON</span>.stringify(data);
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.error(e);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            