
---
title: 'vue的通信方式总结及案例分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f9525d0d6f2442ba0730a7afbde0f63~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 23:58:41 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f9525d0d6f2442ba0730a7afbde0f63~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文主要基于的vue 2.x版本</p>
<p>vue中的通信方式比较多，以我个人使用到的做了一些总结，大致有一下几种：</p>
<ul>
<li>props</li>
<li>events</li>
</ul>

<ul>
<li>slot</li>
<li>ref</li>
</ul>

<ul>
<li>eventBus</li>
<li>vuex</li>
</ul>

<ul>
<li>provide / inject</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f9525d0d6f2442ba0730a7afbde0f63~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
下面就介绍每种通信方式的使用方式以及各自的区别。</p>
<h3 data-id="heading-0">props</h3>
<p><code>props</code>是最常用，最基本的一种通信方式，通过子组件声明参数，父组件直接传入参数。这种方式大家应该都早就烂熟于心了，就没什么好介绍的了，不过需要注意的是，如果子组件没有在<code>props</code>中声明的参数，父组件传入，会被识别为普通的attr属性，子组件将无法通过<code>this</code>直接获取。</p>
<p>一下就是几个要点：</p>
<ul>
<li>需要提前在组件props中声明</li>
<li><code>String</code>类型的传参，如果不是变量可以直接传入，无需使用：标注，比如<code><button size='mini'>按钮</button></code></li>
</ul>

<ul>
<li>Boolean类型的传参，如果值是true，且无需变量控制，则可以直接只写参数名，比如<code><button disabled>按钮</button></code></li>
</ul>
<h3 data-id="heading-1">events</h3>
<p>events也是最常用的一种通信方式，主要用于子组件返回参数给父组件。最简单的用法就是有子组件触发事件，父组件监听事件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//子组件</span>
<span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'submit'</span>,data)

<span class="hljs-comment">//父组件</span>
<child @submit=<span class="hljs-string">'submit'</span>/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@</code>其实就是<code>v-on</code>的缩写，v-on除了可以监听子组件的事件，也可以监听dom的原生事件，并且具有比较多的修饰符来实现更多的方式，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23v-on" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/api/#v-on" ref="nofollow noopener noreferrer">官方示例</a>。</p>
<p>这边有一个知识点：this.$emit触发的事件，除了父组件可以监听之外，子组件自身也可以监听到该事件，这个vue的文档中有说明，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23vm-on" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/api/#vm-on" ref="nofollow noopener noreferrer">官方示例</a>，具体有什么用途我们后续说到。</p>
<p>props和events是最常用的两种组件通信方式，除了一般的使用方式，vue还提供了<code>inheritAttrs:false</code>属性，用于组件的封装使用，可以让父组件传入的所有属性都通过<code>this.$attrs</code>访问到，这样我们在包装一个组件时，可以通过v-bing=<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi><mi>t</mi><mi>t</mi><mi>r</mi><mi>s</mi><mtext>一次把所有的父组件传入属性绑定到子组件中，</mtext><mi>v</mi><mo>−</mo><mi>o</mi><mi>n</mi><mo>=</mo></mrow><annotation encoding="application/x-tex">attrs一次把所有的父组件传入属性绑定到子组件中，v-on=</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">次</span><span class="mord cjk_fallback">把</span><span class="mord cjk_fallback">所</span><span class="mord cjk_fallback">有</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">父</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">传</span><span class="mord cjk_fallback">入</span><span class="mord cjk_fallback">属</span><span class="mord cjk_fallback">性</span><span class="mord cjk_fallback">绑</span><span class="mord cjk_fallback">定</span><span class="mord cjk_fallback">到</span><span class="mord cjk_fallback">子</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">中</span><span class="mord cjk_fallback">，</span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span></span></span></span></span>listeners绑定所有父组件监听事件。</p>
<h3 data-id="heading-2">slot</h3>
<p>slot插槽也是一种非常常用的组件传参方式，通过slot可以更灵活的控制通用组件的自定义渲染内容，slot除了可以传入vnode渲染内容，也可以通过slot传递参数。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 接收 prop 的具名插槽 --></span>
<span class="hljs-tag"><<span class="hljs-name">infinite-scroll</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:item</span>=<span class="hljs-string">"slotProps"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
      &#123;&#123; slotProps.item.text &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">infinite-scroll</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种用法在element ui中很多组件都有使用到，比如<code>autocomplete</code>组件的自定义渲染等。</p>
