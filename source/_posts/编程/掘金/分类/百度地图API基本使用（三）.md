
---
title: '百度地图API基本使用（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cb52b10b6f44799bd10c3ffaab2717d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 06:35:25 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cb52b10b6f44799bd10c3ffaab2717d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<p>本文系作者 <a href="https://juejin.cn/user/492230477350926" target="_blank" title="https://juejin.cn/user/492230477350926">chaoCode</a>原创，转载请私信并在文章开头附带作者和原文地址链接。</p>
<p>违者，作者保留追究权利。</p>
<h1 data-id="heading-0">前言</h1>
<p><strong>PS：我所使用的的是百度地图Javascript API 3.0</strong><br>
本文是对之前使用的延续，继续对百度地图API的一些使用去做归纳和总结，本次主要是对地图上的事件以及路线规划做下一下介绍，如果有小伙伴没有看过之前的<a href="https://juejin.cn/post/6991479115643617310" target="_blank" title="https://juejin.cn/post/6991479115643617310">百度地图API基本使用（一）｜8月更文挑战</a>，<a href="https://juejin.cn/post/6991845246388666399" target="_blank" title="https://juejin.cn/post/6991845246388666399">百度地图API基本使用（二）｜8月更文挑战</a>，可以先去观看一下，前期所需要的一些准备，以及一些基本的用法。</p>
<p>感兴趣的小伙伴可以自行查看百度地图官方提供的文档<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbsyun.baidu.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://lbsyun.baidu.com/" ref="nofollow noopener noreferrer">百度地图开放平台</a>开发文档中的JavaScript API</p>
<p>也可以通过下方示例中心更直观的看到百度地图API的一些使用，以及它的一些特性<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbsyun.baidu.com%2Fjsdemo.htm%23SetMapElementPOI" target="_blank" rel="nofollow noopener noreferrer" title="https://lbsyun.baidu.com/jsdemo.htm#SetMapElementPOI" ref="nofollow noopener noreferrer">百度地图开放平台-示例中心</a></p>
<p>想深入研究百度地图avaScript API 3.0方法参数信息的话，可以通过下方类参考<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbsyun.baidu.com%2Fcms%2Fjsapi%2Freference%2Fjsapi_reference_3_0.html%23a3b0" target="_blank" rel="nofollow noopener noreferrer" title="https://lbsyun.baidu.com/cms/jsapi/reference/jsapi_reference_3_0.html#a3b0" ref="nofollow noopener noreferrer">百度地图avaScript API v3.0类参考</a><br>
另外不同版本的API可以自行在开发文档中的类参考类目中找到,请自行查找</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cb52b10b6f44799bd10c3ffaab2717d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>不过要注意：实例中心使用的是BMap去创建容器的，最新版GL地图命名空间为BMapGL, 可按住鼠标右键控制地图旋转、修改倾斜角度。</strong></p>
<p>BMapGL在引入API的方式如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script type=<span class="hljs-string">"text/javascript"</span> src=<span class="hljs-string">"//api.map.baidu.com/api?type=webgl&v=3.0&ak=您的密钥"</span>></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>BMap在引入API的方式如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script type=<span class="hljs-string">"text/javascript"</span> src=<span class="hljs-string">"//api.map.baidu.com/api?v=3.0&ak=您的密钥"</span>></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照你自己的需求去引用</p>
<p>好的，废话不多说，开整</p>
<h1 data-id="heading-1">百度地图API-事件</h1>
<h4 data-id="heading-2">1. 地图事件</h4>
<p>1.地图加载完成事件
这个事件顾名思义就是在地图加载完成之后会调用这个事件，我们可以去做一些操作。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> BMap.Map(<span class="hljs-string">'container'</span>);
map.centerAndZoom(<span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.404</span>, <span class="hljs-number">39.928</span>), <span class="hljs-number">15</span>);
map.enableScrollWheelZoom(<span class="hljs-literal">true</span>);
map.addEventListener(<span class="hljs-string">'tilesloaded'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    alert(<span class="hljs-string">'地图加载完成！'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现的效果就是在地图加载完成之后，会弹出地图加载完成的提示！实际应用的时候可以能就会涉及到一些基于地图的初始化操作。具体情况具体分析，就不做过多赘述了。</p>
<p>2.地图单击事件
这个事件顾名思义就是在当我们鼠标点击地图上的时候，就会触发这个事件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> BMap.Map(<span class="hljs-string">'container'</span>);
map.centerAndZoom(<span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.404</span>, <span class="hljs-number">39.928</span>), <span class="hljs-number">15</span>);
map.enableScrollWheelZoom(<span class="hljs-literal">true</span>);
map.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
    alert(<span class="hljs-string">'点击位置经纬度：'</span> + e.latlng.lng + <span class="hljs-string">','</span> + e.latlng.lat);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们实现的这个就是单击地图的时候就会触发，可以获取到这个点的经纬度等信息。以及我们之前有介绍的覆盖物的一些触发事件，基本上都是使用的是这个单击事件，使用addEventListener监听click去实现的，这个方法还有监听别的事件，就不一一举例了，给大家看一下有哪些事件可以监听，这些都是从官方提供的类参考中找到的。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ed387fc70a742bb88b4b7fc8cf71d51~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3.注销事件
这个注销方法也比较简单，上一个点击事件我们使用的是addEventListener监听click去实现的，这个注销实际上就是移除这个事件，类似于之前的删除覆盖类都是使用的remove这个字段，对应的就是removeEventListener监听click去删除这个点击事件实现的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> BMap.Map(<span class="hljs-string">'container'</span>);
map.centerAndZoom(<span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.404</span>, <span class="hljs-number">39.928</span>), <span class="hljs-number">15</span>);
map.enableScrollWheelZoom(<span class="hljs-literal">true</span>);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">showInfo</span>(<span class="hljs-params">e</span>) </span>&#123;
    alert(<span class="hljs-string">'经纬度：'</span> + e.latlng.lng + <span class="hljs-string">','</span> + e.latlng.lat);
