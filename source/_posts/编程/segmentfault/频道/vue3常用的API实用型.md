
---
title: 'vue3常用的API实用型'
categories: 
 - 编程
 - segmentfault
 - 频道
headimg: 'https://segmentfault.com/img/bVcQLzW'
author: segmentfault
comments: false
date: 2021-03-24 12:18:23
thumbnail: 'https://segmentfault.com/img/bVcQLzW'
---

<div>   
<p>vue3.x已经发布了这么久，相关的生态也慢慢起来了，包括vite这个新的打包工具，在vue3.0学习过程中有一些实用性的api对比，希望能在开发中给大家做个示范，准确的使用对应的api去完成我们的项目开发</p><h2>生命周期的变更</h2><p>要特别说明一下的就是，<code>setup</code> 函数代替了 <code>beforeCreate</code> 和 <code>created</code> 两个生命周期函数，因此我们可以认为它的执行时间在<code>beforeCreate</code> 和 <code>created</code> 之间</p><table><thead><tr><th>Vue2</th><th>Vue3</th></tr></thead><tbody><tr><td>beforeCreate</td><td>setup</td></tr><tr><td>created</td><td>setup</td></tr><tr><td>beforeMount</td><td>onBeforeMount</td></tr><tr><td>mounted</td><td>onMounted</td></tr><tr><td>beforeUpdate</td><td>onBeforeUpdate</td></tr><tr><td>updated</td><td>onUpdated</td></tr><tr><td>beforeDestory</td><td>onBeforeUnmount</td></tr><tr><td>destoryed</td><td>onUnmounted</td></tr></tbody></table><p>了解过vue3的小伙伴儿都知道，现在使用都会用到setup函数，关于在setup函数操作数据，我们用例子说明会好一点</p><h2>reactive</h2><p><code>reactive</code> 方法是用来创建一个响应式的数据对象，该API也很好地解决了Vue2通过 <code>defineProperty</code> 实现数据响应式的缺陷</p><p>用法很简单，只需将数据作为参数传入即可</p><pre><code><template>
  <div id="app">
   <!-- 4. 访问响应式数据对象中的 count  -->
   &#123;&#123; state.count &#125;&#125;
  </div>
</template>

