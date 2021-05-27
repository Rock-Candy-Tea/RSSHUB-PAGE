
---
title: 'Vue 3 学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ceb04bade85b42c4b31ca3410558abcf~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 26 May 2021 19:45:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ceb04bade85b42c4b31ca3410558abcf~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>Vue 3 的文档已经有<a href="https://v3.cn.vuejs.org/guide/introduction.html" target="_blank" rel="nofollow noopener noreferrer">中文版</a>，内容很详细，也有 Vue 2 迁移 Vue 3 的<a href="https://v3.cn.vuejs.org/guide/migration/introduction.html#%E6%A6%82%E8%A7%88" target="_blank" rel="nofollow noopener noreferrer">指南</a>。因此这里只记录下自己用到的部分新特性和自己的一些理解。</p>
</blockquote>
<h3 data-id="heading-0">Vue 3  数据响应式</h3>
<p>Vue 2 的数据响应式底层实现是 <code>Object.defineProperty()</code>,对于数组则是拦截了数组的七个方法。这种方式存在的问题是对于对象没有办法检测到属性的添加或删除。对于基于数组索引的变化也不能检测到。</p>
<p>Vue 3 的数据响应式基于 ES6 的 Proxy 实现的，和 Mobx 6 相同。解决了上面提到的问题</p>
<ul>
<li>Proxy 可以实现直接监听对象而非属性，所以对象的属性新增和删除也可以被监听</li>
<li>Proxy 可以直接监听数组的变化。因此数组直接修改下标对应的内容或长度也可以被监听</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> hero = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"赵云"</span>,
    <span class="hljs-attr">hp</span>: <span class="hljs-number">100</span>,
    <span class="hljs-attr">sp</span>: <span class="hljs-number">100</span>,
    <span class="hljs-attr">equipment</span>: [<span class="hljs-string">'马'</span>, <span class="hljs-string">'长枪'</span>]
&#125;
<span class="hljs-keyword">const</span> handler1 = &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, name, receiver</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.get(target, name, receiver)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, value, receiver</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`hero's <span class="hljs-subst">$&#123;key&#125;</span> change to <span class="hljs-subst">$&#123;value&#125;</span>`</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.set(target, key, value, receiver)
    &#125;
&#125;
<span class="hljs-keyword">const</span> handler2 = &#123;
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, key, value, receiver</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`equipment's <span class="hljs-subst">$&#123;key&#125;</span> change to <span class="hljs-subst">$&#123;value&#125;</span>`</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.set(target, key, value, receiver)
    &#125;
&#125;
<span class="hljs-keyword">const</span> heroProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(hero, handler1)
<span class="hljs-keyword">const</span> equipmentProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(heroProxy.equipment, handler2)
heroProxy.equipment = equipmentProxy
<span class="hljs-comment">//hero's equipment change to 马,长枪</span>
heroProxy.name = <span class="hljs-string">"张飞"</span>
<span class="hljs-comment">//hero's name change to 张飞</span>
heroProxy.equipment[<span class="hljs-number">2</span>] = <span class="hljs-string">"盔甲"</span>
<span class="hljs-comment">//equipment's 2 change to 盔甲</span>
heroProxy.level = <span class="hljs-number">100</span>
<span class="hljs-comment">//hero's level change to 100</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">Composition API</h3>
<p>主要目的是为了更方便的拆分，重用代码，Vue 2 如果要复用代码的话需要使用 mixin。官方有<a href="https://v3.cn.vuejs.org/guide/composition-api-introduction.html#%E4%BB%80%E4%B9%88%E6%98%AF%E7%BB%84%E5%90%88%E5%BC%8F-api" target="_blank" rel="nofollow noopener noreferrer">示例</a>，我感觉 Composition API 有点类似 React 的 自定义 Hooks。</p>
<h4 data-id="heading-2">setup</h4>
<p>在 setup 中没有 this，只能使用 props 和 context</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;toRefs&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span>&#123;
    <span class="hljs-comment">// const &#123;title&#125; = props </span>
    <span class="hljs-comment">// ES6 解构会消除 prop 的响应性，如果要解构要写成下面的样子</span>
    <span class="hljs-keyword">const</span> &#123;title&#125; = toRefs(props)
    <span class="hljs-built_in">console</span>.log(title.value)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>context 具有以下属性</p>
