
---
title: '回顾 vue 的 Render 函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfa6a62aa2b04678a75fc9a674555baf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 21:43:29 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfa6a62aa2b04678a75fc9a674555baf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Render 函数</h1>
<p>Vue 推荐在绝大多数情况下使用模板来创建你的 HTML。然而在一些场景中，你真的需要 JavaScript 的<code>完全编程</code>的能力。这时你可以用<strong>渲染函数</strong>，它比模板更接近编译器。</p>
<h2 data-id="heading-1">一、节点、树以及虚拟 DOM</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>My title<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  Some text content
  <span class="hljs-comment"><!-- <span class="hljs-doctag">TODO:</span> Add tagline --></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfa6a62aa2b04678a75fc9a674555baf~tplv-k3u1fbpfcp-watermark.image" alt="dom-tree.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>每个元素都是一个节点。每段文字也是一个节点。甚至注释也都是节点。一个节点就是页面的一个部分。就像家谱树一样，每个节点都可以有孩子节点 (也就是说每个部分可以包含其它的一些部分)。</p>
<p>高效地更新所有这些节点会是比较困难的，不过所幸你不必手动完成这个工作。你只需要告诉 Vue 你希望页面上的 HTML 是什么，这可以是在一个模板里：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; blogTitle &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者一个渲染函数里：</p>
<pre><code class="hljs language-js copyable" lang="js">render: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">createElement</span>) </span>&#123;
  <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'h1'</span>, <span class="hljs-built_in">this</span>.blogTitle)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这两种情况下，Vue 都会自动保持页面的更新，即便 <code>blogTitle</code> 发生了改变。</p>
