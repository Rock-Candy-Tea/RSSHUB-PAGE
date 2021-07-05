
---
title: 'Vue3新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5654815d6f74415b81cd9b8d93fe40e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 21 Sep 2020 23:23:57 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5654815d6f74415b81cd9b8d93fe40e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">vue3的六大亮点</h2>
<ol>
<li>Performance: 性能比vue2.x快1.2-2倍</li>
<li>Tree shaking support: 按需编译，体积比vue2更小</li>
<li>Composition API: 组合api(类似于react hooks)</li>
<li>Better Typescript: 更好的ts的支持</li>
<li>Custom Renderer api: 暴露了自定义的api</li>
<li>Fragment Teleport(Protal) ,suspense: 更先进的组件</li>
</ol>
<h2 data-id="heading-1">vue3是如何变化更快的</h2>
<h3 data-id="heading-2">diff算法的优化</h3>
<p>vue2中的diff算法
vue2.x中的虚拟dom是进行全量的对比,例如</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5654815d6f74415b81cd9b8d93fe40e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
vue2的在线编译   <a href="https://vue-template-explorer.netlify.app/" target="_blank" rel="nofollow noopener noreferrer">vue-template-explorer.netlify.app/</a></p>
<pre><code class="copyable">function render() &#123;
  with(this) &#123;
    return _c('div', [_c('p', [_v("hello world ")]), _c('p', [_v(_s(msg) +
      " ")])])
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vue3中的diff算法，只会给需要动态改变的标签会打上一个flag,这样就减少了diff算法的比对次数</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fa3a54995574efb804eb566ac98c5be~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
vue3的在线编译 <a href="https://vue-next-template-explorer.netlify.app/" target="_blank" rel="nofollow noopener noreferrer">vue-next-template-explorer.netlify.app/</a></p>
<pre><code class="copyable">import &#123; createVNode as _createVNode, toDisplayString as _toDisplayString, openBlock as _openBlock, createBlock as _createBlock &#125; from "vue"

export function render(_ctx, _cache, $props, $setup, $data, $options) &#123;
  return (_openBlock(), _createBlock("div", null, [
    _createVNode("p", null, "hello world "),
    _createVNode("p", null, _toDisplayString(_ctx.msg), 1 /* TEXT */)
  ]))
&#125;

// Check the console for the AST
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么这个flag为1是什么意思呢</p>
<pre><code class="copyable">TEXT = 1 // 动态文本节点
CLASS=1<<1,1 // 2//动态class
STYLE=1<<2，// 4 //动态style
PROPS=1<<3,// 8 //动态属性，但不包含类名和样式
FULLPR0PS=1<<4,// 16 //具有动态key属性，当key改变时，需要进行完整的diff比较。
HYDRATE_ EVENTS = 1 << 5，// 32 //带有监听事件的节点
STABLE FRAGMENT = 1 << 6, // 64 //一个不会改变子节点顺序的fragment
KEYED_ FRAGMENT = 1 << 7, // 128 //带有key属性的fragment 或部分子字节有key
UNKEYED FRAGMENT = 1<< 8, // 256 //子节点没有key 的fragment
NEED PATCH = 1 << 9, // 512 //一个节点只会进行非props比较
DYNAMIC_SLOTS = 1 << 10 // 1024 // 动态slot
HOISTED = -1 // 静态节点
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">静态提升（hoistStatic）</h3>
<p>Vue2.x中虚拟dom每次都会重新创建，进行比对渲染
Vue3.0中对不参与更新的元素，会做静态提升，只会被创建一次，在渲染时直接复用即可
未被提升前</p>
<pre><code class="copyable">import &#123; createVNode as _createVNode, toDisplayString as _toDisplayString, openBlock as _openBlock, createBlock as _createBlock &#125; from "vue"

export function render(_ctx, _cache, $props, $setup, $data, $options) &#123;
  return (_openBlock(), _createBlock("div", null, [
    _createVNode("p", null, "hello world "),
    _createVNode("p", null, "hello "),
    _createVNode("p", null, _toDisplayString(_ctx.msg), 1 /* TEXT */)
  ]))
&#125;

// Check the console for the AST
<span class="copy-code-btn">复制代码</span></code></pre>
<p>被提升后</p>
<pre><code class="copyable">import &#123; createVNode as _createVNode, toDisplayString as _toDisplayString, openBlock as _openBlock, createBlock as _createBlock &#125; from "vue"

const _hoisted_1 = /*#__PURE__*/_createVNode("p", null, "hello world ", -1 /* HOISTED */)
const _hoisted_2 = /*#__PURE__*/_createVNode("p", null, "hello ", -1 /* HOISTED */)

export function render(_ctx, _cache, $props, $setup, $data, $options) &#123;
  return (_openBlock(), _createBlock("div", null, [
    _hoisted_1,
    _hoisted_2,
    _createVNode("p", null, _toDisplayString(_ctx.msg), 1 /* TEXT */)
  ]))
&#125;

// Check the console for the AST
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">事件侦听器缓存</h3>
<p>在vue2中，在元素身上绑定事件后，因为事件是动态变化的，所以会认为dom发生了变化</p>
<pre><code class="copyable">import &#123; toDisplayString as _toDisplayString, createVNode as _createVNode, openBlock as _openBlock, createBlock as _createBlock &#125; from "vue"

