
---
title: 'Vue中 $attrs、$listeners 详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66c5205b4a3b4906a294b70dd17d2dd9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 18:49:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66c5205b4a3b4906a294b70dd17d2dd9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第15天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h4 data-id="heading-0">1. 前言</h4>
<p>多级组件嵌套需要传递数据时，通常使用的方法是通过 vuex。如果仅仅是传递数据，而不做中间处理，使用 vuex 处理，未免有点杀鸡用牛刀。</p>
<p>Vue 2.4 版本提供了另一种方法，使用 v-bind=”$attrs”, 将父组件中不被认为 props 特性绑定的属性传入子组件中，通常配合 interitAttrs 选项一起使用。之所以要提到这两个属性，是因为两者的出现使得组件之间跨组件的通信在不依赖 vuex 和 事件总线 的情况下变得简洁，业务清晰。</p>
<p><strong>首先分析以下应用场景</strong></p>
<p>![3O5K9EU6]S&#123;)PHV2ZV1ES3T.png](<a href="https://link.juejin.cn/?target=https%3A%2F%2Fp6-juejin.byteimg.com%2Ftos-cn-i-k3u1fbpfcp%2F04ea107210e040cdb4e3431a83a0e0ff~tplv-k3u1fbpfcp-watermark.image" target="_blank" rel="nofollow noopener noreferrer" title="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04ea107210e040cdb4e3431a83a0e0ff~tplv-k3u1fbpfcp-watermark.image" ref="nofollow noopener noreferrer">p6-juejin.byteimg.com/tos-cn-i-k3…</a>)</p>
<p><strong>A 组件与 B 组件之间的通信： （父子组件）</strong></p>
<p>如上图所示，A、B、C三个组件依次嵌套，按照 Vue 的开发习惯，父子组件通信可以通过以下方式实现：</p>
<ul>
<li>A to B 通过 props 的方式向子组件传递，B to A 通过在 B 组件中 $emit, A 组件中 v-on 的方式实现；</li>
<li>通过设置全局 Vuex 共享状态，通过 computed 计算属性和 commit mutation 的方式实现数据的获取和更新，以达到父子组件通信的目的；</li>
<li>Vue Event Bus，使用 Vue 的实例，实现事件的监听和发布，实现组件之间的传递；</li>
</ul>
<p>往往数据在不需要全局的情况而仅仅是父子组件通信时，使用第一种方式即可满足。</p>
<p><strong>A 组件与 C 组件之间的通信： （跨多级的组件嵌套关系）</strong></p>
<p>如上图，A 组件与 C 组件之间属于跨多级的组件嵌套关系，以往两者之间如需实现通信，往往通过以下方式实现：</p>
<ul>
<li>借助 B 组件的中转，从上到下 props 依次传递，从下至上 $emit 事件的传递，达到跨级组件通信的效果；</li>
<li>借助 Vuex 的全局状态共享；</li>
<li>Vue Event Bus，使用 Vue 的实例实现事件的监听和发布，实现组件之间的传递</li>
</ul>
<p>第一种通过 props 和 $emit 的方式，使得组件之间的业务逻辑臃肿不堪，B组件在其中仅仅充当的是一个中转站的作用；</p>
<p>第二种 Vuex 的方式，某些情况下似乎又有点大材小用的意味（仅仅是想实现组件之间的一个数据传递，并非数据共享的概念）；</p>
<p>第三种情况的使用在实际的项目操作中发现，如不能实现很好的事件监听与发布的管理，往往容易导致数据流的混乱，在多人协作的项目中，不利于项目的维护；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">$attrs 以及 $listeners 的出现解决的就是第一种情况的问题，B 组件在其中传递 props 以及事件的过程中，不必在写多余的代码，

