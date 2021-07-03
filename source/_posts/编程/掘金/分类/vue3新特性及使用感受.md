
---
title: 'vue3新特性及使用感受'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff94cb96d5684b62aac54b1438785788~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 01:27:33 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff94cb96d5684b62aac54b1438785788~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">VUE3新特性</h1>
<h2 data-id="heading-1">1. Composition API</h2>
<ul>
<li>
<h3 data-id="heading-2">setup</h3>
<p>使用<code>setup</code>时，它接受两个参数：</p>
<ol>
<li>props: 组件传入的属性</li>
<li>context：提供三个属性</li>
</ol>
<p>setup 中接受的<code>props</code>是响应式的， 当传入新的 props 时，会及时被更新。由于是响应式的， 所以<strong>不可以使用 ES6 解构</strong>，解构会消除它的响应式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; xxx &#125; = toRefs(props) <span class="hljs-comment">// 可用toRefs解决</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>setup</code>中不能访问 Vue2 中最常用的<code>this</code>对象，所以<code>context</code>中就提供了<code>this</code>中最常用的三个属性：<code>attrs</code>、<code>slot</code> 和<code>emit</code>，分别对应 Vue2.x 中的 <code>$attr</code>属性、<code>slot</code>插槽 和<code>$emit</code>发射事件。并且这几个属性都是自动同步最新的值，所以我们每次使用拿到的都是最新值。</p>
<p><strong>语法糖 script setup</strong></p>
<p>直接给script标签添加setup属性,不要像旧的语法那样在底部return一堆属性出去</p>
<p>组件import后直接在template使用,不需要注册</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
 <span>&#123;&#123; num &#125;&#125;</span>
  <panel></panel>
  </div>
</template>

<script setup>
  import &#123; ref &#125; from 'vue'
  import Panel from '@/components/Panel.vue'
  
  const num = ref(0)
</srcipt>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://github.com/vuejs/rfcs/blob/script-setup-2/active-rfcs/0000-script-setup.md#summary" target="_blank" rel="nofollow noopener noreferrer">script setup 相关文档</a></p>
</li>
<li>
<h3 data-id="heading-3">reactive</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="about">
    <div>
      <span>count 点击次数: </span>
      <span>&#123;&#123; count &#125;&#125;</span>
      <button @click="addCount">点击增加</button>
    </div>
  </div>
