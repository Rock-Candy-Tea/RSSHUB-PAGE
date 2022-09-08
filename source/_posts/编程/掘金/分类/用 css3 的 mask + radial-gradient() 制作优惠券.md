
---
title: '用 css3 的 mask + radial-gradient() 制作优惠券'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d88ffdabc33b43e2bd3742811f83fbd1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Tue, 06 Sep 2022 19:36:17 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d88ffdabc33b43e2bd3742811f83fbd1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>。</p>
<h1 data-id="heading-0">概览</h1>
<p>最近项目做到优惠券模块，发现 UI 效果图如下：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d88ffdabc33b43e2bd3742811f83fbd1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
之前我前端实现上图这种内凹的圆，都是用 <code>:before</code> 或 <code>:after</code> 伪元素选择器弄 2 个圆，背景色设置成红色，通过绝对定位实现的。但这次不行，因为如果你仔细看会发现优惠券的红色背景，从左往右是有渐变效果的，所以如果还是弄两个红色的圆放上去就会“穿帮”。通过查询资料，我最终使用 css3 的 2 个属性：<code>mask</code> 和 <code>radial-gradient()</code>  实现。先把完整代码放前面，如果急着下班只是想简单 cv 可以直接拿走不谢：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 例 1.1 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"coupon-wrap"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"coupon-wrap_inner"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 例 1.2 */</span>
<span class="hljs-selector-class">.coupon-wrap</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">690px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">30px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(-<span class="hljs-number">87deg</span>, <span class="hljs-number">#ff3939</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#ff6b5e</span> <span class="hljs-number">100%</span>);
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">6px</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.coupon-wrap_inner</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#ffffff</span>;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">6px</span>;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">140px</span> -<span class="hljs-number">6%</span>, <span class="hljs-number">#0000</span> <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span> <span class="hljs-number">0</span>),
    <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">140px</span> <span class="hljs-number">106%</span>, <span class="hljs-number">#0000</span> <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span> <span class="hljs-number">0</span>);
  -webkit-<span class="hljs-attribute">mask-size</span>: <span class="hljs-number">100%</span> <span class="hljs-number">51%</span>;
  -webkit-<span class="hljs-attribute">mask-position</span>: top, bottom;
  -webkit-<span class="hljs-attribute">mask-repeat</span>: no-repeat;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果如下图：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74ee22550da84ce693cc917b083cdf12~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1656229688348-b55e8c43-aa71-4a19-8c9e-d2a423eb25ee.png" loading="lazy" referrerpolicy="no-referrer">
接下来详细说说实现原理。</p>
<h1 data-id="heading-1">mask（遮罩）</h1>
<p>对 css3 中 <code>mask</code> 属性的学习可以多注意和 <code>background</code> 属性进行对比，它们有很多相似之处，下面我们来分别看看几个 <code>mask</code> 属性，并准备一个蓝色的矩形用于测试：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#1e80ff</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">mask-image</h2>
<p>用于设置元素的遮罩图像，值可以是 1 个或多个 <code><image></code>，也就是 png、gif 或 svg 格式的图像，也包括接下去做优惠券会用到的 <code><radial-gradient()></code> 等。如果是多个值只需用 <code>,</code> 分开即可。如下面的例子中用的就是我从掘金官网下载的 logo 图，是一个 svg 图片：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 例 2.1 */</span>
<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-comment">/* ... */</span>
  -webkit-<span class="hljs-attribute">mask-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'./img/logo.svg'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请注意，mask 属性目前还未标准化，所以相关属性在 chrome 浏览器中需要添加 -webkit- 前缀才会生效。其浏览器兼容性可见下图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdfddd9ee20e497ea48b32fa6fabdb93~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1656339265590-96b9ce65-7939-478f-be85-b70c40f7e43a.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>添加完 <code>mask-image</code>属性后效果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05d076e42c6a4b5ba953101b3cda2b38~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
可以看到原本的蓝色矩形现在只剩下了 logo 区域显示了出来，也就是说作为 mask-image 的图片不透明的地方，可以透过去看到被遮罩的图片，而透明的部分反而会隐藏住被遮罩的图片，其实就是 PS 里的蒙版效果。</p>
<p>logo 默认是 x、 y 轴方向进行了重复平铺。如果我们只想显示 1 个 logo 呢？那就需要用到下面的这个 <code>mask-repeat</code> 属性：</p>
<h2 data-id="heading-3">mask-repeat</h2>
<p>设置遮罩的重复模式，和 <code>background-repeat</code>很像，可以接收的值有 <code>repeat-x</code> 或 <code>repeat-y</code> 或是 1 ~ 2 个的 <code>repeat | space | round | no-repeat</code>，代表 x 轴和 y 轴方向 。如果我们不想让 logo 自动重复，可以添加设置 <code>mask-repeat</code> 为 <code>no-repeat</code>：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 例 2.2 */</span>
<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-comment">/* ... */</span>
  -webkit-<span class="hljs-attribute">mask-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'./img/logo.svg'</span>);
  -webkit-<span class="hljs-attribute">mask-repeat</span>: no-repeat;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在效果如下，为了方便看清 logo 在原本矩形中的相对位置，我把鼠标放在了 <code><div class="box"></div></code> 上进行元素审查：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a19b76ad7bd4728b7af6699356fb8d3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1656234940777-46069777-4db4-46dc-9cf4-9634d4e12c91.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到现在就只有 1 个 logo 了，如果我们想让 logo 居中显示，则可以设置 <code>mask-position</code> 属性：</p>
