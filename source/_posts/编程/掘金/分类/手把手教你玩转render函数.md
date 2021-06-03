
---
title: '手把手教你玩转render函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/846b664933c8433d8df509f6a47cf192~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 02 Jun 2021 07:58:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/846b664933c8433d8df509f6a47cf192~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第1天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557?utm_campaign=30day&utm_medium=Ccenter&utm_source=20210528" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>本文及之后所有系列文章组件封装都是基于<code>element-ui</code>组件库进行封装，里面并不会去讲element-ui的API, 本文要探讨是render函数在封装组件中的一些技巧思维且可以用于生产项目的所以并没有用Vue3, 后面会慢慢封装成一个中后台通用表单集成组件， 本文先从输入框开始，</p>
<h2 data-id="heading-1">支持的类型</h2>
<ul>
<li>text</li>
<li>input</li>
<li>number</li>
<li>password</li>
<li>email</li>
<li>textarea</li>
</ul>
<h2 data-id="heading-2">Input Attributes</h2>





























<table><thead><tr><th align="center"><strong>参数</strong></th><th align="center"><strong>说明</strong></th><th><strong>类型</strong></th><th align="center"><strong>默认值</strong></th></tr></thead><tbody><tr><td align="center">value / v-model</td><td align="center">绑定值</td><td><code>[String, Number]</code></td><td align="center">''</td></tr><tr><td align="center">type</td><td align="center">表单类型</td><td><code>["input", "text", "number", "password", "email", "textarea"]</code></td><td align="center"><code>text</code></td></tr><tr><td align="center">支持el-input所有参数</td><td align="center"></td><td></td><td align="center"></td></tr></tbody></table>
<p><code>dynamic-input</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-comment">// 供全局使用</span>
<span class="hljs-keyword">let</span> h

<span class="hljs-comment">// 支持的类型(只做输入框，radio/checkbox另外拆开)</span>
<span class="hljs-keyword">const</span> selectInputType = [
  <span class="hljs-string">'input'</span>,
  <span class="hljs-string">'text'</span>,
  <span class="hljs-string">'number'</span>,
  <span class="hljs-string">'password'</span>,
  <span class="hljs-string">'email'</span>,
  <span class="hljs-string">'textarea'</span>
]
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'DynamicInput'</span>,
  <span class="hljs-comment">// attrs不显示在dom上</span>
  <span class="hljs-attr">inheritAttrs</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">// 类型</span>
    <span class="hljs-attr">type</span>: &#123;
      <span class="hljs-attr">default</span>: <span class="hljs-string">'text'</span>,
      <span class="hljs-attr">validator</span>: <span class="hljs-function"><span class="hljs-params">typeVal</span> =></span> &#123;
        <span class="hljs-keyword">return</span> selectInputType.includes(typeVal)
      &#125;
    &#125;,
    <span class="hljs-comment">// 绑定值</span>
    <span class="hljs-attr">value</span>: &#123;
      <span class="hljs-attr">type</span>: [<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Number</span>],
      <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
    &#125;,

    <span class="hljs-comment">// 支持el-input所有参数</span>
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-attr">newValue</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">&#123; value &#125;</span>)</span> &#123;
        <span class="hljs-keyword">return</span> value
      &#125;,
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">val</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'input'</span>, val)
      &#125;
    &#125;,
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">onInputHandle</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.newValue = val
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    h = <span class="hljs-built_in">this</span>.$createElement
    <span class="hljs-keyword">const</span> &#123;
      onInputHandle,
      $attrs,
    &#125; = <span class="hljs-built_in">this</span>

    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'el-input'</span>, &#123;
      <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-built_in">this</span>.type,
        <span class="hljs-attr">value</span>: <span class="hljs-built_in">this</span>.newValue,
        ...this.$attrs
      &#125;,
      <span class="hljs-attr">on</span>: &#123;
        <span class="hljs-attr">input</span>: onInputHandle,
      &#125;,
    &#125;)
  &#125;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以Get到的技巧</p>
