
---
title: 'Vue实例的源码解析 (实例一)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2839'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 19:49:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=2839'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Vue实例的源码解析</h1>
<p>接下来我将用两个例子来讲解一个<code>vm</code>实例从无到有再到渲染页面的过程，可能比较复杂，望君能沉静下来。</p>
<p><strong>这里只讨论了关于实例的创建以及虚拟节点的创建和挂载部分，并没有讨论生成实例后的数据处理部分。关于数据处理部分我会在后续的文章中详细介绍</strong>。</p>
<h2 data-id="heading-1">示例一：</h2>
<p>示例一的代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./vue-dev/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
            <span class="hljs-attr">data</span>:&#123;
                <span class="hljs-attr">message</span>:<span class="hljs-number">123</span>
            &#125;
        &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个实例很简单，没有用到嵌套组件。接下来我们来讲解一下具体的流程。每一个组件实例都会经历三个阶段(在没有经过数据更改的情况下)，分别是：<code>数据处理阶段</code>，<code>生成vnode阶段</code>和<code>生成真实节点挂载阶段</code>。</p>
<h3 data-id="heading-2">数据处理阶段：</h3>
<p>当我们执行<code>new Vue</code>时候，会执行<code>Vue</code>构造函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Vue</span> (<span class="hljs-params">options</span>) </span>&#123; 
  <span class="hljs-comment">//options是我们传入的配置项</span>
  <span class="hljs-comment">//这个就是大名鼎鼎的vue构造函数，所有的vue项目的开始的地方</span>
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> &&
    !(<span class="hljs-built_in">this</span> <span class="hljs-keyword">instanceof</span> Vue)
    <span class="hljs-comment">//这里的this 其实使 vm实例，看是否用了new Vue</span>
  ) &#123;
    warn(<span class="hljs-string">'Vue is a constructor and should be called with the `new` keyword'</span>)
  &#125;
  <span class="hljs-comment">//这里的this是我们执行new Vue 时构造函数内部生成的实例对象，也可以理解为vm</span>
  <span class="hljs-built_in">this</span>._init(options)
  <span class="hljs-comment">//从这个函数进入我们用initMixin(Vue)初始化添加的_init函数</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给<code>Vue</code>构造函数传入我们的配置项<code>options</code>。此时<code>vm</code>实例已经创建完成，然后调用<code>this._init(options)</code>来初始化我们的数据。</p>
<p><code>vm._init()</code>函数位于<code>src/core/instance/init.js</code>。具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"> Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options?: <span class="hljs-built_in">Object</span></span>) </span>&#123;
    <span class="hljs-comment">//定义一个vm并指向this</span>
    <span class="hljs-keyword">const</span> vm: Component = <span class="hljs-built_in">this</span>
    <span class="hljs-comment">// a uid</span>
    <span class="hljs-comment">//为这个vm实例添加一个唯一的uid,每一个实例都有一个唯一的标识符</span>
    vm._uid = uid++
​
    <span class="hljs-keyword">let</span> startTag, endTag
    <span class="hljs-comment">/* istanbul ignore if */</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && config.performance && mark) &#123;
      startTag = <span class="hljs-string">`vue-perf-start:<span class="hljs-subst">$&#123;vm._uid&#125;</span>`</span>
      endTag = <span class="hljs-string">`vue-perf-end:<span class="hljs-subst">$&#123;vm._uid&#125;</span>`</span>
      mark(startTag)
    &#125;
    <span class="hljs-comment">//监听对象变化时用于过滤vm</span>
    <span class="hljs-comment">// a flag to avoid this being observed</span>
    vm._isVue = <span class="hljs-literal">true</span>
    <span class="hljs-comment">// merge options</span>
    <span class="hljs-comment">// _isComponent是内部创建子组件时才会添加为true的属性</span>
    <span class="hljs-keyword">if</span> (options && options._isComponent) &#123;
      <span class="hljs-comment">// optimize internal component instantiation</span>
      <span class="hljs-comment">// since dynamic options merging is pretty slow, and none of the</span>
      <span class="hljs-comment">// internal component options needs special treatment.</span>
      initInternalComponent(vm, options)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">//合并options</span>
      vm.$options = mergeOptions(
        <span class="hljs-comment">//resolveConstructorOptions函数在后面有定义</span>
        <span class="hljs-comment">//向该函数传入的是vm.constructor也就是Vue</span>
        resolveConstructorOptions(vm.constructor),
        options || &#123;&#125;,
        vm
      )
      <span class="hljs-comment">//vm.$options合并两项</span>
    &#125;
    <span class="hljs-comment">/* istanbul ignore else */</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      initProxy(vm)
    &#125; <span class="hljs-keyword">else</span> &#123;
      vm._renderProxy = vm
    &#125;
    <span class="hljs-comment">// expose real self</span>
    vm._self = vm
    initLifecycle(vm)
    initEvents(vm)
    initRender(vm)
    callHook(vm, <span class="hljs-string">'beforeCreate'</span>)
    initInjections(vm) <span class="hljs-comment">// resolve injections before data/props</span>
    initState(vm)
    initProvide(vm) <span class="hljs-comment">// resolve provide after data/props</span>
    callHook(vm, <span class="hljs-string">'created'</span>)
​
    <span class="hljs-comment">/* istanbul ignore if */</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && config.performance && mark) &#123;
      vm._name = formatComponentName(vm, <span class="hljs-literal">false</span>)
      mark(endTag)
      measure(<span class="hljs-string">`vue <span class="hljs-subst">$&#123;vm._name&#125;</span> init`</span>, startTag, endTag)
    &#125;
​
    <span class="hljs-keyword">if</span> (vm.$options.el) &#123;
      vm.$mount(vm.$options.el)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码非常好懂，首先是将我们的<code>vm</code>实例上挂载<code>uid</code>来标识每一个组件实例，然后添加<code>_isVue</code>。表示的是<code>Vue</code>组件，然后判断是否是一个组件，虽然说我们的根组件也是组件，但是它这里所说的组件其实表示的是子组件。例如你的模板中引入了一个组件。然显然我们的根实例不是子组件那种类型的，然后就会走<code>else</code>分支，该分支的作用是调用<code>mergeOptions</code>函数来合并<code>Vue.options</code>和我们传入的<code>options</code>，合并成一个总的<code>options</code>然后添加到<code>vm.$options</code>上。接着就是进行数据代理处理。当处理完之后会执行:</p>
<pre><code class="hljs language-js copyable" lang="js">  initLifecycle(vm)
    initEvents(vm)
    initRender(vm)
    callHook(vm, <span class="hljs-string">'beforeCreate'</span>)
    initInjections(vm) <span class="hljs-comment">// resolve injections before data/props</span>
    initState(vm)
    initProvide(vm) <span class="hljs-comment">// resolve provide after data/props</span>
    callHook(vm, <span class="hljs-string">'created'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些都是进行一些事件和数据的初始化的，在初始化的过程中会伴随着一些钩子函数的执行。组件的数据处理就集中在这里，我们这里不对数据处理的具体操作进行展开，因为后续会单独的讲解数据处理的部分。当<code>vue</code>数据处理完成后，就进入到了下一个阶段：<code>生成vnode阶段</code></p>
<h3 data-id="heading-3">生成vnode阶段:</h3>
<p>当数据处理完之后会执行:</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">if</span> (vm.$options.el) &#123;
      vm.$mount(vm.$options.el)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为根组件实例的<code>$el</code>是存在的，所以会执行<code>vm.$mount(vm.$options.el)</code>这个函数。该函数位于：<code>./src/platforms/web/entry-runtime-with-complier.js</code>文件中。具体的代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.prototype.$mount = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">
  el?: string | Element,<span class="hljs-comment">//我们传入的el类型有两种，一种是字符串'#app'，另一种是一个元素对象，例如document.getElementById('app')</span>
  hydrating?: boolean
</span>): <span class="hljs-title">Component</span> </span>&#123;  
  el = el && query(el)<span class="hljs-comment">//query函数主要是返回一个元素对象，如果我们传入的el存在，那么就返回该元素的对象形式，如果不存在，那么就会默认是一个div元素对象</span>

  <span class="hljs-comment">/* istanbul ignore if */</span>
  <span class="hljs-keyword">if</span> (el === <span class="hljs-built_in">document</span>.body || el === <span class="hljs-built_in">document</span>.documentElement) &#123;
    <span class="hljs-comment">//这里告诉我们el不能是body和html。原因是它会发生覆盖，这样就会将原来的模板完全覆盖掉。</span>
    process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && warn(
      <span class="hljs-string">`Do not mount Vue to <html> or <body> - mount to normal elements instead.`</span>
    )
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
  &#125;

  <span class="hljs-keyword">const</span> options = <span class="hljs-built_in">this</span>.$options<span class="hljs-comment">//这里的this指向的是vm实例对象</span>
  <span class="hljs-comment">// resolve template/el and convert to render function</span>
  <span class="hljs-keyword">if</span> (!options.render) &#123;
    <span class="hljs-comment">//如果我们没有render函数。那么会进入该区域代码。</span>
    <span class="hljs-keyword">let</span> template = options.template <span class="hljs-comment">//获取模板</span>
    <span class="hljs-keyword">if</span> (template) &#123;
      <span class="hljs-comment">//如果存在template配置项，</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> template === <span class="hljs-string">'string'</span>) &#123;<span class="hljs-comment">//如果配置项的类型为字符串。</span>
        <span class="hljs-keyword">if</span> (template.charAt(<span class="hljs-number">0</span>) === <span class="hljs-string">'#'</span>) &#123;<span class="hljs-comment">//这里我们只处理template为#xxx的格式的模板，也就是类似于template:'#app'这种</span>
          template = idToTemplate(template)<span class="hljs-comment">//该函数返回的是template模板内部的节点的字符串形式。</span>
          <span class="hljs-comment">/* istanbul ignore if */</span>
          <span class="hljs-comment">//这里是template的错误处理</span>
          <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && !template) &#123;
            warn(
              <span class="hljs-string">`Template element not found or is empty: <span class="hljs-subst">$&#123;options.template&#125;</span>`</span>,
              <span class="hljs-built_in">this</span>
            )
          &#125;
        &#125;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (template.nodeType) &#123;
        <span class="hljs-comment">//如果我们传入的template是一个节点对象，那么获取该节点对象中的innerHTML，然会的也是字符串形式</span>
        template = template.innerHTML
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">//不是以上两种格式，那么抛出错误</span>
        <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
          warn(<span class="hljs-string">'invalid template option:'</span> + template, <span class="hljs-built_in">this</span>)
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (el) &#123;
      <span class="hljs-comment">//如果template配置项不存在，那么获取el.outerHTML当作我们的template。返回的也是字符串类型</span>
      template = getOuterHTML(el)
    &#125;
    
    <span class="hljs-keyword">if</span> (template) &#123;
      <span class="hljs-comment">//这是处理好的template。这种template的来源有两种，第一种是我们自己设置的,另一种就是el.outerHTML来充当template</span>
      <span class="hljs-comment">/* istanbul ignore if */</span>
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && config.performance && mark) &#123;
        mark(<span class="hljs-string">'compile'</span>)
      &#125;


      <span class="hljs-comment">//接下来的代码是进行编译，将我们的模板编译成以js描述的对象，即虚拟DOM，然后将虚拟DOM转化为render(渲染函数)。</span>
      <span class="hljs-keyword">const</span> &#123; render, staticRenderFns &#125; = compileToFunctions(template, &#123;
        <span class="hljs-attr">outputSourceRange</span>: process.env.NODE_ENV !== <span class="hljs-string">'production'</span>,
        shouldDecodeNewlines,
        shouldDecodeNewlinesForHref,
        <span class="hljs-attr">delimiters</span>: options.delimiters,
        <span class="hljs-attr">comments</span>: options.comments
      &#125;, <span class="hljs-built_in">this</span>)
      options.render = render
      options.staticRenderFns = staticRenderFns 

      <span class="hljs-comment">/* istanbul ignore if */</span>
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && config.performance && mark) &#123;
        mark(<span class="hljs-string">'compile end'</span>)
        measure(<span class="hljs-string">`vue <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>._name&#125;</span> compile`</span>, <span class="hljs-string">'compile'</span>, <span class="hljs-string">'compile end'</span>)
      &#125;
    &#125;
  &#125;
  <span class="hljs-comment">//如果我们没有render函数，其实通过对template进行编译，我们就会获得render函数，</span>
  <span class="hljs-comment">//然后调用mount.call()函数。</span>
  <span class="hljs-comment">//如果我们自己有render函数，那么我们就可以直接调用mount.call函数，不需要去进行编译。</span>
  <span class="hljs-keyword">return</span> mount.call(<span class="hljs-built_in">this</span>, el, hydrating)<span class="hljs-comment">//this -> vm ; el -> 元素对象</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该函数做的事情很多，我们来具体分析，首先是获取到我们的<code>el</code>元素节点，然后判断我们的<code>el</code>是否是<code>body/html</code>。因为会发生覆盖问题，所以<code>Vue</code>不允许我们的根节点是<code>body/html</code>。然后获取<code>vm</code>实例上的<code>options.render</code>函数，因为我们没有定义<code>render</code>函数，所以就会去判断是否有<code>template</code>模板，我们也没有定义该模板，所以就会走<code>else if</code>的分支：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//如果template配置项不存在，那么获取el.outerHTML当作我们的template。返回的也是字符串类型</span>
      template = getOuterHTML(el)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为我们没有定义<code>template</code>模板，所以<code>Vue</code>就把我们的根节点作为了我们的<code>template</code>模板(字符串形式)。此时<code>vm</code>实例对象就有<code>template</code>模板了，所以会执行：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> &#123; render, staticRenderFns &#125; = compileToFunctions(template, &#123;
        <span class="hljs-attr">outputSourceRange</span>: process.env.NODE_ENV !== <span class="hljs-string">'production'</span>,
        shouldDecodeNewlines,
        shouldDecodeNewlinesForHref,
        <span class="hljs-attr">delimiters</span>: options.delimiters,
        <span class="hljs-attr">comments</span>: options.comments
      &#125;, <span class="hljs-built_in">this</span>)
 <span class="hljs-comment">//将生成的render函数挂载到options.render上</span>
      options.render = render
      options.staticRenderFns = staticRenderFns 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码是干什么的呢？它的作用是将我们的<code>tempalte</code>通过<code>Vue</code>内置的模板编译器把它变为一个<code>render</code>函数。然后将该函数挂载到<code>vm.options.render</code>上面去。<code>compileToFunctions</code>函数的内部比较复杂，有兴趣的话可以自己研究研究。这里提醒一下<code>render</code>函数是一个函数，不是<code>vdom</code>。</p>