export function render(_ctx, _cache, $props, $setup, $data, $options) &#123;
  return (_openBlock(), _createBlock("div", &#123; onClick: _ctx.handleClick &#125;, _toDisplayString(_ctx.msg), 9 /* TEXT, PROPS */, ["onClick"]))
&#125;

// Check the console for the AST
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而在vue3中。会默认给事件加上缓存</p>
<pre><code class="copyable">import &#123; toDisplayString, createVNode, openBlock, createBlock, withScopeId &#125; from "vue"

// Binding optimization for webpack code-split
const _toDisplayString = toDisplayString, _createVNode = createVNode, _openBlock = openBlock, _createBlock = createBlock, _withScopeId = withScopeId
const _withId = /*#__PURE__*/_withScopeId("scope-id")

export const render = /*#__PURE__*/_withId(function render(_ctx, _cache, $props, $setup, $data, $options) &#123;
  return (_openBlock(), _createBlock("div", &#123;
    onClick: _cache[1] || (_cache[1] = (...args) => (_ctx.handleClick(...args)))
  &#125;, _toDisplayString(_ctx.msg), 1 /* TEXT */))
&#125;)

// Check the console for the AST
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">vue3 项目初始化</h2>
<ol>
<li>方法一：利用vite</li>
</ol>
<pre><code class="copyable">npm init vite-app hello-vue3   (# OR yarn create vite-app hello-vue3)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>方法二：利用vue-cli</li>
</ol>
<pre><code class="copyable">npm install -g @vue/cli (# OR yarn global add @vue/cli)
vue create hello-vue3
# select vue 3 preset
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Composition API</h2>
<h3 data-id="heading-7">setup</h3>
<p>setup 函数是一个新的组件选项。它作为在组件内部使用组合 API 的入口点。<br>
调用时间:在创建组件实例时，在初始 prop 解析之后立即调用 setup。在生命周期方面，它是在 beforeCreate 钩子之前调用的。
其他可以参考官方文档（比如setup里面的两个参数）</p>
<h3 data-id="heading-8">ref</h3>
<p>在vue2中只需要在data里定义数据，就可以实现数据层-视图层的双向绑定，而在vue3中使用ref接受一个内部值并返回一个响应式且可变的 ref 对象。ref 对象具有指向内部值的单个 property.value
例如：</p>
<pre><code class="copyable"><template>
 <div>
   &#123;&#123;num&#125;&#125;
 </div>
 <button @click="handleAdd">按钮</button>
</template>
<script>
import &#123; ref &#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
    let num = ref(0)
    function handleAdd() &#123;
      num.value= 2  
      // num = 2  这种写法是错误的。因为ref把里面的数据包装成了一个对象，但是在template中不需要.value vue会根据__v_isRef进行处理
    &#125;
    console.log(num) 
   /*&#123; __v_isRef: true
   _rawValue: 0
   _shallow: false
   _value: 2
   value: 2
   &#125;
   */
    return &#123;num,handleAdd&#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">reactive</h3>
<p>reactive的作用和ref的作用是类似的，都是将数据变成可相应的对象，其实ref的底层其实利用了reactive。
两者的区别，ref包装的对象需要.value ,而reactive中的不需要</p>
<pre><code class="copyable"><template>
 <div>
   &#123;&#123;num.person.name&#125;&#125;----&#123;&#123;num.person.age&#125;&#125;
 </div>
 <button @click="handleAdd">按钮</button> 
</template>
<script>
import &#123; ref,reactive &#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
    let num = reactive(&#123;
      person:&#123;
        name:'yj',
        age:18,
        
      &#125;
    &#125;)
    function handleAdd() &#123;
       num.person.age = num.person.age+1  
    &#125;
    return &#123;num,handleAdd&#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">shallowRef 和 triggerRef</h3>
<p>创建一个 ref，它跟踪自己的 .value 更改，但不会使其值成为响应式的。
使用trigger主动出发视图更新</p>
<pre><code class="copyable"><template>
 <div>
   &#123;&#123;num.person.name&#125;&#125;----&#123;&#123;num.person.age&#125;&#125;---&#123;&#123;num.person.origin.aa.gf&#125;&#125;---&#123;&#123;num.a&#125;&#125;
 </div>
 <button @click="handleAdd">按钮</button>
</template>

<script>
import &#123; shallowRef, triggerRef &#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
    let num = shallowRef(&#123;
      a:1,
      person:&#123;
        name:'yj',
        age:18,
        origin:&#123;
          aa:&#123;
            gf:"bb"
          &#125;
        &#125;
      &#125;
    &#125;)
    function handleAdd() &#123;
       num.value.a = 2
       triggerRef(num)
    &#125;
    return &#123;num,handleAdd&#125;
    
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">shallowReactive</h3>
<p>shallowReactive 只监听第一层值的变化，深层次的不监听(值会发生改变，但是视图不更新)</p>
<pre><code class="copyable"><template>
 <div>
   &#123;&#123;num.person.name&#125;&#125;----&#123;&#123;num.person.age&#125;&#125;---&#123;&#123;num.person.origin.aa.gf&#125;&#125;---&#123;&#123;num.a&#125;&#125;
 </div>
 <button @click="handleAdd">按钮</button>
</template>

<script>
import &#123; shallowReactive &#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
    let num = shallowReactive(&#123;
      a:1,
      person:&#123;
        name:'yj',
        age:18,
        origin:&#123;
          aa:&#123;
            gf:"bb"
          &#125;
        &#125;
      &#125;
    &#125;)
    function handleAdd() &#123;
       num.a++  
    &#125;
    return &#123;num,handleAdd&#125;
  &#125;
&#125;
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">toRaw</h3>
<p>返回 reactive 或 readonly 代理的原始对象。这是一个转义口，可用于临时读取而不会引起代理访问/跟踪开销，也可用于写入而不会触发更改。不建议保留对原始对象的持久引用。请谨慎使用。</p>
<pre><code class="copyable"><template>
 <div>
  &#123;&#123;num&#125;&#125;
 </div>
 <button @click="handleAdd">按钮</button>
</template>

<script>
import &#123; reactive,toRaw &#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
    let obj =&#123;
      a:1,
      b:2,
      c:3
    &#125;
    let num = reactive(obj)
    let obj1 = toRaw(num)   // 暴露出原对象
    console.log(obj1===obj)  //  true  
    function handleAdd() &#123;
     // num 这里是对obj进行了地址引用，但是改变obj的值，并不会出发视图更新
      obj.a = '222233' 
      console.log(num)
    &#125;

    return &#123;num,handleAdd&#125;
    
  &#125;
&#125;
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><template>
 <div>
  &#123;&#123;num.a&#125;&#125;
 </div>
 <button @click="handleAdd">按钮</button>
</template>

<script>
import &#123; ref,toRaw &#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
    let obj =&#123;
      a:1,
      b:2,
      c:3
    &#125;
    let num = ref(obj)
    let obj1 = toRaw(num.value)
    console.log(obj1===obj)
    function handleAdd() &#123;
        obj1.a = '22233333'
        console.log(num)
      // obj.a = '222233' 
      // console.log(num)
    &#125;
    return &#123;num,handleAdd&#125;
    
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">markRaw</h3>
<p>标记一个对象，使其永远不会转换为代理。返回对象本身。</p>
<pre><code class="copyable"><template>
 <div>
  &#123;&#123;num&#125;&#125;
 </div>
 <button @click="handleAdd">按钮</button>
</template>

<script>
import &#123; markRaw, reactive,toRaw &#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
    let obj =&#123;
      a:1,
      b:2,
      c:3
    &#125;
    let obj1 = markRaw(obj)
    let num = reactive(obj1)
    function handleAdd() &#123;
        num.a = '2222'
        console.log(num)
    &#125;
    return &#123;num,handleAdd&#125;
    
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><template>
 <div>
  &#123;&#123;num&#125;&#125;
 </div>
 <button @click="handleAdd">按钮</button>
</template>

<script>
import &#123; markRaw, ref, &#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
    let obj =&#123;
      a:1,
      b:2,
      c:3
    &#125;
    let obj1 = markRaw(obj)
    let num = ref(obj1)
    function handleAdd() &#123;
        num.value.a = '2222'
        console.log(num.value)
    &#125;
    return &#123;num,handleAdd&#125;
    
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">toRef</h3>
<p>如果利用toRef将一个数据变成响应式数据，是会影响到原始数据，但是响应式数据通过toRef。并不回出发ui界面更新(ref式改变，不会影响到原始数据)</p>
<pre><code class="copyable"><template>
 <div>
  &#123;&#123;state&#125;&#125;
 </div>
 <button @click="handleAdd">按钮</button>
</template>

<script>
import &#123; ref, toRef &#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
    let obj =&#123;
      a:1,
      b:2,
      c:3
    &#125;
    // let state = ref(obj.a)
    let state = toRef(obj,'a')
     console.log(state)
    function handleAdd() &#123;
      // 修改响应式数据，并不回改变原始数据
       state.value= "2222222"
       console.log(state)  
       console.log(obj) 

      // 如果利用toref将一个数据变成响应式数据，是会影响到原始数据，但是响应式数据通过toref。并不回出发ui界面更新
    &#125;
    return &#123;state,handleAdd&#125;
    
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">toRefs</h3>
<p>类似toRef,只是一次性处理多次toRef</p>
<pre><code class="copyable"><template>
 <div>
  &#123;&#123;num.a&#125;&#125;
 </div>
 <button @click="handleAdd">按钮</button>
</template>

<script>
import &#123; toRefs,toRaw &#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
    let obj =&#123;
      a:1,
      b:2,
      c:3
    &#125;
    let num = toRefs(obj)
  
    function handleAdd() &#123;
       num.a.value="1111"
       num.b.value="222"
       num.c.value="3333"
       console.log(obj)
    &#125;

    return &#123;num,handleAdd&#125;
    
  &#125;
&#125;
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">customRef</h3>
<p>创建一个自定义的 ref，并对其依赖项跟踪和更新触发进行显式控制。它需要一个工厂函数，该函数接收 track 和 trigger 函数作为参数，并应返回一个带有 get 和 set 的对象。</p>
<pre><code class="copyable"><template>
 <div>
   &#123;&#123;msg&#125;&#125;
 </div>
 <ul>
   <li v-for="(item,index) in state" :key="index">&#123;&#123;item.name&#125;&#125;----&#123;&#123;item.age&#125;&#125;</li>
 </ul>
 <button @click="handleAdd">按钮</button>
</template>

<script>
import &#123; customRef,ref&#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
  let state = getData('../public/ab.json',[])
  console.log(state)
  let msg = initState(5) 
  function  handleAdd()&#123;
    msg.value ++
   &#125; 
   return &#123;msg,handleAdd,state&#125;
  &#125;
&#125;

function getData(url,value)&#123;
  return customRef((track,trigger) => &#123;
    fetch(url).then(res=>&#123;
     return res.json()
    &#125;).then(data=>&#123;
     value = data.data
     trigger()
    &#125;)
     return &#123;
       get() &#123;
         track()
         return value
       &#125;,
       set(newValue) &#123;
         value = newValue
         trigger()  // 出发视图更新
       &#125;
     &#125;
   &#125;)
&#125;

function initState(value) &#123;
  return customRef((track,trigger) => &#123;
     return &#123;
       get() &#123;
         track()
         return value
       &#125;,
       set(newValue) &#123;
         value = newValue
         trigger()  // 出发视图更新
       &#125;
     &#125;
   &#125;)
   &#125; 
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">ref 获取dom</h3>
<pre><code class="copyable">
<template>
 <div ref="box">
  我是div
 </div>
</template>

<script>
import &#123;onMounted, ref&#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
      onMounted(()=>&#123;
         console.log(box.value)
      &#125;)
     let box = ref(null)
     console.log(box.value)
  
    return &#123;box&#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">readonly,shallowReadonly,isReadonly</h3>
<pre><code class="copyable"><template>
 <div>
  &#123;&#123;state.list.b.b1&#125;&#125;
  <button @click="handleAdd">按钮</button>
 </div>

</template>

<script>
import &#123; readonly,shallowReadonly,isReadonly &#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
    // let state = readonly(&#123;
    //   list:&#123;
    //     a:'1111',
    //     b:&#123;
    //       b1:"2222",
    //       c:&#123;
    //         c2:"3333"
    //       &#125;
    //     &#125;
    //   &#125;
    // &#125;)
    let state = shallowReadonly(&#123;
      list:&#123;
        a:'1111',
        b:&#123;
          b1:"2222",
          c:&#123;
            c2:"3333"
          &#125;
        &#125;
      &#125;
    &#125;)
    function handleAdd() &#123;
      state.list= '3333333333'
         console.log(state)
    &#125;
    return &#123;state,handleAdd&#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">实现自己的_shallowreactive _shallowref</h3>
<pre><code class="copyable"><template>
 <div>
  &#123;&#123;state.name&#125;&#125;
  <button @click="handleAdd">按钮</button>
 </div>

</template>

<script>

export default &#123;
  name: 'App',
  setup() &#123;
    let obj = &#123;
      name:"1111",
      age:19,
      info:&#123;
        bb:"55555"
      &#125;
    &#125;
    // let state = _shallowreactive(obj)
    // function  handleAdd()&#123;
    //   state.name ='fghhrt'
    //   state.info.bb ='bdfgsfsd'
    // &#125;
     let state = _shallowref(obj)
    function  handleAdd()&#123;
     state.value = '222'
    &#125;
    return &#123;state,handleAdd&#125;
  &#125;
&#125;

function _shallowreactive(obj)&#123;
  return new Proxy(obj,&#123;
    get(obj,prop)&#123;
      return obj[prop]
    &#125;,
    set(obj,prop,value)&#123;
        obj[prop] = value 
        console.log("更新ui界面")
        console.log(obj)
        return true
    &#125;
  &#125;)
&#125;

function _shallowref(val) &#123;
  return  _shallowreactive(&#123;value:val&#125;)
&#125;
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">实现自己的_reactive</h3>
<pre><code class="copyable"><template>
 <div>
  &#123;&#123;state.name&#125;&#125;
  <button @click="handleAdd">按钮</button>
 </div>

</template>

<script>

export default &#123;
  name: 'App',
  setup() &#123;
    let obj = &#123;
      name:"1111",
      age:19,
      info:&#123;
        bb:"55555"
      &#125;
    &#125;
    let state = _reactive(obj)
    function  handleAdd()&#123;
      state.name = '444444'
     state.info.bb = '222'
    &#125;
    return &#123;state,handleAdd&#125;
  &#125;
&#125;

function _reactive(obj)&#123;
   if(typeof obj === 'object')&#123;
     if(obj instanceof Array)&#123;
      //  如果是数组，取出遍历
       obj.forEach((item,index)=>&#123;
        //   如果数组里面的值是还是对此安好
         if(typeof item === 'object')&#123;
           obj[index] = _reactive(item)
         &#125;
       &#125;)
     &#125;else&#123;
       // 如果是对象
       for(let key in obj)&#123;
         let item = obj[key]
          if(typeof item === 'object')&#123;
           obj[key] = _reactive(item)
         &#125;
       &#125;
     &#125;

   &#125;else&#123;
     console.warn("不是对象")
   &#125;
  return new Proxy(obj,&#123;
    get(obj,prop)&#123;
      return obj[prop]
    &#125;,
    set(obj,prop,value)&#123;
        obj[prop] = value 
        console.log("更新ui界面")
        console.log(obj)
        return true
    &#125;
  &#125;)
&#125;

</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">实现自己的_shallowReadonly</h3>
<pre><code class="copyable"><template>
 <div>
  <!-- &#123;&#123;state.name&#125;&#125; -->
  <button @click="handleAdd">按钮</button>
 </div>

</template>

<script>

export default &#123;
  name: 'App',
  setup() &#123;
    let obj = &#123;
      name:"1111",
      age:19,
      info:&#123;
        bb:"55555"
      &#125;
    &#125;
  
     let state = _shallowReadonly(obj)
    function  handleAdd()&#123;
     state.name = '222'
    //  state.info.bb = '123123'
    &#125;
    return &#123;state,handleAdd&#125;
  &#125;
&#125;

function _shallowReadonly(obj)&#123;
  return new Proxy(obj,&#123;
    get(obj,prop)&#123;
      return obj[prop]
    &#125;,
    set(obj,prop,value)&#123;
      console.warn("不能修改")
      return true
        // obj[prop] = value 
        // console.log("更新ui界面")
        // console.log(obj)
        // return true
    &#125;
  &#125;)
&#125;

</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">Teleport</h2>
<p>有时组件模板的一部分逻辑上属于该组件，而从技术角度来看，最好将模板的这一部分移动到 DOM 中 Vue app 之外的其他位置
最常见的就是类似于element的dialog组件 dialog是fixed定位，而dialog父元素的css会影响dialog。因此要将dialog放在body下</p>
<pre><code class="copyable"><teleport to="body">
  <div class="modal__mask">
    <div class="modal__main">
      <div class="modal__header">
        <h3 class="modal__title">弹窗标题</h3>
        <span class="modal__close">x</span>
      </div>
      <div class="modal__content">
        弹窗文本内容
      </div>
      <div class="modal__footer">
        <button>取消</button>
        <button>确认</button>
      </div>
    </div>
  </div>
</teleport>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在同一目标上使用多个 teleport
一个常见的用例场景是一个可重用的  组件，它可能同时有多个实例处于活动状态。对于这种情况，多个  组件可以将其内容挂载到同一个目标元素。顺序将是一个简单的追加——稍后挂载将位于目标元素中较早的挂载之后。</p>
<pre><code class="copyable"><teleport to="#modals">
  <div>A</div>
</teleport>
<teleport to="#modals">
  <div>B</div>
</teleport>

<!-- result-->
<div id="modals">
  <div>A</div>
  <div>B</div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">Suspense</h2>
<p>前端开发中异步请求是非常常见的事情,比如远程读取图片,调用后端接口等等
Suspense是有两个template插槽的，第一个default代表异步请求完成后，显示的模板内容。fallback代表在加载中时，显示的模板内容。
子组件 child</p>
<pre><code class="copyable"><template>
  <h1>&#123;&#123;result&#125;&#125;</h1>
</template>
<script>
import &#123; defineComponent &#125; from 'vue'
export default defineComponent(&#123;
  setup() &#123;
    return new Promise((resolve) => &#123;
      setTimeout(() => &#123;
        return resolve(&#123;
          result: 1000
        &#125;)
      &#125;, 5000)
    &#125;)
  &#125;
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件
当异步没有执行完的时候。使用fallback里面的组件，当执行成功之后使用default</p>
<pre><code class="copyable"><Suspense>
  <template #default>
    <Child />
  </template>
  <template #fallback>
    <h1>Loading !...</h1>
  </template>
</Suspense>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">处理异步中的错误</h4>
<p>在vue3.x的版本中，可以使用onErrorCaptured这个钩子函数来捕获异常。
当上面的异步发生错误的时候，onErrorCaptured 会捕获错误</p>
<pre><code class="copyable">const app = &#123;
  name: "App",
  components: &#123; Child&#125;,
  setup() &#123;
    onErrorCaptured((error) => &#123;
      return true  
    &#125;)
    return &#123;&#125;;
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">Fragment</h2>
<p>在vue2中,我们创建一个组件，他只有有一个根节点</p>
<pre><code class="copyable"><template>
  <div>
    <div>hello</div>
    <div>world</div>
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么vue2需要这样写，为了底层diff算法
在vue3中可以不用这样写</p>
<pre><code class="copyable"><template>
    <div>hello</div>
    <div>world</div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vue3中默认创建了一个Fragment,尽管Fragment看起来像一个普通的DOM元素，但它是虚拟的，根本不会在DOM树中呈现。这样我们可以将组件功能绑定到一个单一的元素中，而不需要创建一个多余的DOM节点。</p>
<h2 data-id="heading-26">Emits</h2>
<p>Vue 3 目前提供一个 emits 选项，和现有的 props 选项类似。这个选项可以用来定义组件可以向其父组件触发的事件。</p>
<p>在vue2中</p>
<ol>
<li>当emits为数组的时候</li>
</ol>
<p>emits默认要写上，否则当自定义事件和原生事件重名的时候，事件会默认被调用两次</p>
<pre><code class="copyable"><template>
  <div>
    <p>&#123;&#123; text &#125;&#125;</p>
    <button v-on:click="$emit('accepted')">OK</button>
  </div>
</template>
<script>
  export default &#123;
    props: ['text']
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue3中</p>
<pre><code class="copyable"><template>
  <div>
    <p>&#123;&#123; text &#125;&#125;</p>
    <button v-on:click="$emit('accepted')">OK</button>
  </div>
</template>
<script>
  export default &#123;
    props: ['text'],
    emits: ['accepted']
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>当emits为object的时候，可以对emit进行校验。只有符合条件的才会被触发</li>
</ol>
<pre><code class="copyable"><template>
  <div>
    <button @click="handleClick">按钮</button>
  </div>
</template>

<script>

export default&#123;
    emits: &#123;'click':(type)=>&#123;
      return type===1
    &#125;&#125;,
  setup() &#123;
    
  &#125;,
  methods:&#123;
    handleClick() &#123;
      this.$emit('click',1)
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">v-model</h2>
<h4 data-id="heading-28">在vue2中使用v-model，一般我们会写成这样</h4>
<pre><code class="copyable"><div id="app">
     <input v-model="price">
 </div>
<script>
    new Vue(&#123;
        el: '#app',
        data: &#123;
            price: ''
        &#125;
    &#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实v-model只是一个语法糖,内部实现是这样</p>
<pre><code class="copyable"><input type="text" :value="price" @input="price=$event.target.value">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue中父子组件传值的方法</p>
<h6 data-id="heading-29">方法一</h6>
<pre><code class="copyable">父组件
<template>
    <div>
        <!--在子组件中用emit("test")传达给父组件的getData方法中-->
        <child @test="getData" :keywords="keywords"></child>
        <button @click="submit">提交</button>
    </div>
</template>
<script>
import child from './child.vue'
export default &#123;
    data() &#123;
        return &#123;
            keywords: '123143'
        &#125;
    &#125;,
    components: &#123;
        child
    &#125;,
    methods: &#123;
        // 在这里实现更改父组件的值
        getData(val)&#123;
            this.keywords = val
        &#125;,
        submit() &#123;
            console.log('keywords:', this.keywords)
        &#125;
    &#125;
&#125;
</script>
子组件
<template>
    <div>
        <input @input="inputChange" type="text" :value="keywords">
    </div>
</template>
<script>
export default &#123;
    props: ['keywords'],
    methods: &#123;
        inputChange(e) &#123;
          // 传给父元素的test函数
            this.$emit('test', e.target.value)
        &#125;
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种办法一相对麻烦一点，需要定义在父组件中也要定义一个事件</p>
<h6 data-id="heading-30">方法二  v-model</h6>
<p>一个组件上的 v-model 默认会利用名为 value 的 prop 和名为 input 的事件，但是像单选框、复选框等类型的输入控件可能会将 value attribute 用于不同的目的。model 选项可以用来避免这样的冲突：</p>
<pre><code class="copyable">Vue.component('base-checkbox', &#123;
  model: &#123;
    prop: 'checked',
    event: 'change'
  &#125;,
  props: &#123;
    checked: Boolean
  &#125;,
  template: `
    <input
      type="checkbox"
      v-bind:checked="checked"
      v-on:change="$emit('change', $event.target.checked)"
    >
  `
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在在这个组件上使用 v-model 的时候：</p>
<pre><code class="copyable"><base-checkbox v-model="lovingVue"></base-checkbox>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 lovingVue 的值将会传入这个名为 checked 的 prop。同时当  触发一个 change 事件并附带一个新的值的时候，这个 lovingVue 的 property 将会被更新。</p>
<h6 data-id="heading-31">方法三  .sync</h6>
<pre><code class="copyable"><template>
  <div class="details">
    <myComponent
        :show.sync='valueChild'
        style="padding: 30px 20px 30px 5px;border:1px solid #ddd;margin-bottom: 10px;"
    >
    </myComponent>
    <button @click="changeValue">toggle</button>
  </div>
</template>
<script>
import Vue from 'vue'

Vue.component(
    'myComponent', &#123;
      template: `
        <div v-if="show">
        <p>默认初始值是&#123;&#123; show &#125;&#125;，所以是显示的</p>
        <button @click.stop="closeDiv">关闭</button>
        </div>`,
      props: ['show'],
      methods: &#123;
        closeDiv() &#123;
          this.$emit('update:show', false); //触发 input 事件，并传入新值
        &#125;
      &#125;
    &#125;)
export default &#123;
  data() &#123;
    return &#123;
      valueChild: true,
    &#125;
  &#125;,
  methods: &#123;
    changeValue() &#123;
      this.valueChild = !this.valueChild
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">在vue3中将v-model和.sync进行了统一</h4>
<p>父组件</p>
<pre><code class="copyable"><model02
v-model:age="age02"
v-model:name="name02"
 ></model02>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件</p>
<pre><code class="copyable"><template>
  <div class="custom-input">
    <h1>vue3中的v-model</h1>
    <input type="text" :value="age" @input="onAgeInput"/>
    <br>
    <input type="text" :value="name" @input="onNameInput"/>
  </div>
</template>

<script>
export default &#123;
  name: "Model02",
  props: [
    'age',
    'name'
  ],
  methods: &#123;
    onAgeInput(e) &#123;
      this.$emit('update:age', parseFloat(e.target.value));
    &#125;,
    onNameInput(e) &#123;
      this.$emit('update:name', e.target.value)
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-33">渲染函数api</h2>
<h4 data-id="heading-34">api的变化</h4>
<p>在vue2中</p>
<pre><code class="copyable">export default &#123;
  render(h) &#123;
    return h('div')
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue3中 从vue中导出h</p>
<pre><code class="copyable">import &#123; h, reactive &#125; from 'vue'

export default &#123;
  setup(props, &#123; slots, attrs, emit &#125;) &#123;
    const state = reactive(&#123;
      count: 0
    &#125;)

    function increment() &#123;
      state.count++
    &#125;
    // 返回render函数
    return () =>
      h(
        'div',
        &#123;
          onClick: increment
        &#125;,
        state.count
      )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">h函数传参的变化</h4>
<p>vue2中
domProps 包含 VNode props 中的嵌套列表   点击事件是在on里面</p>
<pre><code class="copyable">&#123;
  class: ['button', 'is-outlined'],
  style: &#123; color: '#34495E' &#125;,
  attrs: &#123; id: 'submit' &#125;,
  domProps: &#123; innerHTML: '' &#125;,
  on: &#123; click: submitForm &#125;,
  key: 'submit-button'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue3中</p>
<pre><code class="copyable">&#123;
  class: ['button', 'is-outlined'],
  style: &#123; color: '#34495E' &#125;,
  id: 'submit',
  innerHTML: '',
  onClick: submitForm,
  key: 'submit-button'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-36">data</h2>
<p>在vue2中data可以是一个函数或者一个对象,在vue3中data只能是一个函数</p>
<h2 data-id="heading-37">函数组件</h2>
<p>在vue2中，函数组件的两种写法</p>
<pre><code class="copyable">export default &#123;
  functional: true,
  props: ['level'],
  render(h, &#123; props, data, children &#125;) &#123;
    return h(`h$&#123;props.level&#125;`, data, children)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><template functional>
  <component
    :is="`h$&#123;props.level&#125;`"
    v-bind="attrs"
    v-on="listeners"
  />
</template>

<script>
export default &#123;
  props: ['level']
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue3中 不支持函数组件，你可以像下面这样书写</p>
<pre><code class="copyable">import &#123; h &#125; from 'vue'

const DynamicHeading = (props, context) => &#123;
  return h(`h$&#123;props.level&#125;`, context.attrs, context.slots)
&#125;

DynamicHeading.props = ['level']

export default DynamicHeading
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 3.x 中，有状态组件和函数式组件之间的性能差异已经大大减少，并且在大多数用例中是微不足道的。因此，在 SFCs 上使用 functional 的开发人员的迁移路径是删除该 attribute，并将 props 的所有引用重命名为 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>p</mi><mi>r</mi><mi>o</mi><mi>p</mi><mi>s</mi><mtext>，将</mtext><mi>a</mi><mi>t</mi><mi>t</mi><mi>r</mi><mi>s</mi><mtext>重命名为</mtext></mrow><annotation encoding="application/x-tex">props，将 attrs 重命名为 </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">p</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">p</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">将</span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">重</span><span class="mord cjk_fallback">命</span><span class="mord cjk_fallback">名</span><span class="mord cjk_fallback">为</span></span></span></span></span>attrs。</p>
<pre><code class="copyable"><template>
  <component
    v-bind:is="`h$&#123;$props.level&#125;`"
    v-bind="$attrs"
  />
</template>

<script>
export default &#123;
  props: ['level']
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-38">异步组件</h2>
<h4 data-id="heading-39">vue2中使用异步组件的两种方式</h4>
<ol>
<li></li>
</ol>
<pre><code class="copyable">Vue.component(
  'async-webpack-example',
  // 这个动态导入会返回一个 `Promise` 对象。
  () => import('./my-async-component')
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li></li>
</ol>
<pre><code class="copyable">const AsyncComponent = () => (&#123;
  // 需要加载的组件 (应该是一个 `Promise` 对象)
  component: import('./MyComponent.vue'),
  // 异步组件加载时使用的组件
  loading: LoadingComponent,
  // 加载失败时使用的组件
  error: ErrorComponent,
  // 展示加载时组件的延时时间。默认值是 200 (毫秒)
  delay: 200,
  // 如果提供了超时时间且组件加载也超时了，
  // 则使用加载失败时使用的组件。默认值是：`Infinity`
  timeout: 3000
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-40">在vue3中使用异步组件</h4>
<ol>
<li></li>
</ol>
<pre><code class="copyable">import &#123; defineAsyncComponent &#125; from 'vue'

const AsyncComp = defineAsyncComponent(() =>
  import('./components/AsyncComponent.vue')
)

app.component('async-component', AsyncComp)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>这里和vue2有点区别  component 替换成了loader</li>
</ol>
<pre><code class="copyable"> AsyncPageWithOptions: defineAsyncComponent(&#123;
  loader: () => import(".NextPage.vue"),
  delay: 200, 
  timeout: 3000,
  errorComponent: () => import("./ErrorComponent.vue"),
  loadingComponent: () => import("./LoadingComponent.vue"),
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-41">event</h2>
<h4 data-id="heading-42">事件</h4>
<p>vue2中的<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>o</mi><mi>n</mi><mtext>，</mtext></mrow><annotation encoding="application/x-tex">on，</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mord cjk_fallback">，</span></span></span></span></span>off 和 $once 实例方法已被移除，应用实例不再实现事件触发接口
在vue3中如果还想用，就使用第三方库mitt</p>
<h4 data-id="heading-43">事件修饰符</h4>
<p>vue3中不在支持
非兼容：不再支持使用数字 (即键码) 作为 v-on 修饰符
非兼容：不再支持 config.keyCodes</p>
<h6 data-id="heading-44">vue2中</h6>
<pre><code class="copyable"><!-- 键码版本 -->
<input v-on:keyup.13="submit" />

<!-- 别名版本 -->
<input v-on:keyup.enter="submit" />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，你可以通过全局 config.keyCodes 选项。</p>
<pre><code class="copyable">Vue.config.keyCodes = &#123;
  f1: 112
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><!-- 键码版本 -->
<input v-on:keyup.112="showHelpText" />

<!-- 自定别名版本 -->
<input v-on:keyup.f1="showHelpText" />
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-45">vue3中</h6>
<pre><code class="copyable"><!-- Vue 3 在 v-on 上使用 按键修饰符 -->
<input v-on:keyup.delete="confirmDelete" />
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-46">指令</h2>
<ol>
<li>首先写一个简单的指令(和vue2类似) 生命周期发生了变化(请看后续)</li>
</ol>
<pre><code class="copyable">const app = Vue.createApp(&#123;&#125;)
// 注册一个全局自定义指令 `v-focus`
app.directive('focus', &#123;
  // 当被绑定的元素挂载到 DOM 中时……
  mounted(el) &#123;
    // 聚焦元素
    el.focus()
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-47">生命周期(和组件的生命周期一致)</h4>
<p>created：在绑定元素的 attribute 或事件监听器被应用之前调用。在指令需要附加须要在普通的 v-on 事件监听器前调用的事件监听器时，这很有用。
beforeMount：当指令第一次绑定到元素并且在挂载父组件之前调用。
mounted：在绑定元素的父组件被挂载后调用。
beforeUpdate：在更新包含组件的 VNode 之前调用。
updated：在包含组件的 VNode 及其子组件的 VNode 更新后调用。
beforeUnmount：在卸载绑定元素的父组件之前调用
unmounted：当指令与元素解除绑定且父组件已卸载时，只调用一次。
每一个钩子函数都有如下参数：
el: 指令绑定的元素，可以用来直接操作DOM
binding: 数据对象，包含以下属性
instance: 当前组件的实例，一般推荐指令和组件无关，如果有需要使用组件上下文ViewModel，可以从这里获取
value: 指令的值
oldValue: 指令的前一个值，在beforeUpdate和Updated 中，可以和value是相同的内容。
arg: 传给指令的参数，例如v-on:click中的click。
modifiers: 包含修饰符的对象。例如v-on.stop:click 可以获取到一个&#123;stop:true&#125;的对象
vnode: Vue 编译生成的虚拟节点,
prevVNode: Update时的上一个虚拟节点</p>
<h4 data-id="heading-48">动态指令参数</h4>
<p>假设我们现在需要开发一个定位指令，就是把某个元素固定在页面的某个位置。</p>
<ol>
<li>首先让元素固定</li>
</ol>
<pre><code class="copyable"><div v-fix:left="20">
     &#123;&#123;count&#125;&#125;
</div>

 directives: &#123;
   fix: &#123;
     mounted(el) &#123;
        el.style.position = 'fixed'
     &#125;,
   &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>让元素固定在指定位置</li>
</ol>
<pre><code class="copyable"> directives: &#123;
   fix: &#123;
     mounted(el) &#123;
        el.style.position = 'fixed'
        const s = binding.arg || 'top'
        el.style[s] = binding.value + 'px'
     &#125;,
   &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就完成了一个自定义指令的开发</p>
<h4 data-id="heading-49">指令的value可以是一个对象</h4>
<pre><code class="copyable"><div v-demo="&#123; color: 'white', text: 'hello!' &#125;"></div>
app.directive('demo', (el, binding) => &#123;
  console.log(binding.value.color) // => "white"
  console.log(binding.value.text) // => "hello!"
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-50">watchEffect 和 watch</h2>
<h4 data-id="heading-51">watchEffect和watch的不同之处</h4>
<ol>
<li>watchEffect 不需要指定监听的属性，他会自动的收集依赖</li>
<li>只要我们回调中引用到了 响应式的属性， 那么当这些属性变更的时候，这个回调都会执行，而 watch 只能监听指定的属性而做出变更(v3开始可以同时指定多个)</li>
<li>第二点就是 watch 可以获取到新值与旧值（更新前的值），而 watchEffect 是拿不到的</li>
<li>第三点是 watchEffect 如果存在的话，在组件初始化的时候就会执行一次用以收集依赖（与computed同理），而后收集到的依赖发生变化，这个回调才会再次执行，而 watch 不需要，因为他一开始就指定了依赖。</li>
</ol>
<h4 data-id="heading-52">watwatchEffect的使用</h4>
<pre><code class="copyable"><template>
 <div>
   <div>
     123123123
   </div>
   <div>
     &#123;&#123;count&#125;&#125;
   </div>
   <button @click="handleClick">增加</button>
 </div>
</template>

<script>
import &#123; ref,watchEffect &#125; from 'vue'


export default &#123;
emits:['click'],
 setup() &#123;
  let count = ref(0)
  const handleClick = () =>&#123;
    count.value++
  &#125;
  watchEffect(() => console.log(count.value))
  return &#123;
    count,
    handleClick
  &#125;
 &#125;,
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-53">watchEffect的停止</h6>
<p>watchEffect 会返回一个用于停止这个监听的函数</p>
<pre><code class="copyable">const stop = watchEffect(() => &#123;
  /* ... */
&#125;)

// later
stop()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-54">清除副作用</h4>
<p>假设我们现在用一个用户ID去查询用户的详情信息，然后我们监听了这个用户ID， 当用户ID 改变的时候我们就会去发起一次请求，这很简单，用watch 就可以做到。 但是如果在请求数据的过程中，我们的用户ID发生了多次变化，那么我们就会发起多次请求，而最后一次返回的数据将会覆盖掉我们之前返回的所有用户详情。这不仅会导致资源浪费，还无法保证 watch 回调执行的顺序。而使用 watchEffect 我们就可以做到。</p>
<pre><code class="copyable">// 当id改变的时候，之前的异步没有执行完成，会取消之前的异步
watchEffect((onInvalidate) => &#123;
  const token = asyncOperation(id.value);
  onInvalidate(() => &#123;
    // run if id has changed or watcher is stopped
    token.cancel();
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-55">副作用刷新时机</h4>
<p>Vue 的响应性系统会缓存副作用函数，并异步地刷新它们，这样可以避免同一个“tick” 中多个状态改变导致的不必要的重复调用。
如果你希望副作用函数在组件更新前发生，可以将flush设为'post'（默认是'pre'）
一般用于获取dom之后的值，会用到post</p>
<pre><code class="copyable">watchEffect(
  () => &#123;
    /* ... */
  &#125;,
  &#123;
    flush: 'post'//默认值为 'pre'
  &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-56">watch的使用</h4>
<p>和watchEffect相比较</p>
<ol>
<li>懒执行副作用；</li>
<li>更具体地说明什么状态应该触发侦听器重新运行；</li>
<li>访问侦听状态变化前后的值。</li>
</ol>
<h6 data-id="heading-57">监听单个数据源</h6>
<pre><code class="copyable">const count = ref(0)
watch(count, (count, prevCount) => &#123;
  /* ... */
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-58">监听多个数据源</h6>
<pre><code class="copyable">  watch ([countObj, count], ([oneNewName, twoNewName], [oneOldName, twoOldName]) => &#123;
      console.log(oneNewName, oneOldName, twoNewName, twoOldName)
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-59">停止侦听，清除副作用</h6>
<p>watch 与 watchEffect共享停止侦听，清除副作用 (相应地 onInvalidate 会作为回调的第三个参数传入)、副作用刷新时机和侦听器调试行为。</p>
<h2 data-id="heading-60">mixin</h2>
<h4 data-id="heading-61">在vue2中使用mixin</h4>
<p>把 methods、components 和 directives，将被合并为同一个对象。两个对象键名冲突时，取组件对象的键值对。</p>
<pre><code class="copyable">export default&#123;
data()&#123;
return&#123;
&#125;
&#125;,
created() &#123;
    // do something...
  &#125;,
methods:&#123;...&#125;
&#125;

// vue页面中引入
import mixin from 'mixin.js'
export default&#123;
data()&#123;&#125;,
mixins: [mixin]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-62">在vue3中使用mixin</h4>
<ol>
<li>数据对象在内部会进行递归合并，并在发生冲突时以组件数据优先。</li>
</ol>
<pre><code class="copyable">const myMixin = &#123;
  data() &#123;
    return &#123;
      message: 'hello',
      foo: 'abc'
    &#125;
  &#125;
&#125;

const app = Vue.createApp(&#123;
  mixins: [myMixin],
  data() &#123;
    return &#123;
      message: 'goodbye',
      bar: 'def'
    &#125;
  &#125;,
  created() &#123;
    console.log(this.$data) // => &#123; message: "goodbye", foo: "abc", bar: "def" &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>当同名钩子函数将合并为一个数组，因此都将被调用 (两个create都会被调用)</li>
</ol>
<pre><code class="copyable">const myMixin = &#123;
  data() &#123;
    return &#123;
      message: 'hello',
      foo: 'abc'
    &#125;
  &#125;
  created() &#123;
    console.log(this.$.message) // => &#123; message: "goodbye", foo: "abc", bar: "def" &#125;
  &#125;
&#125;

const app = Vue.createApp(&#123;
  mixins: [myMixin],
  data() &#123;
    return &#123;
      message: 'goodbye',
      bar: 'def'
    &#125;
  &#125;,
  created() &#123;
    console.log(this.$data) // => &#123; message: "goodbye", foo: "abc", bar: "def" &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>
<p>值为对象的选项，例如 methods、components 和 directives，将被合并为同一个对象。两个对象键名冲突时，取组件对象的键值对。(这个和vue2一样)</p>
</li>
<li>
<p>自定义合并策略</p>
</li>
</ol>
<pre><code class="copyable">const app = Vue.createApp(&#123;
  custom: 'hello!'
&#125;)

app.config.optionMergeStrategies.custom = (toVal, fromVal) => &#123;
  console.log(fromVal, toVal)
  // => "goodbye!", undefined
  // => "hello", "goodbye!"
  return fromVal || toVal
&#125;

app.mixin(&#123;
  custom: 'goodbye!',
  created() &#123;
    console.log(this.$options.custom) // => "hello!"
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-63">全局api</h2>
<ol>
<li>vue3对于全局api有了很大的调整。 vue2中没有app的概念，我们定义的应用只是通过new Vue()创建vue实例,而且所有的方法都是静态方法绑定在Vue的身上,
这样会导致两个问题。 全局配置容易污染其他测试用例，2. 经过webpack打包之后会有很多冗余代码</li>
<li>createApp</li>
</ol>
<pre><code class="copyable">vue3中
createApp(Main).mount('#app')
vue2中
new Vue(&#123;

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他api的调整</p>
<pre><code class="copyable">Vue.config                app.config
Vue.config.productionTip  removed 
Vue.config.ignoredElementsapp.config.isCustomElement
Vue.component              app.component
Vue.directive              app.directive
Vue.mixin                  app.mixin
Vue.use                    app.use
Vue.prototype              app.config.globalProperties
<span class="copy-code-btn">复制代码</span></code></pre>
<p>全部调整为 import  &#123;nextTick,observable&#125; from 'vue'</p>
<pre><code class="copyable">Vue.nextTick
Vue.observable (用 Vue.reactive 替换)
Vue.version
Vue.compile (仅完整构建版本)
Vue.set (仅兼容构建版本)
Vue.delete (仅兼容构建版本)

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-64">slot</h2>
<p>后期更新</p>
<h2 data-id="heading-65">自定义渲染器</h2>
<p>后期更新</p>
<h2 data-id="heading-66">vue写一个todoList(后续详细讲解，体会vue3的优势)</h2>
<pre><code class="copyable"><template>
 <ul>
   <input type="text" placeholder="id" v-model="addform.form.id">
    <input type="text" placeholder="姓名" v-model="addform.form.name">
     <input type="text" placeholder="年龄" v-model="addform.form.age">
     <button @click="handleAdd">按钮</button>
   <li v-for="(item,index) in todoList.list" :key="item.id" @click="handleDelete(index)">&#123;&#123;item.name&#125;&#125;---&#123;&#123;item.age&#125;&#125;</li>
 </ul> 
</template>

<script>
import &#123; reactive &#125; from 'vue'

export default &#123;
  name: 'App',
  setup() &#123;
    let &#123;todoList,handleDelete&#125; = DeleteTodo()
    let &#123;addform,handleAdd&#125; = AddTodo(todoList)
    return &#123;todoList,addform,handleDelete,handleAdd&#125;
  &#125;,
&#125;

function DeleteTodo() &#123;
let obj = [
        &#123;id:1,name:'zs',age:10&#125;,
        &#123;id:2,name:'ls',age:20&#125;,
        &#123;id:3,name:'ww',age:30&#125;
       ]
    let todoList = reactive(&#123;list: obj&#125;);
    function handleDelete(i)&#123;
      todoList.list = todoList.list.filter((item,index)=>&#123;
        return index !== i
      &#125;)
    &#125;
    return &#123;todoList,handleDelete &#125;
&#125;

function AddTodo(todoList) &#123;
 let form = &#123;
      id: '',
      name: '',
      age: ''
    &#125;
  let addform = reactive(&#123;form:form&#125;)
  function handleAdd() &#123;
      todoList.list.push(form)
    &#125;
  return &#123; addform, handleAdd&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上图: 在vue2中如果我们需要实现一个todolist，首先我们需要在data里面定义数据，然后在methods里面定义方法，可以还需要computed，或者watch，这样一个功能的代码逻辑在多处使用到了，不利于维护。而vue3中可以将一个功能的代码逻辑抽离出来，这样便于维护</p></div>  
</div>
            