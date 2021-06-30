
---
title: 'Vue.js常用知识点，你都掌握了么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7873'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 01:32:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=7873'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>做了多年的前端开发，Vue.js也用了几年啦，总结了些常用的知识点纪录下来，方便自己查看。</p>
<hr>
<p><strong>常用指令</strong></p>
<p>v-once  进入页面时  只渲染一次 不在进行渲染</p>
<p>v-cloak  防止闪烁</p>
<p>v-pre  把标签内部的元素原位输出</p>
<p>v-html 解析渲染html标签</p>
<p>v-text  解析文本   /  &#123;&#123;title&#125;&#125;和v-text="title"等同</p>
<p>v-bind:class简写:class</p>
<p>v-on:click 主要用来监听dom事件，以便执行一些代码块，简写@click</p>
<p>v-on:keyup.enter 回车keyup事件，简写@keyup.enter</p>
<p>v-model 双向绑定（在input textarea select中使用）</p>
<p>v-model的修饰符
v-model.lazy 只有在input输入框发生一个blur时才触发（转变为在change事件再同步）
v-model.trim 将用户输入的前后的空格去掉
v-model.number 将用户输入的字符串转换成number</p>
<hr>
<p><strong>动态添加类名 v-bind:class</strong></p>
<p><strong>三种绑定方法</strong></p>
<p>1、对象型</p>
<p><1>对象语法</p>
<pre><code class="hljs language-js copyable" lang="js">data: &#123;
    <span class="hljs-attr">isActive</span>: <span class="hljs-literal">true</span>,  
    <span class="hljs-attr">hasError</span>: <span class="hljs-literal">false</span>
&#125;
<div :<span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"&#123;'is-active':isActive, 'text-danger':hasError&#125;"</span>></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><!--因为hasError: <span class="hljs-literal">false</span>，所以text-danger不被渲染-->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span> = <span class="hljs-string">"is-active"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><2>直接绑定数据对象</p>
<pre><code class="hljs language-js copyable" lang="js">data: &#123;
    <span class="hljs-attr">classObject</span>:&#123;
        <span class="hljs-string">'is-active'</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-string">'text-danger'</span>:<span class="hljs-literal">true</span>
    &#125;           
&#125;
<div :<span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"classObject"</span>><span class="hljs-number">12345</span></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><!--因为<span class="hljs-string">'is-active'</span>: <span class="hljs-literal">false</span>，所以is-active不被渲染-->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span> = <span class="hljs-string">"text-danger"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、三目型</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">'isred ? "red" : "blue"'</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、数组型</p>
<pre><code class="hljs language-js copyable" lang="js">data: &#123;
    <span class="hljs-attr">activeClass</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">errorClass</span>: <span class="hljs-string">'text-danger'</span>
&#125;
<p :<span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"[&#123;'is-active':activeClass&#125;,errorClass]"</span>><span class="hljs-number">12345</span></p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><!--因为<span class="hljs-string">'is-active'</span>: <span class="hljs-literal">false</span>，所以is-active不被渲染-->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span> = <span class="hljs-string">"text-danger"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>Object.assign</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">this</span>.$data,<span class="hljs-built_in">this</span>.$options.data())   <span class="hljs-comment">// 重置data</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>vm.$data</strong></p>
<p>获取Vue实例的data选项（对象）</p>
<p><strong>vm.$options</strong></p>
<p>获取Vue实例的自定义属性（如vm.$options.methods,获取Vue实例的自定义属性methods）</p>
<hr>
<p><strong>this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi><mi>l</mi><mtext>和</mtext><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">el 和 this.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord cjk_fallback">和</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>ref</strong></p>
<p><strong>this.$el</strong></p>
<p>获取Vue实例关联的DOM元素；</p>
<p><strong>this.$refs</strong></p>
<p>获取页面中所有含有ref属性的DOM元素（如this.$refs.hello，获取页面中含有属性ref = “hello”的DOM元素，如果有多个元素，那么只返回最后一个）</p>
<p>this.$el是在mounted中才会出现的，在created的时候是没有的，所以我们引用的时候</p>
<pre><code class="hljs language-js copyable" lang="js">mounted () &#123;
  <span class="hljs-built_in">this</span>.$el.addEventListener(<span class="hljs-string">'touchstart'</span>, <span class="hljs-built_in">this</span>.itemTouchStart)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不能再created中出现$el，在mounted中是ok的</p>
