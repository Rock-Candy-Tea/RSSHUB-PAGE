
---
title: '卷死了！再不学vue3就没有人要你了！速来围观vue3新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ae3dbeb906d47d09f8b438b71344bbb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 16:03:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ae3dbeb906d47d09f8b438b71344bbb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">一文入门了解vue3新特性</h1>
<p>这是我参与更文挑战的第22天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>紧跟新技术的步伐，周一也开始学起了 <code>vue3</code> 。去年11月份的时候对 <code>vue3</code> 其实已经有所耳闻，但当时对 <code>vue3</code> 完全没有想学习的欲望。当时就觉得，够用就行，新技术那么多哪里学得动。然而现在……悔不当初😭，时代在推你进步，你却停滞不前，只会被时代淘汰。迫于内卷压力，再不学 <code>vue3</code> 真的感觉在跟时代划一道鸿沟。</p>
<p>所以，今年赶忙把 <code>vue3</code> 提上日程。原本 <code>vue3</code> 的学习计划是在三月份，但因为各种事情耽搁了到了现阶段才进行。</p>
<p><strong>求求别再卷了</strong>……我学❗❗我学❗❗</p>
<p>在今天的这篇文章中，将带领大家全面了解 <code>vue3</code>  的新特性，<code>vue3</code> 与 <code>vue2</code> 的一些区别， <code>Composition API</code> 和 <code>Options API</code> 的区别。</p>
<p>下面开始进行本文的讲解🤪</p>
<h1 data-id="heading-1">一、😶vue3比vue2有什么优势？</h1>
<p>vue3比vue2来说，<strong>性能上更好</strong>，<strong>代码体积更小</strong>，并且有<strong>更好的ts支持</strong>。</p>
<p>同时，更为突出的特点是，vue3有<strong>更好的代码组织能力</strong>，有<strong>更好的逻辑抽离能力</strong>，并且还有<strong>更多各式各样的新功能</strong>。</p>
<p>其中尤为突出的就是大家平常耳熟能详的 <code>Composition API</code> 和 <code>Options API</code> 。</p>
<p>那是不是 <code>vue3</code> 就一定比 <code>vue2</code> 好呢？或者是 <code>Composition API</code> 就一定比 <code>Options API</code> 好呢？</p>
<p>其实大家心里可能在此打下了一个问号⁉️</p>
<p>那接下来就带着这个问号，一起来了解 <code>vue3</code> 的新特性吧！</p>
<h1 data-id="heading-2">二、🧐Vue3升级了哪些重要的功能</h1>
<h2 data-id="heading-3">1、createApp</h2>
<p>与 <code>vue2</code> 不同的是， <code>vue2</code> 使用 <code>new</code> 的方式来<strong>初始化一个实例</strong>，而 <code>vue3</code> 则用 <code>Vue.createApp</code> 来<strong>初始化一个实例</strong>。<strong>如下所示：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//vue2.x 实例化方式</span>
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123; <span class="hljs-comment">/*选项*/</span> &#125;)
<span class="hljs-comment">//vue2.x 使用方式</span>
Vue.use(<span class="hljs-comment">/*...*/</span>)
Vue.mixin(<span class="hljs-comment">/*...*/</span>)
Vue.component(<span class="hljs-comment">/*...*/</span>)
Vue.directive(<span class="hljs-comment">/*...*/</span>)

