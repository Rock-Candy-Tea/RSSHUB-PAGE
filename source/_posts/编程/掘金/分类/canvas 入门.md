
---
title: 'canvas 入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ac5656e36de4cad8c505d130c515df4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 19:33:19 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ac5656e36de4cad8c505d130c515df4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">canvas 简介</h2>
<p>什么是<code>canvas</code>？简单来说，canvas是h5中提供的一个元素，可以用来在网页上绘制图像或者动画，甚至可以进行实时视频的处理和渲染工作；</p>
<blockquote>
<p>它最初由苹果内部使用自己 MacOS X WebKit 推出，供应用程序使用像仪表盘的构件和 Safari 浏览器使用。后来，有人通过 Gecko 内核的浏览器 (尤其是 Mozilla和Firefox)，Opera 和 Chrome 和超文本网络应用技术工作组建议为下一代的网络技术使用该元素。<br>
Canvas 是由 HTML 代码配合高度和宽度属性而定义出的可绘制区域。JavaScript 代码可以访问该区域，类似于其他通用的二维 API，通过一套完整的绘图函数来动态生成图形。<br>
Mozilla 程序从 Gecko 1.8 (Firefox 1.5) 开始支持 <code><canvas></code>, Internet Explorer 从 IE9 开始 <code><canvas></code> 。Chrome 和 Opera 9+ 也支持 <code><canvas></code>。<br>
引自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fw3cnote%2Fhtml5-canvas-intro.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/w3cnote/html5-canvas-intro.html" ref="nofollow noopener noreferrer">www.runoob.com/w3cnote/htm…</a></p>
</blockquote>
<h2 data-id="heading-1">基本使用</h2>
<h3 data-id="heading-2">新建canvas</h3>
<p>在我们的html中添加如下元素，就可以得到一个新的canvas画布</p>
<pre><code class="hljs language-js copyable" lang="js"><canvas id=<span class="hljs-string">"container"</span> style=<span class="hljs-string">"border:1px solid black;"</span>></canvas>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时并没有给这个元素设置宽高，它的默认width为300px、height为150px
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ac5656e36de4cad8c505d130c515df4~tplv-k3u1fbpfcp-watermark.image" height="200px" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3"><canvas> 元素</h3>
<p><canvas> 只有两个可选的属性：width、heigth 属性。<br>
如果不给 <canvas> 设置 widht、height 属性时，则默认 width为300、height 为 150，单位都是 px。也可以使用 css 属性来设置宽高，但是如宽高属性和初始比例不一致，它会出现扭曲。所以，建议永远不要使用 css 属性来设置 <canvas> 的宽高。</p>
<p><code>>>>什么是canvas的扭曲？</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--index.html--></span>
<span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">canvas</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
      <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid black;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100px"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200px"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">'canvas.js'</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// canvas.js</span>
<span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'canvas'</span>);

<span class="hljs-keyword">const</span> ctx = canvas.getContext(<span class="hljs-string">'2d'</span>);

