
---
title: 'Vue第二波ref语法提案来袭，这次会进入到标准吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2118'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 16:29:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=2118'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>⚠️本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<h1 data-id="heading-0">前言</h1>
<p>其实之前<code>Vue3</code>做过好多次语法糖的提案，最经典的莫过于<code><script setup></code>提案。但一开始这个提案夹杂着<code>ref</code>语法糖，所以很多批评的声音接踵而来：什么<code>Vue</code>又开始创造新概念啦、不忠于<code>JavsScript</code>啦、不如叫<code><script lang="vue-script"></code>之类的…</p>
<p>但<code>尤雨溪</code>发现反对的意见大多数是对<code>ref</code>语法糖不满，于是继续细分，把<code><script setup></code>和<code>ref</code>语法糖分成了两个不同的提案，如果不太清楚我说的到底是什么东西的话，可以点进这两篇文章看一看：<a href="https://juejin.cn/post/6894606141087875080" target="_blank" title="https://juejin.cn/post/6894606141087875080">《[译]尤雨溪: Ref语法糖提案》</a>、<a href="https://juejin.cn/post/6899439012331651079" target="_blank" title="https://juejin.cn/post/6899439012331651079">《Vue 3.0.3 : 新增CSS变量注入以及最新的Ref提案》</a></p>
<p>最近我看到<code><script setup></code>这个提案终于定稿了，已经进入<code>Vue</code>的标准里面去了，我们在用新版<code>Vue</code>的时候是默认支持这种写法的。不过由于<code>ref</code>这个提案反对意见太多，尤大怕如果不顾大家的反对意见坚决推进的话，可能会失去大家的信任从而流失一批用户、顺便再给自己多招点黑…</p>
<p>于是<code>ref</code>这个提案就被放弃掉了。正当我以为终于不用再搞那些花里胡哨的玩意之后，新版的<code>ref</code>语法糖提案又来了… 原来尤大解决<code>ref</code>的<code>.value</code>属性这个决心一直都没有改变，你们不同意原来的写法？那好，换个语法再来一遍！</p>
<h1 data-id="heading-1">为什么老想做这个 ref 语法糖？</h1>
<p>自从引入 <code>Composition API</code> 以来，一个主要未解决的问题是 <code>ref</code> 对象的使用。<code>.value</code>在任何地方使用都可能很麻烦，如果不使用 TS 的话，很容易就会忘记写这个<code>.value</code>属性，就像这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">let</span> loading = ref(<span class="hljs-literal">true</span>)

<span class="hljs-keyword">if</span> (loading) &#123;
    <span class="hljs-comment">// 此处省略若干代码</span>
    loading = <span class="hljs-literal">false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但实际上我们要写成这样才会正确运行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (loading.value) &#123;
    <span class="hljs-comment">// 此处省略若干代码</span>
    loading.value = <span class="hljs-literal">false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就很烦，所以一些用户特别倾向于只用<code>reactive()</code>这个函数，这样他们就不必面对<code>ref</code>的<code>.value</code>属性了，就像这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">const</span> state = reactive(&#123;
    <span class="hljs-attr">loading</span>: <span class="hljs-literal">true</span>
&#125;)

<span class="hljs-keyword">if</span> (state.loading) &#123;
    <span class="hljs-comment">// 此处省略若干代码</span>
    state.loading = <span class="hljs-literal">false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但其实这些写法在<code>尤雨溪</code>的眼里都不是最好的解决方案，于是他参考了<code>Svelte</code>的写法，用了几乎快被废弃掉的<code>label</code>语法：</p>
<pre><code class="hljs language-js copyable" lang="js">ref: loading = <span class="hljs-literal">true</span>

<span class="hljs-keyword">if</span> (loading) &#123;
    <span class="hljs-comment">// 此处省略若干代码</span>
    loading = <span class="hljs-literal">false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个语法为何遭到大家的强烈反对呢？因为我们声明一个变量通常会用<code>let</code>、<code>const</code>以及<code>var</code>关键字对吧，但这个压根儿就没用到任何声明的关键字，取而代之的是不伦不类的<code>ref:</code>。这个语法并不是尤雨溪自创的啊，它是<code>JS</code>里的<code>label</code>语法，但几乎没人用，可能有一部分人听都没听过，它主要是在多重嵌套的循环中配合<code>break</code>及<code>continue</code>使用的，就像这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> num = <span class="hljs-number">0</span>
