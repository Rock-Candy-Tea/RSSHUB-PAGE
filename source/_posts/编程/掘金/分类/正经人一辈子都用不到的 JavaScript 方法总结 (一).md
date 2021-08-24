
---
title: '正经人一辈子都用不到的 JavaScript 方法总结 (一)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66be095462ac4986815bc7569b4ae7ad~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 05:29:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66be095462ac4986815bc7569b4ae7ad~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第24天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>假如有这样一个需求：要求将给定的一个文件路径 <code>D:\bianchengsanmei\blogs\categories\JavaScript</code> 在页面展示出来。</p>
<p>最基本的实现方法可能是下面这个：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span> = <span class="hljs-string">"container"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> filePath = <span class="hljs-string">"D:\bianchengsanmei\blogs\categories\JavaScript"</span>;
<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#container"</span>).innerText = filePath;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果真能这么简单就实现的话，那我这篇文章到这里就结束了，这是要写个寂寞吗？</p>
<p>结束是不可能结束的，不信，你看看输出结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66be095462ac4986815bc7569b4ae7ad~tplv-k3u1fbpfcp-watermark.image" alt="image-20210824204649951" loading="lazy" referrerpolicy="no-referrer"></p>
<p>显然，我们很多时候会忘记有<strong>转义符</strong>这回事。</p>
<blockquote>
<p>因为在 HTML 网页里，像 <code>>、<、</code> 等字符是有特殊含义的，再加上有些字符在 ASCII 字符集中没有定义，因此需要使用转义字符串来表示。</p>
</blockquote>
<p>要想正确显示，应该这么写：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> filePath = <span class="hljs-string">"D:\\bianchengsanmei\\blogs\\categories\\JavaScript"</span>;
<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#container"</span>).innerText = filePath;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转义符 + "\" 表示的是字符串 \。</p>
<p>我今天写这篇文章的意思呢，就是推荐给大家另外一种实现方法。</p>
<h2 data-id="heading-1">String.raw 简介</h2>
<p><code>String.raw()</code> 是一个模板字符串的标签函数，用来获取一个模板字符串的原始字符串的，比如说，占位符（例如 $&#123;foo&#125;）会被处理为它所代表的其他字符串，而转义字符（例如 \n）不会。</p>
<h3 data-id="heading-2">语法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">String</span>.raw(callSite, ...substitutions)
<span class="hljs-built_in">String</span>.raw<span class="hljs-string">`templateString`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">参数</h3>
<ul>
<li><strong>callSite</strong>    一个模板字符串的“调用点对象”。类似&#123; raw: ['foo', 'bar', 'baz'] &#125;。</li>
<li><strong>...substitutions</strong>    任意个可选的参数，表示任意个内插表达式对应的值。</li>
<li><strong>templateString</strong>    模板字符串，可包含占位符（$&#123;...&#125;）。</li>
</ul>
<h3 data-id="heading-4">返回值</h3>
<p>给定模板字符串的原始字符串。</p>
<h3 data-id="heading-5">使用示例</h3>
<p>以下是一些关于 <code>String.raw</code> 的使用示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">String</span>.raw<span class="hljs-string">`Hi\n<span class="hljs-subst">$&#123;<span class="hljs-number">2</span>+<span class="hljs-number">3</span>&#125;</span>!`</span>;
<span class="hljs-comment">// 'Hi\\n5!'，Hi 后面的字符不是换行符，\ 和 n 是两个不同的字符</span>

<span class="hljs-built_in">String</span>.raw <span class="hljs-string">`Hi\u000A!`</span>;
<span class="hljs-comment">// "Hi\\u000A!"，同上，这里得到的会是 \、u、0、0、0、A 6个字符，</span>
<span class="hljs-comment">// 任何类型的转义形式都会失效，保留原样输出，不信你试试.length</span>

<span class="hljs-keyword">let</span> name = <span class="hljs-string">"Bob"</span>;
<span class="hljs-built_in">String</span>.raw <span class="hljs-string">`Hi\n<span class="hljs-subst">$&#123;name&#125;</span>!`</span>;
<span class="hljs-comment">// "Hi\\nBob!"，内插表达式还可以正常运行</span>


<span class="hljs-comment">// 正常情况下，你也许不需要将 String.raw() 当作函数调用。</span>
<span class="hljs-comment">// 但是为了模拟 `t$&#123;0&#125;e$&#123;1&#125;s$&#123;2&#125;t` 你可以这样做:</span>
<span class="hljs-built_in">String</span>.raw(&#123; <span class="hljs-attr">raw</span>: <span class="hljs-string">'test'</span> &#125;, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>); <span class="hljs-comment">// 't0e1s2t'</span>
<span class="hljs-comment">// 注意这个测试, 传入一个 string, 和一个类似数组的对象</span>
<span class="hljs-comment">// 下面这个函数和 `foo$&#123;2 + 3&#125;bar$&#123;'Java' + 'Script'&#125;baz` 是相等的.</span>
<span class="hljs-built_in">String</span>.raw(&#123;
  <span class="hljs-attr">raw</span>: [<span class="hljs-string">'foo'</span>, <span class="hljs-string">'bar'</span>, <span class="hljs-string">'baz'</span>]
&#125;, <span class="hljs-number">2</span> + <span class="hljs-number">3</span>, <span class="hljs-string">'Java'</span> + <span class="hljs-string">'Script'</span>); <span class="hljs-comment">// 'foo5barJavaScriptbaz'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">实现需求</h3>
<p>我们使用 <code>String.raw</code> 来实现以下文章开头的需求：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> filePath = <span class="hljs-built_in">String</span>.raw<span class="hljs-string">`D:\bianchengsanmei\blogs\categories\JavaScript`</span>;
<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#container"</span>).innerText = filePath;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正确显示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e6167e272804bca90e08552c4173cda~tplv-k3u1fbpfcp-watermark.image" alt="image-20210824211345755" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，使用 String.raw 可以原汁原味的输出期望结果，再也不会因为转义字符的原因导致各种预期之外的结果。</p>
<h2 data-id="heading-7">总结</h2>
<p>我们可以使用 String.raw 来保证模板字符的输出结果是原始值。</p>
<p>~</p>
<p>~本文完，感谢阅读！</p>
<p>~</p>
<blockquote>
<p>学习有趣的知识，结识有趣的朋友，塑造有趣的灵魂！</p>
<p>大家好，我是〖<a href="https://juejin.cn/user/2893570333750744/posts" target="_blank" title="https://juejin.cn/user/2893570333750744/posts">编程三昧</a>〗的作者 <strong>隐逸王</strong>，我的公众号是『<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fyinyiwang%2FblogImages%2Fraw%2Fmaster%2Fimages%2F20210604%2520%2F19-26-03-txvEvM.png" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/yinyiwang/blogImages/raw/master/images/20210604%20/19-26-03-txvEvM.png" ref="nofollow noopener noreferrer">编程三昧</a>』，欢迎关注，希望大家多多指教！</p>
<p>你来，怀揣期望，我有墨香相迎！ 你归，无论得失，唯以余韵相赠！</p>
<p>知识与技能并重，内力和外功兼修，理论和实践两手都要抓、两手都要硬！</p>
</blockquote></div>  
</div>
            