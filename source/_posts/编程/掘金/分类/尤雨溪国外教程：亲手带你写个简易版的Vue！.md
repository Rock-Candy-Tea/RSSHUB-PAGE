
---
title: '尤雨溪国外教程：亲手带你写个简易版的Vue！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/702a6f2449b14e358ca6886f7690a049~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 18:04:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/702a6f2449b14e358ca6886f7690a049~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>⚠️本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<h1 data-id="heading-0">前言</h1>
<p>很多时候我们都对<code>源码</code>展现出了一定的渴求，但当被问到究竟为什么想看源码时，答案无非也就那么几种：</p>
<ul>
<li>为了面试</li>
<li>为了在简历上写自己会源码</li>
<li>了解底层原理 学习高手思路</li>
<li>通过源码来学习一些小技巧(<em>骚操作</em>)</li>
<li>对框架如何实现的各种功能感到好奇</li>
<li>内卷严重 不看不行 逆水行舟 不进则退</li>
<li>自己也想造轮子 先看看别人都是怎么做的</li>
<li>各种公众号和卖课的都在贩卖焦虑 被洗脑洗的</li>
</ul>
<p>但其实很少人会真正的看明白源码，一方面是由于代码量实在是太多了，另一方面则是当我们阅读别人代码的时候就是容易搞得一头雾水。因为每个人的编码方式以及编码习惯都大相径庭，在看一个编码习惯与自己不同的人的代码时是很累的。</p>
<p>况且不仅是由于每个人的编码风格相差甚远，人与人之间各自擅长的技术方向以及技术水平也都是<code>横看成岭侧成峰</code>，<code>远近高低各不同</code>。刨除掉以上的种种原因之后，更重要的一个原因是很多人框架用的都不够精通呢、用过的<code>API</code>也就那么几个常见的，其他不常用但很高阶的<code>API</code>都没怎么用过，连用都没用明白呢，这样的人看源码的时候当然会被绕晕啦！</p>
<blockquote>
<p>那肯定有人会说：尤雨溪他框架就一定用的很6吗？我每天都在用他的框架写代码，他还不一定有我熟练呢！</p>
</blockquote>
<p>这么说确实有一定的道理，但如果论底层，他比谁都了解。之所以我们啃不动源码的很重要的一个原因就是：细枝末节的东西实在是太多了，很容易令大家找不到重点。这些细枝末节的东西自然有它们存在的道理，但它们确成为了我们行走在钻研源码这条路上的绊脚石。</p>
<h2 data-id="heading-1">题外话</h2>
<p>怎样学习源码才是最科学的方式呢？我们来看一个例子：有一些听起来非常高大上的高科技产品，如<code>电磁轨道炮</code>。各个军事强国都在争相探索这一领域，假设有一天，我们一觉醒来成为了<code>国家电磁轨道炮首席研究员</code>，是专门负责研究电磁轨道炮底层技术的。那么当我们拆解一个电磁轨道炮的时候，大概率你是看不懂它的内部构造的。因为里面会包含许多非常复杂的<code>高强度材料</code>、<code>控制磁力的电极</code>、<code>蜿蜒曲折的电线</code>、<code>提高精准度的装置</code>以及一些<code>利于使用者操控的封装</code>等等…</p>
<p>那么此时的你可能就不太容易搞明白<code>电磁轨道炮的真正原理</code>，直到有一次在网上偶然间看到一个视频，视频中的人用了一些磁铁、若干钢珠、以及几个我们日常生活中能够搞到的材料来制作了一个<code>简易版的电磁轨道炮</code>。这样我们一下子就能够搞懂<code>电磁轨道炮的真正原理</code>，虽然这样的轨道炮并不能真正的用于实战，但只要我们明白了最基础的那部分，我们就可以在此基础上一步步进行扩展，慢慢弄懂整个能够用于实战的复杂轨道炮。</p>
<blockquote>
<p>源码也是同理，我们按照<code>电磁轨道炮</code>的思路一步步来，先搞清楚最核心的基础部分，慢慢的再一步步去进阶。这样的学习方法比我们肯定一上来就去拆解一个完整版的<code>电磁轨道炮</code>要强得多</p>
</blockquote>
<p>既然我们有这样的需求，那么作为一个流行框架的作者就必然会有所回应：在一次培训的过程中，<code>尤雨溪</code>带领大家写了一个非常微型的<code>Vue3</code>。不过可惜这是他在国外办过的为期一天的培训，我们国内的观众并没有福气能够享受到<code>被框架作者培训</code>的这么一次教学。但好在<code>尤雨溪已经把代码全部上传到了codepen上</code>，大家可以点击<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fcollection%2FDkxpbE" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/collection/DkxpbE" ref="nofollow noopener noreferrer">这个链接</a>来阅读尤雨溪亲手写的代码，或者也可以选择留在本篇文章内，看我来用中文为大家讲解<code>尤雨溪的亲笔代码</code>！</p>
<h1 data-id="heading-2">响应式篇</h1>
<p><code>尤雨溪</code>在某次直播时曾表示过：<code>Vue3 的源码要比 Vue2 的源码要好学很多</code>。<code>Vue3</code>在架构以及模块的耦合关系设计方面比<code>Vue2</code>更好，可以一个模块一个模块看，这样比较容易理解。如果是刚上手，可以从<code>Reactivity</code>看起。因为<code>Reactivity</code>是整个<code>Vue3</code>中跟外部没有任何耦合的一个模块。</p>
<p><code>Reactivity</code>就是我们常说的<code>响应式</code>，大名鼎鼎的<code>React</code>也是这个意思，不信仔细对比一下前五个字母。那么什么是响应式呢？想想看<code>React</code>是什么框架？<code>MVVM</code>对吧？<code>MVVM</code>的主打口号是：</p>
<blockquote>
<p><strong>数据驱动视图！</strong></p>
</blockquote>
<p>也就是说当数据发生改变时我们会重新渲染一下组件，这样就能够达到一修改数据，页面上用到这个数据的地方就会实时发生变化的效果。不过在数据发生变化时也不仅仅只是能够更新视图，还可以做些别的呢！尤雨溪在创建<code>@vue/reactivity</code>这个模块的时候，借鉴的是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnx-js%2Fobserver-util" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nx-js/observer-util" ref="nofollow noopener noreferrer">@nx-js/observer-util</a>这个库。我们来看一眼它在<code>GitHub</code>上<code>README.md</code>里展示的一段示例代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; observable, observe &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@nx-js/observer-util'</span>;