&#125;
<span class="hljs-comment">// 添加地图点击事件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addMapEvent</span>(<span class="hljs-params"></span>) </span>&#123;
    map.addEventListener(<span class="hljs-string">'click'</span>, showInfo);
&#125;
<span class="hljs-comment">// 移除地图点击事件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeMapEvent</span>(<span class="hljs-params"></span>) </span>&#123;
    map.removeEventListener(<span class="hljs-string">'click'</span>, showInfo);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想研究比较详细的地图事件的小伙伴可以自行查看研究<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbsyun.baidu.com%2Fjsdemo.htm%23kMapLoadOverEvent" target="_blank" rel="nofollow noopener noreferrer" title="https://lbsyun.baidu.com/jsdemo.htm#kMapLoadOverEvent" ref="nofollow noopener noreferrer">事件-地图事件</a></p>
<h4 data-id="heading-3">2. 覆盖物事件</h4>
<p>1.覆盖物鼠标事件
这个覆盖物鼠标事件实质就是地图的点击事件，只不过对象换成了覆盖物对象，本质都是使用addEventListener去监听事件的发生。<br>
创建一个点和一个面覆盖物，然后去给这两个覆盖物添加鼠标点击事件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> BMap.Map(<span class="hljs-string">'container'</span>);
<span class="hljs-keyword">var</span> point = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.404</span>, <span class="hljs-number">39.915</span>);
map.centerAndZoom(point, <span class="hljs-number">15</span>);
map.enableScrollWheelZoom(<span class="hljs-literal">true</span>);

<span class="hljs-comment">// 绘制点</span>
<span class="hljs-keyword">var</span> marker = <span class="hljs-keyword">new</span> BMap.Marker(point);
map.addOverlay(marker);

<span class="hljs-comment">// 绘制面</span>
<span class="hljs-keyword">var</span> polygon = <span class="hljs-keyword">new</span> BMap.Polygon([
    <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.387112</span>, <span class="hljs-number">39.920977</span>),
    <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.385243</span>, <span class="hljs-number">39.913063</span>),
    <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.394226</span>, <span class="hljs-number">39.917988</span>),
    <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.401772</span>, <span class="hljs-number">39.921364</span>),
    <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.41248</span>, <span class="hljs-number">39.927893</span>)
], &#123;
    <span class="hljs-attr">strokeColor</span>: <span class="hljs-string">'blue'</span>,
    <span class="hljs-attr">strokeWeight</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">strokeOpacity</span>: <span class="hljs-number">0.5</span>
&#125;);
map.addOverlay(polygon);

