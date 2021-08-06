
---
title: 'PPT 居然可以用 js 写？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://img.alicdn.com/imgextra/i1/O1CN01bNJswj1bY3Q3PcSwB_!!6000000003476-2-tps-2688-1584.png'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 18:57:58 GMT
thumbnail: 'https://img.alicdn.com/imgextra/i1/O1CN01bNJswj1bY3Q3PcSwB_!!6000000003476-2-tps-2688-1584.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>文/ 阿里淘系 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.imgcook.com%2Fblog" target="_blank" rel="nofollow noopener noreferrer" title="https://www.imgcook.com/blog" ref="nofollow noopener noreferrer">F(x) Team</a> - 旭伦</p>
</blockquote>
<p>用 powerpoint 或者 keynote 写演示文稿，对于代码、数学公式等的支持一直是个痛点。而且对于前端同学来说，一身的 css 功力用不上也是个痛点。对于使用 markdown 来写文档的同学来说，将文档转成ppt需要重新排版也是件重复性的工作量。</p>
<p>于是我们需要一个基于 web 技术的 ppt 框架，reveal.js 在这个领域成名已久了，而且上个月还有发布新版本，维护得还蛮好，第一步我们就选它了。</p>
<h2 data-id="heading-0">将 reveal.js 运行起来</h2>
<p>首先 clone 一份 reveal.js 最新的代码：</p>
<pre><code class="copyable">git clone https://github.com/hakimel/reveal.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们照抄一份index.html，比如叫做study.html:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">title</span>></span>reveal.js<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"dist/reset.css"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"dist/reveal.css"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"dist/theme/black.css"</span>></span>

