
---
title: '一文深入了解Vue2和Vue3的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ce0f8d19d994e83be971699fe4461e9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 19:06:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ce0f8d19d994e83be971699fe4461e9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与「新人创作礼」活动， 一起开启掘金创作之路。</p>
<h1 data-id="heading-0">Vue3 和 Vue2 的区别</h1>
<h2 data-id="heading-1">考点</h2>
<ul>
<li>Vue3 和 Vue2 的介绍</li>
<li>Vue3 新增特性</li>
<li>Vue3 的优缺点</li>
<li>Vue2 的优缺点</li>
<li>Vue3 相对于Vue2 的非兼容性变更</li>
</ul>
<h2 data-id="heading-2">答案</h2>
<h3 data-id="heading-3">Vue3 的优点</h3>
<h4 data-id="heading-4">1. 速度更快</h4>
<ul>
<li>Vue3 相比 Vue2 来说，Vue3 重写了虚拟 <code>Dom</code> 实现，编译模板的优化，更高效的组件初始化，<code>undate</code>性能提高 1.3 ~ 2 倍，<code>SSR</code> 速度提高了 2 ~ 3 倍。</li>
</ul>
<h4 data-id="heading-5">2. 体积更小</h4>
<ul>
<li>通过 <code>webpack</code> 的 <code>tree-shaking</code> 功能，可以将无用模块“剪辑”，仅打包需要的模块。</li>
</ul>
<h4 data-id="heading-6">3. 更易维护</h4>
<ul>
<li><code>compositon Api</code> 可与现有的 <code>Options API</code> 一起使用。</li>
<li>灵活的逻辑组合与复用。</li>
<li><code>Vue3</code> 模块可以和其他框架搭配使用。</li>
</ul>
<h4 data-id="heading-7">4. 更接近原生</h4>
<ul>
<li>可以自定义渲染 API 。</li>
</ul>
<h4 data-id="heading-8">更易使用</h4>
<ul>
<li>响应式 <code>Api</code> 暴露出来。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ce0f8d19d994e83be971699fe4461e9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></li>
<li>轻松识别组件重新渲染原因。</li>
</ul>
<h3 data-id="heading-9">Vue3 新增特性</h3>
<ul>
<li>Vue3 中需要关注的一些新功能：
<ul>
<li><code>framents</code></li>
<li><code>Teleport</code></li>
<li><code>composition</code></li>
<li><code>createRenderer</code></li>
</ul>
</li>
</ul>
<h4 data-id="heading-10">framents</h4>
<ul>
<li>在 Vue3.x 中，组件现在支持有多个根节点。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- Layout.vue --></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">header</span>></span>...<span class="hljs-tag"></<span class="hljs-name">header</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">main</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"$attrs"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">main</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">footer</span>></span>...<span class="hljs-tag"></<span class="hljs-name">footer</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">Teleport</h4>
<ul>
<li><code>Teleport</code> 是一种能够将我们的模板移动到 <code>DOM</code> 中 <code>Vue app</code> 之外的其他位置的技术，就有点像哆啦A梦的“任意门”。</li>
<li>在 <code>vue2</code> 中，像 <code>modals</code>，<code>toast</code> 等这样的元素，如果我们嵌套在 Vue 的某个组件内部，那么处理<code>嵌套组件的定位</code>、<code>z-index</code> 和<code>样式</code>就会变得很困难。</li>
<li>通过 <code>Teleport</code> ，我们可以在组件的逻辑位置写模板代码，然后在 Vue 应用范围之外渲染它。
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"showToast"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn"</span>></span>打开 toast<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-comment"><!-- to 属性就是目标位置 --></span>
<span class="hljs-tag"><<span class="hljs-name">teleport</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"#teleport-target"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"visible"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"toast-wrap"</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"toast-msg"</span>></span>我是一个 Toast 文案<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">teleport</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-12">createRenderer</h4>
<ul>
<li>通过 <code>createRenderer</code> ，我们能够<code>构建自定义渲染器</code>，我们能够将 vue 的开发模型扩展到其他平台。</li>
<li>我们可以将其生成在 <code>canvas</code> 画布上。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcd1c610b62d4e05b06ee7871e92b6ec~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></li>
<li>了解 <code>createRenderer</code> 的基本使用。
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createRenderer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/runtime-core'</span>

<span class="hljs-keyword">const</span> &#123; render, createApp &#125; = <span class="hljs-title function_">createRenderer</span>(&#123;
  patchProp,
  insert,
  remove,
  createElement,
  <span class="hljs-comment">// ...</span>
&#125;)

<span class="hljs-keyword">export</span> &#123; render, createApp &#125;

<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/runtime-core'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-13">composition Api</h4>
<ul>
<li>composition Api，也就是组合式 <code>API</code>，通过这种形式，我们能够更加容易维护我们的代码，将相同功能的变量进行一个<code>集中式的管理</code>。</li>
<li>composition Api 的使用：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/759cb6e62c054d17ae980d1550413ddc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></li>
<li>composition Api 的简单使用：
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-title function_">setup</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">const</span> count = <span class="hljs-title function_">ref</span>(<span class="hljs-number">0</span>)
    <span class="hljs-keyword">const</span> double = <span class="hljs-title function_">computed</span>(<span class="hljs-function">() =></span> count.<span class="hljs-property">value</span> * <span class="hljs-number">2</span>)
    <span class="hljs-keyword">function</span> <span class="hljs-title function_">increment</span>(<span class="hljs-params"></span>) &#123;
        count.<span class="hljs-property">value</span>++
    &#125;
    <span class="hljs-title function_">onMounted</span>(<span class="hljs-function">() =></span> <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'component mounted!'</span>))
    <span class="hljs-keyword">return</span> &#123;
        count,
        double,
        increment
    &#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-14">非兼容性变更</h3>