<span class="hljs-comment">// 绘制一个50*50的矩形</span>
ctx.fillRect(<span class="hljs-number">10</span>,<span class="hljs-number">10</span>,<span class="hljs-number">50</span>,<span class="hljs-number">50</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img height="100px" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d1a271f59af42ea8df365996e59c036~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们执行上面的代码之后，本意是在画布上绘制一个50*50的矩形，但是实际上的效果却显然跟我们预期的不一致，这时候就是canvas发生了扭曲。可以这么理解，画布和形状是先渲染在页面上的，然后由css设置的宽高进行了拉伸，最后出现的就是拉伸后的结果。</p>
<h4 data-id="heading-4">替换内容</h4>
<p>可以看到canvas并没有像img中一样的alt属性，在浏览器不支持canvas时，可以用下面的这种方式来进行文本替换</p>
<pre><code class="hljs language-js copyable" lang="js"><canvas>
    你的浏览器不支持 canvas，请升级你的浏览器。
</canvas>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">canvas 渲染上下文</h3>
<p>从前文中可以看到，canvas在初始化的时候是一片空白的，那么如何进行绘图呢？就是通过canvas提供的上下文进行；
canvas提供了多种渲染上下文</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6c6bbee76b4479f8aff81aede068ebe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<ul>
<li>"2d", 建立一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FCanvasRenderingContext2D" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/CanvasRenderingContext2D" ref="nofollow noopener noreferrer">CanvasRenderingContext2D</a> 二维渲染上下文。</li>
<li>"webgl" (或"experimental-webgl") 将创建一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWebGLRenderingContext" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/WebGLRenderingContext" ref="nofollow noopener noreferrer">WebGLRenderingContext</a> 三维渲染上下文对象。只在支持<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGL_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API" ref="nofollow noopener noreferrer">WebGL</a> 版本1(OpenGL ES 2.0)的浏览器上可用。</li>
<li>"webgl2" (或 "experimental-webgl2") 这将创建一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWebGL2RenderingContext" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/WebGL2RenderingContext" ref="nofollow noopener noreferrer">WebGL2RenderingContext</a> 三维渲染上下文对象。只在支持 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebGL_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API" ref="nofollow noopener noreferrer">WebGL</a> 版本2 (OpenGL ES 3.0)的浏览器上可用。</li>
<li>"bitmaprenderer" 将创建一个只提供将canvas内容替换为指定<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FImageBitmap" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/ImageBitmap" ref="nofollow noopener noreferrer">ImageBitmap</a>功能的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FImageBitmapRenderingContext" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/ImageBitmapRenderingContext" ref="nofollow noopener noreferrer">ImageBitmapRenderingContext</a>  。</li>
</ul>
</blockquote>
<p>这里我们还是专注于<strong>2d</strong>上下文环境（<em>后文简称为ctx</em>），看它可以帮助我们做哪些事情。</p>
<h3 data-id="heading-6">栅格</h3>
<p>在真正开始绘制之前，首先需要了解一下画布栅格（canvas grid）以及坐标空间。<br>
假设我们创建了一个宽150px, 高150px的canvas元素。canvas元素默认被网格所覆盖。通常来说网格中的一个单元相当于canvas元素中的一像素。栅格的起点为左上角（坐标为（0,0））。所有元素的位置都相对于原点定位。所以图中蓝色方形左上角的坐标为距离左边（X轴）x像素，距离上边（Y轴）y像素（坐标为（x,y））。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/655aeca761e14f0d919e8ab64dfc80df~tplv-k3u1fbpfcp-watermark.image" alt="image.png" title="引用自MDN：https://developer.mozilla.org/zh-CN/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">绘制形状</h3>
<p>不同于svg提供的多种默认形状，<canvas>只支持两种形式的图形绘制：矩形和路径（由一系列点连成的线段），各种路径的组合绘制出所有其他类型的图形。canvas中提供了多种绘制路径的方法。</p>
<h4 data-id="heading-8">矩形</h4>
<p>首先看如何绘制矩形
canvast 提供了三种方法绘制矩形：</p>
<blockquote>
<p>1、fillRect(x, y, width, height)：绘制一个填充的矩形;<br>
2、strokeRect(x, y, width, height)：绘制一个矩形的边框;<br>
3、clearRect(x, y, widh, height)：清除指定的矩形区域，然后这块区域会变的完全透明;</p>
</blockquote>
<p><strong>说明</strong>：这 3 个方法具有相同的参数。</p>
<blockquote>
<ul>
<li>x, y：指的是矩形的左上角的坐标。(相对于canvas的坐标原点)</li>
<li>width, height：指的是绘制的矩形的宽和高</li>
</ul>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'canvas'</span>);
<span class="hljs-keyword">const</span> ctx = canvas.getContext(<span class="hljs-string">'2d'</span>);

