
---
title: '如何在 vscode 里面放烟花'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07ca3d24ed924e6a847365782316689c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 21:06:21 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07ca3d24ed924e6a847365782316689c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近一直在研究 vscode 插件，今天给大家一分享一个效果特别炫的插件，名字叫 power mode。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07ca3d24ed924e6a847365782316689c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>编写代码边放烟花、编辑器还会抖动。</p>
<p>效果很炫，但是我们肯定不能满足于会用，得研究下它是怎么实现的。</p>
<h2 data-id="heading-0">实现思路</h2>
<p>在 vscode 里大家可能没啥思路，但如果这个效果放到网页里呢，文本改变的时候抖动编辑器、然后再上面出现一些烟花效果。这个可能有的同学就有思路了。</p>
<p><code>抖动编辑器</code>：抖动不也是个动画么，就是左右位移，这一秒右移，下一秒回到原位置，这样就抖起来了。</p>
<p><code>烟花效果</code>：不管啥花里胡哨的烟花，给个 gif 我们就能搞定，就是在文本上方加一个元素，然后把 gif 放上去，下次加 gif 的时候把上次的删除。</p>
<p>这样就能在网页里实现编辑器抖动 + 放烟花效果了。</p>
<p>把这个效果放到 vscode 里实现也是一样的思路，因为 vscode 是基于 electron 实现的啊。</p>
<p>而 electron 又是基于 chromium + nodejs，也就是 ui 部分是网页。我们可以在 vscode 帮助里打开开发者工具：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9966fd5da3640c190552e1ecd415939~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后，可以看到，这编辑器部分就是个 div 啊</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9843ae24ddc64503a7eb8afb17082890~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以刚才在网页里实现的效果，可以放到 vscode 里实现，思路一样。</p>
<p>思路是一样，但是具体怎么做呢？</p>
<p>这就需要了解下 vscode 的 extension api 了，其实也不难，我给大家介绍一下这里用到的 api：</p>
<p>首先，引入 vscode 包，所有的 api 都在这个包里。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> vscode <span class="hljs-keyword">from</span> <span class="hljs-string">'vscode'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们要给文本加样式，怎么加呢？</p>
<p>在 vscode 的编辑器里面加样式不是直接操作 dom 的，是受到限制的，要这样几步：</p>
<ul>
<li>通过 vscode.window 拿到当前的 editor</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> activeEditor = vscode.window.activeTextEditor;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>拿到当前 editor 的正在编辑的位置</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> cursorPosition = activeTextEditor.selection.active;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>根据位置计算出要添加装饰的范围（range）</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> newRange = <span class="hljs-keyword">new</span> vscode.Range(
    cursorPosition.with(cursorPosition.line, cursorPosition.character),
    cursorPosition.with(cursorPosition.line, <span class="hljs-built_in">Math</span>.max(<span class="hljs-number">0</span>, cursorPosition.character + delta))
);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>创建装饰对象</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">vscode.window.createTextEditorDecorationType(&#123;
    <span class="hljs-attr">before</span>: &#123;
        <span class="hljs-attr">contentText</span>:<span class="hljs-string">''</span>,
        <span class="hljs-attr">textDecoration</span>: <span class="hljs-string">`none; <span class="hljs-subst">$&#123;defaultCssString&#125;</span><span class="hljs-subst">$&#123;backgroundCssString&#125;</span> <span class="hljs-subst">$&#123;customCssString&#125;</span>`</span>,
    &#125;,
    <span class="hljs-attr">textDecoration</span>: <span class="hljs-string">`none; position: relative;`</span>,
    <span class="hljs-attr">rangeBehavior</span>: vscode.DecorationRangeBehavior.ClosedClosed
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>然后，给这段 range 的文本加装饰</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">activeEditor.setDecorations(decoration, [newRange]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们就在 vscode 编辑器里面，你正在编辑的位置，加上了一段样式。</p>
<p>装饰对象可以添加 before、after，这不就是伪元素么？没错，就是伪元素，而且还可以加一系列样式呢。加啥样式都可以。</p>
<p>到了这，是不是就有如何在编辑器里做那些效果的思路了呢？</p>
<p>接下来，我们来看看 power-mode 的实现细节。</p>
<h2 data-id="heading-1">代码实现</h2>
<p>我们先从效果实现开始看吧，主要是抖动和放烟花：</p>
<h3 data-id="heading-2">抖动</h3>
<p>抖动的原理我们分析过了，就是定时做位移。</p>
<p>首先，它定义了一系列的位移的装饰对象，就是通过 <code>vscode.window.createTextEditorDecorationType</code> 这个创建装饰对象的 api：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">public activate = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.dispose();
    <span class="hljs-built_in">this</span>.negativeX = vscode.window.createTextEditorDecorationType(<vscode.DecorationRenderOptions>&#123;
        <span class="hljs-attr">textDecoration</span>: <span class="hljs-string">`none; margin-left: 0px;`</span>
    &#125;);

    <span class="hljs-built_in">this</span>.positiveX = vscode.window.createTextEditorDecorationType(<vscode.DecorationRenderOptions>&#123;
        <span class="hljs-attr">textDecoration</span>: <span class="hljs-string">`none; margin-left: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.config.shakeIntensity&#125;</span>px;`</span>
    &#125;);

    <span class="hljs-built_in">this</span>.negativeY = vscode.window.createTextEditorDecorationType(<vscode.DecorationRenderOptions>&#123;
        <span class="hljs-attr">textDecoration</span>: <span class="hljs-string">`none; margin-top: 0px;`</span>
    &#125;);

    <span class="hljs-built_in">this</span>.positiveY = vscode.window.createTextEditorDecorationType(<vscode.DecorationRenderOptions>&#123;
        <span class="hljs-attr">textDecoration</span>: <span class="hljs-string">`none; margin-top: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.config.shakeIntensity&#125;</span>px;`</span>
    &#125;);

    <span class="hljs-built_in">this</span>.shakeDecorations = [
        <span class="hljs-built_in">this</span>.negativeX,
        <span class="hljs-built_in">this</span>.positiveX,
        <span class="hljs-built_in">this</span>.negativeY,
        <span class="hljs-built_in">this</span>.positiveY
    ];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后呢？就是定时让 editor 抖起来啊：</p>
<p>也是根据编辑的 position 算出 range，然后给这段 range 加装饰</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">private shake = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.config.enableShake) &#123;
        <span class="hljs-keyword">return</span>;
    &#125;

   <span class="hljs-comment">// 当前 editor</span>
    <span class="hljs-keyword">const</span> activeEditor = vscode.window.activeTextEditor;

  <span class="hljs-comment">// 要抖动的 range，也就是当前行</span>
    <span class="hljs-keyword">const</span> xRanges = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < activeEditor.document.lineCount; i++) &#123;
        xRanges.push(<span class="hljs-keyword">new</span> vscode.Range(<span class="hljs-keyword">new</span> vscode.Position(i, <span class="hljs-number">0</span>), <span class="hljs-keyword">new</span> vscode.Position(i, <span class="hljs-number">1</span>)));
    &#125;

  <span class="hljs-comment">// 加装饰</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Math</span>.random() > <span class="hljs-number">0.5</span>) &#123;
        activeEditor.setDecorations(<span class="hljs-built_in">this</span>.negativeX, []);
        activeEditor.setDecorations(<span class="hljs-built_in">this</span>.positiveX, xRanges);
    &#125; <span class="hljs-keyword">else</span> &#123;
        activeEditor.setDecorations(<span class="hljs-built_in">this</span>.positiveX, []);
        activeEditor.setDecorations(<span class="hljs-built_in">this</span>.negativeX, xRanges);
    &#125;

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Math</span>.random() > <span class="hljs-number">0.5</span>) &#123;
        activeEditor.setDecorations(<span class="hljs-built_in">this</span>.negativeY, []);
        activeEditor.setDecorations(<span class="hljs-built_in">this</span>.positiveY, <span class="hljs-built_in">this</span>.fullRange);
    &#125; <span class="hljs-keyword">else</span> &#123;
        activeEditor.setDecorations(<span class="hljs-built_in">this</span>.positiveY, []);
        activeEditor.setDecorations(<span class="hljs-built_in">this</span>.negativeY, <span class="hljs-built_in">this</span>.fullRange);
    &#125;

    <span class="hljs-built_in">clearTimeout</span>(<span class="hljs-built_in">this</span>.shakeTimeout);
    <span class="hljs-built_in">this</span>.shakeTimeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.unshake();
    &#125;, <span class="hljs-number">1000</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，就是定时加不同的位移样式，随机上下左右抖。</p>
<h3 data-id="heading-3">放烟花</h3>
<p>然后我们来放烟花，思路我们分析过了，就是在编辑的位置加上一个 gif，然后下次放的时候去掉上次的。</p>
<p>来按流程走一遍：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 当前编辑器</span>
<span class="hljs-keyword">const</span> activeEditor = vscode.window.activeTextEditor;
<span class="hljs-comment">// 当前编辑位置</span>
<span class="hljs-keyword">const</span> cursorPosition = vscode.window.activeTextEditor.selection.active;
<span class="hljs-comment">// 要加装饰的范围</span>
<span class="hljs-keyword">const</span> delta = left ? -<span class="hljs-number">2</span> : <span class="hljs-number">1</span>;
<span class="hljs-keyword">const</span> newRange = <span class="hljs-keyword">new</span> vscode.Range(
    cursorPosition.with(cursorPosition.line, cursorPosition.character),
    cursorPosition.with(cursorPosition.line, <span class="hljs-built_in">Math</span>.max(<span class="hljs-number">0</span>, cursorPosition.character + delta))
);
<span class="hljs-comment">//创建装饰对象</span>
<span class="hljs-keyword">const</span> decoration = vscode.window.createTextEditorDecorationType(<vscode.DecorationRenderOptions>&#123;
    <span class="hljs-attr">before</span>: &#123;
        <span class="hljs-comment">// before 样式</span>
    &#125;,
    <span class="hljs-attr">textDecoration</span>: <span class="hljs-string">`当前元素样式`</span>,
    <span class="hljs-attr">rangeBehavior</span>: vscode.DecorationRangeBehavior.ClosedClosed
&#125;);
<span class="hljs-comment">// 给该范围加装饰</span>
activeEditor.setDecorations(decoration, [newRange]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>加装饰的流程我们走完了，但是样式还没填，怎么加呢？</p>
<p>首先当前元素要相对定位，然后加个 before 伪元素，设置为绝对定位并且 left 和 top 为负数。</p>
<p>之后就是设置背景图片了，power mode 提供了这么多 gif 可选。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e64e7a9aba674fb18d1785d8b810ba06~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以呢，装饰对象就是这样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 背景图片的样式</span>
<span class="hljs-keyword">const</span> backgroundCss = <span class="hljs-built_in">this</span>.getBackgroundCssSettings(explosionUrl);

<span class="hljs-comment">//位置的样式</span>
<span class="hljs-keyword">const</span> defaultCss = &#123;
    <span class="hljs-attr">position</span>: <span class="hljs-string">'absolute'</span>,
    [CSS_LEFT] : <span class="hljs-string">`-10px`</span>,
    [CSS_TOP]: <span class="hljs-string">`-1.2rem`</span>,
    <span class="hljs-attr">width</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.config.explosionSize&#125;</span>ch`</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.config.explosionSize&#125;</span>rem`</span>,
    <span class="hljs-attr">display</span>: <span class="hljs-string">`inline-block`</span>,
    [<span class="hljs-string">'z-index'</span>]: <span class="hljs-number">1</span>,
    [<span class="hljs-string">'pointer-events'</span>]: <span class="hljs-string">'none'</span>,
&#125;;

<span class="hljs-comment">// 样式对象转换为字符串</span>
<span class="hljs-keyword">const</span> backgroundCssString = <span class="hljs-built_in">this</span>.objectToCssString(backgroundCss);
<span class="hljs-keyword">const</span> defaultCssString = <span class="hljs-built_in">this</span>.objectToCssString(defaultCss);
<span class="hljs-keyword">const</span> customCssString = <span class="hljs-built_in">this</span>.objectToCssString(<span class="hljs-built_in">this</span>.config.customCss || &#123;&#125;);

<span class="hljs-comment">// 创建装饰对象</span>
<span class="hljs-keyword">const</span> decoration = vscode.window.createTextEditorDecorationType(<vscode.DecorationRenderOptions>&#123;
    <span class="hljs-attr">before</span>: &#123;
        <span class="hljs-attr">contentText</span>:<span class="hljs-string">''</span>,
        <span class="hljs-attr">textDecoration</span>: <span class="hljs-string">`none; <span class="hljs-subst">$&#123;defaultCssString&#125;</span><span class="hljs-subst">$&#123;backgroundCssString&#125;</span> <span class="hljs-subst">$&#123;customCssString&#125;</span>`</span>,
    &#125;,
    <span class="hljs-attr">textDecoration</span>: <span class="hljs-string">`none; position: relative;`</span>,
    <span class="hljs-attr">rangeBehavior</span>: vscode.DecorationRangeBehavior.ClosedClosed
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">性能优化</h4>
<p>每次编辑都加一个 gif 性能肯定很差，所以得做优化，可以从触发频率、同时存在的 gif 数量来考虑：</p>
<ul>
<li>节流，每1秒只能触发一次</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ab23543f6ce48878573d16791e968bd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>gif 存在一段时间就删掉</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15a5523287914f18a72f5dc76263e148~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>大功告成，这样我们把抖动和放烟花在 vscode 里面实现了一遍。</p>
<p>但是，还得加个触发的入口。</p>
<p>什么时候触发呢？涉及到两个 api：</p>
<ul>
<li>编辑文本的时候，出现效果</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">vscode.workspace.onDidChangeTextDocument(onDidChangeTextDocument);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>修改了插件配置的时候，重新设置插件对象</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">vscode.workspace.onDidChangeConfiguration(onDidChangeConfiguration);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从怎么触发的，到触发后干什么，我们都清楚了，接下来呢，还要会怎么注册这个插件到 vscode 中。</p>
<h2 data-id="heading-5">插件注册</h2>
<p>注册插件就是在 package.json 里面配置一下，指定触发时机：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"activationEvents"</span>: [
    <span class="hljs-string">"*"</span>
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>指定插件入口：</p>
<pre><code class="copyable">  "main": "./out/src/extension",
<span class="copy-code-btn">复制代码</span></code></pre>
<p>指定插件的配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"contributes"</span>: &#123;
    <span class="hljs-string">"configuration"</span>: &#123;
      <span class="hljs-string">"title"</span>: <span class="hljs-string">"Power Mode"</span>,
      <span class="hljs-string">"properties"</span>: &#123;
        <span class="hljs-string">"powermode.enabled"</span>: &#123;
          <span class="hljs-string">"default"</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 默认值</span>
          <span class="hljs-string">"type"</span>: <span class="hljs-string">"boolean"</span>,<span class="hljs-comment">// 值类型</span>
          <span class="hljs-string">"description"</span>: <span class="hljs-string">"Enable to activate POWER MODE!!!"</span>
        &#125;
      &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">总结</h2>
<p>vscode 基于 electron，而 electron 基于 chromium，所以还是用网页来做 ui 的，那么很多网页里面的效果，基本都可以在编辑器实现。</p>
<p>但是是受约束的，要熟悉整个加装饰的流程：</p>
<ul>
<li>拿到当前编辑器 (activeEditor)</li>
<li>拿到当前编辑的位置 (position)</li>
<li>算出要加装饰的范围 (range)</li>
<li>创建装饰对象 (decorationType)</li>
<li>给那段范围的文本加装饰 （addDecoration）</li>
</ul>
<p>抖动和放烟花都是基于这个 api 实现的，不过抖动是做上下左右的随机位移，放烟花是在编辑的位置加动图。</p>
<p>实现思路有了，还得指定触发的入口，也就是文本编辑的时候（onDidChangeTextDocument）。还有配置改变也得做下处理（onDidChangeConfiguration）。</p>
<p>之后，注册到 vscode 就可以了，在 package.json 里面配置入口（main）、生效事件（activeEvent）、配置项（contibutes.configuration）</p>
<p>希望这篇文章能够帮你理清 vscode 里面一些编辑效果的实现思路。</p>
<p>兄弟萌，让我们一起在 vscode 里面放烟花吧！</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07ca3d24ed924e6a847365782316689c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>(插件名叫 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhoovercj%2Fvscode-power-mode" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/hoovercj/vscode-power-mode" ref="nofollow noopener noreferrer">vscode-power-mode</a>，感兴趣可以体验一下，或者去看看源码)。</p></div>  
</div>
            