<h2 data-id="heading-4">mask-position</h2>
<p>设置遮罩的位置模式，同 <code>background-position</code> 一样可以接收 2 个值，分别作用于 x 轴和 y 轴。值可以是 <code>center | left | top | right | bottom </code>这种关键字，也可以是百分比 <code><percentage></code> 或长度 <code><length></code>，比如 <code>50%</code>  或 <code>200px</code>。  想让 logo 居中只需添加 <code>mask-position</code> 属性为 <code>center</code>：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 例 2.3 */</span>
<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-comment">/* ... */</span>
  -webkit-<span class="hljs-attribute">mask-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'./img/logo.svg'</span>);
  -webkit-<span class="hljs-attribute">mask-repeat</span>: no-repeat;
  -webkit-<span class="hljs-attribute">mask-position</span>: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在 logo 就移动到矩形中间位置了：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcdf8da829f842c7a902307f1e366d57~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1656236188124-57c29413-5b6f-4c0d-b33b-b7d034d4447b.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">mask-size</h2>
<p>我们可以通过 <code>mask-size</code> 来设置遮罩，也就是 logo 的大小，其值可以是百分比 <code><percentage></code> ，或类似 <code>100px</code> 这样的长度 <code><length></code> 值，也可以是 <code>cover | contain</code> 这种关键词，同样可以结合 <code>background-size</code> 进行理解。如果我们想让 logo 的大小完全占据整个矩形，可以让 <code>mask-size</code> 的值为 <code>100%</code></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 例 2.4 */</span>
<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-comment">/* ... */</span>
  -webkit-<span class="hljs-attribute">mask-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'./img/logo.svg'</span>);
  -webkit-<span class="hljs-attribute">mask-repeat</span>: no-repeat;
  -webkit-<span class="hljs-attribute">mask-position</span>: center;
  -webkit-<span class="hljs-attribute">mask-size</span>: <span class="hljs-number">100%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4b5edb1559741a8889c69643dc1625e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1656236950601-a141330e-097a-4f42-a470-743f7378d099.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">合并简写</h2>