<h3 data-id="heading-3">ref</h3>
<p>ref实例的方式实现的数据交互是比较强大的，通过调用组件的实例，可以获取到组件所有的数据，实例方法等。通过在子组件上声明ref属性，就可以通过$refs调取到对应的组件实例。</p>
<p>通过调取实例，我们可以操作实例中的所有参数，比如</p>
<pre><code class="hljs language-html copyable" lang="html">//代码仅作实例，实际并非如此
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">'input'</span> /></span>

this.$refs.input.value = 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类似以上例子，我们可以在其他组件中直接修改某个组件中的数据，同样也可以读取其数据，但是一般不推荐这种用法。组件的数据应该由组件自身去维护，如果有类似需要修改其数据的情况，我们应该在该组件中声明一个修改数据的方法，而其他组件去调取该方法来修改数据，这样做的目的是让组件更加的可控，不会出现一些莫名其妙的错误，而无法定位。</p>
<p>\</p>
<p>除了通过ref的声明方式获取组件的实例，我们也可以通过<code>$parent</code>获取父组件的实例，<code>$root</code>获取当前组件树的根实例，<code>$children</code>获取当前组件的子组件实例数组等。</p>
<p>需要注意的是，所有的组件实例都需要在该组件<code>mounted</code>生命周期后才可以被调取到，在该声明周期之前，实例都未挂载，无法正常调取到，这个在vue的文档中有提到：</p>
<blockquote>
<p>mounted
实例被挂载后调用，这时 el 被新创建的 vm.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi><mi>l</mi><mtext>替换了。如果根实例挂载到了一个文档内的元素上，当</mtext><mi>m</mi><mi>o</mi><mi>u</mi><mi>n</mi><mi>t</mi><mi>e</mi><mi>d</mi><mtext>被调用时</mtext><mi>v</mi><mi>m</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">el 替换了。如果根实例挂载到了一个文档内的元素上，当 mounted 被调用时 vm.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord cjk_fallback">替</span><span class="mord cjk_fallback">换</span><span class="mord cjk_fallback">了</span><span class="mord cjk_fallback">。</span><span class="mord cjk_fallback">如</span><span class="mord cjk_fallback">果</span><span class="mord cjk_fallback">根</span><span class="mord cjk_fallback">实</span><span class="mord cjk_fallback">例</span><span class="mord cjk_fallback">挂</span><span class="mord cjk_fallback">载</span><span class="mord cjk_fallback">到</span><span class="mord cjk_fallback">了</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">文</span><span class="mord cjk_fallback">档</span><span class="mord cjk_fallback">内</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">元</span><span class="mord cjk_fallback">素</span><span class="mord cjk_fallback">上</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">当</span><span class="mord mathnormal">m</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal">d</span><span class="mord cjk_fallback">被</span><span class="mord cjk_fallback">调</span><span class="mord cjk_fallback">用</span><span class="mord cjk_fallback">时</span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mord mathnormal">m</span><span class="mord">.</span></span></span></span></span>el 也在文档内。</p>
</blockquote>
<h3 data-id="heading-4">provide / inject</h3>
<p>该用法是在vue 2.2之后新增的，主要作用就是用于父组件共享数据给子组件使用，听上去用法是不是和props一样吗？可以说效果确实如此，但是使用的场景不同。</p>
<p>props传参必须是子组件直接使用在父组件中才可以方便传参，如果是子组件是父组件中的子组件的子组件，那么父组件怎么怎么传参给该子组件呢？</p>
<p>比较笨一点的方法，就是父组件先传参给第一层子组件，子组件在传参给其下层子组件。可以说效果是可以达到，但是非常的麻烦，而且如果层次多了，工作量大增的同时，每层组件都得声明一边props，一次传入，非常的不可控，也不优雅。</p>
<p>provide/inject就是为了解决这样的问题。父组件声明需要传递的参数，子组件声明需要接受的参数，中间不管嵌套几层组件，子组件都可以直接在其this中访问到父组件传递的参数。</p>
<p>官方示例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 父级组件提供 'foo'</span>
<span class="hljs-keyword">var</span> Provider = &#123;
  <span class="hljs-attr">provide</span>: &#123;
    <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span>
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-comment">// 子组件注入 'foo'</span>
<span class="hljs-keyword">var</span> Child = &#123;
  <span class="hljs-attr">inject</span>: [<span class="hljs-string">'foo'</span>],
  created () &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.foo) <span class="hljs-comment">// => "bar"</span>
  &#125;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个我们在使用element ui中的form组件应该有感受，我们只需要在form组件上传入label-width，rules等参数，而所有的子组件el-form-item都可以起作用。后面我会以el-form为例，分析一下各种通信方式在其中的应用。</p>