<span class="hljs-keyword">const</span> counter = observable(&#123; <span class="hljs-attr">num</span>: <span class="hljs-number">0</span> &#125;);
<span class="hljs-keyword">const</span> countLogger = observe(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(counter.num));

<span class="hljs-comment">// 这行代码将会调用 countLogger 这个函数并打印出：1</span>
counter.num++;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是很像<code>Vue3</code>的<code>reactive</code>和<code>watchEffect</code>啊？其实就是我们提前定义好一个函数，当函数里面依赖的数据项发生变化时就会自动执行这段函数，这就是响应式！</p>
<p>数据驱动视图那就更容易理解了，既然当数据发生变化时可以执行一段函数，那么这段函数为什么不可以执行一段更新视图的操作呢：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; store, view &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-easy-state'</span>;

<span class="hljs-keyword">const</span> counter = store(&#123;
  <span class="hljs-attr">num</span>: <span class="hljs-number">0</span>,
  <span class="hljs-function"><span class="hljs-title">up</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.num++;
  &#125;
&#125;);

<span class="hljs-comment">// 这是一个响应式的组件, 当 counter.num 发生变化时会自动重新渲染组件</span>
<span class="hljs-keyword">const</span> UserComp = view(<span class="hljs-function">() =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;counter.up&#125;</span>></span>&#123;counter.num&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>react-easy-state</code>是他们(<em>尤雨溪借鉴的那个库</em>)专门针对<code>React</code>来进行封装的，不难看出<code>view</code>这个函数就是<code>observe</code>函数的一个变形，<code>observe</code>是要你传一个函数进去，你函数里面想执行啥就执行啥。而<code>view</code>是要你传一个组件进去，当数据变化时会去执行他们提前写好的一段更新逻辑，那不就跟你自己在<code>observe</code>里写一段更新操作是一样的嘛！用了这个库写出来的<code>React</code>就像是在写<code>Vue</code>一样。</p>
<h2 data-id="heading-3">源码</h2>
<p>理解了什么是响应式之后就可以方便我们来查看源码了，来看看<code>尤雨溪</code>是怎么仅用十几行代码就实现的<code>响应式</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> activeEffect

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
  subscribers = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
  <span class="hljs-function"><span class="hljs-title">depend</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (activeEffect) &#123;
      <span class="hljs-built_in">this</span>.subscribers.add(activeEffect)
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.subscribers.forEach(<span class="hljs-function"><span class="hljs-params">effect</span> =></span> effect())
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">watchEffect</span>(<span class="hljs-params">effect</span>) </span>&#123;
  activeEffect = effect
  effect()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现完了，再来看看该怎么用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> dep = <span class="hljs-keyword">new</span> Dep()

<span class="hljs-keyword">let</span> actualCount = <span class="hljs-number">0</span>
<span class="hljs-keyword">const</span> state = &#123;
  <span class="hljs-keyword">get</span> <span class="hljs-title">count</span>() &#123;
    dep.depend()
    <span class="hljs-keyword">return</span> actualCount
  &#125;,
  <span class="hljs-keyword">set</span> <span class="hljs-title">count</span>(<span class="hljs-params">newCount</span>) &#123;
    actualCount = newCount
    dep.notify()
  &#125;
&#125;

watchEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(state.count)
&#125;) <span class="hljs-comment">// 0</span>

state.count++ <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在观看这十几二十来行代码时都会觉得绕的话，那就说明你的基础属实不怎么样。因为明眼人一眼就可以看出来，这是一个非常经典的设计模式：<code>发布-订阅模式</code></p>
<h3 data-id="heading-4">发布-订阅模式</h3>
<p>如果不太了解<code>发布-订阅模式</code>的话，我们可以简单的来讲一下。但如果你对这些设计模式早已了如指掌，并且能够轻松读懂刚才那段代码的话，建议暂且先跳过这一段。</p>
<p>在<code>《JavaScript设计模式与开发实践》</code>一书中，作者<code>曾探</code>为<code>发布-订阅模式</code>举了一个十分生动形象的例子：</p>
<blockquote>
<p>小明最近看上了一套房子，到了售楼处之后才被告知，该楼盘的房子早已售罄。好在售楼 MM 告诉小明，不久之后还有一些尾盘推出，开发商正在办理相关手续，手续办好后便可以购买。但到底是什么时候，目前还没有人能够知道。</p>
</blockquote>
<blockquote>
<p>于是小明记下了售楼处的电话，以后每天都会打电话过去询问是不是已经到了购买时间。除了小明，还有小红、小强、小龙也会每天向售楼处咨询这个问题。一个星期过后，售楼 MM 决定辞职，因为厌倦了每天回答 1000 个相同内容的电话。</p>
</blockquote>
<blockquote>
<p>当然现实中没有这么笨的销售公司，实际上故事是这样的：小明离开之前，把电话号留在了售楼处。售楼 MM 答应他，新楼盘一推出就马上发信息通知小明。小红、小强和小龙也是一样，他们的电话号码都被记载售楼处的花名册上，新楼盘推出的时候，售楼 MM 会翻开花名册，遍历上面的电话号码，依次发送一条短信来通知他们。</p>
</blockquote>
<blockquote>
<p>在刚刚的例子中，发送短信通知就是一个典型的发布-订阅模式，小明、小红等购买者都是订阅者，他们订阅了房子开售的消息。售楼处作为发布者，会在合适的时候遍历花名册上的电话号码，依次给购房者发布消息。</p>
</blockquote>
<p>如果你曾经用过<code>xxx.addEventListener</code>这个函数为<code>DOM</code>添加过事件的话，那么实际上就已经算是用过<code>发布-订阅模式</code>啦！想一想是不是和售楼处的这个例子很相似：</p>
<ul>
<li>我们需要在一定条件下干一些事情</li>
<li>但我们不知道的是这个条件会在什么时间点成立</li>
<li>所以我们留下我们的函数</li>
<li>当条件成立时自动执行</li>
</ul>
<p>那么我们就来简单的模拟一下<code>addEventListener</code>发生的事情以便于大家理解<code>发布-订阅模式</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DOM</span> </span>&#123;
    #eventObj = &#123;
        <span class="hljs-attr">click</span>: [],
        <span class="hljs-attr">mouseover</span>: [],
        <span class="hljs-attr">mouseout</span>: [],
        <span class="hljs-attr">mousemove</span>: [],
        <span class="hljs-attr">keydown</span>: [],
        <span class="hljs-attr">keyup</span>: []
        <span class="hljs-comment">// 还有很多事件类型就不一一写啦</span>
    &#125;
    addEventListener (event, fn) &#123;
        <span class="hljs-built_in">this</span>.#eventObj[event].push(fn)
    &#125;
    removeEventListener (event, fn) &#123;
        <span class="hljs-keyword">const</span> arr = <span class="hljs-built_in">this</span>.#eventObj[event]
        <span class="hljs-keyword">const</span> index = arr.indexOf(fn)
        arr.splice(index, <span class="hljs-number">1</span>)
    &#125;
    click () &#123;
        <span class="hljs-built_in">this</span>.#eventObj.click.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn.apply(<span class="hljs-built_in">this</span>))
    &#125;
    mouseover () &#123;
        <span class="hljs-built_in">this</span>.#eventObj.mouseover.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn.apply(<span class="hljs-built_in">this</span>))
    &#125;
    <span class="hljs-comment">// 还有很多事件方法就不一一写啦</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来用一下试试：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> dom = <span class="hljs-keyword">new</span> DOM()

dom.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'点击啦！'</span>))
dom.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>) &#125;)

