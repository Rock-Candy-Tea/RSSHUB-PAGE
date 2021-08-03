
---
title: '阿ken的HTML、CSS的入门指南_CSS盒子模型（笔记五）贰｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6a5b3fb98d94f5799a1f446f1f45d12~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 17:52:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6a5b3fb98d94f5799a1f446f1f45d12~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>感激相遇 你好 我是阿ken</strong></p>
<blockquote>
<p>作者：请叫我阿ken<br>
链接：<a href="https://juejin.cn/user/1091187754155048/posts" target="_blank" title="https://juejin.cn/user/1091187754155048/posts">juejin.cn/user/109118…</a><br>
来源：掘金<br>
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。</p>
</blockquote>
<h1 data-id="heading-0"><strong>🌊🌈关于前言：</strong></h1>
<p><strong>文章部分内容及图片出自网络，如有问题请与我本人联系(主页介绍中有公众号)</strong></p>
<p><strong>本博客暂适用于刚刚接触HTML以及好久不看想要复习的小伙伴</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6a5b3fb98d94f5799a1f446f1f45d12~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>击鼓之后，我们把在黑暗中跳舞的心脏叫做月亮</strong><br>
                               <strong>海子《亚洲铜》</strong></p>
<h1 data-id="heading-1"><strong>🌊🌈关于内容：</strong></h1>
<h3 data-id="heading-2"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>🦞🐙🦀5.2.2  边距属性</h3>
<p><code>CSS</code>的边距属性包括“内边距”和“外边距”两种。</p>
<h4 data-id="heading-3"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>🗨🦁1. 内边距</h4>
<p>在网页设计中，为了调整内容在盒子中的显示位置，常需要给元素设置内边距，<strong>所谓内边距指的是元素内容与边框之间的距离，也常常称为内填充</strong>，<strong>在<code>CSS</code>中<code>padding</code>属性用于设置内边距，同边框属性<code>border</code>一样，<code>padding</code>也是复合属性</strong>，其相关设置方法如下:\</p>
<p>● <code>padding-top</code>: 上内边距;</p>
<p>● <code>padding-right</code>: 右内边距;</p>
<p>● <code>padding-bottom</code>: 下内边距;</p>
<p>● <code>padding-left</code>: 左内边距:</p>
<p>● <code>padding</code>: 上内边距 [ 右内边距 下内边距 左内边距 ]。</p>
<p>在上面的设置中，<strong><code>padding</code>相关属性的取值可为<code>auto</code>自动(默认值)、不同单位的数值相对于父元素(或浏览器)宽度的百分比(%)，实际工作中最常用的是像素值(<code>px</code>)，不允许使用负值。</strong></p>
<p><strong>同边框相关属性一样，使用复合属性<code>padding</code>定义内边距时，必顶按顺时针顺序采用值复制，一个值为四边、两个值为上下/左右，三个值为上/左右/下。</strong></p>
<p>案例:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>设置内边距<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-class">.border</span> &#123;
<span class="hljs-attribute">border</span>: <span class="hljs-number">5px</span> solid <span class="hljs-number">#F60</span>;
&#125; <span class="hljs-comment">/*为图像和段落设置边框*/</span>

<span class="hljs-selector-tag">img</span> &#123;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">80px</span>;<span class="hljs-comment">/*图像4个方向内边距相同*/</span>
<span class="hljs-attribute">padding-bottom</span>: <span class="hljs-number">0</span>;<span class="hljs-comment">/*单独设置下内边距*/</span>
&#125;   <span class="hljs-comment">/*上面两行代码等价于 padding:80px 80px 0;*/</span>