<script>
// 1. 从 vue 中导入 reactive 
import &#123;reactive&#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
    // 2. 创建响应式的数据对象
    const state = reactive(&#123;count: 3&#125;)

    // 3. 将响应式数据对象state return 出去，供template使用
    return &#123;state&#125;
  &#125;
&#125;
</script></code></pre><h2>ref</h2><p>在介绍 <code>setup</code> 函数时，我们使用了 <code>ref</code> 函数包装了一个响应式的数据对象，这里表面上看上去跟 <code>reactive</code> 好像功能一模一样啊，确实差不多，因为 <code>ref</code> 就是通过 <code>reactive</code> 包装了一个对象 ，然后是将值传给该对象中的 <code>value</code> 属性，这也就解释了为什么每次访问时我们都需要加上 <code>.value</code></p><p>我们可以简单地把 <code>ref(obj)</code> 理解为这个样子 <code>reactive(&#123;value: obj&#125;)</code></p><pre><code><script>
import &#123;ref, reactive&#125; from 'vue'
export default &#123;
  name: 'App',
  setup() &#123;
   const obj = &#123;count: 3&#125;
   const state1 = ref(obj)
   const state2 = reactive(obj)

    console.log(state1)
    console.log(state2)
  &#125;
  
&#125;
</script></code></pre><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcQLzW" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p><strong>注意：</strong> 这里指的 <code>.value</code> 是在 <code>setup</code> 函数中访问 <code>ref</code> 包装后的对象时才需要加的，在 <code>template</code> 模板中访问时是不需要的，因为在编译时，会自动识别其是否为 <code>ref</code> 包装过的</p><h4><strong>那么我们到底该如何选择 <code>ref</code> 和 <code>reactive</code> 呢？</strong></h4><p><strong>建议：</strong></p><ol><li>基本类型值（<code>String</code> 、<code>Nmuber</code> 、<code>Boolean</code> 等）或单值对象（类似像 <code>&#123;count: 3&#125;</code> 这样只有一个属性值的对象）使用 <code>ref</code></li><li>引用类型值（<code>Object</code> 、<code>Array</code>）使用 <code>reactive</code></li></ol><h2>我们在vue2.x中获取元素标签是用 <code>ref</code> ，vue3.x我们要获取元素标签怎么办呢？</h2><pre><code><template>
  <div>
    <div ref="el">div元素</div>
  </div>
</template>

<script>
import &#123; ref, onMounted &#125; from 'vue'
export default &#123;
  setup() &#123;
    // 创建一个DOM引用，名称必须与元素的ref属性名相同
    const el = ref(null)

    // 在挂载后才能通过 el 获取到目标元素
    onMounted(() => &#123;
      el.value.innerHTML = '内容被修改'
    &#125;)

    // 把创建的引用 return 出去
    return &#123;el&#125;
  &#125;
&#125;
</script></code></pre><p>获取元素的操作一共分为以下几个步骤：</p><ol><li>先给目标元素的 <code>ref</code> 属性设置一个值，假设为 <code>el</code></li><li>然后在 <code>setup</code> 函数中调用 <code>ref</code> 函数，值为 <code>null</code>，并赋值给变量 <code>el</code>，这里要注意，该变量名必须与我们给元素设置的 <code>ref</code> 属性名相同</li><li>把对元素的引用变量 <code>el</code> 返回（return）出去</li></ol><blockquote><strong>补充</strong>：设置的元素引用变量只有在组件挂载后才能访问到，因此在挂载前对元素进行操作都是无效的</blockquote><p>当然如果我们引用的是一个组件元素，那么获得的将是该组件的实例对象</p><h2>toRef</h2><p><code>toRef</code> 是将某个对象中的某个值转化为响应式数据，其接收两个参数，第一个参数为 <code>obj</code> 对象；第二个参数为对象中的属性名</p><pre><code><script>
// 1. 导入 toRef
import &#123;toRef&#125; from 'vue'
export default &#123;
    setup() &#123;
        const obj = &#123;count: 3&#125;
        // 2. 将 obj 对象中属性count的值转化为响应式数据
        const state = toRef(obj, 'count')
  
        // 3. 将toRef包装过的数据对象返回供template使用
        return &#123;state&#125;
    &#125;
&#125;
</script></code></pre><p>上面又有个ref，又有个toRef，不是冲突了吗？两个有不一样的功效：</p><pre><code><template>
    <p>&#123;&#123; state1 &#125;&#125;</p>
    <button @click="add1">增加</button>

 <p>&#123;&#123; state2 &#125;&#125;</p>
    <button @click="add2">增加</button>
</template>

<script>
import &#123;ref, toRef&#125; from 'vue'
export default &#123;
    setup() &#123;
        const obj = &#123;count: 3&#125;
        const state1 = ref(obj.count)
        const state2 = toRef(obj, 'count')

        function add1() &#123;
            state1.value ++
            console.log('原始值：', obj);
            console.log('响应式数据对象：', state1);
        &#125;

        function add2() &#123;
            state2.value ++
            console.log('原始值：', obj);
            console.log('响应式数据对象：', state2);
        &#125;

        return &#123;state1, state2, add1, add2&#125;
    &#125;
&#125;
</script></code></pre><p><code>ref</code> 是对原数据的一个<strong>拷贝</strong>，不会影响到原始值，同时响应式数据对象值改变后会同步更新视图<br><code>toRef</code> 是对原数据的一个<strong>引用</strong>，会影响到原始值，但是响应式数据对象值改变后会不会更新视图</p><h2>toRefs</h2><p>将传入的对象里所有的属性的值都转化为响应式数据对象，该函数支持一个参数，即 <code>obj</code> 对象</p><pre><code><script>
// 1. 导入 toRefs
import &#123;toRefs&#125; from 'vue'
export default &#123;
    setup() &#123;
        const obj = &#123;
          name: '前端印象',
          age: 22,
          gender: 0
        &#125;
        // 2. 将 obj 对象中属性count的值转化为响应式数据
        const state = toRefs(obj)
  
        // 3. 打印查看一下
        console.log(state)
    &#125;
&#125;
</script></code></pre><p>返回的是一个对象，对象里包含了每一个包装过后的响应式数据对象</p><h2>shallowReactive</h2><p>听这个API的名称就知道，这是一个浅层的 <code>reactive</code>，难道意思就是原本的 <code>reactive</code> 是深层的呗，没错，这是一个用于性能优化的API</p><pre><code><script>
<template>
 <p>&#123;&#123; state.a &#125;&#125;</p>
 <p>&#123;&#123; state.first.b &#125;&#125;</p>
 <p>&#123;&#123; state.first.second.c &#125;&#125;</p>
 <button @click="change1">改变1</button>
 <button @click="change2">改变2</button>
</template>
<script>
import &#123;shallowReactive&#125; from 'vue'
export default &#123;
    setup() &#123;
        const obj = &#123;
          a: 1,
          first: &#123;
            b: 2,
            second: &#123;
              c: 3
            &#125;
          &#125;
        &#125;
        
        const state = shallowReactive(obj)
  
        function change1() &#123;
          state.a = 7
        &#125;

        function change2() &#123;
          state.first.b = 8
          state.first.second.c = 9
          console.log(state);
        &#125;

        return &#123;state&#125;
    &#125;
&#125;
</script></code></pre><p>首先我们点击了第二个按钮，改变了第二层的 <code>b</code> 和第三层的 <code>c</code>，虽然值发生了改变，但是视图却没有进行更新；</p><p>当我们点击了第一个按钮，改变了第一层的 <code>a</code> 时，整个视图进行了更新；</p><p>由此可说明，<code>shallowReactive</code> 监听了第一层属性的值，一旦发生改变，则更新视图</p><h2>shallowRef</h2><p>这是一个浅层的 <code>ref</code>，与 <code>shallowReactive</code> 一样是拿来做性能优化的，配合<code>triggerRef</code> ，调用它就可以立马更新视图，其接收一个参数 <code>state</code> ，即需要更新的 <code>ref</code> 对象</p><p><code>shallowReactive</code> 是监听对象第一层的数据变化用于驱动视图更新，那么 <code>shallowRef</code> 则是监听 <code>.value</code> 的值的变化来更新视图的</p><pre><code><template>
 <p>&#123;&#123; state.a &#125;&#125;</p>
 <p>&#123;&#123; state.first.b &#125;&#125;</p>
 <p>&#123;&#123; state.first.second.c &#125;&#125;</p>
 <button @click="change">改变</button>
</template>

<script>
import &#123;shallowRef, triggerRef&#125; from 'vue'
export default &#123;
    setup() &#123;
        const obj = &#123;
          a: 1,
          first: &#123;
            b: 2,
            second: &#123;
              c: 3
            &#125;
          &#125;
        &#125;
        
        const state = shallowRef(obj)
        console.log(state);

        function change() &#123;
          state.value.first.b = 8
          state.value.first.second.c = 9
          // 修改值后立即驱动视图更新
          triggerRef(state)
          console.log(state);
        &#125;

        return &#123;state, change&#125;
    &#125;
&#125;
</script></code></pre><h2>toRaw</h2><p><code>toRaw</code> 方法是用于获取 <code>ref</code> 或 <code>reactive</code> 对象的原始数据的</p><pre><code><script>
import &#123;reactive, toRaw&#125; from 'vue'
export default &#123;
    setup() &#123;
        const obj = &#123;
          name: '前端印象',
          age: 22
        &#125;

        const state = reactive(obj) 
        const raw = toRaw(state)

        console.log(obj === raw)   // true
    &#125;
&#125;
</script></code></pre><p>上述代码就证明了 <code>toRaw</code> 方法从 <code>reactive</code> 对象中获取到的是原始数据，因此我们就可以很方便的通过修改原始数据的值而不更新视图来做一些性能优化了</p><blockquote><strong>注意：</strong> 补充一句，当 <code>toRaw</code> 方法接收的参数是 <code>ref</code> 对象时，需要加上 <code>.value</code> 才能获取到原始数据对象</blockquote><h2>markRaw</h2><p><code>markRaw</code> 方法可以将原始数据标记为非响应式的，即使用 <code>ref</code> 或 <code>reactive</code> 将其包装，仍无法实现数据响应式，其接收一个参数，即原始数据，并返回被标记后的数据。即使我们修改了值也不会更新视图了，即没有实现数据响应式</p><pre><code><template>
 <p>&#123;&#123; state.name &#125;&#125;</p>
 <p>&#123;&#123; state.age &#125;&#125;</p>
 <button @click="change">改变</button>
</template>

<script>
import &#123;reactive, markRaw&#125; from 'vue'
export default &#123;
    setup() &#123;
        const obj = &#123;
          name: '前端印象',
          age: 22
        &#125;
        // 通过markRaw标记原始数据obj, 使其数据更新不再被追踪
        const raw = markRaw(obj)   
        // 试图用reactive包装raw, 使其变成响应式数据
        const state = reactive(raw) 

        function change() &#123;
          state.age = 90
          console.log(state);
        &#125;

        return &#123;state, change&#125;
    &#125;
&#125;
</script></code></pre><h2>watchEffect</h2><p><code>watchEffect</code> 它与 <code>watch</code> 的区别主要有以下几点：</p><ol><li>不需要手动传入依赖</li><li>每次初始化时会执行一次回调函数来自动获取依赖</li><li>无法获取到原值，只能得到变化后的值</li></ol><pre><code><script>
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
</script></code></pre><p>没有像 <code>watch</code> 方法一样先给其传入一个依赖，而是直接指定了一个回调函数</p><p>当组件初始化时，将该回调函数执行一次，自动获取到需要检测的数据是 <code>state.count</code> 和 <code>state.name</code></p><p>根据以上特征，我们可以自行选择使用哪一个监听器</p><h2>getCurrentInstance</h2><p>我们都知道在Vue2的任何一个组件中想要获取当前组件的实例可以通过 <code>this</code> 来得到，而在Vue3中我们大量的代码都在 <code>setup</code> 函数中运行，并且在该函数中 <code>this</code> 指向的是<code>undefined</code>，那么该如何获取到当前组件的实例呢？这时可以用到另一个方法，即 <code>getCurrentInstance</code></p><pre><code><template>
 <p>&#123;&#123; num &#125;&#125;</p>
</template>
<script>
import &#123;ref, getCurrentInstance&#125; from 'vue'
export default &#123;
    setup() &#123; 
        const num = ref(3)
        const instance = getCurrentInstance()
        console.log(instance)

        return &#123;num&#125;
    &#125;
&#125;
</script></code></pre><p><code>instance</code> 中重点关注 <code>ctx</code> 和 <code>proxy</code> 属性，这两个才是我们想要的 <code>this</code>。可以看到 <code>ctx</code> 和 <code>proxy</code> 的内容十分类似，只是后者相对于前者外部包装了一层 <code>proxy</code>，由此可说明 <code>proxy</code> 是响应式的</p><h2>useStore</h2><p>在Vue2中使用 Vuex，我们都是通过 <code>this.$store</code> 来与获取到Vuex实例，但上一部分说了原本Vue2中的 <code>this</code> 的获取方式不一样了，并且我们在Vue3的 <code>getCurrentInstance().ctx</code> 中也没有发现 <code>$store</code> 这个属性，那么如何获取到Vuex实例呢？这就要通过 <code>vuex</code> 中的一个方法了，即 <code>useStore</code></p><pre><code>// store 文件夹下的 index.js
import Vuex from 'vuex'

const store = Vuex.createStore(&#123;
    state: &#123;
      name: '前端印象',
      age: 22
    &#125;,
    mutations: &#123;
      ……
    &#125;,
    ……
&#125;)

// example.vue
<script>
// 从 vuex 中导入 useStore 方法
import &#123;useStore&#125; from 'vuex'
export default &#123;
    setup() &#123; 
        // 获取 vuex 实例
        const store = useStore()

        console.log(store)
    &#125;
&#125;
</script></code></pre><p>然后接下来就可以像之前一样正常使用 <code>vuex</code> 了</p><p>参考：<a href="https://mp.weixin.qq.com/s/ywsOPLQYTDke65EXqtsJhg" rel="nofollow">vue3常用api使用</a></p>  
</div>
            