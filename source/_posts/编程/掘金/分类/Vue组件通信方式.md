
---
title: 'Vue组件通信方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b02c95becc784782bec693dfd65c8528~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Apr 2021 22:44:56 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b02c95becc784782bec693dfd65c8528~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这篇文章希望从整体上认识Vue的几种通信方式，希望做到快速全面掌握。</p>
<h3 data-id="heading-0">一、父子组件-props/$emit</h3>
<p>这种通信方式很常用，也很基础，大家都很熟悉。不展示代码，仅总结用法：</p>
<p><strong>父组件->子组件：</strong> 父组件 v-bind:绑定变量传给子组件。子组件通过props接收数据。</p>
<p><strong>子组件->父组件：</strong> 子组件通过emit提交，向父组件传值，父组件通过v-on绑定事件接收数据。</p>
<pre><code class="copyable">   this.$emit("titleChanged","子向父组件传值");//自定义事件  传递值“子向父组件传值”
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件通过props向下传递数据给子组件。(Vue的单向数据流)</p>
<p>注：组件中的数据共有三种形式：data、props、computed</p>
<h3 data-id="heading-1">二、父子组件-通过获取组件实例的方式— parent / $children 和 ref（ref更常用）</h3>
<p>(标题写法：parent 前面也有$。编辑器的问题。下面也都有。)</p>
<p><strong>$root</strong> ：当前组件树的根 Vue 实例。如果当前实例没有父实例，此实例将会是其自己。</p>
<p><strong>$parent</strong>：父实例，如果当前实例有的话。</p>
<p><strong>$children</strong>：</p>
<p>当前实例的直接子组件。需要注意 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>c</mi><mi>h</mi><mi>i</mi><mi>l</mi><mi>d</mi><mi>r</mi><mi>e</mi><mi>n</mi><mtext>并不保证顺序，也不是响应式的。如果你发现自己正在尝试使用</mtext></mrow><annotation encoding="application/x-tex">children 并不保证顺序，也不是响应式的。如果你发现自己正在尝试使用 </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">c</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">d</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord cjk_fallback">并</span><span class="mord cjk_fallback">不</span><span class="mord cjk_fallback">保</span><span class="mord cjk_fallback">证</span><span class="mord cjk_fallback">顺</span><span class="mord cjk_fallback">序</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">也</span><span class="mord cjk_fallback">不</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">响</span><span class="mord cjk_fallback">应</span><span class="mord cjk_fallback">式</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">。</span><span class="mord cjk_fallback">如</span><span class="mord cjk_fallback">果</span><span class="mord cjk_fallback">你</span><span class="mord cjk_fallback">发</span><span class="mord cjk_fallback">现</span><span class="mord cjk_fallback">自</span><span class="mord cjk_fallback">己</span><span class="mord cjk_fallback">正</span><span class="mord cjk_fallback">在</span><span class="mord cjk_fallback">尝</span><span class="mord cjk_fallback">试</span><span class="mord cjk_fallback">使</span><span class="mord cjk_fallback">用</span></span></span></span></span>children 来进行数据绑定，考虑使用一个数组配合 v-for 来生成子组件，并且使用 Array 作为真正的来源。</p>
<p>子实例可以用 this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>p</mi><mi>a</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mtext>访问父实例，子实例被推入父实例的</mtext></mrow><annotation encoding="application/x-tex">parent 访问父实例，子实例被推入父实例的 </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">p</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord cjk_fallback">访</span><span class="mord cjk_fallback">问</span><span class="mord cjk_fallback">父</span><span class="mord cjk_fallback">实</span><span class="mord cjk_fallback">例</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">子</span><span class="mord cjk_fallback">实</span><span class="mord cjk_fallback">例</span><span class="mord cjk_fallback">被</span><span class="mord cjk_fallback">推</span><span class="mord cjk_fallback">入</span><span class="mord cjk_fallback">父</span><span class="mord cjk_fallback">实</span><span class="mord cjk_fallback">例</span><span class="mord cjk_fallback">的</span></span></span></span></span>children 数组中。</p>
<p>需要注意的是：这两种都是直接得到组件实例，使用后可以直接调用组件的方法或访问数据。</p>
<pre><code class="copyable">this.$parent.message     //在子组件中访问父组件中的数据
this.$children[0].num    //因为父组件可能有很多子组件
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong></p>
<pre><code class="copyable">节制地使用 $parent 和 $children - 它们的主要目的是作为访问组件的应急方法。更推荐用 props 和 events 实现父子组件通信
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>ref：</strong>
如果在普通的 DOM 元素上使用，引用指向的就是 DOM 元素；如果用在子组件上，引用就指向组件实例。</p>
<p><strong>注意</strong>：ref 也是很重要的一种方式，且实际工作中很常用。
除了可以使用它获取数据，还可以通过ref调用子组件中的方法，使其执行。</p>
<h3 data-id="heading-2">三、EventBus中央事件总线-emit/ on</h3>
<p>这种方法通过一个空的Vue实例作为中央事件总线（事件中心），用它来触发事件和监听事件,巧妙而轻量地实现了任何组件间的通信，包括父子、兄弟、跨级。当我们的项目比较大时，可以选择更好的状态管理解决方案vuex。</p>
<pre><code class="copyable">var bus = new Vue()
// 组件A
bus.$emit('id-selected', 1)
// 组件B
bus.$on('id-selected', function (id) &#123;
 console.log(id)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>$on 监听了自定义事件，因为有时不确定何时会触发事件，一般会在 mounted 或 created 钩子中来监听。</p>
<h3 data-id="heading-3">四、Vuex</h3>
<p>详见本人文章： Vuex的使用和原理</p>
<h3 data-id="heading-4">五、localstorage /sessionstorage使用</h3>
<p>这种通信比较简单,缺点是数据和状态比较混乱,不太容易维护。</p>
<p>localStorage / sessionStorage可以结合vuex, 实现数据的持久保存,同时使用vuex解决数据和状态混乱问题.</p>
<h3 data-id="heading-5">六、attrs/listeners （前面都有$符）</h3>
<p>多级组件嵌套需要传递数据时，通常使用的方法是通过vuex。但如果仅仅是传递数据，而不做中间处理，也可使用Vue2.4 版本提供的另一种方法----<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi><mi>t</mi><mi>t</mi><mi>r</mi><mi>s</mi><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">attrs/</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord">/</span></span></span></span></span>listeners。</p>
<p>vm.$attrs</p>
<p>包含了父作用域中不作为 prop 被识别 (且获取) 的 attribute 绑定 (class 和 style 除外)。当一个组件没有声明任何 prop 时，这里会包含所有父作用域的绑定 (class 和 style 除外)，并且可以通过 v-bind="$attrs" 传入内部组件——在创建高级别的组件时非常有用。</p>
<p>$listeners：</p>
<p>包含了父作用域中的 (不含 .native 修饰器的) v-on 事件监听器。它可以通过 v-on="$listeners" 传入内部组件。</p>
<pre><code class="copyable">// 父组件 index.vue
<list class="list-box" title="标题" desc="描述" :list="list"></list>

// 子组件 list.vue
props: &#123;
    list: [],
&#125;,
mounted() &#123;
    console.log(this.$attrs)  // &#123;title: "标题", desc: "描述"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 子组件 list.vue
<detail v-bind="$attrs"></detial>

// 孙子组件 detail.vue
// 不定义props，直接打印 $attrs
mounted() &#123;
    console.log(this.$attrs)  // &#123;title: "标题", desc: "描述"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样的，通过 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>l</mi><mi>i</mi><mi>s</mi><mi>t</mi><mi>e</mi><mi>n</mi><mi>e</mi><mi>r</mi><mi>s</mi><mtext>用类似的操作方式可以进行跨级的事件传递，实现子到父的通信。</mtext></mrow><annotation encoding="application/x-tex">listeners 用类似的操作方式可以进行跨级的事件传递，实现子到父的通信。</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">用</span><span class="mord cjk_fallback">类</span><span class="mord cjk_fallback">似</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">操</span><span class="mord cjk_fallback">作</span><span class="mord cjk_fallback">方</span><span class="mord cjk_fallback">式</span><span class="mord cjk_fallback">可</span><span class="mord cjk_fallback">以</span><span class="mord cjk_fallback">进</span><span class="mord cjk_fallback">行</span><span class="mord cjk_fallback">跨</span><span class="mord cjk_fallback">级</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">事</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">传</span><span class="mord cjk_fallback">递</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">实</span><span class="mord cjk_fallback">现</span><span class="mord cjk_fallback">子</span><span class="mord cjk_fallback">到</span><span class="mord cjk_fallback">父</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">通</span><span class="mord cjk_fallback">信</span><span class="mord cjk_fallback">。</span></span></span></span></span>listeners 包含了父作用域中不含 .native 修饰的 v-on 事件监听器，通过 v-on="$listeners" 传递到子组件内部。</p>
<pre><code class="copyable">// 父组件 index.vue
<list @change="change" @update.native="update"></list>

// 子组件 list.vue
<detail v-on="$listeners"></detail>
// 孙子组件 detail.vue
mounted() &#123;
    this.$listeners.change()
    this.$listeners.update() // TypeError: this.$listeners.update is not a function
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">七、provide / inject API （一般开发不用）</h3>
<p>在根组件中，传入变量，然后在后代组件中使用即可。</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b02c95becc784782bec693dfd65c8528~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">// 父级组件提供 'foo'
var Provider = &#123;
  provide: &#123;
    foo: 'bar'
  &#125;,
  // ...
&#125;
// 子组件注入 'foo'
var Child = &#123;
  inject: ['foo'],
  created () &#123;
    console.log(this.foo) // => "bar"
  &#125;
  // ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用 ES2015 Symbols、函数 provide 和对象 inject：</p>
<pre><code class="copyable">const s = Symbol()

const Provider = &#123;
  provide () &#123;
    return &#123;
      [s]: 'foo'
    &#125;
  &#125;
&#125;

const Child = &#123;
  inject: &#123; s &#125;,
  // ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>慎用 provide/inject</p>
<blockquote>
<p>provide 和 inject 主要在开发高阶插件/组件库时使用。并不推荐用于普通应用程序代码中。</p>
</blockquote>
<p>Vuex 和 provide/inject 最大的区别在于，Vuex 中的全局状态的每次修改是可以追踪回溯的，而 provide/inject 中变量的修改是无法控制的，换句话说，你不知道是哪个组件修改了这个全局状态。</p>
<p><a href="https://www.cnblogs.com/karthuslorin/p/11802622.html" target="_blank" rel="nofollow noopener noreferrer">了解参考</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            