<p>就像 <code>background</code> 那样， <code>mask</code> 也可以多个属性结合在一起简写，比如例 2.4 就可以简写成：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 例 2.5 */</span>
<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-comment">/* ... */</span>
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'./img/logo.svg'</span>) center/<span class="hljs-number">100%</span> no-repeat;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>mask</code> 后第 1 个值为 <code>mask-image</code> 的值，第 2 个值为设置 <code>mask-position</code>，在后面添加 <code>/</code> 代表设置 <code>mask-size</code>，第 3 个值为设置 <code>mask-repeat</code>。 其实 mask 还有其它一些属性，比如 <code>mask-mode</code>、<code>mask-composite</code> 等，但是制作优惠券用不上，就不多做介绍了。</p>
<h1 data-id="heading-7">radial-gradient()</h1>
<p>了解完 <code>mask</code> 属性，我们再来看看优惠券的需求，就是要想办法弄出上下两张各自有个部分椭圆形为透明的矩形对白色矩形进行遮罩，而这种图片使用  css3  做径向渐变的 <code>radial-gradient()</code> 函数可以直接实现，而且前面我们也说到， <code>mask-image</code> 的值可以是 <code><radial-gradient()></code>：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a6d4785e29949b8aff5d7005d5940de~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<code>radial-gradient()</code> CSS 函数创建的是一个径向渐变图像，得到的是一个 CSS <code><gradient></code> 数据类型的对象，是 <code><image></code> 的一种。所谓径向，就是从“一个点”向四周的渐变，既然是渐变，那么至少需要定义 2 种颜色节点。语法如下：</p>
<pre><code class="hljs language-css copyable" lang="css">radial-gradient(<shape> <size> at <<span class="hljs-attribute">position</span>> ,  <<span class="hljs-attribute">color</span>-stop-list>, ...,  <<span class="hljs-attribute">color</span>-stop-list>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面对各个参数值做个解释：</p>
<h2 data-id="heading-8">参数值</h2>
<h3 data-id="heading-9">shape</h3>
<p>定义渐变的形状，默认是椭圆（<code>ellipse</code>），也可以指定为圆（<code>circle</code>）;</p>
<h3 data-id="heading-10">size</h3>
<p>设置渐变的半径大小，值可以是</p>
<ul>
<li><code>closest-side</code>：半径为从圆心到最<strong>近</strong>的<strong>边</strong>；</li>
<li><code>closest-corner</code>：半径为从圆心到最<strong>近</strong>的<strong>角</strong>；</li>
<li><code>farthest-side</code>：半径为从圆心到最<strong>远</strong>的<strong>边</strong>；</li>
<li><code>farthest-corner</code>：半径为从圆心到最<strong>远</strong>的<strong>角</strong>。</li>
</ul>
<h3 data-id="heading-11">position</h3>
<p>定义渐变的圆心，默认是 <code>center center</code>，和 <code>mask-position</code> 一样也可以是 <code>left | top | right | bottom</code> 这种关键字，或是百分比 <code><percentage></code> 或长度 <code><length></code>。</p>
<h3 data-id="heading-12">color-stop-list</h3>
<p>用于指定渐变的起止颜色，<code><color-stop-list></code> 表示多个 <code><color-stop></code> 的集合，而 <code><color-stop></code> 表示颜色断点。比如  <code>background-image: linear-gradient(red 10%, yellow 60%)</code> 中的 <code>red 10%</code> 和 <code>yellow 60%</code> 就属于 <code><color-stop></code>。</p>
<h2 data-id="heading-13">示例</h2>
<p>我们还是准备一个类名为 <code>box</code> 的矩形 div：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 例 3.1 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加样式如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 例 3.2 */</span>
<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">radial-gradient</span>(red, yellow);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例 3.2 中第 5 行 <code>radial-gradient()</code> 的参数只写了 2 个颜色，意味着其它参数都为默认值，所以效果如下图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88b68b8afca940ef853a0d0f34fb76e7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1656339804306-d5325647-c488-4b6b-8992-f3fde8082c5a.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到默认情况下是一个颜色均匀渐变的椭圆。注意，容器的宽高我故意设置成不一样的，让它是一个长方形而不是正方形，才能看出默认条件下的 <code><shape></code> 为椭圆。</p>
<p>如果我们给颜色添加上位置信息，让红色为 30%，黄色为 60%：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 例 3.3 */</span>
<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-comment">/* ... */</span>
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">radial-gradient</span>(red <span class="hljs-number">30%</span>, yellow <span class="hljs-number">60%</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下，可以看到从 0%（表示虚拟渐变射线的起点） 到 30% 是纯红色，从 30% 到 60% 是红黄渐变，60% 到 100%（表示虚拟渐变线与渐变容器相交的位置） 是纯黄色：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c469453ccaa748d28d7d1d01cdea049c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1656419866037-a28c2b53-4917-46a2-bc84-21e7d4cbbe20.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>例 3.2 相当于是 <code>background-image: radial-gradient(red 0%, yellow 100%);</code></p>
<p>我们再来试试设置默认形状为圆并且改变 <code><position></code> 的效果，让渐变的起始点的 x 轴坐标为 20%，y 轴坐标为 0：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 例 3.4 */</span>
<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-comment">/* ... */</span>
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">20%</span> <span class="hljs-number">0</span>, red <span class="hljs-number">30%</span>, yellow <span class="hljs-number">60%</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在的效果如下图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b864ef10ea7e48f9adac66f372f1f426~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1656420983751-3e0678fc-3892-40be-9eec-4d7fda1a9656.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>想要最终变为我们制作优惠券想要的效果，上图红色的圆需要变小，然后透明度变为 0。可以使用 <code>rgba(255, 0, 0, 0)</code> 来表示纯红透明的颜色，其实既然是透明的，颜色也就无所谓了，可以改成 <code>rgba(0, 0, 0, 0)</code>，再少打几个字可以直接写成 <code>#0000</code>（注意，css 十六进制颜色设置，透明度设置在色值后位，比如 <code>#00000010</code>，从 00 ~ FF，一共 256 个梯度），至于大小可以由 20% 改为 20px；为了效果更明显，黄色也可以改为黑色：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 例 3.5 */</span>
<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-comment">/* ... */</span>
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">radial-gradient</span>(
    circle at <span class="hljs-number">20%</span> <span class="hljs-number">0</span>,
    <span class="hljs-number">#0000</span> <span class="hljs-number">20px</span>,
    <span class="hljs-number">#000</span> <span class="hljs-number">60%</span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c55cc990cff420398fe2f9eedad3da7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1656421503880-5e1e2006-7e2d-437f-8f37-596bbe7705fb.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>作为 mask-image 的图片只有完全透明的部分才会完全挡住被遮罩的图层，所以我们需要将上图中 20% ~ 60% 这半透明的区域变为完全不透明的。实现的方法就是让黑色的位置小于透明的位置，比如 10px，为了简单直接设置为 0：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 例 3.6 */</span>
<span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-comment">/* ... */</span>
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">radial-gradient</span>(
    circle at <span class="hljs-number">20%</span> <span class="hljs-number">0</span>,
    <span class="hljs-number">#0000</span> <span class="hljs-number">20px</span>,
    <span class="hljs-number">#000</span> <span class="hljs-number">0</span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在就基本实现了我们想要的效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e203e54427d458db551abbb8142e2cf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1656422296103-72fd702e-5857-41ef-9bb7-91b5876baf99.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">总结</h1>
<p>回头去看例 1.2 中我们实现优惠券的代码，其实就是用 <code>radial-gradient()</code> 生成了上下 2 张类似例 3.6 的 <code><image></code>，作为 <code>mask-image</code> 的值，对优惠券里面那个白色矩形做了遮罩而已。</p>
<p>需要注意的有 2 点：</p>
<ol>
<li><code>mask</code> 的第一个值也就是 <code>mask-image</code> 我们设置了 2 个，上下各一个，所以 <code>mask-position</code> 的值也是 2 个，用 <code>,</code> 隔开；</li>
<li><code>mask-size</code>中第 2 值（height）设置为 51%，是为了确保上下 2 张遮罩层的图像之间不会留有缝隙导致“穿帮”。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d160e26986d1447e8ef2dfe783fc6eb6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="感谢.gif" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a7fbbcaca1c480c942b7735a7228e9f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="点赞.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            