<span class="hljs-selector-tag">p</span>&#123;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">5%</span>;
&#125;  <span class="hljs-comment">/*段落内边距为父元素宽度的5%*/</span> 

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"border"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3660691301,837491451&fm=26&gp=0.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"阿ken"</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"border"</span>></span>段落内边距为父元素宽度的5%。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201120105631235.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于段落的内边距设置了%数值，当拖动浏览器窗口改其宽度时，段落的内边距会随之发生变化(<strong>此时< p>标记的父元素为< body></strong> )。</p>
<blockquote>
<p><strong>注意:</strong></p>
<p><strong>如果设置内外边距为百分比，则不论上下或左右的内外边距， 都是相对于父元素宽度 width 的百分比，随父元素 width 的变化而变化，和高度 height 无关</strong>。</p>
</blockquote>
<h4 data-id="heading-4"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>🗨🦁2.  外边距</h4>
<p>网页是由多个盒子排列而成的，要想拉开盒子与盒于之间的距离，合理地布局网页，就需要为盒子设置外边距，<strong>所谓外边距指的是元素边框与相邻元素之间的距离</strong>。在<code>CSS</code>中<code>margin</code>属性用于设置外边距，它是一个复合属性， 与内边距<code>padding</code>的用法类似，设置外边距的方法如下：</p>
<p>● <code>margin-top</code>: 上外边距;</p>
<p>● <code>margin-right</code>: 右外边距;</p>
<p>● <code>margin-bottom</code>: 下外边距;</p>
<p>● <code>margin-left</code>: 左外边距;</p>
<p>● <code>margin</code>: 上外边距 [右外边距 下外边距 左外边距] 。</p>
<p><code>margin</code>相关属性的值，以及复合属性<code>margin</code>取 1 ~ 4 个值的情况与<code>padding</code>相同。但是外边距可以使用负值，使相邻元素重叠。</p>
<p><strong>当对块级元素应用宽度属性<code>width</code>，并将左右的外边距都设置为<code>auto</code>,可使块级元素水平居中</strong>，实际工作中常用这种方式进行网页布局，示例代码如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.header</span>&#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">960px</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>案例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>设置外边距<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">img</span>&#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">5px</span> solid red;
<span class="hljs-attribute">float</span>: left; <span class="hljs-comment">/*设置图像左浮动*/</span>
<span class="hljs-attribute">margin-right</span>: <span class="hljs-number">50px</span>; <span class="hljs-comment">/*设置图像的右外边距*/</span>
<span class="hljs-attribute">margin-left</span>: <span class="hljs-number">30px</span>;  <span class="hljs-comment">/*设置图像的左外边距*/</span>
<span class="hljs-comment">/*上面两行代码等价于margin: 0 50px 0 30px;*/</span>
&#125;

