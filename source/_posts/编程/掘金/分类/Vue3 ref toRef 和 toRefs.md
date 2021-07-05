
---
title: 'Vue3 ref toRef 和 toRefs'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a3fec262898412c9b15d2405d04ec09~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 01:36:29 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a3fec262898412c9b15d2405d04ec09~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">ref</h1>
<h2 data-id="heading-1">基本用法</h2>
<ol>
<li>生成值类型的响应式数据</li>
<li>可用于模板和 reactive</li>
<li>通过.value修改值</li>
</ol>
<p>示例代码</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>Ref Demo for &#123;&#123;state.name&#125;&#125; and &#123;&#123;ageRef&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"elementRef"</span>></span>这是用来验证 ref template的<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, reactive, onMounted &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Ref'</span>,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> ageRef = ref(<span class="hljs-number">20</span>) <span class="hljs-comment">//值类型 响应式</span>
        <span class="hljs-keyword">const</span> nameRef = ref(<span class="hljs-string">'Bean'</span>)

        <span class="hljs-keyword">const</span> elementRef = ref(<span class="hljs-literal">null</span>)

        <span class="hljs-keyword">const</span> state = reactive(&#123;     <span class="hljs-comment">//可用于reactive</span>
            <span class="hljs-attr">name</span>: nameRef
        &#125;)

        onMounted(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"ref template is ===> "</span>, elementRef.value)
        &#125;)

        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"age is ===>"</span> + ageRef.value)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"name is ===> "</span> + state.name)

            ageRef.value = <span class="hljs-number">30</span>
            nameRef.value = <span class="hljs-string">'Bean Mother'</span>
        &#125;, <span class="hljs-number">1200</span>);

        <span class="hljs-keyword">return</span> &#123; ageRef, state, elementRef &#125;
    &#125;    
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a3fec262898412c9b15d2405d04ec09~tplv-k3u1fbpfcp-watermark.image" alt="vue3-ref.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">toRef</h1>
<h2 data-id="heading-3">基本用法</h2>
<ol>
<li>针对一个响应式对象（reactive）的prop</li>
<li>创建一个ref，具有响应式</li>
<li>两者保持引用关系</li>
</ol>
<p>示例代码</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span> toRef Demo for &#123;&#123;state.name&#125;&#125; -- &#123;&#123;ageRef&#125;&#125; --&#123;&#123;state.age&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, toRef, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'ToRef'</span>,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> state = reactive(&#123;    <span class="hljs-comment">//响应式对象，可以尝试把state设置成普通对象再实验，有什么效果？</span>
            <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'Bean'</span>
        &#125;)

        <span class="hljs-keyword">const</span> ageRef = toRef(state, <span class="hljs-string">'age'</span>)  <span class="hljs-comment">//创建一个ref</span>

        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;    <span class="hljs-comment">//ref和reactive保持引用关系，互相影响对方</span>
            state.age = <span class="hljs-number">30</span>
        &#125;, <span class="hljs-number">1200</span>);

        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            ageRef.value = <span class="hljs-number">40</span>
        &#125;, <span class="hljs-number">2400</span>);

        <span class="hljs-keyword">return</span> &#123;
            state, ageRef
        &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9df6dd4b42947748f570c88431e7abe~tplv-k3u1fbpfcp-watermark.image" alt="vue3-toRef.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">toRefs</h1>
<h2 data-id="heading-5">基本用法</h2>
<ol>
<li>将响应式对象（reactive封装）转换成普通对象</li>
<li>对象的每个prop都是对应的ref</li>
<li>两者保持引用关系</li>
</ol>
<p>示例代码</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <!-- <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span> toRefs Demo for &#123;&#123;nameRef&#125;&#125; -- &#123;&#123;ageRef&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span> -->
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span> toRefs Demo for &#123;&#123;name&#125;&#125; -- &#123;&#123;age&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, toRef, toRefs, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'ToRefs'</span>,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> state = reactive(&#123;    <span class="hljs-comment">//响应式对象</span>
            <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'Bean'</span>
        &#125;)

        <span class="hljs-keyword">const</span> stateToRefs = toRefs(state) <span class="hljs-comment">//普通对象</span>

        <span class="hljs-comment">//用法一</span>
        <span class="hljs-comment">// const &#123; age: ageRef, name: nameRef&#125; = stateToRefs  //每个属性都是ref对象</span>
        <span class="hljs-comment">// return &#123;</span>
        <span class="hljs-comment">//     ageRef, nameRef</span>
        <span class="hljs-comment">// &#125;</span>

        <span class="hljs-comment">//用法二</span>
        <span class="hljs-keyword">return</span> stateToRefs
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1214327d9cd47bbae70440fd4313197~tplv-k3u1fbpfcp-watermark.image" alt="vue3-toRefs.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">ref toRef 和 toRefs的最佳使用方式</h1>
<ol>
<li>用reactive做对象的响应式，用ref做值类型的响应式</li>
<li>setup中返回toRefs(state), 或者 toRef(state, '属性名')</li>
<li>合成函数返回响应式对象时，使用 toRefs</li>
</ol>
<p>合成函数的示例代码</p>
<p>定义一个合成函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">demo1</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> state = reactive(&#123;
        <span class="hljs-attr">x</span>: <span class="hljs-number">25</span>,
        <span class="hljs-attr">y</span>: <span class="hljs-string">'Bean'</span>
    &#125;)
    <span class="hljs-comment">//逻辑运行状态，省略N行</span>
    。。。。。。
    
    <span class="hljs-comment">//返回时转换为ref</span>
    <span class="hljs-keyword">return</span> toRefs(state)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用合成函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123;x, y&#125; = demo1()
        
        <span class="hljs-keyword">return</span> &#123;
            x, y
        &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">为啥需要用ref</h1>
<p>在setup、computed、合成函数中，都有可能返回值类型。而值类型的返回，往往容易丢失响应式。</p>
<p>Vue3对响应式的处理方式有些改变，使用了Proxy。而这种方式对值类型的响应式却无能为力，所以在Vue3中只能通过ref这种方式来解决值类型响应式的问题。</p>
<h1 data-id="heading-8">那为啥ref需要.value?</h1>
<ul>
<li>ref是一个对象（不丢失响应式），value是存储值</li>
<li>通过.value属性的get和set实现响应式</li>
<li>只有ref用于模板、reactive时不需要.value,其他情况都需要</li>
</ul>
<h1 data-id="heading-9">为啥需要 toRef 和 toRefs</h1>
<ul>
<li>初衷： 在保证不丢失响应式的前提下，把对象解构，方便对象数据分解和扩散</li>
<li>前提：针对的是响应式对象（reactive封装的）非普通对象</li>
<li>注意： 不创造响应式（那是reactive的事情），只是延续响应式</li>
</ul></div>  
</div>
            