</template>
<script>
import &#123; reactive, toRefs &#125; from 'vue'
export default &#123;
  setup () &#123;
    const state = reactive(&#123;
      count: 0
    &#125;)
    const addCount = function () &#123;
      state.count++
    &#125;
    return &#123;
      // 这样展开后state property会失去响应式，因为是取值返回，不是引用
      // ...state,
      ...toRefs(state),
      addCount,
    &#125;
  &#125;,
&#125;
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h3 data-id="heading-4">ref</h3>
<p><code>ref</code>函数将一个普通对象转化为响应式包装对象，将一个 <code>ref</code> 值暴露给渲染上下文，在渲染过程中，Vue 会直接使用其内部的值，在模板中可以把 <code>&#123;&#123; num.value &#125;&#125;</code> 直接写为 <code>&#123;&#123; num &#125;&#125;</code> ，但是在js中还是需要通过 <code>num.value</code>取值和赋值</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="about">
    <div>
      <span>num 点击次数: </span>
      <span>&#123;&#123; num &#125;&#125;</span>
      <button @click="addNum">点击增加</button>
    </div>
  </div>
</template>
<script>
import &#123; ref &#125; from 'vue'
export default &#123;
  setup () &#123;
    const num = ref(0)

    const addNum = function () &#123;
      num.value++
    &#125;
    return &#123;
      num,
      addNum
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h3 data-id="heading-5">toRefs</h3>
<p><code>toRefs</code>将<code>reactive</code>对象转换为普通对象，其中结果对象上的每个属性都是指向原始对象中相应属性的<code>ref</code>引用对象，这在组合函数返回响应式状态时非常有用，这样保证了开发者使用对象解构或拓展运算符不会丢失原有响应式对象的响应</p>
</li>
<li>
<h3 data-id="heading-6">readonly</h3>
<p>对于不允许写的对象，不管是普通<code>object</code>对象、<code>reactive</code>对象、<code>ref</code>对象，都可以通过<code>readonly</code>方法返回一个只读对象</p>
<p>直接修改<code>readonly</code>对象，控制台会打印告警信息，不会报错</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> state = reactive(&#123;
  <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
&#125;)
<span class="hljs-keyword">const</span> readonlyState = readonly(state)

<span class="hljs-comment">// 监听只读属性，state.count修改后依然会触发readonlyState.count更新</span>
watch(<span class="hljs-function">() =></span> readonlyState.count, <span class="hljs-function">(<span class="hljs-params">newVal, oldVal</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'readonly state is changed!'</span>)
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 修改只读属性会打印告警信息，但是不会报错</span>
    readonlyState.count = <span class="hljs-number">666</span>
  &#125;, <span class="hljs-number">1000</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h3 data-id="heading-7">生命周期</h3>
</li>
</ul>
<p>setup 执行时机是在 beforeCreate 之前执行</p>
<p>相对应的生命周期，3版本的执行时机总比2版本的早</p>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff94cb96d5684b62aac54b1438785788~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>
<h3 data-id="heading-8">Computed</h3>
<p>接受一个 getter 函数，并为从 getter 返回的值返回一个不变的响应式 <a href="https://v3.cn.vuejs.org/api/refs-api.html#ref" target="_blank" rel="nofollow noopener noreferrer">ref</a> 对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">1</span>)
<span class="hljs-keyword">const</span> plusOne = computed(<span class="hljs-function">() =></span> count.value + <span class="hljs-number">1</span>)

<span class="hljs-built_in">console</span>.log(plusOne.value) <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者，它也可以使用具有 <code>get</code> 和 <code>set</code> 函数的对象来创建可写的 ref 对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">1</span>)
<span class="hljs-keyword">const</span> plusOne = computed(&#123;
  <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> count.value + <span class="hljs-number">1</span>,
  <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-params">val</span> =></span> &#123;
    count.value = val - <span class="hljs-number">1</span>
  &#125;
&#125;)

plusOne.value = <span class="hljs-number">1</span>
<span class="hljs-built_in">console</span>.log(count.value) <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h3 data-id="heading-9">watch</h3>
</li>
</ul>
<pre><code class="hljs language-vue copyable" lang="vue">watch(source, callback, [options])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​参数说明：</p>
<p>​source: 可以支持 string,Object,Function,Array; 用于指定要侦听的响应式变量</p>
<p>​callback: 执行的回调函数</p>
<p>​options：支持 deep、immediate 和 flush 选项。</p>
<h4 data-id="heading-10">侦听 reactive 定义的数据</h4>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">const</span> state = reactive(&#123; <span class="hljs-attr">nickname</span>: <span class="hljs-string">"lilei"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">20</span> &#125;);
    <span class="hljs-comment">// 修改age值时会触发 watch的回调</span>
    watch(
      <span class="hljs-function">() =></span> state.age,             
      <span class="hljs-function">(<span class="hljs-params">curAge, preAge</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"新值:"</span>, curAge, <span class="hljs-string">"老值:"</span>, preAge);
      &#125;
    );
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">侦听 ref 定义的数据</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> year = ref(<span class="hljs-number">0</span>);
watch(year, <span class="hljs-function">(<span class="hljs-params">newVal, oldVal</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"新值:"</span>, newVal, <span class="hljs-string">"老值:"</span>, oldVal);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">侦听多个数据</h4>
<pre><code class="hljs language-js copyable" lang="js">watch(
  [<span class="hljs-function">() =></span> state.age, year],
  <span class="hljs-function">(<span class="hljs-params">[curAge, newVal], [preAge, oldVal]</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"新值:"</span>, curAge, <span class="hljs-string">"老值:"</span>, preAge);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"新值:"</span>, newVal, <span class="hljs-string">"老值:"</span>, oldVal);
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">侦听复杂的嵌套对象</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> state = reactive(&#123;
  <span class="hljs-attr">room</span>: &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">100</span>,
    <span class="hljs-attr">attrs</span>: &#123;
      <span class="hljs-attr">size</span>: <span class="hljs-string">"140平方米"</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">"三室两厅"</span>,
    &#125;,
  &#125;,
&#125;);
watch(
  <span class="hljs-function">() =></span> state.room,
  <span class="hljs-function">(<span class="hljs-params">newType, oldType</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"新值:"</span>, newType, <span class="hljs-string">"老值:"</span>, oldType);
  &#125;,
  &#123; <span class="hljs-attr">deep</span>: <span class="hljs-literal">true</span> &#125;
);

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">stop 停止监听</h4>
<p>我们在组件中创建的<code>watch</code>监听，会在组件被销毁时自动停止。如果在组件销毁之前我们想要停止掉某个监听， 可以调用<code>watch()</code>函数的返回值，操作如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> stopWatchRoom = watch(<span class="hljs-function">() =></span> state.room, <span class="hljs-function">(<span class="hljs-params">newType, oldType</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"新值:"</span>, newType, <span class="hljs-string">"老值:"</span>, oldType);
&#125;, &#123;<span class="hljs-attr">deep</span>:<span class="hljs-literal">true</span>&#125;);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-comment">// 停止监听</span>
    stopWatchRoom()
&#125;, <span class="hljs-number">3000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">2. Fragment</h2>
<ol>
<li>
<p>可以直接写多个节点，根节点不是必要的，无需创建了，减少了节点数。</p>
</li>
<li>
<p>Fragment节点是虚拟的，不会DOM树中呈现。</p>
</li>
</ol>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
    <div></div>
    <div></div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">3. Teleport</h2>
<p>例子：在子组件<code>Header</code>中使用到<code>Dialog</code>组件，此时<code>Dialog</code>就被渲染到一层层子组件内部，处理嵌套组件的定位、<code>z-index</code>和样式都变得困难。 <code>Dialog</code>从用户感知的层面，应该是一个独立的组件，从 dom 结构应该完全剥离 Vue 顶层组件挂载的 DOM；同时还可以使用到 Vue 组件内的状态（<code>data</code>或者<code>props</code>）的值。</p>
<p>​      <strong>即希望继续在组件内部使用<code>Dialog</code>, 又希望渲染的 DOM 结构不嵌套在组件的 DOM 中</strong>。</p>
<p>若希望 Dialog 渲染的 dom 和顶层组件是兄弟节点关系, 在<code>index.html</code>文件中定义一个供挂载的元素:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"dialog"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义一个<code>Dialog</code>组件<code>Dialog.vue</code>,    <code>to</code> 属性， 与上面的<code>id</code>选择器一致：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <teleport to="#dialog">
    <div class="dialog">
 ...
    </div>
  </teleport>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在一个子组件<code>Header.vue</code>中使用<code>Dialog</code>组件。<code>header</code>组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><div class="header">
    ...
    <navbar />
    <Dialog v-if="dialogVisible"></Dialog>
</div>
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Dom 渲染效果如下：</p>
 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/712e61d275cb4b7da5252bb9cd6d2afa~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"> 
<p>使用 <code>teleport</code> 组件，通过 <code>to</code> 属性，指定该组件渲染的位置与 <code><div id="app"></div></code> 同级，也就是在 <code>body</code> 下，但是 <code>Dialog</code> 的状态 <code>dialogVisible</code> 又是完全由内部 Vue 组件控制.</p>
<h2 data-id="heading-17">4. Suspense</h2>
<img src="https://juejin.cn/Users/rzz/Library/Application%20Support/typora-user-images/image-20210629141155408.png" alt="image-20210629141155408" loading="lazy" referrerpolicy="no-referrer">
<p>在正确渲染组件之前进行一些异步请求是很常见的事。组件通常会在本地处理这种逻辑，绝大多数情况下这是非常完美的做法。</p>
<p>该 <code><suspense></code> 组件提供了另一个方案，允许等待整个组件树处理完毕而不是单个组件。</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <suspense>
     <template #default>
       <async-component></async-component>
     </template>
     <template #fallback>
       <div> 
         Loading...
       </div>
     </template>
  </suspense>
</template> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 <code><suspense></code> 组件有两个插槽。它们都只接收一个子节点。<code>default</code> 插槽里的节点会尽可能展示出来。如果不能，则展示 <code>fallback</code> 插槽里的节点。</p>
<p>重要的是，异步组件不需要作为 <code><suspense></code> 的最近子节点。它可以在组件树任意深度的位置且不需要出现在和 <code><suspense></code> 自身相同的模板中。只有所有的后代组件都准备就绪，该内容才会被认为解析完毕。</p>
<h2 data-id="heading-18">5. vue-router</h2>
<p>vue2.x使用路由选项redirect设置路由自动调整，vue3.x中移除了这个选项，将在子路由中添加一个空路径路由来匹配跳转</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue2.x router</span>
[
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">component</span>: Layout,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'WebHome'</span>,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/dashboard'</span>, <span class="hljs-comment">// 这里写跳转</span>
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'dashboard'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Dashboard'</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/dashboard/index.vue'</span>)
      &#125;
    ]
  &#125;
]

<span class="hljs-comment">// vue3.x router</span>
[
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">component</span>: Layout,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'WebHome'</span>,
    <span class="hljs-attr">children</span>: [
      &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>, <span class="hljs-attr">redirect</span>: <span class="hljs-string">'dashboard'</span> &#125;, <span class="hljs-comment">// 这里写跳转</span>
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'dashboard'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Dashboard'</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/dashboard/index.vue'</span>)
      &#125;
    ]
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useRouter, useRoute &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  setup () &#123;
    <span class="hljs-keyword">const</span> router = useRouter()
    <span class="hljs-keyword">const</span> route = useRoute()
    <span class="hljs-keyword">return</span> &#123;
      
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">6. Vuex</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  setup () &#123;
    <span class="hljs-keyword">const</span> store = userStore()

    <span class="hljs-keyword">const</span> userId = computed(<span class="hljs-function">() =></span> store.state.app.userId)
    <span class="hljs-keyword">const</span> getUserInfo = <span class="hljs-function">() =></span> store.dispatch(<span class="hljs-string">'xxxx'</span>)
<span class="hljs-keyword">const</span> setUserInfo = <span class="hljs-function">() =></span> store.commit(<span class="hljs-string">'xxx'</span>)
    <span class="hljs-keyword">return</span> &#123;
      userId
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">7. getCurrentInstance</h2>
<p>获取当前的组件实例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; getCurrentInstance &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  setup () &#123;
    <span class="hljs-comment">// const &#123; ctx &#125; = getCurrentInstance()          ctx 只在开发环境生效，生产环境无效</span>
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">proxy</span>: ctx &#125; = getCurrentInstance()
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ccccc'</span>, ctx)
    <span class="hljs-keyword">return</span> &#123;
     
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21"><strong>了解更多可查看<a href="https://vue3js.cn/docs/zh/guide/composition-api-introduction.html#%E4%BB%80%E4%B9%88%E6%98%AF%E7%BB%84%E5%90%88%E5%BC%8F-api" target="_blank" rel="nofollow noopener noreferrer">官方文档</a></strong></h4>
<h1 data-id="heading-22">使用总结</h1>
<ol>
<li>
<p>在2版本时候，当代码行数很多时,data,计算属性，watch都分布在不同区域，要来回切换，开发体验不好，新版本可以按业务逻辑放到一块</p>
</li>
<li>
<p>组合式Api开发起来更加灵活,逻辑复用较好</p>
</li>
<li>
<p>业务逻辑集中写在setup中，可能会导致代码臃肿较难维护</p>
</li>
</ol>
<p>​       组件抽离、要统一开发规范</p>
<ol start="4">
<li>
<p>利用 ES6 模块系统import/export，按需编译，体积比Vue2.x更小 (Tree shaking）</p>
<p><code>import &#123; computed, watch &#125; from "vue";</code></p>
</li>
</ol>
<h1 data-id="heading-23">问题：</h1>
<h3 data-id="heading-24">watch监听reactive的数据为什么需要用函数返回？</h3>
<p><strong>1.官网，data源要是返回值的getter函数或ref</strong></p>
<img src="https://juejin.cn/Users/rzz/Library/Application%20Support/typora-user-images/image-20210702170541469.png" alt="image-20210702170541469" loading="lazy" referrerpolicy="no-referrer">
<p><strong>watch源码</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">watch</span><<span class="hljs-title">T</span> = <span class="hljs-title">any</span>>(<span class="hljs-params">
  source: WatchSource<T> | WatchSource<T>[],  <span class="hljs-comment">/* getter方法  */</span>
  cb: WatchCallback<T>,                       <span class="hljs-comment">/* hander回调函数 */</span>
  options?: WatchOptions                      <span class="hljs-comment">/* watchOptions */</span>
</span>): <span class="hljs-title">StopHandle</span> </span>&#123; 
  <span class="hljs-keyword">return</span> doWatch(source, cb, options)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>watch接受三个参数，分别是getter方法，回调函数，和options配置项。</p>
<h3 data-id="heading-25">doWatch核心方法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">doWatch</span>(<span class="hljs-params">
  source: WatchSource | WatchSource[] | WatchEffect,
  cb: WatchCallback | <span class="hljs-literal">null</span>,
  &#123; immediate, deep, flush, onTrack, onTrigger &#125;: WatchOptions = EMPTY_OBJ
</span>): <span class="hljs-title">StopHandle</span> </span>&#123;
  <span class="hljs-comment">/* 此时的 instance 是当前正在初始化操作的 instance  */</span>
  <span class="hljs-keyword">const</span> instance = currentInstance
  <span class="hljs-keyword">let</span> getter: <span class="hljs-function">() =></span> any
  <span class="hljs-keyword">if</span> (isArray(source)) &#123; <span class="hljs-comment">/*  判断source 为数组 ，此时是watch情况 */</span>
    getter = <span class="hljs-function">() =></span>
      source.map(
        <span class="hljs-function"><span class="hljs-params">s</span> =></span>
          isRef(s)
            ? s.value
            : callWithErrorHandling(s, instance, ErrorCodes.WATCH_GETTER)
      )
  <span class="hljs-comment">/* 判断ref情况 ，此时watch api情况*/</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isRef(source)) &#123;
    getter = <span class="hljs-function">() =></span> source.value
   <span class="hljs-comment">/* 正常watch情况，处理getter () => state.count */</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (cb) &#123; 
    getter = <span class="hljs-function">() =></span>
      callWithErrorHandling(source, instance, ErrorCodes.WATCH_GETTER)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">/*  watchEffect 情况 */</span>
    getter = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (instance && instance.isUnmounted) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-keyword">if</span> (cleanup) &#123;
        cleanup()
      &#125;
      <span class="hljs-keyword">return</span> callWithErrorHandling(
        source,
        instance,
        ErrorCodes.WATCH_CALLBACK,
        [onInvalidate]
      )
    &#125;
  &#125;
   <span class="hljs-comment">/* 处理深度监听逻辑 */</span>
  <span class="hljs-keyword">if</span> (cb && deep) &#123;
    <span class="hljs-keyword">const</span> baseGetter = getter
    <span class="hljs-comment">/* 将当前 */</span>
    getter = <span class="hljs-function">() =></span> traverse(baseGetter())
  &#125;

  <span class="hljs-keyword">let</span> cleanup: <span class="hljs-function">() =></span> <span class="hljs-keyword">void</span>
  <span class="hljs-comment">/* 清除当前watchEffect */</span>
  <span class="hljs-keyword">const</span> onInvalidate: InvalidateCbRegistrator = <span class="hljs-function">(<span class="hljs-params">fn: () => <span class="hljs-keyword">void</span></span>) =></span> &#123;
    cleanup = runner.options.onStop = <span class="hljs-function">() =></span> &#123;
      callWithErrorHandling(fn, instance, ErrorCodes.WATCH_CLEANUP)
    &#125;
  &#125;
  
  <span class="hljs-keyword">let</span> oldValue = isArray(source) ? [] : INITIAL_WATCHER_VALUE

  <span class="hljs-keyword">const</span> applyCb = cb
    ? <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">if</span> (instance && instance.isUnmounted) &#123;
          <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-keyword">const</span> newValue = runner()
        <span class="hljs-keyword">if</span> (deep || hasChanged(newValue, oldValue)) &#123;
          <span class="hljs-keyword">if</span> (cleanup) &#123;
            cleanup()
          &#125;
          callWithAsyncErrorHandling(cb, instance, ErrorCodes.WATCH_CALLBACK, [
            newValue,
            oldValue === INITIAL_WATCHER_VALUE ? <span class="hljs-literal">undefined</span> : oldValue,
            onInvalidate
          ])
          oldValue = newValue
        &#125;
      &#125;
    : <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>
  <span class="hljs-comment">/* <span class="hljs-doctag">TODO:</span>  scheduler事件调度*/</span>
  <span class="hljs-keyword">let</span> scheduler: <span class="hljs-function">(<span class="hljs-params">job: () => any</span>) =></span> <span class="hljs-keyword">void</span>
  <span class="hljs-keyword">if</span> (flush === <span class="hljs-string">'sync'</span>) &#123; <span class="hljs-comment">/* 同步执行 */</span>
    scheduler = invoke
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (flush === <span class="hljs-string">'pre'</span>) &#123; <span class="hljs-comment">/* 在组件更新之前执行 */</span>
    scheduler = <span class="hljs-function"><span class="hljs-params">job</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (!instance || instance.isMounted) &#123;
        queueJob(job)
      &#125; <span class="hljs-keyword">else</span> &#123;
        job()
      &#125;
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;  <span class="hljs-comment">/* 正常情况 */</span>
    scheduler = <span class="hljs-function"><span class="hljs-params">job</span> =></span> queuePostRenderEffect(job, instance && instance.suspense)
  &#125;
  <span class="hljs-keyword">const</span> runner = effect(getter, &#123;
    <span class="hljs-attr">lazy</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">/* 此时 lazy 为true ,当前watchEffect不会立即执行 */</span>
    <span class="hljs-attr">computed</span>: <span class="hljs-literal">true</span>,
    onTrack,
    onTrigger,
    <span class="hljs-attr">scheduler</span>: applyCb ? <span class="hljs-function">() =></span> scheduler(applyCb) : scheduler
  &#125;)

  recordInstanceBoundEffect(runner)
  <span class="hljs-comment">/* 执行watcherEffect函数 */</span>
  <span class="hljs-keyword">if</span> (applyCb) &#123;
    <span class="hljs-keyword">if</span> (immediate) &#123;
      applyCb()
    &#125; <span class="hljs-keyword">else</span> &#123;
      oldValue = runner()
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    runner()
  &#125;
  <span class="hljs-comment">/* 返回函数 ，用终止当前的watchEffect */</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
    stop(runner)
    <span class="hljs-keyword">if</span> (instance) &#123;
      remove(instance.effects!, runner)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            