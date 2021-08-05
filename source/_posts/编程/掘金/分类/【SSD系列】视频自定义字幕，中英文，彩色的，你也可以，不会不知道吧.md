
---
title: '【SSD系列】视频自定义字幕，中英文，彩色的，你也可以，不会不知道吧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e79d1df95158430bba225be82c3f2876~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 16:31:48 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e79d1df95158430bba225be82c3f2876~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p>关于【SSD系列】：<br>
<strong>前端一些有意思的内容，旨在3-10分钟里，有所获，又不为所累。</strong></p>
<p>字幕，大家见过吧，其实你也可以，真的可以，真的真的可以。不难，不难，真的不难。 我们一起来做点有意思的弹幕吧。</p>
<p>源码： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxiangwenhu%2FJuejinBlogs%2Ftree%2Fmaster%2F%25E8%2587%25AA%25E5%25AE%259A%25E4%25B9%2589%25E5%25AD%2597%25E5%25B9%2595" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xiangwenhu/JuejinBlogs/tree/master/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%AD%97%E5%B9%95" ref="nofollow noopener noreferrer">自定义字幕</a></p>
<h2 data-id="heading-1">字幕效果演示</h2>
<h3 data-id="heading-2">字幕和特殊字符演示</h3>
<p>下面的字幕效果，没用使用任何JS代码。</p>
<p>因gif的视频文件太大，拆分为两份。<br>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e79d1df95158430bba225be82c3f2876~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="zimy1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21d2ae0016f44476811c3fa7208c3d09~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="zimy2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">字幕切换演示</h3>
<p>还支持多种字幕，如下演示切换字幕：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17eb1b52424b4413874b02c8e85381d0~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="zimy3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">原理 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWebVTT_AP" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/WebVTT_AP" ref="nofollow noopener noreferrer">WebVTT</a></h2>
<p>MDN的解释</p>
<blockquote>
<p><strong>Web视频文本跟踪格式</strong> (<strong>WebVTT</strong>) 是一种使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTML%2FElement%2Ftrack" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/track" ref="nofollow noopener noreferrer"><code><track></code></a>元素显示定时文本轨道（如字幕或标题）的格式。 WebVTT文件的主要用途是将文本叠加添加到<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTML%2FElement%2Fvideo" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/video" ref="nofollow noopener noreferrer"><code><video></code></a>。</p>
</blockquote>
<p>基本使用:</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">video</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"videoEL"</span> <span class="hljs-attr">controls</span> <span class="hljs-attr">autoplay</span> <span class="hljs-attr">crossorigin</span>=<span class="hljs-string">"anonymous"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./gg.mp4"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"500"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">track</span> <span class="hljs-attr">default</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./zh.vtt"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"中文字幕"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">track</span> <span class="hljs-attr">default</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./en.vtt"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"英文字幕"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">video</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出来，<code>track</code>是video的子标签，其<code>src</code>属性引用了一个<code>vtt</code>类型的文件，额外注意一下<code>label</code>属性，这个属性值是切换字幕时的标题。</p>
<p>所以下一章节的<code>vtt</code>文件是重点。</p>
<h2 data-id="heading-5">vtt文件</h2>
<p>先看一段范本：</p>
<pre><code class="hljs language-vtt copyable" lang="vtt">WEBVTT

00:00.400 --> 00:00.900 line:38% position:35%
干什么呢

00:01.600 --> 00:01.600 line:40% position:35%
就你个小不点

<span class="copy-code-btn">复制代码</span></code></pre>
<p>vtt文件书写有很多规范，我们就抓住<strong>三个核心要素</strong> <strong>TSP</strong>:</p>
<ol>
<li>时间  <strong>T</strong></li>
<li>样式  <strong>S</strong></li>
<li>位置 <strong>P</strong></li>
</ol>
<p>连起来： 字幕 <strong>什么时间，在什么位置，什么身姿</strong> 出现。</p>
<h3 data-id="heading-6">时间</h3>
<p><strong>就是字幕应该什么时候出现</strong>, 我觉得你看一下就懂， [开始] --> [结束]</p>
<pre><code class="hljs language-vtt copyable" lang="vtt">00:00.400 --> 00:00.900   // 400ms-900ms的时候出现
<span class="copy-code-btn">复制代码</span></code></pre>
<p>时间如下两种格式，至于各个字母的含义，我想作为前端都能理解。</p>
<ul>
<li><code>mm:ss.ttt</code></li>
<li><code>hh:mm:ss.ttt</code></li>
</ul>
<h3 data-id="heading-7">样式</h3>
<p><strong>就是字幕以什么的身姿出色</strong></p>
<h4 data-id="heading-8">样式定义的方式</h4>
<p>我们演示效果是有明显的颜色，所以肯定是有地方定义了样式。我们有两种方式定义样式</p>
<ol>
<li>外挂样式，写在css文件或者style节点里面</li>
</ol>
<p>下面的代码就是定义默认字幕的样式</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">video</span><span class="hljs-selector-pseudo">::cue</span> &#123;
    <span class="hljs-attribute">background-color</span>: transparent;
    <span class="hljs-attribute">color</span>: yellow;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">text-shadow</span>: peachpuff <span class="hljs-number">0</span> <span class="hljs-number">1px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>内联样式，就是<strong>写在vtt文件</strong>里面的样式</li>
