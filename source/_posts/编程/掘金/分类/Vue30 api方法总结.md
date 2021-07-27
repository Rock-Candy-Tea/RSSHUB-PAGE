
---
title: 'Vue3.0 api方法总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d2edc7545f849a8a16aad9c4bbf5022~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 04:56:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d2edc7545f849a8a16aad9c4bbf5022~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ol>
<li>ref与toRef、toRefs</li>
</ol>
<p><code>ref</code>函数包装了一个响应式的数据对象。<br>
<code>toRef</code> 是将某个对象中的某个值转化为响应式数据，其接收两个参数，第一个参数为 <code>obj</code> 对象；第二个参数为对象中的属性名。<br>
<code>toRefs</code>其作用就是将传入的对象里所有的属性的值都转化为响应式数据对象，该函数支持一个参数，即 <code>obj</code> 对象<br>
<code>ref</code> 是对传入数据的拷贝；<code>toRef</code> 是对传入数据的引用<br>
<code>ref</code> 的值改变会更新视图；<code>toRef</code> 的值改变不会更新视图<br></p>
<ol start="2">
<li>reactive与shallowReactive<br></li>
</ol>
<p><code>reactive</code> 方法是用来创建一个响应式的数据对象，可以是嵌套的对象，会给内部的每一个对像都加入一个Proxy包裹着<br>
<code>shallowReactive</code>代表一个浅层的 <code>reactive</code>,意思就是监听了第一层属性的值，一旦发生改变，则更新视图。代表着当使用时只给第一层加入了Proxy</p>
<pre><code class="copyable"><template>
  <div>&#123;&#123;state.count&#125;&#125;</div>
</template>

