
---
title: '奇技淫巧之当你不得不 decode HTML Entity 字符串'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a76f7a2476f54542b5f4810f5f9532d2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 03:41:49 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a76f7a2476f54542b5f4810f5f9532d2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">从一个 bug 说起</h2>
<p>某天产品反馈了一个问题，业务一页面的富文本展示有问题，管理后台输入的是 <code>a<b<c</code>，但最终页面只展示出 <code>a</code>。定位发现富文本渲染存在一个问题逻辑，它针对管理后台输入的 HTML Entity 字符做了还原，在输入一些类似 HTML 标签的字符时，浏览器在展示时将输入识别成 HTML 标签，结果这部分字符便凭空消失。</p>
<p>此处的富文本渲染流程：</p>
<blockquote>
<p>HTML 输入 --> Entity decode --> dangerouslySetInnerHTML --> DOM --> 最终 UI</p>
</blockquote>
<p>当 HTML 输入类似这样的格式： <code><p>a&lt;b&lt;c</p></code>，Decode 以后它变成了 <code><p>a<b<c</p></code>，导致后面的 <code><b<c</code> 被识别成了 HTML 的 Tag，只留下 <code>a</code> 在节点中：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a76f7a2476f54542b5f4810f5f9532d2~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决这个问题，最直接的办法自然是拿掉 <code>Entity decode</code> 这一步骤，但实际操作时陷入一尴尬境地：这段逻辑属于积淀多年的历史代码，被众多地方引用，改动影响范围过大，且带来很大的测试工作量，不敢轻举妄动。</p>
<p>从稳妥的角度出发，既然难以干掉，在有机会赶上大规模测试前，那么是否可以先简单上一个对冲的机制？以此抵消 <code>Entity decode</code> 的作用，产生预期内的UI效果；并把改动控制在问题模块内，不影响到其他引用此渲染逻辑的模块，从而让测试工作量变得可控。</p>
<p>修改后的富文本渲染流程类似：</p>
<blockquote>
<p>HTML 输入 --> <strong>【特殊处理】</strong> --> Entity decode --> dangerouslySetInnerHTML --> DOM --> 最终 UI</p>
</blockquote>
<p>实验表明，确实可以！</p>
<h2 data-id="heading-1">理论学习</h2>
<p>关于这个【特殊处理】逻辑的实现，直接针对会出问题的场景做个替换，是最朴实简单粗暴的想法。但这本身治标不治本，且还带着引发新的问题的担忧。我们能否从本质角度，一次处理完所有可能的 case？</p>
<p>HTML 存在的意义，并非它各种奇奇怪怪的语法，更核心的点在于描述要让浏览器构造一个什么样的 DOM 树，所以我们的关注点放在浏览器解析 HTML 的过程上。根据 WHATWG 的文档，结合一点点的编译原理知识，可以明确这里基本的工作模式：读取输入字符流，然后通过 Tokenizer（词法分析器）分析词法结构，构建起 DOM。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4224313fd2c4d42b532c60193842fde~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Tokenizer 分析的过程，涉及到「有限状态机」的概念。大致来说，Tokenizer 内部维护了一个状态机，定义了 HTML 解析过程涉及到的所有状态，从前往后一个个读取字符，一步步跳转到不同的状态。浏览器引擎也专门在内部维护了一套 DOM 树，当解析状态机进入其中的特定状态，状态机产生新的 Token，触发 Tree Construction 步骤，填充完善 DOM 树结构。当字符流读取结束，DOM 树也最终确定下来。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fhtml.spec.whatwg.org%2Fmultipage%2Fparsing.html%23tag-open-state" target="_blank" rel="nofollow noopener noreferrer" title="https://html.spec.whatwg.org/multipage/parsing.html#tag-open-state" ref="nofollow noopener noreferrer">WHATWG HTML5 文档</a> 为我们提供了完整的解析流程与状态机定义。其中与这里的标签解析场景相关最关键的是 <code>Tag open state</code> 与 <code>End tag open state</code>。解析器从 <code>Data state</code> 状态开始，输入下一个字符是 <code><</code> 时，状态进入 <code>Tag open state </code> 状态。紧接着下一个字符的输入非常关键，决定了是否开始按照标签解析。</p>
<p>由定义文档了解到，<code>Tag open state</code> 的下一个输入可能跳转的状态分为以下 6 种情况：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/974b7981ff9f4eed8dc97c7c76354d89~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中 <code>U+xxxxF</code> 代表的是十六进制 Unicode 字符，我们可以适当放弃一些极度精确的严谨性，从直观的角度我们大体可以这么展开：</p>
<ol>
<li><code>!</code> 感叹号：跳转到 <code>markup declaration open state</code> （针对 <code><!DOCTYPE html></code> / <code><!-- 注释 --></code> / <code><[CDATA[</code> 等情况）</li>
<li><code>/</code> 斜杠：跳转到 <code>end tag open state</code>（针对关闭标签场景，如 <code></div></code>）</li>
<li>ASCII 大小写字母：进入 <code>tag name state</code>，按照标签解析</li>
<li><code>?</code> 问号：解析异常，产生一个空的注释节点，转向 <code>bogus comment state</code> 重新解析（Reconsume，注释继续包含 ? 号）</li>
<li>EOF 结束输入：输出 <code><</code> 号（此时没有更多的输入了）</li>
<li>其他情况：输出 <code><</code> 号（此时产生一个 <code>invalid first character of tag name</code> 异常信号，但不影响工作）</li>
</ol>
<p>从文档看，只要我们保证 <code><</code> 以后不出现情况 1-4，Tokenizer 就不会进入标签解析的状态，不产生新的节点，直接展示原文，也就避免了标签结构不匹配导致显示不完全的情况。</p>
<h2 data-id="heading-2">hack 实战</h2>
<p>从理论上可以跑通，现实落地中我们如何快速验证这个想法、确认合适的字符串替换方案呢？除了写一些 HTML 代码通过不断编辑-刷新验证外，还可借助 DevTools Elements 面板的 Edit as HTML 功能去实时编辑调试。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9963a27bab5b4203a9ef30bae4426be3~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但这都不够直观，只靠观察与猜测还是有些繁琐。我想要做的是针对 WHATWG HTML5 标准解析器的 hack，WHATWG HTML5 Spec 既然是一个标准，或许会有人会基于此做一些不依赖浏览器的 HTML5 解析方案？带着这个问题，简单搜索了下，发现针对 Node.js 做的 HTML5 代码解析器 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Finikulin%2Fparse5" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/inikulin/parse5" ref="nofollow noopener noreferrer">parse5</a>；顺着项目主页的 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fastexplorer.net%2F%23%2F1CHlCXc4n4" target="_blank" rel="nofollow noopener noreferrer" title="http://astexplorer.net/#/1CHlCXc4n4" ref="nofollow noopener noreferrer">Online Playground</a>，还找到一个叫 AST Explorer 的网站。好家伙！这下可以直接观察某 HTML 文本所产生的 DOM 树了，感谢社区。</p>
<p>以这段代码为例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Test<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>我的第一个标题<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我的第一个段落。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 AST Explorer，这段代码产生的 DOM 树的细节可以说是一览无余：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b91f2c2c4ec04f0887da551385607e6a~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>输入有问题的 <code><p>a<b<c</p></code>，观察发现其产生的是一个名为 <code>b<c<</code> ，带一个 <code>p</code> 属性的节点，与标准文档的描述一致。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7aa0bdbd53d84a25ac171c8aa7594490~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>继续脑洞替换策略：原则上不希望影响UI；我们在 <code><</code> 与会产生 tag 的字符之间，加一个不会在渲染树产生节点的空注释节点即可，效果如下。</p>
<p>HTML 输入：<code><p>a<<!---->b<<!---->c</p></code></p>
<p>效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21c96b5c6361485796a0304fa6109d7d~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>显示也符合预期：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/973efea7cacc430fa6cd6429952c8bd4~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>篇幅有限，其他几种情况生成的 Node 暂且不表（<code><!</code> / <code><?</code> / <code></</code>，以及它们的组合），有兴趣的读者可以自行尝试 :P</p>
<p>再补充完善一些关于 Entity 的细节，得到最终解决方案，在实体编码前加上这么一道字符串正则过滤（因为是 hack 代码，需要写上足量的注释，避免未来翻车）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 根据 whatwg 的状态机，解析到 "<" 时会进入 Tag open state
 * 下一个字符若遇到以下 1-4 情况，会导致显示不全
 * 1. "!"，会导致后面字符按注释解析
 * 2. "/"，导致按结束标签解析，若下一个字母是 ascii alpha 产生结束标签，若是 ">" 则空，其他情况会变成注释
 * 3. "?"，导致后面变成注释，不显示
 * 4. ascii alpha 字母，进入 tag name 状态，接下来的字符都会变成标签名，导致无显示
 * 5. 其他情况：正常产生 "<"
 *
 * 替换策略：当匹配到情况 1-4 时，给 "<" 与符号之间补一个空注释节点 <!---->
 *
 * 详情：https://html.spec.whatwg.org/multipage/parsing.html#tag-open-state
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>input 输入的带实体HTML字符串
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">replaceHTMLEntityTagStr</span>(<span class="hljs-params">input = <span class="hljs-string">''</span></span>) </span>&#123;
  <span class="hljs-comment">// entity 有三种：命名、十六进制、十进制</span>
  <span class="hljs-keyword">return</span> input.replace(
    <span class="hljs-regexp">/((&lt;)|(&#x3C;)|(&#60;))(!|\/|\?|[a-zA-Z])/gi</span>,
    <span class="hljs-function">(<span class="hljs-params">all, p1, p2, p3, p4, p5</span>) =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;p1&#125;</span><!----><span class="hljs-subst">$&#123;p5&#125;</span>`</span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>兼容性的考虑：</p>
<ol>
<li>HTML Tag 解析属于浏览器最最基础的功能，理论上不会有兼容问题（在 Safari / Chromium 的爷爷 WebKit 的最初版本，可以找到与此一致的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FWebKit%2FWebKit%2Fblob%2F2f223952eb27bdd4493e4185046cb139cfcb6ca0%2FSource%2FWebCore%2Fhtml%2Fparser%2FHTMLTokenizer.cpp%23L309" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/WebKit/WebKit/blob/2f223952eb27bdd4493e4185046cb139cfcb6ca0/Source/WebCore/html/parser/HTMLTokenizer.cpp#L309" ref="nofollow noopener noreferrer">Tokenizer 代码</a>，与最新的代码相比并无明显改动）</li>
<li>问题页面用于移动端（iOS 统一系统 WebView；Android 有 QQ 浏览器 X5 内核），可以保持一个比较高版本的 WebKit / Chromium 浏览器内核</li>
<li>本替换逻辑在 IE 7 以上测试均可用，iOS 11 的 Safari / Chromium 44 / Firefox 91.01 测试正常（其他版本暂未验证）</li>
</ol>
<h2 data-id="heading-3">hack 心得</h2>
<p>与 bug 的互怼中感触良多，简单总结几点「人生的经验」：</p>
<p>1. 相比于手段而言，更需要关注的是目的本身，罗马只有一个，但通往罗马的道路可以有千万条。在通常的视角，DOM 决定了 UI 的展示，我们的关注点一般会放在 DOM 上，这也成为了一个思维定势。</p>
<p>一棵 DOM 树的来源可以分为这两块：</p>
<ul>
<li>浏览器解析 HTML，在词法分析中构建起 DOM 树</li>
<li>在 JavaScript 层面，通过 createElement、appendChild 等 API 去构造；在 React / Vue 等 GUI 框架等层面，它将这些方法封装起来，通过构造 Object 树，然后统一 Render 出对应的 DOM 节点</li>
</ul>
<p>而这一次的异常 hack 场景因为现实条件限制，关注点已不仅仅是 DOM 层面，所以我们的“罗马”也放在最终的 UI 上。相同的 UI 展示的背后，可能对应不同的 DOM 树，从数学的角度类似一个 <code>n --> 1</code> 的映射。当一条路难以走通时，我们可以不走寻常路，用另外的方式达成相同的目的。当然，不走寻常路，也意味着自己需要独自去面对一些少有人遇到的风险。</p>
<p>2. 虽然是写前端页面（俗称“切图”），但计算机基础知识也总在不经意间用上，尝试抓住一些共性的东西，在适当的时候可以实现降维打击；当然这里也不需要太过于高深，一些基础的编译原理知识足矣，标准文档早已把所有要用到的术语概念、算法等都写在了上面，需要的仅仅是静下来阅读的心境。</p>
<p>3. 事物的发展总在一种渐进式的状态，达到理想并非一蹴而就之事，先稳住局面，才有时间优化。一开始可能难以做得完美，更多的是先完成再完美的状态。由此也想到，对于工程师这一角色的要求，除了代码质量外，更重要的大概是一种，在有限的时间内，面向业务对质量与效率的不同需求，得到最合适的解决方案的能力，类似 “快速达到60分” 与 “精细打磨到90+分” 之间的一个灵活控制。</p></div>  
</div>
            