<span class="hljs-comment"><!-- Theme used for syntax highlighted code --></span>
<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"plugin/highlight/monokai.css"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"reveal"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"slides"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">section</span>></span>Slide 1<span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="hljs-tag"><<span class="hljs-name">section</span>></span>Slide 2<span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"dist/reveal.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"plugin/notes/notes.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"plugin/markdown/markdown.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"plugin/highlight/highlight.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-comment">// More info about initialization & config:</span>
<span class="hljs-comment">// - https://revealjs.com/initialization/</span>
<span class="hljs-comment">// - https://revealjs.com/config/</span>
Reveal.initialize(&#123;
<span class="hljs-attr">hash</span>: <span class="hljs-literal">true</span>,

<span class="hljs-comment">// Learn about plugins: https://revealjs.com/plugins/</span>
<span class="hljs-attr">plugins</span>: [ RevealMarkdown, RevealHighlight, RevealNotes ]
&#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在reveal.js目录下运行npm install, 然后运行npm start就可以启动一个server来查看上面的ppt网页。
默认使用8000端口，如果被占用了可以通过指定port参数换一个，比如我们换成30800吧：</p>
<pre><code class="copyable">npm start -- --port=30800
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后通过访问浏览器的127.0.0.1:30800/study.html就可以看到我们的ppt啦：</p>
<div align="middle"><img src="https://img.alicdn.com/imgextra/i1/O1CN01bNJswj1bY3Q3PcSwB_!!6000000003476-2-tps-2688-1584.png" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<h2 data-id="heading-1">reveal.js step by step</h2>
<p>上面这个网页其实挺容易懂的，不用react或vue框架，也不需要配置webpack。
其核心内容部分其实非常简单，就是每一页演示文稿对应一个section。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"reveal"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"slides"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">section</span>></span>Slide 1<span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="hljs-tag"><<span class="hljs-name">section</span>></span>Slide 2<span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">支持markdown</h3>
<p>reveal.js的第一个强大功能是直接可以使用markdown来写演示文稿。在我们上面默认的html模板中已经加载了RevealMarkdown插件。所以我们要做的就是在下面的模板上写markdown就好。</p>
<pre><code class="hljs language-html copyable" lang="html">                <span class="hljs-tag"><<span class="hljs-name">section</span> <span class="hljs-attr">data-markdown</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">textarea</span> <span class="hljs-attr">data-markdown</span>></span>                     
                    <span class="hljs-tag"></<span class="hljs-name">textarea</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来看个例子：</p>
<pre><code class="hljs language-html copyable" lang="html">                <span class="hljs-tag"><<span class="hljs-name">section</span> <span class="hljs-attr">data-markdown</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">textarea</span> <span class="hljs-attr">data-markdown</span>></span>
推荐系统的主要算法包括：
- 矩阵分解
- 线性模型
- 树模型
- 深度学习模型                        
                    <span class="hljs-tag"></<span class="hljs-name">textarea</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成的幻灯片如下：</p>
<div align="middle"><img src="https://img.alicdn.com/imgextra/i3/O1CN01WiPvEH1kYocgEjma6_!!6000000004696-2-tps-2688-1594.png" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<h3 data-id="heading-3">换个主题</h3>
<p>如果觉得黑底白字的太丑了，我们可以换个主题。</p>
<p>主题就是个css，在这条语句里引用：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"dist/theme/black.css"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>换成dist/theme/下面其它的css主题，或者干脆自己撸一个。</p>
<p>比如改成：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"dist/theme/beige.css"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果变成这样：</p>
<div align="middle"><img src="https://img.alicdn.com/imgextra/i3/O1CN016ujuxc1wDXc3ji9BW_!!6000000006274-2-tps-2688-1588.png" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<h3 data-id="heading-4">支持数学公式</h3>
<p>支持数学公式的js库和插件默认并没有包含在默认模板中，我们需要将其增加进来。</p>
<p>我们先把数学公式库的js引进来：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"plugin/math/math.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在初始化时Reveal.initialize增加对于数学公式的配置,并且引入cdn上的mathjax库：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">      Reveal.initialize(&#123;
        <span class="hljs-attr">hash</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">math</span>: &#123;
          <span class="hljs-attr">mathjax</span>:
            <span class="hljs-string">"https://cdn.jsdelivr.net/gh/mathjax/mathjax@2.7.8/MathJax.js"</span>,
          <span class="hljs-attr">config</span>: <span class="hljs-string">"TeX-AMS_HTML-full"</span>,
          <span class="hljs-comment">// pass other options into `MathJax.Hub.Config()`</span>
          <span class="hljs-attr">TeX</span>: &#123; <span class="hljs-attr">Macros</span>: &#123; <span class="hljs-attr">RR</span>: <span class="hljs-string">"&#123;\\bf R&#125;"</span> &#125; &#125;,
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，在plugins中增加RevealMath插件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">        plugins: [RevealMarkdown, RevealHighlight, RevealNotes, RevealMath],
      &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整的代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"plugin/math/math.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      Reveal.initialize(&#123;
        <span class="hljs-attr">hash</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">math</span>: &#123;
          <span class="hljs-attr">mathjax</span>:
            <span class="hljs-string">"https://cdn.jsdelivr.net/gh/mathjax/mathjax@2.7.8/MathJax.js"</span>,
          <span class="hljs-attr">config</span>: <span class="hljs-string">"TeX-AMS_HTML-full"</span>,
          <span class="hljs-comment">// pass other options into `MathJax.Hub.Config()`</span>
          <span class="hljs-attr">TeX</span>: &#123; <span class="hljs-attr">Macros</span>: &#123; <span class="hljs-attr">RR</span>: <span class="hljs-string">"&#123;\\bf R&#125;"</span> &#125; &#125;,
        &#125;,

        <span class="hljs-attr">plugins</span>: [RevealMarkdown, RevealHighlight, RevealNotes, RevealMath],
      &#125;);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>插件引入之后我们就可以在幻灯片中写公式了。</p>
<p>可以直接在section中写：</p>
<pre><code class="copyable">        <section>
            \[\begin&#123;aligned&#125;
            \ MAE(X,h)=\frac&#123;1&#125;&#123;m&#125; \sum_&#123;i=1&#125;^m|h(x^i)-y^&#123;(i)&#125;| \
            \end&#123;aligned&#125; \]
        </section>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以嵌入到markdown中：</p>
<pre><code class="copyable">        <section data-markdown>
          <textarea data-markdown>
                        $MAE(X,h)=\frac&#123;1&#125;&#123;m&#125; \sum_&#123;i=1&#125;^m|h(x^i)-y^&#123;(i)&#125;|$                      
          </textarea>
        </section>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>出来的效果是这样的：</p>
<div align="middle"><img src="https://img.alicdn.com/imgextra/i2/O1CN01t48e7E1WMzmNxEiDa_!!6000000002775-2-tps-2016-1260.png" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<h3 data-id="heading-5">代码高亮</h3>
<p>代码高亮默认是支持的，我们可以在markdown里面用```来使用：</p>
<div align="middle"><img src="https://img.alicdn.com/imgextra/i2/O1CN01REPLjO2A4IEqZ1QbK_!!6000000008149-2-tps-652-442.png" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<p>显示出来的效果如下：</p>
<div align="middle"><img src="https://img.alicdn.com/imgextra/i2/O1CN01VOrzf41hnytHPXiPg_!!6000000004323-2-tps-1240-734.png" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<p>也可以直接使用html的pre和code标签来显示：</p>
<pre><code class="hljs language-html copyable" lang="html">        <span class="hljs-tag"><<span class="hljs-name">section</span>></span>
            
<span class="hljs-tag"><<span class="hljs-name">pre</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">code</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"language-javascript"</span>></span>
                    model.compile(&#123;
                        optimizer: tf.train.sgd(0.000001),
                        loss: 'meanSquaredError'
                    &#125;);
                
                    return model.fitDataset(flattenedDataset, &#123;
                        epochs: 10,
                        callbacks: &#123;
                            onEpochEnd: async (epoch, logs) => &#123;
                                console.log(epoch + ':' + logs.loss);
                            &#125;
                        &#125;
                    &#125;);
                <span class="hljs-tag"></<span class="hljs-name">code</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">pre</span>></span>
<span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示的效果如下：</p>
<div align="middle"><img src="https://img.alicdn.com/imgextra/i3/O1CN01q6KanQ1hduAxcnLLw_!!6000000004301-2-tps-2688-1598.png" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<p>代码高亮的theme也是可以更换的，只要更换plugin/highlight下面的css即可，例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"plugin/highlight/zenburn.css"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们顺便把reveal.js的theme也换一下：</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"dist/theme/moon.css"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果变成下面这样：</p>
<div align="middle"><img src="https://img.alicdn.com/imgextra/i3/O1CN01rnw8iX1kNp7CMCB2j_!!6000000004672-2-tps-2688-1582.png" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<p>我们汇总下上面的代码：</p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"
    />

    <title>reveal.js学习</title>

    <link rel="stylesheet" href="dist/reset.css" />
    <link rel="stylesheet" href="dist/reveal.css" />
    <link rel="stylesheet" href="dist/theme/moon.css" />

    <!-- Theme used for syntax highlighted code -->
    <link rel="stylesheet" href="plugin/highlight/monokai.css" />
  </head>
  <body>
    <div class="reveal">
      <div class="slides">
        <section>Slide 1</section>
        <section>
            \[\begin&#123;aligned&#125;
            \ MAE(X,h)=\frac&#123;1&#125;&#123;m&#125; \sum_&#123;i=1&#125;^m|h(x^i)-y^&#123;(i)&#125;| \
            \end&#123;aligned&#125; \]
        </section>
        <section data-markdown>
          <textarea data-markdown>
推荐系统的主要算法包括：
- 矩阵分解
- 线性模型
- 树模型
- 深度学习模型                        
                    </textarea
          >
        </section>
        <section data-markdown>
          <textarea data-markdown>
                        $MAE(X,h)=\frac&#123;1&#125;&#123;m&#125; \sum_&#123;i=1&#125;^m|h(x^i)-y^&#123;(i)&#125;|$                      
          </textarea>
        </section>
        <section>
            
<pre>
                <code class="language-javascript">
                    model.compile(&#123;
                        optimizer: tf.train.sgd(0.000001),
                        loss: 'meanSquaredError'
                    &#125;);
                
                    return model.fitDataset(flattenedDataset, &#123;
                        epochs: 10,
                        callbacks: &#123;
                            onEpochEnd: async (epoch, logs) => &#123;
                                console.log(epoch + ':' + logs.loss);
                            &#125;
                        &#125;
                    &#125;);
                </code>
            </pre>
</section>
      </div>
    </div>

    <script src="dist/reveal.js"></script>
    <script src="plugin/notes/notes.js"></script>
    <script src="plugin/markdown/markdown.js"></script>
    <script src="plugin/highlight/highlight.js"></script>
    <script src="plugin/math/math.js"></script>
    <script>
      // More info about initialization & config:
      // - https://revealjs.com/initialization/
      // - https://revealjs.com/config/
      Reveal.initialize(&#123;
        hash: true,
        math: &#123;
          mathjax:
            "https://cdn.jsdelivr.net/gh/mathjax/mathjax@2.7.8/MathJax.js",
          config: "TeX-AMS_HTML-full",
          // pass other options into `MathJax.Hub.Config()`
          TeX: &#123; Macros: &#123; RR: "&#123;\\bf R&#125;" &#125; &#125;,
        &#125;,

        // Learn about plugins: https://revealjs.com/plugins/
        plugins: [RevealMarkdown, RevealHighlight, RevealNotes, RevealMath],
      &#125;);
    </script>
  </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">背景图片</h3>
<p>section支持data-background-image属性来指定背景图片。</p>
<p>例：</p>
<pre><code class="hljs language-html copyable" lang="html">        <span class="hljs-tag"><<span class="hljs-name">section</span> <span class="hljs-attr">data-background-image</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/www.jsdelivr.com/000a3f2b6a7baa6ae0f786a251fd105e4b230d8e/img/landing/network-map@2x.png"</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">HTML and CSS</h2>
<p>比起markdown，HTML和CSS也是写演示文稿的好手段，可控的方法更多。而且也可以跟reveal.js的功能有更好的结合。</p>
<p>在section中，可以像在普通网页中一样写HTML标签：</p>
<pre><code class="hljs language-html copyable" lang="html">        <span class="hljs-tag"><<span class="hljs-name">section</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h3</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"&#123;color: #ffec3d;&#125;"</span>></span>推荐系统的冷启动<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span>></span>利用热门数据<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span>></span>利用用户注册信息<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span>></span>利用第三方数据<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span>></span>利用物品内容属性<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以在header中写style属性给section中使用。</p>
<p>比如默认字体太大了，我们可以给调一调：</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">ul</span> &#123;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">18px</span>;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">淡入淡出</h3>
<p>结合html标签，可以指定淡入淡出的效果。
这可以通过给标签添加class属性为fragment实现。</p>
<p>我们来看个淡入的例子：</p>
<pre><code class="hljs language-html copyable" lang="html">        <span class="hljs-tag"><<span class="hljs-name">section</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>推荐系统的冷启动<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"fragment"</span>></span>利用热门数据<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"fragment"</span>></span>利用用户注册信息<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"fragment"</span>></span>利用第三方数据<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"fragment"</span>></span>利用物品内容属性<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<div align="middle"><img src="https://img.alicdn.com/imgextra/i3/O1CN01GjJhgu1Oo0D1QvKZj_!!6000000001751-2-tps-2688-1586.png" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<p>除了淡入之外，我们还可以对某项进行标红：</p>
<pre><code class="hljs language-html copyable" lang="html">        <span class="hljs-tag"><<span class="hljs-name">section</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>推荐系统的冷启动<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"fragment highlight-red"</span>></span>利用热门数据<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span>></span>利用用户注册信息<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span>></span>利用第三方数据<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span>></span>利用物品内容属性<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<div align="middle"><img src="https://img.alicdn.com/imgextra/i1/O1CN01FdK6DZ1g4oD2Pddoh_!!6000000004089-2-tps-2688-1592.png" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<h2 data-id="heading-9">导出为pdf</h2>
<p>演示文稿做好之后，除了在浏览器中看，我们也可以导出成为pdf格式。
方法是在URI之后增加"?print-pdf"后缀，比如：<a href="https://link.juejin.cn/?target=http%3A%2F%2F0.0.0.0%3A30800%2Fstudy.html%3Fprint-pdf" target="_blank" rel="nofollow noopener noreferrer" title="http://0.0.0.0:30800/study.html?print-pdf" ref="nofollow noopener noreferrer">http://0.0.0.0:30800/study.html?print-pdf</a></p>
<p>然后我们再用另存为pdf格式功能来保存下来就好。</p>
<div align="middle"><img src="https://img.alicdn.com/imgextra/i3/O1CN01tOnY6w1kTJrs50QIB_!!6000000004684-2-tps-2686-1594.png" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<h2 data-id="heading-10">更进一步</h2>
<p>除了上面介绍的基本特性之外，reveal.js支持自动播放、自制插件、支持处理事件等等有利于开发人员写slides的特性。相信能给你的slides带来新的好玩的东西，将汇报与分享变成乐趣。
Enjoy it!</p>
  <br>
  <hr>
  <div align="middle"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fweibo.com%2F7513068590%2Fprofile%3Ftopnav%3D1%26wvr%3D6%26is_all%3D1" target="_blank" rel="nofollow noopener noreferrer" title="https://weibo.com/7513068590/profile?topnav=1&wvr=6&is_all=1" ref="nofollow noopener noreferrer"> 淘系前端-F-x-Team 开通微博</a> 啦！（微博登录后可见）</div>
  <div align="middle">除文章外还有更多的团队内容等你解锁🔓</div>
  <div align="middle">
    <a href="https://link.juejin.cn/?target=https%3A%2F%2Fweibo.com%2F7513068590%2Fprofile%3Ftopnav%3D1%26wvr%3D6%26is_all%3D1" target="_blank" rel="nofollow noopener noreferrer" title="https://weibo.com/7513068590/profile?topnav=1&wvr=6&is_all=1" ref="nofollow noopener noreferrer"> 
      <img src="https://img.alicdn.com/imgextra/i3/O1CN014UK2871d3UCv0TA9F_!!6000000003680-2-tps-611-530.png" loading="lazy" referrerpolicy="no-referrer">
    </a>
  </div>
  <br></div>  
</div>
            