</ol>
<p>下面就是写在vtt文件里面默认字幕样式，注意其<code>STYLE</code>开头</p>
<pre><code class="hljs language-css copyable" lang="css">STYLE
<span class="hljs-selector-pseudo">::cue</span> &#123;
    <span class="hljs-attribute">background-color</span>: transparent;
    <span class="hljs-attribute">color</span>: yellow;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">text-shadow</span>: peachpuff <span class="hljs-number">0</span> <span class="hljs-number">1px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">多种字幕样式</h4>
<p>上面的样式都只提到了默认样式，演示效果上有两种颜色的字幕，这是怎么做到的，答案很简单，还可以给字幕自定义样式</p>
<p>格式如下：</p>
<pre><code class="hljs language-vtt copyable" lang="vtt"><c.classname>text</c>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看一段完整代码，让字幕是白色，并有阴影效果。</p>
<p>vtt文件:</p>
<pre><code class="hljs language-vtt copyable" lang="vtt">00:00.200 --> 00:00.800 line:58% position:80%
<c.mn>大块头</c.mn>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>样式文件：  <code>c.mn</code> 是关键哦。</p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-tag">video</span><span class="hljs-selector-pseudo">::cue</span>(c<span class="hljs-selector-class">.mn</span>) &#123;  
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#FFF</span>;
    <span class="hljs-attribute">text-shadow</span>: peachpuff <span class="hljs-number">0</span> <span class="hljs-number">1px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">可定义样式的属性</h4>
<p>虽说可以自定义样式，主要是字体，背景色，outline, 文本相关的一些属性罢了。 更多参见 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2F%3A%3Acue" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/CSS/::cue" ref="nofollow noopener noreferrer">::cue</a></strong><br>
css3的动画，你就别想了。</p>
<h3 data-id="heading-11">位置</h3>
<p><strong>就是字幕在哪出现</strong></p>
<p>字幕可以水平展示，也可以垂直展示。</p>
<h4 data-id="heading-12"><strong>line</strong></h4>
<p>指定文本垂直显示的位置。如果设置垂直，则行指定文本水平显示的位置。</p>
<h4 data-id="heading-13"><strong>position</strong></h4>
<p>指定文本将水平显示的位置。如果设置为垂直，则位置指定文本将垂直显示的位置。</p>
<p>看一段代码分析：</p>
<p>这条字幕在<strong>距顶部38%，左边35%</strong> 的位置出现。</p>
<pre><code class="hljs language-vtt copyable" lang="vtt">00:00.400 --> 00:00.900 line:38% position:35% 干什么呢
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">其他</h4>
<p><strong>到此为止，你掌握了三要素，能处理大部分情况了。</strong>
还有其他的可选字节顺序标记，注释等等, 重要吗？当然重要，需要的时候才重要。</p>
<h2 data-id="heading-15">完整代码</h2>
<p>是的，就是这么简单。</p>
<p>最后附上完整的演示视频的代码：</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">video</span><span class="hljs-selector-pseudo">::cue</span> &#123;
            <span class="hljs-attribute">background-color</span>: transparent;
            <span class="hljs-attribute">color</span>: yellow;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
            <span class="hljs-attribute">text-shadow</span>: peachpuff <span class="hljs-number">0</span> <span class="hljs-number">1px</span>;
        &#125;

        <span class="hljs-selector-tag">video</span><span class="hljs-selector-pseudo">::cue</span>(c<span class="hljs-selector-class">.mn</span>) &#123;
            <span class="hljs-attribute">color</span>: <span class="hljs-number">#FFF</span>;
            <span class="hljs-attribute">text-shadow</span>: peachpuff <span class="hljs-number">0</span> <span class="hljs-number">1px</span>;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    
     <span class="hljs-tag"><<span class="hljs-name">video</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"videoEL"</span> <span class="hljs-attr">controls</span> <span class="hljs-attr">autoplay</span> <span class="hljs-attr">crossorigin</span>=<span class="hljs-string">"anonymous"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./gg.mp4"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"500"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">track</span> <span class="hljs-attr">default</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./zh.vtt"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"中文字幕"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">track</span> <span class="hljs-attr">default</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./en.vtt"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"英文字幕"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">video</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-vtt copyable" lang="vtt">WEBVTT

00:00.400 --> 00:00.900 line:38% position:35%
干什么呢

00:01.600 --> 00:01.600 line:40% position:35%
就你个小不点

00:01.600 --> 00:03.000 line:30% position:30%
说啥

00:04.000 --> 00:04.800 line:34% position:30%
真嚣张

00:05.000 --> 00:06.000 line:34% position:30%
找教训


00:00.200 --> 00:00.800 line:58% position:80%
<c.mn>大块头</c.mn>

00:01.500 --> 00:02.000 line:58% position:80%
<c.mn>干架</c.mn>

00:02.500 --> 00:03.000 line:58% position:80%
<c.mn>来啊</c.mn>

00:04.000 --> 00:04.800 line:58% position:80%
<c.mn>来啊</c.mn>

00:04.000 --> 00:04.800 line:58% position:80%
<c.mn>来啊</c.mn>

00:05.000 --> 00:06.000 line:58% position:35%
🔨🔨

00:07.201 --> 00:07.400 line:58% position:35%
💔

00:07.401 --> 00:07.800 line:58% position:35%
💔
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">写在最后</h2>
<p>写作不易，你的一言一评，就是最大的努力。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWebVTT_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/WebVTT_API" ref="nofollow noopener noreferrer">WebVTT_API</a><br>
<a href="https://juejin.cn/post/6844903593670246414" target="_blank" title="https://juejin.cn/post/6844903593670246414">HTML5 video视频字幕的使用和制作</a></p>
</blockquote></div>  
</div>
            