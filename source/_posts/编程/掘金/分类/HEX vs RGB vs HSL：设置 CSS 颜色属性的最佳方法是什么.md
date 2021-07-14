
---
title: 'HEX vs RGB vs HSL：设置 CSS 颜色属性的最佳方法是什么'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0840578e85e410781042dd1585cff65~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 02:03:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0840578e85e410781042dd1585cff65~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.bitsrc.io%2Fhex-vs-rgb-vs-hsl-what-is-the-best-method-to-set-css-color-property-f45d2debeee" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.bitsrc.io/hex-vs-rgb-vs-hsl-what-is-the-best-method-to-set-css-color-property-f45d2debeee" ref="nofollow noopener noreferrer">HEX vs RGB vs HSL: What is the Best Method to set CSS Color Property</a></li>
<li>原文作者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2F%40wnethmi96" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/@wnethmi96" ref="nofollow noopener noreferrer">Nethmi Wijesinghe</a></li>
<li>译文出自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%2Fblob%2Fmaster%2Farticle%2F2021%2Fhex-vs-rgb-vs-hsl-what-is-the-best-method-to-set-css-color-property.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner/blob/master/article/2021/hex-vs-rgb-vs-hsl-what-is-the-best-method-to-set-css-color-property.md" ref="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FPassionPenguin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/PassionPenguin" ref="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FChorer" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Chorer" ref="nofollow noopener noreferrer">Chorer</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnia3y" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nia3y" ref="nofollow noopener noreferrer">nia3y</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FCarlosChenN" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/CarlosChenN" ref="nofollow noopener noreferrer">CarlosChenN</a></li>
</ul>
</blockquote>
<p>不知道你是否了解 HEX、RGB 和 HSL 之间的区别，以及其中任意一种的各种优势？</p>
<hr>
<p>在深入探讨这个问题之前，让我们简要了解每种颜色方法的含义。</p>
<h1 data-id="heading-0">颜色方法的定义</h1>
<p><strong>Hex</strong> 颜色值是最流行的设置 CSS 颜色属性的方法之一，尤其是在开发人员中。几乎所有浏览器都支持它。</p>
<p>我们可以在十六进制颜色代码中定义紫色，如下所示：</p>
<pre><code class="hljs language-text copyable" lang="text">800080
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的颜色的格式规定是 <code>#RRGGBB</code>，其中 <code>RR</code>（红色）、<code>GG</code>（绿色）和 <code>BB</code>（蓝色）是介于 <code>00</code> 和 <code>FF</code> 之间的<strong>十六进制整数</strong>，表示色彩强度。</p>
<h1 data-id="heading-1">HEX 和 RGB 的区别</h1>
<p><strong>RGB</strong> 或 <strong>Red/Green/Blue</strong>（即红/绿/蓝）也被用于在 CSS 中定义颜色，是另一种广受欢迎的方法。RGB 配色方案是一种三通道格式，其中 r、g、b 三色的数值是 0 到 255 之间的整数。以下是 RGB 颜色的示例：</p>
<pre><code class="hljs language-text copyable" lang="text">rgb(128, 0, 128)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述 RGB 颜色代码的实现与上文中 HEX 颜色一致。你可能想知道，明明十六进制颜色代码更容易记住和输入，为什么我们还要使用 RGB 呢？</p>
<blockquote>
<p>嗯，每种颜色方法都有自己的好处。RGB 的美妙之处在于它允许你为颜色添加不透明度。</p>
</blockquote>
<p>这就是 <strong>RGBA</strong> 的强处了 😎。在 CSS3 中，RGB 配色方案新增了一个额外的 <strong>alpha</strong> 通道，以指示颜色的不透明度。</p>
<blockquote>
<p>译者注：其实嘛，Hex 也支持，比如说 50% 黑色就是 <code>#00000088</code>，最后两位数为十六进制的透明度，范围也是 <code>00</code> 到 <code>FF</code>。</p>
</blockquote>
<h1 data-id="heading-2">新人，HSL！</h1>
<p><strong>HSL</strong> 代表色相 Hue、饱和度 Saturation 和亮度 Lightness，是另一种在 CSS 中声明颜色的方式。紫色的 HSL 颜色值可以指定如下：</p>
<pre><code class="hljs language-text copyable" lang="text">hsl(300, 100%, 25.1%)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如你所见，第一个参数用于定义色相，它是实际纯色的值，例如红色、黄色、绿色、蓝色、洋红色等。色相是一个颜色轮，取值为 0 到 360 的度数。这里 0 和 360 度代表红色，120 度代表绿色，240 度代表蓝色。</p>
<p>与 RGB 不同，在 HSL 中，颜色的饱和度和亮度都可以改变。</p>
<p>这些颜色可以是暗淡的，也可以是鲜艳的。颜色越少，它变成灰色的阴影就越多。<strong>饱和度</strong>指代混合色中存在多少颜色，它能控制颜色的<strong>鲜艳或暗淡</strong>程度。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0840578e85e410781042dd1585cff65~tplv-k3u1fbpfcp-zoom-1.image" alt="使用 Brandon Mathis 的 HSL 颜色选择器" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如你所见，当饱和度值沿线从 100% 变为 0% 时，颜色会从纯色调变为暗色调。</p>
<p>此外，还有第三个参数代表亮度。这玩意也是一个百分比值，数值范围也是 0% 到 100%，用于描述颜色中黑色或白色的占比。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c815cdb29eb6490da02361b051c177f5~tplv-k3u1fbpfcp-zoom-1.image" alt="使用 Brandon Mathis 的 HSL 颜色选择器" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这类似于水彩在绘画中的使用。如果你想让颜色更亮，你可以添加白色，如果你想让颜色更深，你可以添加黑色。因此，100% 的亮度表示完全的白色，50% 表示实际色调颜色，0% 表示纯黑色。</p>
<p><strong>HSLA</strong> 与 RGBA 类似，是 HSL 的扩展。第四个通道表示颜色的不透明度，与 RGBA 和 Hex-alpha 并无二致。不透明度以十进制值指定，就像在 RGBA 中一样，其中 1 表示完全不透明，0 表示完全透明，中间的所有取值都是部分不透明的。</p>
<p>然而，尽管大多数浏览器支持 RGB 和 Hex 颜色代码，HSL 颜色主要还是在基于 HTML5 的浏览器中得到支持。</p>
<hr>
<p>你可能已经在 CSS 中设置颜色属性时使用过所有或部分的这些颜色方法。Hex 是我个人的最爱，但是他们之间究竟有什么区别，各自又有着怎样的优势？话不多说，一起来了解一下吧！</p>
<h1 data-id="heading-3">在 CSS 中指定颜色的最佳方法是什么？</h1>
<p>如果你习惯了 HTML，你可能更习惯使用 Hex 颜色值，因为 Hex 颜色值在 HTML 中被大量使用。但如果你学过设计，你可能会使用 RGB 表示法，因为它是大多数设计软件（如 Photoshop、Corel 和 Illustrator）中最常用的格式。</p>
<p>我的建议是，如果你是一名纯粹的开发人员并且只想完成你的项目，请继续使用你最熟悉的颜色方式。</p>
<blockquote>
<p>因为浏览器并不真正关心你使用的是哪种颜色格式，即使不同方法之间有细微的性能变化，但性能差异可以忽略不计。</p>
</blockquote>
<p>除此之外，如果你担心可用性、决策对开发人员的影响等，让我们看看哪种方法最适合你的情况。</p>
<p>让我们从十六进制表示法开始。由于其简短的符号，十六进制非常有吸引力。许多开发人员发现，与 RGB 和 HSL 相比，Hex 值非常易于阅读，而且更容易复制到他们喜欢的文本编辑器中。</p>
<p>RGB 在较旧版本的 Internet Explorer（9 及更早版本）中广为人知并受支持。</p>
<h2 data-id="heading-4">HSL 旨在让人类更容易理解！</h2>
<p>RGB 和 Hex 等格式的机器可读性比人类可读性强。相反，HSL 旨在让人类更好地理解。HSL 是一种更新且自然的颜色处理方式。</p>
<blockquote>
<p>与在 Hex 和 RGBA 中你必须通过一些数字来获得你想要的颜色不同，在 HSL 中，我们可以使用 Hue 定义颜色并使用第二和第三个参数百分比来获得你想要的饱和度和亮度级别。</p>
</blockquote>
<p>如果我告诉你网页标题需要是 <code>#578557</code> 或 <code>rgb(87, 133, 87)</code>，你能猜出是什么颜色吗？ 😵 不，除非你是电脑。但是，与此同时，如果我给你 HSL 中的颜色：<code>hsl(120, 21%, 43%)</code>？现在猜测有点容易了吧？ Hue 值为 120°，表示它是纯绿色。接下来，它的饱和度为 61%，表明它距离暗灰色（一种非常不饱和的绿色）还有 21%。最后，亮度 43% 意味着颜色从纯色到较暗的一面有 7%。</p>
<p>好的，假设你想让按钮颜色在悬停时更亮，单击时更暗。使用 HSL 轻而易举 —— 只需要增加和减少亮度值，仅此而已，是不是非常吃惊！！ 😎 但是在不使用工具或设计师的帮助下用十六进制或 RGB 来做到这一点是不可能的。</p>
<blockquote>
<p>HSL 是一种模仿现实世界的直观颜色符号。</p>
</blockquote>
<p>例如，让我们考虑一张浅蓝色的色纸。它的三种格式的颜色值分别是：</p>