<p>当这些执行完之后就会执行<code>mount.call(this, el, hydrating)</code>函数，可能你会问，<code>mount</code>函数是什么。这里简要说一下，<code>Vue</code>官方给我们提供了两个版本，第一个版本是我们的<code>runtime + complier</code>版本，另一个版本是<code>runtimeOnly</code>版本，这两个版本有什么不同呢？前者是允许我们写<code>template</code>的，或者说是允许我们添加<code>el</code>属性的，因为该版本内置的有编译器，而后者是让我们写<code>render</code>函数的，并不会进行模板编译处理，而<code>mount</code>函数是后者的挂载函数，为什么前者引用了呢。原因是因为我们前者虽然没有<code>render</code>函数，但是通过模板编译还是会生成，生成之后仍需要挂载，所以还是会用到<code>mount</code>函数。好了我们来看该函数内部的代码实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//  /web/runtime/index.js</span>
Vue.prototype.$mount = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">
  el?: string | Element,
  hydrating?: boolean
</span>): <span class="hljs-title">Component</span> </span>&#123;
  el = el && inBrowser ? query(el) : <span class="hljs-literal">undefined</span><span class="hljs-comment">//这里之所以对再一次的对el进行判断，是因为这里的$mount是runtime-only版本的，所以对你传入的el进行判断。</span>
  <span class="hljs-keyword">return</span> mountComponent(<span class="hljs-built_in">this</span>, el, hydrating)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先还是先获取<code>el</code>元素节点，然后执行<code>mountComponent()</code>函数。代码很简单，不过多介绍，我们接下来看<code>mountComponent</code>函数。该函数的具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//./src/core/instance/lifecycle.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mountComponent</span> (<span class="hljs-params">
  vm: Component,
  el: ?Element,
  hydrating?: boolean
</span>): <span class="hljs-title">Component</span> </span>&#123;
  vm.$el = el<span class="hljs-comment">//将el元素对象挂载到vm.$el上，也就是说，vm.$el是在执行$mount的时候挂载上去的。宏观的将，它是在created钩子函数之后，beforeMount钩子函数之前被挂载的。</span>
  <span class="hljs-keyword">if</span> (!vm.$options.render) &#123;<span class="hljs-comment">//这里的vm.$options.render是处理之后的render函数，也就是说，如果我们如果不传入render函数或者编译后的虚拟DOM无法生成render函数，那么vm.$options.render都为false</span>
    vm.$options.render = createEmptyVNode<span class="hljs-comment">//如果在上述中为真，那么我们就给vm.$options.render赋值一个由空虚拟DOM组成的渲染函数。</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      <span class="hljs-comment">/* istanbul ignore if */</span>
      <span class="hljs-comment">//这里的警告就是你用了runtime-only，但是你写了template/el那么就会报错，它只能接收render函数。这是版本问题</span>
      <span class="hljs-keyword">if</span> ((vm.$options.template && vm.$options.template.charAt(<span class="hljs-number">0</span>) !== <span class="hljs-string">'#'</span>) ||
        vm.$options.el || el) &#123;
        warn(
          <span class="hljs-string">'You are using the runtime-only build of Vue where the template '</span> +
          <span class="hljs-string">'compiler is not available. Either pre-compile the templates into '</span> +
          <span class="hljs-string">'render functions, or use the compiler-included build.'</span>,
          vm
        )
      &#125; <span class="hljs-keyword">else</span> &#123;
        warn(
          <span class="hljs-string">'Failed to mount component: template or render function not defined.'</span>,
          vm
        )
      &#125;
    &#125;
  &#125;
  <span class="hljs-comment">//触发berforeMount钩子函数</span>
  callHook(vm, <span class="hljs-string">'beforeMount'</span>)

  <span class="hljs-keyword">let</span> updateComponent
  <span class="hljs-comment">/* istanbul ignore if */</span>
  <span class="hljs-comment">//这和运行性能有关，暂时可以忽视</span>
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && config.performance && mark) &#123;
 ......
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">//最终定义updateComponent函数</span>
    updateComponent = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">//vm._update是在lifecycleMixin(Vue)中定义的</span>
      <span class="hljs-comment">//vm._render是在renderMixin中定义的。</span>
      <span class="hljs-comment">//hydrating:false</span>
      <span class="hljs-comment">//该函数的执行其实是在new Watcher()中执行的，我们暂时只关注它的执行，不去关注在什么地方触发。</span>
      vm._update(vm._render(), hydrating)
    &#125;
  &#125;

  <span class="hljs-comment">// we set this to vm._watcher inside the watcher's constructor</span>
  <span class="hljs-comment">// since the watcher's initial patch may call $forceUpdate (e.g. inside child</span>
  <span class="hljs-comment">// component's mounted hook), which relies on vm._watcher being already defined</span>
  <span class="hljs-keyword">new</span> Watcher(vm, updateComponent, noop, &#123;
    before () &#123;
      <span class="hljs-keyword">if</span> (vm._isMounted && !vm._isDestroyed) &#123;
        callHook(vm, <span class="hljs-string">'beforeUpdate'</span>)
      &#125;
    &#125;
  &#125;, <span class="hljs-literal">true</span> <span class="hljs-comment">/* isRenderWatcher */</span>)
  hydrating = <span class="hljs-literal">false</span>

  <span class="hljs-comment">// manually mounted instance, call mounted on self</span>
  <span class="hljs-comment">// mounted is called for render-created child components in its inserted hook</span>
  <span class="hljs-keyword">if</span> (vm.$vnode == <span class="hljs-literal">null</span>) &#123;
    vm._isMounted = <span class="hljs-literal">true</span>
    callHook(vm, <span class="hljs-string">'mounted'</span>)
  &#125;
  <span class="hljs-keyword">return</span> vm
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将<code>el</code>节点挂载到<code>vm</code>实例的<code>$el</code>属性上，然后判断<code>vm.$options.render</code>函数是否存在。因为<code>vm</code>实例已经通过编译根节点获取到<code>render</code>函数了，所以向下执行。在这里触发<code>beforeMount</code>钩子函数。</p>
<p>接着就定义<code>updateComponent</code>函数，其具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">  updateComponent = <span class="hljs-function">() =></span> &#123;
      vm._update(vm._render(), hydrating)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码是非常重要的，所以后面我们会经常讲他。</p>
<p>接下来的代码是定义一个<code>watcher</code>实例对象，具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">new</span> Watcher(vm, updateComponent, noop, &#123;
    before () &#123;
      <span class="hljs-keyword">if</span> (vm._isMounted && !vm._isDestroyed) &#123;
        callHook(vm, <span class="hljs-string">'beforeUpdate'</span>)
      &#125;
    &#125;
  &#125;, <span class="hljs-literal">true</span> <span class="hljs-comment">/* isRenderWatcher */</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么要定义<code>watcher</code>呢？每一个组件都会有一个自己的独一无二的<code>watcher</code>实例，<code>watcher</code>用要标识我们的组件，什么意思呢？如果我们的组件引用了一个属性，那么这个属性的<code>deps</code>中就会添加这个组件的<code>watcher</code>，表示该组件引用了该属性。就是追踪关系。现在我们进入<code>Watcher</code>构造函数的内部，来解析一下它的具体代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//D:\vue-src-jx\vue-dev\vue-dev\src\core\observer\watcher.js</span>
<span class="hljs-title">constructor</span> (<span class="hljs-params">
    vm: Component,
    expOrFn: string | <span class="hljs-built_in">Function</span>,<span class="hljs-comment">//updateComponent</span>
    cb: <span class="hljs-built_in">Function</span>,
    options?: ?<span class="hljs-built_in">Object</span>,
    isRenderWatcher?: boolean
  </span>) &#123;
    <span class="hljs-built_in">this</span>.vm = vm
    <span class="hljs-keyword">if</span> (isRenderWatcher) &#123;
      vm._watcher = <span class="hljs-built_in">this</span>
    &#125;
    vm._watchers.push(<span class="hljs-built_in">this</span>)
    <span class="hljs-comment">// options</span>
    <span class="hljs-keyword">if</span> (options) &#123;
      <span class="hljs-built_in">this</span>.deep = !!options.deep
      <span class="hljs-built_in">this</span>.user = !!options.user
      <span class="hljs-built_in">this</span>.lazy = !!options.lazy
      <span class="hljs-built_in">this</span>.before = options.before
      <span class="hljs-built_in">this</span>.sync = !!options.sync
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.deep = <span class="hljs-built_in">this</span>.user = <span class="hljs-built_in">this</span>.lazy = <span class="hljs-built_in">this</span>.sync = <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-built_in">this</span>.cb = cb
    <span class="hljs-built_in">this</span>.id = ++uid <span class="hljs-comment">// uid for batching</span>
    <span class="hljs-built_in">this</span>.active = <span class="hljs-literal">true</span>
    <span class="hljs-built_in">this</span>.dirty = <span class="hljs-built_in">this</span>.lazy <span class="hljs-comment">// for lazy watchers </span>
    <span class="hljs-built_in">this</span>.deps = []
    <span class="hljs-built_in">this</span>.newDeps = []
    <span class="hljs-built_in">this</span>.depIds = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>() 
    <span class="hljs-built_in">this</span>.newDepIds = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
    <span class="hljs-built_in">this</span>.expression = process.env.NODE_ENV !== <span class="hljs-string">'production'</span>
      ? expOrFn.toString()
      : <span class="hljs-string">''</span>
    <span class="hljs-comment">// parse expression for getter</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> expOrFn === <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-built_in">this</span>.getter = expOrFn
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.getter = parsePath(expOrFn)
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.getter) &#123;
        <span class="hljs-built_in">this</span>.getter = noop
        process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && warn(
          <span class="hljs-string">`Failed watching path: "<span class="hljs-subst">$&#123;expOrFn&#125;</span>" `</span> +
          <span class="hljs-string">'Watcher only accepts simple dot-delimited paths. '</span> +
          <span class="hljs-string">'For full control, use a function instead.'</span>,
          vm
        )
      &#125;
    &#125;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.lazy
      ? <span class="hljs-literal">undefined</span>
      : <span class="hljs-built_in">this</span>.get()
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们只放出了<code>Watcher</code>构造函数的<code>constructor</code>函数，因为其他的函数时辅助函数，没有必要一次性放出来。首先将<code>vm</code>实例对象挂载到<code>watcher.vm</code>上，然后判断是否是渲染<code>watcher</code>。在<code>Vue</code>中的<code>watcher</code>分为两种：<code>renderWatcher/userWatcher</code>。我的理解是<code>renderWatcher</code>是：属性的<code>deps</code>中的<code>watcher</code>是渲染<code>watcher</code>。因为在生成<code>vdom</code>的时候组件会去引用一些属性，而属性就会把这些组件的<code>watcher</code>放到它们的<code>deps</code>当中，也就是在渲染生成<code>vdom</code>的时候添加的<code>watcher</code>叫做渲染<code>watcher</code>。而<code>userWatcher</code>指的是当我们在<code>vm.$watch</code>函数中引入的属性，此时也会把组件的<code>watcher</code>放入到属性的<code>deps</code>中，只不过这种不是在渲染的时候添加的<code>watcher</code>是<code>userWatcher</code>。回到我们的代码当中，因为在执行<code>new Watcher</code>的时候传入的<code>isRenderWatcher === true</code>。所以是渲染<code>watcher</code>，这样就会将该<code>watcher</code>添加到<code>vm._watcher</code>上。后续的代码就是为实例的<code>watcher</code>添加各种属性。其中有几行需要我们注意：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.before = options.before
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个是用来添加下面的函数的：</p>
<pre><code class="hljs language-js copyable" lang="js">  before () &#123;
      <span class="hljs-keyword">if</span> (vm._isMounted && !vm._isDestroyed) &#123;
        callHook(vm, <span class="hljs-string">'beforeUpdate'</span>)
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后为每一个<code>watcher</code>都添加一个<code>uid</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.id = ++uid
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然感觉这行代码很不起眼，但是将会在我们的组件更新上面起到很大的作用，那就是组件的更新顺序。</p>
<p>然后为<code>watcher</code>实例添加下面的属性：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-built_in">this</span>.deps = []
    <span class="hljs-built_in">this</span>.newDeps = []
    <span class="hljs-built_in">this</span>.depIds = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>() 
    <span class="hljs-built_in">this</span>.newDepIds = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个是用来依赖收集的，这里我们不过多展开。然后判断<code>expOrFn</code>是否是一个函数，这个变量就是传入的<code>updateComponent</code>函数，然后就执行：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.lazy
      ? <span class="hljs-literal">undefined</span>
      : <span class="hljs-built_in">this</span>.get()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来看看<code>watcher.get()</code>函数做了什么：</p>
