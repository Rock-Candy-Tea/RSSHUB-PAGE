
---
title: '小程序实现TabBar创意动画(文末附完整源代码)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abcf4006f0504658bea3964917306a83~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 01:53:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abcf4006f0504658bea3964917306a83~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">小程序实现<strong>TabBar</strong>创意动画(文末附完整源代码)</h1>
<blockquote>
<p>小程序日益增多的情况下，UI风格显得越来越重要，在页面中如果能让<code>TabBar</code>个性化一点，加一些小交互，用户体验会大大提升。由于小程序对<code>svg</code>不太友好，所以我们尽量使用<code>css</code>动画进行实现。之前文章<a href="https://juejin.cn/post/6953831336079523870" target="_blank">小程序开发技巧</a>中提到过<code>TabBar</code>自定义方案，感兴趣的可以了解一下。下面就分享一下今天写的几个交互效果，文末也会分享源代码。记得点赞+关注+收藏！</p>
</blockquote>
<h2 data-id="heading-1">NO.1</h2>
<blockquote>
<p>这种效果主要使用了<code>transform</code>和<code>opacity</code>来实现。文字默认隐藏并缩小，点击后<code>icon</code>图标<code>transform</code>的<code>y轴</code>方向上移，同时控制文字的<code>opacity</code>。圆形块根据点击的<code>index</code>去动态计算<code>x轴</code>的偏移位置即可。</p>
</blockquote>
<p><a href="https://imgtu.com/i/gRsjhj" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abcf4006f0504658bea3964917306a83~tplv-k3u1fbpfcp-zoom-1.image" alt="gRsjhj.gif" loading="lazy" referrerpolicy="no-referrer"></a></p>
<ul>
<li>核心css代码(完整代码见文末)：</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css">    <span class="hljs-selector-class">.tabbar</span> <span class="hljs-selector-class">.item</span> <span class="hljs-selector-class">.text</span>&#123;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">10</span>rpx;
        <span class="hljs-attribute">text-align</span>: center;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">22</span>rpx;
        <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">transition</span>: all .<span class="hljs-number">8s</span>;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0.8</span>);
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    &#125;
    <span class="hljs-selector-class">.tabbar</span> <span class="hljs-selector-class">.item</span><span class="hljs-selector-class">.active</span> <span class="hljs-selector-class">.text</span>&#123;
        <span class="hljs-attribute">opacity</span>: <span class="hljs-number">1</span>;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1</span>);
    &#125;

    <span class="hljs-selector-class">.tabbar</span> <span class="hljs-selector-class">.item</span><span class="hljs-selector-class">.active</span> <span class="hljs-selector-class">.icon</span>&#123;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#3561f5</span>;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(-<span class="hljs-number">55</span>rpx);
    &#125;

    <span class="hljs-selector-class">.tabbar</span> <span class="hljs-selector-class">.item</span> <span class="hljs-selector-class">.icon</span>&#123;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">50</span>rpx<span class="hljs-meta">!important</span>;
        <span class="hljs-attribute">text-align</span>: center;
        <span class="hljs-attribute">transition</span>: all .<span class="hljs-number">8s</span>;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">NO.2</h2>
<blockquote>
<p>这个效果用到一个css动画工具库：<a href="http://bouncejs.com/" target="_blank" rel="nofollow noopener noreferrer">bouncejs</a>，它可以在线生成css动画，然后复制到项目中使用即可。下方效果采用跳跃式切换，整体看上去非常有活力。使用了<code>animation</code>动画。由于css动画代码过多，想看完整代码见文末<code>github</code>地址。</p>
</blockquote>
<p><a href="https://imgtu.com/i/gR2KRH" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cf6107723274cac9cf73b830f9277c3~tplv-k3u1fbpfcp-zoom-1.image" alt="gR2KRH.gif" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h2 data-id="heading-3">NO.3</h2>
<blockquote>
<p>下方这个效果还是用<a href="http://bouncejs.com/" target="_blank" rel="nofollow noopener noreferrer">bouncejs</a>在线编辑，编辑完成后只需要点击后给相应的元素添加类名即可。</p>
</blockquote>
<p><a href="https://imgtu.com/i/gRRn00" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e90838016d4e427fbcd7ea0887a04d1d~tplv-k3u1fbpfcp-zoom-1.image" alt="gRRn00.gif" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h2 data-id="heading-4">结尾</h2>
<blockquote>
<p>如需源代码可以移步<a href="https://github.com/LonJinUp/wxTabBar.git" target="_blank" rel="nofollow noopener noreferrer">github</a>。  👉<a href="https://juejin.cn/column/6961059476208091149" target="_blank">关注前端365</a>：分享前端小技巧以及开发过程中的一些问题，欢迎关注+收藏+点赞，感谢支持～</p>
</blockquote></div>  
</div>
            