<ul>
<li>借助computed来实现双向绑定</li>
<li>通过<code>$attrs</code>来进行参数透传，可以省略<code>prop</code>不必传的参数</li>
</ul>
<p>这里讲下<code>inheritAttrs</code>，这个参数就是是否将$attrs中定义的数据挂载到dom层面上，直接上图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/846b664933c8433d8df509f6a47cf192~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>表单支持的修饰符</p>
<ul>
<li>number： 通过 <code>parseFloat()</code>解析之后的字符串数值</li>
<li>trim： 过滤首尾空白字符</li>
<li>lazy： 将事件触发从input从而转为在「 类似change」在值确认之后响应(当输入法没有按下时不做值变动可以使用这个)</li>
</ul>
<p>最常见的就是当我们使用number类型输入框但输入框最后给定的值是字符串，这个时候可以通过添加<code>.number</code>修饰符内部帮你自动转换为number类型</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">dynamic-input</span>
  <span class="hljs-attr">v-model</span>=<span class="hljs-string">"testVal"</span>
  <span class="hljs-attr">type</span>=<span class="hljs-string">"number"</span>
 /></span>
<span class="hljs-comment"><!-- testVal => 'string' --></span>

<span class="hljs-tag"><<span class="hljs-name">dynamic-input</span>
  <span class="hljs-attr">v-model.number</span>=<span class="hljs-string">"testVal"</span>
  <span class="hljs-attr">type</span>=<span class="hljs-string">"number"</span>
 /></span>
<span class="hljs-comment"><!-- testVal => 'number' --></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>「lazy修饰符的效果」</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b99ba374c6c4427c807a874e95be40c7~tplv-k3u1fbpfcp-zoom-1.image" alt="lazy修饰符" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">Input Events</h2>
<p>支持<code>el-input</code>所有事件</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">dynamic-input</span>
    <span class="hljs-attr">ref</span>=<span class="hljs-string">"dynamicInput"</span>
    <span class="hljs-attr">v-model.lazy</span>=<span class="hljs-string">"testVal"</span>
    <span class="hljs-attr">:type</span>=<span class="hljs-string">"testType"</span>
    <span class="hljs-attr">:class</span>=<span class="hljs-string">"computedClass"</span>
    @<span class="hljs-attr">change</span>=<span class="hljs-string">"changeMethod"</span>
    @<span class="hljs-attr">input.native</span>=<span class="hljs-string">"inputMethod"</span>
  /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> dynamicInput <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/common/dynamic-input'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'CkTestInput'</span>,
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-string">'dynamic-input'</span>: dynamicInput
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">testType</span>: <span class="hljs-string">'text'</span>,
      <span class="hljs-attr">testVal</span>: <span class="hljs-string">''</span>,
      <span class="hljs-attr">restaurants</span>: []
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">computedClass</span>(<span class="hljs-params">&#123; testVal &#125;</span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-string">'is-fill'</span>: testVal &#125;
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">changeTestVal</span>(<span class="hljs-params">changeVal</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.testVal = changeVal
    &#125;,
    <span class="hljs-function"><span class="hljs-title">inputMethod</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(val, <span class="hljs-string">'-->'</span>)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">changeMethod</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(val, <span class="hljs-string">'-->'</span>)
    &#125;,
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>同样支持原生修饰符事件</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b0a627114e14807ab90d8500a106609~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">Input Methods</h2>
<p>支持<code>el-input</code>所有方法，前提得通过ref去引用<code>dynamic-input</code>组件，组件封装的<code>el-input</code>默认取名<code>elInput</code></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <dynamic-input
    ref="dynamicInput
    value="test"
  />
</template>