<pre><code class="hljs language-js copyable" lang="js">  get () &#123;
    pushTarget(<span class="hljs-built_in">this</span>)
    <span class="hljs-keyword">let</span> value
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>.vm
    <span class="hljs-keyword">try</span> &#123;
      value = <span class="hljs-built_in">this</span>.getter.call(vm, vm)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.user) &#123;  
        handleError(e, vm, <span class="hljs-string">`getter for watcher "<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.expression&#125;</span>"`</span>)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">throw</span> e
      &#125; 
    &#125; <span class="hljs-keyword">finally</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.deep) &#123;
        traverse(value)
      &#125;
      popTarget()<span class="hljs-comment">//</span>
      <span class="hljs-built_in">this</span>.cleanupDeps()
    &#125;
    <span class="hljs-keyword">return</span> value
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先就是执行：<code>pushTarget(this)</code>，这里的<code>this</code>指向的是<code>watcher</code>实例对象，而<code>pushTarget</code>函数是干什么的呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushTarget</span> (<span class="hljs-params">target: ?Watcher</span>) </span>&#123;
  targetStack.push(target)
  Dep.target = target
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数的作用是将我们的<code>watcher</code>实例对象放入到<code>targetStack</code>栈中，然后<code>Dep.target = target</code>。为什么这样做呢？这是很有讲究的，首先，<code>Vue</code>是不是正在创建根组件实例对象，后面会有生成<code>vnode</code>环节，那么当我们访问到一个属性的时候，是不是一定会触发它们的<code>get</code>函数，那么此时它就知道有组件引用了它。但是，没错我要说但是了，它不知道谁引用的，就像你蒙着眼被班里的同学亲了一下，你知道你被亲了，但是你不知道是谁亲的。那么这个属性如何判断是谁亲(呸，是谁引用)的呢？答案很简单，那就是当一个组件在渲染的时候先把这个组件的<code>watcher</code>给放到全局的变量<code>Dep.target</code>上，当有组件引用的时候，属性就看<code>Dep.target</code>上存的是谁的<code>watcher</code>，然后就将该<code>watcher</code>放到自己的<code>deps</code>口袋里，当该属性的值改变的时候就会循环遍历通知每一个<code>watcher</code>。此时可能还有疑问，你是怎么确定当有属性被引用的时候就一定是<code>Dep.target</code>上的<code>wathcer</code>对应的组件引用的呢？嗯，这个问题问的不错，这是一个哲学问题......，哈哈开玩笑的，原因很简单，当我们的组件在将要渲染的时候会把它对应的<code>watcher</code>放到<code>Dep.target</code>上去，那么此时是不是该组件正在占用<code>Dep.target</code>。好了问题就来了，现在我们的组件要渲染生成<code>vnode</code>了，生成的过程中一定会引用属性，你觉得哪些属性会被触发<code>get</code>函数呢？当然<code>watcher</code>对应的组件所引用的属性，该属性倒是想让其他的组件引用它呢，但是其他的组件没有渲染，怎么会引用它的，只有当前的根组件引用了它，当然是根组件引用它了。这就好比你在班里被蒙着眼，此时班里只有一个人，你觉得是谁亲的呢，答案很明显了。所以希望大家都能找到自己的另一半。好了，关于<code>pushTarget</code>就暂时到这里了。让我们回到<code>watcher.get()</code>函数当中，获取<code>watcher</code>所对应的组件实例，然后执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.getter.call(vm, vm)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实等价于执行：</p>
<pre><code class="hljs language-js copyable" lang="js">updateComponent.call(vm,vm)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，到了我们的重头戏了，我们先来回顾一下该函数的定义：</p>
<pre><code class="hljs language-js copyable" lang="js">  updateComponent = <span class="hljs-function">() =></span> &#123;
      vm._update(vm._render(), hydrating)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>进入到该函数中，首先我们执行的是<code>vm._render()</code>函数，我先剧透一下，它的主要目的是生成组件对应的<code>vnode</code>。那它具体是怎么生成的呢？我们来看<code>vm._render</code>的具体代码：</p>
