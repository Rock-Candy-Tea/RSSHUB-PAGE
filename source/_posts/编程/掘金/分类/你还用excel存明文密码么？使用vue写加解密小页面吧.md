
---
title: '你还用excel存明文密码么？使用vue写加解密小页面吧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e07c3febab4c4b1f8a27f36fd6d742a6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 06:38:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e07c3febab4c4b1f8a27f36fd6d742a6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;font-family:-apple-system,system-ui,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial;color:#00325e&#125;.markdown-body ::selection&#123;background-color:#00325e;color:#fff&#125;.markdown-body blockquote&#123;padding:10px 20px;background-color:#fffaf0;box-shadow:0 3px 10px 0 rgba(255,172,194,.24);border:1px solid #f3ca8e;transition:all .2s;margin:1em 0;border-radius:5px&#125;.markdown-body blockquote p&#123;font-size:14px;line-height:25px;color:#795548&#125;.markdown-body blockquote p:last-child&#123;margin:0&#125;.markdown-body blockquote:hover&#123;border-color:#ff9800;background-color:#fff8e0;box-shadow:0 6px 10px -5px rgba(225,173,98,.3803921569)&#125;.markdown-body blockquote code&#123;color:#ff502c&#125;.markdown-body pre&#123;border:1px solid #8cc0f3;box-shadow:0 3px 10px 0 rgba(255,198,198,.28);border-radius:5px;transition:all .2s;overflow-x:auto;white-space:pre-wrap&#125;.markdown-body pre:hover&#123;border-color:#6d9dce&#125;.markdown-body pre>code&#123;padding:10px 20px;color:#00325e;background:#f0f8ff;font-size:12px;line-height:1.6;display:block&#125;.markdown-body code&#123;background:#f6fbff;color:#0b5393;padding:2px 4px;border-radius:4px;font-size:12px&#125;.markdown-body p&#123;font-size:14px;line-height:28px;text-align:justify;margin-bottom:17px;color:#595959&#125;.markdown-body a&#123;color:#00325e;text-decoration:none&#125;.markdown-body a:after&#123;content:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAQdJREFUKFNt0DtLA0EUBeBzZle0Eks7rcUfEfBRCha7NorYa6NmVJzgyi4smUgKtdZGCJktLMVH4Y8QeztLWyE7VyLEuNFbXj4Oh0P8c8mZm+uJrEN4BJFTeP/MUVe3bnocfALwkOlo1zS7iZAzf6Cx7oXgbaqjxiDEWCcVaGyxQ8pSWo9XhqhoQ/xUFbaKjhe5V+CmR7mnSplEEF6GSmJ+F/d0KHvbCIIJCLc85U6BC5mONgbJNM3uFag++sX7z8O8MzsWBucifMx0dDGE1kmm458KDVukAlnNdDz/exEeW3dNkbfsYC0xtmgDWP6ELLZ0/F6BJu/UoFQN5AkoeUjeJPvx6+i+X5Sjah4tA6gYAAAAAElFTkSuQmCC);margin-left:2px&#125;.markdown-body a:hover&#123;box-shadow:0 1px&#125;.markdown-body table&#123;max-width:100%;border-collapse:collapse;border-spacing:0;box-shadow:0 3px 10px 0 rgba(255,238,172,.24);transition:all .2s&#125;.markdown-body table:hover&#123;box-shadow:0 3px 10px 0 rgba(185,169,103,.24)&#125;.markdown-body table tr th&#123;border:1px solid #8cc0f3;background-color:#f0f8ff;padding:12px 15px&#125;.markdown-body table tr td&#123;border:1px solid rgba(243,202,142,.4);padding:12px 15px&#125;.markdown-body table tbody tr&#123;transition:all .2s&#125;.markdown-body table tbody tr:hover td&#123;border-color:#f3ca8e;background-color:#fff8e0;z-index:1&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body h1&#123;font-size:20px;margin-top:30px;margin-bottom:10px;padding-left:30px;position:relative&#125;.markdown-body h1>code&#123;font-size:20px&#125;.markdown-body h1:before&#123;content:"🍺";display:block;font-size:18px;width:18px;height:18px;left:0;position:absolute&#125;.markdown-body h2&#123;font-size:18px;margin-top:30px;margin-bottom:10px;padding-left:28px;position:relative&#125;.markdown-body h2>code&#123;font-size:18px&#125;.markdown-body h2:before&#123;content:"🍻";display:block;font-size:16px;width:16px;height:16px;left:0;position:absolute&#125;.markdown-body h3&#123;font-size:16px;margin-top:30px;margin-bottom:10px;padding-left:26px;position:relative&#125;.markdown-body h3>code&#123;font-size:16px&#125;.markdown-body h3:before&#123;content:"🥂";display:block;font-size:14px;width:14px;height:14px;left:0;position:absolute&#125;.markdown-body h4&#123;font-size:14px;margin-top:30px;margin-bottom:10px;padding-left:24px;position:relative&#125;.markdown-body h4>code&#123;font-size:14px&#125;.markdown-body h4:before&#123;content:"🥃";display:block;font-size:12px;width:12px;height:12px;left:0;position:absolute&#125;.markdown-body h5&#123;font-size:12px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h5>code&#123;font-size:12px&#125;.markdown-body h6&#123;font-size:10px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h6>code&#123;font-size:10px&#125;.markdown-body h1,.markdown-body h2&#123;color:#ff502c&#125;.markdown-body hr&#123;height:4px;border:none;margin-top:32px;margin-bottom:32px;background-size:4px 1px;background-image:linear-gradient(270deg,#6d9dce,#8cc0f3 25%,transparent 50%)&#125;.markdown-body hr:nth-child(2n)&#123;background-image:linear-gradient(270deg,#ff9800,#fff8e0 25%,transparent 50%)&#125;.markdown-body ul&#123;padding-inline-start:20px&#125;.markdown-body ul li&#123;list-style-type:"🔸"&#125;.markdown-body ul li li&#123;list-style-type:"◻️"&#125;.markdown-body ul li li li&#123;list-style-type:"▫️"&#125;.markdown-body ol&#123;padding-inline-start:20px&#125;.markdown-body ol ::marker&#123;color:#ff9800&#125;.markdown-body ol,.markdown-body ul&#123;line-height:2em&#125;.markdown-body li&#123;padding-inline-start:1ch&#125;.markdown-body li.task-list-item&#123;list-style:none;padding-inline-start:0&#125;.markdown-body li input&#123;padding-right:2px&#125;.markdown-body li input[type=checkbox i]&#123;appearance:none&#125;.markdown-body li input:before&#123;content:"🟩";display:block;width:13px;height:13px&#125;.markdown-body li input:checked:before&#123;content:"✅"&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
<p>相信在座的很多大佬们还在使用<code>excel</code>直接存储明文密码。如果泄漏了，那将是毁灭性的打击哦。本篇文章使用<code>vue</code>实现对数据<strong>最简单</strong>的加解密(这里解释了最简单的加解密，大佬误杠！)，快来使用一下，给你的安全等级加加加吧。</p>
<blockquote>
<p>前端大佬莫笑话，运维小弟献丑了。</p>
</blockquote>
<h3 data-id="heading-0">项目展示</h3>
<p>码上掘金</p>
<p><span href="https://code.juejin.cn/pen/7143474023316324382?embed=true" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7143474023316324382" data-src="https://code.juejin.cn/pen/7143474023316324382?embed=true" style="display: none" loading="lazy"></iframe></span></p>
<p>项目截图</p>
<p>将</p>
<p>“是以圣人处无为之事，行不言之教，万物作焉而不辞，生而不有，为而不恃，功成而弗居。夫惟弗居，是以不去。”</p>
<p>加密。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e07c3febab4c4b1f8a27f36fd6d742a6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解密加密后的字符串</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b97e8e0808ac4dd5be08a4a933f2e43f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">初始化项目</h3>
<blockquote>
<p>如果你已经使用过【码上掘金】这个工具，可以略过本段落，直接看下一段落【项目核心概念】。</p>
</blockquote>
<p>我们打开【码上掘金(<a href="https://code.juejin.cn/" target="_blank" title="https://code.juejin.cn/">code.juejin.cn/</a>)】，创建一个新的【空白片段】。</p>
<p>点击【新建代码片段】【新建空白片段】，我们就可以创建一个空白项目了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b39dee25a330455e856d690f78559127~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们点击<code>Script</code>右侧的设置按钮，可以添加依赖。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c101f2440d374eaaa8261ddaeb085a66~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于我们是编写<code>vue</code>的程序，所以我们添加<code>vue</code>的地址。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8e640c2b5144df99cc03460044a9fe0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而后，我们编写一个最简单的<code>vue</code>实例来验证环境的正确性。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70d59269d04d4513a47726bd58e3d66a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上，我们使用<code>vue</code>来计算一个表达式<code>3+2-5+12</code>，点击运行后，结果为<code>12</code>，由此证明我们已经将环境搭建好了。</p>
<h3 data-id="heading-2">项目核心概念</h3>
<p>其实如果你查看<code>vue</code>代码的编写，会发现项目代码非常简单。由此我们来讲解一下，我们是如何进行加密解密的。其中最核心的概念是异或运算(<code>xor</code>)，符号为: <code>^</code>。</p>
<p>由此，我们介绍下相关原理： 所谓的异或运算是指二进制运算， 如果对应的二进制位相同(同为0或者同为1)的时候，结果为0，否则为1，在进行运算时，高位不足需要补0。</p>
<p>我们来演示一下:
假设我们 <code>12 xor 24 == 20</code> ， 这个<code>20</code>是如何得来的呢? 我们来看下</p>
<p>12的二进制为: <code>1100</code></p>
<p>而24的二进制位: <code>11000</code></p>
<p>由于高位不足需要补0，所以12的二进制同等于 <code>01100</code></p>
<p>所以我们执行异或结果为:</p>
<p>如果二进制位相同，则为0，否则为1。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58646c3c32a34d67be07a0bcb3745f3a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们再将结果<code>10100</code>转换为10进制，结果为: <code>20</code>，所以这就是最终的结果。</p>
<p>我们有了如上的基础，我们再来思考一个问题:</p>
<p><code>(A ^ B) ^ B</code> 应该等于多少呢？</p>
<p>如上式子我们可以写为: <code>A ^ (B ^ B)</code></p>
<p>如果不好计算，我们就带入式子，假设: A 为 <code>0011</code>, B 为<code>1000</code>，而<code>B ^ B</code>可得:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f99d4fa219c447038822f6816eb71b28~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而，<code>A ^ 0</code> ，我们带入可得:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3aaf4be26aa45f2bab1e74c7339a8b1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，<code>A ^ B ^ B == A ^ 0 == A</code></p>
<p>如果我们将<code>B</code>理解为秘钥，那么，可得:</p>
<p><code>A ^ B == C</code>以及<code>C ^ B == A</code>是成立的。</p>
<p>我们以第一个问题来收尾:</p>
<p><code>12 xor 24 == 20</code>和<code>20 xor 24 == 12</code>是成立的，其计算结果如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37fcff87ee7841aaab92c31a5a913216~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>关于异或就暂时介绍到这里。</p>
<h3 data-id="heading-3">页面编码</h3>
<p>关于前端页面，我们想设计出一个内容输入框，2个秘钥输入框，以及一个计算按钮，我们很快就可以写出骨干来，如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c3271b623cc43748457ce1825985acd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>前端页面，较为简单，我们内容框框，使用<code><textarea></code>标签、秘钥和确认秘钥框框我们使用<code>input</code>标签即可 最后的 按钮我们使用<code>button</code>。</p>
<p>我们编写<code>css</code>装饰一下框架，效果为:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38df96b4f9c9492cb86b3e046716f148~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>页面稍微有点丑。</p>
</blockquote>
<h3 data-id="heading-4">vue编码</h3>
<p>由于有了【项目核心概念】的铺垫，所以我们直接开始编写注意事项，而后上代码，由于异或操作对象为二进制，所以我们不能直接操作字符，需要先将字符转为其底层编码，而后再将编码转为字符。</p>
<p>这里介绍一个小例子:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-number">3</span> ^ <span class="hljs-number">5</span> ^ <span class="hljs-number">5</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个结果为: <code>3</code></p>
<p>而</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'a'</span> ^ <span class="hljs-string">'b'</span> ^ <span class="hljs-string">'a'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果为: <code>0</code>，因为它没法处理，我们得将其转化为:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-title class_">String</span>.<span class="hljs-title function_">fromCharCode</span>((<span class="hljs-string">'a'</span>.<span class="hljs-title function_">charCodeAt</span>() ^ <span class="hljs-string">'b'</span>.<span class="hljs-title function_">charCodeAt</span>() ^ <span class="hljs-string">'a'</span>.<span class="hljs-title function_">charCodeAt</span>())))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里才能正常输出结果<code>b</code>。</p>
<p>其中<code>fromCharCode</code>是将编码转换为字符，而<code>charCodeAt</code>是将字符转换为编码。</p>
<p>好了，有了如上的铺垫，我们来看<code>vue</code>代码:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vue</span>(&#123;
  <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-title class_">TextContent</span>: <span class="hljs-string">""</span>,
    <span class="hljs-title class_">SecretKey</span>: <span class="hljs-string">""</span>,
    <span class="hljs-title class_">ReSecretKey</span>: <span class="hljs-string">""</span>,
    <span class="hljs-attr">msg</span>: <span class="hljs-string">"小提示: 秘钥很重要，请记住哦"</span>,
    <span class="hljs-attr">result</span>: <span class="hljs-string">""</span>
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-title function_">sd</span>(<span class="hljs-params"></span>) &#123;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">result</span> = <span class="hljs-string">""</span>
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">msg</span> = <span class="hljs-string">"小提示: 秘钥很重要，请记住哦"</span>

      <span class="hljs-keyword">if</span> (<span class="hljs-string">""</span> == <span class="hljs-variable language_">this</span>.<span class="hljs-property">TextContent</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">msg</span> = <span class="hljs-string">"小提示: 您输入的内容为空"</span>
        <span class="hljs-keyword">return</span>
      &#125;

      <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">SecretKey</span> != <span class="hljs-variable language_">this</span>.<span class="hljs-property">ReSecretKey</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">msg</span> = <span class="hljs-string">"小提示: 您2次输入的密码不相同哦"</span>
        <span class="hljs-keyword">return</span>
      &#125;

      <span class="hljs-keyword">if</span> (<span class="hljs-string">""</span> == <span class="hljs-variable language_">this</span>.<span class="hljs-property">SecretKey</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">msg</span> = <span class="hljs-string">"小提示: 你输入的秘钥为空，将为你指定为默认秘钥"</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">SecretKey</span> = <span class="hljs-string">"T!a4Z)Az"</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">ReSecretKey</span> = <span class="hljs-variable language_">this</span>.<span class="hljs-property">SecretKey</span>
      &#125;

      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-variable language_">this</span>.<span class="hljs-property">TextContent</span>.<span class="hljs-property">length</span>;i++) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">result</span> = <span class="hljs-variable language_">this</span>.<span class="hljs-property">result</span> + <span class="hljs-title class_">String</span>.<span class="hljs-title function_">fromCharCode</span>((<span class="hljs-variable language_">this</span>.<span class="hljs-property">TextContent</span>[i].<span class="hljs-title function_">charCodeAt</span>() ^ <span class="hljs-variable language_">this</span>.<span class="hljs-property">SecretKey</span>[i % <span class="hljs-variable language_">this</span>.<span class="hljs-property">SecretKey</span>.<span class="hljs-property">length</span>].<span class="hljs-title function_">charCodeAt</span>()))
      &#125;
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>TextContent</code>是用户输入的内容，<code>SecretKey</code>、<code>ReSecretKey</code>是秘钥和验证秘钥，<code>msg</code>是程序输出的小提示，最后是<code>result</code>加解密的结果。</p>
<p><code>vue</code>会判断，用户输入的内容为空、秘钥未输入和2次秘钥不相同等。</p>
<p>这些做完之后，会进入到异或运算中，这里有个注意的点为: 当用户输入内容长度 大于 秘钥长度的时候，需要轮训使用秘钥，还记得之前我们在介绍核心概念的时候，说过会高位补齐，那个是已经在进行二进制运算的时候了。 这个是在取字符的二进制呢。</p>
<p>其中轮训使用的算法为遍历的内容的下标对秘钥长度取余: <code>i % this.SecretKey.length</code>，在加上编码转换，所以核心语句是:</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-keyword">this</span>.result = <span class="hljs-keyword">this</span>.result + String.fromCharCode((<span class="hljs-keyword">this</span>.TextContent[i].charCodeAt() ^ <span class="hljs-keyword">this</span>.SecretKey[i % <span class="hljs-keyword">this</span>.SecretKey.length].charCodeAt()))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">测试</h3>
<p>我们拿几个测试案例来测试一下:</p>
<p>加密:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef5d584182d145478bcce4a25f996a53~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解密</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c2b4ca4b0b1462b88988e25f6856f66~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>加密</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8766e7e83fd441338f2366dec8d0cdc7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解密</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/290b2e6bc9c34226837c8db2bf13c8b3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">总结</h3>
<p>正如前文所述，这是一种较为简单的加密，因为它可以通过 明文 和 密文 来推算出 秘钥，如果你的整个交互过程都是使用同一个秘钥的话，且该秘钥也会分享出去给他人使用，那么就很危险了。但是像文章这种，自定义秘钥，安全性还是很高的。</p>
<p>怎么样，好玩吧，动动你的小手指，快来试试吧。</p></div>  
</div>
            