<span class="hljs-comment">//vue3 实例化方式</span>
<span class="hljs-keyword">const</span> app = Vue.createApp(&#123; <span class="hljs-comment">/*选项*/</span> &#125;)
<span class="hljs-comment">//vue3 使用方式</span>
app.use(<span class="hljs-comment">/*...*/</span>)
app.mixin(<span class="hljs-comment">/*...*/</span>)
app.component(<span class="hljs-comment">/*...*/</span>)
app.directive(<span class="hljs-comment">/*...*/</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">2、emits(父子组件间的通信)</h2>
<h3 data-id="heading-5">（1）通信方式</h3>

















<table><thead><tr><th align="center">传递形式</th><th align="center">通信方式</th></tr></thead><tbody><tr><td align="center">emits</td><td align="center">子组件向父组件传递数据</td></tr><tr><td align="center">props</td><td align="center">父组件的数据需要通过props把数据传给子组件，props的取值可以是<strong>数组</strong>也可以是<strong>对象</strong></td></tr></tbody></table>
<h3 data-id="heading-6">（2）举个例子🌰</h3>
<p>在 <code>vue2 </code>的时候，我们可以用 <code>$emit</code> 和 <code>props</code> 来进行<strong>父子组件间的通信</strong>。而现在， <code>vue3</code> 使用 <code>emits</code> 和 <code>props</code> 来实现<strong>父子组件间的通信</strong>。</p>
<p>我们定义一个父组件， 名字叫 <code>App.vue</code> ，<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">HelloWorld</span> <span class="hljs-attr">msg</span>=<span class="hljs-string">"Hello Vue 3.0 + Vite"</span> @<span class="hljs-attr">onSayHello</span>=<span class="hljs-string">"sayHello"</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> HelloWorld <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/HelloWorld.vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-attr">components</span>: &#123;
    HelloWorld,
  &#125;,

  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'hello vue3'</span>
    &#125; 
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params">info</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>, info)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再定义一个子组件，名字叫 <code>HelloWorld.vue</code> ，<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'HelloWorld'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">msg</span>: <span class="hljs-built_in">String</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      
    &#125;
  &#125;,
  <span class="hljs-attr">emits</span>: [<span class="hljs-string">'onSayHello'</span>],
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, &#123; emit &#125;</span>)</span> &#123;
    emit(<span class="hljs-string">'onSayHello'</span>, <span class="hljs-string">'vue3'</span>)
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>此时浏览器的显示效果如下：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ae3dbeb906d47d09f8b438b71344bbb~tplv-k3u1fbpfcp-zoom-1.image" alt="emits" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 <code>vue3</code> 中，可以直接将 <code>emit</code> 参数传入 <code>setup</code> 生命周期里面，来达到<strong>父子组件的通信</strong>。</p>
<h2 data-id="heading-7">3、多事件处理</h2>
<p>在 <code>vue2</code> 时，每一个点击只能定义一个事件；而在 <code>vue3</code> 时，打破原有的规则，每一个 <code>@click</code> 可以<strong>点击多个事件</strong>。<strong>如下代码所示：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 在 methods 里定义 one two 两个函数 --></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"one($event), two($event)"</span>></span>
submit
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">4、Fragment</h2>
<p><code>fragment</code> ，中文翻译过来就是<strong>碎片</strong>的意思。</p>
<p>在 <code>vue2.x</code> 时，是不允许有碎片存在的。所以我们每次在写程序时，最外层总要再给它包个 <code>div</code> 。但这个时候就会感觉特别麻烦，因为有时候想这个 <code>div</code> 的 <code>class</code> 名还得思考给命个什么名字好，感觉心里都已经没墨水了。</p>
<p>因此，在 <code>vue3 </code> 时，就除去了这个规范，可以不用最外层再包个 <code>div</code> 。<strong>如下代码所示：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- vue2.x 组件模板 --></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"detail"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;&#123; title &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-html</span>=<span class="hljs-string">"content"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- vue3 组件模板 --></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;&#123;title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-html</span>=<span class="hljs-string">"content"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">5、移除.sync</h2>
<h3 data-id="heading-10">（1）vue2</h3>
<p>在 <code>vue2</code> 时，我们会通过 <code>v-bind:title.sync</code> 来进行<strong>数据双向绑定</strong>。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- vue2.x --></span>
<span class="hljs-tag"><<span class="hljs-name">MyComponent</span> <span class="hljs-attr">v-bind:title.sync</span>=<span class="hljs-string">"title"</span>></span><span class="hljs-tag"></<span class="hljs-name">MyComponent</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">（2）vue3</h3>
<p>而在 <code>vue3</code> 时，直接放弃掉  <code>.sync</code> 而使用 <code>v-model</code> 的形式来对数据进行绑定。<strong>具体代码对下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- vue3.x --></span>
<span class="hljs-tag"><<span class="hljs-name">MyComponent</span> <span class="hljs-attr">v-model:title</span>=<span class="hljs-string">"title"</span>></span><span class="hljs-tag"></<span class="hljs-name">MyComponent</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再用一个例子🌰来展示 <code>vue3</code> 是怎么对数据进行双向绑定的。<strong>具体代码如下：</strong></p>
<p>我们先定义一个子组件，名字叫 <code>UserInfo.vue</code> ，<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"name"</span> @<span class="hljs-attr">input</span>=<span class="hljs-string">"$emit('update:name', $event.target.value)"</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"age"</span> @<span class="hljs-attr">input</span>=<span class="hljs-string">"$emit('update:age', $event.target.value)"</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'UserInfo'</span>,
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-built_in">String</span>
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来定义一个父组件，名字叫 <code>index.vue</code> ，<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;name&#125;&#125; &#123;&#123;age&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">user-info</span>
        <span class="hljs-attr">v-model:name</span>=<span class="hljs-string">"name"</span>
        <span class="hljs-attr">v-model:age</span>=<span class="hljs-string">"age"</span>
    ></span><span class="hljs-tag"></<span class="hljs-name">user-info</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; reactive, toRefs &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> UserInfo <span class="hljs-keyword">from</span> <span class="hljs-string">'./UserInfo.vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'VModel'</span>,
    <span class="hljs-attr">components</span>: &#123; UserInfo &#125;,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> state = reactive(&#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'monday'</span>,
            <span class="hljs-attr">age</span>: <span class="hljs-string">'18'</span>
        &#125;)

        <span class="hljs-keyword">return</span> toRefs(state)
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>此时浏览器的显示效果如下：</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/917ebfb20ee6440784e5bfab7390e8a1~tplv-k3u1fbpfcp-zoom-1.image" alt="v-model" loading="lazy" referrerpolicy="no-referrer">
此时，我们可以得出结论：子组件通过控制 <code>:value</code> 和 <code>@input</code> 来控制input的值，同时父组件通过 <code>v-model:propertyName</code> 来绑定子组件的值，这样一来，两者就实现了<strong>双向数据绑定</strong>。</p>
<h2 data-id="heading-12">6、异步组件</h2>
<p>在 <code>vue2</code> 时，引入异步组件的方法比较简单，直接使用import即可。<strong>代码如下：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Vue(&#123;
<span class="hljs-comment">//…</span>
<span class="hljs-attr">components</span>:&#123;
<span class="hljs-string">'my-component'</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./my-async-component.vue'</span>)
&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而在 <code>vue3</code> 时，引入异步组件需要使用 <code>defineAsyncComponent</code> 方法来进行引入。<strong>代码如下：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp, defineAsyncComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">new</span> Vue(&#123;
<span class="hljs-comment">//…</span>
<span class="hljs-attr">components</span>:&#123;
<span class="hljs-attr">AsyncComponent</span>: defineAsyncComponent(<span class="hljs-function">() =></span>
<span class="hljs-keyword">import</span>(<span class="hljs-string">'./components/AsyncComponent.vue'</span>)
)
&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">7、移除filter</h2>
<p>在 <code>vue2</code> 时，有 <code>filter</code> 这个功能，但其实这个功能的使用频率还挺低的。所以，在 <code>vue3</code> 中，彻底去除了 <code>filter</code> 这个功能，不再可用。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 以下filter在vue3中不再可用！！ --></span>
<span class="hljs-comment"><!-- 在双花括号中 --></span>
&#123;&#123; message | capitalize &#125;&#125;

<span class="hljs-comment"><!-- 在v-bind中使用 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind:id</span>=<span class="hljs-string">"rawId | formatId"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">8、Teleport</h2>
<p><code>Teleport</code> ，中文翻译过来就是<strong>远距离传送</strong>。在 <code>vue2</code> 中，比如我们要定义点击某个按钮，去跳转一个模态框，这个时候一般需要去操作 <code>DOM</code> 元素，或者再定义一个新的组件。但是在 <code>vue3</code> ，我们可以用 <code>teleport</code> 来解决。我们可以使用 <code>teleport</code> 来直接定义在当前组件中，之后通过v-if等方式来控制其显示与否。<strong>演示代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- data 中设置modalOpen: false --></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"modalOpen = true"</span>></span>
    Open full scree modal!(With teleport!)
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">teleport</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"body"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"modalOpen"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"modal"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            telePort 弹窗(父元素是body)
            <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"modalOpen = false"</span>></span>Colse<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">teleport</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">9、Suspense</h2>
<p>Suspense，是对vue2.x中的<strong>插槽</strong>做一个封装，这里不进行一一讲解。<strong>下面给出代码演示：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">Suspense</span>></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Test1</span>/></span> <span class="hljs-comment"><!--  是一个异步组件 --></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    
    <span class="hljs-comment"><!-- #fallback就是一个具名插槽。即Suspense组件内部，有两个slot，其中一个具名为 fallback --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> #<span class="hljs-attr">fallback</span>></span>
    Loading...
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">Suspense</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">三、😜Options API 和 Composition API</h1>
<h2 data-id="heading-17">1、生命周期对比</h2>
<p>以下给出 <code>Vue2</code> 与 <code>Vue3</code> 生命周期的对比。</p>


















































<table><thead><tr><th align="center">Vue2生命周期(Options API)</th><th align="center">Vue3生命周期(Composition API)</th><th align="center">含义</th></tr></thead><tbody><tr><td align="center">beforeCreate</td><td align="center">setup</td><td align="center">在实例初始化之后，数据观测(data observer) 和 event/watcher 事件配置之前被调用</td></tr><tr><td align="center">created</td><td align="center">setup</td><td align="center">页面还没有渲染，但是vue的实例已经初始化结束。</td></tr><tr><td align="center">beforeMount</td><td align="center">onBeforeMount</td><td align="center">在挂载开始之前被调用：相关的 render 函数首次被调用。</td></tr><tr><td align="center">mounted</td><td align="center">onMounted</td><td align="center">页面已经渲染完毕。</td></tr><tr><td align="center">beforeUpdate</td><td align="center">onBeforeUpdate</td><td align="center">数据更新时调用，发生在虚拟 DOM 重新渲染和打补丁之前。你可以在这个钩子中进一步地更改状态，这不会触发附加的重渲染过程。</td></tr><tr><td align="center">updated</td><td align="center">onUpdated</td><td align="center">由于数据更改导致的虚拟 DOM 重新渲染和打补丁，在这之后会调用该钩子。当这个钩子被调用时，组件 DOM 已经更新，所以你现在可以执行依赖于 DOM 的操作。</td></tr><tr><td align="center">beforeDestory</td><td align="center">onBeforeUnmount</td><td align="center">实例销毁之前调用。在这一步，实例仍然完全可用。</td></tr><tr><td align="center">destroy</td><td align="center">onUnmounted</td><td align="center">Vue 实例销毁后调用。</td></tr></tbody></table>
<h2 data-id="heading-18">2、Composition API 和 Options API 对比</h2>
<h3 data-id="heading-19">（1）Composition API带来了什么？</h3>
<p><code>Composition API</code> 相较于 <code>Options API</code> 来说，拥有更好的代码组织能力，更好的逻辑复用能力，以及更好的类型推导。</p>
<p>这里引用<strong>大帅老师</strong>的几张动图来对 <code>Composition API</code> 和 <code>Options API</code> 做一个对比。原文搓👉<a href="https://juejin.cn/post/6890545920883032071" target="_blank">做了一夜动画，就为让大家更好的理解Vue3的Composition Api</a>，再悄悄告诉各位小伙伴，大帅老师的文章融入大量的动画，通俗易懂，路过的小伙伴赶紧<a href="https://juejin.cn/user/2955079655898093/posts" target="_blank">关注一波</a>哦，学习路上不迷路🚦</p>
<p>废话不多说，赶紧来看看 <code>Options API</code> 和 <code>Composition API</code> 的区别。</p>
<p><strong>Options API：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/872d46f3aa1a4c3f93fb57bbf09da728~tplv-k3u1fbpfcp-zoom-1.image" alt="options API" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f2300264f394d838687d55d092216c9~tplv-k3u1fbpfcp-zoom-1.image" alt="options API" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Composition API：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/727c00d5c6f94bde9b0d9184f29ec70b~tplv-k3u1fbpfcp-zoom-1.image" alt="composition API" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6196c1ed518c443a9d9f456a987e58ad~tplv-k3u1fbpfcp-zoom-1.image" alt="composition API" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上图中可以看到，对于 <code>Options API</code> 来说，它的逻辑是散落在各处的，懒懒散散的。假设我们现在有一个功能要实现，而这个功能的逻辑代码有<strong>2000-3000行</strong>，试想一下，如果我们用 <code>Options API</code> 来实现的话，假设这个功能在 <code>methods</code> 里面有定义了一个方法，然后呢又要<strong>滑动一两千行</strong>去 <code>mounted</code> 里面看挂载的内容，这真的是出奇的浪费时间呐！所以， <code>vue3</code> 提出了 <code>composition API</code> ，就来解决这个问题了。</p>
<p><code>composition API</code> 把代码的逻辑抽离出来封装，并把封装的内容直接引用到生命周期里面，这样使用起来真的方便太多了。</p>
<p>我们举个简单的例子来看看 <code>composition API</code> 的使用方式。<strong>如下代码所示：</strong></p>
<p><strong>抽离某个逻辑放在同一个函数上：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> a = ref(<span class="hljs-number">10</span>);
    <span class="hljs-keyword">let</span> b = computed(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> a.value * <span class="hljs-number">2</span>
    &#125;)
    
    <span class="hljs-keyword">const</span> handleSum = <span class="hljs-function">() =></span> &#123;
        a.value = a.value + b
    &#125;
    
    <span class="hljs-keyword">return</span> &#123;
        a,
        b,
        handleSum
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>将sum函数逻辑放在组件中使用：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">const</span> &#123; a, b, handleSum &#125; = sum();
        <span class="hljs-keyword">return</span> &#123;
            a,
            b,
            handleSum
        &#125;
&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>综上可以得出，对于一个项目来说，尤其是代码量越多，逻辑越复杂的， <code>Composition API</code> 的优势会更加明显。<strong>那对于一个项目来说，我们应该在这两者中如何抉择而选择更好的方案呢？</strong> 接着我们继续往下看。</p>
<h3 data-id="heading-20">（2）Composition API和Options API如何选择？</h3>
<p>通过上面的分析我们可以知道， <code>Composition API</code> 虽然好用，但也不能乱用。因此，对于 <code>Composition API</code> 和 <code>Options API</code> 的使用，<strong>主要有以下几点建议：</strong></p>
<ul>
<li>两者不建议共用，不然很容易引起混乱；</li>
<li>对于小型项目、或者业务逻辑比较简单的项目，建议使用 <code>Options API</code> ；</li>
<li>对于中大型项目、或者逻辑比较复杂的项目，建议使用 <code>Composition API</code> ，相较于 <code>Options API</code> 来说， <code>Composition API</code> 对大型项目更好一些，逻辑的抽离，代码的复用，使得大型项目得以更好的维护。</li>
</ul>
<h3 data-id="heading-21">（3）别误解Composition API</h3>
<p>很多小伙伴在没学 <code>vue3</code> 之前，就依稀有听到 <code>Composition API</code> 的声音，这个时候就会使得很多人觉得，要想学会 <code>Vue3</code> ，就得先学会 <code>Composition API</code> 。</p>
<p>其实……不是这样的。</p>
<p><code>Composition API</code> 属于<strong>高阶技巧</strong>，<strong>并不是学基础时必须要会的内容</strong>。</p>
<p>正如上面所演示的内容， <code>Composition API</code> 的出现是为了<strong>解决复杂业务逻辑而设计</strong>，而不是为了学基础而设计的。</p>
<p>所以说，对于小白学 <code>vue3</code> 时，需要先学会 <code>vue3</code> 的基础，再来学 <code>Composition API</code> ，这样的学习路线更为合理。</p>
<h1 data-id="heading-22">四、🙃结束语</h1>
<p><code>vue3</code> 确实解决了 <code>vue2</code> 的很多问题，上文所描述的也只是冰山一角。但并没有说 <code>vue3</code> 出了就是 <code>vue3</code> 最好， <code>vue2</code> 不用了。因为 <code>vue3</code> 确实解决了一些问题，但同时也带来了一些问题，所以说，两者更多的是一个<strong>相辅相成</strong>的结果。</p>
<p>关于 <code>vue3</code> 的超入门知识就讲到这里啦！希望对大家有帮助~</p>
<blockquote>
<ul>
<li>关注公众号 <strong>星期一研究室</strong> ，第一时间关注学习干货，<strong>更多有趣的专栏待你解锁</strong>~</li>
<li>如果这篇文章对你有用，记得 <strong>一键三连</strong> 再走哦！</li>
<li>我们下期见！🥂🥂🥂</li>
</ul>
</blockquote></div>  
</div>
            