<pre><code class="hljs language-js copyable" lang="js">  
  Vue.prototype._render = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>): <span class="hljs-title">VNode</span> </span>&#123;
    <span class="hljs-keyword">const</span> vm: Component = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">const</span> &#123; render, _parentVnode &#125; = vm.$options<span class="hljs-comment">//从vm.$options中拿到render函数。</span>

    <span class="hljs-keyword">if</span> (_parentVnode) &#123;
      vm.$scopedSlots = normalizeScopedSlots(
        _parentVnode.data.scopedSlots,
        vm.$slots,
        vm.$scopedSlots
      )
    &#125;

    <span class="hljs-comment">// set parent vnode. this allows render functions to have access</span>
    <span class="hljs-comment">// to the data on the placeholder node.</span>
    vm.$vnode = _parentVnode
    <span class="hljs-comment">// render self</span>
    <span class="hljs-keyword">let</span> vnode
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// There's no need to maintain a stack because all render fns are called</span>
      <span class="hljs-comment">// separately from one another. Nested component's render fns are called</span>
      <span class="hljs-comment">// when parent component is patched.</span>
      currentRenderingInstance = vm
      <span class="hljs-comment">//vm._renderProxy在生产环境下其实就是vm。通过调用render函数来生产vnode。</span>
      <span class="hljs-comment">//</span>
      vnode = render.call(vm._renderProxy, vm.$createElement)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      handleError(e, vm, <span class="hljs-string">`render`</span>)
      <span class="hljs-comment">// return error render result,</span>
      <span class="hljs-comment">// or previous vnode to prevent render error causing blank component</span>
      <span class="hljs-comment">/* istanbul ignore else */</span>
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && vm.$options.renderError) &#123;
        <span class="hljs-keyword">try</span> &#123;
          vnode = vm.$options.renderError.call(vm._renderProxy, vm.$createElement, e)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          handleError(e, vm, <span class="hljs-string">`renderError`</span>)
          vnode = vm._vnode
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        vnode = vm._vnode
      &#125;
    &#125; <span class="hljs-keyword">finally</span> &#123;
      currentRenderingInstance = <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-comment">// if the returned array contains only a single node, allow it</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(vnode) && vnode.length === <span class="hljs-number">1</span>) &#123;
      vnode = vnode[<span class="hljs-number">0</span>]
    &#125;
    <span class="hljs-comment">// return empty vnode in case the render function errored out</span>
    <span class="hljs-keyword">if</span> (!(vnode <span class="hljs-keyword">instanceof</span> VNode)) &#123;
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && <span class="hljs-built_in">Array</span>.isArray(vnode)) &#123;
        warn(
          <span class="hljs-string">'Multiple root nodes returned from render function. Render function '</span> +
          <span class="hljs-string">'should return a single root node.'</span>,
          vm
        )
      &#125;
      vnode = createEmptyVNode()
    &#125;
    <span class="hljs-comment">// set parent</span>
    vnode.parent = _parentVnode
    <span class="hljs-keyword">return</span> vnode
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先看最后一行代码：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">return</span> vnode
<span class="copy-code-btn">复制代码</span></code></pre>
<p>懂我意思吧[挑眉]。首先从<code>vm.$options</code>中解构出<code>render/_parentVnode</code>两个值，然后判断，因为<code>vm</code>实例没有<code>_parentVnode</code>所以不会执行该分支代码。然后执行：</p>
<pre><code class="hljs language-js copyable" lang="js">vnode = render.call(vm._renderProxy, vm.$createElement)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为<code>vm</code>实例对象的<code>render</code>函数不是我们传入的，而是通过编译模板得到的，所以<code>render</code>函数算是<code>Vue</code>内部的函数，所以不能够直接的得到，但是这并不能够影响我们接下来的讲解。</p>
<p>我们可以通过代码调试的方式获取到了它的内部代码：</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">anonymous</span>(<span class="hljs-params">
</span>) </span>&#123;
<span class="hljs-function"><span class="hljs-title">with</span>(<span class="hljs-params"><span class="hljs-built_in">this</span></span>)</span>&#123;<span class="hljs-keyword">return</span> _c(<span class="hljs-string">'div'</span>,&#123;<span class="hljs-attr">attrs</span>:&#123;<span class="hljs-string">"id"</span>:<span class="hljs-string">"app"</span>&#125;&#125;,[_c(<span class="hljs-string">'span'</span>,[_v(_s(message))])])&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们发现它最后调用了<code>_c</code>方法，那么我们就来看<code>vm._c</code>方法是何方神圣。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//D:\vue-src-jx\vue-dev\vue-dev\src\core\instance\render.js</span>
vm._c = <span class="hljs-function">(<span class="hljs-params">a, b, c, d</span>) =></span> createElement(vm, a, b, c, d, <span class="hljs-literal">false</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们从上面的代码可以看到编译后的<code>render</code>的模样，我们来分别讲一下<code>a/b/c/d</code>代表什么，按照顺序分别是：标签名，<code>data</code>，<code>childrend</code>即该节点的直属子节点，<code>normalizationType</code>。这里的<code>data</code>很有意思，为什么这么说呢，有没有发现在内部代码的时候<code>Vue</code>一共调用了两次<code>_c</code>函数，但是参数却不同，第一个传入了三个参数，而第二个传入了两个参数。所以<code>data</code>代表什么就不确定了，可能是该节点的属性对象，也可能是该节点的子节点数组。无论是哪种，都会执行这个操作：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//这是  createElement 函数中的代码</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(data) || isPrimitive(data)) &#123;
    normalizationType = children
    children = data
    data = <span class="hljs-literal">undefined</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就执行了：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">return</span> _createElement(context, tag, data, children, normalizationType)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在向下讲之前，我们回头来看一下上面的一段代码：</p>
<pre><code class="hljs language-js copyable" lang="js">_c(<span class="hljs-string">'div'</span>,&#123;<span class="hljs-attr">attrs</span>:&#123;<span class="hljs-string">"id"</span>:<span class="hljs-string">"app"</span>&#125;&#125;,[_c(<span class="hljs-string">'span'</span>,[_v(_s(message))])])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码中我们可以看到<code>Vue</code>一共调用了两次<code>_c</code>函数，其实每调用一次会有很复杂的操作，但是为了让大家能够明白里面发生了什么，所以我两个函数的调用都会讲。根据调用顺序，首先调用的是第二个<code>_c</code>函数(其实本质上会先调用<code>_s/_v</code>这两个函数，但是这并不是我们讲的重点)，我们把传入的参数一一对应：</p>
<pre><code class="hljs language-js copyable" lang="js">a:<span class="hljs-string">'span'</span>
<span class="hljs-attr">b</span>:[VNode]<span class="hljs-comment">//这个vnode其实就是一个生成好的文本节点，因为如果再往下讲文本节点有点麻烦，所以就省略掉了</span>
<span class="hljs-attr">c</span>:<span class="hljs-literal">undefined</span>
<span class="hljs-attr">d</span>:<span class="hljs-literal">undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们进行到<code>_c</code>函数的内部，其实它的内部就是调用了<code>createElement(vm, a, b, c, d, false)</code>。我们来看看该函数内部的具体的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span> (<span class="hljs-params">
  context: Component,
  tag: any,
  data: any,
  children: any,
  normalizationType: any,
  alwaysNormalize: boolean
</span>)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们先展示它传入的参数，内部代码后续再展示，我们把参数一一对应一下：</p>
<pre><code class="hljs language-js copyable" lang="js">context:vm
<span class="hljs-attr">tag</span>:<span class="hljs-string">'span'</span>
<span class="hljs-attr">data</span>:[VNode]
<span class="hljs-attr">children</span>:<span class="hljs-literal">undefined</span>
<span class="hljs-attr">normalizationType</span>:<span class="hljs-literal">undefined</span>
<span class="hljs-attr">alwaysNormalize</span>:<span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们逐行讲解该函数内部的代码，首先是：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(data) || isPrimitive(data)) &#123;
    normalizationType = children
    children = data
    data = <span class="hljs-literal">undefined</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一通操作后，那么此时的变量就变为了：</p>
<pre><code class="hljs language-js copyable" lang="js">context:vm
<span class="hljs-attr">tag</span>:<span class="hljs-string">'span'</span>
<span class="hljs-attr">data</span>:<span class="hljs-literal">undefined</span>
<span class="hljs-attr">children</span>:[VNode]
<span class="hljs-attr">normalizationType</span>:<span class="hljs-literal">undefined</span>
<span class="hljs-attr">alwaysNormalize</span>:<span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这相当于参数值后移？对的，后移。然后执行：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">if</span> (isTrue(alwaysNormalize)) &#123;
    normalizationType = ALWAYS_NORMALIZE
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显该分支走不到，然后就执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">return</span> _createElement(context, tag, data, children, normalizationType)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来看看<code>_createElement()</code>函数，和上面一样，我们先展示参数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span> (<span class="hljs-params">
  context: Component,
  tag: any,
  data: any,
  children: any,
  normalizationType: any,
  alwaysNormalize: boolean
</span>)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们将参数一一对应：</p>
<pre><code class="hljs language-js copyable" lang="js">context:vm
<span class="hljs-attr">tag</span>:<span class="hljs-string">'span'</span>
<span class="hljs-attr">data</span>:<span class="hljs-literal">undefined</span>
<span class="hljs-attr">children</span>:[VNode]
<span class="hljs-attr">normalizationType</span>:<span class="hljs-literal">undefined</span>
<span class="hljs-attr">alwaysNormalize</span>:<span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们来逐行的解读代码，首先执行的是：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">if</span> (isDef(data) && isDef((data: any).__ob__)) &#123;
    process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && warn(
      <span class="hljs-string">`Avoid using observed data object as vnode data: <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(data)&#125;</span>\n`</span> +
      <span class="hljs-string">'Always create fresh vnode data objects in each render!'</span>,
      context
    )
    <span class="hljs-keyword">return</span> createEmptyVNode()
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为我们的<code>data</code>不存在，所以走不到这个分支，然后：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">if</span> (isDef(data) && isDef(data.is)) &#123;
    tag = data.is
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也走不到，我们继续看：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">if</span> (isDef(data) && isDef(data.is)) &#123;
    tag = data.is
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>走不到，我们继续看：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">if</span> (!tag) &#123;
    <span class="hljs-comment">// in case of component :is set to falsy value</span>
    <span class="hljs-keyword">return</span> createEmptyVNode()
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>走不到，我们继续看：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> &&
    isDef(data) && isDef(data.key) && !isPrimitive(data.key)
  ) &#123;
    <span class="hljs-keyword">if</span> (!__WEEX__ || !(<span class="hljs-string">'@binding'</span> <span class="hljs-keyword">in</span> data.key)) &#123;
      warn(
        <span class="hljs-string">'Avoid using non-primitive value as key, '</span> +
        <span class="hljs-string">'use string/number value instead.'</span>,
        context
      )
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>走不到，我们继续看：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(children) &&
    <span class="hljs-keyword">typeof</span> children[<span class="hljs-number">0</span>] === <span class="hljs-string">'function'</span>
  ) &#123;
    data = data || &#123;&#125;
    data.scopedSlots = &#123; <span class="hljs-attr">default</span>: children[<span class="hljs-number">0</span>] &#125;
    children.length = <span class="hljs-number">0</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，这段代码也走不到，我们接着看：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">if</span> (normalizationType === ALWAYS_NORMALIZE) &#123;
    children = normalizeChildren(children)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (normalizationType === SIMPLE_NORMALIZE) &#123;
    children = simpleNormalizeChildren(children)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码也走不到，其实这段代码是将<code>vm</code>实例的<code>children</code>数组扁平化。然后继续执行：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">let</span> vnode, ns
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> tag === <span class="hljs-string">'string'</span>) &#123;  
    <span class="hljs-keyword">let</span> Ctor
    ns = (context.$vnode && context.$vnode.ns) || config.getTagNamespace(tag)
    <span class="hljs-keyword">if</span> (config.isReservedTag(tag)) &#123;
      <span class="hljs-comment">// platform built-in elements</span>
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && isDef(data) && isDef(data.nativeOn)) &#123;
        warn(
          <span class="hljs-string">`The .native modifier for v-on is only valid on components but it was used on <<span class="hljs-subst">$&#123;tag&#125;</span>>.`</span>,
          context
        )
      &#125;
      vnode = <span class="hljs-keyword">new</span> VNode(
        config.parsePlatformTagName(tag), data, children,
        <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, context
      )
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> ((!data || !data.pre) && isDef(Ctor = resolveAsset(context.$options, <span class="hljs-string">'components'</span>, tag))) &#123;
      <span class="hljs-comment">// component</span>
      <span class="hljs-keyword">debugger</span>
      vnode = createComponent(Ctor, data, context, children, tag)
      <span class="hljs-built_in">console</span>.log(vnode)
    &#125; <span class="hljs-keyword">else</span> &#123;
      vnode = <span class="hljs-keyword">new</span> VNode(
        tag, data, children,
        <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, context
      )
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    vnode = createComponent(tag, data, context, children)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先定义两个变量<code>vnode/ns</code>，然后判断我们的<code>tag</code>是否是<code>string</code>类型的，很明显，是的，然后执行：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> Ctor
    ns = (context.$vnode && context.$vnode.ns) || config.getTagNamespace(tag)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为我们暂时还没有生成<code>vnode</code>。所以是没有<code>$vnode</code>这个属性的，那么就会调用<code>config.getTagNamespace</code>。这个函数的作用很简单，它的代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTagNamespace</span> (<span class="hljs-params">tag</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isSVG(tag)) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'svg'</span>
    &#125;
    <span class="hljs-comment">// basic support for MathML</span>
    <span class="hljs-comment">// note it doesn't support other MathML elements being component roots</span>
    <span class="hljs-keyword">if</span> (tag === <span class="hljs-string">'math'</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'math'</span>
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以<code>ns</code>的结果是<code>undefined</code>。然后执行：</p>
<pre><code class="hljs language-js copyable" lang="js">config.isReservedTag(tag)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数判断<code>tag</code>是否是保留标记，就是判断该<code>tag</code>是否是<code>html</code>标签，仅此而已，我们继续看代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && isDef(data) && isDef(data.nativeOn)) &#123;
        warn(
          <span class="hljs-string">`The .native modifier for v-on is only valid on components but it was used on <<span class="hljs-subst">$&#123;tag&#125;</span>>.`</span>,
          context
        )
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个分支是走不到的，所以会执行下面的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"> vnode = <span class="hljs-keyword">new</span> VNode(
        config.parsePlatformTagName(tag), data, children,
        <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, context
      )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，要开始正是的创建一个<code>vnode</code>了。</p>
<p>在创建<code>vnode</code>之前，我们需要搞明白，我们到底创建的是谁的<code>vnode</code>。<code>vue</code>执行的是第二个<code>_c()</code>函数，说明创建的是子元素节点<code>span</code>的<code>vnode</code>。<code>VNode</code>构造函数没有什么特别的操作，其主要的目的就是创建一个对象，而这个对象里面有一些属性，那么我们来具体的看看都有哪些属性：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-title">constructor</span> (<span class="hljs-params">
    tag?: string,
    data?: VNodeData,
    children?: ?<span class="hljs-built_in">Array</span><VNode>,
    text?: string,
    elm?: Node,
    context?: Component,
    componentOptions?: VNodeComponentOptions,
    asyncFactory?: <span class="hljs-built_in">Function</span>
  </span>) &#123;
      <span class="hljs-comment">/*当前节点的标签名*/</span>
      <span class="hljs-built_in">this</span>.tag = tag
      <span class="hljs-comment">/*当前节点对应的对象，包含了具体的一些数据信息，是一个VNodeData类型，可以参考VNodeData类型中的数据信息*/</span>
      <span class="hljs-built_in">this</span>.data = data
      <span class="hljs-comment">/*当前节点的子节点，是一个数组*/</span>
      <span class="hljs-built_in">this</span>.children = children
      <span class="hljs-comment">/*当前节点的文本*/</span>
      <span class="hljs-built_in">this</span>.text = text
      <span class="hljs-comment">/*当前虚拟节点对应的真实dom节点*/</span>
      <span class="hljs-built_in">this</span>.elm = elm
      <span class="hljs-comment">/*当前节点的名字空间*/</span>
      <span class="hljs-built_in">this</span>.ns = <span class="hljs-literal">undefined</span>
      <span class="hljs-comment">/*编译作用域*/</span>
      <span class="hljs-built_in">this</span>.context = context
      <span class="hljs-comment">/*函数化组件作用域*/</span>
      <span class="hljs-built_in">this</span>.functionalContext = <span class="hljs-literal">undefined</span>
      <span class="hljs-comment">/*节点的key属性，被当作节点的标志，用以优化*/</span>
      <span class="hljs-built_in">this</span>.key = data && data.key
      <span class="hljs-comment">/*组件的option选项*/</span>
      <span class="hljs-built_in">this</span>.componentOptions = componentOptions
      <span class="hljs-comment">/*当前节点对应的组件的实例*/</span>
      <span class="hljs-built_in">this</span>.componentInstance = <span class="hljs-literal">undefined</span>
      <span class="hljs-comment">/*当前节点的父节点*/</span>
      <span class="hljs-built_in">this</span>.parent = <span class="hljs-literal">undefined</span>
      <span class="hljs-comment">/*简而言之就是是否为原生HTML或只是普通文本，innerHTML的时候为true，textContent的时候为false*/</span>
      <span class="hljs-built_in">this</span>.raw = <span class="hljs-literal">false</span>
      <span class="hljs-comment">/*静态节点标志*/</span>
      <span class="hljs-built_in">this</span>.isStatic = <span class="hljs-literal">false</span>
      <span class="hljs-comment">/*是否作为跟节点插入*/</span>
      <span class="hljs-built_in">this</span>.isRootInsert = <span class="hljs-literal">true</span>
      <span class="hljs-comment">/*是否为注释节点*/</span>
      <span class="hljs-built_in">this</span>.isComment = <span class="hljs-literal">false</span>
      <span class="hljs-comment">/*是否为克隆节点*/</span>
      <span class="hljs-built_in">this</span>.isCloned = <span class="hljs-literal">false</span>
      <span class="hljs-comment">/*是否有v-once指令*/</span>
      <span class="hljs-built_in">this</span>.isOnce = <span class="hljs-literal">false</span>
    <span class="hljs-built_in">this</span>.asyncFactory = asyncFactory
    <span class="hljs-built_in">this</span>.asyncMeta = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.isAsyncPlaceholder = <span class="hljs-literal">false</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里只展示了一部分的代码，主要是来初始化我们的<code>vnode</code>实例的。我们来看看创建完成的<code>vnode</code>是个什么样子的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//span 的 vnode</span>
