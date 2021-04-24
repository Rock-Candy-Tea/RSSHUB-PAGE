
---
title: '手写Vue2.0源码（八）-组件原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/396c604a21a3466c86f43ceb3ccf1b1f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Apr 2021 18:26:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/396c604a21a3466c86f43ceb3ccf1b1f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>此篇主要手写 Vue2.0 源码-<strong>组件原理</strong></p>
<p>上一篇咱们主要介绍了 Vue <a href="https://juejin.cn/post/6953433215218483236" target="_blank">diff 算法原理</a> 是对渲染更新的优化 大家都知道 Vue 的一大特色就是组件化 此篇主要介绍整个组件创建和渲染流程 其中 Vue.extend 这一 api 是创建组件的核心</p>
<p><strong>适用人群：</strong></p>
<p>1.想要深入理解 vue 源码更好的进行日常业务开发</p>
<p>2.想要在简历写上精通 vue 框架源码（再也不怕面试官的连环夺命问 哈哈）</p>
<p>3.没时间去看官方源码或者初看源码觉得难以理解的同学</p>
<hr>
<h3 data-id="heading-1">正文</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 全局组件</span>
  Vue.component(<span class="hljs-string">"parent-component"</span>, &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>我是全局组件</div>`</span>,
  &#125;);
  <span class="hljs-comment">// Vue实例化</span>
  <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">aa</span>: <span class="hljs-number">1</span>,
      &#125;;
    &#125;,
    <span class="hljs-comment">// render(h) &#123;</span>
    <span class="hljs-comment">//   return h('div',&#123;id:'a'&#125;,'hello')</span>
    <span class="hljs-comment">// &#125;,</span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div id="a">
      hello 这是我自己写的Vue&#123;&#123;aa&#125;&#125;
      <parent-component><parent-component>
      <child-component></child-component>
      </div>`</span>,
    <span class="hljs-comment">// 局部组件</span>
    <span class="hljs-attr">components</span>: &#123;
      <span class="hljs-string">"child-component"</span>: &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>我是局部组件</div>`</span>,
      &#125;,
    &#125;,
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面演示了最基础的全局组件和局部组件的用法 其实我们每一个组件都是一个继承自 Vue 的子类 能够使用 Vue 的原型方法</p>
<h4 data-id="heading-2">1.全局组件注册</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/global-api/index.js</span>

<span class="hljs-keyword">import</span> initExtend <span class="hljs-keyword">from</span> <span class="hljs-string">"./initExtend"</span>;
<span class="hljs-keyword">import</span> initAssetRegisters <span class="hljs-keyword">from</span> <span class="hljs-string">"./assets"</span>;
<span class="hljs-keyword">const</span> ASSETS_TYPE = [<span class="hljs-string">"component"</span>, <span class="hljs-string">"directive"</span>, <span class="hljs-string">"filter"</span>];
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initGlobalApi</span>(<span class="hljs-params">Vue</span>) </span>&#123;
  Vue.options = &#123;&#125;; <span class="hljs-comment">// 全局的组件 指令 过滤器</span>
  ASSETS_TYPE.forEach(<span class="hljs-function">(<span class="hljs-params">type</span>) =></span> &#123;
    Vue.options[type + <span class="hljs-string">"s"</span>] = &#123;&#125;;
  &#125;);
  Vue.options._base = Vue; <span class="hljs-comment">//_base指向Vue</span>

  initExtend(Vue); <span class="hljs-comment">// extend方法定义</span>
  initAssetRegisters(Vue); <span class="hljs-comment">//assets注册方法 包含组件 指令和过滤器</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>initGlobalApi方法主要用来注册Vue的全局方法 比如之前写的Vue.Mixin 和今天的Vue.extend Vue.component等</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/global-api/asset.js</span>

<span class="hljs-keyword">const</span> ASSETS_TYPE = [<span class="hljs-string">"component"</span>, <span class="hljs-string">"directive"</span>, <span class="hljs-string">"filter"</span>];
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initAssetRegisters</span>(<span class="hljs-params">Vue</span>) </span>&#123;
  ASSETS_TYPE.forEach(<span class="hljs-function">(<span class="hljs-params">type</span>) =></span> &#123;
    Vue[type] = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">id, definition</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (type === <span class="hljs-string">"component"</span>) &#123;
        <span class="hljs-comment">//   this指向Vue</span>
        <span class="hljs-comment">// 全局组件注册</span>
        <span class="hljs-comment">// 子组件可能也有extend方法  VueComponent.component方法</span>
        definition = <span class="hljs-built_in">this</span>.options._base.extend(definition);
      &#125;
      <span class="hljs-built_in">this</span>.options[type + <span class="hljs-string">"s"</span>][id] = definition;
    &#125;;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>this.options._base 就是指代 Vue 可见所谓的全局组件就是使用 Vue.extend 方法把传入的选项处理之后挂载到了 Vue.options.components 上面</p>
<h4 data-id="heading-3">2.Vue.extend 定义</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//  src/global-api/initExtend.js</span>

<span class="hljs-keyword">import</span> &#123; mergeOptions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../util/index"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initExtend</span>(<span class="hljs-params">Vue</span>) </span>&#123;
  <span class="hljs-keyword">let</span> cid = <span class="hljs-number">0</span>; <span class="hljs-comment">//组件的唯一标识</span>
  <span class="hljs-comment">// 创建子类继承Vue父类 便于属性扩展</span>
  Vue.extend = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">extendOptions</span>) </span>&#123;
    <span class="hljs-comment">// 创建子类的构造函数 并且调用初始化方法</span>
    <span class="hljs-keyword">const</span> Sub = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">VueComponent</span>(<span class="hljs-params">options</span>) </span>&#123;
      <span class="hljs-built_in">this</span>._init(options); <span class="hljs-comment">//调用Vue初始化方法</span>
    &#125;;
    Sub.cid = cid++;
    Sub.prototype = <span class="hljs-built_in">Object</span>.create(<span class="hljs-built_in">this</span>.prototype); <span class="hljs-comment">// 子类原型指向父类</span>
    Sub.prototype.constructor = Sub; <span class="hljs-comment">//constructor指向自己</span>
    Sub.options = mergeOptions(<span class="hljs-built_in">this</span>.options, extendOptions); <span class="hljs-comment">//合并自己的options和父类的options</span>
    <span class="hljs-keyword">return</span> Sub;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue.extend 核心思路就是使用原型继承的方法返回了 Vue 的子类 并且利用 mergeOptions 把传入组件的 options 和父类的 options 进行了合并</p>
<h4 data-id="heading-4">3.组件的合并策略</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/init.js</span>

Vue.prototype._init = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>;
  vm.$options = mergeOptions(vm.constructor.options, options); <span class="hljs-comment">//合并options</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还记得我们 Vue 初始化的时候合并 options 吗 全局组件挂载在 Vue.options.components 上 局部组件也定义在自己的 options.components 上面 那我们怎么处理全局组件和局部组件的合并呢</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/util/index.js</span>

<span class="hljs-keyword">const</span> ASSETS_TYPE = [<span class="hljs-string">"component"</span>, <span class="hljs-string">"directive"</span>, <span class="hljs-string">"filter"</span>];
<span class="hljs-comment">// 组件 指令 过滤器的合并策略</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeAssets</span>(<span class="hljs-params">parentVal, childVal</span>) </span>&#123;
  <span class="hljs-keyword">const</span> res = <span class="hljs-built_in">Object</span>.create(parentVal); <span class="hljs-comment">//比如有同名的全局组件和自己定义的局部组件 那么parentVal代表全局组件 自己定义的组件是childVal  首先会查找自已局部组件有就用自己的  没有就从原型继承全局组件  res.__proto__===parentVal</span>
  <span class="hljs-keyword">if</span> (childVal) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> k <span class="hljs-keyword">in</span> childVal) &#123;
      res[k] = childVal[k];
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> res;
&#125;

<span class="hljs-comment">// 定义组件的合并策略</span>
ASSETS_TYPE.forEach(<span class="hljs-function">(<span class="hljs-params">type</span>) =></span> &#123;
  strats[type + <span class="hljs-string">"s"</span>] = mergeAssets;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里又使用到了原型继承的方式来进行组件合并 组件内部优先查找自己局部定义的组件 找不到会向上查找原型中定义的组件</p>
<h4 data-id="heading-5">4.创建组件 Vnode</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/util/index.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isObject</span>(<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-comment">//判断是否是对象</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> data !== <span class="hljs-string">"object"</span> || data == <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isReservedTag</span>(<span class="hljs-params">tagName</span>) </span>&#123;
  <span class="hljs-comment">//判断是不是常规html标签</span>
  <span class="hljs-comment">// 定义常见标签</span>
  <span class="hljs-keyword">let</span> str =
    <span class="hljs-string">"html,body,base,head,link,meta,style,title,"</span> +
    <span class="hljs-string">"address,article,aside,footer,header,h1,h2,h3,h4,h5,h6,hgroup,nav,section,"</span> +
    <span class="hljs-string">"div,dd,dl,dt,figcaption,figure,picture,hr,img,li,main,ol,p,pre,ul,"</span> +
    <span class="hljs-string">"a,b,abbr,bdi,bdo,br,cite,code,data,dfn,em,i,kbd,mark,q,rp,rt,rtc,ruby,"</span> +
    <span class="hljs-string">"s,samp,small,span,strong,sub,sup,time,u,var,wbr,area,audio,map,track,video,"</span> +
    <span class="hljs-string">"embed,object,param,source,canvas,script,noscript,del,ins,"</span> +
    <span class="hljs-string">"caption,col,colgroup,table,thead,tbody,td,th,tr,"</span> +
    <span class="hljs-string">"button,datalist,fieldset,form,input,label,legend,meter,optgroup,option,"</span> +
    <span class="hljs-string">"output,progress,select,textarea,"</span> +
    <span class="hljs-string">"details,dialog,menu,menuitem,summary,"</span> +
    <span class="hljs-string">"content,element,shadow,template,blockquote,iframe,tfoot"</span>;
  <span class="hljs-keyword">let</span> obj = &#123;&#125;;
  str.split(<span class="hljs-string">","</span>).forEach(<span class="hljs-function">(<span class="hljs-params">tag</span>) =></span> &#123;
    obj[tag] = <span class="hljs-literal">true</span>;
  &#125;);
  <span class="hljs-keyword">return</span> obj[tagName];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上诉是公用工具方法 在创建组件 Vnode 过程会用到</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/vdom/index.js</span>

<span class="hljs-keyword">import</span> &#123; isObject, isReservedTag &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../util/index"</span>;
<span class="hljs-comment">// 创建元素vnode 等于render函数里面的 h=>h(App)</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">vm, tag, data = &#123;&#125;, ...children</span>) </span>&#123;
  <span class="hljs-keyword">let</span> key = data.key;

  <span class="hljs-keyword">if</span> (isReservedTag(tag)) &#123;
    <span class="hljs-comment">// 如果是普通标签</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Vnode(tag, data, key, children);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 否则就是组件</span>
    <span class="hljs-keyword">let</span> Ctor = vm.$options.components[tag]; <span class="hljs-comment">//获取组件的构造函数</span>
    <span class="hljs-keyword">return</span> createComponent(vm, tag, data, key, children, Ctor);
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createComponent</span>(<span class="hljs-params">vm, tag, data, key, children, Ctor</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (isObject(Ctor)) &#123;
    <span class="hljs-comment">//   如果没有被改造成构造函数</span>
    Ctor = vm.$options._base.extend(Ctor);
  &#125;
  <span class="hljs-comment">// 声明组件自己内部的生命周期</span>
  data.hook = &#123;
    <span class="hljs-comment">// 组件创建过程的自身初始化方法</span>
    <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">vnode</span>)</span> &#123;
      <span class="hljs-keyword">let</span> child = (vnode.componentInstance = <span class="hljs-keyword">new</span> Ctor(&#123; <span class="hljs-attr">_isComponent</span>: <span class="hljs-literal">true</span> &#125;)); <span class="hljs-comment">//实例化组件</span>
      child.$mount(); <span class="hljs-comment">//因为没有传入el属性  需要手动挂载 为了在组件实例上面增加$el方法可用于生成组件的真实渲染节点</span>
    &#125;,
  &#125;;

  <span class="hljs-comment">// 组件vnode  也叫占位符vnode  ==> $vnode</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Vnode(
    <span class="hljs-string">`vue-component-<span class="hljs-subst">$&#123;Ctor.cid&#125;</span>-<span class="hljs-subst">$&#123;tag&#125;</span>`</span>,
    data,
    key,
    <span class="hljs-literal">undefined</span>,
    <span class="hljs-literal">undefined</span>,
    &#123;
      Ctor,
      children,
    &#125;
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改写 createElement 方法 对于非普通 html 标签 就需要生成组件 Vnode 把 Ctor 和 children 作为 Vnode 最后一个参数 componentOptions 传入</p>
<p>这里需要注意组件的 data.hook.init 方法 我们手动调用 child.$mount()方法 此方法可以生成组件的真实 dom 并且挂载到自身的 $el 属性上面 对此处有疑问的可以查看小编之前文章 <a href="https://juejin.cn/post/6937120983765483528" target="_blank">手写 Vue2.0 源码（三）-初始渲染原理</a></p>
<h4 data-id="heading-6">5.渲染组件真实节点</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/vdom/patch.js</span>

<span class="hljs-comment">// patch用来渲染和更新视图</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!oldVnode) &#123;
    <span class="hljs-comment">// 组件的创建过程是没有el属性的</span>
    <span class="hljs-keyword">return</span> createElm(vnode);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">//   非组件创建过程省略</span>
  &#125;
&#125;

<span class="hljs-comment">// 判断是否是组件Vnode</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createComponent</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-comment">// 初始化组件</span>
  <span class="hljs-comment">// 创建组件实例</span>
  <span class="hljs-keyword">let</span> i = vnode.data;
  <span class="hljs-comment">//   下面这句话很关键 调用组件data.hook.init方法进行组件初始化过程 最终组件的vnode.componentInstance.$el就是组件渲染好的真实dom</span>
  <span class="hljs-keyword">if</span> ((i = i.hook) && (i = i.init)) &#123;
    i(vnode);
  &#125;
  <span class="hljs-comment">// 如果组件实例化完毕有componentInstance属性 那证明是组件</span>
  <span class="hljs-keyword">if</span> (vnode.componentInstance) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125;
&#125;

<span class="hljs-comment">// 虚拟dom转成真实dom</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElm</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; tag, data, key, children, text &#125; = vnode;
  <span class="hljs-comment">//   判断虚拟dom 是元素节点还是文本节点</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> tag === <span class="hljs-string">"string"</span>) &#123;
    <span class="hljs-keyword">if</span> (createComponent(vnode)) &#123;
      <span class="hljs-comment">// 如果是组件 返回真实组件渲染的真实dom</span>
      <span class="hljs-keyword">return</span> vnode.componentInstance.$el;
    &#125;
    <span class="hljs-comment">//   虚拟dom的el属性指向真实dom 方便后续更新diff算法操作</span>
    vnode.el = <span class="hljs-built_in">document</span>.createElement(tag);
    <span class="hljs-comment">// 解析虚拟dom属性</span>
    updateProperties(vnode);
    <span class="hljs-comment">// 如果有子节点就递归插入到父节点里面</span>
    children.forEach(<span class="hljs-function">(<span class="hljs-params">child</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> vnode.el.appendChild(createElm(child));
    &#125;);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">//   文本节点</span>
    vnode.el = <span class="hljs-built_in">document</span>.createTextNode(text);
  &#125;
  <span class="hljs-keyword">return</span> vnode.el;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>判断如果属于组件 Vnode 那么把渲染好的组件真实 dom ==>vnode.componentInstance.$el 返回</p>
<h4 data-id="heading-7">6.组件的思维导图</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/396c604a21a3466c86f43ceb3ccf1b1f~tplv-k3u1fbpfcp-watermark.image" alt="Vue2.0源码-组件.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">小结</h2>
<p>至此 Vue 的 组件源码已经完结 其实每一个组件都是一个个 Vue 的实例 都会经历 init 初始化方法 建议学习组件之前先把前面的系列搞懂 组件就比较容易理解了 大家可以看着思维导图自己动手写一遍核心代码哈 遇到不懂或者有争议的地方欢迎评论留言</p>
<blockquote>
<p>最后如果觉得本文有帮助 记得<strong>点赞三连</strong>哦 十分感谢！</p>
</blockquote>
<h2 data-id="heading-9">系列链接（后续都会更新完毕）</h2>
<ul>
<li><a href="https://juejin.cn/post/6935344605424517128" target="_blank">手写 Vue2.0 源码（一）-响应式数据原理</a></li>
<li><a href="https://juejin.cn/post/6936024530016010276" target="_blank">手写 Vue2.0 源码（二）-模板编译原理</a></li>
<li><a href="https://juejin.cn/post/6937120983765483528" target="_blank">手写 Vue2.0 源码（三）-初始渲染原理</a></li>
<li><a href="https://juejin.cn/post/6938221715281575973" target="_blank">手写 Vue2.0 源码（四）-渲染更新原理</a></li>
<li><a href="https://juejin.cn/post/6939704519668432910" target="_blank">手写 Vue2.0 源码（五）-异步更新原理 </a></li>
<li><a href="https://juejin.cn/post/6953433215218483236" target="_blank">手写 Vue2.0 源码（六）-diff 算法原理</a></li>
<li><a href="https://juejin.cn/post/6951671158198501383" target="_blank">手写 Vue2.0 源码（七）-Mixin 混入原理</a></li>
<li><a href="https://juejin.cn/post/6954173708344770591">手写 Vue2.0 源码（八）-组件原理</a></li>
<li><a href="https://juejin.cn/post/6954173708344770591">手写 Vue2.0 源码（九）-计算属性和侦听属性原理</a></li>
<li><a href="https://juejin.cn/post/6954173708344770591">手写 Vue2.0 源码（十）-全局 api 分析</a></li>
<li><a href="https://juejin.cn/post/6954173708344770591">vue 面试真题-深入源码解析</a></li>
<li><a href="https://juejin.cn/post/6954173708344770591">手写 vue-router 源码</a></li>
<li><a href="https://juejin.cn/post/6954173708344770591">手写 vuex 源码</a></li>
<li><a href="https://juejin.cn/post/6954173708344770591">手写 vue3.0 源码</a></li>
</ul></div>  
</div>
            