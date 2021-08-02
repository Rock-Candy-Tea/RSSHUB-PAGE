
---
title: 'vue3初探'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc2675263eb244a4b7e8417b64dfae13~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 18:26:46 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc2675263eb244a4b7e8417b64dfae13~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">组合式API</h2>
<p>我们先来看一个简单的vue2小例子</p>
<pre><code class="copyable"><template lang="pug">
div
    div &#123;&#123; number &#125;&#125;
    button(@click="handleDoubleNumber") 倍增数字
    div &#123;&#123; string &#125;&#125;
    button(@click="handleDoubleString") 倍增字符串
</template>
<script>
export default &#123;
    data() &#123;
        return &#123;
            number: 1,
            string: 'hi',
        &#125;
    &#125;,
    methods: &#123;
        handleDoubleNumber() &#123;
            this.number = this.number * 2
        &#125;,
        handleDoubleString() &#123;
            this.string += this.string
        &#125;,
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5695ddd9024429bb850c381277b2ded~tplv-k3u1fbpfcp-watermark.image" alt="code1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们继续新增功能时，代码块就会越来越多，导致书写以及阅读困难。相信小伙伴们有在公司碰到过要去修改前人很臭很长的代码，明明只要改动一点逻辑，但是却要捋清楚整个代码，让人着实焦躁。另外如果有部分功能有多个页面需要使用时，一般我们需要抽离出来使用mixin混入，但是mixin存在命名冲突，变量的来源未知，代码难以理解，难以维护等弊端。这种碎片化使得理解和维护复杂组件变得困难，选项的分离掩盖了潜在的逻辑问题。此外，在处理单个逻辑关注点时，我们必须不断地“跳转”相关代码的选项块。</p>
<p>我们能够将与同一个逻辑关注点相关的代码配置在一起会更好，而这正是组合式API使我们能够做到的。我们使用组合式API来重写下上面的代码。</p>
<p>新建一个useDoubleNumber.js</p>
<pre><code class="copyable">import &#123; ref &#125; from 'vue'
export default function useDoubleNumber() &#123;
    const number = ref(1)

    const handleDoubleNumber = () => &#123;
        number.value = number.value * 2
    &#125;

    return &#123;
        number,
        handleDoubleNumber,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建一个useDoubleString.js</p>
<pre><code class="copyable">import &#123; ref &#125; from 'vue'
export default function useDoubleString() &#123;
    const string = ref('hi')

    const handleDoubleString = () => &#123;
        string.value += string.value
    &#125;

    return &#123;
        string,
        handleDoubleString,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面中使用</p>
<pre><code class="copyable"><template lang="pug">
div
    div &#123;&#123; number &#125;&#125;
    button(@click="handleDoubleNumber") 倍增数字
    div &#123;&#123; string &#125;&#125;
    button(@click="handleDoubleString") 倍增字符串
</template>
<script>
import &#123; defineComponent &#125; from 'vue'
import useDoubleNumber from './useDoubleNumber'
import useDoubleString from './useDoubleString'