<h3 data-id="heading-5">eventBus</h3>
<p>从名字就可以看出是一种事件通信方式，其实原理很简单，就是利用的上面提到的组件实例可以监听到自身emit触发的事件，来实现的一种全局通信方式，同时也利用了ref的实例通信方式。使用方式如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//main.js</span>

Vue.prototype.$EventBus=<span class="hljs-keyword">new</span> Vue() <span class="hljs-comment">//在vue的实例上挂载一个vue的实例</span>

<span class="hljs-comment">//组件A 利用共享的实例注册其监听事件</span>
<span class="hljs-built_in">this</span>.$EventBus.$on(<span class="hljs-string">'input'</span>,<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;<span class="hljs-built_in">console</span>.log(value)&#125;)

<span class="hljs-comment">//组件B 利用共享的实例触发事件</span>
<span class="hljs-built_in">this</span>.$EventBus.$emit(<span class="hljs-string">'input'</span>,<span class="hljs-string">'test'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样本质其实是new的vue实例触发事件，监听自己的事件，然后通过共享该实例，来让不同的组件通过该实例来做到数据通信。</p>
<p>需要注意的是，由于该实例是挂载在整个vue实例上的，所以即便在组件销毁之后，事件监听任然是存在的，为了避免重复触发事件，在不需要时或者组件销毁时，通过this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>E</mi><mi>v</mi><mi>e</mi><mi>n</mi><mi>t</mi><mi>B</mi><mi>u</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">EventBus.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.05764em;">E</span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.05017em;">B</span><span class="mord mathnormal">u</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>off去注销监听事件。</p>
<h3 data-id="heading-6">vuex</h3>
<p>vuex就不多说了，vue中重量级的状态管理管理库了，通过vue的数据的响应式来驱动，具体的用法就直接看文档吧</p>
<h3 data-id="heading-7">示例分析</h3>
<p>以上差不多把我比较熟知的几种vue通信方式都简要的梳理了一边，但是观看用法可能比较枯燥，不够形象，下面就以element中的form组件为例，来看看该组件的封装中使用了哪些通信方式，element作为vue中最流行的开源框架，很多的设计和实现是非常值得学习的。</p>
<p>直接看源码吧：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//el-form</span>
<template>
 ...
</template>
<script>
  <span class="hljs-keyword">import</span> objectAssign <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui/src/utils/merge'</span>;

  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'ElForm'</span>,

    <span class="hljs-attr">componentName</span>: <span class="hljs-string">'ElForm'</span>,

    <span class="hljs-function"><span class="hljs-title">provide</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">elForm</span>: <span class="hljs-built_in">this</span>
      &#125;;
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这边一上来就可以看到el-form这个父组件使用了<code>provide</code>声明了<code>elForm</code>属性，并传入了自身的实例<code>this</code>，那么很显然，子组件肯定会接受该参数，我们看到子组件代码。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'ElFormItem'</span>,

    <span class="hljs-attr">componentName</span>: <span class="hljs-string">'ElFormItem'</span>,

    <span class="hljs-attr">mixins</span>: [emitter],

    <span class="hljs-function"><span class="hljs-title">provide</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">elFormItem</span>: <span class="hljs-built_in">this</span>
      &#125;;
    &#125;,

    <span class="hljs-attr">inject</span>: [<span class="hljs-string">'elForm'</span>],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>果然，ElFormItem中利用inject获取了elForm参数，同时声明了一个elFormItem的共享参数，这个自然也是给其子组件使用的，我们暂时不看。我们先看看通过elForm，ElFormItem组件可以实现什么。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//el-form-item</span>
<span class="hljs-function"><span class="hljs-title">contentStyle</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> ret = &#123;&#125;;
        <span class="hljs-keyword">const</span> label = <span class="hljs-built_in">this</span>.label;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.form.labelPosition === <span class="hljs-string">'top'</span> || <span class="hljs-built_in">this</span>.form.inline) <span class="hljs-keyword">return</span> ret;
        <span class="hljs-keyword">if</span> (!label && !<span class="hljs-built_in">this</span>.labelWidth && <span class="hljs-built_in">this</span>.isNested) <span class="hljs-keyword">return</span> ret;
        <span class="hljs-keyword">const</span> labelWidth = <span class="hljs-built_in">this</span>.labelWidth || <span class="hljs-built_in">this</span>.form.labelWidth;
        <span class="hljs-keyword">if</span> (labelWidth === <span class="hljs-string">'auto'</span>) &#123;
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.labelWidth === <span class="hljs-string">'auto'</span>) &#123;
            ret.marginLeft = <span class="hljs-built_in">this</span>.computedLabelWidth;
          &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.form.labelWidth === <span class="hljs-string">'auto'</span>) &#123;
            ret.marginLeft = <span class="hljs-built_in">this</span>.elForm.autoLabelWidth;
          &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
          ret.marginLeft = labelWidth;
        &#125;
        <span class="hljs-keyword">return</span> ret;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">form</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> parent = <span class="hljs-built_in">this</span>.$parent;
        <span class="hljs-keyword">let</span> parentName = parent.$options.componentName;
        <span class="hljs-keyword">while</span> (parentName !== <span class="hljs-string">'ElForm'</span>) &#123;
          <span class="hljs-keyword">if</span> (parentName === <span class="hljs-string">'ElFormItem'</span>) &#123;
            <span class="hljs-built_in">this</span>.isNested = <span class="hljs-literal">true</span>;
          &#125;
          parent = parent.$parent;
          parentName = parent.$options.componentName;
        &#125;
        <span class="hljs-keyword">return</span> parent;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">_formSize</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.elForm.size;
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的代码，我们可以看到子组件直接可以通过<code>this.elForm</code>获取到父组件上传入的一些公共的配置，但是同时我们注意到还有一个<code>form</code>的<code>computed</code>参数，实现的方式是循环查找到<code>ElForm</code>这个父级组件实例。</p>
<p>这么看来<code>this.elForm</code>岂不是和<code>this.form</code>是一个效果，那这么做的意义是什么呢？</p>
<p>其实这是一个历史原因，因为上面提到<code>provide</code>的特性是在vue 2.2之后才新增的，而element ui早在这之前就有这些组件了，最初的实现方式则是通过computed中的循环查找的方式来获取的父级实例实现的参数共享，而在element ui 2.0之后的版本则新增了<code>provide</code>的方式来共享参数，之后的功能则是基于该特性来实现的，老原来的代码并未使用新特性重构（以上是个人参考github仓库推测而来）</p>
<p>接着往下看，我们知道el-form主要实现的一个功能就是数据校验，我们在输入组件中输入值可以触发el-form的数据校验和错误提示，使用方式就是在el-form上传入mode，rules以及在el-form-item上传入prop,然后就可以根据校验规则触发数据校验，这个是怎么实现的呢，细看代码。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//首先我们找一个简单的组件入手，直接从el-input来看，其他原理都是一样的。</span>
<span class="hljs-comment">//el-input</span>
    <span class="hljs-attr">inject</span>: &#123;
      <span class="hljs-attr">elForm</span>: &#123;
        <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
      &#125;,
      <span class="hljs-attr">elFormItem</span>: &#123;
        <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
      &#125;
    &#125;