仅仅是将 $attrs 以及 $listeners 向上或者向下传递即可。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2. 知识点</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66c5205b4a3b4906a294b70dd17d2dd9~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>inheritAttrs：默认值 true，继承所有的父组件属性（除 props 的特定绑定）作为普通的HTML特性应用在子组件的根元素上，如果你不希望组件的根元素继承特性设置 inheritAttrs: false ,但是 class 属性会继承。
（简单的说，inheritAttrs：true 继承除 props 之外的所有属性；inheritAttrs：false 只继承 class style 属性）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b950ee83c984cf4a2beabb3012da6f6~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>$attrs--继承所有的父组件属性（除了 prop 传递的属性、class 和 style ），一般用在子组件的子元素上</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9664adbaadc4d778bb9a913b5379ffa~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>l</mi><mi>i</mi><mi>s</mi><mi>t</mi><mi>e</mi><mi>n</mi><mi>e</mi><mi>r</mi><mi>s</mi><mtext>属性，它是一个对象，里面包含了作用在这个组件上的所有监听器，你就可以配合</mtext><mi>v</mi><mo>−</mo><mi>o</mi><mi>n</mi><mo>=</mo><mi mathvariant="normal">"</mi></mrow><annotation encoding="application/x-tex"> listeners属性，它是一个对象，里面包含了作用在这个组件上的所有监听器，你就可以配合 v-on="</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.77777em;vertical-align:-0.08333em;"></span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">属</span><span class="mord cjk_fallback">性</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">它</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">对</span><span class="mord cjk_fallback">象</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">里</span><span class="mord cjk_fallback">面</span><span class="mord cjk_fallback">包</span><span class="mord cjk_fallback">含</span><span class="mord cjk_fallback">了</span><span class="mord cjk_fallback">作</span><span class="mord cjk_fallback">用</span><span class="mord cjk_fallback">在</span><span class="mord cjk_fallback">这</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">上</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">所</span><span class="mord cjk_fallback">有</span><span class="mord cjk_fallback">监</span><span class="mord cjk_fallback">听</span><span class="mord cjk_fallback">器</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">你</span><span class="mord cjk_fallback">就</span><span class="mord cjk_fallback">可</span><span class="mord cjk_fallback">以</span><span class="mord cjk_fallback">配</span><span class="mord cjk_fallback">合</span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord">"</span></span></span></span></span>listeners" 将所有的事件监听器指向这个组件的某个特定的子元素。（相当于子组件继承父组件的事件）</p>
<h4 data-id="heading-2">3. 示例</h4>
<p><strong>A组件（App.vue）</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!-- 此处监听了两个事件，可以在B组件或者C组件中直接触发 --></span>
    <span class="hljs-tag"><<span class="hljs-name">child1</span>  <span class="hljs-attr">:pchild1</span>=<span class="hljs-string">"child1"</span> <span class="hljs-attr">:pchild2</span>=<span class="hljs-string">"child2"</span> <span class="hljs-attr">:pchild3</span>=<span class="hljs-string">"child3"</span> @<span class="hljs-attr">method1</span>=<span class="hljs-string">"onMethod1"</span> @<span class="hljs-attr">method2</span>=<span class="hljs-string">"onMethod2"</span>></span><span class="hljs-tag"></<span class="hljs-name">child1</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> Child1 <span class="hljs-keyword">from</span> <span class="hljs-string">"./Child1.vue"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">child1</span>:<span class="hljs-string">'1'</span>,
      <span class="hljs-attr">child2</span>: <span class="hljs-number">2</span>,
      <span class="hljs-attr">child3</span>:&#123;
        <span class="hljs-attr">name</span>:<span class="hljs-string">'child3'</span>
      &#125;
    &#125;;
  &#125;,
  <span class="hljs-attr">components</span>: &#123; Child1 &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">onMethod1</span>(<span class="hljs-params">msg1</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;msg1&#125;</span> running`</span>);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">onMethod2</span>(<span class="hljs-params">msg2</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;msg2&#125;</span> running`</span>);
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>B组件（Child1.vue）</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child-1"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>in child1<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>props: &#123;&#123; pchild1 &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>$attrs: &#123;&#123; $attrs &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">hr</span>/></span>
    <span class="hljs-comment"><!-- 通过 v-bind 绑定$attrs属性，C组件可以直接获取到A组件中传递下来的props（除了B组件中props声明的） --></span>
    <span class="hljs-comment"><!-- C组件中能直接触发test的原因在于 B组件调用C组件时 使用 v-on 绑定了$listeners 属性 --></span>
    <span class="hljs-tag"><<span class="hljs-name">child2</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"$attrs"</span> <span class="hljs-attr">v-on</span>=<span class="hljs-string">"$listeners"</span>></span><span class="hljs-tag"></<span class="hljs-name">child2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> Child2 <span class="hljs-keyword">from</span> <span class="hljs-string">"./Child2.vue"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">child1</span>:<span class="hljs-string">'child1'</span>  
    &#125;;
  &#125;,
  <span class="hljs-attr">components</span>: &#123; Child2 &#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">pchild1</span>:&#123;
      <span class="hljs-attr">type</span>:<span class="hljs-built_in">String</span>
    &#125;
  &#125;,  
  <span class="hljs-attr">inheritAttrs</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">"method1"</span>,<span class="hljs-built_in">this</span>.child1);
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>C 组件 (Child2.vue)</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child-2"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>in child2:<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>props: &#123;&#123; pChild2 &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>$attrs: &#123;&#123; $attrs &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>pchild3Name: &#123;&#123; $attrs.pchild3.name &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">hr</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">child2</span>:<span class="hljs-string">'child2'</span>
    &#125;;
  &#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">pChild2</span>:&#123;
      <span class="hljs-attr">type</span>:<span class="hljs-built_in">String</span>,
    &#125;
  &#125;,
  <span class="hljs-attr">inheritAttrs</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">"method2"</span>,<span class="hljs-built_in">this</span>.child2);
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45f3bc495a34436a90a999343d71bb2c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            