<span class="hljs-selector-tag">p</span>&#123;
<span class="hljs-attribute">text-indent</span>: <span class="hljs-number">2em</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1471480362,870954799&fm=26&gp=0.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"我是阿ken"</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>你好，我是阿ken<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201120105903642.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用浮动属性<code>float</code>使图像居左，同时设置图像的左外边距和右外边距，使图像和文本之间拉开一定的距离， 实现常见的排版效果(对于浮动，这里了解即可，后面章节将会详细介绍)。</p>
<p>图像和段落文本之间拉开了一定的距离，实现了图文混排的效果。但是仔细观察效果图会发现，浏览器边界与网页内容之间也存在一定的距离， 然而我们并没有对<code><p></code>或<code><body></code>元素应用内边距或外边距，可见这些<strong>元素默认就存在内边距和外边距样式。网页中默认就存在内外边距的元素有<code><body></code>、<code><h1>~<h6></code>、<code><p></code>等。</strong></p>
<p>为了更方便地控制网页中的元素，制作网页时，可使用如下代码清除元素的默认内外边距：</p>
<pre><code class="hljs language-css copyable" lang="css">* &#123;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>; <span class="hljs-comment">/*清除内边距*/</span>
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;  <span class="hljs-comment">/*清除外边距*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>清除元素默认内边距和外边距样式后，浏览器边界与网页内容之间的距离消失。</p>
<h3 data-id="heading-5"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>🦞🐙🦀5.2.3  box-shadow属性</h3>
<p>在网页制作中，经常需要对盒子添加阴影效果。<strong><code>CSS</code>中的<code>box-shadow</code>属性可以实现阴影的添加</strong>。</p>
<p>基本语法格式：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">box-shadow</span>: 像素值<span class="hljs-number">1</span> 像素值<span class="hljs-number">2</span> 像素值<span class="hljs-number">3</span> 像素值<span class="hljs-number">4</span> 颜色值 阴影类型;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的语法格式中，<code>box-shadow</code>属性共包含 6个参数值。</p>
<p><strong>box-shadow 属性参数值：</strong></p>

































<table><thead><tr><th>参数值</th><th>说明</th></tr></thead><tbody><tr><td>像素值1</td><td>表示元素水平阴影位置，可以为负值(必选属性)</td></tr><tr><td>像素值2</td><td>表示元素垂直阴影位置，可以为负值(必选属性)</td></tr><tr><td>像素值3</td><td>阴影模糊半径(可选属性)</td></tr><tr><td>像素值4</td><td>阴影扩展半径，不能为负值(可选属性)</td></tr><tr><td>颜色值</td><td>阴影颜色(可选属性)</td></tr><tr><td>阴影类型</td><td>内阴影 ( inset ) /外阴影 (默认) (可选属性)</td></tr></tbody></table>
<p><strong>其中“像素值1”、“像素值2”为必选参数值不可以省略，其余为可选参数值，不设置”阴影类型“参数时默认为”外阴影“，设置"<code>inset</code>"参数值后，阴影类型变为内阴影</strong>。</p>
<p>案例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>box-shadow属性<span class="hljs-tag"></<span class="hljs-name">tit1e</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">img</span>&#123;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>;
<span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#CCC</span>;
<span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">5px</span> <span class="hljs-number">5px</span> <span class="hljs-number">10px</span> <span class="hljs-number">2px</span> <span class="hljs-number">#999</span> inset;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"border"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://dss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1172960894,4133724990&fm=26&gp=0.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"阿ken"</span>/></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201120110931809.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
代码定义了一个水平位置和垂直位置均为5px，模糊半径为10px，扩展半径为2px的浅灰色内阴影。</p>
<p><strong>图片出现了内阴影效果。值得一提的是， 同<code>text-shadow</code>属性(文字阴影属性)一样，<code>box-shadow</code>属性也可以改变阴影的投射方向及添加多重阴影效果。</strong></p>
<p>案例：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">5px</span> <span class="hljs-number">5px</span> <span class="hljs-number">10px</span> <span class="hljs-number">2px</span> <span class="hljs-number">#999</span> inset, -<span class="hljs-number">5px</span> -<span class="hljs-number">5px</span> <span class="hljs-number">10px</span> <span class="hljs-number">2px</span> <span class="hljs-number">#333</span> inset;
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201120111227395.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>🦞🐙🦀5.2.4  box-sizing 属性</h3>
<p><strong>当一个盒子的总宽度确定之后，要想给盒子添加边框或内边距，往往需要更改<code>width</code>属性值，才能保证盒子总宽度不变，操作起来烦琐且容易出错</strong>，运用<code>CSS3</code>的<code>box-sizing</code>属性可以轻松解决这个问题。<code>box-sizing</code>属性用于定义盒子的宽度值和高度值是否包含元素的内边距和边框。</p>
<p>基本语法格式：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">box-sizing</span>: content-box/border-box;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的语法格式中，<strong><code>box-sizing</code>属性的取值可以为<code>content-box</code>或<code>border-box</code>。</strong></p>
<p>对它们的解释如下：</p>
<p>● <strong>content-box: 浏览器对盒模型的解释遵从 W3C 标准， 当定义 width 和 height 时，它的参数值不包括 border 和 padding 。</strong></p>
<p>● <strong>border-box: 当定义 width 和 height 时，border 和 padding 的参数值被包含在 width 和 height 之内。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>box-sizing<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-class">.box1</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">padding-right</span>: <span class="hljs-number">10px</span>;
<span class="hljs-attribute">background</span>: <span class="hljs-number">#F90</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">10px</span> solid <span class="hljs-number">#CCC</span>;
<span class="hljs-attribute">box-sizing</span>: content-box;
&#125;

<span class="hljs-selector-class">.box2</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
<span class="hljs-attribute">padding-right</span>: <span class="hljs-number">10px</span>;
<span class="hljs-attribute">background</span>: <span class="hljs-number">#F90</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">10px</span> solid <span class="hljs-number">#CCC</span>;
<span class="hljs-attribute">box-sizing</span>: border-box;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box1"</span>></span>content_box属性<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box2"</span>></span>border_box属性<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201120114308223.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上述代码中定义了两个盒子，并对它们设置相同的宽、高、右内边距和边框样式。并且，对第一个盒子定义 “<code>box-sizing: content-box</code>; ” 样式，对第二个盒子定义 “<code>box-sizing: border-box;</code>” 样式。</p>
<p>应用了 “<code>box-sizing: content-box;</code>” 样式的盒子1，宽度比<code>width</code>参数值多出 30px，总宽度为 330px；而应用了 “<code>box-sizing: border-box;</code>” 样式的盒子2，宽度等于<code>width</code>参数值，总宽度仍为 300px。</p>
<p>可见应用 “<code>box-sizing: border-box;</code>” 样式后，盒子<code>border</code>和<code>padding</code>的参数值是被包含在<code>width</code>和<code>height</code>之内的。</p>
<h2 data-id="heading-7"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>🌴🌵🌳5.3  背景属性</h2>
<h3 data-id="heading-8"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>🦞🐙🦀5.3.1  设置背景颜色(background-color)</h3>
<p>在<code>CSS</code>中，<strong>使用<code>background-color</code>属性来设置网页元素的背景颜色</strong>，其属性值与文本颜色的取值一样，可使用预定义的颜色值、十六进制#RRGGBB或RGB代码rgb(r,g,b)。<br>
<strong><code>background-color</code>的默认值为<code>transparent</code>,即背景透明，此时子元素会显示其父元素的背景。</strong></p>
<p>案例:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>设置背景颜色<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-tag">body</span>&#123;
<span class="hljs-attribute">background-color</span>: <span class="hljs-number">#CCC</span>;
&#125;<span class="hljs-comment">/*设置网页的背景颜色*/</span>