<ul>
<li>props</li>
<li>attrs</li>
<li>slots</li>
<li>emit</li>
</ul>
<h4 data-id="heading-3">生命周期钩子</h4>
<p>setup 的生命周期钩子基本就是在选项式 API 的基础上加上 <code>on</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span>&#123;
    onMounted(<span class="hljs-function">()=></span>&#123;
        ...
    &#125;)
&#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">ref 和 reactive</h4>
<p>ref 和 reactive 都用于为数据添加响应式状态，但是 reactive 只接受对象类型的参数。一般数据为对象的话使用 reactive,基本类型使用 ref。 在 JS 中使用 ref 对象的值要加上 <code>.value</code>，在 Template 中使用则不需要。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)
<span class="hljs-built_in">console</span>.log(count.value) <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">Provide / Inject</h4>
<p>跟 Vue 2 中的 Provide 和Inject 功能类似，可以用于组件间通信。可以将 provide 提供的数据变为 inject 的组件只读的。</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <MyMarker />
</template>
<script>
import &#123; provide, reactive, readonly, ref &#125; from 'vue'
import MyMarker from './MyMarker.vue

export default &#123;
  components: &#123;
    MyMarker
  &#125;,
  setup() &#123;
    const location = ref('North Pole')
    const geolocation = reactive(&#123;
      longitude: 90,
      latitude: 135
    &#125;)
    const updateLocation = () => &#123;
      location.value = 'South Pole'
    &#125;
    provide('location', readonly(location))
    provide('geolocation', readonly(geolocation))
    provide('updateLocation', updateLocation)
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">Teleport</h4>
<p>可以把元素移动到我们想要的位置</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">teleport</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"body"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        ...
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">teleport</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">v-model 用法的变更</h3>
<p>Vue 2 中的 v-model 相当于绑定 value prop 和 input 事件：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ChildComponent</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"pageTitle"</span>></span>
<span class="hljs-comment"><!--是以下的简写：--></span>
<span class="hljs-tag"><<span class="hljs-name">ChildComponent</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"pageTitle"</span> @<span class="hljs-attr">input</span>=<span class="hljs-string">"pageTitle = $event"</span>/></span>    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 Vue 3 中的 v-model 更像是.sync</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- Vue2 --></span>
<span class="hljs-tag"><<span class="hljs-name">ChildComponent</span> <span class="hljs-attr">:title.sync</span>=<span class="hljs-string">"pageTitle"</span>/></span>
<span class="hljs-comment"><!-- Vue3 --></span>
<span class="hljs-tag"><<span class="hljs-name">ChildComponent</span> <span class="hljs-attr">v-model:title</span>=<span class="hljs-string">"pageTitle"</span>/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">组件事件需要在 emits 选项中声明</h3>
<p>组件需要在 emits 中声明触发的事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">emits</span>:[<span class="hljs-string">'accept'</span>,<span class="hljs-string">'cancel'</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>否则控制台会有警告</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ceb04bade85b42c4b31ca3410558abcf~tplv-k3u1fbpfcp-zoom-1.image" alt="QQ图片20210520193758" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">watchEffect</h3>
<p>这个跟 MobX 的 autorun 非常像，它会立即执行传入的函数并响应式追踪其依赖，依赖变更久重新执行</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)
watchEffect(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(count.value))
<span class="hljs-comment">// -> logs 0</span>
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  count.value++
  <span class="hljs-comment">// -> logs 1</span>
&#125;, <span class="hljs-number">100</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">与 watch 的区别</h4>
<ul>
<li>watch 可以访问到侦听状态变化前后的值</li>
<li>watch 只有在侦听的源发生变化时才会执行回调</li>
<li>可以更具体的说明什么情况下回调函数执行</li>
</ul>
<h3 data-id="heading-11">v-for 中的 Ref</h3>
<p>ref 可以绑定一个函数，来确定要绑定的 Dom 元素</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"color-tabs-nav-item"</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(t,index) in titles"</span> <span class="hljs-attr">:ref</span>=<span class="hljs-string">"el => &#123; if (index === selectedIndex) this.selectedItem = el &#125;"</span>
   <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>&#123;&#123; t &#125;&#125;
 <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-12">参考</h3>
<ol>
<li><a href="https://zhuanlan.zhihu.com/p/60126477" target="_blank" rel="nofollow noopener noreferrer">深入实践 ES6 Proxy & Reflect</a></li>
<li><a href="https://v3.cn.vuejs.org/guide/reactivity.html#vue-%E5%A6%82%E4%BD%95%E8%BF%BD%E8%B8%AA%E5%8F%98%E5%8C%96" target="_blank" rel="nofollow noopener noreferrer">Vue 3 文档 - 深入响应式原理</a></li>
<li><a href="https://es6.ruanyifeng.com/#docs/reflect" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 6 入门</a></li>
<li><a href="https://juejin.cn/post/6908185323801575432" target="_blank">Vue 3.0 学习笔记</a></li>
</ol></div>  
</div>
            