<hr>
<p><strong>1）$refs</strong></p>
<p>首先给子组件做标记，例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><firstchild ref=<span class="hljs-string">"one"</span>></firstchild>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在父组件中，通过this.$refs.one就可以访问了这个自组件了，包括访问自组件的data里面的数据，调用它的函数。</p>
<p><strong>2）$children</strong></p>
<p>它返回的是一个组件集合，如果你能清楚的知道子组件的顺序，你也可以使用下标来操作；</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-built_in">this</span>.$children.length;i++)&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$children[i].msg);输出子组件的msg数据；
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3）$parent</strong></p>
<p>示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$parent.$children[<span class="hljs-number">0</span>].query()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>总结一下：</strong></p>
<p>1）组件只能一个根节点；</p>
<p>2）可以在自定义组件中使用this.$parent.属性值，或者函数；</p>
<p>3）在父组件中可以使用this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>e</mi><mi>f</mi><mi>s</mi><mi mathvariant="normal">.</mi><mtext>组件的标记访问子组件，或者</mtext><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">refs.组件的标记访问子组件，或者this.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mord mathnormal">s</span><span class="mord">.</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">标</span><span class="mord cjk_fallback">记</span><span class="mord cjk_fallback">访</span><span class="mord cjk_fallback">问</span><span class="mord cjk_fallback">子</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">或</span><span class="mord cjk_fallback">者</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>children[i].属性(方法名)，访问子组件的属性或者方法；</p>
<p>4）需要注意this的指向。</p>
<hr>
<p><strong>事件修饰符</strong></p>
<p><strong>.stop</strong>  阻止事件继续传播</p>
<p><strong>.prevent</strong> 事件不再重载页面</p>
<p><strong>.capture</strong> 使用事件捕获模式,即元素自身触发的事件先在此处处理，然后才交由内部元素进行处理</p>
<p><strong>.self</strong> 只当在 event.target 是当前元素自身时触发处理函数</p>
<p><strong>.once</strong> 事件将只会触发一次</p>
<p><strong>.passive</strong> 告诉浏览器你不想阻止事件的默认行为</p>
<p><strong>示例：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><!-- 阻止单击事件继续传播 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">v-on:click.stop</span>=<span class="hljs-string">"doThis"</span>></span><span class="hljs-tag"></<span class="hljs-name">a</span>></span></span>

<!-- 提交事件不再重载页面 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">v-on:submit.prevent</span>=<span class="hljs-string">"onSubmit"</span>></span><span class="hljs-tag"></<span class="hljs-name">form</span>></span></span>

<!-- 只有修饰符 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">v-on:submit.prevent</span>></span><span class="hljs-tag"></<span class="hljs-name">form</span>></span></span>

<!-- 修饰符可以串联 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">v-on:click.stop.prevent</span>=<span class="hljs-string">"doThat"</span>></span><span class="hljs-tag"></<span class="hljs-name">a</span>></span></span>

<!-- 添加事件监听器时使用事件捕获模式 -->
<!-- 即元素自身触发的事件先在此处处理，然后才交由内部元素进行处理 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-on:click.capture</span>=<span class="hljs-string">"doThis"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

<!-- 只当在 event.target 是当前元素自身时触发处理函数 -->
<!-- 即事件不是从内部元素触发的 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-on:click.self</span>=<span class="hljs-string">"doThat"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

<!-- 点击事件将只会触发一次 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">v-on:click.once</span>=<span class="hljs-string">"doThis"</span>></span><span class="hljs-tag"></<span class="hljs-name">a</span>></span></span>