&#123;
<span class="hljs-attr">asyncFactory</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">asyncMeta</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">children</span>: [VNode]
<span class="hljs-attr">componentInstance</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">componentOptions</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">context</span>: Vue &#123;<span class="hljs-attr">_uid</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">_isVue</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">$options</span>: &#123;…&#125;, <span class="hljs-attr">_renderProxy</span>: <span class="hljs-built_in">Proxy</span>, <span class="hljs-attr">_self</span>: Vue, …&#125;
<span class="hljs-attr">data</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">elm</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">fnContext</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">fnOptions</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">fnScopeId</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">isAsyncPlaceholder</span>: <span class="hljs-literal">false</span>
<span class="hljs-attr">isCloned</span>: <span class="hljs-literal">false</span>
<span class="hljs-attr">isComment</span>: <span class="hljs-literal">false</span>
<span class="hljs-attr">isOnce</span>: <span class="hljs-literal">false</span>
<span class="hljs-attr">isRootInsert</span>: <span class="hljs-literal">true</span>
<span class="hljs-attr">isStatic</span>: <span class="hljs-literal">false</span>
<span class="hljs-attr">key</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">ns</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">parent</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">raw</span>: <span class="hljs-literal">false</span>
<span class="hljs-attr">tag</span>: <span class="hljs-string">"span"</span>
<span class="hljs-attr">text</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">child</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">__proto__</span>: <span class="hljs-built_in">Object</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是它展开后的，为了方便起见，我们看它没有展开的样子：</p>
<pre><code class="hljs language-js copyable" lang="js">VNode &#123;<span class="hljs-attr">tag</span>: <span class="hljs-string">"span"</span>, <span class="hljs-attr">data</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-attr">children</span>: <span class="hljs-built_in">Array</span>(<span class="hljs-number">1</span>), <span class="hljs-attr">text</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-attr">elm</span>: <span class="hljs-literal">undefined</span>, …&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们从没有展开的<code>vnode</code>可以看出：首先，<code>vnode</code>只是一个对象，而这个对象是用来描述的<code>span</code>节点的。<code>vnode</code>就是我们<code>span</code>节点的对象描述形式。</p>
<p>好了，当<code>vm</code>实例生成了<code>vnode</code>之后，代码进行回退。回到<code>_craeteElement</code>函数当中来。接下来执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(vnode)) &#123;
    <span class="hljs-keyword">return</span> vnode
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(vnode)) &#123;
    <span class="hljs-keyword">if</span> (isDef(ns)) applyNS(vnode, ns)
    <span class="hljs-keyword">if</span> (isDef(data)) registerDeepBindings(data)
    <span class="hljs-keyword">return</span> vnode
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> createEmptyVNode()
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们会发现，其实这段代码只会执行<code>else if</code>分支，但是这个分支里面的其他分支是不执行的，也就是说，这段代码并没对<code>vnode</code>做了什么，然后直接返回。然后回退到<code>createElement</code>函数，因为是最后一行代码会接着回退。然后它回退到什么时候停止呢？答案是回退到这段代码后停止：</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">anonymous</span>(<span class="hljs-params">
</span>) </span>&#123;
<span class="hljs-function"><span class="hljs-title">with</span>(<span class="hljs-params"><span class="hljs-built_in">this</span></span>)</span>&#123;<span class="hljs-keyword">return</span> _c(<span class="hljs-string">'div'</span>,&#123;<span class="hljs-attr">attrs</span>:&#123;<span class="hljs-string">"id"</span>:<span class="hljs-string">"app"</span>&#125;&#125;,[_c(<span class="hljs-string">'span'</span>,[_v(_s(message))])])&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二个<code>_c()</code>函数已经执行完毕了，现在开始执行第一个<code>_c()</code>函数了。好，我们接下来分析第一个<code>_c()</code>的执行过程，因为了第二个的铺垫，所以第一个函数的执行我们会进行的稍微快一些。首先依旧是进入到<code>_c()</code>函数的内部，然后执行如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js">vm._c = <span class="hljs-function">(<span class="hljs-params">a, b, c, d</span>) =></span> createElement(vm, a, b, c, d, <span class="hljs-literal">false</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在进入到<code>createElement</code>函数内部之前，我们先来进行参数的一一对应：</p>
<pre><code class="hljs language-js copyable" lang="js">context:vm
<span class="hljs-attr">tag</span>:<span class="hljs-string">'div'</span>
<span class="hljs-attr">data</span>:&#123;<span class="hljs-attr">attrs</span>:&#123;<span class="hljs-string">"id"</span>:<span class="hljs-string">"app"</span>&#125;&#125;
<span class="hljs-attr">children</span>: VNode &#123;<span class="hljs-attr">tag</span>: <span class="hljs-string">"span"</span>, <span class="hljs-attr">data</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-attr">children</span>: <span class="hljs-built_in">Array</span>(<span class="hljs-number">1</span>), <span class="hljs-attr">text</span>: <span class="hljs-literal">undefined</span>, ...&#125;
<span class="hljs-attr">normalizationType</span>:<span class="hljs-literal">undefined</span>
<span class="hljs-attr">alwaysNormalize</span>:<span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后走下面的代码：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(data) || isPrimitive(data)) &#123;
    normalizationType = children
    children = data
    data = <span class="hljs-literal">undefined</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实上面的代码是不会执行的，第一<code>vm</code>的<code>data</code>不是数组，然后进入到<code>isPrimitive</code>函数中。我们来看看这个函数是干什么的：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isPrimitive</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-keyword">return</span> (
      <span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'string'</span> ||
      <span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'number'</span> ||
      <span class="hljs-comment">// $flow-disable-line</span>
      <span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'symbol'</span> ||
      <span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'boolean'</span>
    )
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是判断传入的<code>data</code>是否和这几个值相等，很显然不相等，所以不会执行。</p>
<p>然后执行：</p>
<pre><code class="hljs language-js copyable" lang="js">_createElement(context, tag, data, children, normalizationType)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们依旧来看一下参数的一一对应：</p>
<pre><code class="hljs language-js copyable" lang="js">context:vm
<span class="hljs-attr">tag</span>:<span class="hljs-string">'div'</span>
<span class="hljs-attr">data</span>:&#123;<span class="hljs-attr">attrs</span>:&#123;<span class="hljs-string">"id"</span>:<span class="hljs-string">"app"</span>&#125;&#125;
<span class="hljs-attr">children</span>:VNode &#123;<span class="hljs-attr">tag</span>: <span class="hljs-string">"span"</span>, <span class="hljs-attr">data</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-attr">children</span>: <span class="hljs-built_in">Array</span>(<span class="hljs-number">1</span>), <span class="hljs-attr">text</span>: <span class="hljs-literal">undefined</span>, ...&#125;
<span class="hljs-attr">normalizationType</span>:<span class="hljs-literal">undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们进入到<code>_createElement</code>函数中去。下面这些代码都不会执行：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">if</span> (isDef(data) && isDef((data: any).__ob__)) &#123;
    process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && warn(
      <span class="hljs-string">`Avoid using observed data object as vnode data: <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(data)&#125;</span>\n`</span> +
      <span class="hljs-string">'Always create fresh vnode data objects in each render!'</span>,
      context
    )
    <span class="hljs-keyword">return</span> createEmptyVNode()
  &#125;
  <span class="hljs-comment">// object syntax in v-bind</span>
  <span class="hljs-keyword">if</span> (isDef(data) && isDef(data.is)) &#123;
    tag = data.is
  &#125;
  <span class="hljs-keyword">if</span> (!tag) &#123;
    <span class="hljs-comment">// in case of component :is set to falsy value</span>
    <span class="hljs-keyword">return</span> createEmptyVNode()
  &#125;
  <span class="hljs-comment">// warn against non-primitive key</span>
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> &&
    isDef(data) && isDef(data.key) && !isPrimitive(data.key)
  ) &#123;
    <span class="hljs-keyword">if</span> (!__WEEX__ || !(<span class="hljs-string">'@binding'</span> <span class="hljs-keyword">in</span> data.key)) &#123;
      warn(
        <span class="hljs-string">'Avoid using non-primitive value as key, '</span> +
        <span class="hljs-string">'use string/number value instead.'</span>,
        context
      )
    &#125;
  &#125;
  <span class="hljs-comment">// support single function children as default scoped slot</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(children) &&
    <span class="hljs-keyword">typeof</span> children[<span class="hljs-number">0</span>] === <span class="hljs-string">'function'</span>
  ) &#123;
    data = data || &#123;&#125;
    data.scopedSlots = &#123; <span class="hljs-attr">default</span>: children[<span class="hljs-number">0</span>] &#125;
    children.length = <span class="hljs-number">0</span>
  &#125;
  <span class="hljs-keyword">if</span> (normalizationType === ALWAYS_NORMALIZE) &#123;
    children = normalizeChildren(children)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (normalizationType === SIMPLE_NORMALIZE) &#123;
    children = simpleNormalizeChildren(children)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后开始判断<code>tag</code>的类型，然后就是一通判断，和我们创建<code>span</code>的<code>vnode</code>一样，他最后会走这段代码：</p>
<pre><code class="hljs language-js copyable" lang="js">vnode = <span class="hljs-keyword">new</span> VNode(
        config.parsePlatformTagName(tag), data, children,
        <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, context
      )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好，我们来进行参数的一一对应：</p>
<pre><code class="hljs language-js copyable" lang="js">tag:<span class="hljs-string">'div'</span>
<span class="hljs-attr">data</span>:&#123;<span class="hljs-attr">attrs</span>:&#123;<span class="hljs-string">"id"</span>:<span class="hljs-string">"app"</span>&#125;&#125;
<span class="hljs-attr">children</span>:children:VNode &#123;<span class="hljs-attr">tag</span>: <span class="hljs-string">"span"</span>, <span class="hljs-attr">data</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-attr">children</span>: <span class="hljs-built_in">Array</span>(<span class="hljs-number">1</span>), <span class="hljs-attr">text</span>: <span class="hljs-literal">undefined</span>, ...&#125;
<span class="hljs-attr">text</span>:<span class="hljs-literal">undefined</span>
<span class="hljs-attr">elm</span>:<span class="hljs-literal">undefined</span>
<span class="hljs-attr">context</span>:vm
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们就进入到<code>VNode</code>构造函数中了。执行的过程和<code>span</code>标签一样，我们这里看他最后的生成结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//div 的 vnode</span>
VNode &#123;<span class="hljs-attr">tag</span>: <span class="hljs-string">"div"</span>, <span class="hljs-attr">data</span>: &#123;…&#125;, <span class="hljs-attr">children</span>: <span class="hljs-built_in">Array</span>(<span class="hljs-number">1</span>), <span class="hljs-attr">text</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-attr">elm</span>: <span class="hljs-literal">undefined</span>, …&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>展开后：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
<span class="hljs-attr">asyncFactory</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">asyncMeta</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">children</span>: [VNode]
<span class="hljs-attr">componentInstance</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">componentOptions</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">context</span>: Vue &#123;<span class="hljs-attr">_uid</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">_isVue</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">$options</span>: &#123;…&#125;, <span class="hljs-attr">_renderProxy</span>: <span class="hljs-built_in">Proxy</span>, <span class="hljs-attr">_self</span>: Vue, …&#125;
<span class="hljs-attr">data</span>: &#123;<span class="hljs-attr">attrs</span>: &#123;…&#125;&#125;
<span class="hljs-attr">elm</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">fnContext</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">fnOptions</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">fnScopeId</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">isAsyncPlaceholder</span>: <span class="hljs-literal">false</span>
<span class="hljs-attr">isCloned</span>: <span class="hljs-literal">false</span>
<span class="hljs-attr">isComment</span>: <span class="hljs-literal">false</span>
<span class="hljs-attr">isOnce</span>: <span class="hljs-literal">false</span>
<span class="hljs-attr">isRootInsert</span>: <span class="hljs-literal">true</span>
<span class="hljs-attr">isStatic</span>: <span class="hljs-literal">false</span>
<span class="hljs-attr">key</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">ns</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">parent</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">raw</span>: <span class="hljs-literal">false</span>
<span class="hljs-attr">tag</span>: <span class="hljs-string">"div"</span>
<span class="hljs-attr">text</span>: <span class="hljs-literal">undefined</span>
<span class="hljs-attr">child</span>: (...)
<span class="hljs-attr">__proto__</span>: <span class="hljs-built_in">Object</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后回退到<code>_createElement</code>函数中去，在该函数中继续执行下面的代码：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(vnode)) &#123;
    <span class="hljs-keyword">return</span> vnode
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(vnode)) &#123;
    <span class="hljs-keyword">if</span> (isDef(ns)) applyNS(vnode, ns)
    <span class="hljs-keyword">if</span> (isDef(data)) registerDeepBindings(data)
    <span class="hljs-keyword">return</span> vnode
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> createEmptyVNode()
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这次和<code>span</code>的<code>vnode</code>有所不同，它会执行这段代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (isDef(data)) registerDeepBindings(data)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们进入到<code>registerDeepBindings</code>函数中。具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">registerDeepBindings</span> (<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (isObject(data.style)) &#123;
    traverse(data.style)
  &#125;
  <span class="hljs-keyword">if</span> (isObject(data.class)) &#123;
    traverse(data.class)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数主要是对<code>style/class</code>进行了处理，所以对<code>id</code>这个属性是忽略的。所以继续回退。一直回退到<code>Vue._render</code>函数当中，因为我们在该函数中执行了：</p>