<h4 data-id="heading-15">Global API</h4>
<ul>
<li>全局 <code>Vue API</code> 已更改为使用应用程序实例。</li>
<li><code>全局</code>和<code>内部 API</code> 已经被重构为可 <code>tree-shakable</code> 。</li>
</ul>
<h4 data-id="heading-16">模板指令</h4>
<ul>
<li>组件上 <code>v-model</code> 用法已更改。</li>
<li><code><template v-for></code> 和 <code>非 v-for</code> 节点上 <code>key</code> 用法已更改。</li>
<li>在<code>同一元素</code>上使用的 <code>v-if</code> 和 <code>v-for</code> 优先级已更改。
*<code> v-bind="object"</code> 现在排序敏感。</li>
<li><code>v-for 中的 ref 不再注册 ref 数组</code> 。</li>
</ul>
<h4 data-id="heading-17">组件</h4>
<ul>
<li>只能使用<code>普通函数</code>创建功能组件。</li>
<li><code>functional</code> 属性在单文件组件 <code>(SFC)</code> 。</li>
<li>异步组件现在需要 <code>defineAsyncComponent</code> 方法来创建。</li>
</ul>
<h4 data-id="heading-18">渲染函数</h4>
<ul>
<li>渲染函数 <code>API</code> 改变。</li>
<li><code>$scopedSlots</code> property 已删除，所有插槽都通过 <code>$slots</code> 作为函数暴露。</li>
<li>自定义指令 API 已更改为与组件生命周期一致。</li>
<li>一些转换 <code>class</code> 被重命名了：
<ul>
<li><code>v-enter</code> -> <code>v-enter-from</code>。</li>
<li><code>v-leave</code> -> <code>v-leave-from</code>。</li>
</ul>
</li>
<li>组件 <code>watch</code> 选项和实例方法 <code>$watch</code> 不再支持点分隔字符串路径，请改用计算函数作为参数。</li>
<li>在 <code>Vue 2.x</code> 中，应用根容器的 <code>outerHTML</code> 将替换为根组件模板 (如果根组件没有模板/渲染选项，则最终编译为模板)。<code>Vue3.x</code> 现在使用应用程序容器的 <code>innerHTML</code>。</li>
</ul>
<h4 data-id="heading-19">其他小改变</h4>
<ul>
<li><code>destroyed</code> 生命周期选项被重命名为 <code>onUnmounted</code>。</li>
<li><code>beforeDestroy</code> 生命周期选项被重命名为 <code>onBeforeUnmount</code>。</li>
<li><code>[prop default</code> 工厂函数不再有权访问 <code>this</code> 是上下文。</li>
<li>自定义指令 API 已更改为与组件生命周期一致。</li>
<li><code>data</code> 应始终声明为函数。</li>
<li>来自 <code>mixin</code> 的 <code>data</code> 选项现在可<code>简单地合并</code>。</li>
<li><code>attribute</code> 强制策略已更改。</li>
<li>一些过渡 <code>class</code> 被重命名。</li>
<li>组建 watch 选项和实例方法 <code>$watch</code> 不再支持以点分隔的字符串路径。请改用计算属性函数作为参数。</li>
<li><code><template></code> 没有特殊指令的标记 <code>(v-if/else-if/else、v-for 或 v-slot) </code> 现在被视为普通元素，并将生成原生的 <code><template></code> 元素，而不是渲染其内部内容。</li>
<li>在 <code>Vue 2.x</code> 中，应用根容器的 <code>outerHTML</code> 将替换为根组件模板 (如果根组件没有模板/渲染选项，则最终编译为模板)。<code>Vue 3.x</code> 现在使用应用容器的 <code>innerHTML</code>，这意味着容器本身不再被视为模板的一部分。</li>
</ul>
<h4 data-id="heading-20">移除 API</h4>
<ul>
<li><code>keyCode</code> 支持作为 <code>v-on</code> 的修饰符。</li>
<li><code>$on</code>，<code>$off</code> 和 <code>$once</code> 实例方法。</li>
<li>过滤 <code>filter</code> 。</li>
<li>内联模板 <code>attribute</code> 。</li>
<li><code>$destroy</code> 实例方法。用户不应再手动管理单个 Vue 组件的生命周期。</li>
</ul>
<h2 data-id="heading-21">扩展</h2>
<h3 data-id="heading-22">能够使用 webpack 的 tree-shaking 有什么好处？</h3>
<ul>
<li>
<p>对开发人员：能够使用 <code>vue</code> 开发出更多其他的功能，而不必担忧整体体积过大。</p>
</li>
<li>
<p>对使用者：打包出来的包体积变小了。</p>
</li>
</ul></div>  
</div>
            