<table><thead><tr><th>Hex</th><th>RGB</th><th>HSL</th></tr></thead><tbody><tr><td>#ADD8E6</td><td>rgb(173, 216, 230)</td><td>hsl(195, 53.3%, 79%)</td></tr></tbody></table>
<p>好的，现在把你的手握在离表面几英寸的地方。你手的影子让表面变暗了一点，对吧？在不改变颜色本身的情况下，我们是无法使用 RGB 或十六进制表示法表示这种颜色变化的。但是在 HSL 中，我们仅仅需要稍微调整亮度值，然后就 <strong>大功告成 💥</strong> 了！我们根本不需要对原始颜色进行任何更改，是不是真的很酷？</p>























<table><thead><tr><th></th><th>Hex</th><th>RGB</th><th>HSL</th></tr></thead><tbody><tr><td>原值</td><td>#4f2017</td><td>rgb(79, 32, 23)</td><td>hsl(195, 53.3%, 79%)</td></tr><tr><td>新值</td><td>#2F819D</td><td>rgb(47, 129, 157)</td><td>hsl(195, 53.3%, 50%)</td></tr></tbody></table>
<p>如你所见，Hex 和 RGB 值已经被改到面目全非了，而对于 HSL，只有一个值发生了变化。毫无疑问，在构建配色方案时，HSL 是最有用的。以底色为基础，根据需要调整饱和度和亮度，就是这样！有了 HSL，建立一个配色方案，简直就是小菜一碟。 😋</p>
<h2 data-id="heading-5">最后，这一切都取决于个人喜好！</h2>
<p>现在你可能认为 HSL 是最好的颜色表示法。但是，正如我上面提到的，旧版本的 Internet Explorer 不支持 HSL。同样，每种颜色格式都有其优点和缺点。问题是，这并不重要。</p>
<blockquote>
<p>最重要的是尽可能保持在项目中使用到的类型的一致性，因为它有助于提高生产力。</p>
</blockquote>
<ul>
<li><s>和其他两种颜色相比 Hex 有不支持透明度的限制</s>（译者注：Hex 是支持的……）</li>
<li>不使用特定工具来调整 RGBA 颜色是很很困难的</li>
<li>旧浏览器不支持 HSLA
<ul>
<li>如果你所服务的浏览器支持 HSLA 那就忽略这条吧！你可以选择使用任何格式！</li>
</ul>
</li>
</ul>
<p>在选择在项目中设置 CSS 颜色属性的最佳方法时，你可以考虑以下因素。</p>
<ol>
<li>使用与开发团队其他成员相同的格式来提高可维护性。</li>
<li>如果你已经熟悉 RGB 格式，请使用它。</li>
<li>如果你的目标访问者使用严重过时的浏览器访问你的网站，请使用 Hex，或者使用如下后备代码：</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#FF0000</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-built_in">hsla</span>(<span class="hljs-number">0</span>, <span class="hljs-number">100%</span>, <span class="hljs-number">50%</span>, <span class="hljs-number">1</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>如果以上三点还是没能让你决定使用哪一种，请使用 HSLA。HSLA 允许你像 RGBA 一样使用透明度，而且更具备可访问性。</li>
</ol>
<h2 data-id="heading-6">有哪些替代方案？</h2>
<p>除了上面提到的方法，还有一些其他方法可以用来在 CSS 中设置颜色属性。</p>
<ul>
<li><strong>使用颜色名称</strong>：所有现代浏览器都支持 140 个标准 CSS 颜色名称。颜色名称是代表特定颜色的关键字，如 <code>coral</code>。</li>
<li><code>currentcolor</code> <strong>关键字</strong>：如果需要引用一个元素的颜色，可以使用这个关键字。</li>
<li><strong>HWB 值：</strong> HWB 代表色相、白度、黑度。虽然目前 HTML 不支持它，但它被建议作为 CSS4 的新标准。</li>
<li><strong>CMYK 值</strong>：CMYK 是青色、洋红色、黄色和黑色的组合。尽管计算机屏幕使用 RGB 值来显示颜色，但打印机通常使用 CMYK 颜色值来显示颜色。与 HWB 类似，CMYK 在 HTML 中尚不支持，不过也是被建议作为 CSS4 中的新标准。</li>
</ul>
<h2 data-id="heading-7">最后</h2>
<p>颜色在网页中起着至关重要的作用。在 CSS 中，我们能使用 RGB、Hex 和 HSL 等方法来定义颜色。在本文中，我们了解了用于在 CSS 中设置颜色属性的三种主要方法，以及它们的区别和各自的优缺点，还有可用于在 CSS 中定义颜色属性的其他替代方法。</p>
<blockquote>
<p>尽管 HSLA 由于其人类可读性而比其他两种方法略有优势，但如果不是针对特定情况，则无关紧要。你可以使用任何你觉得舒服的方式。</p>
</blockquote>
<p>看看不同的优缺点，每种方法都优于其他方法，总而言之，决定使用哪种方式在 CSS 中设置颜色属性应取决于以下三个因素：</p>
<ul>
<li>偏好</li>
<li>可维护性</li>
<li>性能与效果</li>
</ul>
<p>那么，你更喜欢用什么来设置 CSS 中的颜色？Hex、RGBA、HSLA 或其他什么？原因又是什么？在评论区告诉我吧。 😃</p>
<hr>
<p>希望能在另一篇令人兴奋的文章中再次遇见你。祝你编码愉快！ 💻</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" title="https://juejin.im">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23android" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#android" ref="nofollow noopener noreferrer">Android</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23ios" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#ios" ref="nofollow noopener noreferrer">iOS</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2589%258D%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" ref="nofollow noopener noreferrer">前端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2590%258E%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" ref="nofollow noopener noreferrer">后端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%258C%25BA%25E5%259D%2597%25E9%2593%25BE" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" ref="nofollow noopener noreferrer">区块链</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25A7%25E5%2593%2581" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" ref="nofollow noopener noreferrer">产品</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E8%25AE%25BE%25E8%25AE%25A1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" ref="nofollow noopener noreferrer">设计</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" ref="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="https://link.juejin.cn/?target=http%3A%2F%2Fweibo.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="http://weibo.com/juejinfanyi" ref="nofollow noopener noreferrer">官方微博</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/juejinfanyi" ref="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            