<script>
export default &#123;
  mounted() &#123;
    // 可以获取到dynamicInput组件内封装的elInput组件
    this.$refs.dynamicInput.$refs.elInput
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你也可以通过定义refName去重命名内部elInput组件的ref值</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">dynamic-input</span>
    <span class="hljs-attr">ref</span>=<span class="hljs-string">"dynamicInput"</span>
    <span class="hljs-attr">refName</span>=<span class="hljs-string">"child-input'
    value="</span><span class="hljs-attr">test</span>"
  /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 可以获取到dynamicInput组件内封装的elInput组件</span>
    <span class="hljs-built_in">this</span>.$refs.dynamicInput.$refs[<span class="hljs-string">'child-input'</span>]
    <span class="hljs-keyword">const</span> &#123;
      dynamicInput
    &#125; = <span class="hljs-built_in">this</span>.$refs
    <span class="hljs-comment">// 可以通过去调用el-input组件提供方法</span>
    dynamicInput.$refs[<span class="hljs-string">'child-input'</span>].focus() 
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们只要在render函数中添加这一行判断就行</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
 <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> &#123;
      $attrs
    &#125; = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'el-input'</span>, &#123;
      <span class="hljs-comment">// ...</span>
      <span class="hljs-attr">ref</span>: $attrs[<span class="hljs-string">'ref-name'</span>] || <span class="hljs-string">'elInput'</span>
    &#125;)
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">Input Slots</h2>
<p>支持所有<code>el-input</code>提供的内置slot</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">dynamic-input</span>
    <span class="hljs-attr">ref</span>=<span class="hljs-string">"dynamicInput"</span>
    <span class="hljs-attr">refName</span>=<span class="hljs-string">"child-input'
    value="</span><span class="hljs-attr">test</span>"
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"prepend"</span>></span>Http://<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"prefix"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-input__icon el-icon-search"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"suffix"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-input__icon el-icon-date"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">dynamic-input</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于插槽解析这一块我们需要注意一下，官方文档对于render函数写slot没有列子，对于怎么去实现这一块也写的很晦涩，需要注意的是render函数中的第三个参数是描述当前组件的子内容，虽然slot是当前组件提供的内置内容，让你可以渲染到当前组件的指定内容，但是并不是这样就能实现的</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    h = <span class="hljs-built_in">this</span>.$createElement
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'el-input'</span>, &#123;
      <span class="hljs-comment">// ....</span>
    &#125;, <span class="hljs-built_in">Object</span>.values(<span class="hljs-built_in">this</span>.$slots))
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里第三个参数最后的结果是 => [VNode, VNode], 但是要注意VNode并没有<strong>指定插槽名称</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d42223b6751348b883b3dd7302c59857~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>文档只在这里很浅的带过了一下 <a href="https://cn.vuejs.org/v2/guide/render-function.html#%E6%B7%B1%E5%85%A5%E6%95%B0%E6%8D%AE%E5%AF%B9%E8%B1%A1" target="_blank" rel="nofollow noopener noreferrer">深入数据对象👉</a></p>
<p>所以渲染el-input提供的内置插槽内容的时候我们需要去定义一个提供slot名称的数据对象来渲染VNode，这里我们借助一个无状态的函数式组件做件事</p>
<p><code>slotContent.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 用于处理插槽</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'SlotContent'</span>,
  <span class="hljs-comment">// 声明这是一个函数式组件</span>
  <span class="hljs-attr">functional</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">render</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Function</span>,
      <span class="hljs-attr">require</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">data</span>: <span class="hljs-built_in">Object</span>
  &#125;,
  <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h, ctx</span>) =></span> &#123;
    <span class="hljs-comment">// 函数式组件中没有this, 所有可用的API都提供在ctx中</span>
    <span class="hljs-keyword">return</span> ctx.props.render(h, ctx.props.data)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于一些不做任何状态处理的组件，可以用函数式组件的方式来生成相对比较「轻量」的组件， <a href="https://cn.vuejs.org/v2/guide/render-function.html#%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BB%84%E4%BB%B6" target="_blank" rel="nofollow noopener noreferrer">详情看文档描述👉</a></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-comment">// 渲染el-input提供的slot</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderElInputSlots</span>(<span class="hljs-params">$scopedSlots</span>) </span>&#123;
  <span class="hljs-keyword">const</span> slots = <span class="hljs-built_in">Object</span>.keys($scopedSlots).map(<span class="hljs-function"><span class="hljs-params">slotName</span> =></span> &#123;
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'slot-content'</span>, &#123;
      <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">render</span>: $scopedSlots[slotName]
      &#125;,
      <span class="hljs-attr">slot</span>: slotName,
      <span class="hljs-attr">key</span>: slotName
    &#125;)
  &#125;)

  <span class="hljs-keyword">return</span> slots
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    h = <span class="hljs-built_in">this</span>.$createElement
    <span class="hljs-keyword">const</span> &#123;
      $scopedSlots,
    &#125; = <span class="hljs-built_in">this</span>

    <span class="hljs-comment">// 配置插槽(当用户传递了el-input提供的slot才去渲染)</span>
    <span class="hljs-keyword">let</span> elInputSlotsVNode = []
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.keys($scopedSlots).length) &#123;
      elInputSlotsVNode = renderElInputSlots($scopedSlots)
    &#125;

    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'el-input'</span>, &#123;
      <span class="hljs-comment">// ...</span>
    &#125;, elInputSlotsVNode)
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>「效果图💗」</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd2113774ce7440c8349b5f1c65e4da0~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">Autocomplete</h2>
<p>autocomplete 是一个可带输入建议的输入框组件。可用于远程搜索， 通过传递<code>is-autocomplete</code>来确定是否渲染<code>el-autocomplete</code>组件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4377dff447e4f60b6b3db25dbf6ddfe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意⚠：这里的is-autocomplete是用来判断是否渲染el-autocomplete组件的，并不是input提供的autocomplete属性</p>
</blockquote>























