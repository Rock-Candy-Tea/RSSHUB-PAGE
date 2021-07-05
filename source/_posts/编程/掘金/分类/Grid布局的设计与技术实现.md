
---
title: 'Grid布局的设计与技术实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/775e377c97d2472d85f210ac7549d85c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 03:32:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/775e377c97d2472d85f210ac7549d85c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>参考：</p>
<p><a href="https://zh.wikipedia.org/wiki/%E6%A0%85%E6%A0%BC%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">维基百科：栅格设计</a></p>
<p><a href="https://zhuanlan.zhihu.com/p/55494640" target="_blank" rel="nofollow noopener noreferrer">深度好文！如何用栅格系统布局网页界面</a></p>
<p><a href="https://www.uisdc.com/grid-system-and-application-in-background-design" target="_blank" rel="nofollow noopener noreferrer">超全面！栅格系统及其在后台设计中的应用总结</a></p>
<p><a href="https://spec.fm/specifics/8-pt-grid" target="_blank" rel="nofollow noopener noreferrer">8 Point Grid</a></p>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/grid" target="_blank" rel="nofollow noopener noreferrer">MDN-Grid</a></p>
</blockquote>
<p><em>Antd组件库是最好的组件库😎</em></p>
<h1 data-id="heading-0">前言</h1>
<p>最近在NoCode项目碰到了对于栅格（Grid）布局组件的处理，对它深入研究了一下，发现还是蛮有意思的，遂以此文记录Grid这种设计概念以及它在Antd组件库中的React技术实现。</p>
<p>栅格组件其实是前端开发中经常使用到的一种经典布局、排版组件，用它来实现功能可能是没有问题，但是对于它的设计理念以及React技术实现，了解的人却很少。</p>
<p>比如，栅格的基本组成部分是哪些？为什么AntDesign对于Row的gutter属性推荐使用 16+8n px（n是自然数）？为什么常见的栅格系统都是12列或24列？React技术如何实现栅格？诸如此类，都很有意思并且值得去探究。</p>
<p>PS：本文会混用栅格和Grid这两个词，读者知道它们表示同一个东西即可。</p>
<h1 data-id="heading-1">什么是栅格（Grid）</h1>
<h2 data-id="heading-2">定义</h2>
<p>首先，栅格是一个设计概念，并且是一个比较经典的平面设计概念，摘一段维基百科的描述：</p>
<blockquote>
<p>栅格设计系统（又称网格设计系统、标准尺寸系统、程序版面设计、瑞士平面设计风格、国际主义平面设计风格），是一种平面设计的方法与风格。运用固定的格子设计版面布局，其风格工整简洁，在二战后大受欢迎，已成为今日出版物设计的主流风格之一。</p>
<p>1629年，法王路易十四命令成立一个管理印刷的皇家特别委员会，由数学家尼古拉斯·加宗（Nicolas Jaugeon）担任领导。委员会提出了新字体设计建议：以罗马体为基础，采用方格为设计依据，每个字体方格分为64个基本方格单位，每个方格单位再分成36小格，这样，一个印刷版面就由2304个小格组成。这是世上最早对字体和版面进行科学实验的活动。也是栅格系统的雏形。</p>
<p>20世纪50年代，栅格设计系统终于在前西德与瑞士得到完善。通过瑞士平面设计杂志的宣传，将瑞士苏黎士和巴塞尔两个城市的设计家从20世纪40年代探索的成果全面展示，并影响世界各国，因此也被称为“瑞士平面设计风格”（Swiss Design）。由于这种风格简单明确，传达功能准确，因而很快得到世界范围内的普遍认可，成为战后影响最大的一种平面设计风格，也是国际最流行的风格，因此又被称为“国际主义平面设计风格”（International Typographic Style）。</p>
</blockquote>
<p>通俗的理解，栅格布局就是以网格的方式来实现二维排版布局的方式，如下图所示，就是经典的栅格设计风格：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/775e377c97d2472d85f210ac7549d85c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">组成部分</h2>
<h3 data-id="heading-4">网格原子单位</h3>
<p>从微观角度来看，栅格系统会把可视区域划分为一系列规格一致的小网格，这些网格会辅助设计师更规范的排版和布局，这些小网格也是整个栅格系统的最小单位，需要注意的是，对于研发来说一般不会注意到这个网格原子单位的存在。</p>
<p>以AntDesign为代表的大部分设计语言会把网格原子单位定为8，为什么会定为8而不是其他的数字呢？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf8d5d09b3934f42a60a844daa7c4e64~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果以4、6、8、10、12作为栅格的原子单位，可以看到目前主流屏幕分辨率和它们的整除关系如下图，可以看出来4是整除率最高的单位，但是4作为原子单位实在是太小，增减看起来差别并不明显，所以在整除率和合适之间寻求一个平衡，选择8作为栅格的原子单位，这也就解释了为什么AntDesign的Grid组件要使用（16+8n）px来作为栅格间隔水槽。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7888184ab7a64de48303585c02b5a9f0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">列（Column）和水槽（Gutter）</h3>
<p>上面讲到了栅格的网格原子单位，但是在使用中我们会把整个可视区域划分为若干列，我们会直接声明某个内容区域在横向占了多少列来标识整个内容区域的宽度。</p>
<p>通常我们使用的组件库中的Grid组件会直接把可视区域划分为12列或者24列，那为什么是12和24呢？我还特意查了一下这个问题，得到的解答（知乎）是：</p>
<p>“</p>
<p>因为12是1，2，3，4，6的最小公倍数，所以12列栅格系统相对较灵活，支持将一行分成1列，2列，3列，4列，6列。若是想要支持5列，那1，2，3，4，5的最小公倍数是60，而60这个数对于栅格系统来说显然太大了。18能均分4列不？24能做的12都能做，所以12是最好的选择。</p>
<p>”</p>
<p>水槽是相邻两个列宽之间的间隔，用来规范页面中内容间的间距，水槽的值越大，页面中留白部分的面积越多，视觉效果越松散，反之，页面越紧凑。水槽通常设置为定值。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6081de125b649108f49719d9303f980~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">React组件实现</h1>
<p>文章中只是部分代码，完整代码地址：<a href="https://github.com/erdong-fe/toy-antd" target="_blank" rel="nofollow noopener noreferrer">github.com/erdong-fe/t…</a></p>
<p>为了探究React组件对于Grid的实现，我研读了Antd对于Grid的源码。</p>
<p>React组件对于Grid的实现，关键在于使用一维的Flex布局来模拟二维的效果，它分拆出了两个组件，分别是Row和Col，来实现行和列的摆放布局，所以对于React Grid的研究，重点在于研究Row和Col这两个组件。</p>
<h2 data-id="heading-7">Row</h2>
<p>Row组件最大的作用在于创建一个Flex布局的Dom容器，并且接收行相关的参数，为了简单起见，我只实现Row接收gutter参数，Row的参数定义如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">interface RowProps <span class="hljs-keyword">extends</span> React.HTMLAttributes<HTMLDivElement> &#123;
    gutter?: number
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一个问题需要注意，比如对于下面这个Grid布局来说，列与列之间有gutter，这个比较好实现，设置列左右的margin就行了，但是对于最左侧和最右侧的列来说，它们的margin-left和margin-right是多余的，所以我们需要在Row的代码里面做调整</p>
<p>调整代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Row</span>(<span class="hljs-params">props: RowProps</span>) </span>&#123;
<span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">const</span> rowStyle: React.CSSProperties = &#123;&#125;;

  <span class="hljs-keyword">if</span> (gutter && gutter > <span class="hljs-number">0</span>) &#123;
      rowStyle.marginLeft = gutter / -<span class="hljs-number">2</span>;
      rowStyle.marginRight = gutter / -<span class="hljs-number">2</span>;
  &#125;
