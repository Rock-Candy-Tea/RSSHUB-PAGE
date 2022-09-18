
---
title: '一个css属性就能这么强？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99ca7b640f2c4ee2979d5d8bf49250ae~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sun, 18 Sep 2022 01:38:35 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99ca7b640f2c4ee2979d5d8bf49250ae~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>在前端开发领域，css的地位举足轻重，在很多场景下，不管是动画效果还是交互的实现，很多开发者第一时间就是想到的通过<strong>JavaScript</strong>来实现，但是其实很多场景下<strong>css</strong>也可以完成非常多有意思的交互，css的属性非常之多，想要去记住相对很困难，但是有的特别的属性，一个属性就可以完成很多意想不到的效果，我们先来看看我们今天实现的效果。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99ca7b640f2c4ee2979d5d8bf49250ae~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="loading.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4532ceffaad84972abae2a48bc6596ca~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="huoyazi.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>让你实现这样的一个效果你会想到什么呢，第一想法是css不好实现，使用<strong>JavaScript</strong>来实现么，或者是使用<strong>canvas</strong>来绘制么，很显然，这样的作法都过于复杂了，不是我们希望的样子，来看看<strong>css</strong>是如何实现的。</p>
<h3 data-id="heading-0">分析实现</h3>
<p>首先我们想象一下这个东西如何对它分层，上层的文字就是一个简单的文字没什么特殊，但是文字有一个背景色是火焰的效果，并且还会动。</p>
<p>那么我们首先可以想到，如果文字可以是透明色，后面的背景自然就出来了，并且背景如果是一个<strong>gif</strong>图片或者<strong>video</strong>视频让他们动起来就可以实现这个效果了，似乎非常简单，但是我们如何可以让css实现这个效果呢，我们需要用到这个属性：</p>
<h3 data-id="heading-1">mix-blend-mode</h3>
<p><strong>mix</strong>和<strong>blend</strong>翻译过来都是混合的意思，这个特效的属性值也特别多，从字面意思来理解就是混合模式，这个模式我们日常最常见的就是<strong>photoshop</strong>，通过混合可以实现非常多的效果，先来给大家看看这个属性对应了多少种的属性吧：</p>
<pre><code class="hljs language-scss copyable" lang="scss">   &#123;
  <span class="hljs-attribute">mix-blend-mode</span>: normal;         <span class="hljs-comment">// 正常</span>
  <span class="hljs-attribute">mix-blend-mode</span>: multiply;       <span class="hljs-comment">// 正片叠底</span>
  <span class="hljs-attribute">mix-blend-mode</span>: screen;         <span class="hljs-comment">// 滤色</span>
  <span class="hljs-attribute">mix-blend-mode</span>: overlay;        <span class="hljs-comment">// 叠加</span>
  <span class="hljs-attribute">mix-blend-mode</span>: darken;         <span class="hljs-comment">// 变暗</span>
  <span class="hljs-attribute">mix-blend-mode</span>: lighten;        <span class="hljs-comment">// 变亮</span>
  <span class="hljs-attribute">mix-blend-mode</span>: color-dodge;    <span class="hljs-comment">// 颜色减淡</span>
  <span class="hljs-attribute">mix-blend-mode</span>: color-burn;     <span class="hljs-comment">// 颜色加深</span>
  <span class="hljs-attribute">mix-blend-mode</span>: hard-light;     <span class="hljs-comment">// 强光</span>
  <span class="hljs-attribute">mix-blend-mode</span>: soft-light;     <span class="hljs-comment">// 柔光</span>
  <span class="hljs-attribute">mix-blend-mode</span>: difference;     <span class="hljs-comment">// 差值</span>
  <span class="hljs-attribute">mix-blend-mode</span>: exclusion;      <span class="hljs-comment">// 排除</span>
  <span class="hljs-attribute">mix-blend-mode</span>: hue;            <span class="hljs-comment">// 色相</span>
  <span class="hljs-attribute">mix-blend-mode</span>: saturation;     <span class="hljs-comment">// 饱和度</span>
  <span class="hljs-attribute">mix-blend-mode</span>: color;          <span class="hljs-comment">// 颜色</span>
  <span class="hljs-attribute">mix-blend-mode</span>: luminosity;     <span class="hljs-comment">// 亮度</span>

  <span class="hljs-attribute">mix-blend-mode</span>: initial;
  <span class="hljs-attribute">mix-blend-mode</span>: inherit;
  <span class="hljs-attribute">mix-blend-mode</span>: unset;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除去 <code>initial</code> 默认、<code>inherit</code> 继承 和 <code>unset</code> 还原这 3 个所有 CSS 属性都可以取的值外，还有另外的 16 个具体的取值，对应不同的混合效果。</p>
<p>这个属性个人感觉非常复杂，实验了一些属性感觉日常中应该也会很低频的使用到，这次我们就用<strong>mix-blend-mode: screen</strong>来完成上图的例子吧：</p>
<h3 data-id="heading-2">喷火的文字</h3>
<p>实现这个呢我们只需要两层，一层放置我们的火焰背景，这个背景图不一定是火焰也可以是其他的自己可以随便替换，上面这一层再去显示我们的文字，再让两者进行混合即可实现：</p>
<h3 data-id="heading-3">Loading加载</h3>
<p>这里其实看图就知道无非是三个<strong>div</strong>在沿着一个方向旋转，同时让三个方向的动画 有一定时间的延迟，但是呢我们如何没有这个属性不然其混合，最上面的这层肯定就是最后一层div呢，就只有三种颜色很不协调，一旦我们用了这个属性之后，就会通过混合让中间的交叉部分混合出第四种颜色，一下就感觉好看多了，但是这里还有一个点需要注意的是不同颜色混合出来的最终颜色是不同的，如果需要自己指定颜色则其他三个色也是需要在一定区间之内才可以完成的,这里就涉及到了差值算法就比较复杂了。</p>
<h3 data-id="heading-4">在线体验</h3>
<p>下面是完整的体验地址，实现都特别简单，重要的是学习这样一个属性，让我们发动脑洞去思考是否可以去尝试更多玩法</p>
<p><span href="https://code.juejin.cn/pen/7144313000277573646" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7144313000277573646" data-src="https://code.juejin.cn/pen/7144313000277573646" style="display: none" loading="lazy"></iframe></span></p></div>  
</div>
            