<pre><code class="hljs language-js copyable" lang="js">vnode = render.call(vm._renderProxy, vm.$createElement)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以会一直回退到这个函数当中来。</p>
<p>好回到<code>vm._render</code>函数中来，我们继续讲解后面执行的代码，当执行完：</p>
<pre><code class="hljs language-js copyable" lang="js">vnode = render.call(vm._renderProxy, vm.$createElement)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后会执行：</p>
<pre><code class="hljs language-js copyable" lang="js">currentRenderingInstance = <span class="hljs-literal">null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后执行后续代码，其实后续的代码大部分都走不到，如：</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-comment">// if the returned array contains only a single node, allow it</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(vnode) && vnode.length === <span class="hljs-number">1</span>) &#123;
      vnode = vnode[<span class="hljs-number">0</span>]
    &#125;
    <span class="hljs-comment">// return empty vnode in case the render function errored out</span>
    <span class="hljs-keyword">if</span> (!(vnode <span class="hljs-keyword">instanceof</span> VNode)) &#123;
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && <span class="hljs-built_in">Array</span>.isArray(vnode)) &#123;
        warn(
          <span class="hljs-string">'Multiple root nodes returned from render function. Render function '</span> +
          <span class="hljs-string">'should return a single root node.'</span>,
          vm
        )
      &#125;
      vnode = createEmptyVNode()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后它会执行：</p>
<pre><code class="hljs language-js copyable" lang="js"> vnode.parent = _parentVnode;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将<code>_parentVnode</code>挂载到<code>vnode.parnet</code>。因为这个根节点的<code>vnode</code>不存在父节点，所以为<code>undefined</code>。执行完后将<code>vnode</code>返回。当返回之后就会回到一个函数当中，这个函数的代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"> updateComponent = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        vm._update(vm._render(), hydrating);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>刚在返回<code>vnode</code>这一操作是在<code>vm._render()</code>函数中执行的，这也验证了我们之前说的那句话，<code>vm._render()</code>函数是用来创建<code>vnode</code>的。接下来就是<code>vm._update</code>函数的执行了。我们来看内部的具体代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//D:\vue-src-jx\vue-dev\vue-dev\src\core\instance\lifecycle.js  </span>
Vue.prototype._update = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">vnode: VNode, hydrating?: boolean</span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm: Component = <span class="hljs-built_in">this</span><span class="hljs-comment">//这里是vm实例</span>
    <span class="hljs-keyword">const</span> prevEl = vm.$el
    <span class="hljs-keyword">const</span> prevVnode = vm._vnode<span class="hljs-comment">//undefined</span>
    <span class="hljs-keyword">const</span> restoreActiveInstance = setActiveInstance(vm)
    vm._vnode = vnode
    <span class="hljs-comment">// Vue.prototype.__patch__ is injected in entry points</span>
    <span class="hljs-comment">// based on the rendering backend used.</span>
    <span class="hljs-keyword">if</span> (!prevVnode) &#123;
      <span class="hljs-comment">// initial render 首次渲染</span>
      vm.$el = vm.__patch__(vm.$el, vnode, hydrating, <span class="hljs-literal">false</span> <span class="hljs-comment">/* removeOnly */</span>)
        <span class="hljs-comment">//首次渲染地时候vm.$el是真实地DOM节点对象 vnode是渲染后生成地虚拟DOM</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// updates 数据更新渲染</span>
      vm.$el = vm.__patch__(prevVnode, vnode)
    &#125;
    restoreActiveInstance()
    <span class="hljs-comment">// update __vue__ reference </span>
    <span class="hljs-keyword">if</span> (prevEl) &#123;
      prevEl.__vue__ = <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-keyword">if</span> (vm.$el) &#123;
      vm.$el.__vue__ = vm
    &#125;
    <span class="hljs-comment">// if parent is an HOC, update its $el as well</span>
    <span class="hljs-keyword">if</span> (vm.$vnode && vm.$parent && vm.$vnode === vm.$parent._vnode) &#123;
      vm.$parent.$el = vm.$el
    &#125;
    <span class="hljs-comment">// updated hook is called by the scheduler to ensure that children are</span>
    <span class="hljs-comment">// updated in a parent's updated hook.</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该函数的前半部分是对一些变量的赋值，因为我们是第一次渲染，所以<code>prevVnode</code>为<code>undefined</code>。所以会走这个分支：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (!prevVnode) &#123;
      <span class="hljs-comment">// initial render 首次渲染</span>
      vm.$el = vm.__patch__(vm.$el, vnode, hydrating, <span class="hljs-literal">false</span> <span class="hljs-comment">/* removeOnly */</span>)
        <span class="hljs-comment">//首次渲染地时候vm.$el是真实地DOM节点对象 vnode是渲染后生成地虚拟DOM</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个分支是针对首次渲染的实例对象。首次渲染会执行：</p>
<pre><code class="hljs language-js copyable" lang="js"> vm.__patch__(vm.$el, vnode, hydrating, <span class="hljs-literal">false</span> <span class="hljs-comment">/* removeOnly */</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来该函数内部具体的实现,，因为在本质上<code>vm.__patch__</code>的调用其实就是调用的是<code>patch</code>。所以我们来看<code>patch</code>函数的内部实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//D:\vue-src-jx\vue-dev\vue-dev\src\core\vdom\patch.js</span>
<span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span> (<span class="hljs-params">oldVnode, vnode, hydrating, removeOnly</span>) </span>&#123;
   
    <span class="hljs-keyword">if</span> (isUndef(vnode)) &#123;<span class="hljs-comment">//删除逻辑</span>
      <span class="hljs-keyword">if</span> (isDef(oldVnode)) invokeDestroyHook(oldVnode)
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">let</span> isInitialPatch = <span class="hljs-literal">false</span>
    <span class="hljs-keyword">const</span> insertedVnodeQueue = []
    <span class="hljs-keyword">if</span> (isUndef(oldVnode)) &#123;
      <span class="hljs-comment">// empty mount (likely as component), create new root element</span>
      isInitialPatch = <span class="hljs-literal">true</span>
      createElm(vnode, insertedVnodeQueue)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">const</span> isRealElement = isDef(oldVnode.nodeType)<span class="hljs-comment">//isRealElement: true</span>
      <span class="hljs-keyword">if</span> (!isRealElement && sameVnode(oldVnode, vnode)) &#123;
        <span class="hljs-comment">// patch existing root node</span>
        patchVnode(oldVnode, vnode, insertedVnodeQueue, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, removeOnly)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">if</span> (isRealElement) &#123;
          <span class="hljs-comment">// mounting to a real element</span>
          <span class="hljs-comment">// check if this is server-rendered content and if we can perform</span>
          <span class="hljs-comment">// a successful hydration.</span>
          <span class="hljs-keyword">if</span> (oldVnode.nodeType === <span class="hljs-number">1</span> && oldVnode.hasAttribute(SSR_ATTR)) &#123;<span class="hljs-comment">//不是服务端渲染，所以走不到该逻辑</span>
            oldVnode.removeAttribute(SSR_ATTR)
            hydrating = <span class="hljs-literal">true</span>
          &#125;
          <span class="hljs-keyword">if</span> (isTrue(hydrating)) &#123;<span class="hljs-comment">//false</span>
            <span class="hljs-keyword">if</span> (hydrate(oldVnode, vnode, insertedVnodeQueue)) &#123;
              invokeInsertHook(vnode, insertedVnodeQueue, <span class="hljs-literal">true</span>)
              <span class="hljs-keyword">return</span> oldVnode
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
              warn(
                <span class="hljs-string">'The client-side rendered virtual DOM tree is not matching '</span> +
                <span class="hljs-string">'server-rendered content. This is likely caused by incorrect '</span> +
                <span class="hljs-string">'HTML markup, for example nesting block-level elements inside '</span> +
                <span class="hljs-string">'<p>, or missing <tbody>. Bailing hydration and performing '</span> +
                <span class="hljs-string">'full client-side render.'</span>
              )
            &#125;
          &#125;
          <span class="hljs-comment">// either not server-rendered, or hydration failed.</span>
          <span class="hljs-comment">// create an empty node and replace it</span>
          <span class="hljs-comment">//该代码的意思是将我们的真实的DOM转化为VDOM.</span>
          oldVnode = emptyNodeAt(oldVnode)
        &#125;

        <span class="hljs-comment">// replacing existing element</span>
        <span class="hljs-keyword">const</span> oldElm = oldVnode.elm <span class="hljs-comment">//这个是真实地dom，虽然我们把真实地dom转为了虚拟dom，但是还是保留了原来地dom</span>
      
        <span class="hljs-keyword">const</span> parentElm = nodeOps.parentNode(oldElm)<span class="hljs-comment">//这是真实地父节点。</span>

        <span class="hljs-comment">// create new node</span>
        createElm(
          vnode,
          insertedVnodeQueue,
          <span class="hljs-comment">// extremely rare edge case: do not insert if old element is in a</span>
          <span class="hljs-comment">// leaving transition. Only happens when combining transition +</span>
          <span class="hljs-comment">// keep-alive + HOCs. (#4590)</span>
          oldElm._leaveCb ? <span class="hljs-literal">null</span> : parentElm,
          nodeOps.nextSibling(oldElm)
        )

        <span class="hljs-comment">// update parent placeholder node element, recursively</span>
        <span class="hljs-keyword">if</span> (isDef(vnode.parent)) &#123;
          <span class="hljs-keyword">let</span> ancestor = vnode.parent
          <span class="hljs-keyword">const</span> patchable = isPatchable(vnode)
          <span class="hljs-keyword">while</span> (ancestor) &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.destroy.length; ++i) &#123;
              cbs.destroy[i](ancestor)
            &#125;
            ancestor.elm = vnode.elm
            <span class="hljs-keyword">if</span> (patchable) &#123;
              <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < cbs.create.length; ++i) &#123;
                cbs.create[i](emptyNode, ancestor)
              &#125;
              <span class="hljs-comment">// #6513</span>
              <span class="hljs-comment">// invoke insert hooks that may have been merged by create hooks.</span>
              <span class="hljs-comment">// e.g. for directives that uses the "inserted" hook.</span>
              <span class="hljs-keyword">const</span> insert = ancestor.data.hook.insert
              <span class="hljs-keyword">if</span> (insert.merged) &#123;
                <span class="hljs-comment">// start at index 1 to avoid re-invoking component mounted hook</span>
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < insert.fns.length; i++) &#123;
                  insert.fns[i]()
                &#125;
              &#125;
            &#125; <span class="hljs-keyword">else</span> &#123;
              registerRef(ancestor)
            &#125;
            ancestor = ancestor.parent
          &#125;
        &#125;

        <span class="hljs-comment">// destroy old node</span>
        <span class="hljs-keyword">if</span> (isDef(parentElm)) &#123;
          removeVnodes([oldVnode], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isDef(oldVnode.tag)) &#123;
          invokeDestroyHook(oldVnode)
        &#125;
      &#125;
    &#125;

    invokeInsertHook(vnode, insertedVnodeQueue, isInitialPatch)
    <span class="hljs-keyword">return</span> vnode.elm
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在解析函数代码之前，我们来对参数进行简单的讲解。<code>vm.$el</code>是根组件的根元素节点，也就是<code>div</code>。它是一个真实的节点，并不是一个<code>vnode</code>。第二个参数就是根组件的<code>vnode</code>。接下来我们进入函数内部，来看看它的具体执行。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">if</span> (isUndef(vnode)) &#123;<span class="hljs-comment">//删除逻辑</span>
      <span class="hljs-keyword">if</span> (isDef(oldVnode)) invokeDestroyHook(oldVnode)
      <span class="hljs-keyword">return</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先判断<code>vnode</code>是否存在，如果不存在<code>Vue</code>就判定你想要删除这个节点，所以这个分支我们走不到。然后向下执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (isUndef(oldVnode)) &#123;
    ......
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码是走不到的，因为<code>vm</code>实例的<code>oldVnode</code>是存在的。然后继续向下执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> isRealElement = isDef(oldVnode.nodeType);
        <span class="hljs-keyword">if</span> (!isRealElement && sameVnode(oldVnode, vnode)) &#123;
          <span class="hljs-comment">// patch existing root node</span>
          patchVnode(oldVnode, vnode, insertedVnodeQueue, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, removeOnly);
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为<code>oldVnode</code>是真实的节点，所以<code>isRealElement</code>为真，所以直接走<code>else</code>分支：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">if</span> (isRealElement) &#123;
          <span class="hljs-comment">// mounting to a real element</span>
          <span class="hljs-comment">// check if this is server-rendered content and if we can perform</span>
          <span class="hljs-comment">// a successful hydration.</span>
          <span class="hljs-keyword">if</span> (oldVnode.nodeType === <span class="hljs-number">1</span> && oldVnode.hasAttribute(SSR_ATTR)) &#123;<span class="hljs-comment">//不是服务端渲染，所以走不到该逻辑</span>
            oldVnode.removeAttribute(SSR_ATTR)
            hydrating = <span class="hljs-literal">true</span>
          &#125;
          <span class="hljs-keyword">if</span> (isTrue(hydrating)) &#123;<span class="hljs-comment">//false</span>
            <span class="hljs-keyword">if</span> (hydrate(oldVnode, vnode, insertedVnodeQueue)) &#123;
              invokeInsertHook(vnode, insertedVnodeQueue, <span class="hljs-literal">true</span>)
              <span class="hljs-keyword">return</span> oldVnode
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
              warn(
                <span class="hljs-string">'The client-side rendered virtual DOM tree is not matching '</span> +
                <span class="hljs-string">'server-rendered content. This is likely caused by incorrect '</span> +
                <span class="hljs-string">'HTML markup, for example nesting block-level elements inside '</span> +
                <span class="hljs-string">'<p>, or missing <tbody>. Bailing hydration and performing '</span> +
                <span class="hljs-string">'full client-side render.'</span>
              )
            &#125;
          &#125;
          <span class="hljs-comment">// either not server-rendered, or hydration failed.</span>
          <span class="hljs-comment">// create an empty node and replace it</span>
          <span class="hljs-comment">//该代码的意思是将我们的真实的DOM转化为VDOM.</span>
          oldVnode = emptyNodeAt(oldVnode)
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码是<code>else</code>分支的前半段，<code>Vue</code>首先判断<code>isRealElement</code>。很明显为真，所以就向下执行，下面的这些代码都不会执行：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">if</span> (oldVnode.nodeType === <span class="hljs-number">1</span> && oldVnode.hasAttribute(SSR_ATTR)) &#123;<span class="hljs-comment">//不是服务端渲染，所以走不到该逻辑</span>
            oldVnode.removeAttribute(SSR_ATTR)
            hydrating = <span class="hljs-literal">true</span>
          &#125;
          <span class="hljs-keyword">if</span> (isTrue(hydrating)) &#123;<span class="hljs-comment">//false</span>
            <span class="hljs-keyword">if</span> (hydrate(oldVnode, vnode, insertedVnodeQueue)) &#123;
              invokeInsertHook(vnode, insertedVnodeQueue, <span class="hljs-literal">true</span>)
              <span class="hljs-keyword">return</span> oldVnode
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
              warn(
                <span class="hljs-string">'The client-side rendered virtual DOM tree is not matching '</span> +
                <span class="hljs-string">'server-rendered content. This is likely caused by incorrect '</span> +
                <span class="hljs-string">'HTML markup, for example nesting block-level elements inside '</span> +
                <span class="hljs-string">'<p>, or missing <tbody>. Bailing hydration and performing '</span> +
                <span class="hljs-string">'full client-side render.'</span>
              )
            &#125;
          &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就执行这段代码：</p>