<span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>剩下的就是实现Row代码结构里包含Col、把Row接受的参数透传给Col组件以及相关的样式代码即可，完整代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-comment">/** RowContext文件 **/</span>

<span class="hljs-keyword">import</span> &#123; createContext, Context &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">export</span> interface RowContextState &#123;
    gutter?: number
&#125;

<span class="hljs-keyword">const</span> RowContext: Context<RowContextState> = createContext(&#123;&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> RowContext;
  
<span class="hljs-comment">/** row文件 **/</span>
  
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> RowContext <span class="hljs-keyword">from</span> <span class="hljs-string">'./RowContext'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./style.scss'</span>;

interface RowProps <span class="hljs-keyword">extends</span> React.HTMLAttributes<HTMLDivElement> &#123;
    gutter?: number
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Row</span>(<span class="hljs-params">props: RowProps</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123;
        gutter = <span class="hljs-number">0</span>,
        children
    &#125; = props;

    <span class="hljs-keyword">const</span> rowStyle: React.CSSProperties = &#123;&#125;;

    <span class="hljs-keyword">if</span> (gutter && gutter > <span class="hljs-number">0</span>) &#123;
        rowStyle.marginLeft = gutter / -<span class="hljs-number">2</span>;
        rowStyle.marginRight = gutter / -<span class="hljs-number">2</span>;
    &#125;

    <span class="hljs-keyword">const</span> rowContext = React.useMemo(<span class="hljs-function">() =></span> (&#123; gutter &#125;), [gutter])

    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RowContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;rowContext&#125;</span>></span> 
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"row"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;...rowStyle&#125;&#125;</span>></span>
                &#123; children &#125;
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">RowContext.Provider</span>></span></span>
    )
&#125;

<span class="hljs-comment">/** style.scss **/</span>

.row &#123;
    <span class="hljs-attr">display</span>: flex;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">Col</h2>
<p>列组件实现要点是：</p>
<p>读取自身的span参数，并且根据24等分实现自身宽度</p>
<p>从Row组件中读取gutter参数，并且把它变成相应的“水槽”宽度</p>
<p>首先实现读取span参数和实现自身宽度：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-comment">/** style.scss **/</span>

@<span class="hljs-keyword">for</span> $index <span class="hljs-keyword">from</span> <span class="hljs-number">1</span> to <span class="hljs-number">24</span> &#123;
    .col-#&#123;$index&#125; &#123;
        <span class="hljs-attr">flex</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> percentage($number: $index / $grid-columns);
    &#125;
&#125;
.col &#123;
    box-sizing: border-box;
&#125;

<span class="hljs-comment">/** Col文件 **/</span>

interface ColProps <span class="hljs-keyword">extends</span> React.HTMLAttributes<HTMLDivElement> &#123;
    <span class="hljs-attr">span</span>: number
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Col</span>(<span class="hljs-params">props: ColProps</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123;
        children,
        span
    &#125; = props;

    <span class="hljs-keyword">const</span> classObj = &#123;
        [<span class="hljs-string">`col-<span class="hljs-subst">$&#123;span&#125;</span>`</span>]: span !== <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>
    &#125;
    <span class="hljs-keyword">const</span> classes = classNames(<span class="hljs-string">'col'</span>, classObj);

    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;classes&#125;</span>></span>
            &#123; children &#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后实现从Row组件中读取gutter参数，并且把它变成相应的“水槽”宽度，完整代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; useContext, CSSProperties &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> classNames <span class="hljs-keyword">from</span> <span class="hljs-string">'classnames'</span>;
<span class="hljs-keyword">import</span> RowContext <span class="hljs-keyword">from</span> <span class="hljs-string">'./RowContext'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./style.scss'</span>;

interface ColProps <span class="hljs-keyword">extends</span> React.HTMLAttributes<HTMLDivElement> &#123;
    <span class="hljs-attr">span</span>: number
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Col</span>(<span class="hljs-params">props: ColProps</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123;
        children,
        span
    &#125; = props;

    <span class="hljs-keyword">const</span> classObj = &#123;
        [<span class="hljs-string">`col-<span class="hljs-subst">$&#123;span&#125;</span>`</span>]: span !== <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>
    &#125;
    <span class="hljs-keyword">const</span> classes = classNames(<span class="hljs-string">'col'</span>, classObj);

    <span class="hljs-keyword">const</span> &#123; gutter &#125; = useContext(RowContext);
    <span class="hljs-keyword">const</span> styleObj: CSSProperties = &#123;&#125;;
    <span class="hljs-keyword">if</span> (gutter && gutter > <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">const</span> horizontalGutter = gutter / <span class="hljs-number">2</span>;
        styleObj.paddingLeft = horizontalGutter;
        styleObj.paddingRight = horizontalGutter;
    &#125;

    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;classes&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;...styleObj&#125;&#125;</span>></span>
            &#123; children &#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>综上所述，一个基本的Grid React组件就实现完了</p>
<h1 data-id="heading-9">总结</h1>
<p>前端组件里面除了代码实现以外，也有很多设计思想的体现，理解设计思想或许比单纯会实现代码更有意义</p></div>  
</div>
            