<span class="hljs-attr">outermost</span>:
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < <span class="hljs-number">10</span>; j++) &#123;
        <span class="hljs-keyword">if</span> (i == <span class="hljs-number">5</span> && j == <span class="hljs-number">5</span>) &#123;
            <span class="hljs-keyword">continue</span> outermost
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">console</span>.log(i, j, <span class="hljs-number">88</span>)
        &#125;
        num++
    &#125;
&#125;
<span class="hljs-built_in">console</span>.log(num) <span class="hljs-comment">//95</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看不懂没关系啊，也没必要弄懂这种语法，因为它不够直观，用处也不是很大，所以几乎没什么人用它！不过既然没什么人在用，同时它还是<code>JS</code>的合法语法，那用它来告诉编译器这里是声明了一个<code>ref</code>变量岂不是很完美？</p>
<p>那么大家为何会如此反对呢？就是因为<code>label</code>语法压根儿就不是这么用的，人家原本是为了和<code>break</code>、<code>continue</code>配合使用的，虽然在别的地方用也不算是语法错误，但你这么做明显是修改了<code>JS</code>原本的语意！</p>
<p>那尤大新提的这个<code>ref</code>语法糖长什么样呢，我们来看一下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">let</span> loading = $ref(<span class="hljs-literal">true</span>)

