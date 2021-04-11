
---
title: '前端微周刊（第8期）：使用CSS hsl函数和CSS 变量，自动生成暗黑模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/242e48fbc0fb40589aad3ffbed7c39ec~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 08:54:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/242e48fbc0fb40589aad3ffbed7c39ec~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>“前端微周刊”，为前端开发者提供技术相关资讯及文章。</p>
<p>微信关注**“前端微志”**公众号，及时获取最新周刊。</p>
</blockquote>
<h2 data-id="heading-0">📰 资讯</h2>
<h3 data-id="heading-1"><a href="https://github.com/tailwindlabs/tailwindcss/releases/tag/v2.1.0" target="_blank" rel="nofollow noopener noreferrer">Tailwind CSS v2.1发布</a></h3>
<p><code>Tailwind</code> CSS 发布了v2.0之后的第一个含多个特性更新的版本。其中，三月份发布的<code>Just-In-Time</code>引擎已经合并到主包中，可以在<code>tailwind.config.js</code>中通过配置<code>mode: 'jit</code>启用该特性，另外还有<code>CSS filters</code>、<code>mix-blend-mode</code>、<code>isolation</code>、<code>box-decoration-break</code>等功能的支持。</p>
<p>这里简单提一下这次比较受关注的新特性<code>Just-In-Time</code>，它到底能带来哪些好处？</p>
<p>受益于这种实时地class分析能力，不管是在<code>development</code>还是<code>production</code>模式下，都可以实现样式的按需打包，保证了开发环境和线上环境的一致。之前，<code>Tailwind</code>只能在生产环境进行这种按需的样式打包，开发环境因计算量较大，体验不太好。</p>
<p>这个能力，还可以支持用户通过类似串行的方式定义样式，如<code>sm:focus:hover:active:font-bold</code>可以实现在鼠标悬停和选中状态下的字体加粗。还支持自定义样式，如<code>bg-[#a0cdae]</code>可以自定义背景颜色。</p>
<p>目前来看，<code>Tailwind</code>已经越来越成熟了，可以考虑在你的项目中实践一下了。</p>
<h3 data-id="heading-2"><a href="https://developer.chrome.com/blog/migrating-to-typescript/" target="_blank" rel="nofollow noopener noreferrer">Chrome DevTools架构调整：整合到TypeScript</a></h3>
<p><img alt="DevTools 迁移 TypeScript" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/242e48fbc0fb40589aad3ffbed7c39ec~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>DevTools</code>在2013年决定使用一个类型检查器，当时选择的是<code>Closure Compiler</code>，之后就经常被问到一个问题：你们有没有考虑迁移到一个新的类型检查器？</p>
<p>在<a href="https://developer.chrome.com/blog/migrating-to-js-modules/" target="_blank" rel="nofollow noopener noreferrer">迁移到JavaScript modules</a>之后，<code>Closure Compiler</code>已经不能发现一些JavaScript中的异常。</p>
<p>由于<code>TypeScript</code>团队自身也使用<code>DevTools</code>来做用例的测试，所以两者自身的兼容适配上有一定的优势。在对比了一些性能指标之后，决定使用<code>TypeScript</code>。</p>
<h2 data-id="heading-3">📖 文章</h2>
<h3 data-id="heading-4"><a href="https://zhuanlan.zhihu.com/p/359122473" target="_blank" rel="nofollow noopener noreferrer">Notion 编辑器原理分析</a></h3>
<p><img alt="Notion 表现层与数据层的数据流" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24e897b74fc842c29e03fb344bbdd677~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>所以整个 notion 可以分两层，数据层专门负责存储数据；渲染层负责把数据渲染成界面，接收用户的事件并转化成 op 操作交给数据层执行。</p>
</blockquote>
<h3 data-id="heading-5"><a href="https://dev.to/afif/100-underline-overlay-animation-the-ultimate-css-collection-4p40" target="_blank" rel="nofollow noopener noreferrer">100 underline/overlay animations</a></h3>
<p><img alt="underline动画效果" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b946a10118f4a36b7b0c4b7f838c5b6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>文中提供了百种通过<code>underline</code>和<code>overlay</code>的动画方式，实现多变的鼠标悬停动效，
建议读后收藏。</p>
<p>这些动画，都是使用<code>CSS</code>中的基本属性，如<code>background</code>，<code>transition</code>等，没有<code>SVG</code>和<code>JavaScript</code>，且只有一个HTML标签，只需要定义一个样式<code>class</code>使用即可。</p>
<h3 data-id="heading-6"><a href="https://product.hubspot.com/blog/how-to-learn-complex-things-quickly" target="_blank" rel="nofollow noopener noreferrer">How to Learn Complex Things Quickly: A Guide</a></h3>
<p>这是一篇方法论的表述：如何学习复杂事物？</p>
<p>通常面对复杂事物时，第一反应都会想到很多阻碍和困难，然后就立即劝退了。文中通过循序渐进的方式，讲述如何拆解目标并一步一步地实现目标。大概分为以下几步：</p>
<ul>
<li>确定目标</li>
<li>阅读完整目录，先不要搞那么细</li>
<li>试着研究深入一点点</li>
<li>不要害怕寻求帮助</li>
<li>总结经验，复盘问题</li>
</ul>
<p>道理我们都懂，等于没说？戳原文细度以下，你会有些收获的。</p>
<h3 data-id="heading-7"><a href="https://lea.verou.me/2021/03/inverted-lightness-variables/" target="_blank" rel="nofollow noopener noreferrer">Dark mode in 5 minutes, with inverted lightness variables</a></h3>
<p><img alt="自动生成的暗黑模式效果对比" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/800951df738b4a7dbba9415d8c5c2075~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>要实现网站的暗黑模式，没有一个标准答案，每种方式都有各自的优缺点，除了要考虑老项目的改造成本，还要考虑后期的持续维护成本。所以，我们需要一个规则简单，易维护的方案。</p>
<p>本文介绍了一种通过使用<code>CSS</code>中的<code>hsl</code>函数和<code>CSS 变量</code>相结合，实现自动生成暗黑模式的功能的技术方案。</p>
<p>示例代码：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-pseudo">:root</span> &#123;
--primary-hs: <span class="hljs-number">250</span> <span class="hljs-number">30%</span>;
&#125;

<span class="hljs-selector-tag">h1</span> &#123;
<span class="hljs-attribute">color</span>: <span class="hljs-built_in">hsl</span>(<span class="hljs-built_in">var</span>(--primary-hs) <span class="hljs-number">30%</span>);
&#125;

<span class="hljs-selector-tag">article</span> &#123;
<span class="hljs-attribute">background</span>: <span class="hljs-built_in">hsl</span>(<span class="hljs-built_in">var</span>(--primary-hs) <span class="hljs-number">90%</span>);
&#125;

<span class="hljs-selector-tag">article</span> <span class="hljs-selector-tag">h2</span> &#123;
<span class="hljs-attribute">background</span>: <span class="hljs-built_in">hsl</span>(<span class="hljs-built_in">var</span>(--primary-hs) <span class="hljs-number">40%</span>);
<span class="hljs-attribute">color</span>: white;
&#125;

<span class="hljs-keyword">@media</span> (<span class="hljs-attribute">prefers-color-scheme</span>: dark) &#123;
  <span class="hljs-selector-pseudo">:root</span> &#123;
    --primary-hs: <span class="hljs-number">320</span> <span class="hljs-number">30%</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你对<code>hsl</code>函数不熟悉，这里提一下它的关键知识点。它接收三个参数，分别是<code>色相</code>、<code>饱和度</code>和<code>亮度</code>。<code>饱和度</code>和<code>亮度</code>好理解，那<code>色相</code>指什么？</p>
<p><code>色相</code>是一个从0到360范围内的数值，表示颜色从红色到绿色再到蓝色间的渐变色，其中0和360表示红色，120表示绿色，240表示蓝色。</p>
<h3 data-id="heading-8"><a href="https://areknawo.com/discovering-observer-web-apis/" target="_blank" rel="nofollow noopener noreferrer">Discovering Observer Web APIs</a></h3>
<p>浏览器环境下，有一些<code>API</code>可以用来监听页面变化，如：</p>
<ul>
<li><code>MutationObserver</code>（监视DOM树中节点的增删改查变化）</li>
<li><code>ResizeObserver</code>（监听标签HTML元素和SVG标签的边界改变）</li>
<li><code>IntersectionObserver</code>（异步监视目标标签元素与根节点间的交叉状态变化）</li>
</ul>
<p>文中深入地研究如何使用它们，实现某些需要监视页面变化场景下的功能。</p>
<h2 data-id="heading-9">🛠 工具、插件</h2>
<h3 data-id="heading-10"><a href="https://figma-to-react.vercel.app/" target="_blank" rel="nofollow noopener noreferrer">Figma to React</a></h3>
<p><img alt="示例：左侧为设计稿，右侧为生成的React代码" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e481045641e4365897b63130fdf7c2e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>Figma to React</code>可以将一个<code>Figma</code>绘制的一页内容，转换为<code>React</code>语法的代码，支持<code>React Native</code>和<code>Next.js</code>框架的代码导出。</p>
<h3 data-id="heading-11"><a href="https://github.com/denoland/deno_std" target="_blank" rel="nofollow noopener noreferrer">Deno standard library</a></h3>
<p><code>Deno</code>核心团队支持的一个所有<code>Deno</code>项目都可以放心使用的高质量代码集合的标准，这些模块没有额外的依赖，如果你想要创建<code>Deno</code>生态下的项目，可以参考这些模块的代码。</p>
<h3 data-id="heading-12"><a href="https://chrome.google.com/webstore/detail/web-developer-checklist/iahamcpedabephpcgkeikbclmaljebjp/related?hl=en" target="_blank" rel="nofollow noopener noreferrer">Web Developer Checklist（Chrome插件）</a></h3>
<p><img alt="使用该插件分析 https://tinyshare.cn" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c275f55bff240408c4df8dc90707818~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这是一个开发者工具，针对网站的<code>SEO</code>、<code>可用性</code>、<code>移动端适配</code>、<code>Accessibility</code>和<code>Performance</code>等指标的检查项进行分析，给出可供开发者参考的数据。</p>
<h3 data-id="heading-13"><a href="https://yaireo.github.io/tagify/" target="_blank" rel="nofollow noopener noreferrer">Tagify</a></h3>
<p><code>Tagify</code>是一个强大的<code>input</code>插件，可以将<code>input</code>中的内容展示成可交互的<code>tag</code>，支持各种自定义配置。</p>
<h2 data-id="heading-14">🥅 代码片段</h2>
<h3 data-id="heading-15">使用JS复制内容添加到剪切板</h3>
<p>在浏览器中复制内容，很简单，用户只需要选中内容，然后<code>ctrl+c</code>即可完成复制。但是这需要用户主动选中内容，如果你的需求是只能一次点击来完成复制操作，那就需要使用浏览器中的一些API来实现了。</p>
<p>下面介绍两种方法：</p>
<p>**方法一：**使用`execCommand('copy')</p>
<p>根据<code>MDN</code>的文档，<code>document.execCommand</code>这个API已经不被建议使用了，但它还是可以在<code>textarea</code>标签中正常运行。如果你的页面没有<code>textarea</code>标签，可以创建一个隐藏的<code>textarea</code>，将内容填充到这个标签内，再执行复制的操作。复制操作的示例代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copyTextFromTextArea</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> area = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#text-area'</span>)
  area.select();
  <span class="hljs-built_in">document</span>.execCommand(<span class="hljs-string">'copy'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>方法二：</strong><code>Clipboard API</code></p>
<p><code>Clipboard API</code>是一个更现代化，且基于<code>Promise</code>实现。实现一个简单的复制操作，示例代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copyTextFromParagraph</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> cb = navigator.clipboard;
  <span class="hljs-keyword">const</span> paragraph = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'p'</span>);
  cb.writeText(paragraph.innerText).then(<span class="hljs-function">() =></span> alert(<span class="hljs-string">'Text copied'</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">使用<code>IntersectionObserver</code>监听页面元素变化</h3>
<p><code>IntersectionObserver</code>对象用于异步监听页面元素及其根元素交叉状态的方法。我们可以利用这一特性API，实现一个“页面滚动时触发CSS动画”的功能：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> observer = <span class="hljs-keyword">new</span> IntersectionObserver(<span class="hljs-function"><span class="hljs-params">entries</span> =></span> &#123;
  <span class="hljs-comment">// 循环所有入口</span>
  entries.forEach(<span class="hljs-function"><span class="hljs-params">entry</span> =></span> &#123;
    <span class="hljs-comment">// 如果元素是可见的</span>
    <span class="hljs-keyword">if</span> (entry.isIntersecting) &#123;
      <span class="hljs-comment">// 添加动画class</span>
      entry.target.classList.add(<span class="hljs-string">'square-animation'</span>)
    &#125;
  &#125;)
&#125;);
observer.observe(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.square));
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">在JavaScript中使用<code>媒体查询</code>（Media Query）</h3>
<p>通常，我们都是在<code>CSS</code>中使用媒体查询做网页的自适应开发，如对<code>min-width</code>、<code>max-width</code>、<code>dpr</code>等设备条件进行自定义的样式配置。</p>
<p>其实，我们也可以通过<code>JavaScript</code>实现媒体查询的功能。这里要提到<code>window.matchMedia</code>这个方法，它接收一个<code>媒体查询条件</code>作为参数，并返回一个<a href="https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList" target="_blank" rel="nofollow noopener noreferrer"><code>MediaQueryList</code></a>对象，<code>MediaQueryList.matches</code>即表示当前文档页面是否符合要查询的<code>媒体查询条件</code>。</p>
<p>下面给出一个简单的示例（来自MDN）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> para = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'p'</span>);
<span class="hljs-keyword">var</span> mql = <span class="hljs-built_in">window</span>.matchMedia(<span class="hljs-string">'(max-width: 600px)'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">screenTest</span>(<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (e.matches) &#123;
    <span class="hljs-comment">/* 该 viewport 宽度小于等于600px */</span>
    para.textContent = <span class="hljs-string">'This is a narrow screen — less than 600px wide.'</span>;
    <span class="hljs-built_in">document</span>.body.style.backgroundColor = <span class="hljs-string">'red'</span>;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">/* 该 viewport 宽度大于600px */</span>
    para.textContent = <span class="hljs-string">'This is a wide screen — more than 600px wide.'</span>;
    <span class="hljs-built_in">document</span>.body.style.backgroundColor = <span class="hljs-string">'blue'</span>;
  &#125;
&#125;

<span class="hljs-comment">// 监听 mql 的变化</span>
mql.addEventListener(<span class="hljs-string">'change'</span>, screenTest);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>文章首发于微信公众号：前端微志。</p>
<p>想要第一时间收到文章推送，更有前端前瞻性技术分享，请微信搜索关注“前端微志”，</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            