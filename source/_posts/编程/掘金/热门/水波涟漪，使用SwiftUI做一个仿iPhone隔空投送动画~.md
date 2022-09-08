
---
title: '水波涟漪，使用SwiftUI做一个仿iPhone隔空投送动画~'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36b8a64f70d446be8da7c2e959e4aef6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 25 Aug 2022 04:38:21 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36b8a64f70d446be8da7c2e959e4aef6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>携手创作，共同成长！这是我参与「掘金日新计划 · 8 月更文挑战」的第28天，<a href="https://juejin.cn/post/7123120819437322247" title="https://juejin.cn/post/7123120819437322247" target="_blank">点击查看活动详情</a>。</p>
<h2 data-id="heading-0">项目背景</h2>
<p>使用<code>iPhone</code>以来，最好用的莫过于<strong>隔空投送</strong>了，只要在<strong>同一个局域网</strong>下，公司里使用iPhone的童鞋都可以互相快速的分享照片、文件。</p>
<p>而且iPhone接收到的文件，也能快速地投送到MacBook中，也能分享给iPad……</p>
<p>享受功能服务的我发现iPhone隔空投送动画挺好意思，有点像“水波涟漪”的效果，就想着使用<code>SwiftUI</code>做一个仿iPhone隔空投送动画。</p>
<p>说干就干。</p>
<h2 data-id="heading-1">项目搭建</h2>
<p>首先，创建一个新的<code>SwiftUI</code>项目，命名为<code>SwiftUIAirDrop</code>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36b8a64f70d446be8da7c2e959e4aef6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">逻辑分析</h2>
<p>隔空投送的动画元素比较简单，我们可以看到是由一个<code>Image</code>图标和一圈圈“<code>水波</code>”组成，然后“<code>水波</code>”一圈一圈出现又消失，形成一种“<code>涟漪</code>”效果。</p>
<p>那么样式部分，我们就可以先完成中心的<code>Image</code>图标，再加上一圈圈的圆。交互部分，我们可以让圆出现后消失，模拟水波效果。</p>
<h2 data-id="heading-3">样式部分</h2>
<p>首先是中间的隔空投送的图标，我们使用<code>Image</code>完成基本的样式，示例：</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-built_in">Image</span>(systemName: "antenna.radiowaves.left.and.right.circle.fill")
    <span class="hljs-selector-class">.resizable</span>()
    <span class="hljs-selector-class">.aspectRatio</span>(contentMode: .fill)
    <span class="hljs-selector-class">.frame</span>(width: <span class="hljs-number">60</span>, height: <span class="hljs-number">60</span>)
    <span class="hljs-selector-class">.foregroundColor</span>(.blue)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e5f0bcc2cc542c68ae7418da3699bce~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>水波涟漪我们可以看作一圈圈的圆，而且这些圆是叠加的层级进行排布，示例：</p>
<pre><code class="hljs language-scss copyable" lang="scss">ZStack &#123;
    <span class="hljs-built_in">Image</span>(systemName: "antenna.radiowaves.left.and.right.circle.fill")
        <span class="hljs-selector-class">.resizable</span>()
        <span class="hljs-selector-class">.aspectRatio</span>(contentMode: .fill)
        <span class="hljs-selector-class">.frame</span>(width: <span class="hljs-number">60</span>, height: <span class="hljs-number">60</span>)
        <span class="hljs-selector-class">.foregroundColor</span>(.blue)

    Circle()
        <span class="hljs-selector-class">.stroke</span>()
        <span class="hljs-selector-class">.frame</span>(width: <span class="hljs-number">340</span>, height: <span class="hljs-number">340</span>)
        <span class="hljs-selector-class">.foregroundColor</span>(.blue)

    Circle()
        <span class="hljs-selector-class">.stroke</span>()
        <span class="hljs-selector-class">.frame</span>(width: <span class="hljs-number">240</span>, height: <span class="hljs-number">240</span>)
        <span class="hljs-selector-class">.foregroundColor</span>(.blue)

    Circle()
        <span class="hljs-selector-class">.stroke</span>()
        <span class="hljs-selector-class">.frame</span>(width: <span class="hljs-number">150</span>, height: <span class="hljs-number">150</span>)
        <span class="hljs-selector-class">.foregroundColor</span>(.blue)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基础样式完成得差不多了，我们来加一点交互效果，水波涟漪的效果是<strong>从里向外展开</strong>，且<strong>由内向外逐渐消失</strong>。</p>