<pre><code class="hljs language-js copyable" lang="js">  oldVnode = emptyNodeAt(oldVnode)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么此时你可能会有疑惑，<code>if(isRealElement)</code>到底是用来干什么的？其实这就要涉及到<code>patch</code>的渲染原理了。我们可以想一下，<code>patch</code>在什么情况下会执行。答案有两个：第一，当进行组件的首次渲染。第二，当数据更新是触发的再次渲染。也就是说有两次。在进行<code>patch</code>渲染的时候<code>Vue</code>一定会做一件事，那就是新旧<code>vdom</code>的比对。也就是说会将新的和旧的进行对比，然后找出渲染的最优解。但是组件在首次渲染的时候是没有旧<code>vnode</code>。既然没有，那么就创建一个，因为首次渲染新旧<code>dom</code>是一样的，为了使函数运行兼容，所以就会创建一个旧<code>vnode</code>出来，然后进行<code>patch</code>对比。</p>
<p>我们讲完了旧节点的创建原因，接下来继续向下执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> oldElm = oldVnode.elm <span class="hljs-comment">//这个是真实地dom，虽然我们把真实地dom转为了虚拟dom，但是还是保留了原来的dom</span>
<span class="hljs-keyword">const</span> parentElm = nodeOps.parentNode(oldElm)<span class="hljs-comment">//这是真实地父节点。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面的代码执行就很关键了。因为组件将要进入到另一个阶段：<code>生成真实节点挂载阶段</code>。</p>
<h3 data-id="heading-4">生成真实节点挂载阶段</h3>
<p>在生成真实节点并挂载的阶段，<code>Vue</code>主要执行的是<code>createElm</code>函数。具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElm</span> (<span class="hljs-params">
    vnode,
    insertedVnodeQueue,
    parentElm,
    refElm,
    nested,
    ownerArray,
    index
  </span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isDef(vnode.elm) && isDef(ownerArray)) &#123;
      <span class="hljs-comment">// This vnode was used in a previous render!</span>
      <span class="hljs-comment">// now it's used as a new node, overwriting its elm would cause</span>
      <span class="hljs-comment">// potential patch errors down the road when it's used as an insertion</span>
      <span class="hljs-comment">// reference node. Instead, we clone the node on-demand before creating</span>
      <span class="hljs-comment">// associated DOM element for it.</span>
      vnode = ownerArray[index] = cloneVNode(vnode)
    &#125;

    vnode.isRootInsert = !nested <span class="hljs-comment">// for transition enter check</span>
    <span class="hljs-keyword">if</span> (createComponent(vnode, insertedVnodeQueue, parentElm, refElm)) &#123;
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">const</span> data = vnode.data
    <span class="hljs-keyword">const</span> children = vnode.children
    <span class="hljs-keyword">const</span> tag = vnode.tag
    <span class="hljs-keyword">if</span> (isDef(tag)) &#123; 
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
        <span class="hljs-keyword">if</span> (data && data.pre) &#123;
          creatingElmInVPre++
        &#125;
        <span class="hljs-keyword">if</span> (isUnknownElement(vnode, creatingElmInVPre)) &#123;
          warn(
            <span class="hljs-string">'Unknown custom element: <'</span> + tag + <span class="hljs-string">'> - did you '</span> +
            <span class="hljs-string">'register the component correctly? For recursive components, '</span> +
            <span class="hljs-string">'make sure to provide the "name" option.'</span>,
            vnode.context
          )
        &#125;
      &#125;

      <span class="hljs-comment">//nodeOps是一个原生DOM API的一个封装对象，nodeOps.createElement(tag)其实就是document.createElement(tag)。</span>
      <span class="hljs-comment">//vnode.elm此时就是通过nodeOps.createElement()函数创建的真实节点对象。</span>
      vnode.elm = vnode.ns
        ? nodeOps.createElementNS(vnode.ns, tag)
        : nodeOps.createElement(tag, vnode)
      setScope(vnode)

      <span class="hljs-comment">/* istanbul ignore if */</span>
      <span class="hljs-keyword">if</span> (__WEEX__) &#123;
        <span class="hljs-comment">//WEEX端的渲染</span>
        <span class="hljs-comment">// in Weex, the default insertion order is parent-first.</span>
        <span class="hljs-comment">// List items can be optimized to use children-first insertion</span>
        <span class="hljs-comment">// with append="tree".</span>
        <span class="hljs-keyword">const</span> appendAsTree = isDef(data) && isTrue(data.appendAsTree)
        <span class="hljs-keyword">if</span> (!appendAsTree) &#123;
          <span class="hljs-keyword">if</span> (isDef(data)) &#123;
            invokeCreateHooks(vnode, insertedVnodeQueue)
          &#125;
          insert(parentElm, vnode.elm, refElm)
        &#125;
        createChildren(vnode, children, insertedVnodeQueue)
        <span class="hljs-keyword">if</span> (appendAsTree) &#123;
          <span class="hljs-keyword">if</span> (isDef(data)) &#123;
            invokeCreateHooks(vnode, insertedVnodeQueue)
          &#125;
          insert(parentElm, vnode.elm, refElm)
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">//</span>
        createChildren(vnode, children, insertedVnodeQueue)
        <span class="hljs-keyword">if</span> (isDef(data)) &#123;
          invokeCreateHooks(vnode, insertedVnodeQueue)
        &#125;
        insert(parentElm, vnode.elm, refElm)
      &#125;

      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && data && data.pre) &#123;
        creatingElmInVPre--
      &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isTrue(vnode.isComment)) &#123;
      vnode.elm = nodeOps.createComment(vnode.text)
      insert(parentElm, vnode.elm, refElm)
    &#125; <span class="hljs-keyword">else</span> &#123;
      vnode.elm = nodeOps.createTextNode(vnode.text)
      insert(parentElm, vnode.elm, refElm)
    &#125;
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数主要是通过<code>vnode</code>来创建一个对应的真实节点。而创建一个真实节点主要经历了四个部分：</p>
<p>第一部分：判断该节点是否是组件节点</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">if</span> (createComponent(vnode, insertedVnodeQueue, parentElm, refElm)) &#123;
      <span class="hljs-keyword">return</span>
    &#125;   
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二部分：创建<code>vnode</code>对应真实节点</p>
<pre><code class="hljs language-js copyable" lang="js">vnode.elm = vnode.ns
        ? nodeOps.createElementNS(vnode.ns, tag)
        : nodeOps.createElement(tag, vnode)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三部分：创建真实子节点</p>
