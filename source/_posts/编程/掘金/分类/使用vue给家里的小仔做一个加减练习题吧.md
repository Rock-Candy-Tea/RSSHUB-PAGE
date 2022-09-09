
---
title: '使用vue给家里的小仔做一个加减练习题吧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/184e5b29a0ea43f99d1dcbcf48873a98~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 00:57:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/184e5b29a0ea43f99d1dcbcf48873a98~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;font-family:-apple-system,system-ui,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial;color:#00325e&#125;.markdown-body ::selection&#123;background-color:#00325e;color:#fff&#125;.markdown-body blockquote&#123;padding:10px 20px;background-color:#fffaf0;box-shadow:0 3px 10px 0 rgba(255,172,194,.24);border:1px solid #f3ca8e;transition:all .2s;margin:1em 0;border-radius:5px&#125;.markdown-body blockquote p&#123;font-size:14px;line-height:25px;color:#795548&#125;.markdown-body blockquote p:last-child&#123;margin:0&#125;.markdown-body blockquote:hover&#123;border-color:#ff9800;background-color:#fff8e0;box-shadow:0 6px 10px -5px rgba(225,173,98,.3803921569)&#125;.markdown-body blockquote code&#123;color:#ff502c&#125;.markdown-body pre&#123;border:1px solid #8cc0f3;box-shadow:0 3px 10px 0 rgba(255,198,198,.28);border-radius:5px;transition:all .2s;overflow-x:auto;white-space:pre-wrap&#125;.markdown-body pre:hover&#123;border-color:#6d9dce&#125;.markdown-body pre>code&#123;padding:10px 20px;color:#00325e;background:#f0f8ff;font-size:12px;line-height:1.6;display:block&#125;.markdown-body code&#123;background:#f6fbff;color:#0b5393;padding:2px 4px;border-radius:4px;font-size:12px&#125;.markdown-body p&#123;font-size:14px;line-height:28px;text-align:justify;margin-bottom:17px;color:#595959&#125;.markdown-body a&#123;color:#00325e;text-decoration:none&#125;.markdown-body a:after&#123;content:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAQdJREFUKFNt0DtLA0EUBeBzZle0Eks7rcUfEfBRCha7NorYa6NmVJzgyi4smUgKtdZGCJktLMVH4Y8QeztLWyE7VyLEuNFbXj4Oh0P8c8mZm+uJrEN4BJFTeP/MUVe3bnocfALwkOlo1zS7iZAzf6Cx7oXgbaqjxiDEWCcVaGyxQ8pSWo9XhqhoQ/xUFbaKjhe5V+CmR7mnSplEEF6GSmJ+F/d0KHvbCIIJCLc85U6BC5mONgbJNM3uFag++sX7z8O8MzsWBucifMx0dDGE1kmm458KDVukAlnNdDz/exEeW3dNkbfsYC0xtmgDWP6ELLZ0/F6BJu/UoFQN5AkoeUjeJPvx6+i+X5Sjah4tA6gYAAAAAElFTkSuQmCC);margin-left:2px&#125;.markdown-body a:hover&#123;box-shadow:0 1px&#125;.markdown-body table&#123;max-width:100%;border-collapse:collapse;border-spacing:0;box-shadow:0 3px 10px 0 rgba(255,238,172,.24);transition:all .2s&#125;.markdown-body table:hover&#123;box-shadow:0 3px 10px 0 rgba(185,169,103,.24)&#125;.markdown-body table tr th&#123;border:1px solid #8cc0f3;background-color:#f0f8ff;padding:12px 15px&#125;.markdown-body table tr td&#123;border:1px solid rgba(243,202,142,.4);padding:12px 15px&#125;.markdown-body table tbody tr&#123;transition:all .2s&#125;.markdown-body table tbody tr:hover td&#123;border-color:#f3ca8e;background-color:#fff8e0;z-index:1&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body h1&#123;font-size:20px;margin-top:30px;margin-bottom:10px;padding-left:30px;position:relative&#125;.markdown-body h1>code&#123;font-size:20px&#125;.markdown-body h1:before&#123;content:"🍺";display:block;font-size:18px;width:18px;height:18px;left:0;position:absolute&#125;.markdown-body h2&#123;font-size:18px;margin-top:30px;margin-bottom:10px;padding-left:28px;position:relative&#125;.markdown-body h2>code&#123;font-size:18px&#125;.markdown-body h2:before&#123;content:"🍻";display:block;font-size:16px;width:16px;height:16px;left:0;position:absolute&#125;.markdown-body h3&#123;font-size:16px;margin-top:30px;margin-bottom:10px;padding-left:26px;position:relative&#125;.markdown-body h3>code&#123;font-size:16px&#125;.markdown-body h3:before&#123;content:"🥂";display:block;font-size:14px;width:14px;height:14px;left:0;position:absolute&#125;.markdown-body h4&#123;font-size:14px;margin-top:30px;margin-bottom:10px;padding-left:24px;position:relative&#125;.markdown-body h4>code&#123;font-size:14px&#125;.markdown-body h4:before&#123;content:"🥃";display:block;font-size:12px;width:12px;height:12px;left:0;position:absolute&#125;.markdown-body h5&#123;font-size:12px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h5>code&#123;font-size:12px&#125;.markdown-body h6&#123;font-size:10px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h6>code&#123;font-size:10px&#125;.markdown-body h1,.markdown-body h2&#123;color:#ff502c&#125;.markdown-body hr&#123;height:4px;border:none;margin-top:32px;margin-bottom:32px;background-size:4px 1px;background-image:linear-gradient(270deg,#6d9dce,#8cc0f3 25%,transparent 50%)&#125;.markdown-body hr:nth-child(2n)&#123;background-image:linear-gradient(270deg,#ff9800,#fff8e0 25%,transparent 50%)&#125;.markdown-body ul&#123;padding-inline-start:20px&#125;.markdown-body ul li&#123;list-style-type:"🔸"&#125;.markdown-body ul li li&#123;list-style-type:"◻️"&#125;.markdown-body ul li li li&#123;list-style-type:"▫️"&#125;.markdown-body ol&#123;padding-inline-start:20px&#125;.markdown-body ol ::marker&#123;color:#ff9800&#125;.markdown-body ol,.markdown-body ul&#123;line-height:2em&#125;.markdown-body li&#123;padding-inline-start:1ch&#125;.markdown-body li.task-list-item&#123;list-style:none;padding-inline-start:0&#125;.markdown-body li input&#123;padding-right:2px&#125;.markdown-body li input[type=checkbox i]&#123;appearance:none&#125;.markdown-body li input:before&#123;content:"🟩";display:block;width:13px;height:13px&#125;.markdown-body li input:checked:before&#123;content:"✅"&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
<p>在培养小孩过程中，其中必不可少的是教小孩加减算法题，这是很基础，这是很重要的，可以锻炼其算术思维。但是我们大人忙的时候，没空给小孩出题。于是乎，我们就可以使用<code>vue</code>给小孩写一个加减练习题。</p>
<blockquote>
<p>各位前端大佬不要笑话，运维小弟献丑了。</p>
</blockquote>
<p>项目代码:
<span href="https://code.juejin.cn/pen/7140843847138934822" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7140843847138934822" data-src="https://code.juejin.cn/pen/7140843847138934822" style="display: none" loading="lazy"></iframe></span></p>
<p>项目运行效果:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/184e5b29a0ea43f99d1dcbcf48873a98~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">创建项目</h3>
<p>我们打开码上掘金(<a href="https://code.juejin.cn/" target="_blank" title="https://code.juejin.cn/">code.juejin.cn/</a>) ，选择【新建代码片段】【新建空白片段】</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8e9747d29364edda731106182ef1c66~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>为什么我们这里新建代码片段的时候不直接选择<code>vue2</code>或者<code>vue3</code>的片段呢？ 因为运维小老弟我还不是很会。只会使用<code>js</code>引用<code>vue</code>。</p>
</blockquote>
<p>我们创建新项目后，我们将<code>vue 2</code>的<code>cdn</code>导入进项目中，选择<code>Script</code>右边的设置按钮</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b6331af0be341e3876f221aca766e0f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>点开后，我们将<code>vue</code>的地址填进去。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/022e4c2774654775850512f482d1c400~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，我们编写代码来验证下，<code>vue</code>环境是否可以正常使用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7a5687df403493dbf3ddca74ebfccec~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上，我们写了一个很简单的<code>vue</code>，运行起来后，我们发现是可以拿到<code>world</code>变量的值的。</p>
<p>证明我们环境设置没问题，接下来我们看看整个项目的设计吧。</p>
<h3 data-id="heading-1">设计思路</h3>
<p>我们想做一个比较简单的加减练习册，根据按钮随机更新题目，用户在输入结果后，点击一下别的地方，就开始验证结果，验证结果会给出正确与否，以及小提示，整体设计草图如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/955f9619ce2949a382e2247e3b178352~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上所述，若输入结果为正确的值，则提示√，否则为×。</p>
<p>当题目打错后，我们会输出一个温馨提示，设计如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c349955f915d42f9bfc4bc37727dc077~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然回答正确的时候，也应当提示，类似于： “你真棒”这类的话。</p>
<p>上面，便是我们整个项目的核心功能了，最后再设计一个按钮，用于刷新题目使用，设计图类似于：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83f4444a4d8244f4bc5904c0c6bffe3c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">静态页面编写</h3>
<p>如上，我们已经描述了设计思路，接着，我们可以编写静态页面了。通过设计思路，我们不难看出，在整个页面，我们有按钮来作为刷新题目使用，还有一个输入框，用于用户输入计算的结果，我们来分析下呢：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99b20492906f40a2b65a239a35c59e1d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上，我们可以很容易的编写出静态页面代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    3 + 2  =
    <span class="hljs-tag"><<span class="hljs-name">input</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>温馨小提示: <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span>></span>换题<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行后，效果如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ad5aa7fb54d4b509d4a7caa1a0b876b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上，我们主体框架搭建完毕了，样子不太好看，不要急，我们给穿上<code>CSS</code>外衣就好看了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d946ebf47db46df8b3bb54d9b0bc7b2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这么样，我们加入<code>css</code>样式后，就好看多了吧。</p>