<span class="hljs-comment">// 绘制一个100*100的矩形，填充黑色</span>
ctx.fillRect(<span class="hljs-number">25</span>, <span class="hljs-number">25</span>, <span class="hljs-number">100</span>, <span class="hljs-number">100</span>);
<span class="hljs-comment">// 清除60*60的矩形区域，背景为透明</span>
ctx.clearRect(<span class="hljs-number">45</span>, <span class="hljs-number">45</span>, <span class="hljs-number">60</span>, <span class="hljs-number">60</span>);
<span class="hljs-comment">// 生成50*50的边框矩形区域</span>
ctx.strokeRect(<span class="hljs-number">50</span>, <span class="hljs-number">50</span>, <span class="hljs-number">50</span>, <span class="hljs-number">50</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6183ddf60c404e29b296f5455fd57ca1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">path 路径</h3>
<p>使用路径绘制图形需要一些额外的步骤：</p>
<ol>
<li>创建路径起始点</li>
<li>调用绘制方法去绘制出路径</li>
<li>把路径封闭</li>
<li>一旦路径生成，通过描边或填充路径区域来渲染图形。</li>
</ol>
<p>下面是canvas提供的方法：</p>
<ol>
<li>
<p>beginPath() -- 新建一条路径，路径一旦创建成功，图形绘制命令被指向到路径上生成路径</p>
</li>
<li>
<p>moveTo(x, y) -- 把画笔移动到指定的坐标(x, y)。相当于设置路径的起始点坐标。</p>
</li>
<li>
<p>closePath() -- 闭合路径之后，图形绘制命令又重新指向到上下文中</p>
</li>
<li>
<p>stroke() -- 通过线条来绘制图形轮廓</p>
</li>
<li>
<p>fill() -- 通过填充路径的内容区域生成实心的图形</p>
</li>
</ol>
<p>接下来开始绘制一些形状和图形</p>
<h4 data-id="heading-10">线段</h4>
<p>首先绘制一条直线</p>
<pre><code class="hljs language-js copyable" lang="js">ctx.beginPath();
ctx.moveTo(<span class="hljs-number">10</span>,<span class="hljs-number">70</span>);
ctx.lineTo(<span class="hljs-number">200</span>,<span class="hljs-number">70</span>);
ctx.stroke();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eff6eb3210614aaebe17ae5ec6b9e268~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
多次调用lineTo，我们可以得到多线段</p>
<pre><code class="hljs language-js copyable" lang="js">ctx.beginPath();
ctx.moveTo(<span class="hljs-number">10</span>,<span class="hljs-number">70</span>);
ctx.lineTo(<span class="hljs-number">40</span>,<span class="hljs-number">70</span>);
ctx.lineTo(<span class="hljs-number">60</span>,<span class="hljs-number">100</span>);
ctx.lineTo(<span class="hljs-number">250</span>,<span class="hljs-number">120</span>);
ctx.stroke();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/265f2dbe7b96414aa94009d8eb9fdba4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">矩形</h4>
<p>尝试使用closePath可以闭合当前形状，这里我们绘制了一个矩形：</p>
<pre><code class="hljs language-js copyable" lang="js">ctx.beginPath();
ctx.moveTo(<span class="hljs-number">10</span>,<span class="hljs-number">10</span>);
ctx.lineTo(<span class="hljs-number">80</span>,<span class="hljs-number">10</span>);
ctx.lineTo(<span class="hljs-number">80</span>,<span class="hljs-number">80</span>);
ctx.lineTo(<span class="hljs-number">10</span>,<span class="hljs-number">80</span>);
ctx.closePath();
ctx.stroke();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6a4d914155e498b88707afe4986a226~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还可以绘制三角形</p>
<pre><code class="hljs language-js copyable" lang="js">ctx.beginPath();
ctx.moveTo(<span class="hljs-number">100</span>,<span class="hljs-number">70</span>);
ctx.lineTo(<span class="hljs-number">200</span>,<span class="hljs-number">70</span>);
ctx.lineTo(<span class="hljs-number">150</span>,<span class="hljs-number">120</span>);
ctx.closePath();
ctx.fill();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f5263cf41164b1ea0ecd991a5fbad9f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">圆形及圆弧</h4>
<p>上面都是使用直线进行绘画，再来看下ctx如何绘制曲线</p>
<pre><code class="hljs language-js copyable" lang="js">ctx.beginPath();
ctx.arc(<span class="hljs-number">75</span>, <span class="hljs-number">75</span>, <span class="hljs-number">50</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">Math</span>.PI * <span class="hljs-number">2</span>, <span class="hljs-literal">true</span>); <span class="hljs-comment">// 绘制</span>
ctx.moveTo(<span class="hljs-number">110</span>, <span class="hljs-number">75</span>);
ctx.arc(<span class="hljs-number">75</span>, <span class="hljs-number">75</span>, <span class="hljs-number">35</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">Math</span>.PI, <span class="hljs-literal">false</span>);   <span class="hljs-comment">// 口(顺时针)</span>
ctx.moveTo(<span class="hljs-number">65</span>, <span class="hljs-number">65</span>);
ctx.arc(<span class="hljs-number">60</span>, <span class="hljs-number">65</span>, <span class="hljs-number">5</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">Math</span>.PI * <span class="hljs-number">2</span>, <span class="hljs-literal">true</span>);  <span class="hljs-comment">// 左眼</span>
ctx.moveTo(<span class="hljs-number">95</span>, <span class="hljs-number">65</span>);
ctx.arc(<span class="hljs-number">90</span>, <span class="hljs-number">65</span>, <span class="hljs-number">5</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">Math</span>.PI * <span class="hljs-number">2</span>, <span class="hljs-literal">false</span>);  <span class="hljs-comment">// 右眼</span>
ctx.stroke();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dbeb9f7a6ec44d38c26c61de0cc04cb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到使用arc方法来绘制了两个圆形，组成了左眼和右眼，并且绘制了一个圆弧。<br>
arc函数如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">void</span> ctx.arc(x, y, r, startAngle, endAngle, anticlockwise)
<span class="hljs-comment">// 以(x, y) 为圆心，以r 为半径，从 startAngle 弧度开始到endAngle弧度结束。</span>
<span class="hljs-comment">// anticlosewise 是布尔值，true 表示逆时针，false 表示顺时针(默认是顺时针)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这里的度数都是弧度。</li>
<li>0 弧度是指的 x 轴正方向。</li>
</ul>
<p>还可以使用arcTo方法进行绘制</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">void</span> ctx.arcTo(x1, y1, x2, y2, radius);
<span class="hljs-comment">/* 使用当前的描点(前一个moveTo或lineTo等函数的止点)。根据当前描点与给定的控制点1连接的直
 线，和控制点1与控制点2连接的直线，作为使用指定半径的圆的切线，画出两条切线之间的弧线路径
 x1,y1为第一个控制点的坐标，x2,y2为第二个控制点坐标，radius为圆弧半径
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c454c8f4ff14c1da3cc830aa1cb39d5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">ctx.beginPath();
ctx.arc(<span class="hljs-number">75</span>, <span class="hljs-number">75</span>, <span class="hljs-number">50</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">Math</span>.PI * <span class="hljs-number">2</span>, <span class="hljs-literal">true</span>); <span class="hljs-comment">// 绘制</span>
ctx.moveTo(<span class="hljs-number">110</span>, <span class="hljs-number">75</span>);
<span class="hljs-comment">// 分别绘制两段圆弧</span>
ctx.arcTo(<span class="hljs-number">110</span>, <span class="hljs-number">110</span>, <span class="hljs-number">65</span>, <span class="hljs-number">110</span>, <span class="hljs-number">35</span>);
ctx.arcTo(<span class="hljs-number">40</span>, <span class="hljs-number">110</span>, <span class="hljs-number">40</span>, <span class="hljs-number">100</span>, <span class="hljs-number">35</span>);
ctx.moveTo(<span class="hljs-number">65</span>, <span class="hljs-number">65</span>);
ctx.arc(<span class="hljs-number">60</span>, <span class="hljs-number">65</span>, <span class="hljs-number">5</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">Math</span>.PI * <span class="hljs-number">2</span>, <span class="hljs-literal">true</span>);  <span class="hljs-comment">// 左眼</span>
ctx.moveTo(<span class="hljs-number">95</span>, <span class="hljs-number">65</span>);
ctx.arc(<span class="hljs-number">90</span>, <span class="hljs-number">65</span>, <span class="hljs-number">5</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">Math</span>.PI * <span class="hljs-number">2</span>, <span class="hljs-literal">false</span>);  <span class="hljs-comment">// 右眼</span>
ctx.stroke();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9109c9a820ef4e819a226493ca908690~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">贝塞尔曲线</h4>
<p><code>quadraticCurveTo(cp1x, cp1y, x, y)  </code><br>
绘制二次贝塞尔曲线，cp1x,cp1y为一个控制点，x,y为结束点。</p>
<p><code>bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y) </code><br>
绘制三次贝塞尔曲线，cp1x,cp1y为控制点一，cp2x,cp2y为控制点二，x,y为结束点。</p>
<p>如果有svg中绘制贝塞尔曲线的经历，这里的参数想必也都很好理解，或者可以根据下图来认识控制点和贝塞尔曲线:</p>
<p>二次贝塞尔曲线</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3063c9080e494f27a531d92dd300c926~tplv-k3u1fbpfcp-watermark.image" alt="b_2_big.gif" title="图来自：https://www.runoob.com/w3cnote/html5-canvas-intro.html" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">ctx.beginPath();
ctx.moveTo(<span class="hljs-number">10</span>, <span class="hljs-number">200</span>); <span class="hljs-comment">//起始点</span>
<span class="hljs-comment">//绘制二次贝塞尔曲线</span>
ctx.quadraticCurveTo(<span class="hljs-number">40</span>, <span class="hljs-number">100</span>, <span class="hljs-number">200</span>, <span class="hljs-number">200</span>);
ctx.stroke();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd9facbc94a046f89d172bfcded76c1e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>三次贝塞尔曲线</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1476955e4961469dba8883da96697914~tplv-k3u1fbpfcp-watermark.image" alt="b_3_big.gif" title="图来自：https://www.runoob.com/w3cnote/html5-canvas-intro.html" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">ctx.beginPath();
ctx.moveTo(<span class="hljs-number">10</span>, <span class="hljs-number">20</span>); <span class="hljs-comment">//起始点</span>
<span class="hljs-comment">//绘制二次贝塞尔曲线</span>
ctx.bezierCurveTo(<span class="hljs-number">20</span>, <span class="hljs-number">100</span>, <span class="hljs-number">100</span>, <span class="hljs-number">50</span>, <span class="hljs-number">200</span>, <span class="hljs-number">130</span>);
ctx.stroke();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/668668320e4a45269c7816f03f53996d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">Path2d 对象 （Experimental）</h3>
<p>path2d是一个实验中的功能</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> rectangle = <span class="hljs-keyword">new</span> Path2D();
rectangle.rect(<span class="hljs-number">10</span>, <span class="hljs-number">10</span>, <span class="hljs-number">50</span>, <span class="hljs-number">50</span>);

<span class="hljs-keyword">const</span> circle = <span class="hljs-keyword">new</span> Path2D();
circle.moveTo(<span class="hljs-number">125</span>, <span class="hljs-number">35</span>);
circle.arc(<span class="hljs-number">100</span>, <span class="hljs-number">35</span>, <span class="hljs-number">25</span>, <span class="hljs-number">0</span>, <span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.PI);

ctx.stroke(rectangle);
ctx.fill(circle);

<span class="hljs-comment">// 使用svg path来初始化路径</span>
<span class="hljs-keyword">const</span> svgPath = <span class="hljs-keyword">new</span> Path2D(<span class="hljs-string">"M150 10 h 80 v 80 h -80 Z"</span>);
ctx.stroke(svgPath);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8dde4151ba94a0386992c7c10add31c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">样式和颜色</h3>
<p>上文中主要介绍了如何绘制不同的形状和路径，但是图案当然还需要一些色彩和样式作为补充。</p>
<h4 data-id="heading-16">颜色</h4>
<p>要给图形增加颜色，可以使用这两个属性：<code>fillStyle</code>和<code>strokeStyle</code>。</p>
<p><strong>fillStyle</strong></p>
<pre><code class="hljs language-js copyable" lang="js">ctx.fillStyle = <span class="hljs-string">'rgb(200,100,200)'</span>;
ctx.fillRect(<span class="hljs-number">30</span>, <span class="hljs-number">30</span>, <span class="hljs-number">100</span>, <span class="hljs-number">100</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e93702647e0d4f4ea57c5efb9e0e2977~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>strokeStyle</strong></p>
<pre><code class="hljs language-js copyable" lang="js">ctx.strokeStyle = <span class="hljs-string">'rgb(200,100,200)'</span>;
ctx.strokeRect(<span class="hljs-number">30</span>, <span class="hljs-number">30</span>, <span class="hljs-number">100</span>, <span class="hljs-number">100</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/426f773b65ee4917a0ab44e57047edf2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">透明度</h4>
<p><code>globalAlpha</code> 这个属性影响到 canvas 里所有图形的透明度，有效的值范围是 0.0 （完全透明）到 1.0（完全不透明），默认是 1.0</p>
<pre><code class="hljs language-js copyable" lang="js">ctx.fillStyle = <span class="hljs-string">'rgb(200,100,200)'</span>;
ctx.globalAlpha = <span class="hljs-number">0.2</span>;
ctx.fillRect(<span class="hljs-number">30</span>, <span class="hljs-number">30</span>, <span class="hljs-number">100</span>, <span class="hljs-number">100</span>);
ctx.globalAlpha = <span class="hljs-number">1</span>;
ctx.fillRect(<span class="hljs-number">150</span>, <span class="hljs-number">30</span>, <span class="hljs-number">100</span>, <span class="hljs-number">100</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/625df8f784174852b0ce3ded66163a02~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们还可以使用rgba的方式来设置透明度，也可以达到同样的效果：</p>
<pre><code class="hljs language-js copyable" lang="js">ctx.fillStyle = <span class="hljs-string">'rgb(200,100,200,0.2)'</span>;
ctx.fillRect(<span class="hljs-number">30</span>, <span class="hljs-number">30</span>, <span class="hljs-number">100</span>, <span class="hljs-number">100</span>);
ctx.fillStyle = <span class="hljs-string">'rgb(200,100,200)'</span>;
ctx.fillRect(<span class="hljs-number">150</span>, <span class="hljs-number">30</span>, <span class="hljs-number">100</span>, <span class="hljs-number">100</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af80f9950d3149f1be8303774df78514~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">线形</h4>
<p>对于线的样式，canvas提供了很多的属性可以配置，依次来介绍一下：</p>
<p><code>lineWidth</code> 设置当前绘线的粗细。属性值必须为正数。默认值是1.0。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++)&#123;
    ctx.lineWidth = <span class="hljs-number">1</span>+i;
    ctx.beginPath();
    ctx.moveTo(<span class="hljs-number">5</span>+i*<span class="hljs-number">14</span>,<span class="hljs-number">5</span>);
    ctx.lineTo(<span class="hljs-number">5</span>+i*<span class="hljs-number">14</span>,<span class="hljs-number">140</span>);
    ctx.stroke();
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b726b7dc70a540288af5ff3725270920~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
需要注意的是，线宽是指给定路径的中心到两边的粗细，也就是在路径的两边各绘制线宽的一半。因为画布的坐标并不和像素直接对应，当需要获得精确的水平或垂直线的时候要特别注意。</p>
<p>在上面的例子中，用递增的宽度绘制了10条直线。最左边的线宽1.0单位。并且，最左边的以及所有宽度为奇数的线并不能精确呈现，这就是因为路径的定位问题。</p>
<p><code>如果我们「仔细观察」上图，可以发现两点问题：</code></p>
<ul>
<li>宽度1.0与宽度2.0从粗细上看起来没有什么差异;</li>
<li>奇数粗细的线边缘都有些模糊。</li>
</ul>
<p>再从下图来开始分析边的绘制过程：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b26b919aab654edfa782a2c798304b76~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<div align="center"><i title="https://media.prod.mdn.mozit.cloud/attachments/2012/07/09/201/7a73750ba89126b2b66a4b8900461552/canvas-grid.png">图解来自MDN</i></div>
<p>如果你想要绘制一条从 (3,1) 到 (3,5)，宽度是 1.0 的线条，你会得到像第二幅图一样的结果。实际填充区域（深蓝色部分）仅仅延伸至路径两旁各一半像素。而这半个像素又会以近似的方式进行渲染，这意味着那些像素只是部分着色，结果就是以实际笔触颜色一半色调的颜色来填充整个区域（浅蓝和深蓝的部分）。这就是上例中为何宽度为 1.0 的线并不准确的原因。</p>
<p>要解决这个问题，你必须对路径施以更加精确的控制。已知粗 1.0 的线条会在路径两边各延伸半像素，那么像第三幅图那样绘制从 (3.5,1) 到 (3.5,5) 的线条，其边缘正好落在像素边界，填充出来就是准确的宽为 1.0 的线条。</p>
<p><code>lineCap</code> 属性决定了线端点的样式。它可以为下面的三种的其中之一：<code>butt</code>，<code>round</code> 和 <code>square</code>。默认是 <code>butt</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建路径</span>
ctx.strokeStyle = <span class="hljs-string">'#09f'</span>;
ctx.beginPath();
ctx.moveTo(<span class="hljs-number">10</span>, <span class="hljs-number">10</span>);
ctx.lineTo(<span class="hljs-number">140</span>, <span class="hljs-number">10</span>);
ctx.moveTo(<span class="hljs-number">10</span>, <span class="hljs-number">140</span>);
ctx.lineTo(<span class="hljs-number">140</span>, <span class="hljs-number">140</span>);
ctx.stroke();

<span class="hljs-comment">// 画线条</span>
ctx.strokeStyle = <span class="hljs-string">'black'</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < lineCap.length; i++) &#123;
  ctx.lineWidth = <span class="hljs-number">15</span>;
  ctx.lineCap = lineCap[i];
  ctx.beginPath();
  ctx.moveTo(<span class="hljs-number">25</span> + i * <span class="hljs-number">50</span>, <span class="hljs-number">10</span>);
  ctx.lineTo(<span class="hljs-number">25</span> + i * <span class="hljs-number">50</span>, <span class="hljs-number">140</span>);
  ctx.stroke();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fc8f9f2b4a34180a4a76014d26f39ff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>lineJoin</code> 的属性值决定了图形中两线段连接处所显示的样子。它可以是这三种之一：round, bevel 和 miter。默认是 miter。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> lineJoin = [<span class="hljs-string">'round'</span>, <span class="hljs-string">'bevel'</span>, <span class="hljs-string">'miter'</span>];
ctx.lineWidth = <span class="hljs-number">10</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < lineJoin.length; i++) &#123;
  ctx.lineJoin = lineJoin[i];
  ctx.beginPath();
  ctx.moveTo(-<span class="hljs-number">5</span>, <span class="hljs-number">5</span> + i * <span class="hljs-number">40</span>);
  ctx.lineTo(<span class="hljs-number">35</span>, <span class="hljs-number">45</span> + i * <span class="hljs-number">40</span>);
  ctx.lineTo(<span class="hljs-number">75</span>, <span class="hljs-number">5</span> + i * <span class="hljs-number">40</span>);
  ctx.lineTo(<span class="hljs-number">115</span>, <span class="hljs-number">45</span> + i * <span class="hljs-number">40</span>);
  ctx.lineTo(<span class="hljs-number">155</span>, <span class="hljs-number">5</span> + i * <span class="hljs-number">40</span>);
  ctx.stroke();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3c6d560ffe9404fb1fb8509039440f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在使用miter属性的时候，线段的外侧边缘会被延伸交汇于一点上。线段之间夹角比较大时，交点不会太远，但随着夹角变小，交点距离会呈指数级增大。<code>miterLimit</code> 属性就是用来设定外延交点与连接点的最大距离，如果交点距离大于此值，连接效果会变成了 bevel。</p>
<pre><code class="copyable">ctx.lineWidth = 10;
ctx.strokeStyle = '#000';
ctx.miterLimit = 5;
ctx.beginPath();
ctx.moveTo(0, 100);
for (let i = 0; i < 24; i++) &#123;
  var dy = i % 2 == 0 ? 25 : -25;
  ctx.lineTo(Math.pow(i, 1.5) * 2, 75 + dy);
&#125;
ctx.stroke();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ba0f77a590443e3be4b2caa789e4d09~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到，最左侧的几条线由于夹角太小而延长线太长，导致连接线样式更改为bevel。</p>
<h4 data-id="heading-19">虚线</h4>
<p>可以用 <code>setLineDash</code> 方法和 <code>lineDashOffset</code> 属性来制定虚线样式。区别在于 <code>setLineDash</code> 方法接受一个数组，来指定线段与间隙的交替；<code>lineDashOffset</code> 属性设置起始偏移量。</p>
<pre><code class="copyable">ctx.beginPath();
ctx.setLineDash([4,2]);
ctx.strokeRect(10,10, 100, 100);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae8b7aea0e294c72b10be43390ebdb25~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-20">canvas 文本绘制</h3>
<p>canvas 提供了两种方法来渲染文本:</p>
<p><code>fillText(text, x, y [, maxWidth])</code><br>
在指定的(x,y)位置填充指定的文本，绘制的最大宽度是可选的.</p>
<pre><code class="copyable">ctx.font = "48px serif";
ctx.fillText("Hello world", 10, 50);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99d54ebba7184ab48af44bdf2e9deed5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>strokeText(text, x, y [, maxWidth])</code><br>
在指定的(x,y)位置绘制文本边框，绘制的最大宽度是可选的.</p>
<pre><code class="copyable">ctx.font = "48px serif";
ctx.strokeText("Hello world", 10, 50);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b712a3c9ff7b4d099fcc41c018ef89ee~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们可以通过以下的属性来配置文本样式：<br>
<strong>font = value</strong><br>
当前我们用来绘制文本的样式. 这个字符串使用和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Ffont" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/font" ref="nofollow noopener noreferrer">CSS font</a> 属性相同的语法. 默认的字体是 <code>10px sans-serif</code>。</p>
<p><strong>textAlign = value</strong><br>
文本对齐选项. 可选的值包括：<code>start</code>, <code>end</code>, <code>left</code>, <code>right</code> or <code>center</code>. 默认值是 start。</p>
<blockquote>
<p>这里的textAlign="center"比较特殊。textAlign的值为center时候文本的居中是基于你在fillText的时候所给的x的值，也就是说文本一半在x的左边，一半在x的右边（可以理解为计算x的位置时从默认文字的左端，改为文字的中心，因此你只需要考虑x的位置即可）。所以，如果你想让文本在整个canvas居中，就需要将fillText的x值设置成canvas的宽度的一半。</p>
</blockquote>
<p><strong>textBaseline = value</strong><br>
决定文字垂直方向的对齐方式. 可选的值包括：<code>top</code>, <code>hanging</code>, <code>middle</code>, <code>alphabetic</code>, <code>ideographic</code>, <code>bottom</code>。默认值是 <code>alphabetic</code>。</p>
<p><strong>direction = value</strong><br>
文本方向。可能的值包括：<code>ltr</code>, <code>rtl</code>, <code>inherit</code>。默认值是 <code>inherit</code>。</p>
<h3 data-id="heading-21">状态管理</h3>
<p>Saving and restoring state 是绘制复杂图形时必不可少的操作，在这里我们简单介绍一下作为一个预备知识。</p>
<p><code>save</code> 和 <code>restore</code> 方法是用来保存和恢复 canvas 状态的，都没有参数。</p>
<p>Canvas 的状态就是当前画面应用的所有<code>样式</code>和<code>变形</code>的一个快照。</p>
<p><strong>save()</strong>
Canvas状态存储在栈中，每当save()方法被调用后，当前的状态就被推送到栈中保存。<br>
一个绘画状态包括：</p>
<ol>
<li>
<p>当前应用的变形（即移动，旋转和缩放）</p>
</li>
<li>
<p>各种样式的值（strokeStyle, fillStyle, globalAlpha, lineWidth, lineCap, lineJoin, miterLimit, shadowOffsetX, shadowOffsetY, shadowBlur, shadowColor, globalCompositeOperation）</p>
</li>
<li>
<p>当前的裁切路径（clipping path）</p>
</li>
</ol>
<p>可以调用任意多次 <code>save</code> 方法。</p>
<p><strong>restore()</strong><br>
每一次调用 <code>restore</code> 方法，上一个保存的状态就从栈中弹出，所有设定都恢复(类似数组的 pop())。</p>
<pre><code class="copyable">ctx.fillRect(0, 0, 150, 150);   // 使用默认设置绘制一个矩形
ctx.save();                  // 保存默认状态

ctx.fillStyle = 'red'       // 在原有配置基础上对颜色做改变
ctx.fillRect(15, 15, 120, 120); // 使用新的设置绘制一个矩形

ctx.save();                  // 保存当前状态
ctx.fillStyle = '#FFF'       // 再次改变颜色配置
ctx.fillRect(30, 30, 90, 90);   // 使用新的配置绘制一个矩形

ctx.restore();               // 重新加载之前的颜色状态
ctx.fillRect(45, 45, 60, 60);   // 使用上一次的配置绘制一个矩形

ctx.restore();               // 加载默认颜色配置
ctx.fillRect(60, 60, 30, 30);   // 使用加载的配置绘制一个矩形
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0e9a7359ce64bd0b9c0e16938833cf1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-22">裁剪路径</h3>
<p>前面我们介绍了使用stroke、fill方法，canvas还提供了clip方法用来裁剪路径。<br>
裁切路径和普通的 canvas 图形差不多，不同的是它的作用是遮罩，用来隐藏不需要的部分。<br>
<code>ctx.clip(path, fillRule)</code></p>
<p><code>fillRule</code><br>
这个算法判断一个点是在路径内还是在路径外。<br>
允许的值：<br>
"nonzero": 非零环绕原则，默认的原则。</p>
<ul>
<li>在路径包围的区域中，随便找一点，向外发射一条射线，</li>
<li>和所有围绕它的边相交，</li>
<li>然后开启一个计数器，从0计数，</li>
<li>如果这个射线遇到顺时针围绕，那么+1，</li>
<li>如果遇到逆时针围绕，那么-1，</li>
<li>如果最终值非0，则这块区域在路径内。</li>
</ul>
<p>"evenodd": 奇偶环绕原则。</p>
<ul>
<li>在路径包围的区域中，随便找一点，向外发射一条射线，</li>
<li>和所有围绕它的边相交，</li>
<li>查看相交线的个数，如果为奇数，就填充，如果是偶数，就不填充。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1bca598cc1b4605a73cda4d1a8b51a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于箭头发起的区域，左为奇偶环绕规则，右为非零环绕规则</p>
<pre><code class="copyable">const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');
const w = canvas.width;
const h = canvas.height;

const x = w / 2;
const y = h / 2;
const r = 200;
const start = -Math.PI / 2;
const end = Math.PI * 3 / 2;

ctx.arc(x, y, r, start, end);
ctx.fillStyle = '#D43D59';
ctx.fill();

ctx.beginPath();
ctx.moveTo(x, y - r);

// 顶点连下左
ctx.lineTo(x - r * Math.sin(Math.PI / 5), y + r * Math.cos(Math.PI / 5));

// 下左连上右
ctx.lineTo(x + r * Math.cos(Math.PI / 10), y - r * Math.sin(Math.PI / 10));

// 上右连上左
ctx.lineTo(x - r * Math.cos(Math.PI / 10), y - r * Math.sin(Math.PI / 10));

// 上左连下右
ctx.lineTo(x + r * Math.sin(Math.PI / 5), y + r * Math.cos(Math.PI / 5));

ctx.fillStyle = '#246AB2';
// fill填充规则---奇偶原则
ctx.fill('evenodd');
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f095573d5f7943fd88b6e05af04d2ae9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>path</code><br>
需要剪切的 Path2D 路径。</p>
<h3 data-id="heading-23">变形 Transformations</h3>
<h4 data-id="heading-24">translate</h4>
<p><strong>translate(x, y)</strong></p>
<p>用来移动 canvas 的原点到指定的位置。<br>
translate 方法接受两个参数。x 是左右偏移量，y 是上下偏移量，如下图所示。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cd1a071d7934ba5ae867f3ccddb53d4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">ctx.save(); //保存坐原点平移之前的状态
ctx.translate(10, 10);
ctx.strokeRect(0, 0, 30, 30);
ctx.restore(); //恢复到最初状态
ctx.translate(50, 50);
ctx.fillRect(0, 0, 30, 30);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/454bd4373e324244856d685a6b6d75c8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>rotate(angle)</strong><br>
旋转坐标轴。</p>
<p>这个方法只接受一个参数：旋转的角度(angle)，它是顺时针方向的，以弧度为单位的值。
旋转的中心是坐标原点。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18dd987e7528464798c30e8e13988b77~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">ctx.fillStyle = "red";
ctx.save();

ctx.translate(100, 100);
ctx.rotate(Math.PI / 180 * 45);
ctx.fillStyle = "blue";
ctx.fillRect(0, 0, 100, 100);
ctx.restore();

ctx.save();
ctx.translate(0, 0);
ctx.fillRect(0, 0, 50, 50)
ctx.restore();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdf3905104804c0b936599467302aade~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>scale(x, y)</strong><br>
用来增减图形在 canvas 中的像素数目，对形状，位图进行缩小或者放大。</p>
<p>scale方法接受两个参数。x,y 分别是横轴和纵轴的缩放因子，它们都必须是正值。值比 1.0 小表示缩 小，比 1.0 大则表示放大，值为 1.0 时什么效果都没有。</p>
<blockquote>
<p>默认情况下，canvas 的 1 单位就是 1 个像素。举例说，如果我们设置缩放因子是 0.5，1 个单位就变成对应 0.5 个像素，这样绘制出来的形状就会是原先的一半。同理，设置为 2.0 时，1 个单位就对应变成了 2 像素，绘制的结果就是图形放大了 2 倍。</p>
</blockquote>
<pre><code class="copyable">ctx.fillStyle = "red";
ctx.scale(1,2);
ctx.fillRect(100, 20, 100, 100);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a514fa81ce2944c3b542c87b89636646~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>变形矩阵</strong></p>
<p><code>transform(a, b, c, d, e, f)</code>这个方法是将当前的变形矩阵乘上一个基于自身参数的矩阵.</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1196788be0684abd9b1da591e8810b63~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>a (m11)</code> 水平方向的缩放;<br>
<code>b(m12)</code> 竖直方向的倾斜偏移;<br>
<code>c(m21)</code> 水平方向的倾斜偏移;<br>
<code>d(m22)</code> 竖直方向的缩放;<br>
<code>e(dx)</code> 水平方向的移动;<br>
<code>f(dy)</code> 竖直方向的移动;</p>
<p>我们可以猜测出默认的矩阵值（1,0,0,1,0,0）;</p>
<p><code>setTransform(a, b, c, d, e, f)</code><br>
这个方法会将当前的变形矩阵重置为单位矩阵，然后用相同的参数调用 transform 方法。如果任意一个参数是无限大，那么变形矩阵也必须被标记为无限大，否则会抛出异常。从根本上来说，该方法是取消了当前变形,然后设置为指定的变形,一步完成。</p>
<p><code>resetTransform()</code><br>
重置当前变形为单位矩阵，它等价于ctx.setTransform(1, 0, 0, 1, 0, 0)。</p>
<pre><code class="copyable">ctx.transform(1, 1, 0, 1, 0, 0);
ctx.fillRect(0, 0, 100, 100);
ctx.resetTransform();
ctx.fillRect(110, 110, 100, 100);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04b4ec08a4e64df08f38ab96f51c1230~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-25">canvas VS svg</h2>
<p><code>svg</code>相关的入门介绍可以看<a href="https://juejin.cn/post/6982384216860262430" target="_blank" title="https://juejin.cn/post/6982384216860262430">这里</a></p>
<blockquote>
<p>canvas与svg相比，两种技术个人觉得并不好说哪种有绝对的优劣，只能说应用场景存在差异，但在一些js库的帮助下，这两者间的能力壁垒可能会有些突破，比如说<code>zRender</code>，使用数据驱动，并且提供类Dom事件模型，弥补了canvas本身弱事件操作的一些问题。</p>
</blockquote>
<p>简单对两者做一些比较：</p>



































<table><thead><tr><th>标题</th><th>canvas</th><th>svg</th></tr></thead><tbody><tr><td>使用方式</td><td>偏向于使用js程序式绘图，动态生成</td><td>使用xml描述绘图</td></tr><tr><td>操作对象</td><td>基于像素点(单canvas元素)</td><td>基于svg的图形元素(多元素Rect、Path、Text等)</td></tr><tr><td>使用场景</td><td>像素处理，适合动态渲染以及大数据量绘制</td><td>大面积的小数据量，高保真场景(如打印等)</td></tr><tr><td>设计原理</td><td>基于位图，不能改变大小，只能缩放</td><td>基于矢量，能很好处理图形大小的改变</td></tr><tr><td>功能支持</td><td>2d(图形、动画)、3d(webgl)绘制</td><td>图形、滤镜、动画</td></tr></tbody></table>
<h2 data-id="heading-26">参考资料</h2>
<p>MDN：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FCanvas_API%2FTutorial%2FDrawing_shapes" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a><br>
菜鸟教程：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fw3cnote%2Fhtml5-canvas-intro.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/w3cnote/html5-canvas-intro.html" ref="nofollow noopener noreferrer">www.runoob.com/w3cnote/htm…</a><br>
canvas填充原则：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fd4b8b5d931df" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/d4b8b5d931df" ref="nofollow noopener noreferrer">www.jianshu.com/p/d4b8b5d93…</a></p></div>  
</div>
            