<pre><code class="hljs language-js copyable" lang="js">createChildren(vnode, children, insertedVnodeQueue)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>createChildren</code>函数中又会执行<code>createElm</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"> createElm(children[i], insertedVnodeQueue, vnode.elm, <span class="hljs-literal">null</span>, <span class="hljs-literal">true</span>, children, i)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>当调用createElm函数的时候，会把当前节点的vnode.elm作为父节点传入到createElm函数中，当创建子节点的时候，该子节点的parentElm就是我们传入的vnode.elm元素</strong>。</p>
<p>第四部分：将该真实节点插入到父节点中。</p>
<pre><code class="hljs language-js copyable" lang="js">insert(parentElm, vnode.elm, refElm)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们对每一个部分都进行详细的解释，然后再整体进行分析一波。第一部分是通过调用<code>createComponent</code>函数来判断我们传入的<code>vnode</code>是不是一个组件<code>vnode</code>。如果是一个组件<code>vnode</code>。那么就回去创建一个组件实例，然后执行对应的组件创建代码。很显然，在这里并不是一个组件<code>vnode</code>。第二部分是创建我们当前<code>vnode</code>所对应的节点，当创建完成后就挂载到当前节点的<code>vnode.elm</code>上。这个挂载是很有用的，后面<code>insert</code>的时候就体现出来了。也就是说在第二部的时候，我们的<code>vnode</code>所对应的节点就已经被创建出来了。而第三步开始创建子节点，其实子节点是是一个独立的节点，它也有自己的<code>vnode</code>。所以在<code>createChildren</code>函数中还是调用了<code>createElm</code>函数。第四步是进行插入操作，将我们创建好的当前节点插入到对一个的父节点当中。在插入操作的时候我们必须清楚两个基本点，那么就是我们打算插谁，把它插在哪里。首先我们来解决第一个基本点，那就是插谁，很简单插当前<code>vnode</code>所创建的真实节点。第二个基本点，插在哪里，插在父节点中，那么我们怎么获取到父节点呢？其实很简单。我举个例子，我们有一个模板：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们想获取到这两个节点，那么就需要调用两次<code>createElm</code>函数，第一次调用时创建父节点<code>div</code>。第二次调用时创建子节点<code>span</code>。当父节点创建完之后，我们开始创建子节点了，那么当子节点也创建完之后我们如何将子节点插入到父节点<code>div</code>当中呢，<code>Vue</code>的做法就是在第二个节点创建之前，向<code>createElm</code>函数出入第三个参数，这个参数就是父节点的<code>vnode.elm</code>即刚创建的<code>div</code>元素节点。将这个节点作为子节点的父节点传入，当子节点创建完成后就进行插入操作，因为<code>div</code>节点没有父元素，所以在第一次调用<code>createElm</code>函数的时候就没有传入第三个参数，所以默认为<code>undefined</code>。</p>
<p>好了，上面的四个部分都讲完了，我们现在了重新梳理一遍，我们就以上面的模板为实例。那么生成的<code>vnode</code>如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//简易版本</span>
&#123;
    <span class="hljs-attr">tag</span>:<span class="hljs-string">'div'</span>,
    <span class="hljs-attr">data</span>:<span class="hljs-literal">undefined</span>,
    <span class="hljs-attr">children</span>:[&#123;
        <span class="hljs-attr">tag</span>:<span class="hljs-string">'span'</span>,
        <span class="hljs-attr">data</span>:<span class="hljs-literal">undefined</span>,
        <span class="hljs-attr">children</span>:<span class="hljs-literal">undefined</span>,
        ......
    &#125;],
   ......
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通过上面的那个模板将我们上面的四步走一遍。</p>
<p>首先是<code>if</code>判断，因为我们提供的是一个正常的元素节点，所以不会去创建一个组件实例，然后通过<code>nodeOps.createElement(tag, vnode)</code>代码，创建了一个真实的<code>div</code>元素节点，并把这个节点挂载到了这个<code>div</code>的<code>vnode.elm</code>上，好了我们第一个<code>div</code>元素创建完成。接着就开始执行<code>createChildren(vnode, children, insertedVnodeQueue)</code>。当执行该函数的时候，其实就是循环执行<code>createElm</code>这个函数。</p>
<p>好我们第二次进入这个函数当中。在第二次调用的时候，也就是生成<code>span</code>节点的时候，我们把父元素的<code>vnode.elm</code>作为第三个参数传入到了<code>createElm</code>函数中，目的是当<code>span</code>节点创建完成好以这个节点为父节点来进行插入操作。</p>
<p>首先还是<code>if</code>判断，依然不成立，然后执行：</p>
<pre><code class="hljs language-js copyable" lang="js">vnode.elm = vnode.ns
        ? nodeOps.createElementNS(vnode.ns, tag)
        : nodeOps.createElement(tag, vnode)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时的<code>tag</code>已经是<code>span</code>。所以创建的是<code>span</code>的真实节点。然后将创建的<code>span</code>节点挂载到<code>span</code>的<code>vnode</code>的<code>elm</code>属性上，然后就看是执行<code>createChildren</code>。因为我们的<code>span</code>节点是没有子节点的，所以执行<code>insert</code>操作。因为我们已经将<code>div</code>的<code>vnode.elm</code>作为<code>parentElm</code>传入，所以新创建的<code>span</code>节点就会插入到<code>div</code>节点当中。好了，插入完之后进行回退，回退到<code>createChildren</code>函数当中，因为没有其他子节点了，所以会继续回退。然后回退到第一次调用<code>createElm</code>函数中，然后进行<code>div</code>元素的<code>insert</code>操作，而<code>parentElm</code>就是<code>div</code>元素所对应的父元素节点。</p>
<p>好了，对于节点的生成和挂载的框架我们已经搭建好了，接下来我们回到我们最初的实例当中，来一一走一遍<code>createElm</code>函数。</p>
<p>我们先来回顾一下我们的实例是什么样子的，模板如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染函数如下：</p>
<pre><code class="hljs language-js copyable" lang="js">_c(<span class="hljs-string">'div'</span>,&#123;<span class="hljs-attr">attrs</span>:&#123;<span class="hljs-string">"id"</span>:<span class="hljs-string">"app"</span>&#125;&#125;,[_c(<span class="hljs-string">'span'</span>,[_v(_s(message))])])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在知道了我们的模板和渲染函数了，那么我们就来走一下<code>createElm</code>函数。</p>
<p>首先依旧实判断是否该节点是一个组件节点，很显然不是组件节点。然后就定义一些变量并赋值，用于条件的判断，然后判断我们的<code>tag</code>是否存在，很显然是存在的，然后调用：</p>
<pre><code class="hljs language-js copyable" lang="js">vnode.elm = vnode.ns
        ? nodeOps.createElementNS(vnode.ns, tag)
        : nodeOps.createElement(tag, vnode)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们的第一个元素节点<code>div</code>就这样诞生了，然后将其赋值给<code>div</code>所对应的<code>vnode</code>的<code>elm</code>属性，然后执行：</p>
<pre><code class="hljs language-js copyable" lang="js">createChildren(vnode, children, insertedVnodeQueue)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>createChildren</code>函数中会循环创建子节点：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < children.length; ++i) &#123;
        <span class="hljs-comment">//这个就是深度遍历并创建节点。</span>
        createElm(children[i], insertedVnodeQueue, vnode.elm, <span class="hljs-literal">null</span>, <span class="hljs-literal">true</span>, children, i)
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在执行<code>createElm</code>函数去创建<code>span</code>节点的时候，把<code>div</code>真实节点作为<code>parentElm</code>传给该参数。同样的，这个函数执行的时候首先就会去创建<code>span</code>节点，然后调用<code>createChildern</code>函数，在调用这个函数的时候依旧会执行<code>createElm</code>函数去创建文本节点，此时我们会把<code>span</code>节点作为<code>parentElm</code>传入到<code>createElm</code>函数中，在<code>createElm</code>函数中，首先会创建文本节点，因为文本节点没有子节点，所以执行<code>insert</code>操作，因为此时的<code>parentElm</code>是<code>span</code>节点，所以就把文本插入到该节点当中，然后进行回退，回退到<code>createChildren</code>函数中，因为<code>span</code>节点没有其他的子节点，所以执行<code>insert</code>操作，因为此时<code>span</code>的父节点是我们传入的<code>div</code>节点，所以就把该节点插入到<code>div</code>节点当中。然后回退到<code>div</code>的<code>createChildren</code>函数当中，因为<code>div</code>节点没有其他子节点，所以执行<code>insert</code>操作，此时<code>div</code>的<code>parentElm</code>是<code>body</code>节点，所以将该节点插入到<code>body</code>当中，一旦插入到<code>body</code>。此时就说明我们更改了文档的<code>DOM</code>结构，会引发浏览器的重新渲染。到此，我们的生成真实节点挂载阶段就结束了，我们会发现：<strong>创建节点是由父到子，挂载节点是由子到父</strong>。
节点的创建和挂载是完成了，但是这还是有一个问题的，此时调试代码的时候你会发现页面的元素里有两个:</p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>123<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说<code>Vue</code>完成了挂载，但是它并没有将页面的原有节点删除，所以此时<code>Vue</code>要做的事情就是将页面上原有的节点删除，所以会调用：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">if</span> (isDef(parentElm)) &#123;
          removeVnodes([oldVnode], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>removeVnodes</code>函数会将原有的节点删除。当执行完该函数后会执行：</p>
<pre><code class="hljs language-js copyable" lang="js">   invokeInsertHook(vnode, insertedVnodeQueue, isInitialPatch)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该函数的具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">invokeInsertHook</span> (<span class="hljs-params">vnode, queue, initial</span>) </span>&#123;
    <span class="hljs-comment">// delay insert hooks for component root nodes, invoke them after the</span>
    <span class="hljs-comment">// element is really inserted</span>
    <span class="hljs-keyword">if</span> (isTrue(initial) && isDef(vnode.parent)) &#123;
      vnode.parent.data.pendingInsert = queue
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < queue.length; ++i) &#123;
        queue[i].data.hook.insert(queue[i])
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为我们这测试的案例并不会触发这个函数，到后面我们讲解嵌套组件的时候会具体讲解。</p>
<p>然后回退到<code>patch</code>函数中，然后执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">return</span> vnode.elm
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行完之后就会回退到<code>Vue._update()</code>函数当中去，后面的代码就是进行一些列的挂载，挂载完之后进行回退，一直回退到<code>watcher.get()</code>函数当中，因为我们是在这个函数中调用的<code>updateComponent</code>函数的。然后执行<code>watcher.get</code>中的代码，首先是判断<code>this.deep</code>。这个在一开始的时候是<code>false</code>。然后调用<code>popTarget</code>表示我们当前的组件已经完成了，然后将该组件的<code>watcher</code>出栈，一旦有属性在被访问，那么就是下一个<code>watcher</code>干的事情了。然后执行<code>watcher.cleanupDeps()</code>。为什么执行这个函数，我们会面再讲。此处先省略。接着就会继续回退，一直回退到<code>mountComponent</code>函数当中，然后执行：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">if</span> (vm.$vnode == <span class="hljs-literal">null</span>) &#123;
      vm._isMounted = <span class="hljs-literal">true</span>;
      callHook(vm, <span class="hljs-string">'mounted'</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为此时的<code>vm.$vnode</code>还不存在，所以就会执行<code>mounted</code>钩子函数，在执行之前将该组件实例标记为<code>已挂载</code>状态。当把上面的代码执行完之后，就算是真正的执行完毕，接着就会一直回退到<code><script></code>标签当中的代码。</p>
<p>至此，我们的这一个简单的小案例就已经讲完了，你是到君是否能明白。</p>
<p>我们前面讲到了我们为什么要执行<code>cleanDeps</code>，该函数的具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">  cleanupDeps () &#123;
    <span class="hljs-keyword">let</span> i = <span class="hljs-built_in">this</span>.deps.length<span class="hljs-comment">//获取watcher中存储的deps个数</span>
    <span class="hljs-keyword">while</span> (i--) &#123;
      <span class="hljs-keyword">const</span> dep = <span class="hljs-built_in">this</span>.deps[i]<span class="hljs-comment">//获取到对应的deps</span>
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.newDepIds.has(dep.id)) &#123;<span class="hljs-comment">//判断新deps中是否存在旧的deps。因为在触发重新渲染的时候会有一份新的deps。所以将新的和旧的进行比较</span>
        dep.removeSub(<span class="hljs-built_in">this</span>)<span class="hljs-comment">//如果新的deps中有同样的dep，说明该组件还在依赖这个deps，所以保留，如果没有，那么说明该组件已经不依赖这个deps了，所以两个解除互相绑定的关系，即删除，那么此时的this.deps中存的就是新deps用的到的dep，deps中的dep新的deps都有，但是，新的deps中的dep，deps就不一定有了。</span>
      &#125;
    &#125;
    <span class="hljs-keyword">let</span> tmp = <span class="hljs-built_in">this</span>.depIds
    <span class="hljs-built_in">this</span>.depIds = <span class="hljs-built_in">this</span>.newDepIds
    <span class="hljs-built_in">this</span>.newDepIds = tmp
    <span class="hljs-built_in">this</span>.newDepIds.clear()
      <span class="hljs-comment">//看下面的部分就可以了</span>
    tmp = <span class="hljs-built_in">this</span>.deps
    <span class="hljs-built_in">this</span>.deps = <span class="hljs-built_in">this</span>.newDeps
    <span class="hljs-built_in">this</span>.newDeps = tmp
    <span class="hljs-built_in">this</span>.newDeps.length = <span class="hljs-number">0</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么要删除旧的<code>deps</code>呢？因为当我们更新数据的时候会引发<code>vue</code>重新渲染<code>vdom</code>。而再渲染的过程中会再一次的访问属性，而访问属性的过程中会再一次的触发属性的<code>get</code>函数，进而又一次的收集依赖，但是我们以前有了旧依赖怎么办，那么我们就必须删除旧依赖然后保存新依赖。然后把新依赖放入到旧依赖中，等待下一次的更新。</p>
<p>在实例一中，因为我们没有进行数据的更新，所以执行该操作基本没有什么影响。</p></div>  
</div>
            