export default defineComponent(&#123;
    setup() &#123;
        const &#123; number, handleDoubleNumber &#125; = useDoubleNumber()
        const &#123; string, handleDoubleString &#125; = useDoubleString()
        return &#123;
            number,
            handleDoubleNumber,
            string,
            handleDoubleString,
        &#125;
    &#125;,
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的改造，我们可以发现页面的逻辑非常的清晰，功能复用也非常的方便。这样代码的可读性和可维护性也大大的提高了。</p>
<h3 data-id="heading-1">setup组件选项</h3>
<p>为了开始使用组合式API，我们首先需要一个可以实际使用它的地方。在Vue组件中，我们将此位置称为<code>setup</code>。</p>
<p>新的<code>setup</code>组件选项在创建组件之前执行，一旦<code>props</code>被解析，并充当合成API的入口点。由于在执行<code>setup</code>的时候尚未创建组件实例，因此在<code>setup</code>选项中没有<code>this</code>。</p>
<p><code>setup</code>选项应该是一个接受<code>props</code>和<code>context</code>的函数。此外，我们从<code>setup</code>返回的所有内容都将暴露给组件的其余部分（计算属性、方法、生命周期钩子等等）以及组件的模板。</p>
<p><strong>Props</strong></p>
<p><code>setup</code>中的第一个参数就是<code>props</code>。<code>setup</code>函数中的props是<code>props</code>是响应式的，当传入新的prop时，它将被更新。因为<code>props</code>是响应式的，所以我们不能对其进行解构，这样会消除它的响应式。</p>
<pre><code class="copyable">export default &#123;
  props: &#123;
    title: String
  &#125;,
  setup(props) &#123;
    console.log(props.title)
    // 对props进行解构是错误的
    const &#123; title &#125; = props
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那如果我们既想对<code>props</code>进行解构又想保持它的响应性要怎么做呢，下文中我们将会介绍。</p>
<p><strong>上下文</strong></p>
<p>传递给<code>setup</code>函数的第二个参数是<code>context</code>。<code>context</code>是一个普通的JavaScript对象，它暴露三个组件的property：</p>
<pre><code class="copyable">export default &#123;
  setup(props, context) &#123;
    // Attribute (非响应式对象),相当于this.$attrs
    console.log(context.attrs)

    // 插槽 (非响应式对象),相当于this.$slots
    console.log(context.slots)

    // 触发事件 (方法),相应于this.$emits
    console.log(context.emit)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们有说到<code>setup</code>中是没有this的，那么在<code>setup</code>中我们如何获取组件的实例呢？</p>
<p>我们可以使用<code>getCurrentInstance</code>方法，该方法只能在<code>setup</code>或者生命周期钩子中使用。</p>
<pre><code class="copyable"><template>
    <p @click="handleClick">&#123;&#123; num &#125;&#125;</p>
</template>
<script>
import &#123; ref, getCurrentInstance &#125; from 'vue'
export default &#123;
    setup() &#123;
        const num = ref(3)
        const instance = getCurrentInstance() // works
        console.log(instance)

        const handleClick = () => &#123;
            getCurrentInstance() // doesn't work
        &#125;
        return &#123; num, handleClick &#125;
    &#125;,
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印出来后，会发现有两个属性<code>ctx</code>和<code>proxy</code>,如下（仅截取部分属性）：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc2675263eb244a4b7e8417b64dfae13~tplv-k3u1fbpfcp-watermark.image" alt="code2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这便是我们想要获取的实例的内容，两者唯一的区别是<code>proxy</code>属性是响应式的。</p>
<h3 data-id="heading-2">ref、reactive、toRefs</h3>
<p>在vue2中数据都是定义在data中，那vue3怎么来定义响应式变量呢？</p>
<p>我们在上面的例子中看到了从vue中引入了一个<code>ref</code>函数声明了一个变量，该变量发生变化的时候我们的视图会随着更新。在vue3中，我们可以通过一个新的<code>ref</code>函数使任何响应式变量在任何地方起作用。<code>ref</code>接受参数并返回它包装在具有<code>value</code>的property的对象中，然后可以使用该property访问或者更改响应式变量的值，在template里可以直接访问.</p>
<pre><code class="copyable">import &#123; ref &#125; from 'vue'

const counter = ref(0)

console.log(counter) // &#123; value: 0 &#125;
console.log(counter.value) // 0

counter.value++
console.log(counter.value) // 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般<code>ref</code>是用来定义一个基本类型的响应式数据(也可用来定义引用类型的)，定义引用类型的响应式数据采用<code>reactive</code>(不可用来定义基本类型)。</p>
<p><code>reactive</code>返回对象的响应式副本。响应式转换时"深层"的-它影响所有嵌套property。</p>
<pre><code class="copyable">import &#123; reactive &#125; from 'vue'

const state = reactive(&#123; counter: 0 &#125;)
console.log(state.counter) // 0

state.counter++
console.log(state.counter) // 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原本我们在上文中有提到不能对<code>props</code>进行解构，否则会失去其响应性。这个时候我们可以使用<code>toRefs</code>来将响应式对象转换为普通对象，其中结果对象的每个property都是指向原始对象相应property的<code>ref</code>。</p>
<pre><code class="copyable">import &#123; reactive &#125; from 'vue'

const state = reactive(&#123;
  foo: 1,
  bar: 2
&#125;)

const stateAsRefs = toRefs(state)

state.foo++
console.log(stateAsRefs.foo.value) // 2

stateAsRefs.foo.value++
console.log(state.foo) // 3
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ref</code>其实还有一个作用，那就是可以获取到标签元素和组件，在vue2中，我们获取元素都是通过给元素一个<code>ref</code>属性，然后通过<code>this.$refs.xx</code>来访问，但是在vue3中已经不适用了，我们来看看vue3中怎么获取元素的：</p>
<pre><code class="copyable"><template>
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
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">生命周期钩子</h3>
<p>为了使组合式API的特性与选项式API相比更加完整，我们还需要一种在<code>setup</code>中注册生命周期钩子的方法。组合式API上的生命周期钩子与选项式API的名称相同，但前缀为<code>on</code>，如下：</p>

















































<table><thead><tr><th>选项式API</th><th>Hook inside <code>setup</code></th></tr></thead><tbody><tr><td><code>beforeCreate</code></td><td>Not needed*</td></tr><tr><td><code>created</code></td><td>Not needed*</td></tr><tr><td><code>beforeMount</code></td><td><code>onBeforeMount</code></td></tr><tr><td><code>mounted</code></td><td><code>onMounted</code></td></tr><tr><td><code>beforeUpdate</code></td><td><code>onBeforeUpdate</code></td></tr><tr><td><code>updated</code></td><td><code>onUpdated</code></td></tr><tr><td><code>beforeUnmount</code></td><td><code>onBeforeUnmount</code></td></tr><tr><td><code>errorCaptured</code></td><td><code>onErrorCaptured</code></td></tr><tr><td><code>renderTracked</code></td><td><code>onRenderTracked</code></td></tr><tr><td><code>renderTriggered</code></td><td><code>onRenderTriggered</code></td></tr></tbody></table>
<p>这些函数接受一个回调函数，当钩子被组件调用时将会被执行：</p>
<pre><code class="copyable">import &#123; onMounted &#125; from 'vue'

export default &#123;
  setup() &#123;
    // mounted
    onMounted(() => &#123;
      console.log('Component is mounted!')
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">watch 响应式更改</h3>
<p>在vue2中，如果我们想要监听某个数据的改变从而执行一些操作的时候，我们一般会使用<code>watch</code>。</p>
<pre><code class="copyable">export default &#123;
  data() &#123;
    return &#123;
      counter: 0
    &#125;
  &#125;,
  watch: &#123;
    counter(newValue, oldValue) &#123;
      console.log('The new counter value is: ' + this.counter)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue3中，我们可以使用从Vue导入的<code>watch</code>函数执行相同的操作。它接受3个参数：</p>
<ul>
<li>一个响应式引用或我们想要侦听的getter函数</li>
<li>一个回调</li>
<li>可选的配置选项</li>
</ul>
<pre><code class="copyable">import &#123; ref, reactive, watch &#125; from 'vue'

// 侦听一个getter
const state = reactive(&#123; count: 0 &#125;)
watch(
  () => state.count,
  (count, prevCount) => &#123;
    /* ... */
  &#125;
)

// 直接侦听一个ref
const count = ref(0)
watch(count, (count, prevCount) => &#123;
  /* ... */
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它还可以使用数组同时侦听多个源：</p>
<pre><code class="copyable">watch([fooRef, barRef], ([foo, bar], [prevFoo, prevBar]) => &#123;
  /* ... */
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue3中，还有个侦听器<code>watchEffect</code>，它与<code>watch</code>的不同在于它是立即执行的，同时响应式追踪其依赖，并在依赖变更时重新运行该函数。但是<code>watchEffect</code>访问不了依赖变更之前的值。</p>
<pre><code class="copyable">import &#123; ref, watchEffect &#125; from 'vue'

const count = ref(0)

watchEffect(() => console.log(count.value))
// -> logs 0

setTimeout(() => &#123;
  count.value++
  // -> logs 1
&#125;, 100)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>watch</code>和<code>watchEffect</code>均在组件的<code>setup()</code>函数或生命周期钩子被调用时，侦听器会被链接到该组件的生命周期，并在组件卸载时自动停止。也可以根据需要，显示调用返回值以停止侦听。</p>
<pre><code class="copyable">const stop = watchEffect(() => &#123;
  /* ... */
&#125;)

// later
stop()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">独立的computed属性</h3>
<p>依赖于其它状态的状态，在vue中，我们一般是用计算属性来处理的，在vue2中，计算属性使用方法如下：</p>
<pre><code class="copyable">export default &#123;
  data() &#123;
    return &#123;
      counter: 0
    &#125;
  &#125;,
  computed: &#123;
    doubleCounter() &#123;
       return this.counter * 2
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue3中，计算属性使用方法如下：</p>
<pre><code class="copyable">import &#123; ref, watchEffect &#125; from 'vue'

const count = ref(1)
const plusOne = computed(() => count.value++)

console.log(plusOne.value) // 2

plusOne.value++ // error
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者，它可以使用一个带有<code>get</code>和<code>set</code>函数的对象来创建一个可写的ref对象</p>
<pre><code class="copyable">import &#123; ref, watchEffect &#125; from 'vue'

const count = ref(1)
const plusOne = computed(&#123;
  get: () => count.value + 1,
  set: val => &#123;
    count.value = val - 1
  &#125;
&#125;)

plusOne.value = 1
console.log(count.value) // 0
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Teleport</h2>
<p><code>Teleport</code>这个单词是"传输"的意思，利用它，我们可以把子组件或者dom节点插入到任何我们想要插入的地方。</p>
<pre><code class="copyable"><template>
    <div>
        第一层包裹元素
        <div>
            第二层包裹元素
            <teleport to="#app"> 瞅瞅我在哪 </teleport>
        </div>
    </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们打开控制台看下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61a1b1743e6248389e34cebb54f7e690~tplv-k3u1fbpfcp-watermark.image" alt="code3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到我们的元素跑到了id为app的元素下，这个暂时还不理解到底什么情况下可以使用。。。</p>
<h2 data-id="heading-7">片段</h2>
<p>在vue2中，不支持多根组件，当用户意外创建多根组件时会发出警告，因此，为了修复此错误，许多组件被包装在一个<code><div></code>中。但是在vue3中，组件可以有多个根节点。</p>
<pre><code class="copyable"><template>
  <header>...</header>
  <main>...</main>
  <footer>...</footer>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">非兼容的变更</h2>
<h3 data-id="heading-9">全局API</h3>
<p>vue2有许多的全局API和配置，这些API和配置可以全局改变Vue的行为。我们定义的应用只是通过<code>new Vue()</code>创建的根Vue实例。从同。一个Vue构造函数创建的每个根实例共享相同的全局配置。这会使得同一个页面上的多个"app"之间共享同一个Vue副本变的困难。</p>
<pre><code class="copyable">// 这会影响两个根实例
Vue.mixin(&#123;
  /* ... */
&#125;)

const app1 = new Vue(&#123; el: '#app-1' &#125;)
const app2 = new Vue(&#123; el: '#app-2' &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了避免这些问题，vue3中有个新的全局API：<code>createApp</code>，调用<code>createApp</code>返回一个应用实例。</p>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'

const app = createApp(&#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>应用实例暴露当前API的子集，任何全局改变Vue行为的API都会移动到应用实例下：</p>





































<table><thead><tr><th>2.x全局API</th><th>3.x实例API(app)</th></tr></thead><tbody><tr><td>Vue.config</td><td>app.config</td></tr><tr><td>Vue.config.productionTip</td><td>removed</td></tr><tr><td>Vue.config.ignoredElements</td><td>app.config.isCustomElement</td></tr><tr><td>Vue.component</td><td>app.component</td></tr><tr><td>Vue.directive</td><td>app.directive</td></tr><tr><td>Vue.mixin</td><td>app.mixin</td></tr><tr><td>Vue.use</td><td>app.use</td></tr></tbody></table>
<pre><code class="copyable">const app = createApp(MyApp)

app.component('button-counter', &#123;
  data: () => (&#123;
    count: 0
  &#125;),
  template: '<button @click="count++">Clicked &#123;&#123; count &#125;&#125; times.</button>'
&#125;)

app.directive('focus', &#123;
  mounted: el => el.focus()
&#125;)

// 现在所有应用实例都挂载了，与其组件树一起，将具有相同的 “button-counter” 组件 和 “focus” 指令不污染全局环境
app.mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有其它不全局改变行为的全局API只能作为ES模块构建的命名导出进行访问，例如：</p>
<pre><code class="copyable">import &#123; nextTick &#125; from 'vue'

nextTick(() => &#123;
  // 一些和DOM有关的东西
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若多个应用之间需要共享配置，一种方式是创建工厂功能,如下所示：</p>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
import Foo from './Foo.vue'
import Bar from './Bar.vue'

const createMyApp = options => &#123;
  const app = createApp(options)
  app.directive('focus' /* ... */)

  return app
&#125;

createMyApp(Foo).mount('#foo')
createMyApp(Bar).mount('#bar')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，Foo和Bar实例及其后代中都可以使用<code>focus</code>指令。</p>
<h3 data-id="heading-10">v-model</h3>
<p>在vue2中，在组件上使用<code>v-model</code>相当于绑定<code>value</code>prop和<code>input</code>时间:</p>
<pre><code class="copyable"><ChildComponent v-model="pageTitle" />

<!-- 简写: -->

<ChildComponent :value="pageTitle" @input="pageTitle = $event" />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要将属性或事件名称更改为其它名称，则需要在<code>ChildComponent</code>组件中添加<code>model</code>选项(也可使用<code>v-bind.sync</code>)：</p>
<pre><code class="copyable"><!-- ParentComponent.vue -->

<ChildComponent v-model="pageTitle" />
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// ChildComponent.vue

export default &#123;
  model: &#123;
    prop: 'title',
    event: 'change'
  &#125;,
  props: &#123;
    // 这将允许 `value` 属性用于其他用途
    value: String,
    // 使用 `title` 代替 `value` 作为 model 的 prop
    title: &#123;
      type: String,
      default: 'Default title'
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，在这个例子中<code>v-model</code>的简写如下：</p>
<pre><code class="copyable"><ChildComponent :title="pageTitle" @change="pageTitle = $event" />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue3中，自定义组件上的<code>v-model</code>相当于传递了<code>modelValue</code>prop并接收抛出的<code>update:modelValue</code>事件：</p>
<pre><code class="copyable"><ChildComponent v-model="pageTitle" />

<!-- 简写: -->

<ChildComponent
  :modelValue="pageTitle"
  @update:modelValue="pageTitle = $event"
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若需要更改<code>model</code>名称，而不是修改组件内的<code>model</code>选项，那么现在我们可以将一个argument传递给<code>model</code>：</p>
<pre><code class="copyable"><ChildComponent v-model:title="pageTitle" />

<!-- 简写: -->

<ChildComponent :title="pageTitle" @update:title="pageTitle = $event" />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这也可以作为<code>.sync</code>修饰符的替代，而且允许我们在自定义组件上使用多个<code>v-model</code>。</p>
<pre><code class="copyable"><ChildComponent v-model:title="pageTitle" v-model:content="pageContent" />

<!-- 简写： -->

<ChildComponent
  :title="pageTitle"
  @update:title="pageTitle = $event"
  :content="pageContent"
  @update:content="pageContent = $event"
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11"><template v-for> 和非 - v-for 节点上 key 用法已更改</h3>
<p>特殊的 key attribute 被用于提示 Vue 的虚拟 DOM 算法来保持对节点身份的持续跟踪。这样 Vue 可以知道何时能够重用和修补现有节点，以及何时需要对它们重新排序或重新创建。</p>
<p>Vue2建议在<code>v-if</code>/<code>v-else</code>/<code>v-else-if</code> 的分支中使用 <code>key</code>。若设置了<code>key</code>在 Vue3中仍能正常工作。但是我们不再建议在 <code>v-if</code>/<code>v-else</code>/<code>v-else-if</code> 的分支中继续使用 <code>key</code> attribute，因为没有为条件分支提供 <code>key</code> 时，也会自动生成唯一的 <code>key</code>。</p>
<p>在 Vue 2中 <code><template></code> 标签不能拥有 <code>key</code>。不过你可以为其每个子节点分别设置 <code>key</code>。在 Vue 3 中 <code>key</code> 则应该被设置在 <code><template></code> 标签上。</p>
<h3 data-id="heading-12">v-if 与 v-for 的优先级对比</h3>
<p>vue2版本中在一个元素上同时使用 v-if 和 v-for 时，v-for 会优先作用。vue3版本中 v-if 总是优先于 v-for 生效。</p>
<h3 data-id="heading-13">slot具名插槽的语法</h3>
<p>在vue2中，插槽的用法如下</p>
<pre><code class="copyable">// 子组件
<slot name="content" :data="data"></slot>
export default &#123;
    data()&#123;
        return&#123;
            data:["喜羊羊","懒羊羊","美羊羊"]
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 父组件使用
<template slot="content" slot-scope="scoped">
    <div v-for="item in scoped.data">&#123;&#123;item&#125;&#125;</div>
<template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue3中父组件使用变更如下：</p>
<pre><code class="copyable">// 父组件中使用
 <template v-slot:content="scoped">
   <div v-for="item in scoped.data">&#123;&#123;item&#125;&#125;</div>
</template>

// 也可以简写成：
<template #content="&#123;data&#125;">
    <div v-for="item in data">&#123;&#123;item&#125;&#125;</div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，<code>v-slot</code>只能添加在<code><template></code>上，只有一种情况例外，那就是当被提供的内容只有默认插槽时，组件的标签才可以被当作插槽的模板来使用。这样我们就可以把<code>v-slot</code>直接用在组件上。</p>
<pre><code class="copyable"><todo-list v-slot:default="slotProps">
  <i class="fas fa-check"></i>
  <span class="green">&#123;&#123; slotProps.item &#125;&#125;</span>
</todo-list>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以这样写：</p>
<pre><code class="copyable"><todo-list v-slot="slotProps">
  <i class="fas fa-check"></i>
  <span class="green">&#123;&#123; slotProps.item &#125;&#125;</span>
</todo-list>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不带参数的<code>v-slot</code>被假定对应默认插槽。默认插槽的缩写语法不能和具名插槽混用。</p>
<h3 data-id="heading-14">被移除的语法</h3>
<p>1、vue3中不再支持数字（即键码）作为<code>v-on</code>的修饰符，例如：</p>
<pre><code class="copyable"><!-- 键码版本 -->
<input v-on:keyup.13="submit" />

<!-- 别名版本 -->
<input v-on:keyup.enter="submit" />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、<code>$on</code>，<code>$off</code> 和 <code>$once</code> 实例方法已被移除，应用实例不再实现事件触发接口。</p>
<p>在vue2中，我们经常使用<code>$bus</code>来进行组件通信，采用<code>$on</code>注册事件，<code>$emit</code>触发事件，<code>$off</code>移除事件，<code>$once</code>事件只执行一次。在Vue3中仅保留<code>$emit</code>，因为它用于触发父组件已声明方式附加的事件处理程序，其它的均移除。</p>
<p>3、过滤器已删除</p>
<p>在Vue2中我们经常使用过滤器，对我们要展示的数据进行格式处理等。在Vue3中，过滤器已移除，建议使用方法调用或者计算属性替换。</p>
<p>如果在应用中全局注册了过滤器，那就不方便在每个组件中使用计算属性或者方法来替换它了，这个时候我们可以采用全局属性。</p>
<pre><code class="copyable">// main.js
const app = createApp(App)

app.config.globalProperties.$filters = &#123;
  currencyUSD(value) &#123;
    return '$' + value
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后可以通过<code>$filters</code>对象修改所有的模板，像下面这样：</p>
<pre><code class="copyable"><template>
  <h1>Bank Account Balance</h1>
  <p>&#123;&#123; $filters.currencyUSD(accountBalance) &#125;&#125;</p>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">参考文档</h2>
<p>1、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.vue3js.cn%2Fdocs%2Fzh%2Fguide%2Finstallation.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.vue3js.cn/docs/zh/guide/installation.html" ref="nofollow noopener noreferrer">Vue3中文文档 - vuejs</a></p></div>  
</div>
            