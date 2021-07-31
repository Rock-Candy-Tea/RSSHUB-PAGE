
---
title: 'CSS（四）：盒模型（The Box Model）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5135'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 01:39:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=5135'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>在 CSS 布局中，所有元素都被盒子包围。</p>
<h1 data-id="heading-0">块级盒子和内联盒子</h1>
<p>CSS 中有两种盒子：块级盒子（Block box） 和 内联盒子（Inline box）。它们在页面流（page flow）和元素之间的关系表现不同的行为。</p>
<h2 data-id="heading-1">块级盒子</h2>
<ol>
<li>盒子会在内联的方向上扩展并占据父容器在该方向上的所有可用空间，在绝大数情况下意味着盒子会和父容器一样宽</li>
<li>每个盒子都会换行</li>
<li>width 和 height 属性可以发挥作用</li>
<li>内边距（padding）, 外边距（margin） 和 边框（border） 会将其他元素从当前盒子周围“推开”</li>
</ol>
<p>除非特殊指定，诸如标题(<h1>等)和段落(<p>)默认情况下都是块级的盒子。</p>
<h2 data-id="heading-2">内联盒子</h2>
<ol>
<li>盒子不会产生换行。</li>
<li>width 和 height 属性将不起作用。</li>
<li>垂直方向的内边距、外边距以及边框会被应用但是不会把其他处于 inline 状态的盒子推开。</li>
<li>水平方向的内边距、外边距以及边框会被应用且会把其他处于 inline 状态的盒子推开。</li>
</ol>
<p>用做链接的 <a> 元素、 <span>、 <em> 以及 <strong> 都是默认处于 inline 状态的。</p>
<p>我们通过对盒子 display 属性的设置，比如 inline 或者 block ，来控制盒子的外部显示类型。</p>
<h1 data-id="heading-3">内部和外部显示类型</h1>
<h2 data-id="heading-4">外部显示类型</h2>
<p>CSS 的盒子模型有一个外部显示类型，来决定盒子是块级还是内联。</p>
<h2 data-id="heading-5">内部显示类型</h2>
<p>盒子包模型还有内部显示类型，来决定盒子内部元素如何布局。默认按照正常文档流布局，也就是上面说的那样。</p>
<p>但是，也可以使用 flex 的 display 属性来更改内部显示类型。比如设置一个外部显示类型为 block 的元素 display:flex，那么它的内部显示类型就是 flex，该盒子内的所有直接子元素成为 flex 元素，按照弹性盒子规则布局。</p>
<h1 data-id="heading-6">CSS 盒模型</h1>
<p>完整的盒模型应用于块级盒子，内联盒子只能使用部分内容。</p>
<p>盒模型定义了四个属性：margin、border、padding、content。</p>
<ul>
<li>margin：盒子和其他元素的空白区域。通过 margin 相关属性设置。</li>
<li>border：盒边框。通过 border 相关属性设置。</li>
<li>padding：在盒子内但在内容区域外的空白区域。通过 padding 相关属性设置。</li>
<li>content：内容区域。通过 width、height 设置。</li>
</ul>
<h2 data-id="heading-7">标准盒模型</h2>
<p>在标准盒模型中，设置的 width 和 height 作用于 content。再加上 padding、border 一起决定整个盒子的大小。</p>
<blockquote>
<p>margin 不计入实际大小。它影响的是盒子外部的空间。盒子的范围到边框为止。</p>
</blockquote>
<h2 data-id="heading-8">替代（IE）盒模型</h2>
<p>浏览器默认使用标准盒模型。</p>
<p>如果需要使用替代盒模型，需设置 box-sizing: border-box。</p>
<p>替代盒模型的长宽等于 content+padding+border，所以 content=width/height - padding - border。</p>
<p>如果想要全部使用替代盒模型，可以设置：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">html</span> &#123;
  <span class="hljs-attribute">box-sizing</span>: border-box;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">margin</h2>
<p>外边距会把其他元素从盒子身边推开。外边距也可以设置为负值，这会导致和其他内容重叠。无论是标准还是替代盒模型，外边距总是在计算可见部分后添加。
margin 属性有：</p>
<ul>
<li>margin</li>
<li>margin-top</li>
<li>margin-bottom</li>
<li>margin-right</li>
<li>margin-left</li>
</ul>
<h3 data-id="heading-10">外边距折叠</h3>
<p>两个外边距相接的元素，更大的设置会被保留，小的则消失。并不是两个外边距的总和。</p>
<h2 data-id="heading-11">边框</h2>
<p>如果使用标准盒模型，添加边框将增加整个宽高。</p>
<p>如果使用替代盒模型，添加边框将减少 content。</p>
<p>border 的属性有：</p>
<ul>
<li>border</li>
</ul>
<p>设置宽度、颜色、样式</p>
<ul>
<li>border-top</li>
<li>border-bottom</li>
<li>border-right</li>
<li>border-left</li>
</ul>
<p>设置所有边的宽度、颜色、样式</p>
<ul>
<li>border-width</li>
<li>border-style</li>
<li>border-color</li>
</ul>
<p>设置某条边的宽度、颜色、样式可以用特定的</p>
<ul>
<li>border-top-witdh</li>
<li>border-top-style</li>
<li>border-top-color</li>
<li>border-right-witdh</li>
<li>border-right-style</li>
<li>border-right-color</li>
<li>border-bottom-witdh</li>
<li>border-bottom-style</li>
<li>border-bottom-color</li>
<li>border-left-witdh</li>
<li>border-left-style</li>
<li>border-left-color</li>
</ul>
<h2 data-id="heading-12">内边距</h2>
<p>内外距不能为负，必须是0或正值。</p>
<p>padding属性有：</p>
<ul>
<li>padding</li>
<li>padding-top</li>
<li>padding-bottom</li>
<li>padding-right</li>
<li>padding-left</li>
</ul>
<h2 data-id="heading-13">display:inline-block</h2>
<p>元素可以不换到新行，但又可以设定宽度和高度。</p>
<h1 data-id="heading-14">参考</h1>
<p>MDN：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FLearn%2FCSS%2FBuilding_blocks%2FThe_box_model" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/The_box_model" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p></div>  
</div>
            