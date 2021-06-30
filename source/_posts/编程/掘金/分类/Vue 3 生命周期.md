
---
title: 'Vue 3 生命周期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5240f1425e4446cab4473d709168334~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 01:59:02 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5240f1425e4446cab4473d709168334~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在组件化的框架中，比如Vue为组件定义了生命周期这个概念。每个组件实例在被创建时都要经过一系列的初始化过程，比如模板编译、更新、销毁等。同时，在这些过程中也会运行一些叫做生命周期钩子的函数，他们提供给开发者在组件的不同阶段添加自己的代码逻辑的机会。</p>
<p>使用过Vue2.x的朋友肯定对Vue2的生命周期钩子很熟悉，因为在实际开发中我们或多或少会用到过他们，比如mounted里的异步调用，比如beforeDestory的清除自定义事件等等。而在Vue3.0中，Vue2.x的Options API形式的生命周期钩子和新的Composition API都可以使用，来代码示例。</p>
<h1 data-id="heading-0">Options API基本使用</h1>
<p>App.vue</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">lifeCycles</span> <span class="hljs-attr">:msg</span>=<span class="hljs-string">"msg"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"flag"</span> /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"updateMsg"</span>></span>change message<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"updateFlag"</span>></span>change flag<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> LifeCycles <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/LifeCycles.vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-attr">components</span>: &#123;
    LifeCycles
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'Welcome to Vue3'</span>,
      <span class="hljs-attr">flag</span>: <span class="hljs-literal">true</span>,
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">updateMsg</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.msg = <span class="hljs-string">'Welcome to Vue3 Update '</span> + <span class="hljs-built_in">Date</span>.now();
    &#125;,
    <span class="hljs-function"><span class="hljs-title">updateFlag</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.flag = !<span class="hljs-built_in">this</span>.flag;
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>LifeCycles.vue</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>生命周期 &#123;&#123;msg&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'LifeCycles'</span>,
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">msg</span>: <span class="hljs-built_in">String</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'before create'</span>)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'created'</span>)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">beforeMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'before mount'</span>)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mounted'</span>)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">beforeUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'before update'</span>)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">updated</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'updated'</span>)
    &#125;,
    <span class="hljs-comment">//beforeDestory已废弃</span>
    <span class="hljs-function"><span class="hljs-title">beforeUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'before unmount'</span>)
    &#125;,
    <span class="hljs-comment">//destroyed已废弃</span>
    <span class="hljs-function"><span class="hljs-title">unmounted</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mounted'</span>)
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5240f1425e4446cab4473d709168334~tplv-k3u1fbpfcp-watermark.image" alt="vue3-optionAPI.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">Composition API基本使用</h1>
<p>Compistion API的示例代码</p>
<p>LifeCycles.vue</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>生命周期 &#123;&#123;msg&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'LifeCycles'</span>,
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">msg</span>: <span class="hljs-built_in">String</span>
    &#125;,
    <span class="hljs-comment">//等同于 beforeCreate 和 created</span>
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'set up'</span>);

        onBeforeMount(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'before mount'</span>)
        &#125;)
        onMounted(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mounted'</span>)
        &#125;)
        onBeforeUpdate(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'before update'</span>)    
        &#125;)
        onUpdated(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'updated'</span>)
        &#125;)
        onBeforeUnmount(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'before unmount'</span>)
        &#125;)
        onUnmounted(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mounted'</span>)
        &#125;)
    &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26567e35a75f4416b8c3ef187218a464~tplv-k3u1fbpfcp-watermark.image" alt="vue3-compositionAPI.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">为什么会有Composition API？</h1>
<h2 data-id="heading-3">为了更好的代码组织</h2>
<p>假设一个vue组件是一个大型组件，它的内部有很多处理逻辑的关注点(对应Options API)。有没有一种碎片化的感觉，这种碎片化使得开发者很难去理解和维护组件。
Composition API的出现就是解决这个问题的，它将某个逻辑关注点相关的代码全都放在一个函数里，这样当需要修改一个功能时，就不需要在文件中跳来跳去。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68d311f558724536977084dd13f536b6~tplv-k3u1fbpfcp-watermark.image" alt="1161361-20210203191859382-111855115.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">示例对比</h3>
<p>这是一个用Vue2 Option API写的一个加法组件：</p>
<ul>
<li>3个参数，加数(num1)和被加数(num2)，还有一个和(sum)</li>
<li>2个input框</li>
<li>1个method</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"add"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>Addition Calculator<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"sum"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"form-control"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"num1"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"form-control"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"num2"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"addNumbers"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-light"</span>></span>
                Add me!
            <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">form</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">strong</span>></span>Sum:<span class="hljs-tag"></<span class="hljs-name">strong</span>></span> &#123;&#123; sum &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Add'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">num1</span>: <span class="hljs-number">0</span>,
            <span class="hljs-attr">num2</span>: <span class="hljs-number">0</span>,
            <span class="hljs-attr">sum</span>: <span class="hljs-number">0</span>
        &#125;;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-attr">addNumbers</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">this</span>.sum = <span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">this</span>.num1) + <span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">this</span>.num2);
        &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>改成Composition API之后</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"add"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>Addition Calculator<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"sumComp"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"form-control"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"num1"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"form-control"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"num2"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"addNumbers"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-light"</span>></span>
            Add me!
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">form</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">strong</span>></span>Sum:<span class="hljs-tag"></<span class="hljs-name">strong</span>></span> &#123;&#123; sum &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/composition-api'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'AddComposition'</span>,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> num1 = ref(<span class="hljs-number">0</span>);
        <span class="hljs-keyword">let</span> num2 = ref(<span class="hljs-number">0</span>);
        <span class="hljs-keyword">let</span> sum = ref(<span class="hljs-number">0</span>);
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addNumbers</span>(<span class="hljs-params"></span>) </span>&#123;
            sum.value = <span class="hljs-built_in">parseInt</span>(num1.value) + <span class="hljs-built_in">parseInt</span>(num2.value);
        &#125;
        <span class="hljs-keyword">return</span> &#123;
            num1,
            num2,
            sum,
            addNumbers
        &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">为了更好的逻辑复用</h2>
<h3 data-id="heading-6">TODO</h3>
<h1 data-id="heading-7">如何选择？</h1>
<ul>
<li>不建议共用，会引起混乱</li>
<li>小型项目、业务逻辑简单，用Options API</li>
<li>中大型项目、逻辑复杂，用Composition API</li>
</ul></div>  
</div>
            