<span class="hljs-selector-tag">h2</span>&#123;
<span class="hljs-attribute">font-family</span>: <span class="hljs-string">"微软雅黑"</span>;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#FFF</span>;
<span class="hljs-attribute">background-color</span>: <span class="hljs-number">#FC3</span>;
&#125;<span class="hljs-comment">/*设置标题的背景颜色*/</span>

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>你好<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是阿ken<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201120114832668.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码运行后，标题文本的背景颜色为黄色，段落文本显示父元素<code>body</code>的背景颜色。这是由于未对段落标记<code><p></code>设置背景颜色时，会默认为透明背景(transparent)，所以段落将显示其父元素的背景颜色。</p>
<h3 data-id="heading-9"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>🦞🐙🦀5.3.2  设置背景图像(background-image)</h3>
<p>背景不仅可以设置为某种颜色，还可以将图像作为元素的背景。在<code>CSS</code>中<strong>通过<code>background-image</code>属性设置背景图像</strong>。</p>
<p>案例：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span>&#123;
<span class="hljs-attribute">background-color</span>: <span class="hljs-number">#CCC</span>; <span class="hljs-comment">/*设置网页的背景颜色*/</span>
<span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">#</span>); <span class="hljs-comment">/*设置网页的背景图像*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>阿ken<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201120174030459.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码运行后，容易看出，背景图像自动沿着水平和竖直两个方向平铺，充满整个页面，并且覆盖了<code><body></code>的背景颜色。</p>
<h3 data-id="heading-10"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>🦞🐙🦀5.3.3  背景与图片不透明度的设置</h3>
<h4 data-id="heading-11"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>🗨🦁1. <strong>RGBA模式</strong></h4>
<p><strong>RGBA是</strong><code>CSS3</code>新增的颜色模式，它是<code>RGB</code>颜色模式的延伸，该模式是<strong>在红、绿、蓝三原色的基础上添加了不透明度参数</strong>。</p>
<p>语法格式:</p>
<pre><code class="hljs language-css copyable" lang="css">rgba(r, g, <span class="hljs-selector-tag">b</span>, alpha);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的语法格式中，前三个参数与<code>RGB</code>中的参数含义相同，<strong><code>alpha</code>参数是一个介于 0.0 ( 完全透明 ) 和 1.0 ( 完全不透明 ) 之间的数字</strong>。</p>
<p>案例：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
<span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.5</span>);
&#125;<span class="hljs-comment">/*RGBA模式为p元素指定透明度为0.5，颜色为红色的背景*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>阿ken<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d0cbd0fbefe4c60ac24023e0de7eb47~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>🗨🦁2. opacity 属性</h4>
<p>在<code>CSS3</code>中，使用 <strong><code>opacity</code>属性能够使任何元素呈现出透明效果</strong>。</p>
<p>语法格式:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">opacity</span>: opacityValue;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述语法中，<strong><code>opacity</code>属性用于定义元素的不透明度，参数<code>opacityVaule</code>表示不透明度的值，它是一个介于 0 ~ 1 的浮点数值。其中，0 表示完全透明，1 表示完全不透明</strong>，而 0.5 则表示半透明。</p>
<p>案例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!doctype <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>opacity属性设置图像的透明度<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">

