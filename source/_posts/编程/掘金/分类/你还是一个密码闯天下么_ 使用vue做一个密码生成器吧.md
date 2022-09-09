
---
title: '你还是一个密码闯天下么_ 使用vue做一个密码生成器吧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efe0596e6ca94fb89ca3188ba421afad~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 23:03:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efe0596e6ca94fb89ca3188ba421afad~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;font-family:-apple-system,system-ui,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial;color:#00325e&#125;.markdown-body ::selection&#123;background-color:#00325e;color:#fff&#125;.markdown-body blockquote&#123;padding:10px 20px;background-color:#fffaf0;box-shadow:0 3px 10px 0 rgba(255,172,194,.24);border:1px solid #f3ca8e;transition:all .2s;margin:1em 0;border-radius:5px&#125;.markdown-body blockquote p&#123;font-size:14px;line-height:25px;color:#795548&#125;.markdown-body blockquote p:last-child&#123;margin:0&#125;.markdown-body blockquote:hover&#123;border-color:#ff9800;background-color:#fff8e0;box-shadow:0 6px 10px -5px rgba(225,173,98,.3803921569)&#125;.markdown-body blockquote code&#123;color:#ff502c&#125;.markdown-body pre&#123;border:1px solid #8cc0f3;box-shadow:0 3px 10px 0 rgba(255,198,198,.28);border-radius:5px;transition:all .2s;overflow-x:auto;white-space:pre-wrap&#125;.markdown-body pre:hover&#123;border-color:#6d9dce&#125;.markdown-body pre>code&#123;padding:10px 20px;color:#00325e;background:#f0f8ff;font-size:12px;line-height:1.6;display:block&#125;.markdown-body code&#123;background:#f6fbff;color:#0b5393;padding:2px 4px;border-radius:4px;font-size:12px&#125;.markdown-body p&#123;font-size:14px;line-height:28px;text-align:justify;margin-bottom:17px;color:#595959&#125;.markdown-body a&#123;color:#00325e;text-decoration:none&#125;.markdown-body a:after&#123;content:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAQdJREFUKFNt0DtLA0EUBeBzZle0Eks7rcUfEfBRCha7NorYa6NmVJzgyi4smUgKtdZGCJktLMVH4Y8QeztLWyE7VyLEuNFbXj4Oh0P8c8mZm+uJrEN4BJFTeP/MUVe3bnocfALwkOlo1zS7iZAzf6Cx7oXgbaqjxiDEWCcVaGyxQ8pSWo9XhqhoQ/xUFbaKjhe5V+CmR7mnSplEEF6GSmJ+F/d0KHvbCIIJCLc85U6BC5mONgbJNM3uFag++sX7z8O8MzsWBucifMx0dDGE1kmm458KDVukAlnNdDz/exEeW3dNkbfsYC0xtmgDWP6ELLZ0/F6BJu/UoFQN5AkoeUjeJPvx6+i+X5Sjah4tA6gYAAAAAElFTkSuQmCC);margin-left:2px&#125;.markdown-body a:hover&#123;box-shadow:0 1px&#125;.markdown-body table&#123;max-width:100%;border-collapse:collapse;border-spacing:0;box-shadow:0 3px 10px 0 rgba(255,238,172,.24);transition:all .2s&#125;.markdown-body table:hover&#123;box-shadow:0 3px 10px 0 rgba(185,169,103,.24)&#125;.markdown-body table tr th&#123;border:1px solid #8cc0f3;background-color:#f0f8ff;padding:12px 15px&#125;.markdown-body table tr td&#123;border:1px solid rgba(243,202,142,.4);padding:12px 15px&#125;.markdown-body table tbody tr&#123;transition:all .2s&#125;.markdown-body table tbody tr:hover td&#123;border-color:#f3ca8e;background-color:#fff8e0;z-index:1&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body h1&#123;font-size:20px;margin-top:30px;margin-bottom:10px;padding-left:30px;position:relative&#125;.markdown-body h1>code&#123;font-size:20px&#125;.markdown-body h1:before&#123;content:"🍺";display:block;font-size:18px;width:18px;height:18px;left:0;position:absolute&#125;.markdown-body h2&#123;font-size:18px;margin-top:30px;margin-bottom:10px;padding-left:28px;position:relative&#125;.markdown-body h2>code&#123;font-size:18px&#125;.markdown-body h2:before&#123;content:"🍻";display:block;font-size:16px;width:16px;height:16px;left:0;position:absolute&#125;.markdown-body h3&#123;font-size:16px;margin-top:30px;margin-bottom:10px;padding-left:26px;position:relative&#125;.markdown-body h3>code&#123;font-size:16px&#125;.markdown-body h3:before&#123;content:"🥂";display:block;font-size:14px;width:14px;height:14px;left:0;position:absolute&#125;.markdown-body h4&#123;font-size:14px;margin-top:30px;margin-bottom:10px;padding-left:24px;position:relative&#125;.markdown-body h4>code&#123;font-size:14px&#125;.markdown-body h4:before&#123;content:"🥃";display:block;font-size:12px;width:12px;height:12px;left:0;position:absolute&#125;.markdown-body h5&#123;font-size:12px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h5>code&#123;font-size:12px&#125;.markdown-body h6&#123;font-size:10px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h6>code&#123;font-size:10px&#125;.markdown-body h1,.markdown-body h2&#123;color:#ff502c&#125;.markdown-body hr&#123;height:4px;border:none;margin-top:32px;margin-bottom:32px;background-size:4px 1px;background-image:linear-gradient(270deg,#6d9dce,#8cc0f3 25%,transparent 50%)&#125;.markdown-body hr:nth-child(2n)&#123;background-image:linear-gradient(270deg,#ff9800,#fff8e0 25%,transparent 50%)&#125;.markdown-body ul&#123;padding-inline-start:20px&#125;.markdown-body ul li&#123;list-style-type:"🔸"&#125;.markdown-body ul li li&#123;list-style-type:"◻️"&#125;.markdown-body ul li li li&#123;list-style-type:"▫️"&#125;.markdown-body ol&#123;padding-inline-start:20px&#125;.markdown-body ol ::marker&#123;color:#ff9800&#125;.markdown-body ol,.markdown-body ul&#123;line-height:2em&#125;.markdown-body li&#123;padding-inline-start:1ch&#125;.markdown-body li.task-list-item&#123;list-style:none;padding-inline-start:0&#125;.markdown-body li input&#123;padding-right:2px&#125;.markdown-body li input[type=checkbox i]&#123;appearance:none&#125;.markdown-body li input:before&#123;content:"🟩";display:block;width:13px;height:13px&#125;.markdown-body li input:checked:before&#123;content:"✅"&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
<p>在我们日常工作和生活中，经常一个密码走天下，殊不知这样做，某个网站/app密码泄露后，可能会引起撞库的风险，今天我们尝试使用<code>vue</code>做一个密码生成器，让每个密码都不一样吧，这样安全等级加加加。</p>
<h3 data-id="heading-0">效果展示</h3>
<p>码上掘金</p>
<p><span href="https://code.juejin.cn/pen/7141205652596064270?embed=true" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7141205652596064270" data-src="https://code.juejin.cn/pen/7141205652596064270?embed=true" style="display: none" loading="lazy"></iframe></span></p>
<p>运行后效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efe0596e6ca94fb89ca3188ba421afad~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">初始化项目</h3>
<blockquote>
<p>如果你已经会用【码上掘金】，那么可以跳过该段落，直接跳过看下一段落就好。</p>
</blockquote>
<p>我们打开码上掘金(<a href="https://code.juejin.cn/" target="_blank" title="https://code.juejin.cn/">code.juejin.cn/</a>) ,选择【新建代码片段】【新建空白片段】</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17174dc1748448e49b79a0a4c0022286~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们由于是编写<code>vue</code>，所以得引入外部依赖，点击<code>Script</code>左边的设置按钮，输入<code>vue.js</code>的地址即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ca3151c0613438ab6f27e753cfac761~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff2b5cd1598d4e60a1456b5c6bac63ea~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着，我们再编写<code>vue</code>测试代码，运行看看效果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6461d84166d44f889d5a80a6634370b4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样的话，我们整个项目初始化便算完成了。</p>
<h3 data-id="heading-2">如何拆解项目</h3>
<p>该项目让用户选择密码类型，有 数字、大小写字母 以及 特殊字符， 再让用户选择一个密码长度， 最后是密码生成按钮。整个<code>UI</code>效果如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3393827fcff444ae80ee834161c6117d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着来介绍一下，这个项目最核心的点，是如何生成该密码。目前我们使用的是，建立一个大的字典池，如果用户勾选数字，那么我们就将0-9放入池子中，如果勾选的是大小字母、小写字母，那么我们就将<code>A-Z</code>、<code>a-z</code>放入池子中，如果勾选的是特殊字符，那么我们就将<code>!、"、#、$、%、&、'、( ...</code> 等特殊字符放入池子中。</p>
<p>如果要生成密码，我们将取到长度<code>n</code>，我们做<code>n</code>次循环，每次都在池子中选择一个随机值，最后将结果返回，这就是我们生成的密码了。</p>
<p>好了，现在有一个问题来了，我们是否需要提前定义数字、大写字母、小写字母、以及特殊字符呢？</p>
<p>答案是可以定义，那么你就要这样写了：</p>
<pre><code class="hljs language-ini copyable" lang="ini">let <span class="hljs-attr">lowerArr</span> = [<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>...]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样写的话，有点占用内存，而且写出来很麻烦，我们可以借助<code>ascii</code>来实现该需求，例如，我们要输出<code>a-z</code>:</p>
<p>我们来看看小写字母的<code>ascii</code>。</p>
<p>这里暂不解释编码规则。</p>
<blockquote>
<p>在linux中，可以使用<code>man ascii</code>查看<code>ascii</code>编码。 你还可以使用百度 搜索"<code>ascii</code> 编码" 来获取相关信息。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc16f2e0e17a4c0c85e0f72f6de94ffe~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到，数字97对应的字母，正好的是<code>a</code>，后面以此类推，那么我们就可以使用如下语句打印<code>a-z</code>了：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> <span class="hljs-built_in">id</span>=97;<span class="hljs-built_in">id</span><123;<span class="hljs-built_in">id</span>++) &#123;
    console.log(String.fromCharCode(<span class="hljs-built_in">id</span>))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的<code>ascii</code>表其中<code>97</code>代表<code>a</code>，而<code>122</code>代表<code>z</code>，而<code>String.fromCharCode()</code>函数是将数字转为字符，我们尝试下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68e6643e379a42d38df9187846d2e1c5~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其他字符，包括特殊字符，都是一样的。</p>
