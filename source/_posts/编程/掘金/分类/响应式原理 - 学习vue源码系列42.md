
---
title: '响应式原理 - 学习vue源码系列4.2'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec9be50979844f2499291083177ecae3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 02:26:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec9be50979844f2499291083177ecae3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>决定跟着<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoding.imooc.com%2Flesson%2F228.html%23mid%3D14869" target="_blank" rel="nofollow noopener noreferrer" title="https://coding.imooc.com/lesson/228.html#mid=14869" ref="nofollow noopener noreferrer">黄轶老师的 vue2 源码课程</a>好好学习下<code>vue2</code>的源码，学习过程中，尽量输出自己的所得，提高学习效率，水平有限，不对的话请指正~</p>
<p>将<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue" ref="nofollow noopener noreferrer">vue 的源码</a>clone 到本地，切换到分支<code>2.6</code>。</p>
<h2 data-id="heading-0">Introduction</h2>
<p>前面说了，vue 是怎么实现<strong>初始化</strong>数据渲染和组件化的，但当数据变动的时候，dom 又是怎么更新的呢。</p>
<h2 data-id="heading-1">先看个 demo</h2>
<p>数据变更:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>hello<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假设希望点击之后能将<code>hello</code>变成<code>hello world</code>的话，寻常怎么操作。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1.修改数据</span>
<span class="hljs-keyword">const</span> text = <span class="hljs-string">"hello world"</span>;
<span class="hljs-comment">// 2.获取dom，监听事件</span>
<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#app"</span>).onclick = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 3.手动操作dom重新渲染</span>
  app.innerHTML = text;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果需要多次修改的话，就不得不<strong>每次</strong>都手动操作 dom，重新渲染。</p>
<p>而 vue，去掉了<code>手动操作dom</code>，根据数据变化<strong>自动</strong>操作 dom。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"changeMsg"</span>></span>&#123;&#123; message &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"/Users/zhm/mygit/vue/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">var</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">"Hello Vue!"</span>,
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">changeMsg</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 这边只是 改变了数据，其余的由vue本身去更新dom，重新渲染</span>
        <span class="hljs-built_in">this</span>.message = <span class="hljs-string">"Hello World!"</span>;
      &#125;,
    &#125;,
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">响应式对象</h2>
<p>其实<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2FdefineProperty" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty" ref="nofollow noopener noreferrer"><code>Object.defineProperty</code></a>应该都听过了，嗯，主要就是用这个属性。</p>
<p>普通获取对象属性，设置对象属性都可以用这个，但是比较麻烦，所以一般分场景使用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** 普通创建属性的方式： **/</span>
<span class="hljs-keyword">var</span> obj = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;;

<span class="hljs-comment">/** defineProperty创建、获取和设置属性的方式： **/</span>
<span class="hljs-keyword">var</span> obj = &#123;&#125;;
<span class="hljs-comment">// ！注意需要另设一个变量，存储属性的值。</span>
<span class="hljs-keyword">let</span> value = <span class="hljs-number">1</span>;
<span class="hljs-built_in">Object</span>.defineProperty(obj, <span class="hljs-string">"a"</span>, &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"get"</span>);
    <span class="hljs-keyword">return</span> value;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"set"</span>);
    value = newValue;
  &#125;,
&#125;);