<h3 data-id="heading-3">完成主线代码</h3>
<p>如上，我们静态页面已经写好了，现在我们接入<code>vue.js</code>，让它变为动态的，那么我们应该如何写呢？ 我们最简单的想法是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47ba1905453b4134bb3965b3b0a85132~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们使用计算属性，来算出<code>n</code>和<code>m</code>正确的值，再让它和用户输入的值做对比，如果一致，则证明计算正确，否则计算错误。</p>
<p>基于此，我们修改下代码</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad25973e41b54f54a3a991cb39a53b80~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上代码我们加入了<code>vue</code>变量,<code>m</code>,<code>n</code>,<code>op</code>最后还定义了一个计算变量<code>realResult</code>。</p>
<p>我们使用<code>v-model</code>来活动用户的结果输入，编写如下</p>
<pre><code class="hljs language-js copyable" lang="js">v-model.<span class="hljs-property">lazy</span>=<span class="hljs-string">"inputResult"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>lazy</code>参数表示只有聚焦离开了输入框，再传参值<code>vue</code>中，相应的，我们在<code>vue.data</code>中也应该写上该变量才行。</p>
<p>我们定义完该变量后，我们可以开始写监听器了，代码如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-attr">watch</span>: &#123;
  <span class="hljs-attr">inputResult</span>: &#123;
    <span class="hljs-title function_">handler</span>(<span class="hljs-params">newValue</span>)&#123;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">ok</span> = <span class="hljs-literal">false</span>
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">fail</span> = <span class="hljs-literal">false</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">realResult</span> == newValue) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">ok</span> = <span class="hljs-literal">true</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">result_text</span> = <span class="hljs-string">"恭喜你，回答正确，结果为: "</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">realResult</span> + <span class="hljs-string">"。"</span>
      &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">fail</span> = <span class="hljs-literal">true</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">result_text</span> = <span class="hljs-string">"你小子，回答错了，正确的结果为: "</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">realResult</span> + <span class="hljs-string">"。"</span>
      &#125; 
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于<code>ok</code>、<code>fail</code>等，不在主线内，我们后续会说明。</p>
<p>最后我们就只剩下一个换题了，换题由于是按钮，所以我们可以写一个函数来操作，我们将此函数命名为: <code>changeTitle</code>，我们编写如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-attr">methods</span>: &#123;
  <span class="hljs-title function_">changeTitle</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">result_text</span> = <span class="hljs-string">"请删掉上一题的答案继续答题"</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">ok</span> = <span class="hljs-literal">false</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">fail</span> = <span class="hljs-literal">false</span>
    
    <span class="hljs-keyword">const</span> ops = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">floor</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>() * <span class="hljs-number">2</span>)
    <span class="hljs-keyword">if</span> (ops == <span class="hljs-number">0</span>) &#123;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">op</span> = <span class="hljs-string">"+"</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">op</span> = <span class="hljs-string">"-"</span>
    &#125;

    <span class="hljs-variable language_">this</span>.<span class="hljs-property">n1</span> = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">floor</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>() * <span class="hljs-number">100</span>)
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">n2</span> = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">floor</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>() * <span class="hljs-number">100</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">完善边角料</h3>
<p>还记得我们在设计思路的时候，提及到了√和×么？ 以及温馨小提示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40f8d6b0b9134960948581fb8acb45a6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们可以使用<code>vue</code>中的<code>v-if</code>来完成，具体代码如下:</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"ok"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"result_ok"</span> <span class="hljs-attr">disabled</span>=<span class="hljs-string">"disable"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"√"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"fail"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"result_fail"</span> <span class="hljs-attr">disabled</span>=<span class="hljs-string">"disable"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"×"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>温馨小提示: &#123;&#123;result_text&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于这里的细节，可以看代码，这里不再赘述。</p>
<h3 data-id="heading-5">总结</h3>
<p>学习了一段时间前端，不由感叹一句，前端是真的太卷了，知识点太多了，我就只会写<code>html</code>和一点点的<code>vue.js</code>，遇到<code>css</code>就只能抓瞎了，纯粹的面向网页编程，文章写的不是很好，涉及的点，有点多，却不想放弃任何一点，所以看起来，有点杂乱。好咯，就这样咯，快来动动你的小手指，给你家小孩搞一个练习题吧。</p></div>  
</div>
            