<span class="hljs-comment">//给点添加点击事件</span>
marker.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    alert(marker.toString() +  <span class="hljs-string">'被单击!'</span>);
&#125;);
<span class="hljs-comment">//给面添加点击事件</span>
polygon.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    alert(polygon.toString() +  <span class="hljs-string">'被单击!'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想研究比较详细的覆盖物事件的小伙伴可以自行查看研究<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbsyun.baidu.com%2Fjsdemo.htm%23kOverlayAddEvent" target="_blank" rel="nofollow noopener noreferrer" title="https://lbsyun.baidu.com/jsdemo.htm#kOverlayAddEvent" ref="nofollow noopener noreferrer">事件-覆盖物事件</a></p>
<h1 data-id="heading-4">百度地图API-路线规划</h1>
<p>首先说明一下这个路线规划分为4种，分别是驾车路线规划，公交路线规划，步行路线规划，以及骑行路线规划，使用的类是不一样的，我们一起来看一看。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a12538b33e841748718d0d4a8d6a86a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">1. 驾车路线规划</h4>
<p>1.基础驾车路线规划服务示例：<br>
代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> BMap.Map(<span class="hljs-string">"container"</span>); 
map.centerAndZoom(<span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.404</span>, <span class="hljs-number">39.915</span>), <span class="hljs-number">14</span>); 
<span class="hljs-keyword">var</span> driving = <span class="hljs-keyword">new</span> BMap.DrivingRoute(map, &#123; 
    <span class="hljs-attr">renderOptions</span>: &#123; 
        <span class="hljs-attr">map</span>: map, 
        <span class="hljs-attr">autoViewport</span>: <span class="hljs-literal">true</span> 
&#125; 
&#125;);
<span class="hljs-keyword">var</span> start = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.310791</span>, <span class="hljs-number">40.003419</span>);
<span class="hljs-keyword">var</span> end = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.486419</span>, <span class="hljs-number">39.877282</span>);
driving.search(start, end);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.数据接口<br>
驾车导航服务也提供了丰富的数据接口，通过onSearchComplete回调函数可以得到BMap.DrivingRouteResult对象，它包含了驾车导航结果数据信息。 结果会包含若干驾车方案，每条方案中包含了若干驾车线路。 每条驾车线路又会包含一系列的关键步骤（BMap.Step），关键步骤描述了具体驾车行驶方案。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> BMap.Map(<span class="hljs-string">"container"</span>); 
map.centerAndZoom(<span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.404</span>, <span class="hljs-number">39.915</span>), <span class="hljs-number">14</span>); 
<span class="hljs-keyword">var</span> options = &#123; 
    <span class="hljs-attr">onSearchComplete</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">results</span>)</span>&#123; 
        <span class="hljs-keyword">if</span> (driving.getStatus() == BMAP_STATUS_SUCCESS)&#123; 
            <span class="hljs-comment">// 获取第一条方案 </span>
            <span class="hljs-keyword">var</span> plan = results.getPlan(<span class="hljs-number">0</span>); 
            <span class="hljs-comment">// 获取方案的驾车线路 </span>
            <span class="hljs-keyword">var</span> route = plan.getRoute(<span class="hljs-number">0</span>); 
            <span class="hljs-comment">// 获取每个关键步骤，并输出到页面 </span>
            <span class="hljs-keyword">var</span> s = []; 
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < route.getNumSteps(); i ++) &#123; 
                <span class="hljs-keyword">var</span> step = route.getStep(i); 
                <span class="hljs-built_in">console</span>.log(step); 
            &#125; 
        &#125; 
    &#125; 