<!-- 滚动事件的默认行为 (即滚动行为) 将会立即触发 -->
<!-- 而不会等待 <span class="hljs-string">`onScroll`</span> 完成  -->
<!-- 这其中包含 <span class="hljs-string">`event.preventDefault()`</span> 的情况 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-on:scroll.passive</span>=<span class="hljs-string">"onScroll"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用修饰符时，顺序很重要；相应的代码会以同样的顺序产生。因此，用v-on:click.prevent.self会阻止所有的点击，而 v-on:click.self.prevent 只会阻止对元素自身的点击。</p>
<hr>
<p><strong>深层选择器</strong></p>
<p>让组件内部样式生效的写法：</p>
<p>修改第三方组件的CSS，这些都是 scoped 样式，移除 scope 或打开一个新的样式是不可能的。
现在，深层选择器  >>>   /deep/  ::v-deep  可以帮助你。</p>
<pre><code class="hljs language-js copyable" lang="js">&::v-deep   or     /deep/    or   >>> 
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>Vue刷新当前页面数据(reload) 【Vue开发小程序】</strong></p>
<pre><code class="hljs language-js copyable" lang="js">reLoad () &#123;
  <span class="hljs-comment">// console.log('getCurrentPages().length='+getCurrentPages().length)</span>
  <span class="hljs-comment">// console.log(getCurrentPages())</span>
  <span class="hljs-comment">// pages 获取到当前页码数,然后执行当前页的onLoad </span>
  <span class="hljs-comment">//(如果页面中初始化Ajax函数写在onShow或者onReady中的，那么这里将使用onShow或者onReady)</span>
  <span class="hljs-keyword">const</span> pages = getCurrentPages()
  pages[pages.length - <span class="hljs-number">1</span>].onLoad()
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>vue-cli如何新增自定义指令？</strong></p>
<p>1、创建局部指令</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">data</span>: &#123;    
    &#125;,
    <span class="hljs-comment">// 创建指令(可以多个)</span>
    <span class="hljs-attr">directives</span>: &#123;
        <span class="hljs-comment">// 指令名称</span>
        <span class="hljs-attr">dir1</span>: &#123;
            <span class="hljs-comment">// 被绑定元素插入父节点时调用（父节点存在即可调用，不必存在于document 中）</span>
            <span class="hljs-function"><span class="hljs-title">inserted</span>(<span class="hljs-params">el,binding</span>)</span> &#123;
                <span class="hljs-comment">// 指令中第一个参数是当前使用指令的DOM</span>
                <span class="hljs-built_in">console</span>.log(el);
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>);
                <span class="hljs-comment">// 对DOM进行操作</span>
                el.style.width = <span class="hljs-string">'200px'</span>;
                el.style.height = <span class="hljs-string">'200px'</span>;
                el.style.background = <span class="hljs-string">'#000'</span>;
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者在组件中也接受一个 directives 的选项</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
  &#125;,
  <span class="hljs-attr">directives</span>: &#123;
    <span class="hljs-attr">dir1</span> : &#123;
      <span class="hljs-comment">// 被绑定元素插入父节点时调用（父节点存在即可调用，不必存在于document 中）</span>
      inserted (el) &#123;
        el.focus()
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、全局指令</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.directive(<span class="hljs-string">'dir2'</span>, &#123;
    <span class="hljs-function"><span class="hljs-title">inserted</span>(<span class="hljs-params">el</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(el,binding);
        el.focus()
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、指令的使用</p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-dir1</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-dir2</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>vue如何自定义一个过滤器？</strong></p>
<p>html代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
     <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"msg"</span> /></span></span>
     &#123;&#123; msg| capitalize &#125;&#125;
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JS代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> vm=<span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
    <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">msg</span>:<span class="hljs-string">''</span>
    &#125;,
    <span class="hljs-attr">filters</span>: &#123;
      <span class="hljs-attr">capitalize</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (!value) <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
        value = value.toString()
        <span class="hljs-keyword">return</span> value.charAt(<span class="hljs-number">0</span>).toUpperCase() + value.slice(<span class="hljs-number">1</span>)
      &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>全局定义过滤器</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.filter(<span class="hljs-string">'capitalize'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!value) <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
    value = value.toString()
    <span class="hljs-keyword">return</span> value.charAt(<span class="hljs-number">0</span>).toUpperCase() + value.slice(<span class="hljs-number">1</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>过滤器接收表达式的值 (msg) 作为第一个参数。capitalize 过滤器将会收到 msg的值作为第一个参数。</p>
<p>Vue过滤器实际应用</p>
<pre><code class="hljs language-js copyable" lang="js"><div  <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"item-border"</span>>总计(元): &#123;&#123;(order.salePrice?order.salePrice:price)|numFilter&#125;&#125;</div>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">filters</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">numFilter</span>(<span class="hljs-params">value</span>)</span> &#123;
          <span class="hljs-comment">// 截取当前数据到小数点后两位</span>
          <span class="hljs-keyword">let</span> realVal = <span class="hljs-built_in">Number</span>(value).toFixed(<span class="hljs-number">2</span>)
          <span class="hljs-comment">// num.toFixed(2)获取的是字符串</span>
          <span class="hljs-keyword">return</span> <span class="hljs-built_in">Number</span>(realVal)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>如果组件里用使用计时器</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在组件销毁时(即切换组件或关闭页面)，调用destroyed方法清除计时器</span>
<span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">clearTimeout</span>(<span class="hljs-built_in">this</span>.timer)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>props 类型为数组或者对象时，不能直接定义空对象的默认值，必须使用 工厂函数 return 回一个默认值</p>
<pre><code class="hljs language-js copyable" lang="js">props: &#123;
    <span class="hljs-attr">options</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> []
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue中如何让v-for循环出来的列表里面的click事件只对当前列表内元素有效</p>
<pre><code class="hljs language-js copyable" lang="js"><li v-<span class="hljs-keyword">for</span>=<span class="hljs-string">'item in items'</span> @click=<span class="hljs-string">"toggle(item)"</span> key=<span class="hljs-string">"item.id"</span>>
　　<span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">'item.show'</span>></span>&#123;&#123;item.content&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
</li>
toggle:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item</span>)</span>&#123;
　　item.show=!item.show
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>动态添加背景图片</p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"img"</span> :style=<span class="hljs-string">"'background-image: url(https://images.weserv.nl/?url='+article.cover.url.substring(7)+');'"</span>></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>订阅多个变量突变</strong></p>
<p>watcher 不能监听多个变量，但我们可以将目标组合在一起作为一个新的 计算属性，并监视这个新的 "变量"。</p>
<pre><code class="hljs language-js copyable" lang="js">computed: &#123;
  multipleValues () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">value1</span>: <span class="hljs-built_in">this</span>.value1,
      <span class="hljs-attr">value2</span>: <span class="hljs-built_in">this</span>.value2,
    &#125;
  &#125;
&#125;,
<span class="hljs-attr">watch</span>: &#123;
  multipleValues (val, oldVal) &#123;
    <span class="hljs-built_in">console</span>.log(val)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>定时器的销毁</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">timer</span>: <span class="hljs-literal">null</span>
    &#125;
  &#125;,
  mounted () &#123;
    <span class="hljs-built_in">this</span>.timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Date</span>.now())
    &#125;, <span class="hljs-number">1000</span>)
  &#125;,
  beforeDestroy () &#123;
    <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.timer)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使其只能在生命周期钩子内访问。使用 $once 来放弃不必要的东西</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  mounted () &#123;
    <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>
    timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Date</span>.now())
    &#125;, <span class="hljs-number">1000</span>)
    <span class="hljs-built_in">this</span>.$once(<span class="hljs-string">'hook:beforeDestroy'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">clearInterval</span>(timer)
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            