<span class="hljs-comment">//computed</span>
 <span class="hljs-function"><span class="hljs-title">_elFormItemSize</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (<span class="hljs-built_in">this</span>.elFormItem || &#123;&#125;).elFormItemSize;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">validateState</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.elFormItem ? <span class="hljs-built_in">this</span>.elFormItem.validateState : <span class="hljs-string">''</span>;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">needStatusIcon</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.elForm ? <span class="hljs-built_in">this</span>.elForm.statusIcon : <span class="hljs-literal">false</span>;
      &#125;

上面的参数我们可以看到有大量的共享参数的获取，而这些在<span class="hljs-number">1.4</span><span class="hljs-number">.13</span>版本的elementui中式没有的，基本也可以验证上面的推测

<span class="hljs-comment">//methods</span>

     <span class="hljs-function"><span class="hljs-title">handleBlur</span>(<span class="hljs-params">event</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.focused = <span class="hljs-literal">false</span>;
        <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'blur'</span>, event);
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.validateEvent) &#123;
          <span class="hljs-built_in">this</span>.dispatch(<span class="hljs-string">'ElFormItem'</span>, <span class="hljs-string">'el.form.blur'</span>, [<span class="hljs-built_in">this</span>.value]);
        &#125;
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在el-input的失焦事件中，我们可以看到一个<code> this.dispatch('ElFormItem', 'el.form.blur', [this.value]);</code>很明显，这个是和el-from-item组件相关的事件。</p>
<p>不着急，我们先看一下这个dispatch是一个什么方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//element-ui/src/mixins/emitter.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">broadcast</span>(<span class="hljs-params">componentName, eventName, params</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.$children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
    <span class="hljs-keyword">var</span> name = child.$options.componentName;

    <span class="hljs-keyword">if</span> (name === componentName) &#123;
      child.$emit.apply(child, [eventName].concat(params));
    &#125; <span class="hljs-keyword">else</span> &#123;
      broadcast.apply(child, [componentName, eventName].concat([params]));
    &#125;
  &#125;);
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">dispatch</span>(<span class="hljs-params">componentName, eventName, params</span>)</span> &#123;
      <span class="hljs-keyword">var</span> parent = <span class="hljs-built_in">this</span>.$parent || <span class="hljs-built_in">this</span>.$root;
      <span class="hljs-keyword">var</span> name = parent.$options.componentName;

      <span class="hljs-keyword">while</span> (parent && (!name || name !== componentName)) &#123;
        parent = parent.$parent;

        <span class="hljs-keyword">if</span> (parent) &#123;
          name = parent.$options.componentName;
        &#125;
      &#125;
      <span class="hljs-keyword">if</span> (parent) &#123;
        parent.$emit.apply(parent, [eventName].concat(params));
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">broadcast</span>(<span class="hljs-params">componentName, eventName, params</span>)</span> &#123;
      broadcast.call(<span class="hljs-built_in">this</span>, componentName, eventName, params);
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这边有两个方法，一个dispath一个broadcast，从名字就可以看出来，一个是广播事件，一个是派发事件，从dispatch实现上可以看出和上面提到的compued中的form是非常像的，通过向上循环查找对应的组件实例，来触发事件。而boradcast则是怎么向下查找来触发事件，所以他们一个是子组件使用的，一个是父组件使用的，。</p>
<p>所以我们在上面就看到input组件通过该方法向el-form-item来触发输入事件，而el-form-item中我们可以看到利用broadcast事件来重置输入组件的参数等。</p>
<p>说到这边有人就要问了，前面不是说可以通过eventBus的方式实现全局的事件派发和监听吗，为什么要搞这一套，这么麻烦。那是因为element ui作为一个组件库，他是独立使用的，而eventBus则依赖于在main.js中挂载实例才可以使用，作为一个组件库肯定是做到这样的，他必须要可以独立使用，而不能依赖外部不确定性的参数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-function"><span class="hljs-title">resetField</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.validateState = <span class="hljs-string">''</span>;
        <span class="hljs-built_in">this</span>.validateMessage = <span class="hljs-string">''</span>;

        <span class="hljs-keyword">let</span> model = <span class="hljs-built_in">this</span>.form.model;
    ...
        <span class="hljs-built_in">this</span>.broadcast(<span class="hljs-string">'ElTimeSelect'</span>, <span class="hljs-string">'fieldReset'</span>, <span class="hljs-built_in">this</span>.initialValue);
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>回到el-form-item组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//el-form-item     </span>
<span class="hljs-function"><span class="hljs-title">addValidateEvents</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> rules = <span class="hljs-built_in">this</span>.getRules();

        <span class="hljs-keyword">if</span> (rules.length || <span class="hljs-built_in">this</span>.required !== <span class="hljs-literal">undefined</span>) &#123;
          <span class="hljs-built_in">this</span>.$on(<span class="hljs-string">'el.form.blur'</span>, <span class="hljs-built_in">this</span>.onFieldBlur);
          <span class="hljs-built_in">this</span>.$on(<span class="hljs-string">'el.form.change'</span>, <span class="hljs-built_in">this</span>.onFieldChange);
        &#125;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">removeValidateEvents</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.$off();
      &#125;