&#125;; 
<span class="hljs-keyword">var</span> driving = <span class="hljs-keyword">new</span> BMap.DrivingRoute(map, options);
<span class="hljs-keyword">var</span> start = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.310791</span>, <span class="hljs-number">40.003419</span>);
<span class="hljs-keyword">var</span> end = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.486419</span>, <span class="hljs-number">39.877282</span>);
driving.search(start, end);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">2. 公交路线规划</h4>
<p>BMap.TransitRoute类提供公交线路规划服务。<br>
注意：v3.0中，新增了TransitRoutePlan.getTotal 和 TransitRoutePlan.getTotalType方法，可以获取一条公交换成方案中总路段数（步行+公交），和指定路段的交通方式类型（步行或公交）。</p>
<p>1.使用服务示例<br>
代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> BMap.Map(<span class="hljs-string">"container"</span>); 
map.centerAndZoom(<span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.404</span>, <span class="hljs-number">39.915</span>), <span class="hljs-number">14</span>); 
<span class="hljs-keyword">var</span> transit = <span class="hljs-keyword">new</span> BMap.TransitRoute(map, &#123; 
    <span class="hljs-attr">renderOptions</span>: &#123; 
        <span class="hljs-attr">map</span>: map, 
        <span class="hljs-attr">autoViewport</span>: <span class="hljs-literal">true</span> 
    &#125; 
&#125;);
<span class="hljs-keyword">var</span> start = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.310791</span>, <span class="hljs-number">40.003419</span>);
<span class="hljs-keyword">var</span> end = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.486419</span>, <span class="hljs-number">39.877282</span>);
transit.search(start, end);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.进行跨城路线规划<br>
代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> BMap.Map(<span class="hljs-string">"container"</span>); 
map.centerAndZoom(<span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.404</span>, <span class="hljs-number">39.915</span>), <span class="hljs-number">14</span>); 
<span class="hljs-keyword">var</span> transit = <span class="hljs-keyword">new</span> BMap.TransitRoute(map, &#123; 
    <span class="hljs-attr">renderOptions</span>: &#123; 
        <span class="hljs-attr">map</span>: map, 
        <span class="hljs-attr">autoViewport</span>: <span class="hljs-literal">true</span>

    &#125;,

    <span class="hljs-comment">// 配置跨城公交的换成策略为优先出发早</span>

    <span class="hljs-attr">intercityPolicy</span>: BMAP_INTERCITY_POLICY_EARLY_START,

    <span class="hljs-comment">// 配置跨城公交的交通方式策略为飞机优先</span>

    <span class="hljs-attr">transitTypePolicy</span>: BMAP_TRANSIT_TYPE_POLICY_AIRPLANE

&#125;);

<span class="hljs-keyword">var</span> start = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.310791</span>, <span class="hljs-number">40.003419</span>);
<span class="hljs-keyword">var</span> end = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">121.490546</span>, <span class="hljs-number">31.233585</span>);
transit.search(start, end);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">3. 步行路线规划</h4>
<p>BMap.WalkingRoute提供步行线路规划服务。基本用法和驾车线路规划类似。<br>
使用服务示例<br>
代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> BMap.Map(<span class="hljs-string">"container"</span>); 
map.centerAndZoom(<span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.404</span>, <span class="hljs-number">39.915</span>), <span class="hljs-number">14</span>); 
    <span class="hljs-keyword">var</span> walk = <span class="hljs-keyword">new</span> BMap.WalkingRoute(map, &#123; 
    <span class="hljs-attr">renderOptions</span>: &#123;<span class="hljs-attr">map</span>: map&#125; 
&#125;); 
<span class="hljs-keyword">var</span> start = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.310791</span>, <span class="hljs-number">40.003419</span>);
<span class="hljs-keyword">var</span> end = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.486419</span>, <span class="hljs-number">39.877282</span>);
walk.search(start, end);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">4. 骑行路线规划</h4>
<p>BMap.RidingRoute提供骑行线路规划服务，基本用法和步行线路规划基本相同。<br>
使用服务示例<br>
代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> BMap.Map(<span class="hljs-string">"container"</span>); 
map.centerAndZoom(<span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.404</span>, <span class="hljs-number">39.915</span>), <span class="hljs-number">14</span>); 
<span class="hljs-keyword">var</span> riding = <span class="hljs-keyword">new</span> BMap.RidingRoute(map, &#123; 
    <span class="hljs-attr">renderOptions</span>: &#123;<span class="hljs-attr">map</span>: map&#125; 
&#125;); 
<span class="hljs-keyword">var</span> start = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.310791</span>, <span class="hljs-number">40.003419</span>);
<span class="hljs-keyword">var</span> end = <span class="hljs-keyword">new</span> BMap.Point(<span class="hljs-number">116.486419</span>, <span class="hljs-number">39.877282</span>);
riding.search(start, end);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>感兴趣的小伙伴可以自行去研究<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbsyun.baidu.com%2Findex.php%3Ftitle%3Djspopular3.0%2Fguide%2Frouteplan" target="_blank" rel="nofollow noopener noreferrer" title="https://lbsyun.baidu.com/index.php?title=jspopular3.0/guide/routeplan" ref="nofollow noopener noreferrer">百度地图Javascript API 3.0 出行路线规划</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbsyun.baidu.com%2Fjsdemo.htm%23drivingroute" target="_blank" rel="nofollow noopener noreferrer" title="https://lbsyun.baidu.com/jsdemo.htm#drivingroute" ref="nofollow noopener noreferrer">百度地图JS API示例 路线规划</a></p>
<p><strong>感谢诸君的观看，文中如有纰漏，欢迎在评论区来交流。如果这篇文章帮助到了你，欢迎点赞👍和关注。</strong></p></div>  
</div>
            