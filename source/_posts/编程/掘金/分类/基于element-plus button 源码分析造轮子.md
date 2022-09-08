
---
title: '基于element-plus button 源码分析造轮子'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e440b2bc113432c98fb53cd813265a3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 06:06:56 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e440b2bc113432c98fb53cd813265a3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>实现组件 <code>button</code> 新增功能和自定义UI换肤，使用 <code>SCSS</code> 变量和 <code>CSS 自定义属性</code>，参考 <code>element-plus</code> 源码造轮子</p>
<h3 data-id="heading-1">button 组件</h3>
<p>element-plus 的 <code>button</code> 文件
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Fcomponents%2Fbutton%2Fsrc%2Fbutton.vue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/components/button/src/button.vue" ref="nofollow noopener noreferrer">/packages/components/button/src/button.vue</a> 和 element-ui 实现逻辑是相似的，不同地方在于生成 <code>bem</code> 规范实现方式不一样，前者通过函数创建命名空间对象，然后调用 <code>b()</code>、<code>e()</code>、<code>m()</code>、<code>is()</code>等函数返回符合 <code>bem</code> 规范的类，后者通过字符串拼接生成</p>
<p>脚本函数创建命名空间对象</p>
<ul>
<li>优点：可读性强，减少模版编写，方便维护管理，可以动态的更改命名空间前缀</li>
<li>缺点：每个组件创建命名空间对象，占用额外内存</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">// 参考element-plus button 实现
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span>
    <span class="hljs-attr">:class</span>=<span class="hljs-string">"[
      ns.b(), // el-button
      ns.m(type), // 传入 type 生成 el-button--primary/success/info 等
      ns.m(buttonSize), // 传入 size 得到 el-button--large/small
      ns.is('disabled', buttonDisabled), // is-disabled
      ns.is('loading', loading), // is-loading
      ns.is('plain', plain), // is-plain
      ns.is('ghost', ghost), // is-ghost
      ns.is('round', round), // is-round
      ns.is('circle', circle), // is-circle
      ns.is('text', text), // is-text
      ns.is('link', link), // is-link
    ]"</span>
    @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleClick"</span>
    <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"buttonDisabled || loading"</span> // 禁用
    <span class="hljs-attr">:autofocus</span>=<span class="hljs-string">"autofocus"</span>
    <span class="hljs-attr">:type</span>=<span class="hljs-string">"nativeType"</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"loading"</span>></span> // 加载图标
      <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"$slots.loading"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"loading"</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">v-else</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-loading"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    // 自定义图标
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"icon || $slots.icon"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"$slots.icon"</span>></span><span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"icon"</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">v-else</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"icon"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"$slots.default"</span>></span><span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">const</span> &#123; useNamespace &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@element-plus/hooks'</span>
<span class="hljs-comment">// 创建 button 命名空间</span>
<span class="hljs-keyword">const</span> ns = <span class="hljs-title function_">useNamespace</span>(<span class="hljs-string">'button'</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Fhooks%2Fuse-namespace%2Findex.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/hooks/use-namespace/index.ts" ref="nofollow noopener noreferrer">useNamespace</a> 从全局获取命名空间，我这里没有用，直接使用默认的命名空间，例如 <code>el</code>，然后调用不同的函数，根据传入参数判断拼接字符串返回</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> defaultNamespace = <span class="hljs-string">'el'</span>
<span class="hljs-keyword">const</span> statePrefix = <span class="hljs-string">'is-'</span>

<span class="hljs-comment">/**
 * 生成 bem
 * <span class="hljs-doctag">@param</span> &#123;<span class="hljs-type"></span>&#125; namespace 命名空间
 * <span class="hljs-doctag">@param</span> &#123;<span class="hljs-type">*</span>&#125; block 块
 * <span class="hljs-doctag">@param</span> &#123;<span class="hljs-type">*</span>&#125; blockSuffix 块多个单词
 * <span class="hljs-doctag">@param</span> &#123;<span class="hljs-type">*</span>&#125; element 元素
 * <span class="hljs-doctag">@param</span> &#123;<span class="hljs-type">*</span>&#125; modifier 修饰符
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">_bem</span> = (<span class="hljs-params">namespace, block, blockSuffix, element, modifier</span>) => &#123;
  <span class="hljs-keyword">let</span> cls = <span class="hljs-string">`<span class="hljs-subst">$&#123;namespace&#125;</span>-<span class="hljs-subst">$&#123;block&#125;</span>`</span> <span class="hljs-comment">// el-button</span>
  <span class="hljs-keyword">if</span> (blockSuffix) &#123;
    cls += <span class="hljs-string">`-<span class="hljs-subst">$&#123;blockSuffix&#125;</span>`</span>
  &#125;
  <span class="hljs-keyword">if</span> (element) &#123;
    cls += <span class="hljs-string">`__<span class="hljs-subst">$&#123;element&#125;</span>`</span>
  &#125;
  <span class="hljs-keyword">if</span> (modifier) &#123;
    cls += <span class="hljs-string">`--<span class="hljs-subst">$&#123;modifier&#125;</span>`</span>
  &#125;
  <span class="hljs-keyword">return</span> cls
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title function_">useNamespace</span> = (<span class="hljs-params">block</span>) => &#123;
  <span class="hljs-comment">// 默认命名空间</span>
  <span class="hljs-keyword">const</span> namespace = defaultNamespace
  <span class="hljs-comment">// b() => el-button</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">b</span> = (<span class="hljs-params">blockSuffix = <span class="hljs-string">''</span></span>) => <span class="hljs-title function_">_bem</span>(namespace, block, blockSuffix, <span class="hljs-string">''</span>, <span class="hljs-string">''</span>)
  <span class="hljs-comment">// e(primary) => el-button__primary</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">e</span> = (<span class="hljs-params">element</span>) => element ? <span class="hljs-title function_">_bem</span>(namespace, block, <span class="hljs-string">''</span>, element, <span class="hljs-string">''</span>) : <span class="hljs-string">''</span>
  <span class="hljs-comment">// m(primary) => el-button--primary</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">m</span> = (<span class="hljs-params">modifier</span>) => modifier ? <span class="hljs-title function_">_bem</span>(namespace, block, <span class="hljs-string">''</span>, <span class="hljs-string">''</span>, modifier) : <span class="hljs-string">''</span>

  <span class="hljs-keyword">const</span> <span class="hljs-title function_">be</span> = (<span class="hljs-params">blockSuffix, element</span>) => blockSuffix && element
    ? <span class="hljs-title function_">_bem</span>(namespace, block, blockSuffix, element, <span class="hljs-string">''</span>)
    : <span class="hljs-string">''</span>

  <span class="hljs-keyword">const</span> <span class="hljs-title function_">em</span> = (<span class="hljs-params">element, modifier</span>) => element && modifier
    ? <span class="hljs-title function_">_bem</span>(namespace, block, <span class="hljs-string">''</span>, element, modifier)
    : <span class="hljs-string">''</span>

  <span class="hljs-keyword">const</span> <span class="hljs-title function_">bm</span> = (<span class="hljs-params">blockSuffix, modifier</span>) => blockSuffix && modifier
    ? <span class="hljs-title function_">_bem</span>(namespace, block, blockSuffix, <span class="hljs-string">''</span>, modifier)
    : <span class="hljs-string">''</span>

  <span class="hljs-keyword">const</span> <span class="hljs-title function_">bem</span> = (<span class="hljs-params">blockSuffix, element, modifier</span>) => blockSuffix && element && modifier
    ? <span class="hljs-title function_">_bem</span>(namespace, block, blockSuffix, element, modifier)
    : <span class="hljs-string">''</span>
  <span class="hljs-comment">// is(disabled) => is-disabled</span>
  <span class="hljs-keyword">const</span> <span class="hljs-title function_">is</span> = (<span class="hljs-params">name, ...args</span>) => &#123;
    <span class="hljs-keyword">const</span> state = args.<span class="hljs-property">length</span> >= <span class="hljs-number">1</span> ? args[<span class="hljs-number">0</span>] : <span class="hljs-literal">true</span>
    <span class="hljs-keyword">return</span> name && state ? <span class="hljs-string">`<span class="hljs-subst">$&#123;statePrefix&#125;</span><span class="hljs-subst">$&#123;name&#125;</span>`</span> : <span class="hljs-string">''</span>
  &#125;
  
  <span class="hljs-keyword">return</span> &#123;
    b,
    e,
    m,
    be,
    em,
    bm,
    bem,
    is,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>bem</code> 规范脚本生成的方式灵活，单独维护不嵌入代码，如果要替换组件库的前缀命名空间，只需要在全局配置传入替换就行</p>
<h3 data-id="heading-2">公共样式 scss 变量</h3>
<p><code>element-plus</code> scss 文件结构和 element-ui 差不多，区别在于使用 <code>Dart Sass</code> 的 <code>sass:map...</code>和 <code>@use</code> 重构所有的 <code>SCSS</code> 变量，解决 <code>@import</code> 造成的重复输出问题，SASS 使用可以看下之前整理的<a href="https://juejin.cn/post/7130472496242884645" target="_blank" title="https://juejin.cn/post/7130472496242884645">这篇文章</a></p>
<p><code>scss</code> 样式变量定义在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Ftheme-chalk%2Fsrc%2Fcommon%2Fvar.scss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/theme-chalk/src/common/var.scss" ref="nofollow noopener noreferrer">packages/theme-chalk/src/common/var.scss</a> ，例如主题颜色、字体颜色、边框颜色、背景颜色、字体大小、组件样式变量等</p>
<p>下面是部分代码，<code>$types</code> 定义 6 种主要类型，是列表数组类型；<code>$colors: () !default;</code> 初始化 <code>$colors</code> 变量，<code>map.deep-merge()</code> 是调用 <code>sass:map</code> 函数深度合并，然后通过 <code>map.get</code> 取值，获取 <code>map</code> 多层嵌套值，传入多个参数，逗号隔开 <code>map.get($colors, 'primary', 'base')</code></p>
<p><strong>注意</strong>：<code>$color-primary</code> 不以下划线或横杆开头声明 <code>$-color-primary</code>，是因为横杠开头声明为私有变量， <code>@use</code> 是没办法在外部引入使用</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@use</span> <span class="hljs-string">'sass:map'</span>;

// types
$types: primary, success, warning, danger, error, info;

// <span class="hljs-attribute">Color</span>
$colors: () !default;
$colors: map.<span class="hljs-built_in">deep-merge</span>(
  (
    <span class="hljs-string">'white'</span>: <span class="hljs-number">#ffffff</span>,
    <span class="hljs-string">'black'</span>: <span class="hljs-number">#000000</span>,
    <span class="hljs-string">'primary'</span>: (
      <span class="hljs-string">'base'</span>: <span class="hljs-number">#409eff</span>,
    ),
    <span class="hljs-string">'success'</span>: (
      <span class="hljs-string">'base'</span>: <span class="hljs-number">#67c23a</span>,
    ),
    <span class="hljs-string">'warning'</span>: (
      <span class="hljs-string">'base'</span>: <span class="hljs-number">#e6a23c</span>,
    ),
    <span class="hljs-string">'danger'</span>: (
      <span class="hljs-string">'base'</span>: <span class="hljs-number">#f56c6c</span>,
    ),
    <span class="hljs-string">'error'</span>: (
      <span class="hljs-string">'base'</span>: <span class="hljs-number">#f56c6c</span>,
    ),
    <span class="hljs-string">'info'</span>: (
      <span class="hljs-string">'base'</span>: <span class="hljs-number">#909399</span>,
    ),
  ),
  $colors
);

$<span class="hljs-attribute">color</span>-white: map.<span class="hljs-built_in">get</span>($colors, <span class="hljs-string">'white'</span>) !default;
$<span class="hljs-attribute">color</span>-black: map.<span class="hljs-built_in">get</span>($colors, <span class="hljs-string">'black'</span>) !default;
$<span class="hljs-attribute">color</span>-primary: map.<span class="hljs-built_in">get</span>($colors, <span class="hljs-string">'primary'</span>, <span class="hljs-string">'base'</span>) !default;
$<span class="hljs-attribute">color</span>-success: map.<span class="hljs-built_in">get</span>($colors, <span class="hljs-string">'success'</span>, <span class="hljs-string">'base'</span>) !default;
$<span class="hljs-attribute">color</span>-warning: map.<span class="hljs-built_in">get</span>($colors, <span class="hljs-string">'warning'</span>, <span class="hljs-string">'base'</span>) !default;
$<span class="hljs-attribute">color</span>-danger: map.<span class="hljs-built_in">get</span>($colors, <span class="hljs-string">'danger'</span>, <span class="hljs-string">'base'</span>) !default;
$<span class="hljs-attribute">color</span>-error: map.<span class="hljs-built_in">get</span>($colors, <span class="hljs-string">'error'</span>, <span class="hljs-string">'base'</span>) !default;
$<span class="hljs-attribute">color</span>-info: map.<span class="hljs-built_in">get</span>($colors, <span class="hljs-string">'info'</span>, <span class="hljs-string">'base'</span>) !default;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@each</code> 遍历 <code>$typs</code>，调用 <code>set-color-mix-level</code> 函数，使用 <code>mix(color1, color2, percent)</code> 进行颜色混合，它接收三个参数，前面两个参数是两种混合的颜色, <code>$mix-color</code> 默认是白色，<code>map.get($colors, $type, 'base')</code> 获取 <code>type</code> 类型 base 颜色，第三个参数是两个混合颜色的百分占比，例如 <code>0.1</code> 表示第一个参数颜色占比 10%，第二个颜色 90%；<code>dark-2</code> 值是混合黑色的颜色</p>
<pre><code class="hljs language-css copyable" lang="css">// https://sass-lang.com/documentation/values/maps#immutability
// mix colors with white/black to generate light/dark level
@mixin <span class="hljs-built_in">set-color-mix-level</span>(
  $type,
  $number,
  $mode: <span class="hljs-string">'light'</span>,
  $mix-color: $color-white
) &#123;
  $colors: map.<span class="hljs-built_in">deep-merge</span>(
    (
      $type: (
        <span class="hljs-string">'#&#123;$mode&#125;-#&#123;$number&#125;'</span>:
          <span class="hljs-built_in">mix</span>(
            $mix-color,
            map.<span class="hljs-built_in">get</span>($colors, $type, <span class="hljs-string">'base'</span>),
            math.<span class="hljs-built_in">percentage</span>(math.<span class="hljs-built_in">div</span>($number, <span class="hljs-number">10</span>))
          ),
      ),
    ),
    $colors
  ) !global;
&#125;

// $colors<span class="hljs-selector-class">.primary</span><span class="hljs-selector-class">.light-i</span>
// <span class="hljs-attr">--el-color-primary-light-i</span>
// <span class="hljs-number">10%</span> <span class="hljs-number">53</span>a8ff
// <span class="hljs-number">20%</span> <span class="hljs-number">66</span>b1ff
// <span class="hljs-number">30%</span> <span class="hljs-number">79</span>bbff
// <span class="hljs-number">40%</span> <span class="hljs-number">8</span>cc5ff
// <span class="hljs-number">50%</span> a0cfff
// <span class="hljs-number">60%</span> b3d8ff
// <span class="hljs-number">70%</span> c6e2ff
// <span class="hljs-number">80%</span> d9ecff
// <span class="hljs-number">90%</span> ecf5ff
<span class="hljs-keyword">@each</span> $type in $types &#123;
  <span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> through <span class="hljs-number">9</span> &#123;
    <span class="hljs-keyword">@include</span> set-color-mix-level($type, $i, <span class="hljs-string">'light'</span>, $color-white);
  &#125;
&#125;

// <span class="hljs-attr">--el-color-primary-dark-2</span>
<span class="hljs-keyword">@each</span> $type in $types &#123;
  <span class="hljs-keyword">@include</span> set-color-mix-level($type, <span class="hljs-number">2</span>, <span class="hljs-string">'dark'</span>, $color-black);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遍历混合后，打印 <code>$colors</code> 颜色值</p>
<pre><code class="hljs language-css copyable" lang="css">(
info: (<span class="hljs-string">"dark-2"</span>: <span class="hljs-number">#73767a</span>, <span class="hljs-string">"light-9"</span>: <span class="hljs-number">#f4f4f5</span>, <span class="hljs-string">"light-8"</span>: <span class="hljs-number">#e9e9eb</span>, <span class="hljs-string">"light-7"</span>: <span class="hljs-number">#dedfe0</span>, <span class="hljs-string">"light-6"</span>: <span class="hljs-number">#d3d4d6</span>, <span class="hljs-string">"light-5"</span>: <span class="hljs-number">#c8c9cc</span>, <span class="hljs-string">"light-4"</span>: <span class="hljs-number">#bcbec2</span>, <span class="hljs-string">"light-3"</span>: <span class="hljs-number">#b1b3b8</span>, <span class="hljs-string">"light-2"</span>: <span class="hljs-number">#a6a9ad</span>, <span class="hljs-string">"light-1"</span>: <span class="hljs-number">#9b9ea3</span>, <span class="hljs-string">"base"</span>: <span class="hljs-number">#909399</span>), 
error: (<span class="hljs-string">"dark-2"</span>: <span class="hljs-number">#cc3c2d</span>, <span class="hljs-string">"light-9"</span>: <span class="hljs-number">#ffedeb</span>, <span class="hljs-string">"light-8"</span>: <span class="hljs-number">#ffdbd7</span>, <span class="hljs-string">"light-7"</span>: <span class="hljs-number">#ffc9c3</span>, <span class="hljs-string">"light-6"</span>: <span class="hljs-number">#ffb7af</span>, <span class="hljs-string">"light-5"</span>: <span class="hljs-number">#ffa59c</span>, <span class="hljs-string">"light-4"</span>: <span class="hljs-number">#ff9388</span>, <span class="hljs-string">"light-3"</span>: <span class="hljs-number">#ff8174</span>, <span class="hljs-string">"light-2"</span>: <span class="hljs-number">#ff6f60</span>, <span class="hljs-string">"light-1"</span>: <span class="hljs-number">#ff5d4c</span>, <span class="hljs-string">"base"</span>: <span class="hljs-number">#FF4B38</span>), 
danger: (<span class="hljs-string">"dark-2"</span>: <span class="hljs-number">#cc3c2d</span>, <span class="hljs-string">"light-9"</span>: <span class="hljs-number">#ffedeb</span>, <span class="hljs-string">"light-8"</span>: <span class="hljs-number">#ffdbd7</span>, <span class="hljs-string">"light-7"</span>: <span class="hljs-number">#ffc9c3</span>, <span class="hljs-string">"light-6"</span>: <span class="hljs-number">#ffb7af</span>, <span class="hljs-string">"light-5"</span>: <span class="hljs-number">#ffa59c</span>, <span class="hljs-string">"light-4"</span>: <span class="hljs-number">#ff9388</span>, <span class="hljs-string">"light-3"</span>: <span class="hljs-number">#ff8174</span>, <span class="hljs-string">"light-2"</span>: <span class="hljs-number">#ff6f60</span>, <span class="hljs-string">"light-1"</span>: <span class="hljs-number">#ff5d4c</span>, <span class="hljs-string">"base"</span>: <span class="hljs-number">#FF4B38</span>), 
warning: (<span class="hljs-string">"dark-2"</span>: <span class="hljs-number">#cc7a00</span>, <span class="hljs-string">"light-9"</span>: <span class="hljs-number">#fff5e6</span>, <span class="hljs-string">"light-8"</span>: <span class="hljs-number">#ffebcc</span>, <span class="hljs-string">"light-7"</span>: <span class="hljs-number">#ffe0b3</span>, <span class="hljs-string">"light-6"</span>: <span class="hljs-number">#ffd699</span>, <span class="hljs-string">"light-5"</span>: <span class="hljs-number">#ffcc80</span>, <span class="hljs-string">"light-4"</span>: <span class="hljs-number">#ffc266</span>, <span class="hljs-string">"light-3"</span>: <span class="hljs-number">#ffb84d</span>, <span class="hljs-string">"light-2"</span>: <span class="hljs-number">#ffad33</span>, <span class="hljs-string">"light-1"</span>: <span class="hljs-number">#ffa31a</span>, <span class="hljs-string">"base"</span>: <span class="hljs-number">#FF9900</span>), 
success: (<span class="hljs-string">"dark-2"</span>: <span class="hljs-number">#309e70</span>, <span class="hljs-string">"light-9"</span>: <span class="hljs-number">#ecf9f4</span>, <span class="hljs-string">"light-8"</span>: <span class="hljs-number">#d8f3e8</span>, <span class="hljs-string">"light-7"</span>: <span class="hljs-number">#c5eedd</span>, <span class="hljs-string">"light-6"</span>: <span class="hljs-number">#b1e8d1</span>, <span class="hljs-string">"light-5"</span>: <span class="hljs-number">#9ee2c6</span>, <span class="hljs-string">"light-4"</span>: <span class="hljs-number">#8adcba</span>, <span class="hljs-string">"light-3"</span>: <span class="hljs-number">#77d6af</span>, <span class="hljs-string">"light-2"</span>: <span class="hljs-number">#63d1a3</span>, <span class="hljs-string">"light-1"</span>: <span class="hljs-number">#50cb98</span>, <span class="hljs-string">"base"</span>: <span class="hljs-number">#3CC58C</span>), 
primary: (<span class="hljs-string">"dark-2"</span>: <span class="hljs-number">#337ecc</span>, <span class="hljs-string">"light-9"</span>: <span class="hljs-number">#ecf5ff</span>, <span class="hljs-string">"light-8"</span>: <span class="hljs-number">#d9ecff</span>, <span class="hljs-string">"light-7"</span>: <span class="hljs-number">#c6e2ff</span>, <span class="hljs-string">"light-6"</span>: <span class="hljs-number">#b3d8ff</span>, <span class="hljs-string">"light-5"</span>: <span class="hljs-number">#a0cfff</span>, <span class="hljs-string">"light-4"</span>: <span class="hljs-number">#8cc5ff</span>, <span class="hljs-string">"light-3"</span>: <span class="hljs-number">#79bbff</span>, <span class="hljs-string">"light-2"</span>: <span class="hljs-number">#66b1ff</span>, <span class="hljs-string">"light-1"</span>: <span class="hljs-number">#53a8ff</span>, <span class="hljs-string">"base"</span>: <span class="hljs-number">#409eff</span>), 
<span class="hljs-string">"white"</span>: <span class="hljs-number">#ffffff</span>, 
<span class="hljs-string">"black"</span>: <span class="hljs-number">#000000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了定义常用的字体颜色、边框颜色等变量外，所有的组件变量也定义在这个文件，例如 <code>checkbox 复选框</code></p>
<pre><code class="hljs language-css copyable" lang="css">// Components
// ---
// Checkbox
// css3 <span class="hljs-selector-tag">var</span> in packages/theme-chalk/<span class="hljs-attribute">src</span>/checkbox<span class="hljs-selector-class">.scss</span>
$checkbox: () !default;
$checkbox: map.<span class="hljs-built_in">merge</span>(
  (
    <span class="hljs-string">'font-size'</span>: <span class="hljs-number">14px</span>,
    <span class="hljs-string">'font-weight'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'font-weight-primary'</span>),
    <span class="hljs-string">'text-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'text-color-regular'</span>),
    <span class="hljs-string">'input-height'</span>: <span class="hljs-number">14px</span>,
    <span class="hljs-string">'input-width'</span>: <span class="hljs-number">14px</span>,
    <span class="hljs-string">'border-radius'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'border-radius-small'</span>),
    <span class="hljs-string">'bg-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'fill-color'</span>, <span class="hljs-string">'blank'</span>),
    <span class="hljs-string">'input-border'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'border'</span>),
    <span class="hljs-string">'disabled-border-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'border-color'</span>),
    <span class="hljs-string">'disabled-input-fill'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'fill-color'</span>, <span class="hljs-string">'light'</span>),
    <span class="hljs-string">'disabled-icon-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'text-color-placeholder'</span>),
    <span class="hljs-string">'disabled-checked-input-fill'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'border-color-extra-light'</span>),
    <span class="hljs-string">'disabled-checked-input-border-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'border-color'</span>),
    <span class="hljs-string">'disabled-checked-icon-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'text-color-placeholder'</span>),
    <span class="hljs-string">'checked-text-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'color-primary'</span>),
    <span class="hljs-string">'checked-input-border-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'color-primary'</span>),
    <span class="hljs-string">'checked-bg-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'color-primary'</span>),
    <span class="hljs-string">'checked-icon-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'color'</span>, <span class="hljs-string">'white'</span>),
    <span class="hljs-string">'input-border-color-hover'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'color-primary'</span>),
  ),
  $checkbox
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面定义变量值有使用 <code>getCssVar()</code> 函数，它是应用 css 自定义属性，接下来介绍它</p>
<h3 data-id="heading-3">两种 css 自定义变量</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2FUsing_CSS_custom_properties" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/Using_CSS_custom_properties" ref="nofollow noopener noreferrer">CSS 自定义属性（变量）</a> 设定标记值（比如： <code>--main-color: black;</code>），由 <code>var()</code> 函数来获取值（比如： <code>color: var(--main-color);</code>）</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-pseudo">:root</span> &#123;
  <span class="hljs-attr">--main-bg-color</span>: brown;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>局部变量时用 <code>var()</code> 函数包裹以表示一个合法的属性值，<code>var()</code> 如果第一个参数不生效，可以接受第二个参数默认值</p>
<p>注意：自定义属性名是大小写敏感的，<code>--my-color</code> 和 <code>--My-color</code> 会被认为是两个不同的自定义属性。</p>
<pre><code class="hljs language-css copyable" lang="css">element &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">var</span>(--main-bg-color);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <code>JavaScript</code> 操作 <code>var</code> 变量值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 获取一个 Dom 节点上的 CSS 变量</span>
element.<span class="hljs-property">style</span>.<span class="hljs-title function_">getPropertyValue</span>(<span class="hljs-string">"--my-var"</span>);

<span class="hljs-comment">// 获取任意 Dom 节点上的 CSS 变量</span>
<span class="hljs-title function_">getComputedStyle</span>(element).<span class="hljs-title function_">getPropertyValue</span>(<span class="hljs-string">"--my-var"</span>);

<span class="hljs-comment">// 修改一个 Dom 节点上的 CSS 变量</span>
element.<span class="hljs-property">style</span>.<span class="hljs-title function_">setProperty</span>(<span class="hljs-string">"--my-var"</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>element-plus</code> 有两种 <code>css</code> 自定义属性：全局 <code>root</code> 和局部组件</p>
<h4 data-id="heading-4">全局 css 变量</h4>
<p>全局的 css 变量定义在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Ftheme-chalk%2Fsrc%2Fvar.scss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/theme-chalk/src/var.scss" ref="nofollow noopener noreferrer">packages/theme-chalk/src/var.scss</a>，它被引入 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Ftheme-chalk%2Fsrc%2Fbase.scss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/theme-chalk/src/base.scss" ref="nofollow noopener noreferrer">theme-chalk/src/base.scs</a> 文件，<code>base.scss</code> 分别引入到了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Ftheme-chalk%2Fsrc%2Findex.scss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/theme-chalk/src/index.scss" ref="nofollow noopener noreferrer">/theme-chalk/src/index.scss</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Fcomponents%2Fbase%2Fstyle%2Fcss.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/components/base/style/css.ts" ref="nofollow noopener noreferrer">packages/components/base/style/css.ts</a></p>
<p>如果全量注册组件，引入 <code>index.scss</code> 打包编译后的样式；如果是按需注册组件，从组件的 <code>style</code> 目录下引入 <code>css</code> 文件，其中加入了 <code>base/style/css.ts</code>，例如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Fcomponents%2Fbutton%2Fstyle%2Fcss.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/components/button/style/css.ts" ref="nofollow noopener noreferrer">button</a></p>
<pre><code class="hljs language-css copyable" lang="css">import '<span class="hljs-keyword">@element-plus</span>/components/base/style/css';
import '<span class="hljs-keyword">@element-plus</span>/theme-chalk/el-button.css';
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Ftheme-chalk%2Fsrc%2Fvar.scss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/theme-chalk/src/var.scss" ref="nofollow noopener noreferrer">element-plus 全局css变量</a> 定义两个 <code>root</code>， 通用和 <code>light</code> 主题</p>
<pre><code class="hljs language-css copyable" lang="css">// common
<span class="hljs-selector-pseudo">:root</span> &#123;
  <span class="hljs-keyword">@include</span> set-css-var-value(<span class="hljs-string">'color-white'</span>, $color-white);
  <span class="hljs-keyword">@include</span> set-css-var-value(<span class="hljs-string">'color-black'</span>, $color-black);

  // get rgb
  <span class="hljs-keyword">@each</span> $type in (primary, success, warning, danger, error, info) &#123;
    <span class="hljs-keyword">@include</span> set-css-color-rgb($type);
  &#125;

  // Typography
  <span class="hljs-keyword">@include</span> set-component-css-var(<span class="hljs-string">'font-size'</span>, $font-size);
  ...
&#125;

// for light
<span class="hljs-selector-pseudo">:root</span> &#123;
  <span class="hljs-attribute">color</span>-scheme: light;

  <span class="hljs-keyword">@include</span> set-css-var-value(<span class="hljs-string">'color-white'</span>, $color-white);
  <span class="hljs-keyword">@include</span> set-css-var-value(<span class="hljs-string">'color-black'</span>, $color-black);

  // <span class="hljs-attr">--el-color-</span>#&#123;$type&#125;
  // <span class="hljs-attr">--el-color-</span>#&#123;$type&#125;-light-&#123;$<span class="hljs-selector-tag">i</span>&#125;
  <span class="hljs-keyword">@each</span> $type in (primary, success, warning, danger, error, info) &#123;
    <span class="hljs-keyword">@include</span> set-css-color-type($colors, $type);
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css 变量生成的函数定义在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Ftheme-chalk%2Fsrc%2Fmixins%2F_var.scss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/theme-chalk/src/mixins/_var.scss" ref="nofollow noopener noreferrer">packages/theme-chalk/src/mixins/_var.scss</a></p>
<p>例如 <code>set-css-var-value('color-white', $color-white)</code>, 调用 <code>joinVarName</code> 得到 <code>--el-color-white</code>，最后结果是 <code>--el-color-white: #fff;</code></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> set-css-var-value($name, $value) &#123;
  #&#123;joinVarName($name)&#125;: #&#123;$value&#125;;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Ftheme-chalk%2Fsrc%2Fmixins%2Ffunction.scss%23L47-L55" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/theme-chalk/src/mixins/function.scss#L47-L55" ref="nofollow noopener noreferrer">theme-chalk/src/mixins/function.scss#L47-L55</a></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@function</span> joinVarName($list) &#123;
  $name: <span class="hljs-string">'--'</span> + config.$namespace;
  <span class="hljs-keyword">@each</span> $item in $list &#123;
    <span class="hljs-keyword">@if</span> $item != <span class="hljs-string">''</span> &#123;
      $name: $name + <span class="hljs-string">'-'</span> + $item;
    &#125;
  &#125;
  <span class="hljs-keyword">@return</span> $name;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>全局 css 变量执行结果如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e440b2bc113432c98fb53cd813265a3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">局部组件css变量</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Ftheme-chalk%2Fsrc%2Fbutton.scss%23L19-L21" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/theme-chalk/src/button.scss#L19-L21" ref="nofollow noopener noreferrer">button.scss</a> 会在前面执行下面这段代码生成 <code>组件局部 css 自定义变量</code></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@include</span> b(button) &#123;
  <span class="hljs-keyword">@include</span> set-component-css-var(<span class="hljs-string">'button'</span>, $button);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>$button</code> 组件变量是定义在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Ftheme-chalk%2Fsrc%2Fcommon%2Fvar.scss%23L628-L650" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/theme-chalk/src/common/var.scss#L628-L650" ref="nofollow noopener noreferrer">common/var.scss</a></p>
<pre><code class="hljs language-css copyable" lang="css">// <span class="hljs-selector-tag">Button</span>
// css3 <span class="hljs-selector-tag">var</span> in packages/theme-chalk/<span class="hljs-attribute">src</span>/<span class="hljs-selector-tag">button</span><span class="hljs-selector-class">.scss</span>
$<span class="hljs-selector-tag">button</span>: () !default;
$<span class="hljs-selector-tag">button</span>: map.<span class="hljs-built_in">merge</span>(
  (
    <span class="hljs-string">'font-weight'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'font-weight-primary'</span>),
    <span class="hljs-string">'border-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'border-color'</span>),
    <span class="hljs-string">'bg-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'fill-color'</span>, <span class="hljs-string">'blank'</span>),
    <span class="hljs-string">'text-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'text-color'</span>, <span class="hljs-string">'regular'</span>),
    <span class="hljs-string">'disabled-text-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'disabled-text-color'</span>),
    <span class="hljs-string">'disabled-bg-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'fill-color'</span>, <span class="hljs-string">'blank'</span>),
    <span class="hljs-string">'disabled-border-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'border-color-light'</span>),
    <span class="hljs-string">'divide-border-color'</span>: <span class="hljs-built_in">rgba</span>($color-white, <span class="hljs-number">0.5</span>),
    <span class="hljs-string">'hover-text-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'color-primary'</span>),
    <span class="hljs-string">'hover-bg-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'color-primary'</span>, <span class="hljs-string">'light-9'</span>),
    <span class="hljs-string">'hover-border-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'color-primary-light-7'</span>),
    <span class="hljs-string">'active-text-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'button-hover-text-color'</span>),
    <span class="hljs-string">'active-border-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'color-primary'</span>),
    <span class="hljs-string">'active-bg-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'button'</span>, <span class="hljs-string">'hover-bg-color'</span>),
    <span class="hljs-string">'outline-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'color-primary'</span>, <span class="hljs-string">'light-5'</span>),
    <span class="hljs-string">'hover-link-text-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'color-info'</span>),
    <span class="hljs-string">'active-color'</span>: <span class="hljs-built_in">getCssVar</span>(<span class="hljs-string">'text-color'</span>, <span class="hljs-string">'primary'</span>),
  ),
  $button
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Ftheme-chalk%2Fsrc%2Fmixins%2F_var.scss%23L38-L46" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/theme-chalk/src/mixins/_var.scss#L38-L46" ref="nofollow noopener noreferrer">set-component-css-var</a> 遍历 <code>$button</code>，然后拼接 <code>css</code> 变量名和值</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> set-component-css-var($name, $variables) &#123;
  <span class="hljs-keyword">@each</span> $attribute, $value in $variables &#123;
    <span class="hljs-keyword">@if</span> $attribute == <span class="hljs-string">'default'</span> &#123;
      #&#123;getCssVarName($name)&#125;: #&#123;$value&#125;;
    &#125; <span class="hljs-keyword">@else</span> &#123;
      #&#123;getCssVarName($name, $attribute)&#125;: #&#123;$value&#125;;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成 button 组件的css局部变量</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffcbb3df025f4b2096c3d34395c9ef75~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>设置相同的 name <code>--name</code> 可以覆盖 <code>root</code> 变量值</p>
<h4 data-id="heading-6">button.scss 源码分析</h4>
<p><code>button.scss</code> 样式文件结构和 element-ui 差别不大，可以阅读 <a href="https://juejin.cn/post/7138611140023566350#heading-8" target="_blank" title="https://juejin.cn/post/7138611140023566350#heading-8">element-ui 组件库 button 源码分析</a></p>
<p>分析一下差异点</p>
<ol>
<li>使用 <code>getCssVar()</code> 设置 css 变量值，例如 <code>getCssVar('button', 'bg-color');</code> 生成 <code>var(--el-button-bg-color</code>，它使用的组件局部 css 变量，局部又是继承全局的 <code>--el-bg-color</code></li>
</ol>
<p>这样做的好处是如果要更改 button 的背景，只需要修改 <code>--el-button-bg-color</code> 值，这样就不会影响到全局的背景颜色 <code>--el-bg-color</code></p>
<ol start="2">
<li>之前生成 <code>primary, success, warning, danger, info</code> 6种类型的按钮分别调用 <code>button-variant</code>，现在使用 Sass 重构后直接 <code>@each</code> 遍历就行</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@each</span> $type in (primary, success, warning, danger, info) &#123;
    <span class="hljs-keyword">@include</span> m($type) &#123;
      <span class="hljs-keyword">@include</span> button-variant($type);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Ftheme-chalk%2Fsrc%2Fmixins%2F_button.scss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/theme-chalk/src/mixins/_button.scss" ref="nofollow noopener noreferrer">_button.scss</a> 文件的 <code>button-variant</code> 悬浮、激活、禁用等状态不再直接编写代码，而是定义好各个状态的数据结构，然后遍历修改 <code>background</code>、<code>color</code>、<code>border-color</code> css变量值</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> button-variant($type) &#123;
  $<span class="hljs-selector-tag">button</span>-<span class="hljs-attribute">color</span>-types: (
    <span class="hljs-string">''</span>: (
      <span class="hljs-string">'text-color'</span>: (
        <span class="hljs-string">'color'</span>,
        <span class="hljs-string">'white'</span>,
      ),
      <span class="hljs-string">'bg-color'</span>: (
        <span class="hljs-string">'color'</span>,
        $type,
      ),
      <span class="hljs-string">'border-color'</span>: (
        <span class="hljs-string">'color'</span>,
        $type,
      ),
      <span class="hljs-string">'outline-color'</span>: (
        <span class="hljs-string">'color'</span>,
        $type,
        <span class="hljs-string">'light-5'</span>,
      ),
      <span class="hljs-string">'active-color'</span>: (
        <span class="hljs-string">'color'</span>,
        $type,
        <span class="hljs-string">'dark-2'</span>,
      ),
    ),
    <span class="hljs-string">'hover'</span>: (
      <span class="hljs-string">'text-color'</span>: (
        <span class="hljs-string">'color'</span>,
        <span class="hljs-string">'white'</span>,
      ),
      <span class="hljs-string">'link-text-color'</span>: (
        <span class="hljs-string">'color'</span>,
        $type,
        <span class="hljs-string">'light-5'</span>,
      ),
      <span class="hljs-string">'bg-color'</span>: (
        <span class="hljs-string">'color'</span>,
        $type,
        <span class="hljs-string">'light-3'</span>,
      ),
      <span class="hljs-string">'border-color'</span>: (
        <span class="hljs-string">'color'</span>,
        $type,
        <span class="hljs-string">'light-3'</span>,
      ),
    ),
    <span class="hljs-string">'active'</span>: (
      <span class="hljs-string">'bg-color'</span>: (
        <span class="hljs-string">'color'</span>,
        $type,
        <span class="hljs-string">'dark-2'</span>,
      ),
      <span class="hljs-string">'border-color'</span>: (
        <span class="hljs-string">'color'</span>,
        $type,
        <span class="hljs-string">'dark-2'</span>,
      ),
    ),
    <span class="hljs-string">'disabled'</span>: (
      <span class="hljs-string">'text-color'</span>: (
        <span class="hljs-string">'color'</span>,
        <span class="hljs-string">'white'</span>,
      ),
      <span class="hljs-string">'bg-color'</span>: (
        <span class="hljs-string">'color'</span>,
        $type,
        <span class="hljs-string">'light-5'</span>,
      ),
      <span class="hljs-string">'border-color'</span>: (
        <span class="hljs-string">'color'</span>,
        $type,
        <span class="hljs-string">'light-5'</span>,
      ),
    ),
  );

  <span class="hljs-keyword">@each</span> $type, $typeMap in $button-color-types &#123;
    <span class="hljs-keyword">@each</span> $typeColor, $list in $typeMap &#123;
      <span class="hljs-keyword">@include</span> css-var-from-global((<span class="hljs-string">'button'</span>, $type, $typeColor), $list);
    &#125;
  &#125;

  &<span class="hljs-selector-class">.is-plain</span>,
  &<span class="hljs-selector-class">.is-text</span>,
  &<span class="hljs-selector-class">.is-link</span> &#123;
    <span class="hljs-keyword">@include</span> button-plain($type);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上是 <code>element-plus</code> button 源码分析，造轮子的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjefferyxzf.github.io%2Fdouluo-ui%2Fpackages%2Felement%2Fbutton%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jefferyxzf.github.io/douluo-ui/packages/element/button/" ref="nofollow noopener noreferrer">演示地址</a></p></div>  
</div>
            