<p>我们可以声明一个<code>动画变量</code>进行控制，示例：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@State</span> <span class="hljs-keyword">private</span> <span class="hljs-type">var</span> <span class="hljs-variable">animateCircle</span> <span class="hljs-operator">=</span> <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们给圆加上<code>缩放</code>和<code>显隐</code>的修饰符，示例：</p>
<pre><code class="hljs language-scss copyable" lang="scss">ZStack &#123;
    <span class="hljs-built_in">Image</span>(systemName: "antenna.radiowaves.left.and.right.circle.fill")
        <span class="hljs-selector-class">.resizable</span>()
        <span class="hljs-selector-class">.aspectRatio</span>(contentMode: .fill)
        <span class="hljs-selector-class">.frame</span>(width: <span class="hljs-number">60</span>, height: <span class="hljs-number">60</span>)
        <span class="hljs-selector-class">.foregroundColor</span>(.blue)

    Circle()
        <span class="hljs-selector-class">.stroke</span>()
        <span class="hljs-selector-class">.frame</span>(width: <span class="hljs-number">340</span>, height: <span class="hljs-number">340</span>)
        <span class="hljs-selector-class">.foregroundColor</span>(.blue)
        <span class="hljs-selector-class">.scaleEffect</span>(animateCircle ? <span class="hljs-number">1</span> : <span class="hljs-number">0.3</span>)
        <span class="hljs-selector-class">.opacity</span>(animateCircle ? <span class="hljs-number">0</span> : <span class="hljs-number">1</span>)

    Circle()
        <span class="hljs-selector-class">.stroke</span>()
        <span class="hljs-selector-class">.frame</span>(width: <span class="hljs-number">240</span>, height: <span class="hljs-number">240</span>)
        <span class="hljs-selector-class">.foregroundColor</span>(.blue)
        <span class="hljs-selector-class">.scaleEffect</span>(animateCircle ? <span class="hljs-number">1</span> : <span class="hljs-number">0.3</span>)
        <span class="hljs-selector-class">.opacity</span>(animateCircle ? <span class="hljs-number">0</span> : <span class="hljs-number">1</span>)

    Circle()
        <span class="hljs-selector-class">.stroke</span>()
        <span class="hljs-selector-class">.frame</span>(width: <span class="hljs-number">150</span>, height: <span class="hljs-number">150</span>)
        <span class="hljs-selector-class">.foregroundColor</span>(.blue)
        <span class="hljs-selector-class">.scaleEffect</span>(animateCircle ? <span class="hljs-number">1</span> : <span class="hljs-number">0.3</span>)
        <span class="hljs-selector-class">.opacity</span>(animateCircle ? <span class="hljs-number">0</span> : <span class="hljs-number">1</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，在视图加载时，我们调用动画且让动画<code>每3秒循环1次</code>，每次循环切换<code>animateCircle</code>变量状态，示例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">.<span class="hljs-property">onAppear</span> &#123;
    <span class="hljs-title function_">withAnimation</span>(<span class="hljs-params">.easeIn(duration: <span class="hljs-number">3</span>).repeatForever(autoreverses: <span class="hljs-literal">false</span>)</span>)&#123;
        self.<span class="hljs-property">animateCircle</span>.<span class="hljs-title function_">toggle</span>()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">项目预览</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e9620c1cfb84b69aa39678ea105d987~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>恭喜你，完成了本章的全部内容！</p>
<p>快来动手试试吧。</p>
<p><strong>如果本专栏对你有帮助，不妨点赞、评论、关注～</strong></p></div>  
</div>
            