<p>我们拿到池子后，只需要遍历传入的个数，然后随机池子中间的字符，就可以完成该需求了。</p>
<p>我们画一个图来解释一下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/358aae02d6b74fe4bf2c2a002c5306d8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">代码编写</h3>
<p>先看<code>html</code>部分</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04d7b0bb6cb64e69a5617d50f038bd62~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>哦，对了，这里有个点来注意一下，<code>checkbox</code>在<code>vue</code>接收中，类型应该为数组，而非字符，对于本项目变量<code>passwdTypes</code>，我们定义的值应当为: <code>passwdTypes: []</code>。</p>
<p>后面便是vue的部分了，我们先来看看定义</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/077a94e4a69b4114996e531737d97f99~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们给定的初始值为 密码长度为12位，密码类型为 数字、大小写字母 以及 特殊字符。</p>
<p>接下来，主要重点在于按钮，所执行的函数部分，代码如下:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">methods</span>:&#123;
  <span class="hljs-title function_">buildPasswd</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">let</span> passwdArray = [];
    <span class="hljs-keyword">let</span> randPass = <span class="hljs-string">""</span>;

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-variable language_">this</span>.<span class="hljs-property">passwdTypes</span>.<span class="hljs-property">length</span>;i++) &#123;
      <span class="hljs-comment">// 数字</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">passwdTypes</span>[i] == <span class="hljs-string">"numbers"</span>) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> id=<span class="hljs-number">48</span>;id<<span class="hljs-number">58</span>;id++) &#123;
          passwdArray.<span class="hljs-title function_">push</span>(<span class="hljs-title class_">String</span>.<span class="hljs-title function_">fromCharCode</span>(id))
        &#125;
      &#125;

      <span class="hljs-comment">// 小写字母</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">passwdTypes</span>[i] == <span class="hljs-string">"lower"</span>) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> id=<span class="hljs-number">97</span>;id<<span class="hljs-number">123</span>;id++) &#123;
          passwdArray.<span class="hljs-title function_">push</span>(<span class="hljs-title class_">String</span>.<span class="hljs-title function_">fromCharCode</span>(id))
        &#125;
      &#125;

      <span class="hljs-comment">// 大写字母</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">passwdTypes</span>[i] == <span class="hljs-string">"upwer"</span>) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> id=<span class="hljs-number">65</span>;id<<span class="hljs-number">91</span>;id++) &#123;
          passwdArray.<span class="hljs-title function_">push</span>(<span class="hljs-title class_">String</span>.<span class="hljs-title function_">fromCharCode</span>(id))
        &#125;
      &#125;

      <span class="hljs-comment">// 特殊字符</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">passwdTypes</span>[i] == <span class="hljs-string">"special"</span>) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> id=<span class="hljs-number">33</span>;id<<span class="hljs-number">47</span>;id++) &#123;
          passwdArray.<span class="hljs-title function_">push</span>(<span class="hljs-title class_">String</span>.<span class="hljs-title function_">fromCharCode</span>(id))
        &#125;
      &#125;
    &#125;

    <span class="hljs-comment">// 生成密码</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> id=<span class="hljs-number">0</span>;id<<span class="hljs-variable language_">this</span>.<span class="hljs-property">passwdLen</span>;id++) &#123;
      <span class="hljs-keyword">let</span> n = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">floor</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>() * passwdArray.<span class="hljs-property">length</span>)
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(n)

      randPass = randPass.<span class="hljs-title function_">concat</span>(passwdArray[n])
    &#125;

    <span class="hljs-comment">// 密码</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">passwd</span> = randPass
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码我们先遍历<code>passwdTypes</code>中的值，而后根据值来将 用户以及选择的数字、大小字母、小写字母 以及 特殊字符 放到桶里面，而后再根据用户输入的密码长度<code>n</code>，来循环<code>n</code>次，每次都在池子里随机选择一个数，从而组装<code>n</code>个长度的密码，再返回到页面上。</p>
<h3 data-id="heading-4">总结</h3>
<p>我们密码生成器就做完了，写的时候，我还知道谁是谁。 写完了，我一瞅<code>id=33;id<47;id++</code>，什么是<code>33</code>，什么是<code>47</code>，我人稍微有点麻，要是再过1个月看这个代码，不知道会不会骂街。不管如何，这个小玩意还是有点意思吧，动动你的小手指，快来试试吧。</p></div>  
</div>
            