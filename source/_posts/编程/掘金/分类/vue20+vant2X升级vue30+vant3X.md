
---
title: 'vue2.0+vant2.X升级vue3.0+vant3.X'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed9f91b7ee8b41499c299113f90a17cb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 02:00:13 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed9f91b7ee8b41499c299113f90a17cb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Vue3.0中你需要了解的变动</h2>
<h3 data-id="heading-1">关于vue3.0的生命周期</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed9f91b7ee8b41499c299113f90a17cb~tplv-k3u1fbpfcp-watermark.image" alt="3.0.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5783a1f8233d436eaebc66cf04f3e1d0~tplv-k3u1fbpfcp-watermark.image" alt="2.0.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>区别：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//创建实例</span>
<span class="hljs-number">1.</span> vue3创建一个实例对象
<span class="hljs-keyword">const</span> app =Vue.createApp(&#123;&#125;)

<span class="hljs-number">2.</span> vue2c创建一个实例对象
<span class="hljs-keyword">const</span> vm=<span class="hljs-keyword">new</span> Vue(&#123;&#125;)

<span class="hljs-comment">//实例对象插件的引入</span>
<span class="hljs-number">1.</span> vue3通过链式调用的方式导入插件
app.use(router).user(store).mount(<span class="hljs-string">'#app'</span>)

<span class="hljs-number">2.</span>vue2通过参数方式导入插件
<span class="hljs-keyword">new</span> Vue(&#123;
    router,
    store,
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">自定义指令、全局过滤器</h3>
<h4 data-id="heading-3">1. 过滤器</h4>
<pre><code class="hljs language-js copyable" lang="js">a. 局部
<span class="hljs-comment">//vue2局部过滤器</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; accountBalance | currencyUSD &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">filters</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">currencyUSD</span>(<span class="hljs-params">value</span>)</span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">'$'</span>+value
        &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="hljs-comment">//vue3局部过滤器改造</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;accountInUSD&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
   <span class="hljs-attr">computed</span>:&#123;
       <span class="hljs-function"><span class="hljs-title">accountInUSD</span>(<span class="hljs-params"></span>)</span>&#123;
           <span class="hljs-keyword">return</span> <span class="hljs-string">'$'</span>+<span class="hljs-built_in">this</span>.accountBalance
       &#125;
   &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
b.全局
<span class="hljs-comment">//vue2全局过滤器</span>
Vue.filter(<span class="hljs-string">'currencyUSD'</span>,<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'$'</span>+value
&#125;)
<span class="hljs-comment">//vue3全局过滤器(本质是在全局注册一个全局属性)</span>
app.config.globalProperties.$filters=&#123;
   <span class="hljs-function"><span class="hljs-title">accountInUSD</span>(<span class="hljs-params">value</span>)</span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'$'</span>+value
   &#125;
&#125;
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;$filters.accountInUSD(accountBalance)&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">2. 自定义指令</h4>
<p>vue2中的自定义指令的api
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08a0735b3cf147729ada97c67c2a6e93~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>vue3中的自定义指令api</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af58419bb24a4c0e95203c5754611b8b~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//2.0写法</span>
Vue.directive(<span class="hljs-string">'highlight'</span>, &#123;
  <span class="hljs-function"><span class="hljs-title">bind</span>(<span class="hljs-params">el, binding, vnode</span>)</span> &#123;
    el.style.background = binding.value
  &#125;
&#125;)
<span class="hljs-comment">//3.0写法</span>
app.directive(<span class="hljs-string">'highlight'</span>, &#123;
  <span class="hljs-function"><span class="hljs-title">beforeMount</span>(<span class="hljs-params">el, binding, vnode</span>)</span> &#123;
    el.style.background = binding.value
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">3. 全局组件</h4>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(component.name, component)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">组件</h3>
<h4 data-id="heading-7">1. 组件</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Farticle%2F1739937" target="_blank" rel="nofollow noopener noreferrer" title="https://cloud.tencent.com/developer/article/1739937" ref="nofollow noopener noreferrer">defineComponent的解析</a></p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-comment">// defineComponent 可以用于手动渲染函数、TSX 和 IDE 工具支持</span>
<span class="hljs-comment">// defineComponent以正确推断 setup() 组件的参数类型</span>
<span class="hljs-comment">// getCurrentInstance获取当前组件实例（注意其中的两个值ctx、proxy），可以获取父组件中的调用的状态</span>
<span class="hljs-comment">// ref 两种用法1.用于为基本数据类型添加响应式状态 2.表示模板应用</span>
<span class="hljs-comment">// reactive 用于为对象添加响应式状态 </span>
<span class="hljs-comment">//toRef用于为源响应式对象上的属性新建一个ref，从而保持对其源对象属性的响应式连接（父组件传递的props数据时，要引用props的某个属性且要保持响应式连接时就很有用）</span>
<span class="hljs-comment">//toRefs用于将响应式对象转换为结果对象，其中结果对象的每个属性都是指向原始对象相应属性的ref（1.将reactive中响应式数据转换成单个的ref,2.将props数据自动的转换ref）</span>
<span class="hljs-keyword">import</span> &#123; reactive,defineComponent,ref,getCurrentInstance,computed,onActivated,onBeforeMount,toRefs&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> &#123;useRoute&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> &#123; useStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'CommonListConent'</span>,
  <span class="hljs-attr">components</span>: &#123;[List.name]: List&#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">currentPage</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> <span class="hljs-number">1</span>,
    &#125;
  &#125;,
  <span class="hljs-comment">//setup第二个参数的使用&#123;attrs,slots,emit&#125;</span>
  <span class="hljs-comment">//attrs可以拿到父组件上面引用时写在上面值</span>
  <span class="hljs-comment">//<searchInput  name='123231'  /></span>
  <span class="hljs-comment">//slots可以拿到父组件传过来的插槽</span>
  <span class="hljs-comment">//<template></span>
  <span class="hljs-comment">//<van-search @update:model-value="searchValue" v-model.trim="search" shape="round" :placeholder="placeholder"></span>
    <span class="hljs-comment">//<template v-slot:[item] v-for="(item, index) in name" :key="index"></span>
      <span class="hljs-comment">//<slot :name="item"></slot></span>
    <span class="hljs-comment">//</template></span>
  <span class="hljs-comment">//</van-search></span>
<span class="hljs-comment">//</template></span>
<span class="hljs-comment">//const name=Object.keys(slots)</span>
  
  
  
  
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props,&#123;emit&#125;</span>)</span> &#123;
    <span class="hljs-keyword">const</span> instance = getCurrentInstance().proxy
    <span class="hljs-keyword">const</span> route=useRoute()
    <span class="hljs-keyword">const</span> state = reactive(&#123;
      <span class="hljs-attr">onFinished</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">onLoading</span>: <span class="hljs-literal">false</span>,
    &#125;);
    <span class="hljs-keyword">const</span> root = ref(<span class="hljs-literal">null</span>)
    <span class="hljs-keyword">const</span> store = useStore();
    <span class="hljs-keyword">const</span> getScrollTop=computed(<span class="hljs-function">()=></span>store.getters[<span class="hljs-string">'homeIndex/getScrollTop'</span>])
    onActivated(<span class="hljs-function">()=></span>&#123;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Reflect</span>.has(getScrollTop.value, route.path))&#123;
        root.value.$el.scrollTop = getScrollTop.value[route.path]
      &#125;
    &#125;)
    <span class="hljs-keyword">const</span> onRefresh=<span class="hljs-function">()=></span>&#123;
      state.freshLoading = <span class="hljs-literal">true</span>;
      emit(<span class="hljs-string">'onRefresh'</span>);
    &#125;,
    <span class="hljs-keyword">const</span> onLoadDisabled=computed(<span class="hljs-function">()=></span>&#123;
      <span class="hljs-keyword">return</span> !instance.onLoad
    &#125;)
    <span class="hljs-keyword">const</span> onRefreshDisabled=computed(<span class="hljs-function">()=></span>&#123;
      <span class="hljs-keyword">return</span> !instance.onRefresh
    &#125;)
    onBeforeMount(<span class="hljs-function">()=></span>&#123;
      state.onFinished = onLoadDisabled.value
    &#125;)
    <span class="hljs-keyword">return</span>&#123;
      ...toRefs(state),
      onRefreshDisabled,
      root,
    &#125;
  &#125;,
  <span class="hljs-attr">emits</span>: [<span class="hljs-string">'onRefresh'</span>,<span class="hljs-string">'onLoad'</span>],
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">2. 函数式组件</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Vue 2 函数式组件</span>
<template functional>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">component</span>
    <span class="hljs-attr">:is</span>=<span class="hljs-string">"`h$&#123;props.level&#125;`"</span>
    <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"attrs"</span>
    <span class="hljs-attr">v-on</span>=<span class="hljs-string">"listeners"</span>
  /></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'level'</span>]
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="hljs-comment">//vue3函数式组件</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">component</span>
    <span class="hljs-attr">v-bind:is</span>=<span class="hljs-string">"`h$&#123;$props.level&#125;`"</span>
    <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"$attrs"</span>
  /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'level'</span>]
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="hljs-comment">//使用$props这样的方式将值呈现在视图上时，不管props中的值是否改变，视图显示值都是最初的方式</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">vue3中的ref使用</h3>
<h4 data-id="heading-10">1.使用</h4>
<pre><code class="hljs language-js copyable" lang="js"><template> 
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"root"</span>></span>This is a root element<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="hljs-keyword">const</span> root = ref(<span class="hljs-literal">null</span>)<span class="hljs-comment">//声明的名要和上面的ref中的名相同，DOM元素将在初始化后分配给ref</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">2. v-for中的用法</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">2.0</span>写法
 <van-checkbox :name=<span class="hljs-string">"res"</span> :ref=<span class="hljs-string">"`checkboxes$&#123;elemIndex&#125;$&#123;index&#125;`"</span> icon-size=<span class="hljs-string">"16px"</span> />
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"res.imgUrl ? res.imgUrl : require('@/assets/images/shopLogo.png')"</span> <span class="hljs-attr">alt</span> /></span>
 <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
 <span class="hljs-number">3.0</span>写法
  <van-checkbox :name=<span class="hljs-string">"res"</span> :ref=<span class="hljs-string">"el=>&#123;if(el) setCheckboxes(el,`$&#123;elemIndex&#125;$&#123;index&#125;`,resIndex)&#125;"</span> @click.stop icon-size=<span class="hljs-string">"16px"</span> />
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"res.imgUrl ? res.imgUrl : require('@/assets/images/shopLogo.png').default"</span> <span class="hljs-attr">alt</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/faae0013404d430e885d48ee2aa85390~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">vue3.0中的插件（vueX vueRouter）</h3>
<h4 data-id="heading-13">1. vuex</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//2.0写法</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">import</span> createPersistedState <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex-persistedstate'</span>
<span class="hljs-keyword">import</span> modules <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>

Vue.use(Vuex)
<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">plugins</span>: [createPersistedState(&#123;
    <span class="hljs-attr">storage</span>: <span class="hljs-built_in">window</span>.sessionStorage
  &#125;)],
  modules
&#125;)

<span class="hljs-comment">//3.0写法</span>
<span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>;
<span class="hljs-keyword">import</span> createPersistedState <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex-persistedstate'</span>;
<span class="hljs-keyword">import</span> modules <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(&#123;
  <span class="hljs-attr">plugins</span>: [createPersistedState(&#123;
    <span class="hljs-attr">storage</span>: <span class="hljs-built_in">window</span>.sessionStorage,
  &#125;)],
  modules,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">2. vuerouter</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//2.0用法</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> routes <span class="hljs-keyword">from</span> <span class="hljs-string">'./routes'</span>
Vue.use(Router)
<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> Router(&#123;
  routes
&#125;)
router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
&#125;)
router.afterEach(<span class="hljs-function">() =></span> &#123;
&#125;)
<span class="hljs-comment">//3.0用法</span>
<span class="hljs-keyword">import</span> &#123; createRouter, createWebHashHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>;
<span class="hljs-keyword">import</span> routes <span class="hljs-keyword">from</span> <span class="hljs-string">'./routes'</span>
<span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-attr">history</span>: createWebHashHistory(),
  routes,
&#125;);
router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
&#125;)
router.afterEach(<span class="hljs-function">() =></span> &#123;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">使用v-bind.sync(对某一个 prop 进行“双向绑定”)</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//2.0写法</span>
<span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'update:title'</span>, newValue)
<span class="hljs-comment">//<ChildComponent :title="pageTitle" @update:title="pageTitle = $event" /></span>
<ChildComponent :title.sync=<span class="hljs-string">"pageTitle"</span> />
<span class="hljs-comment">//3.0写法</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ChildComponent</span> <span class="hljs-attr">v-model:title</span>=<span class="hljs-string">"pageTitle"</span> /></span></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            