<span class="hljs-keyword">if</span> (loading) &#123;
    <span class="hljs-comment">// 此处省略若干代码</span>
    loading = <span class="hljs-literal">false</span>
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尤大心想：你们不是嫌我之前用了不规范的语法么？那我这回这么写应该没问题了吧！想想之前我们定义一个<code>ref</code>变量，首先需要先把<code>ref</code>引进来然后才能用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">const</span> loading = ref(<span class="hljs-literal">true</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而新语法不用引，直接就能用，类似于全局变量的感觉。除了<code>$ref</code>这个特殊的全局变量呢，这次提案还有：<code>$computed</code>、<code>$fromRefs</code>和<code>$raw</code>这几个玩意。我们一个个来看，先看<code>$computed</code>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 以前 --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, computed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">const</span> num = ref(<span class="hljs-number">1</span>)
<span class="hljs-keyword">const</span> num_10 = computed(<span class="hljs-function">() =></span> num.value * <span class="hljs-number">10</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-comment"><!-- 现在 --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">let</span> num = $ref(<span class="hljs-number">1</span>)
<span class="hljs-keyword">const</span> num_10 = $computed(<span class="hljs-function">() =></span> num * <span class="hljs-number">10</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>$fromRefs</code>又是个啥呢？这玩意在之前没有啊！只听说过<code>toRefs</code>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 以前 --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; fromRefs &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span> <span class="hljs-comment">// 这个API并不存在</span>
<span class="hljs-keyword">import</span> &#123; toRefs &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span> <span class="hljs-comment">// 这个API倒是有 也就是只有 to 没有 from</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这个<code>$fromRefs</code>正是为了配合<code>toRefs</code>而产生的，比方说我们在别的地方写了一个<code>useXxx</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">const</span> state = reactive(&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">y</span>: <span class="hljs-number">0</span>
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> = <span class="hljs-function">(<span class="hljs-params">x = <span class="hljs-number">0</span>, y = <span class="hljs-number">0</span></span>) =></span> &#123;
    state.x = x
    state.y = y
    
    <span class="hljs-keyword">return</span> toRefs(state)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>于是我们在使用的时候就：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; useXxx &#125; form <span class="hljs-string">'../useXxx.js'</span>

<span class="hljs-keyword">const</span> &#123; x, y &#125; = useXxx(<span class="hljs-number">100</span>, <span class="hljs-number">200</span>)

<span class="hljs-built_in">console</span>.log(x.value, y.value)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这岂不是又要出现尤大最不想看到的<code>.value</code>属性了吗？所以<code>$fromRefs</code>就是为了解决这个问题而生的：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; useXxx &#125; form <span class="hljs-string">'../useXxx.js'</span>

<span class="hljs-keyword">const</span> &#123; x, y &#125; = $fromRefs(useXxx(<span class="hljs-number">100</span>, <span class="hljs-number">200</span>))

<span class="hljs-built_in">console</span>.log(x, y)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一个 API 就是<code>$raw</code>了，raw 不是原始的意思嘛！那么看名字也能猜到，就是我们用<code>$ref</code>所创建出来的其实是一个响应式<code>对象</code>，而不是一个基本数据类型，但语法糖会让我们在使用的过程中像是在用基本数据类型那样可以改来改去，但有时我们想看看这个<code>对象</code>长什么样，那么我们就需要用到<code>$raw</code>了：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">const</span> loading = $ref(<span class="hljs-literal">true</span>)

<span class="hljs-built_in">console</span>.log(loading) <span class="hljs-comment">// 其实打印的不是 loading 这个对象 而是它里面的值 相当于 loading.value</span>
<span class="hljs-built_in">console</span>.log($raw(loading)) <span class="hljs-comment">// 这回打印的就是 loading 这个对象了</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">嵌套在函数作用域内的语法糖用法(尚未实现)</h1>
<p>从技术上来讲，<code>$ref</code>可以在任何地方被<code>let</code>声明使用，包括嵌套函数范围：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useMouse</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> x = $ref(<span class="hljs-number">0</span>)
  <span class="hljs-keyword">let</span> y = $ref(<span class="hljs-number">0</span>)

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params">e</span>) </span>&#123;
    x = e.pageX
    y = e.pageY
  &#125;

  onMounted(<span class="hljs-function">() =></span> <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'mousemove'</span>, update))
  onUnmounted(<span class="hljs-function">() =></span> <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">'mousemove'</span>, update))

  <span class="hljs-keyword">return</span> $raw(&#123;
    x,
    y
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码将会被编译成这个样子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useMouse</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> x = ref(<span class="hljs-number">0</span>)
  <span class="hljs-keyword">let</span> y = ref(<span class="hljs-number">0</span>)

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params">e</span>) </span>&#123;
    x.value = e.pageX
    y.value = e.pageY
  &#125;

  onMounted(<span class="hljs-function">() =></span> <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'mousemove'</span>, update))
  onUnmounted(<span class="hljs-function">() =></span> <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">'mousemove'</span>, update))

  <span class="hljs-keyword">return</span> &#123;
    x,
    y
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过目前尚不支持这种写法，仅支持不在函数或者其他块级作用域中的<code>ref</code>语法糖。</p>
<h1 data-id="heading-3">尤大还不确定是否要做的功能</h1>
<h2 data-id="heading-4">这种语法糖是否要在单文件组件的外部进行支持</h2>
<p>这种语法糖本质上是可以通过<code>babel</code>等编译工具来转换成任何合法的<code>JS</code>或<code>TS</code>代码的，但新语法目前仅支持写在<code><script setup></code>的单文件组件里，这是因为：</p>
<ul>
<li>尽管是语法上有效的<code>JS</code>或<code>TS</code>语法，但它毕竟不是标准<code>JS</code>语义。<code>JS</code>里并没有<code>$ref</code>、<code>$computed</code>这种全局变量。在单文件组件中的<code><script></code>加上一个<code>setup</code>属性就是用来表示里面的代码将会被预处理一些特殊行为。</li>
<li>因为它被实现为<code>@vue/compiler-sfc</code>这个模块的其中一部分，所以它允许现有的<code>Vue</code>用户在开始使用新语法时不需要任何额外的<code>babel</code>等配置。</li>
<li><code><script setup></code>的编译过程已经实现全<code>AST</code>解析，所以<code>ref</code>语法糖的变换可以重复使用相同的<code>AST</code>，并避免产生额外的解析开销。</li>
<li>新语法的转换还会被编译器进行智能绑定。</li>
</ul>
<h2 data-id="heading-5">如果新语法仅限于单文件组件</h2>
<p>当我们不在单文件组件内写代码时会产生一定的心智负担。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Frfcs%2Fpull%2F222%23issuecomment-723560606" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/rfcs/pull/222#issuecomment-723560606" ref="nofollow noopener noreferrer">先前的研究</a>表明，这种心理成本可能实际上减少了没有语法糖时的使用效率。</p>
<p>不同的语法也会产生摩擦，比方说我们想提取或跨组件重用逻辑时(<em>就是我们俗称的<code>hooks</code></em>)。</p>
<p>不过幸运的是，由于变换规则相对而言比较简单，用语法糖编写的代码可以通过<code>IDE</code>插件来自动转换成没有语法糖的样子。</p>
<h2 data-id="heading-6">新语法如果支持所有文件</h2>
<ul>
<li>解析成本：我们已经解析<code><script setup></code>里面的语法了，所以新的<code>ref</code>语法糖并不会明显增加额外的解析成本。然而，如果应用到所有的<code>JS</code>或<code>TS</code>文件中去的话，将会显著增加额外的解析成本。</li>
<li>这种新语法并不是标准的<code>JavaScript</code>语义，<code>JS</code>里并没有<code>$ref</code>、<code>$raw</code>这种全局变量，让这种语法生效在<code>Vue</code>的特定环境之外可能是个坏主意。</li>
</ul>
<h1 data-id="heading-7">如何开启新语法？</h1>
<p>这种语法是随着<code>Vue 3.2</code>一同发布的，所以我们的<code>Vue</code>版本至少要大于等于<code>Vue 3.2.0-beta.1</code>。由于该语法是实验性的，默认是不启用的，我们需要自行配置：</p>
<h2 data-id="heading-8">在 vue-cli 脚手架中</h2>
<p>我们需要在根目录下新建一个<code>vue.config.js</code>，然后在里面写：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">chainWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    config.module
      .rule(<span class="hljs-string">'vue'</span>)
      .use(<span class="hljs-string">'vue-loader'</span>)
      .tap(<span class="hljs-function"><span class="hljs-params">options</span> =></span> &#123;
        <span class="hljs-keyword">return</span> &#123;
          ...options,
          <span class="hljs-attr">refSugar</span>: <span class="hljs-literal">true</span>
        &#125;
      &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">在 Vite 中</h2>
<p>我们需要在根目录下新建一个<code>vite.config.js</code>，然后在里面写：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">plugins</span>: [
    vue(&#123;
      <span class="hljs-attr">script</span>: &#123;
        <span class="hljs-attr">refSugar</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">在自己搭建的 webpack 脚手架中</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.vue$/</span>,
        loader: <span class="hljs-string">'vue-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">refSugar</span>: <span class="hljs-literal">true</span>
        &#125;
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">注意事项</h1>
<p>首先这个新语法还是实验性质的，并未进入标准，尽量不要在主要项目中开启，因为实验性语法不一定就会进入标准。第一波<code>ref</code>语法糖提案被毙掉之后，我看到有人跑到<code>GitHub</code>上大加吐槽：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c584914fbe44efc9e0bbcc04b517649~tplv-k3u1fbpfcp-watermark.image" alt="WX20210812-160513@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>翻译：</p>
<blockquote>
<p>我注意到 3.2 的测试版已经取消了第一波<code>ref</code>语法糖的支持。我非常失望。因为我已经使用 <code>ref</code> 语法糖半年多了，据我所知它是 <code>vue3</code> 的一部分。</p>
</blockquote>
<blockquote>
<p>与其他人不同，我认为理解起来或学习起来并不难。<code>vue3</code>已经出来快一年了，<code>ref</code>语法糖都已经<code>9</code>个月了。我都已经在我的团队中推进了<code>ref</code>语法糖的使用，它运行良好，以至于我们现在专门使用 <code>Composition API</code> 来进行开发。语法糖带来了很多好处，因为<code>.value</code>真的很无聊，这是与<code>vue2</code>的 <code>Options API</code> 的最大区别，使用语法糖可以不用写<code>.value</code>就具备响应式的能力和可组合性的魔力。</p>
</blockquote>
<blockquote>
<p>但是对于我和我的团队来说，这种变化非常糟糕，我们已经广泛使用了<code>ref</code>语法糖。我不知道我是不是少数，但我都已经用了半年多了，因为它得到了非常好的 <code>IDE</code> 支持（感谢<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjohnsoncodehk" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/johnsoncodehk" ref="nofollow noopener noreferrer">@johnsoncodehk</a> ），而且在用的时候也没发现任何的<code>bug</code>，无论是对对象结构还是对原始值的访问都很棒。这对我的开发体验来说是一个很大的改进。</p>
</blockquote>
<blockquote>
<p>我看了一下新的语法糖，和原来的没什么区别，不还是需要编译器做魔术嘛！因为没有了 <code>label</code> 语法导致它看起来更像原生<code>js</code>，但其实根本就不是。访问原始值和对象结构也变得更加乏味。添加了很多新的 <code>API</code>：<code>$ref</code>, <code>$computed</code>, <code>$fromRefs</code>, <code>$raw</code>, 不知道以后还会不会有<code>$shallowRef</code>, 或者<code>$watch</code>? </p>
</blockquote>
<blockquote>
<p>也不知道别人会不会接受这个新语法糖提案，但是至少是伤害了原本支持和使用第一波<code>ref</code>语法糖的人。由于 3.1.4 现在可以通过选项控制语法糖是否生效，我希望至少能够通过配置保留住第一波语法糖的写法。</p>
</blockquote>
<p>尤雨溪在最后说到：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f9d897e2d3e4599ac23f90eb5bd02de~tplv-k3u1fbpfcp-watermark.image" alt="WX20210812-162239@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如前所述，本提案中使用的标签语法存在各种缺陷——特别是与标准 <code>JS</code> 行为的语义不匹配，我们正在放弃这个提议。</p>
</blockquote>
<blockquote>
<p>再次声明一遍：请记住，<strong>标记为实验性的功能是用于评估和收集反馈意见的</strong>。它们可能随时更改或中断。<strong>除非功能的相应 RFC 已合并，否则无法保证 API 的稳定性</strong>。<code>@vue/compiler-sfc</code>使用实验性功能时的警告应该已经很清楚了。通过选择实验性功能，您承认您愿意在功能更改或删除时重构您的代码。</p>
</blockquote>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Frfcs%2Fdiscussions%2F369" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/rfcs/discussions/369" ref="nofollow noopener noreferrer">#369</a>提出了一个新版本的 ref 语法糖，它不依赖于挪用<code>label</code>语法，也不需要专门的工具支持。它目前在 <code>3.2.0-beta</code> 中发布，并取代了本提案的实现。同样，这也是实验性的，因此上述所有内容也适用于新提案。</p>
</blockquote>
<p>所以说尽可能不要在主要项目中使用它，我们可以没事写个 <code>demo</code> 试验一下，或者在自己的个人项目中使用，不然的话很可能就会像上面那位老哥吐槽的那样了…</p>
<p>其他人也觉得谁让你那么用了，既然用了就要承担风险：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/137a5598f3a8483ca22b96f745243b43~tplv-k3u1fbpfcp-watermark.image" alt="WX20210812-162955@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>你没有考虑到<strong>API 是作为实验性质引入的，以便能够根据用户反馈对其进行调整</strong>（很多人不喜欢 label 语法）。它使用户能够试验<code>API</code>，在某些情况下，这对于 <code>API</code> 的体验感至关重要。当你使用实验性功能时，你将<strong>接受</strong>如果后续版本不兼容的话，你会对原来的代码进行重构甚至不得不将其删除的风险。在 <code>API</code> 稳定并合并到 <code>RFC</code> 之前，它也不是 <code>Vue 的一部分</code></p>
</blockquote>
<blockquote>
<p>不过话虽如此，你应该试试新版的<code>ref</code>语法糖，然后再来提供反馈。因为说不定你可能更喜欢新版的语法糖而不是现有版本。</p>
</blockquote>
<p>也有人支持吐槽的那位老哥：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d12e7c024f0e405090bea52b5acd3a68~tplv-k3u1fbpfcp-watermark.image" alt="WX20210812-163708@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>新一波语法糖提案似乎仍旧令人费解，但这是我们在不改变 JS 原始语法的情况下所能做的最好的事情了（因为有些人总是介意这一点）我同意同时保留新旧两种语法糖。</p>
</blockquote>
<h1 data-id="heading-12">个人观点</h1>
<p>当然这种新语法肯定是有人喜欢有人讨厌的，我个人是比较反感这个新语法的，如果屏幕前的你喜欢这个新语法的话，那么请跳过我对这段对新语法的吐槽，以免因观点不合产生激烈互喷等情况。</p>
<p>首先我认为最大的弊端就是尤雨溪提出来的：<code>这种语法糖是否要在单文件组件的外部进行支持？</code></p>
<p>如果仅在单文件组件里支持，我们在外头写<code>hooks</code>的时候还是要写<code>.value</code>属性，一会需要写一会不用写的这样不一致的写法很容易写错(<code>虽然有工具提示可以降低错误</code>)。但还是很烦，而且这边用着<code>ref</code>函数，到了另一边又变成了<code>$ref</code>…</p>
<p>如果在所有文件都支持的情况下吧，又不得不用到<code>babel</code>等工具进行转换，对性能又是个负担。而且有一个很难受的点就是我们还有<code>customRef</code>这种比较高级的<code>API</code>，引用官网上的一个案例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"text"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useDebouncedRef</span>(<span class="hljs-params">value, delay = <span class="hljs-number">200</span></span>) </span>&#123;
  <span class="hljs-keyword">let</span> timeout
  <span class="hljs-keyword">return</span> customRef(<span class="hljs-function">(<span class="hljs-params">track, trigger</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        track()
        <span class="hljs-keyword">return</span> value
      &#125;,
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
        <span class="hljs-built_in">clearTimeout</span>(timeout)
        timeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          value = newValue
          trigger()
        &#125;, delay)
      &#125;
    &#125;
  &#125;)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">text</span>: useDebouncedRef(<span class="hljs-string">'hello'</span>)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种岂不是又要写<code>.value</code>属性？那在单文件组件里就会出现这个变量需要写<code>.value</code>，那个变量又不需要写的状况，很容易把人搞的头大。虽说以后对<code>customRef</code>这种<code>API</code>可能会单独再出一个<code>$customRef</code>语法糖，但我觉得就算写了个<code>.value</code>属性也没啥吧？至于就跟它较上劲了么… 虽说有时候写多了确实会稍微有点烦，但至少还是很容易理解的嘛：用<code>.value</code>属性触发了<code>Proxy</code>的<code>getter</code>或<code>setter</code>从而引发依赖收集或更新视图等操作。</p>
<p>还有一些其他的<code>API</code>如：<code>provide</code>、<code>inject</code> 等，目前的语法糖并未对它们进行兼容，所以还是会出现一会需要<code>.value</code>一会又不需要的情况。</p>
<p>还有一个最重要的点就是：一个框架的写法老是变来变去的很不利于推广，想想看<code>Vue3.0</code>和<code>Vue 3.2</code>之间有多大的差异，这次开了个坏头的话，以后就更加助长了尤大魔改编译的风气。当然他也确实是为了我们好，改的这些东西也是为了我们写起来更加的方便，有的改的也确实是不错，比如：<a href="https://juejin.cn/post/6856668819344392206" target="_blank" title="https://juejin.cn/post/6856668819344392206">《Vue超好玩的新特性：在CSS中引入JS变量》</a></p>
<p>还有现在已经定了稿的<code><script setup></code>语法糖，以前我们引入一个组件老需要再注册一遍：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Xxx <span class="hljs-keyword">from</span> <span class="hljs-string">'Xxx.vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">components</span>: &#123;
        Xxx
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>写多了这样的代码确实有点烦，现在我们只需要引进来就行，不用注册，但这样本质上并没有改变语意，反而新的语法糖明显改变了语意：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> loading = $ref(<span class="hljs-literal">true</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按理说<code>loading</code>应该是个<code>Proxy</code>代理对象，但是它现在却变成了一个布尔类型的值，而且还多出来个莫名其妙的<code>$ref</code>函数。</p>
<p>当然你可能会说：你不喜欢不用不就得了？话这么说没错，但是你不用不代表别人也不用，有的人用有的人不用，这样的话在语法层面就已经产生了割裂。我们终究是要看别人代码的，有时候是接手一个遗留下来的项目，有时是在<code>GitHub</code>上看看别人的项目，在有的人用有的人不用的情况下就很难受。</p>
<p>大家怎么认为呢？可以在评论区留个言看看是喜欢这种语法糖的人多还是反对它的人多。</p>
<h1 data-id="heading-13">结语</h1>
<p>我们把新语法糖的提案地址放在这里：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Frfcs%2Fdiscussions%2F369" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/rfcs/discussions/369" ref="nofollow noopener noreferrer">github.com/vuejs/rfcs/…</a>，希望大家可以积极参与并进去评论，但一定要注意的一点是：<strong>要用英文！</strong></p>
<p>可能有人会说：都是中国人用什么英文？虽说用英文尤大可以看得懂，但评论区不全是中国人，<code>Vue</code>还是有相当一批外国粉丝的，而且也不全是美国人，那些不是英国人美国人的开发者，他们如果也只图自己痛快而说自己国家的母语的话，想必我们就没有办法进行沟通了，同时这也会进一步拉近国人在海外的形象：别人都用英文，就你们中国人用自己的语言，不遵守规则。</p>
<p>那可能有人英文水平真的很差，我们可以这样嘛：找到百度翻译，输入中文后翻译成英文，然后再把英文复制过去。虽然这样做翻译的可能不完全准确，但最起码能达到勉强看懂的地步。同时还有一个技巧就是把翻译成英文的句子再翻译回中文，看看有哪些地方的语意发生了明显的变化，我们再针对那个地方重新自己写一遍。</p>
<h2 data-id="heading-14">往期精彩文章</h2>
<ul>
<li><a href="https://juejin.cn/post/6992018709439053837" target="_blank" title="https://juejin.cn/post/6992018709439053837">《尤雨溪国外教程：亲手带你写个简易版的Vue！》</a></li>
<li><a href="https://juejin.cn/post/6986453616517185567" target="_blank" title="https://juejin.cn/post/6986453616517185567">《产品经理：能不能让这串数字滚动起来？》</a></li>
<li><a href="https://juejin.cn/post/6979042510400126983" target="_blank" title="https://juejin.cn/post/6979042510400126983">《产品经理：鸿蒙那个开场动画挺帅的 给咱们页面也整一个呗》</a></li>
<li><a href="https://juejin.im/post/6865591917279870990" target="_blank" title="https://juejin.im/post/6865591917279870990">《不依赖任何库打造属于自己的可视化数据地图》</a></li>
<li><a href="https://juejin.cn/post/6946756821675671566" target="_blank" title="https://juejin.cn/post/6946756821675671566">《[译]尤雨溪：Vue3将不会支持IE11 精力会投入到Vue2.7》</a></li>
<li><a href="https://juejin.cn/post/6856668819344392206" target="_blank" title="https://juejin.cn/post/6856668819344392206">《Vue超好玩的新特性：在CSS中引入JS变量》</a></li>
<li><a href="https://juejin.cn/post/6912374170743472135" target="_blank" title="https://juejin.cn/post/6912374170743472135">《什么？仅靠H5标签就能实现收拉效果？》</a></li>
<li><a href="https://juejin.cn/post/6910828161030701064" target="_blank" title="https://juejin.cn/post/6910828161030701064">《整治GitHub不文明现象！微软推出评论区！》</a></li>
<li><a href="https://juejin.cn/post/6899439012331651079" target="_blank" title="https://juejin.cn/post/6899439012331651079">《Vue 3.0.3 : 新增CSS变量传递以及最新的Ref提案》</a></li>
<li><a href="https://juejin.im/post/6893875394584248334" target="_blank" title="https://juejin.im/post/6893875394584248334">《双11小黑盒很炫酷？咱们用CSS变量来改进一下！》</a></li>
<li><a href="https://juejin.im/post/6886770985060532231" target="_blank" title="https://juejin.im/post/6886770985060532231">《千万别小瞧九宫格 一道题就能让候选人原形毕露！》</a></li>
<li><a href="https://juejin.im/post/6884971597498613768" target="_blank" title="https://juejin.im/post/6884971597498613768">《移动端布局面试题 全面考察你的CSS功底(居中篇)》</a></li>
<li><a href="https://juejin.im/post/6877430232987467789" target="_blank" title="https://juejin.im/post/6877430232987467789">《将原型对象设置成Proxy后的一系列迷惑行为》</a></li>
<li><a href="https://juejin.im/post/6868260498417123335" target="_blank" title="https://juejin.im/post/6868260498417123335">《Vue超好玩的新特性：DOM传送门》</a></li>
<li><a href="https://juejin.im/post/6844904030641078280" target="_blank" title="https://juejin.im/post/6844904030641078280">《在Vue项目中使用React超火的CSS-in-JS库: styled-components》</a></li>
<li><a href="https://juejin.im/post/6844904015004696583" target="_blank" title="https://juejin.im/post/6844904015004696583">《终于轮到Vue来带给React灵感了？》</a></li>
<li><a href="https://juejin.im/post/6844904145275584519" target="_blank" title="https://juejin.im/post/6844904145275584519">《Vue3在IOS下的一个小坑》</a></li>
<li><a href="https://juejin.im/post/6844904182357426190" target="_blank" title="https://juejin.im/post/6844904182357426190">《新版vue-router的hooks用法》</a></li>
<li><a href="https://juejin.im/post/6844903823937372174" target="_blank" title="https://juejin.im/post/6844903823937372174">《[译]尤雨溪：Vue3的设计过程》</a></li>
</ul></div>  
</div>
            