<span class="hljs-comment">/* 当然获取属性和设置的话，是一样的 */</span>
<span class="hljs-comment">// 获取</span>
<span class="hljs-built_in">console</span>.log(obj.a);
<span class="hljs-comment">// 设置</span>
obj.a = <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec9be50979844f2499291083177ecae3~tplv-k3u1fbpfcp-zoom-1.image" alt="reactive_1" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>Object.defineProperty</code>的核心就是<code>get</code>和<code>set</code>，因为是函数，所以能做很多事。</p>
<p>所谓的劫持，每次<strong>获取/设置</strong>属性的时候，都会执行<code>get/set</code>函数，既然是函数，自然能做一些别的事情。</p>
<blockquote>
<p>所谓的响应式对象，当对象的某属性有<code>get/set</code>，就称为响应式对象。</p>
</blockquote>
<h2 data-id="heading-3">简版的响应式Vue</h2>
<p>先写个简版的响应式<code>Vue</code>，大致有个印象，真实的源码处理的情景比较多，看懂简版的，再看源码，不容易迷路。。。</p>
<p>主要做了以下几件事：</p>
<ul>
<li>用<code>vm._data</code>指向<code>options.data</code></li>
<li>将<code>vm._data</code>上面的属性都代理到<code>vm</code>上</li>
<li><code>vm._data.__ob__</code>指向Observer实例，而这个实例的value是data的响应式</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123; <span class="hljs-attr">data</span>: &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125; &#125;);
<span class="hljs-built_in">console</span>.dir(vm);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Vue</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.vm = <span class="hljs-built_in">this</span>;
  <span class="hljs-built_in">this</span>.$options = options;
  <span class="hljs-comment">/* this._init() initState()开始 */</span>
  initData(<span class="hljs-built_in">this</span>);
  <span class="hljs-comment">/* this._init() initState()结束 */</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initData</span>(<span class="hljs-params">vm</span>) </span>&#123;
  <span class="hljs-keyword">let</span> data = vm.$options.data;
  vm._data = data;
  <span class="hljs-comment">// 将data上面的属性直接挂在vm上</span>
  <span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
    <span class="hljs-comment">/* proxy(vm, "_data", key) 开始 */</span>
    <span class="hljs-built_in">Object</span>.defineProperty(vm, key, &#123;
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> vm._data[key];
      &#125;,
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
        vm.data[key] = newValue;
      &#125;,
    &#125;);
    <span class="hljs-comment">/* proxy(vm, "_data", key) 结束 */</span>
  &#125;);

  <span class="hljs-comment">/* observe(data) 开始 */</span>
  data.__ob__ = data.__ob__ || <span class="hljs-keyword">new</span> Observer(data);
  <span class="hljs-comment">/* observe(data) 结束 */</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Observer</span>(<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.value = data;
  <span class="hljs-comment">// this.dep = new Dep();</span>
  data.__ob__ = <span class="hljs-built_in">this</span>;
  <span class="hljs-built_in">Object</span>.keys(data).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
    defineReactive(data, key);
  &#125;);
&#125;
<span class="hljs-comment">// defineReactive将 obj.x 这种定义属性的方式  变成Object.defineProperty(obj, 'x' , &#123;get()&#123;&#125;&#125;</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span>(<span class="hljs-params">data, key</span>) </span>&#123;
  <span class="hljs-comment">// const dep = new Dep();</span>
  <span class="hljs-keyword">let</span> value = data[key];

  <span class="hljs-built_in">Object</span>.defineProperty(data, key, &#123;
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveGetter</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// dep.depend();</span>
      <span class="hljs-keyword">return</span> value;
    &#125;,
    <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveSetter</span>(<span class="hljs-params">newValue</span>) </span>&#123;
      <span class="hljs-comment">// dep.notify();</span>
      value = newValue;
    &#125;,
  &#125;);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15b800d212a140ba9ecd96e54815224c~tplv-k3u1fbpfcp-zoom-1.image" alt="reactive_2" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">initState</h2>
<p>Vue 的构造函数，开始就是<code>this._init(..)</code>，而<code>Vue.prototype._init = function()&#123;initState(this)&#125;</code>。</p>
<p>这里的<code>initState</code>就是让<code>Vue</code>的<strong>实例</strong>变成响应式对象的关键，这个方法就是对<code>options</code>进行各种初始化的操作，而本文的重点是对<code>data/props</code>的处理。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/core/instance/state.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initState</span>(<span class="hljs-params">vm: Component</span>) </span>&#123;
  vm._watchers = [];
  <span class="hljs-keyword">const</span> opts = vm.$options;
  <span class="hljs-keyword">if</span> (opts.props) initProps(vm, opts.props);
  <span class="hljs-keyword">if</span> (opts.methods) initMethods(vm, opts.methods);
  <span class="hljs-keyword">if</span> (opts.data) &#123;
    initData(vm);
  &#125; <span class="hljs-keyword">else</span> &#123;
    observe((vm._data = &#123;&#125;), <span class="hljs-literal">true</span> <span class="hljs-comment">/* asRootData */</span>);
  &#125;
  <span class="hljs-keyword">if</span> (opts.computed) initComputed(vm, opts.computed);
  <span class="hljs-keyword">if</span> (opts.watch && opts.watch !== nativeWatch) &#123;
    initWatch(vm, opts.watch);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">props 的处理</h3>
<p>先看<code>initProps</code>，主要其实就是</p>
<ul>
<li>遍历<code>options.props</code></li>
<li>每个 prop 变成响应式（set/get），且每个 prop，也同步到<code>vm._props.xx</code></li>
<li>通过<code>proxy</code>把<code>vm._props.xxx</code> 的访问代理到 <code>vm.xxx</code> 上</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/core/instance/state.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initProps</span>(<span class="hljs-params">vm: Component, propsOptions: <span class="hljs-built_in">Object</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> propsData = vm.$options.propsData || &#123;&#125;;
  <span class="hljs-keyword">const</span> props = (vm._props = &#123;&#125;);
  <span class="hljs-comment">// cache prop keys so that future props updates can iterate using Array</span>
  <span class="hljs-comment">// instead of dynamic object key enumeration.</span>
  <span class="hljs-keyword">const</span> keys = (vm.$options._propKeys = []);
  <span class="hljs-keyword">const</span> isRoot = !vm.$parent;
  <span class="hljs-comment">// root instance props should be converted</span>
  <span class="hljs-keyword">if</span> (!isRoot) &#123;
    toggleObserving(<span class="hljs-literal">false</span>);
  &#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> propsOptions) &#123;
    keys.push(key);
    <span class="hljs-keyword">const</span> value = validateProp(key, propsOptions, propsData, vm);
    defineReactive(props, key, value);
    <span class="hljs-comment">// static props are already proxied on the component's prototype</span>
    <span class="hljs-comment">// during Vue.extend(). We only need to proxy props defined at</span>
    <span class="hljs-comment">// instantiation here.</span>
    <span class="hljs-keyword">if</span> (!(key <span class="hljs-keyword">in</span> vm)) &#123;
      proxy(vm, <span class="hljs-string">`_props`</span>, key);
    &#125;
  &#125;
  toggleObserving(<span class="hljs-literal">true</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">data 的处理</h3>
<p>data 的初始化也做了两件事：</p>
<ul>
<li>遍历<code>data</code>对象，每一个<code>vm._data.xx</code>通过<code>proxy</code>代理到<code>vm._data</code></li>
<li>调用<code>observe</code>观察<code>data</code>变化，将其也变成响应式</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/core/instance/state.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initData</span>(<span class="hljs-params">vm: Component</span>) </span>&#123;
  <span class="hljs-keyword">let</span> data = vm.$options.data;
  data = vm._data = <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">"function"</span> ? getData(data, vm) : data || &#123;&#125;;
  <span class="hljs-keyword">if</span> (!isPlainObject(data)) &#123;
    data = &#123;&#125;;
  &#125;
  <span class="hljs-comment">// proxy data on instance</span>
  <span class="hljs-keyword">const</span> keys = <span class="hljs-built_in">Object</span>.keys(data);
  <span class="hljs-keyword">const</span> props = vm.$options.props;
  <span class="hljs-keyword">const</span> methods = vm.$options.methods;
  <span class="hljs-keyword">let</span> i = keys.length;
  <span class="hljs-keyword">while</span> (i--) &#123;
    <span class="hljs-keyword">const</span> key = keys[i];
    <span class="hljs-keyword">if</span> (!isReserved(key)) &#123;
      proxy(vm, <span class="hljs-string">`_data`</span>, key);
    &#125;
  &#125;
  <span class="hljs-comment">// observe data</span>
  observe(data, <span class="hljs-literal">true</span> <span class="hljs-comment">/* asRootData */</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">proxy 代理</h2>
<p>初始化 data 和 props 一个关键操作，就是让他们变成响应式，然后代理到<code>vm</code>上。</p>
<p>代理？其实就是就是一个中介。本身只是一个线索，会连接到真实的资源。</p>
<p>举个例子，看下面的<code>obj</code>，有个<code>data</code>属性，现在想<code>obj.a</code>也可以访问到 a 属性，怎么办？</p>
<p>此时<code>obj.a</code>就是一个中介，其真实连接的资源是<code>obj.data.a</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">data</span>: &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125; &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实还是利用上面的<code>Object.defineProperty</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.defineProperty(obj, <span class="hljs-string">"a"</span>, &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 这里的obj.data.a就相当于存储变量</span>
    <span class="hljs-keyword">return</span> obj.data.a;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
    obj.data.a = newValue;
  &#125;,
&#125;);
<span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(obj.a);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在看源码里，对于<code>proxy</code>的实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/core/instance/state.js</span>
<span class="hljs-comment">// const noop = function empty()&#123;&#125;</span>
<span class="hljs-keyword">const</span> sharedPropertyDefinition = &#123;
  <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">get</span>: noop,
  <span class="hljs-attr">set</span>: noop,
&#125;;
<span class="hljs-comment">// target相当于obj，sourceKey相当于data，key相当于a</span>
<span class="hljs-comment">// proxy就是可以让vm.x 代理到 vm.data.x</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxy</span>(<span class="hljs-params">target: <span class="hljs-built_in">Object</span>, sourceKey: string, key: string</span>) </span>&#123;
  sharedPropertyDefinition.get = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxyGetter</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>[sourceKey][key];
  &#125;;
  sharedPropertyDefinition.set = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxySetter</span>(<span class="hljs-params">val</span>) </span>&#123;
    <span class="hljs-built_in">this</span>[sourceKey][key] = val;
  &#125;;
  <span class="hljs-built_in">Object</span>.defineProperty(target, key, sharedPropertyDefinition);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">observe：给增加一个 Observer 实例</h2>
<p><code>observe</code> 的功能就是用来监测数据的变化，给非 <code>VNode</code> 的对象类型数据添加一个 <code>Observer</code>，如果已经添加过则直接返回，否则在满足一定条件下去实例化一个 <code>Observer</code> 对象实例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/core/observer/index.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observe</span>(<span class="hljs-params">value: any, asRootData: ?boolean</span>): <span class="hljs-title">Observer</span> | <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-keyword">if</span> (!isObject(value) || value <span class="hljs-keyword">instanceof</span> VNode) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-keyword">let</span> ob: Observer | <span class="hljs-keyword">void</span>;
  <span class="hljs-keyword">if</span> (hasOwn(value, <span class="hljs-string">"__ob__"</span>) && value.__ob__ <span class="hljs-keyword">instanceof</span> Observer) &#123;
    ob = value.__ob__;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (
    shouldObserve &&
    !isServerRendering() &&
    (<span class="hljs-built_in">Array</span>.isArray(value) || isPlainObject(value)) &&
    <span class="hljs-built_in">Object</span>.isExtensible(value) &&
    !value._isVue
  ) &#123;
    ob = <span class="hljs-keyword">new</span> Observer(value);
  &#125;
  <span class="hljs-keyword">if</span> (asRootData && ob) &#123;
    ob.vmCount++;
  &#125;
  <span class="hljs-keyword">return</span> ob;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">Observer 类：给对象的每个属性添加 getter 和 setter</h2>
<p><code>Observer</code> 是一个类，它的作用是给对象的属性添加 getter 和 setter，用于依赖收集和派发更新：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Observer class that is attached to each observed
 * object. Once attached, the observer converts the target
 * object's property keys into getter/setters that
 * collect dependencies and dispatch updates.
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
  <span class="hljs-attr">value</span>: any;
  dep: Dep;
  vmCount: number; <span class="hljs-comment">// number of vms that has this object as root $data</span>

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value: any</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.value = value;
    <span class="hljs-comment">// 实例化 Dep 对象</span>
    <span class="hljs-built_in">this</span>.dep = <span class="hljs-keyword">new</span> Dep();
    <span class="hljs-built_in">this</span>.vmCount = <span class="hljs-number">0</span>;
    def(value, <span class="hljs-string">"__ob__"</span>, <span class="hljs-built_in">this</span>);
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(value)) &#123;
      <span class="hljs-keyword">const</span> augment = hasProto ? protoAugment : copyAugment;
      augment(value, arrayMethods, arrayKeys);
      <span class="hljs-built_in">this</span>.observeArray(value);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.walk(value);
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * Walk through each property and convert them into
   * getter/setters. This method should only be called when
   * value type is Object.
   */</span>
  <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">obj: <span class="hljs-built_in">Object</span></span>)</span> &#123;
    <span class="hljs-keyword">const</span> keys = <span class="hljs-built_in">Object</span>.keys(obj);
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < keys.length; i++) &#123;
      defineReactive(obj, keys[i]);
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * Observe a list of Array items.
   */</span>
  <span class="hljs-function"><span class="hljs-title">observeArray</span>(<span class="hljs-params">items: <span class="hljs-built_in">Array</span><any></span>)</span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, l = items.length; i < l; i++) &#123;
      observe(items[i]);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Observer</code> 的构造函数逻辑很简单:</p>
<ul>
<li>实例化 <code>Dep</code> 对象，</li>
<li>通过执行 <code>def</code> 函数把自身实例添加到数据对象 <code>value</code> 的 <code>__ob__</code> 属性上</li>
</ul>
<p><code>def</code>就是给一个对象，定义一个属性，设置一个属性值，默认此属性是不可遍历的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// def的定义</span>
<span class="hljs-comment">// src/core/util/lang.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">def</span>(<span class="hljs-params">obj: <span class="hljs-built_in">Object</span>, key: string, val: any, enumerable?: boolean</span>) </span>&#123;
  <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
    <span class="hljs-attr">value</span>: val,
    <span class="hljs-attr">enumerable</span>: !!enumerable,
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>def</code>相当于<code>Object.defineProperty</code>的简单封装。</p>
<h2 data-id="heading-10">defineReactive：给对象的某个属性动态添加 getter 和 setter</h2>
<p><code>defineReactive</code> 的功能就是给对象动态添加 <code>getter</code> 和 <code>setter</code>，让对象成为响应式对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/core/observer/index.js</span>
<span class="hljs-comment">/**
 * Define a reactive property on an Object.
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span>(<span class="hljs-params">
  obj: <span class="hljs-built_in">Object</span>,
  key: string,
  val: any,
  customSetter?: ?<span class="hljs-built_in">Function</span>,
  shallow?: boolean
</span>) </span>&#123;
  <span class="hljs-comment">// 初始化 Dep 对象的实例</span>
  <span class="hljs-keyword">const</span> dep = <span class="hljs-keyword">new</span> Dep();
  <span class="hljs-comment">// 拿到 obj 的属性描述符</span>
  <span class="hljs-keyword">const</span> property = <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(obj, key);
  <span class="hljs-keyword">if</span> (property && property.configurable === <span class="hljs-literal">false</span>) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;

  <span class="hljs-comment">// cater for pre-defined getter/setters</span>
  <span class="hljs-keyword">const</span> getter = property && property.get;
  <span class="hljs-keyword">const</span> setter = property && property.set;
  <span class="hljs-keyword">if</span> ((!getter || setter) && <span class="hljs-built_in">arguments</span>.length === <span class="hljs-number">2</span>) &#123;
    val = obj[key];
  &#125;

  <span class="hljs-keyword">let</span> childOb = !shallow && observe(val);
  <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveGetter</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">const</span> value = getter ? getter.call(obj) : val;
      <span class="hljs-keyword">if</span> (Dep.target) &#123;
        dep.depend();
        <span class="hljs-keyword">if</span> (childOb) &#123;
          childOb.dep.depend();
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(value)) &#123;
            dependArray(value);
          &#125;
        &#125;
      &#125;
      <span class="hljs-keyword">return</span> value;
    &#125;,
    <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveSetter</span>(<span class="hljs-params">newVal</span>) </span>&#123;
      <span class="hljs-keyword">const</span> value = getter ? getter.call(obj) : val;
      <span class="hljs-comment">/* eslint-disable no-self-compare */</span>
      <span class="hljs-keyword">if</span> (newVal === value || (newVal !== newVal && value !== value)) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;
      <span class="hljs-comment">/* eslint-enable no-self-compare */</span>
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">"production"</span> && customSetter) &#123;
        customSetter();
      &#125;
      <span class="hljs-keyword">if</span> (setter) &#123;
        setter.call(obj, newVal);
      &#125; <span class="hljs-keyword">else</span> &#123;
        val = newVal;
      &#125;
      childOb = !shallow && observe(newVal);
      dep.notify();
    &#125;,
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>defineReactive</code> 函数：</p>
<ul>
<li>最开始初始化 <code>Dep</code> 对象的实例，</li>
<li>接着拿到 <code>obj</code> 的属性描述符，</li>
<li>然后对子对象递归调用 <code>observe</code>方法</li>
</ul>
<p>这样就保证了无论 <code>obj</code> 的结构多复杂，它的所有子属性也能变成响应式的对象，
这样我们访问或修改 <code>obj</code> 中一个嵌套较深的属性，也能触发 <code>getter</code> 和 <code>setter</code>。</p>
<p>最后利用 <code>Object.defineProperty</code> 去给 <code>obj</code> 的属性 <code>key</code> 添加 <code>getter</code> 和 <code>setter</code>。</p>
<h2 data-id="heading-11">总结</h2>
<p>响应式对象，核心就是利用 <code>Object.defineProperty</code> 给数据添加了 <code>getter</code> 和 <code>setter</code>。
这样在访问数据以及写数据的时候能自动执行一些逻辑：</p>
<ul>
<li><code>getter</code> 做的事情是依赖收集</li>
<li><code>setter</code> 做的事情是派发更新</li>
</ul>
<h2 data-id="heading-12">引用</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoding.imooc.com%2Flesson%2F228.html%23mid%3D14869" target="_blank" rel="nofollow noopener noreferrer" title="https://coding.imooc.com/lesson/228.html#mid=14869" ref="nofollow noopener noreferrer">黄轶老师的 vue2 源码解密课程</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fustbhuangyi.github.io%2Fvue-analysis%2Fv2%2Freactive%2Freactive-object.html" target="_blank" rel="nofollow noopener noreferrer" title="https://ustbhuangyi.github.io/vue-analysis/v2/reactive/reactive-object.html" ref="nofollow noopener noreferrer">vue.js 技术揭秘</a></li>
</ul></div>  
</div>
            