<h2 data-id="heading-2">二、虚拟 DOM</h2>
<p>Vue 通过建立一个<strong>虚拟 DOM</strong> 来追踪自己要如何改变真实 DOM。请仔细看这行代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'h1'</span>, <span class="hljs-built_in">this</span>.blogTitle)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>createElement</code> 到底会返回什么呢？其实不是一个<em>实际的</em> DOM 元素。它更准确的名字可能是 <code>createNodeDescription</code>，因为它所包含的信息会告诉 Vue 页面上需要渲染什么样的节点，包括及其子节点的描述信息。我们把这样的节点描述为“虚拟节点 (virtual node)”，也常简写它为“<strong>VNode</strong>”。“虚拟 DOM”是我们对由 Vue 组件树建立起来的整个 VNode 树的称呼。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// @returns &#123;VNode&#125;</span>
createElement(
  <span class="hljs-comment">// &#123;String | Object | Function&#125;</span>
  <span class="hljs-comment">// 一个 HTML 标签名、组件选项对象，或者</span>
  <span class="hljs-comment">// resolve 了上述任何一种的一个 async 函数。必填项。</span>
  <span class="hljs-string">'div'</span>,

  <span class="hljs-comment">// &#123;Object&#125;</span>
  <span class="hljs-comment">// 一个与模板中 attribute 对应的数据对象。可选。</span>
  &#123;
    <span class="hljs-comment">// (详情见下一节)</span>
  &#125;,

  <span class="hljs-comment">// &#123;String | Array&#125;</span>
  <span class="hljs-comment">// 子级虚拟节点 (VNodes)，由 `createElement()` 构建而成，</span>
  <span class="hljs-comment">// 也可以使用字符串来生成“文本虚拟节点”。可选。</span>
  [
    <span class="hljs-string">'先写一些文字'</span>,
    createElement(<span class="hljs-string">'h1'</span>, <span class="hljs-string">'一则头条'</span>),
    createElement(MyComponent, &#123;
      <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">someProp</span>: <span class="hljs-string">'foobar'</span>
      &#125;
    &#125;)
  ]
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2.1 深入数据对象</h3>
<p>在渲染函数中，一些<code>模板属性</code>会在<code>Vnode</code>数据对象中有顶层字段，同时对象也允许绑定普通的属性，也允许绑定如 <code>innerHTML</code> 这样的 DOM property (这会覆盖 <code>v-html</code> 指令)。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-comment">// 与 `v-bind:class` 的 API 相同，</span>
  <span class="hljs-comment">// 接受一个字符串、对象或字符串和对象组成的数组</span>
  <span class="hljs-string">'class'</span>: &#123;
    <span class="hljs-attr">foo</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">bar</span>: <span class="hljs-literal">false</span>
  &#125;,
  <span class="hljs-comment">// 与 `v-bind:style` 的 API 相同，</span>
  <span class="hljs-comment">// 接受一个字符串、对象，或对象组成的数组</span>
  <span class="hljs-attr">style</span>: &#123;
    <span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span>,
    <span class="hljs-attr">fontSize</span>: <span class="hljs-string">'14px'</span>
  &#125;,
  <span class="hljs-comment">// 普通的 HTML attribute</span>
  <span class="hljs-attr">attrs</span>: &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-string">'foo'</span>
  &#125;,
  <span class="hljs-comment">// 组件 prop</span>
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">myProp</span>: <span class="hljs-string">'bar'</span>
  &#125;,
  <span class="hljs-comment">// DOM property</span>
  <span class="hljs-attr">domProps</span>: &#123;
    <span class="hljs-attr">innerHTML</span>: <span class="hljs-string">'baz'</span>
  &#125;,
  <span class="hljs-comment">// 事件监听器在 `on` 内，</span>
  <span class="hljs-comment">// 但不再支持如 `v-on:keyup.enter` 这样的修饰器。</span>
  <span class="hljs-comment">// 需要在处理函数中手动检查 keyCode。</span>
  <span class="hljs-attr">on</span>: &#123;
    <span class="hljs-attr">click</span>: <span class="hljs-built_in">this</span>.clickHandler
  &#125;,
  <span class="hljs-comment">// 仅用于组件，用于监听原生事件，而不是组件内部使用</span>
  <span class="hljs-comment">// `vm.$emit` 触发的事件。</span>
  <span class="hljs-attr">nativeOn</span>: &#123;
    <span class="hljs-attr">click</span>: <span class="hljs-built_in">this</span>.nativeClickHandler
  &#125;,
  <span class="hljs-comment">// 自定义指令。注意，你无法对 `binding` 中的 `oldValue`</span>
  <span class="hljs-comment">// 赋值，因为 Vue 已经自动为你进行了同步。</span>
  <span class="hljs-attr">directives</span>: [
    &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'my-custom-directive'</span>,
      <span class="hljs-attr">value</span>: <span class="hljs-string">'2'</span>,
      <span class="hljs-attr">expression</span>: <span class="hljs-string">'1 + 1'</span>,
      <span class="hljs-attr">arg</span>: <span class="hljs-string">'foo'</span>,
      <span class="hljs-attr">modifiers</span>: &#123;
        <span class="hljs-attr">bar</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;
  ],
  <span class="hljs-comment">// 作用域插槽的格式为</span>
  <span class="hljs-comment">// &#123; name: props => VNode | Array<VNode> &#125;</span>
  <span class="hljs-attr">scopedSlots</span>: &#123;
    <span class="hljs-attr">default</span>: <span class="hljs-function"><span class="hljs-params">props</span> =></span> createElement(<span class="hljs-string">'span'</span>, props.text)
  &#125;,
  <span class="hljs-comment">// 如果组件是其它组件的子组件，需为插槽指定名称</span>
  <span class="hljs-attr">slot</span>: <span class="hljs-string">'name-of-slot'</span>,
  <span class="hljs-comment">// 其它特殊顶层 property</span>
  <span class="hljs-attr">key</span>: <span class="hljs-string">'myKey'</span>,
  <span class="hljs-attr">ref</span>: <span class="hljs-string">'myRef'</span>,
  <span class="hljs-comment">// 如果你在渲染函数中给多个元素都应用了相同的 ref 名，</span>
  <span class="hljs-comment">// 那么 `$refs.myRef` 会变成一个数组。</span>
  <span class="hljs-attr">refInFor</span>: <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2.2 完整例子</h3>
<p><a href="https://codesandbox.io/s/pensive-bell-ks2mm" target="_blank" rel="nofollow noopener noreferrer">codesandbox.io/s/pensive-b…</a></p>
<h3 data-id="heading-5">2.3 约束</h3>
<h4 data-id="heading-6">VNode 必须唯一</h4>
<p>组件树中的所有 VNode 必须是唯一的。这意味着，下面的渲染函数是不合法的：</p>
<pre><code class="hljs language-js copyable" lang="js">render: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">createElement</span>) </span>&#123;
  <span class="hljs-keyword">var</span> myParagraphVNode = createElement(<span class="hljs-string">'p'</span>, <span class="hljs-string">'hi'</span>)
  <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'div'</span>, [
    <span class="hljs-comment">// 错误 - 重复的 VNode</span>
    myParagraphVNode, myParagraphVNode
  ])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你真的需要重复很多次的元素/组件，你可以使用工厂函数来实现。例如，下面这渲染函数用完全合法的方式渲染了 20 个相同的段落：</p>
<pre><code class="hljs language-js copyable" lang="js">render: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">createElement</span>) </span>&#123;
  <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'div'</span>,
    <span class="hljs-built_in">Array</span>.apply(<span class="hljs-literal">null</span>, &#123; <span class="hljs-attr">length</span>: <span class="hljs-number">20</span> &#125;).map(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'p'</span>, <span class="hljs-string">'hi'</span>)
    &#125;)
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">三、在<code>Render</code>函数中的模板功能</h2>
<h3 data-id="heading-8">3.1 <code>v-if</code> 和 <code>v-for</code></h3>
<p>只要在原生的 JavaScript 中可以轻松完成的操作，Vue 的渲染函数就不会提供专有的替代方法。比如，在模板中使用的 <code>v-if</code> 和 <code>v-for</code>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"items.length"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in items"</span>></span>&#123;&#123; item.name &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-else</span>></span>No items found.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些都可以在渲染函数中用 JavaScript 的 <code>if</code>/<code>else</code> 和 <code>map</code> 来重写：</p>
<pre><code class="hljs language-js copyable" lang="js">props: [<span class="hljs-string">'items'</span>],
<span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">createElement</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.items.length) &#123;
    <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'ul'</span>, <span class="hljs-built_in">this</span>.items.map(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">item</span>) </span>&#123;
      <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'li'</span>, item.name)
    &#125;))
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'p'</span>, <span class="hljs-string">'No items found.'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3.2 <code>v-model</code></h3>
<p>渲染函数中没有与 <code>v-model</code> 的直接对应——你必须自己实现相应的逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js">props: [<span class="hljs-string">'value'</span>],
<span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">createElement</span>) </span>&#123;
  <span class="hljs-keyword">var</span> self = <span class="hljs-built_in">this</span>
  <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'input'</span>, &#123;
    <span class="hljs-attr">domProps</span>: &#123;
      <span class="hljs-attr">value</span>: self.value
    &#125;,
    <span class="hljs-attr">on</span>: &#123;
      <span class="hljs-attr">input</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
        self.$emit(<span class="hljs-string">'input'</span>, event.target.value)
      &#125;
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是深入底层的代价，但与 <code>v-model</code> 相比，这可以让你更好地控制交互细节。</p>
<h3 data-id="heading-10">3.3 事件 & 按键修饰符</h3>
<p>对于 <code>.passive</code>、<code>.capture</code> 和 <code>.once</code> 这些事件修饰符，Vue 提供了相应的前缀可以用于 <code>on</code>：</p>

























<table><thead><tr><th align="left">修饰符</th><th align="left">前缀</th></tr></thead><tbody><tr><td align="left"><code>.passive</code></td><td align="left"><code>&</code></td></tr><tr><td align="left"><code>.capture</code></td><td align="left"><code>!</code></td></tr><tr><td align="left"><code>.once</code></td><td align="left"><code>~</code></td></tr><tr><td align="left"><code>.capture.once</code> 或 <code>.once.capture</code></td><td align="left"><code>~!</code></td></tr></tbody></table>
<p>例如：</p>
<pre><code class="hljs language-js copyable" lang="js">on: &#123;
  <span class="hljs-string">'!click'</span>: <span class="hljs-built_in">this</span>.doThisInCapturingMode,
  <span class="hljs-string">'~keyup'</span>: <span class="hljs-built_in">this</span>.doThisOnce,
  <span class="hljs-string">'~!mouseover'</span>: <span class="hljs-built_in">this</span>.doThisOnceInCapturingMode
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于所有其它的修饰符，私有前缀都不是必须的，因为你可以在事件处理函数中使用事件方法：</p>





























<table><thead><tr><th align="left">修饰符</th><th align="left">处理函数中的等价操作</th></tr></thead><tbody><tr><td align="left"><code>.stop</code></td><td align="left"><code>event.stopPropagation()</code></td></tr><tr><td align="left"><code>.prevent</code></td><td align="left"><code>event.preventDefault()</code></td></tr><tr><td align="left"><code>.self</code></td><td align="left"><code>if (event.target !== event.currentTarget) return</code></td></tr><tr><td align="left">按键： <code>.enter</code>, <code>.13</code></td><td align="left"><code>if (event.keyCode !== 13) return</code> (对于别的按键修饰符来说，可将 <code>13</code> 改为<a href="http://keycode.info/" target="_blank" rel="nofollow noopener noreferrer">另一个按键码</a>)</td></tr><tr><td align="left">修饰键： <code>.ctrl</code>, <code>.alt</code>, <code>.shift</code>, <code>.meta</code></td><td align="left"><code>if (!event.ctrlKey) return</code> (将 <code>ctrlKey</code> 分别修改为 <code>altKey</code>、<code>shiftKey</code> 或者 <code>metaKey</code>)</td></tr></tbody></table>
<p>这里是一个使用所有修饰符的例子：</p>
<pre><code class="hljs language-js copyable" lang="js">on: &#123;
  <span class="hljs-attr">keyup</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
    <span class="hljs-comment">// 如果触发事件的元素不是事件绑定的元素</span>
    <span class="hljs-comment">// 则返回</span>
    <span class="hljs-keyword">if</span> (event.target !== event.currentTarget) <span class="hljs-keyword">return</span>
    <span class="hljs-comment">// 如果按下去的不是 enter 键或者</span>
    <span class="hljs-comment">// 没有同时按下 shift 键</span>
    <span class="hljs-comment">// 则返回</span>
    <span class="hljs-keyword">if</span> (!event.shiftKey || event.keyCode !== <span class="hljs-number">13</span>) <span class="hljs-keyword">return</span>
    <span class="hljs-comment">// 阻止 事件冒泡</span>
    event.stopPropagation()
    <span class="hljs-comment">// 阻止该元素默认的 keyup 事件</span>
    event.preventDefault()
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3.4 插槽</h3>
<p>你可以通过 <a href="https://cn.vuejs.org/v2/api/#vm-slots" target="_blank" rel="nofollow noopener noreferrer"><code>this.$slots</code></a> 访问静态插槽的内容，每个插槽都是一个 VNode 数组：</p>
<pre><code class="hljs language-js copyable" lang="js">render: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">createElement</span>) </span>&#123;
  <span class="hljs-comment">// `<div><slot></slot></div>`</span>
  <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'div'</span>, <span class="hljs-built_in">this</span>.$slots.default)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以通过 <a href="https://cn.vuejs.org/v2/api/#vm-scopedSlots" target="_blank" rel="nofollow noopener noreferrer"><code>this.$scopedSlots</code></a> 访问作用域插槽，每个作用域插槽都是一个返回若干 VNode 的函数：</p>
<pre><code class="hljs language-js copyable" lang="js">props: [<span class="hljs-string">'message'</span>],
<span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">createElement</span>) </span>&#123;
  <span class="hljs-comment">// `<div><slot :text="message"></slot></div>`</span>
  <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'div'</span>, [
    <span class="hljs-built_in">this</span>.$scopedSlots.default(&#123;
      <span class="hljs-attr">text</span>: <span class="hljs-built_in">this</span>.message
    &#125;)
  ])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要用渲染函数向子组件中传递作用域插槽，可以利用 VNode 数据对象中的 <code>scopedSlots</code> 字段：</p>
<pre><code class="hljs language-js copyable" lang="js">render: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">createElement</span>) </span>&#123;
  <span class="hljs-comment">// `<div><child v-slot="props"><span>&#123;&#123; props.text &#125;&#125;</span></child></div>`</span>
  <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'div'</span>, [
    createElement(<span class="hljs-string">'child'</span>, &#123;
      <span class="hljs-comment">// 在数据对象中传递 `scopedSlots`</span>
      <span class="hljs-comment">// 格式为 &#123; name: props => VNode | Array<VNode> &#125;</span>
      <span class="hljs-attr">scopedSlots</span>: &#123;
        <span class="hljs-attr">default</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">props</span>) </span>&#123;
          <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'span'</span>, props.text)
        &#125;
      &#125;
    &#125;)
  ])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">3.5 例子</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; CreateElement, RenderContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue/types/umd'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">functional</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">row</span>: <span class="hljs-built_in">Object</span>,
    <span class="hljs-attr">render</span>: <span class="hljs-built_in">Function</span>,
    <span class="hljs-attr">index</span>: <span class="hljs-built_in">Number</span>,
    <span class="hljs-attr">column</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">null</span>
    &#125;
  &#125;,
  <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h: CreateElement, ctx: RenderContext</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> params: <span class="hljs-built_in">any</span> = &#123;
      <span class="hljs-attr">row</span>: ctx.props.row,
      <span class="hljs-attr">index</span>: ctx.props.index
    &#125;
    <span class="hljs-keyword">if</span> (ctx.props.column) params.column = ctx.props.column
    <span class="hljs-keyword">return</span> ctx.props.render(h, params)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            