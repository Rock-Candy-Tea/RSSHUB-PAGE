
---
title: 'Vue基础知识巩固之全面了解Vuex，比官方更易懂（下）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a132fe04ed8477d9a92dad2b772b761~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 26 Mar 2021 18:39:23 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a132fe04ed8477d9a92dad2b772b761~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Vuex进阶操作</h2>
<h3 data-id="heading-1">辅助函数</h3>
<h4 data-id="heading-2">mapState</h4>
<p>前面我们说了，在组件用访问store实例中的值时我们可以使用<code>computed</code>计算属性，如果我们访问某一个值还好，但是如果我们需要访问多个值时，就需要在<code>computed</code>中写多个计算属性，这样既不省事也不优雅，对于这样的情况，Vuex为我们准备了辅助函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在单独构建的版本中辅助函数为 Vuex.mapState</span>
<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">computed</span>: mapState(&#123;
    <span class="hljs-comment">// 箭头函数可使代码更简练</span>
    <span class="hljs-attr">count</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.count,

    <span class="hljs-comment">// 传字符串参数 'count' 等同于 `state => state.count`</span>
    <span class="hljs-attr">countAlias</span>: <span class="hljs-string">'count'</span>,

    <span class="hljs-comment">// 为了能够使用 `this` 获取局部状态，必须使用常规函数</span>
    countPlusLocalState (state) &#123;
      <span class="hljs-keyword">return</span> state.count + <span class="hljs-built_in">this</span>.localCount
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当映射的计算属性的名称与 state 的子节点名称相同时，我们也可以给 mapState 传一个字符串数组。</p>
<pre><code class="hljs language-js copyable" lang="js">computed: mapState([
  <span class="hljs-comment">// 映射 this.count 为 store.state.count</span>
  <span class="hljs-string">'count'</span>
])
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>mapState</code> 函数返回的是一个对象。我们如何将它与局部计算属性混合使用呢？通常，我们需要使用一个工具函数将多个对象合并为一个，以使我们可以将最终对象传给 computed 属性。但是自从有了对象展开运算符，我们可以极大地简化写法：</p>
<pre><code class="hljs language-js copyable" lang="js">computed: &#123;
  localComputed () &#123; <span class="hljs-comment">/* ... */</span> &#125;,
  <span class="hljs-comment">// 使用对象展开运算符将此对象混入到外部对象中</span>
  ...mapState(&#123;
    <span class="hljs-comment">// ...</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">mapGetters</h4>
<p><code>mapGetters</code> 也放在 <code>computed</code> 中，使用方法和<code>mapState</code>差不多</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapGetters &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">computed</span>: &#123;
  <span class="hljs-comment">// 使用对象展开运算符将 getter 混入 computed 对象中</span>
    ...mapGetters([
      <span class="hljs-string">'doneTodosCount'</span>,
      <span class="hljs-string">'anotherGetter'</span>,
      <span class="hljs-comment">// ...</span>
    ])
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你想将一个 getter 属性另取一个名字，使用对象形式：</p>
<pre><code class="hljs language-js copyable" lang="js">...mapGetters(&#123;
  <span class="hljs-comment">// 把 `this.doneCount` 映射为 `this.$store.getters.doneTodosCount`</span>
  <span class="hljs-attr">doneCount</span>: <span class="hljs-string">'doneTodosCount'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">mapMutations</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapMutations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">methods</span>: &#123;
    ...mapMutations([
      <span class="hljs-string">'increment'</span>, <span class="hljs-comment">// 将 `this.increment()` 映射为 `this.$store.commit('increment')`</span>

      <span class="hljs-comment">// `mapMutations` 也支持载荷：</span>
      <span class="hljs-string">'incrementBy'</span> <span class="hljs-comment">// 将 `this.incrementBy(amount)` 映射为 `this.$store.commit('incrementBy', amount)`</span>
    ]),
    ...mapMutations(&#123;
      <span class="hljs-attr">add</span>: <span class="hljs-string">'increment'</span> <span class="hljs-comment">// 将 `this.add()` 映射为 `this.$store.commit('increment')`</span>
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">mapActions</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">methods</span>: &#123;
    ...mapActions([
      <span class="hljs-string">'increment'</span>, <span class="hljs-comment">// 将 `this.increment()` 映射为 `this.$store.dispatch('increment')`</span>

      <span class="hljs-comment">// `mapActions` 也支持载荷：</span>
      <span class="hljs-string">'incrementBy'</span> <span class="hljs-comment">// 将 `this.incrementBy(amount)` 映射为 `this.$store.dispatch('incrementBy', amount)`</span>
    ]),
    ...mapActions(&#123;
      <span class="hljs-attr">add</span>: <span class="hljs-string">'increment'</span> <span class="hljs-comment">// 将 `this.add()` 映射为 `this.$store.dispatch('increment')`</span>
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">modules</h3>
<p>在写Vue项目时，如果一个项目过于庞大，我们会对项目进行拆分成一个个单独的组件，Vuex也是如此，当一个store实例中存储了过多内容的时候，它将变得非常臃肿，此时，我们也可以将它拆分成一个个单独的组件，类似于下面这样。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)

<span class="hljs-keyword">const</span> moduleA = &#123;
  <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> (&#123; <span class="hljs-attr">count</span>: <span class="hljs-number">5</span> &#125;),
  <span class="hljs-attr">mutations</span>: &#123;
    increment (state) &#123;
      state.count++
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123; &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-string">'moduleA'</span> &#125;
  &#125;
&#125;
<span class="hljs-keyword">const</span> moduleB = &#123;
  <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> (&#123; <span class="hljs-attr">count</span>: <span class="hljs-number">10</span> &#125;),
  <span class="hljs-attr">mutations</span>: &#123;
    increment (state) &#123;
      state.count++
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123; &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-string">'moduleB'</span> &#125;
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
  &#125;,
  <span class="hljs-attr">modules</span>: &#123;
    <span class="hljs-attr">a</span>: moduleA,
    <span class="hljs-attr">b</span>: moduleB
  &#125;
&#125;)


<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">模块的局部状态</h4>
<p>对于模块内部的 mutation 和 getter，接收的第一个参数是模块的局部状态对象。</p>
<p>同样，对于模块内部的 action，访问模块内部的state可以使用 context.state ，访问根节点的state则可以使用context.rootState：</p>
<p>对于模块内部的 getter，根节点state会作为第三个参数传递进去（顺序不能错）</p>
<pre><code class="hljs language-js copyable" lang="js">getters: &#123;
    sumWithRootCount (state, getters, rootState) &#123;
      <span class="hljs-keyword">return</span> state.count + rootState.count
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那我们如何去访问module中的状态和mutation等呢？在module中，state是module的局部状态，所以我们可以这样访问</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$store.state.a.count <span class="hljs-comment">// -> 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下，模块内部的 action、mutation 和 getter 是注册在全局命名空间的——这样使得多个模块能够对同一 mutation 或 action 作出响应。举个栗子</p>
<pre><code class="hljs language-js copyable" lang="js">  mounted () &#123;
    <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'increment'</span>)
    &#125;, <span class="hljs-number">1000</span>)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a132fe04ed8477d9a92dad2b772b761~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们触发一个Mutation时，模块内部的同名Mutation会同时被触发，两个模块内的state都发生了改变。action同样会如此，就不演示了，至于getters，同样会被注册到全局命名空间，如果两个module内有同名的getter，则以先引入的module为主。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)

<span class="hljs-keyword">const</span> moduleA = &#123;
  <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> (&#123; <span class="hljs-attr">count</span>: <span class="hljs-number">5</span> &#125;),
  <span class="hljs-attr">mutations</span>: &#123;
    increment (state) &#123;
      state.count++
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123; &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-string">'moduleA'</span> &#125;
  &#125;
&#125;
<span class="hljs-keyword">const</span> moduleB = &#123;
  <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> (&#123; <span class="hljs-attr">count</span>: <span class="hljs-number">10</span> &#125;),
  <span class="hljs-attr">mutations</span>: &#123;
    increment (state) &#123;
      state.count++
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123; &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-string">'moduleB'</span> &#125;
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
  &#125;,
  <span class="hljs-attr">modules</span>: &#123;
    <span class="hljs-attr">a</span>: moduleA,
    <span class="hljs-attr">b</span>: moduleB
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$store.getters.name <span class="hljs-comment">// -> 'moduleA'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">命名空间</h4>
<p>那么，如果我们就想保持每个模块独立，不去影响全局空间，保持更好的封装性怎么办呢？Vuex给我们提供了提供了开启<strong>命名空间</strong>的选项，我们只需要在模块内部添加 <code>namespaced: true</code> 即可开启模块的命名空间。</p>
<p>开启了命名空间后，当前模块内的getter 和 action 会收到局部化的 getter，dispatch 和 commit，所以我们的代码无需做任何改变，但是我们在外部也就是vue组件内调用模块内的getters、actions和mutations时则需要加上模块名，由于state本来就是模块内的局部状态，所以加不加命名空间都一样</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">modules</span>: &#123;
    <span class="hljs-comment">// 模块名：account</span>
    <span class="hljs-attr">account</span>: &#123;
      <span class="hljs-attr">namespaced</span>: <span class="hljs-literal">true</span>,

      <span class="hljs-comment">// 模块内容（module assets）</span>
      <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> (&#123; ... &#125;), <span class="hljs-comment">// 模块内的状态已经是嵌套的了，使用 `namespaced` 属性不会对其产生影响 </span>
      <span class="hljs-attr">getters</span>: &#123;
        isAdmin () &#123; ... &#125; <span class="hljs-comment">// -> this.$store.getters['account/isAdmin']</span>
      &#125;,
      <span class="hljs-attr">actions</span>: &#123;
        login () &#123; ... &#125; <span class="hljs-comment">// -> this.$store.dispatch('account/login')</span>
      &#125;,
      <span class="hljs-attr">mutations</span>: &#123;
        login () &#123; ... &#125; <span class="hljs-comment">// -> this.$store.commit('account/login')</span>
      &#125;,

      <span class="hljs-comment">// 嵌套模块</span>
      <span class="hljs-attr">modules</span>: &#123;
        <span class="hljs-comment">// 继承父模块的命名空间</span>
        <span class="hljs-attr">myPage</span>: &#123;
          <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> (&#123; ... &#125;),
          <span class="hljs-attr">getters</span>: &#123;
            profile () &#123; ... &#125; <span class="hljs-comment">// -> this.$store.getters['account/profile']</span>
          &#125;
        &#125;,

        <span class="hljs-comment">// 进一步嵌套命名空间</span>
        <span class="hljs-attr">posts</span>: &#123;
          <span class="hljs-attr">namespaced</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> (&#123; ... &#125;),
          <span class="hljs-attr">getters</span>: &#123;
            popular () &#123; ... &#125; <span class="hljs-comment">// -> this.$store.getters['account/posts/popular']</span>
          &#125;
        &#125;
      &#125;
    &#125;
  &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么如果我们开启了命名空间，又想在模块内部访问全局内容怎么办？</p>
<p>在 getter 中，我们可以接收第三个参数 <code>rootState</code>访问全局的 state 和 第四个参数 <code>rootGetters</code> 访问全局的getter</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 模块内部</span>
<span class="hljs-attr">getters</span>:&#123;
  someGetter (state, getters, rootState, rootGetters) &#123;
    ...
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们想要在模块内部的action中调用全局的action或者Mutation，只需要在调用的时候将 <code>&#123; root: true &#125;</code> 作为第三参数传给 dispatch 或 commit 即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 模块内部</span>
<span class="hljs-attr">actions</span>: &#123;
    someAction (&#123;dispatch, commit&#125;) &#123;
        dispatch(<span class="hljs-string">'someOtherAction'</span>, <span class="hljs-literal">null</span>, &#123; <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span> &#125;)
        commit(<span class="hljs-string">'someMutation'</span>, <span class="hljs-literal">null</span>, &#123; <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span> &#125;)
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在带命名空间的模块注册全局 action</strong>
若需要在带命名空间的模块注册全局 action，你可添加 <code>root: true</code>，并将这个 action 的定义放在函数 <code>handler</code> 中。就像我们需要深度监听时候使用watch一样，例如：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 模块内部</span>
  <span class="hljs-attr">namespaced</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">actions</span>: &#123;
    <span class="hljs-attr">someAction</span>: &#123;
      <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 此action将被注册到全局空间内</span>
      handler (namespacedContext, payload) &#123; ... &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还记得我们上面的辅助函数吗？那如果我们在模块内部开启了命名空间，又该如何去使用辅助函数呢？</p>
<p><em>mapGetters 和 mapState用法差不多，mapActions 和 mapMutations 用法差不错，这里就不重复演示了</em></p>
<p>我们共有三种方法去使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> moduleA = &#123;
  <span class="hljs-attr">namespaced</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> (&#123; <span class="hljs-attr">count</span>: <span class="hljs-number">5</span> &#125;),
  <span class="hljs-attr">mutations</span>: &#123;
    addMutation (state) &#123;...&#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
    addAction (&#123;commit&#125;) &#123;...&#125;
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">1</span>
  &#125;,
  <span class="hljs-attr">modules</span>: &#123;
    moduleA <span class="hljs-comment">// moduleA:moduleA 使用ES6的语法简写为 moduleA</span>
  &#125;
&#125;)



<span class="hljs-comment">// => 可以简化为</span>

<span class="hljs-attr">computed</span>: &#123;
  ...mapState(<span class="hljs-string">'moduleA'</span>, &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.count
  &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一种：在用的时候带上路径</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapState, mapMutations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-attr">computed</span>: &#123;
  ...mapState(&#123;
    <span class="hljs-attr">count</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.moduleA.count <span class="hljs-comment">// => 5</span>
  &#125;)
&#125;,
<span class="hljs-attr">methods</span>: &#123;
  ...mapMutations([
    <span class="hljs-string">'moduleA/addMutation'</span> <span class="hljs-comment">// 用的时候 this['moduleA/addMutation']()</span>
  ])
  ...mapMutations(&#123;
    <span class="hljs-attr">addMutation</span>: <span class="hljs-string">'moduleA/addMutation'</span> <span class="hljs-comment">// 用的时候 this.addMutation()</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二种：在第一个参数传入module名</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapState, mapMutations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-attr">computed</span>: &#123;
  ...mapState(‘moduleA’, &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.count <span class="hljs-comment">// => 5</span>
  &#125;)
&#125;,
<span class="hljs-attr">methods</span>: &#123;
  ...mapMutations(‘moduleA’, [
    <span class="hljs-string">'addMutation'</span> <span class="hljs-comment">// 用的时候 this.addMutation()</span>
  ])
  ...mapMutations(‘moduleA’, &#123;
    <span class="hljs-attr">addMutation</span>: <span class="hljs-string">'addMutation'</span> <span class="hljs-comment">// 用的时候 this.addMutation()</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三种：使用 <code>createNamespacedHelpers</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createNamespacedHelpers &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">const</span> &#123; mapState, mapMutations &#125; = createNamespacedHelpers(<span class="hljs-string">'moduleA'</span>)

<span class="hljs-attr">computed</span>: &#123;
  ...mapState(&#123;
    <span class="hljs-attr">count</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.count <span class="hljs-comment">// => 5</span>
  &#125;)
&#125;,
<span class="hljs-attr">methods</span>: &#123;
  ...mapMutations([
    <span class="hljs-string">'addMutation'</span> <span class="hljs-comment">// 用的时候 this.addMutation()</span>
  ])
  ...mapMutations(&#123;
    <span class="hljs-attr">addMutation</span>: <span class="hljs-string">'addMutation'</span> <span class="hljs-comment">// 用的时候 this.addMutation()</span>
  &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">模块重用</h4>
<p>有时我们可能需要创建一个模块的多个实例，例如：</p>
<ul>
<li>创建多个 store，他们公用同一个模块 (例如当 runInNewContext 选项是 false 或 'once' 时，为了在服务端渲染中避免有状态的单例 )</li>
<li>在一个 store 中多次注册同一个模块</li>
</ul>
<p>如果我们使用一个纯对象来声明模块的状态，那么这个状态对象会通过引用被共享，导致状态对象被修改时 store 或模块间数据互相污染的问题。</p>
<p>实际上这和 Vue 组件内的 data 是同样的问题。因此解决办法也是相同的——使用一个函数来声明模块状态（仅 2.3.0+ 支持）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MyReusableModule = &#123;
  <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> (&#123;
    <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span>
  &#125;),
  <span class="hljs-comment">// mutation, action 和 getter 等等...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">扩展知识</h2>
<h3 data-id="heading-11">v-model双向绑定state中的值</h3>
<p>官方不推荐我们直接使用 v-model 直接去绑定state中的值，并且如果我们开启了严格模式，这样做还会报错，那如果我们用vue的思维去解决这个问题，就是使用v-model绑定一个值，然后去监听这个值的变化，之后使用commit去改变state中的值，这样做难免过于繁琐，官方推荐的最优雅的方式是去利用计算属性的 <code>getter</code> 和 <code>setter</code> 属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
<span class="hljs-attr">mutations</span>: &#123;
  updateMessage (state, message) &#123;
    state.obj.message = message
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"message"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
<span class="hljs-attr">computed</span>: &#123;
  <span class="hljs-attr">message</span>: &#123;
    get () &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$store.state.obj.message
    &#125;,
    set (value) &#123;
      <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'updateMessage'</span>, value)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好啦，本篇文章的内容就到此为止啦，时间仓促，知识繁多，学艺不精，难免出错，如果各位大佬有人发现文中不对的地方，希望给与指正，谢谢，希望可以帮到大家，祝大家工作顺利😄</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            