<script>
import &#123; reactive,shallowReactive &#125;from 'vue'
export default &#123;
  name: 'HelloWorld',
  props: &#123;
    msg: String
  &#125;,
  setup() &#123;
    const state= reactive(&#123;count:3&#125;)
    return &#123;
      state
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在对比reactive和shallowReactive<br>
<strong>使用reactive</strong><br></p>
<pre><code class="copyable"><template>
  <div>&#123;&#123;state.count&#125;&#125;</div>
</template>

<script>
import &#123; reactive,shallowReactive &#125;from 'vue'
export default &#123;
  name: 'HelloWorld',
  props: &#123;
    msg: String
  &#125;,
  setup() &#123;
    const obj=&#123;
       one:&#123;
         name:'小明',
         two:&#123;
           name:'小王',
           three:&#123;
            name:'小李',
           &#125;
         &#125;
       &#125;
    &#125;
    const state= reactive(obj)
    console.log(state.one)
    console.log(state.one.two)
    console.log(state.one.two.three)
    return &#123;
      state
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用shallowReactive</strong><br></p>
<pre><code class="copyable"><template>
  <div>&#123;&#123;state.count&#125;&#125;</div>
</template>

<script>
import &#123; reactive,shallowReactive &#125;from 'vue'
export default &#123;
  name: 'HelloWorld',
  props: &#123;
    msg: String
  &#125;,
  setup() &#123;
    const obj=&#123;
       one:&#123;
         name:'小明',
         two:&#123;
           name:'小王',
           three:&#123;
            name:'小李',
           &#125;
         &#125;
       &#125;
    &#125;
    const state= shallowReactive(obj)
    console.log(state)
    console.log(state.one)
    console.log(state.one.two)
    console.log(state.one.two.three)
    return &#123;
      state
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果如下:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d2edc7545f849a8a16aad9c4bbf5022~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>4.toRaw和markRaw <br>
<code>toRaw</code> 方法是用于获取 <code>ref</code> 或 <code>reactive</code> 对象的原始数据的;<br>
示例如下:</p>
<pre><code class="copyable"><script>
import &#123;reactive, toRaw&#125; from 'vue'
export default &#123;
    setup() &#123;
        const obj = &#123;
            name: '哈哈哈哈哈哈哈',
            age: 35
        &#125;

        const state = reactive(obj)
        const raw = toRaw(state)
        console.log(state)
        console.log(raw)
        console.log(obj === raw)   // true
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7523230e27be4de2b92dfd9d3cf8e998~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>markRaw</code> 方法可以将原始数据标记为非响应式的，即使用 <code>ref</code> 或 <code>reactive</code> 将其包装，仍无法实现数据响应式，其接收一个参数，即原始数据，并返回被标记后的数据。示例如下：</p>
<pre><code class="copyable"><script>
import &#123;reactive, toRaw,markRaw&#125; from 'vue'
export default &#123;
    setup() &#123;
        const obj = &#123;
            name: '哈哈哈哈哈哈哈',
            age: 35
        &#125;
        markRaw(obj)
        const state = reactive(obj)
        console.log(obj)
        console.log(state)
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b3fe4b2e2b348d58634a6fa476277b7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>5.useRoute和useRouter</p>
<pre><code class="copyable"><template>
    <div>
        <router-link to="/home">Home</router-link>
        <router-link to='/test'>Test</router-link>
    </div>
    <router-view></router-view>
</template>

<script>
import &#123; onMounted &#125; from "vue";
import &#123; useRoute, useRouter &#125; from "vue-router";
export default &#123;
    setup(props, context) &#123;
        onMounted(() => &#123;
            console.log(route);
            console.log(router);
        &#125;);

        const route = useRoute();
        const router = useRouter();

        return &#123;&#125;;
    &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5a97274782e426b8ac9ea604a32cf0a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
6.watch和watchEffect<br>
<code>watch</code>和<code>watchEffect</code>都是用来监视某项数据变化从而执行指定的操作的,但是他们之间在用法上还是有区别的:<br>
watch( source, cb, [options] )</p>
<ul>
<li>source：可以是表达式或函数，用于指定监听的依赖对象</li>
<li>cb：依赖对象变化后执行的回调函数</li>
<li>options：可参数，可以配置的属性有 immediate（立即触发回调函数）、deep（深度监听）</li>
</ul>
<p>当ref时</p>
<pre><code class="copyable"><template>
    <div>
        <router-link to="/home">Home</router-link>
        <router-link to='/test'>Test</router-link>
    </div>
    <router-view></router-view>
</template>

<script>
import &#123; ref,watch&#125; from "vue";
export default &#123;
    setup() &#123;
       const state = ref(0)
        watch(state, (newValue, oldValue) => &#123;
            console.log(`原值为$&#123;oldValue&#125;`)
            console.log(`新值为$&#123;newValue&#125;`)
            /* 1秒后打印结果：
              原值为0
              新值为1
            */
        &#125;)
        // 1秒后将state值+1
        setTimeout(() => &#123;
            state.value ++
        &#125;, 1000)
    &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当reactive时</p>
<pre><code class="copyable"><script>
import &#123;reactive, watch&#125; from 'vue'
export default &#123;
    setup() &#123;
        const state = reactive(&#123;count: 0&#125;)

        watch(() => state.count, (newValue, oldValue) => &#123;
            console.log(`原值为$&#123;oldValue&#125;`)
            console.log(`新值为$&#123;newValue&#125;`)
            /* 1秒后打印结果：
                            原值为0
                            新值为1
            */
        &#125;)

        // 1秒后将state.count的值+1
        setTimeout(() => &#123;
            state.count ++
        &#125;, 1000)
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb3a64a08ee64008b124929bac48e9ff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
监听多个值：</p>
<pre><code class="copyable"><script>
import &#123;reactive, watch&#125; from 'vue'
export default &#123;
    setup() &#123;
        const state = reactive(&#123; count: 0, name: 'zs' &#125;)

        watch(
            [() => state.count, () => state.name], 
            ([newCount, newName], [oldvCount, oldName]) => &#123;
                console.log(oldvCount) // 旧的 count 值
                console.log(newCount) // 新的 count 值
                console.log(oldName) // 旧的 name 值
                console.log(newName) // 新的 name 值
            &#125;
        )

        setTimeout(() => &#123;
          state.count ++
          state.name = 'ls'
        &#125;, 1000)
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4d0e5c3b7dd49fc8ae9dc82e8c2fbd4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>watchEffect</code>，它与 <code>watch</code> 的区别主要有以下几点：</p>
<ol>
<li>不需要手动传入依赖</li>
<li>每次初始化时会执行一次回调函数来自动获取依赖</li>
<li>无法获取到原值，只能得到变化后的值</li>
</ol>
<pre><code class="copyable"><template>
    <div>
        <router-link to="/home">Home</router-link>
        <router-link to='/test'>Test</router-link>
    </div>
    <router-view></router-view>
</template>

<script>
import &#123;reactive, watchEffect&#125; from 'vue'
export default &#123;
    setup() &#123;
        const state = reactive(&#123; count: 0, name: 'zs' &#125;)

        watchEffect(() => &#123;
            console.log(state.count)
            console.log(state.name)
            /*  初始化时打印：
                            0
                            zs

                1秒后打印：
                            1
                            ls
            */
        &#125;)

        setTimeout(() => &#123;
          state.count ++
          state.name = 'ls'
        &#125;, 1000)
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb27ba009605469e9b81ff0ee1896aac~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
7.computed
返回一个 ref 对象。</p>
<pre><code class="copyable"><script>
import &#123;computed,ref&#125; from 'vue'
export default &#123;
    setup() &#123;
      const x=computed(()=>&#123;
return 'jjjjj'
      &#125;)
      console.log(x.value)
      const count = ref(1)
      const plusOne = computed(&#123;
get: () => &#123; 
          console.log('---------Get',count.value)
          return count.value + 1
        &#125;,
set: val => &#123;
          console.log('---------Set',val)
  count.value = val - 1
  &#125;
&#125;)
       plusOne.value = 1
       console.log(count.value)
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1938ff6795d46f68ee88e4aed84bce4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>8.provide和inject</p>
<ul>
<li><strong>provide</strong> ：向子组件以及子孙组件传递数据。接收两个参数，第一个参数是 <code>key</code>，即数据的名称；第二个参数为 <code>value</code>，即数据的值</li>
<li><strong>inject</strong> ：接收父组件或祖先组件传递过来的数据。接收一个参数 <code>key</code>，即父组件或祖先组件传递的数据名称</li>
</ul>
<pre><code class="copyable">//a.vue
<script>
import &#123;provide&#125; from 'vue'
export default &#123;
    setup() &#123;
        const obj= &#123;
            name: '哈哈哈哈哈哈',
            age: 22
        &#125;

        // 向子组件以及子孙组件传递名为info的数据
        provide('info', obj)
    &#125;
&#125;
</script>

//b.vue
<script>
import &#123;inject&#125; from 'vue'
export default &#123;
    setup() &#123;
        // 接收a.vue传递过来的数据
        inject('info')  // &#123;name: '哈哈哈哈哈哈', age: 22&#125;
    &#125;
&#125;
</script>

//c.vue
<script>
import &#123;inject&#125; from 'vue'
export default &#123;
    setup() &#123;
        // 接收a.vue传递过来的数据
        inject('info')  // &#123;name: '哈哈哈哈哈哈', age: 22&#125;
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>9.vue2与vue3生命周期对比</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a89ce51aef04362b614031a63eede5b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"><template> 
  <div id="app"></div>
</template> 
<script> 
// 1. 从 vue 中引入 多个生命周期函数 
import &#123;onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, unMounted&#125; from 'vue'
 export default &#123; 
  name: 'App', 
  setup() &#123; 
    onBeforeMount(() => &#123; 
    // 在挂载前执行某些代码 
    &#125;) 
    onMounted(() => &#123; // 在挂载后执行某些代码 
    &#125;) 
    onBeforeUpdate(() => &#123; 
      // 在更新前前执行某些代码 
    &#125;) 
    onUpdated(() => &#123; 
    // 在更新后执行某些代码 
    &#125;) 
    onBeforeUnmount(() => &#123; 
      // 在组件销毁前执行某些代码 
    &#125;) 
    unMounted(() => &#123; 
      // 在组件销毁后执行某些代码 
    &#125;)
    return &#123;&#125; 
  &#125; 
&#125; 
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>10.setup(props,context)</p>
<pre><code class="copyable">(1)props:
组件传递的参数,是响应式的,可以通过使用watchEffect或watch进行观测和响应
不要直接使用解构赋值,会使得参数失去响应性
若要解构:const &#123; title &#125; = toRefs(props)

(2)context:
上下文对象            对应之前vue2的
        context.attrs    this.$attrs  组件标签上的属性(非响应式对象)
        context.slots this.$slots 插槽(非响应式对象)
        context.emit  this.$emit 标签上自定义的触发事件(方法)
        context.emit('自定义事件名',参数)
   
无法访问:因为是在组件创建实例之前指向
 data
     computed
     methods
             解构:
context是一个普通的JavaScript对象,也就是说,它不是响应式的,可以直接解构
attrs和slots是内部组件实例上相应值的代理。这样可以确保它们即使在更新后也始终会显示最新值,以便我们可以对它们进行结构分解,而不必担心访问老的引用：
但避免对内部的属性进行解构,并始终以attrs.x或slots.x的方式使用
    
(3)this指向问题:
因为setup()是在解析其它组件选项之前被调用的,所以setup()内部的this的行为与其它选项中的this完全不同

(4)更好的模块化问题:
可以从其他文件引入函数等,然后在setup中执行,其他文件中可以使用v3的组合式api(需先导入),但必须在setup中调用
 
(5)return返回值方式:
返回的内容可以在命令式api中this.x访问到
方式一:
return&#123;
返回的属性和方法,在setup外部能够使用,返回的普通属性不是响应式的,即改变不会更新视图
&#125;
方式二:
return () => h('div', ["哇咔咔"])还可以直接返回一个渲染函数,将替换模板中的内容

方式三:注意此时组件已经变成了一个异步组件,可使用Suspense悬挂展示

可以返回一个成功状态的Promise对象,会将成功态的[[PromiseResult]]结果作为返回值
return new Promise((resolve,reject)=>&#123;也可返回一个Promise对象,使得组件为异步的
...
resolve(&#123;
数据
&#125;)
&#125;)
 
 return await ...
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            