<span class="hljs-selector-id">#boxwrap</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">330px</span>; 
<span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span> auto; 
<span class="hljs-attribute">border</span>: solid <span class="hljs-number">1px</span> <span class="hljs-number">#FF6666</span>;
&#125;

<span class="hljs-selector-tag">img</span><span class="hljs-selector-pseudo">:first</span>-child &#123;
<span class="hljs-attribute">opacity</span>: <span class="hljs-number">1</span>;
&#125;

<span class="hljs-selector-tag">img</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
<span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.8</span>;
&#125;

<span class="hljs-selector-tag">img</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
<span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.5</span>;
&#125;

<span class="hljs-selector-tag">img</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">4</span>) &#123;
<span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.2</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"boxwrap"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"160"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"109"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"160"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"109"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"160"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"109"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"160"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"109"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><img src="https://img-blog.csdnimg.cn/20201120174554690.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2tlbmtlbl8=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述代码通过使用<code>opacity</code>属性为同一张图片设置了不同的透明度， 且<code>opacityVaule</code>依次减小。</p>
<p><strong><code>opacityValue</code>的值越小表示透明度越高。</strong>
<br>
<br><br><br>
<strong>今日入门学习暂时告一段落</strong></p>
<p><strong>Peace</strong></p>
<h1 data-id="heading-13"><strong>🌊🌈往期回顾：</strong></h1>
<p><a href="https://juejin.cn/post/6987731486707286030" title="https://juejin.cn/post/6987731486707286030" target="_blank"><strong>阿ken的HTML、CSS的入门指南_HTML基础(笔记一)</strong></a><br>
<a href="https://juejin.cn/post/6988080294242811918/" title="https://juejin.cn/post/6988080294242811918/" target="_blank"><strong>阿ken的HTML、CSS的入门指南_HTML页面元素和属性(笔记二)</strong></a><br>
<a href="https://juejin.cn/post/6988714719125176351" title="https://juejin.cn/post/6988714719125176351" target="_blank"><strong>阿ken的HTML、CSS的学习笔记_文本样式属性(笔记三)</strong></a><br>
<a href="https://juejin.cn/post/6991276111527149605" title="https://juejin.cn/post/6991276111527149605" target="_blank"><strong>阿ken的HTML、CSS的入门指南_CSS3选择器(笔记四)</strong></a><br>
<a href="https://juejin.cn/post/6991769219910074399" target="_blank" title="https://juejin.cn/post/6991769219910074399"><strong>阿ken的HTML、CSS的入门指南_CSS盒子模型(笔记五)上</strong></a></p>
<p><strong>你好，我是阿ken<br>
感谢阅读<br>
博文若有瑕疵请在评论区留言或在主页个人介绍中添加公众号私聊我<br>
感谢不吝赐教</strong></p></div>  
</div>
            