<table><thead><tr><th align="center"><strong>参数</strong></th><th align="center"><strong>说明</strong></th><th><strong>类型</strong></th><th align="center"><strong>默认值</strong></th></tr></thead><tbody><tr><td align="center"><code>is-autocomplete</code></td><td align="center">是否渲染成autocomplete组件</td><td><code>Boolean</code></td><td align="center"><code>false</code></td></tr><tr><td align="center"><code>fetch-suggestions</code></td><td align="center"><code>返回输入建议的方法，仅当你的输入建议数据 resolve 时，通过调用 callback(data:[]) 来返回它</code></td><td><code>Function</code></td><td align="center">必传</td></tr></tbody></table>
<p>详情请查看Element-Ui官网 <a href="https://element.eleme.cn/#/zh-CN/component/input" target="_blank" rel="nofollow noopener noreferrer">element.eleme.cn/#/zh-CN/com…</a></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">// 是否渲染el-autocomplete组件</span>
    <span class="hljs-attr">isAutocomplete</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-comment">// 支持el-input所有参数</span>
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-comment">// 最终要渲染的组件名称</span>
    <span class="hljs-attr">componentTag</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">&#123; isAutocomplete, $attrs &#125;</span>)</span> &#123;
        <span class="hljs-keyword">const</span> fetchSuggestions = $attrs[<span class="hljs-string">'fetch-suggestions'</span>]
        <span class="hljs-comment">// fetchSuggestions 返回输入建议的方法(isAutocomplete为true时必传)</span>
        <span class="hljs-keyword">return</span> isAutocomplete && <span class="hljs-keyword">typeof</span> fetchSuggestions === <span class="hljs-string">'function'</span>
          ? <span class="hljs-string">'el-autocomplete'</span>
          : <span class="hljs-string">'el-input'</span>
      &#125;
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    h = <span class="hljs-built_in">this</span>.$createElement
    <span class="hljs-keyword">const</span> &#123;
     componentTag
    &#125; = <span class="hljs-built_in">this</span>


    <span class="hljs-keyword">return</span> h(componentTag, &#123;
      <span class="hljs-comment">// ...</span>
    &#125;, elInputSlotsVNode)
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面实现的就类似于内置动态组件[component]组件的效果</p>
<p>至此这个组件就写完了，总的就100来行但相对来说很灵活了，后面在封装<code>Form</code>组件会将这个组件集成进去，这个时候就能很好的体现出render函数封装组件的灵活性</p>
<blockquote>
<p>在线卑微，如果觉得这篇文章对你有帮助的话欢迎大家点个赞👻</p>
</blockquote>
<h2 data-id="heading-7">写在最后</h2>
<p>如果文章中有那块写的不太好或有问题欢迎大家指出，我也会在后面的文章不停修改。也希望自己进步的同时能跟你们一起成长。喜欢我文章的朋友们也可以关注一下</p>
<p>我会很感激第一批关注我的人。<strong>此时，年轻的我和你，轻装上阵；而后，富裕的你和我，满载而归。</strong></p>
<h3 data-id="heading-8">业精于勤，荒于嬉</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad27a6da1b4046ed8e12e70ba786bf30~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">往期文章</h2>
<p><a href="https://juejin.cn/post/6894412199700201485" target="_blank">【建议追更】以模块化的思想来搭建中后台项目</a></p>
<p><a href="https://juejin.cn/post/6913092522814210061" target="_blank">【以模块化的思想开发中后台项目】第一章</a></p>
<p><a href="https://juejin.im/post/6868849475008331783" target="_blank" rel="nofollow noopener noreferrer">【前端体系】从一道面试题谈谈对EventLoop的理解</a> (更新了四道进阶题的解析)</p>
<p><a href="https://juejin.im/post/6867784542338416648" target="_blank" rel="nofollow noopener noreferrer">【前端体系】从地基开始打造一座万丈高楼</a></p>
<p><a href="https://juejin.im/post/6867784542338416648" target="_blank" rel="nofollow noopener noreferrer">【前端体系】正则在开发中的应用场景可不只是规则校验</a></p>
<p><a href="https://juejin.im/post/6878941871259779085" target="_blank" rel="nofollow noopener noreferrer">「函数式编程的实用场景 | 掘金技术征文-双节特别篇」</a></p>
<p><a href="https://juejin.cn/post/6888102016007176200" target="_blank">【建议收藏】css晦涩难懂的点都在这啦</a></p></div>  
</div>
            