dom.addEventListener(<span class="hljs-string">'mouseover'</span>, <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'鼠标进入啦！'</span>))
dom.addEventListener(<span class="hljs-string">'mouseover'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>) &#125;)

<span class="hljs-comment">// 模拟点击事件</span>
dom.click() <span class="hljs-comment">// 依次打印出：'点击啦！' 和相应的 this 对象</span>

<span class="hljs-comment">// 模拟鼠标事件</span>
dom.mouseover() <span class="hljs-comment">// 依次打印出：'鼠标进入啦！' 和相应的 this 对象</span>

<span class="hljs-keyword">const</span> fn = <span class="hljs-function">() =></span> &#123;&#125;
dom.addEventListener(<span class="hljs-string">'click'</span>, fn)
<span class="hljs-comment">// 还可以移除监听</span>
dom.removeEventListener(<span class="hljs-string">'click'</span>, fn)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这个简单的案例应该就能够明白<code>发布-订阅模式</code>了吧？</p>
<p>我们来引用一下<code>《JavaScript设计模式与开发实践》</code>为<code>发布-订阅模式</code>总结出来的三个要点：</p>
<ol>
<li>首先要指定好谁充当发布者（比如售楼处）<code>在本例中是 dom 这个对象</code></li>
<li>然后给发布者添加一个缓存列表，用于存放回调函数以便通知订阅者（售楼处的花名册）<code>在本例中是 dom.#eventObj</code></li>
<li>最后发布消息的时候，发布者会遍历这个缓存列表，依次触发里面存放的订阅者回调函数（遍历花名册，挨个发短信）</li>
</ol>
<p><strong>记住这三个要点后，再来看一眼尤大的代码，看是不是符合这仨要点：</strong></p>
<ul>
<li><code>发布者</code>：dep 对象</li>
<li><code>缓存列表</code>：dep.subscribers</li>
<li><code>发布消息</code>：dep.notify()</li>
</ul>
<p>所以这是一个典型的<code>发布-订阅模式</code></p>
<h2 data-id="heading-5">增强版</h2>
<p><code>尤雨溪</code>的第一版代码实现的还是有些过于简陋了，首先用起来就很不方便，因为我们每次定义数据时都需要这么手写一遍<code>getter</code>和<code>setter</code>、手动的去执行一下依赖收集函数以及触发的函数。这个部分显然是可以继续进行封装的，那么再来看一眼<code>尤雨溪</code>实现的第二版：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> activeEffect

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
  subscribers = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
  <span class="hljs-function"><span class="hljs-title">depend</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (activeEffect) &#123;
      <span class="hljs-built_in">this</span>.subscribers.add(activeEffect)
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.subscribers.forEach(<span class="hljs-function"><span class="hljs-params">effect</span> =></span> effect())
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">watchEffect</span>(<span class="hljs-params">effect</span>) </span>&#123;
  activeEffect = effect
  effect()
  activeEffect = <span class="hljs-literal">null</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">raw</span>) </span>&#123;
  <span class="hljs-comment">// 使用 Object.defineProperty</span>
  <span class="hljs-comment">// 1. 遍历对象上存在的 key</span>
  <span class="hljs-built_in">Object</span>.keys(raw).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
    <span class="hljs-comment">// 2. 为每个 key 都创建一个依赖对象</span>
    <span class="hljs-keyword">const</span> dep = <span class="hljs-keyword">new</span> Dep()

    <span class="hljs-comment">// 3. 用 getter 和 setter 重写原对象的属性</span>
    <span class="hljs-keyword">let</span> realValue = raw[key]
    <span class="hljs-built_in">Object</span>.defineProperty(raw, key, &#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 4. 在 getter 和 setter 里调用依赖对象的对应方法</span>
        dep.depend()
        <span class="hljs-keyword">return</span> realValue
      &#125;,
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
        realValue = newValue
        dep.notify()
      &#125;
    &#125;)
  &#125;)
  <span class="hljs-keyword">return</span> raw
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这一版实现的就比上一版好多了，而且感觉<code>尤雨溪</code>在写这一版代码时比上一版更加认真。因为这版代码里有着详细的注释，所以肯定是认真讲解的一段代码。只不过原来的注释都是用英文写的，我给它翻译成了中文。</p>
<blockquote>
<p>不过各位看官请放心，除了注释被我翻译成了中文以外，其他的地方我一个字母都没有动过，就连空格都是保持的原汁原味的缩进，为的就是能够让大家看到的是<code>尤雨溪的一手代码</code>😋</p>
</blockquote>
<p>不难看出，这版代码在实现上用到了两种设计模式，它们分别是<code>代理模式</code>以及我们刚刚讲过的<code>发布-订阅模式</code>。所以说学好<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1v54y177Di" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1v54y177Di" ref="nofollow noopener noreferrer">设计模式</a>是多么重要的一件事情。如果对<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1v54y177Di" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1v54y177Di" ref="nofollow noopener noreferrer">设计模式</a>感兴趣的话可以去<a href="https://link.juejin.cn/?target=https%3A%2F%2Fspace.bilibili.com%2F1076738791%2Fchannel%2Fdetail%3Fcid%3D195775" target="_blank" rel="nofollow noopener noreferrer" title="https://space.bilibili.com/1076738791/channel/detail?cid=195775" ref="nofollow noopener noreferrer">B站</a>搜索<a href="https://link.juejin.cn/?target=https%3A%2F%2Fspace.bilibili.com%2F1076738791%2Fchannel%2Fdetail%3Fcid%3D195775" target="_blank" rel="nofollow noopener noreferrer" title="https://space.bilibili.com/1076738791/channel/detail?cid=195775" ref="nofollow noopener noreferrer">前端学不动</a>，目前正在连载<a href="https://link.juejin.cn/?target=https%3A%2F%2Fspace.bilibili.com%2F1076738791%2Fchannel%2Fdetail%3Fcid%3D195775" target="_blank" rel="nofollow noopener noreferrer" title="https://space.bilibili.com/1076738791/channel/detail?cid=195775" ref="nofollow noopener noreferrer">设计模式</a>中，个人感觉比慕课网那门卖<code>288</code>的 JavaScript 设计模式课讲的更清晰。</p>
<h3 data-id="heading-6">代理模式</h3>
<p>代理模式相对比较简单，都不用上代码，借用<code>《JavaScript设计模式核⼼原理与应⽤实践》</code>的作者<code>修言</code>举的一个非常有趣的例子就能让大家明白：</p>
<blockquote>
<p>我有个同事，技术很强，发型也很强。多年来因为沉迷 coding，耽误了人生大事。迫于寻找另一半的愿望比较急切，该同事同时是多个优质高端婚恋网站的注册VIP。工作之余，他常常给我们分享近期的<del>相亲</del>情感生活进展。</p>
</blockquote>
<blockquote>
<p>“你们看，这个妹子头像是不是超可爱！”同事哥这天发掘了一个新的婚介所，他举起手机，朝身边几位疯狂挥舞。</p>
</blockquote>
<blockquote>
<p>“哥，那是新垣结衣。。。”同事哥的同桌无奈地摇摇头，没有停下 coding 的手。</p>
</blockquote>
<blockquote>
<p>同事哥恢复了冷静，叹了口气：“这种婚恋平台的机制就是这么严格，一进来只能看到其它会员的姓名、年龄和自我介绍。要想看到本人的照片或者取得对方的联系方式，得先向平台付费成为 VIP 才行。哎，我又要买个 VIP 了。”</p>
</blockquote>
<blockquote>
<p>我一听，哇，这婚恋平台把代理模式玩挺 6 啊！大家想想，主体是同事 A，目标对象是新垣结衣头像的未知妹子。同事 A 不能直接与未知妹子进行沟通，只能通过第三方（婚介所）间接获取对方的一些信息，他能够获取到的信息和权限，取决于第三方愿意给他什么——这不就是典型的代理模式吗？</p>
</blockquote>
<h3 data-id="heading-7">用法</h3>
<p>这一版的响应式在使用起来就要舒服的多：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> state = reactive(&#123;
  <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
&#125;)

watchEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(state.count)
&#125;) <span class="hljs-comment">// 0</span>

state.count++ <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用方式基本上就和<code>Vue3</code>的用法一模一样了！可以看到响应式最核心的原理其实就是<code>发布-订阅</code>+<code>代理模式</code>。不过这还不是最终版，因为他用的是<code>ES5</code>的<code>Object.defineProperty</code>来做的<code>代理模式</code>，如果在不考虑兼容<code>IE</code>的情况下还是<code>ES6</code>的<code>Proxy</code>更适合做<code>代理</code>，因为<code>Proxy</code>翻译过来就是<code>代理权</code>、<code>代理人</code>的意思。所以<code>Vue3</code>采用了<code>Proxy</code>来重构整个响应式代码，我们来看一下<code>尤雨溪</code>写出来的最终版(<code>Proxy</code>版)</p>
<h2 data-id="heading-8">Proxy 版</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> activeEffect

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
  subscribers = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-built_in">this</span>._value = value
  &#125;

  <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
    <span class="hljs-built_in">this</span>.depend()
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._value
  &#125;

  <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">value</span>) &#123;
    <span class="hljs-built_in">this</span>._value = value
    <span class="hljs-built_in">this</span>.notify()
  &#125;

  <span class="hljs-function"><span class="hljs-title">depend</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (activeEffect) &#123;
      <span class="hljs-built_in">this</span>.subscribers.add(activeEffect)
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.subscribers.forEach(<span class="hljs-function">(<span class="hljs-params">effect</span>) =></span> &#123;
      effect()
    &#125;)
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">watchEffect</span>(<span class="hljs-params">effect</span>) </span>&#123;
  activeEffect = effect
  effect()
  activeEffect = <span class="hljs-literal">null</span>
&#125;

<span class="hljs-comment">// proxy version</span>
<span class="hljs-keyword">const</span> reactiveHandlers = &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key</span>)</span> &#123;
    <span class="hljs-keyword">const</span> value = getDep(target, key).value
    <span class="hljs-keyword">if</span> (value && <span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'object'</span>) &#123;
      <span class="hljs-keyword">return</span> reactive(value)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> value
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, value</span>)</span> &#123;
    getDep(target, key).value = value
  &#125;
&#125;

<span class="hljs-keyword">const</span> targetToHashMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getDep</span>(<span class="hljs-params">target, key</span>) </span>&#123;
  <span class="hljs-keyword">let</span> depMap = targetToHashMap.get(target)
  <span class="hljs-keyword">if</span> (!depMap) &#123;
    depMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
    targetToHashMap.set(target, depMap)
  &#125;

  <span class="hljs-keyword">let</span> dep = depMap.get(key)
  <span class="hljs-keyword">if</span> (!dep) &#123;
    dep = <span class="hljs-keyword">new</span> Dep(target[key])
    depMap.set(key, dep)
  &#125;

  <span class="hljs-keyword">return</span> dep
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, reactiveHandlers)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这一版的代码又比上一版更加复杂了点，但在用法上还是和上一版一模一样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> state = reactive(&#123;
  <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
&#125;)

watchEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(state.count)
&#125;) <span class="hljs-comment">// 0</span>

state.count++ <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来重点讲解一下最终版的代码，这一版代码才是最<code>优秀</code>的。麻雀虽小，五脏俱全，不仅做了最基本的<code>发布-订阅模式</code>+<code>代理模式</code>，而且还用到了许多小技巧来做了性能方面的优化。</p>
<h3 data-id="heading-9">详解</h3>
<p>首先尤大定义了一个名为<code>activeEffect</code>的空变量，用于存放<code>watchEffect</code>传进来的函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义一个暂时存放 watchEffect 传进来的参数的变量</span>
<span class="hljs-keyword">let</span> activeEffect
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来定义了一个名为<code>Dep</code>的类，这个<code>Dep</code>应该是<code>Dependence</code>的缩写，意为<code>依赖</code>。实际上就相当于<code>发布-订阅模式</code>中的发布者类：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义一个 Dep 类，该类将会为每一个响应式对象的每一个键生成一个发布者实例</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span> </span>&#123;
  <span class="hljs-comment">// 用 Set 做缓存列表以防止列表中添加多个完全相同的函数</span>
  subscribers = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()

  <span class="hljs-comment">// 构造函数接受一个初始化的值放在私有变量内</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-built_in">this</span>._value = value
  &#125;

  <span class="hljs-comment">// 当使用 xxx.value 获取对象上的 value 值时</span>
  <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>() &#123;
    <span class="hljs-comment">// 代理模式 当获取对象上的value属性的值时将会触发 depend 方法</span>
    <span class="hljs-built_in">this</span>.depend()

    <span class="hljs-comment">// 然后返回私有变量内的值</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._value
  &#125;

  <span class="hljs-comment">// 当使用 xxx.value = xxx 修改对象上的 value 值时</span>
  <span class="hljs-keyword">set</span> <span class="hljs-title">value</span>(<span class="hljs-params">value</span>) &#123;
    <span class="hljs-comment">// 代理模式 当修改对象上的value属性的值时将会触发 notify 方法</span>
    <span class="hljs-built_in">this</span>._value = value
    <span class="hljs-comment">// 先改值再触发 这样保证触发的时候用到的都是已经修改后的新值</span>
    <span class="hljs-built_in">this</span>.notify()
  &#125;

  <span class="hljs-comment">// 这就是我们常说的依赖收集方法</span>
  <span class="hljs-function"><span class="hljs-title">depend</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 如果 activeEffect 这个变量为空 就证明不是在 watchEffect 这个函数里面触发的 get 操作</span>
    <span class="hljs-keyword">if</span> (activeEffect) &#123;
      <span class="hljs-comment">// 但如果 activeEffect 不为空就证明是在 watchEffect 里触发的 get 操作</span>
      <span class="hljs-comment">// 那就把 activeEffect 这个存着 watchEffect 参数的变量添加进缓存列表中</span>
      <span class="hljs-built_in">this</span>.subscribers.add(activeEffect)
    &#125;
  &#125;

  <span class="hljs-comment">// 更新操作 通常会在值被修改后调用</span>
  <span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 遍历缓存列表里存放的函数 并依次触发执行</span>
    <span class="hljs-built_in">this</span>.subscribers.forEach(<span class="hljs-function">(<span class="hljs-params">effect</span>) =></span> &#123;
      effect()
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之前两版尤大都是在外头定义了一个变量用于保存<code>响应式对象</code>每一个键所对应的值，而这次是直接把值放进了<code>Dep</code>类的定义里，定义成了<code>getter</code>和<code>setter</code>，在获取值时会进行依赖收集操作，而在修改值时会进行更新操作。</p>
<p>接下来又定义了一个跟<code>Vue3</code>的<code>watchEffect</code>名称一样的函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 模仿 Vue3 的 watchEffect 函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">watchEffect</span>(<span class="hljs-params">effect</span>) </span>&#123;
  <span class="hljs-comment">// 先把传进来的函数放入到 activeEffect 这个变量中</span>
  activeEffect = effect

  <span class="hljs-comment">// 然后执行 watchEffect 里面的函数</span>
  effect()

  <span class="hljs-comment">// 最后把 activeEffect 置为空值</span>
  activeEffect = <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在使用时不是会在这个函数里面再传进一个函数么：</p>
<pre><code class="hljs language-js copyable" lang="js">watchEffect(<span class="hljs-function">() =></span> state.xxx)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数就被赋值给了<code>activeEffect</code>这个变量上面去，然后立刻执行这个函数，一般来说这个函数里面都会有一些<code>响应式对象</code>的对吧？既然有，那就会触发<code>getter</code>去进行依赖收集操作，而依赖收集则是判断了<code>activeEffect</code>这个变量有没有值，如果有，那就把它添加进缓存列表里。等到执行完这个函数后，就立即将<code>activeEffect</code>这个变量置为空值，防止不在<code>watchEffect</code>这个函数中触发<code>getter</code>的时候也执行依赖收集操作。</p>
<p>接下来就是定义了一个<code>Proxy</code>代理的处理对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> reactiveHandlers = &#123;
  <span class="hljs-comment">// 当触发 get 操作时</span>
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, key</span>)</span> &#123;
    <span class="hljs-comment">// 先调用 getDep 函数取到里面存放的 value 值</span>
    <span class="hljs-keyword">const</span> value = getDep(target, key).value

    <span class="hljs-comment">// 如果 value 是对象的话</span>
    <span class="hljs-keyword">if</span> (value && <span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'object'</span>) &#123;
      <span class="hljs-comment">// 那就把 value 也变成一个响应式对象</span>
      <span class="hljs-keyword">return</span> reactive(value)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 如果 value 只是基本数据类型的话就直接将值返回</span>
      <span class="hljs-keyword">return</span> value
    &#125;
  &#125;,
  <span class="hljs-comment">// 当触发 set 操作时</span>
  <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, value</span>)</span> &#123;
    <span class="hljs-comment">// 调用 getDep 函数并将里面存放的 value 值重新赋值成 set 操作的值</span>
    getDep(target, key).value = value
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果对<code>Proxy</code>不是很了解的话，建议看看阮一峰的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Fproxy" target="_blank" rel="nofollow noopener noreferrer" title="https://es6.ruanyifeng.com/#docs/proxy" ref="nofollow noopener noreferrer">《ES6入门教程》</a>，写的还是不错的。</p>
<p>刚刚那个对象在<code>get</code>和<code>set</code>操作中都用到了<code>getDep</code>这个函数，这个函数时在后面定义的，他会用到一个叫<code>targetToHashMap</code>的<code>WeakMap</code>数据结构来存储数据：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义一个 WeakMap 数据类型 用于存放 reactive 定义的对象以及他们的发布者对象集</span>
<span class="hljs-keyword">const</span> targetToHashMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来就是定义<code>getDep</code>函数啦：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义 getDep 函数 用于获取 reactive 定义的对象所对应的发布者对象集里的某一个键对应的发布者对象</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getDep</span>(<span class="hljs-params">target, key</span>) </span>&#123;
  <span class="hljs-comment">// 获取 reactive 定义的对象所对应的发布者对象集</span>
  <span class="hljs-keyword">let</span> depMap = targetToHashMap.get(target)

  <span class="hljs-comment">// 如果没获取到的话</span>
  <span class="hljs-keyword">if</span> (!depMap) &#123;
    <span class="hljs-comment">// 就新建一个空的发布者对象集</span>
    depMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
    <span class="hljs-comment">// 然后再把这个发布者对象集存进 WeakMap 里</span>
    targetToHashMap.set(target, depMap)
  &#125;

  <span class="hljs-comment">// 再获取到这个发布者对象集里的某一个键所对应的发布者对象</span>
  <span class="hljs-keyword">let</span> dep = depMap.get(key)

  <span class="hljs-comment">// 如果没获取到的话</span>
  <span class="hljs-keyword">if</span> (!dep) &#123;
    <span class="hljs-comment">// 就新建一个发布者对象并初始化赋值</span>
    dep = <span class="hljs-keyword">new</span> Dep(target[key])
    <span class="hljs-comment">// 然后将这个发布者对象放入到发布者对象集里</span>
    depMap.set(key, dep)
  &#125;

  <span class="hljs-comment">// 最后返回这个发布者对象</span>
  <span class="hljs-keyword">return</span> dep
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个地方就稍微有点绕了，我们来上图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/702a6f2449b14e358ca6886f7690a049~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>每一个传进<code>reactive</code>里去的对象，都会被存在<code>WeakMap</code>里的键上。而每一个键所对应的值，就是一个<code>Map</code>：</p>
<pre><code class="hljs language-js copyable" lang="js">                                    <span class="hljs-comment">//     targetToHashMap: &#123;</span>
<span class="hljs-keyword">const</span> obj1 = reactive(&#123; <span class="hljs-attr">num</span>: <span class="hljs-number">1</span> &#125;)   <span class="hljs-comment">//        &#123; num: 1 &#125;: new Map(),</span>
<span class="hljs-keyword">const</span> obj2 = reactive(&#123; <span class="hljs-attr">num</span>: <span class="hljs-number">2</span> &#125;)   <span class="hljs-comment">//        &#123; num: 2 &#125;: new Map(),</span>
<span class="hljs-keyword">const</span> obj3 = reactive(&#123; <span class="hljs-attr">num</span>: <span class="hljs-number">3</span> &#125;)   <span class="hljs-comment">//        &#123; num: 3 &#125;: new Map()</span>
                                    <span class="hljs-comment">//     &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那值(<em>Map</em>)里存的又是什么呢？存的是：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cd17612f0ad47d6b34ffa38902cf9df~tplv-k3u1fbpfcp-watermark.image" alt="WX20210729-192101.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>假设我们<code>reactive</code>了一个对象<code>&#123; a: 0, b: 1, c: 2 &#125;</code>，那么<code>Map</code>里面存的就是：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">'a'</span>: <span class="hljs-keyword">new</span> Dep(<span class="hljs-number">0</span>),
  <span class="hljs-string">'b'</span>: <span class="hljs-keyword">new</span> Dep(<span class="hljs-number">1</span>),
  <span class="hljs-string">'c'</span>: <span class="hljs-keyword">new</span> Dep(<span class="hljs-number">2</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是把对象的键放到<code>Map</code>的键上，然后在用<code>new Dep</code>创建一个发布者对象，再把值传给<code>Dep</code>。Vue3 之所以性能比 Vue2 强很多的其中一个非常重要的优化点就是这个<code>Proxy</code>。并不是说<code>Proxy</code>的性能就比<code>Object.defineProperty</code>高多少，而是说在<code>Proxy</code>里的处理方式比<code>Vue2</code>时期的好很多：<code>Vue2</code>的响应式是一上来就一顿<code>遍历</code>+<code>递归</code>把你定义的所有数据全都变成响应式的，这就会导致如果页面上有很多很复杂的数据结构时，用<code>Vue2</code>写的页面就会白屏一小段时间。毕竟<code>遍历</code>+<code>递归</code>还是相对很慢的一个操作嘛！</p>
<p>而<code>React</code>就没有这个毛病，当然<code>Vue3</code>也不会有这个毛病。从代码中可以看出，当我们获取对象上的某个键对应的值时，会先判断这个值到底有没有对应的发布者对象，没有的话再创建发布者对象。而且当获取到的值是引用类型时再把这个值变成<code>响应式对象</code>，等你用到了响应式对象里的值时再去新建发布者对象。</p>
<blockquote>
<p>总结成一句话就是：<code>Vue3</code>是用到哪部分的数据的时候，再把数据变成响应式的。而<code>Vue2</code>则是不管三七二十一，刚开局就全都给你变成响应式数据。</p>
</blockquote>
<p>最后一步就是定义<code>reactive</code>函数啦：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 模仿 Vue3 的 reactive 函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-comment">// 返回一个传进来的参数对象的代理对象 以便使用代理模式拦截对象上的操作并应用发布-订阅模式</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, reactiveHandlers)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">流程图</h3>
<p>为了便于大家理解，我们使用一遍<code>reactive</code>和<code>watchEffect</code>函数，然后顺便看看到底发生了什么：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fa8673d298648a69ab18665ef80e910~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-132843.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先我们用<code>reactive</code>函数定义了一个对象<code>&#123; num: 0 &#125;</code>，这个对象会传给<code>Proxy</code>的第一个参数，此时还并没有发生什么事情，那么接下来我们就在<code>watchEffect</code>里打印一下这个对象的<code>num</code>属性：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbc1c6edddce460baf2d185c0c9c6a3e~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-133331.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时传给<code>watchEffect</code>的这个函数会赋值给<code>actibveEffect</code>这个变量上去，然后立即执行这个函数：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5690b6593c3b46d488a17ce2473ed7bb~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-133925.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在执行的过程中发现有<code>get</code>操作，于是被<code>Proxy</code>所拦截，走到了<code>get</code>这一步：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcf9a0c533b74acc9e74867845acc899~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-140428.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于在<code>get</code>操作中需要用<code>getDep</code>函数，于是又把<code>&#123; num: 0 &#125;</code>传给了<code>getDep</code>，key 是 num，所以相当于<code>getDep(&#123; num: 0 &#125;, 'num')</code>。进入到<code>getDep</code>函数体内，需要用<code>targetToHashMap</code>来获取<code>&#123; num: 0 &#125;</code>这个键所对应的值，但目前<code>targetToHashMap</code>是空的，所以根本获取不到任何内容。于是进入判断，新建一个<code>Map</code>赋值给<code>targetToHashMap</code>，相当于：<code>targetToHashMap.set(&#123; num: 0 &#125;, new Map())</code>，紧接着就是获取这个<code>Map</code>的<code>key</code>所对应的值：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/656e507827df4d34bf02796eeea2ded9~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-141344.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于<code>Map</code>也是空的，所以还是获取不到值，于是进入判断，新建一个<code>Dep</code>对象：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a403ddf3c0b441a596bf0c692c1a1b87~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-141809.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于是用<code>getDep(...xxx).value</code>来获取到这个对象的<code>value</code>属性，所以就会触发<code>getter</code>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0013639870c4c3b9697ce8fb51d408b~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-142346.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>顺着<code>getter</code>我们又来到了<code>depend</code>方法中，由于<code>activeEffect</code>有值，所以进入判断，把<code>activeEffect</code>加入到<code>subscribes</code>这个<code>Set</code>结构中。此时依赖收集部分就暂且告一段落了，接下来我们来改变<code>obj.num</code>的值，看看都会发生些什么：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99e316ee2c454c3e86246dc23dacec46~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-144029.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先会被<code>Proxy</code>拦截住<code>set</code>操作，然后调用<code>getDep</code>函数：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9facf7196d36496faf4b77150ed21e40~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-143810.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>获取到<code>dep</code>对象后，就会修改它的<code>value</code>属性，从而触发<code>setter</code>操作：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8efbbe4b8f0d444880e2847d6e6078b5~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-144603.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后我们来到了通知(<em>notify</em>)阶段，在通知阶段会找到我们的缓存列表(<em>subscribers</em>)，然后依次触发里面的函数：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/593a67ca5b5c42c9b6eeee2819cde8fb~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-144912.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么此时就会运行<code>() => console.log(obj.num)</code>这个函数，你以为这就完了吗？当然没有！由于运行了<code>obj.num</code>这个操作，所以又会触发<code>get</code>操作被<code>Proxy</code>拦截：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf63451cd1ea46638e84d9f73aa34168~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-145721.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>获取到我们之前创建过的发布者对象后，又会触发发布者对象的<code>getter</code>操作：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bdafafc9ced4599a37569ba963a8e46~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-150316.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一顿绕，绕到<code>depend</code>方法时，我们需要检测一下<code>activeEffect</code>这个变量：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1d9f3f28d59410aa9dbcdaf3dd1cd7e~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-150635.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于不会进入到判断里面去，所以执行了个寂寞(<em>啥也没执行</em>)，那么接下来的代码便是：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe728e3b20304d4f87b7b829afdb8451~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-151831.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最终打印出了<code>10</code>。</p>
<h1 data-id="heading-11">结语</h1>
<p>没想到短短这么七十来行代码这么绕吧？所以说抽丝剥茧的学习方法有多重要。如果直接看源码的话，这里面肯定还会有各种各样的判断。比如<code>watchEffect</code>现在没做任何的判断对吧？那么当我们给<code>watchEffect</code>传了一个不是函数的参数时会怎样？当我们给<code>reactive</code>对象传数组时又会怎样？当传<code>Map</code>、<code>Set</code>时呢？传基本数据类型时呢？而且即使现在我们不考虑这些情况，就传一个对象，里面不要有数组等什么其他的东西，<code>watchEffect</code>也只传函数。那么其实在使用体验上还是有一点与<code>Vue3</code>的<code>watchEffect</code>不同的地方，那就是不能在<code>watchEffect</code>里面改变响应式对象的值：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34ab2a636bc347ed97e561a4fd3f20c6~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-152653.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而写成这样就没有问题：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44c9d3598f7745d0949ac5d5269985eb~tplv-k3u1fbpfcp-watermark.image" alt="WX20210730-152902.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可是在<code>Vue3</code>的<code>watchEffect</code>里就不会出现这样的状况。这是因为如果在<code>watchEffect</code>里对响应式对象进行赋值操作的话就又会触发<code>set</code>操作，从而被<code>Proxy</code>拦截，然后又绕到<code>notify</code>的方法上面去了，<code>notify</code>又会把<code>watchEffect</code>里的函数运行一遍，结果又发现里面有<code>set</code>操作(<em>因为是同一段代码嘛</em>)，然后又会去运行<code>notify</code>方法，继续触发<code>set</code>操作造成死循环。</p>
<p>所以我们还需要考虑到这种死循环的情况，但如果真的考虑的这么全面的话，那相信代码量也相当大了，我们会被进一步绕晕。所以先吃透这段代码，然后慢慢的我们再来看真正的源码都是怎么处理这些情况的。或者也可以先不看源码，自己思考一下这些问题该如何去处理，然后写出自己的逻辑来，测试没有问题后再去跟<code>Vue3</code>的源码进行对比，看看自己实现的和尤雨溪实现的方式有何异同。</p>
<blockquote>
<p>本篇文章到这里就要告一段落了，但还没完，这只是<code>响应式部分</code>。之后还有<code>虚拟DOM</code>、<code>diff算法</code>、<code>组件化</code>、<code>根组件挂载</code>等部分。</p>
</blockquote>
<p>如果等不及看下一篇解析文章的话，也可以直接<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fcollection%2FDkxpbE" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/collection/DkxpbE" ref="nofollow noopener noreferrer">点击这个链接</a>进入到<code>codepen</code>里自行钻研<code>尤雨溪</code>写的代码。代码量很少，是我们学习<code>Vue3</code>原理的<code>绝佳资料</code>！学会了原理之后哪怕不去看真正的源码，在面试的时候都可以跟面试官吹两句。因为毕竟不会有哪个面试官考察源码时会问：你来说一下<code>Vue3</code>的某某文件的第<code>996</code>行代码写的是什么？考察肯定也重点考察的是原理，很少会去考察各种判断参数的边界情况处理。所以<code>点赞</code>+<code>关注</code>，跟着<code>尤雨溪</code>学源码不迷路！</p>
<h2 data-id="heading-12">往期精彩文章</h2>
<ul>
<li><a href="https://juejin.cn/post/6986453616517185567" target="_blank" title="https://juejin.cn/post/6986453616517185567">《产品经理：能不能让这串数字滚动起来？》</a></li>
<li><a href="https://juejin.cn/post/6979042510400126983" target="_blank" title="https://juejin.cn/post/6979042510400126983">《产品经理：鸿蒙那个开场动画挺帅的 给咱们页面也整一个呗》</a></li>
<li><a href="https://juejin.cn/post/6865591917279870990" target="_blank" title="https://juejin.cn/post/6865591917279870990">《不依赖任何库打造属于自己的可视化数据地图》</a></li>
<li><a href="https://juejin.cn/post/6946756821675671566" target="_blank" title="https://juejin.cn/post/6946756821675671566">《[译]尤雨溪：Vue3将不会支持IE11 精力会投入到Vue2.7》</a></li>
<li><a href="https://juejin.cn/post/6856668819344392206" target="_blank" title="https://juejin.cn/post/6856668819344392206">《Vue超好玩的新特性：在CSS中引入JS变量》</a></li>
<li><a href="https://juejin.cn/post/6912374170743472135" target="_blank" title="https://juejin.cn/post/6912374170743472135">《什么？仅靠H5标签就能实现收拉效果？》</a></li>
<li><a href="https://juejin.cn/post/6910828161030701064" target="_blank" title="https://juejin.cn/post/6910828161030701064">《整治GitHub不文明现象！微软推出评论区！》</a></li>
<li><a href="https://juejin.cn/post/6899439012331651079" target="_blank" title="https://juejin.cn/post/6899439012331651079">《Vue 3.0.3 : 新增CSS变量传递以及最新的Ref提案》</a></li>
<li><a href="https://juejin.cn/post/6893875394584248334" target="_blank" title="https://juejin.cn/post/6893875394584248334">《双11小黑盒很炫酷？咱们用CSS变量来改进一下！》</a></li>
<li><a href="https://juejin.cn/post/6886770985060532231" target="_blank" title="https://juejin.cn/post/6886770985060532231">《千万别小瞧九宫格 一道题就能让候选人原形毕露！》</a></li>
<li><a href="https://juejin.cn/post/6884971597498613768" target="_blank" title="https://juejin.cn/post/6884971597498613768">《移动端布局面试题 全面考察你的CSS功底(居中篇)》</a></li>
<li><a href="https://juejin.cn/post/6877430232987467789" target="_blank" title="https://juejin.cn/post/6877430232987467789">《将原型对象设置成Proxy后的一系列迷惑行为》</a></li>
<li><a href="https://juejin.cn/post/6868260498417123335" target="_blank" title="https://juejin.cn/post/6868260498417123335">《Vue超好玩的新特性：DOM传送门》</a></li>
<li><a href="https://juejin.cn/post/6844904030641078280" target="_blank" title="https://juejin.cn/post/6844904030641078280">《在Vue项目中使用React超火的CSS-in-JS库: styled-components》</a></li>
<li><a href="https://juejin.cn/post/6844904015004696583" target="_blank" title="https://juejin.cn/post/6844904015004696583">《终于轮到Vue来带给React灵感了？》</a></li>
<li><a href="https://juejin.cn/post/6844904145275584519" target="_blank" title="https://juejin.cn/post/6844904145275584519">《Vue3在IOS下的一个小坑》</a></li>
<li><a href="https://juejin.cn/post/6844904182357426190" target="_blank" title="https://juejin.cn/post/6844904182357426190">《新版vue-router的hooks用法》</a></li>
<li><a href="https://juejin.cn/post/6844903823937372174" target="_blank" title="https://juejin.cn/post/6844903823937372174">《[译]尤雨溪：Vue3的设计过程》</a></li>
<li><a href="https://juejin.cn/post/6844904159976620045" target="_blank" title="https://juejin.cn/post/6844904159976620045">《Node之父重构的Deno终于发布了，它终究会取代Node吗？》</a></li>
</ul></div>  
</div>
            