...

   <span class="hljs-function"><span class="hljs-title">onFieldBlur</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.validate(<span class="hljs-string">'blur'</span>);
      &#125;,
      <span class="hljs-function"><span class="hljs-title">onFieldChange</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.validateDisabled) &#123;
          <span class="hljs-built_in">this</span>.validateDisabled = <span class="hljs-literal">false</span>;
          <span class="hljs-keyword">return</span>;
        &#125;

        <span class="hljs-built_in">this</span>.validate(<span class="hljs-string">'change'</span>);
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到确实有监听相关的事件，那么很明显了，input在输入之后触发失焦事件，el-form-item监听输入组件的失焦和change事件，在触发参数校验，而rules则通过父级实例获取到，</p>
<p>同时我们看到onFieldBlur等事件虽然有监听输入事件，但是并没有接收事件触发之后的传值，继续看校验方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">computed:&#123;  
<span class="hljs-function"><span class="hljs-title">fieldValue</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> model = <span class="hljs-built_in">this</span>.form.model;
        <span class="hljs-keyword">if</span> (!model || !<span class="hljs-built_in">this</span>.prop) &#123; <span class="hljs-keyword">return</span>; &#125;

        <span class="hljs-keyword">let</span> path = <span class="hljs-built_in">this</span>.prop;
        <span class="hljs-keyword">if</span> (path.indexOf(<span class="hljs-string">':'</span>) !== -<span class="hljs-number">1</span>) &#123;
          path = path.replace(<span class="hljs-regexp">/:/</span>, <span class="hljs-string">'.'</span>);
        &#125;

        <span class="hljs-keyword">return</span> getPropByPath(model, path, <span class="hljs-literal">true</span>).v;
      &#125;,
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">validate</span>(<span class="hljs-params">trigger, callback = noop</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.validateDisabled = <span class="hljs-literal">false</span>;
        <span class="hljs-keyword">const</span> rules = <span class="hljs-built_in">this</span>.getFilteredRule(trigger);
        <span class="hljs-keyword">if</span> ((!rules || rules.length === <span class="hljs-number">0</span>) && <span class="hljs-built_in">this</span>.required === <span class="hljs-literal">undefined</span>) &#123;
          callback();
          <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        &#125;

        <span class="hljs-built_in">this</span>.validateState = <span class="hljs-string">'validating'</span>;

        <span class="hljs-keyword">const</span> descriptor = &#123;&#125;;
        <span class="hljs-keyword">if</span> (rules && rules.length > <span class="hljs-number">0</span>) &#123;
          rules.forEach(<span class="hljs-function"><span class="hljs-params">rule</span> =></span> &#123;
            <span class="hljs-keyword">delete</span> rule.trigger;
          &#125;);
        &#125;
        descriptor[<span class="hljs-built_in">this</span>.prop] = rules;

        <span class="hljs-keyword">const</span> validator = <span class="hljs-keyword">new</span> AsyncValidator(descriptor);
        <span class="hljs-keyword">const</span> model = &#123;&#125;;

        model[<span class="hljs-built_in">this</span>.prop] = <span class="hljs-built_in">this</span>.fieldValue;

        validator.validate(model, &#123; <span class="hljs-attr">firstFields</span>: <span class="hljs-literal">true</span> &#125;, <span class="hljs-function">(<span class="hljs-params">errors, invalidFields</span>) =></span> &#123;
          <span class="hljs-built_in">this</span>.validateState = !errors ? <span class="hljs-string">'success'</span> : <span class="hljs-string">'error'</span>;
          <span class="hljs-built_in">this</span>.validateMessage = errors ? errors[<span class="hljs-number">0</span>].message : <span class="hljs-string">''</span>;

          callback(<span class="hljs-built_in">this</span>.validateMessage, invalidFields);
          <span class="hljs-built_in">this</span>.elForm && <span class="hljs-built_in">this</span>.elForm.$emit(<span class="hljs-string">'validate'</span>, <span class="hljs-built_in">this</span>.prop, !errors, <span class="hljs-built_in">this</span>.validateMessage || <span class="hljs-literal">null</span>);
        &#125;);
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过fieldValue的compued就可以看到在el-form上传入的mode的作用的，输入组件的值，是通过父级传入的formData来获取的。通过rules传入的参数校验之后，控制el-form-item的错误消息是否显示，通知利用共享的elForm实例触发校验事件，因此我们可以在elform组件上才可以监听任意输入组件触发的校验事件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca0f22191c1d4ab6a7c0d85852a2f5b3~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而所有的输入组件自然是通过slot的方式传入el-fom-item的咯</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"el-form-item__content"</span> :style=<span class="hljs-string">"contentStyle"</span>>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span></span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"el-zoom-in-top"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">slot</span>
          <span class="hljs-attr">v-if</span>=<span class="hljs-string">"validateState === 'error' && showMessage && form.showMessage"</span>
          <span class="hljs-attr">name</span>=<span class="hljs-string">"error"</span>
          <span class="hljs-attr">:error</span>=<span class="hljs-string">"validateMessage"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>
            <span class="hljs-attr">class</span>=<span class="hljs-string">"el-form-item__error"</span>
            <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;
              'el-form-item__error--inline': typeof inlineMessage === 'boolean'
                ? inlineMessage
                : (elForm && elForm.inlineMessage || false)
            &#125;"</span>
          ></span>
            &#123;&#123;validateMessage&#125;&#125;
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">transition</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时也可以看到有一个name="error"的slot，传入了一个error的参数，这个就是element ui文中的自定义检验显示方式啦，通过slot传入了错误信息</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0ed3e961f56411d8325941da12451d8~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到el-form除了没有使用vuex来通信以外，上面的通信方式几乎全部使用到了，所以从优秀的开源项目中，我们是可以学习到非常多优秀的设计和实现的，对于我们的水平提高和开发工作还是很有帮助的。</p>
<p>以上是个人的一些总结和分析，或许有很多说的不正确的地方，和大家交流一下想法，也希望能帮到有需要的童鞋下😁</p></div>  
</div>
            