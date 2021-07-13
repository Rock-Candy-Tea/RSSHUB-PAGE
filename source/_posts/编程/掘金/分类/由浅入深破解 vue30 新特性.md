
---
title: '由浅入深破解 vue3.0 新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04e2947e0cc64721b5f9b529223080c5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 01:03:47 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04e2947e0cc64721b5f9b529223080c5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>2020年09月18日，vue3.0正式发布。作为一个大的版本更新，Vue3.0相比于 Vue2.0，自然有着不小的变化。</p>
<p>其中，Vue3的一大核心特性是引入了Composition API（组合式API），那么相比于vue2.0，Composition API有什么不一样？</p>
<h2 data-id="heading-0">一、Composition API</h2>
<h3 data-id="heading-1">组合式 API和配置式 API有什么区别？</h3>
<h4 data-id="heading-2">vue2.0(配置式 API)</h4>
<p>在Vue2.x中，组件的主要逻辑是通过一些配置项来编写，包括一些内置的生命周期方法或者组件方法</p>
<pre><code class="copyable">export default &#123;
  name: 'test',
  components: &#123;&#125;,
  props: &#123;&#125;,
  data () &#123;
    return &#123;&#125;
  &#125;,
  created()&#123;&#125;,
  mounted () &#123;&#125;,
  watch:&#123;&#125;,
  methods: &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通常将components、data、以及各种钩子和watch分开来写，然后通过options的形式传给vue实例。</p>
<h4 data-id="heading-3">vue 3.0(组合式 API)</h4>
<p>setup() 函数是 vue3 中，专门为组件提供的新属性。它为我们使用 vue3 的 Composition API 新特性提供了统一的入口，通俗点来说就是啥玩意都能写到setup()里面。</p>
<pre><code class="copyable">import &#123; fetchGetList &#125; from '@/api/repositories'
import &#123; ref, onMounted, watch, toRefs &#125; from 'vue'

setup (props) &#123;
  const repositories = ref([])
  const getList = async () => &#123;
    repositories.value = await fetchGetList()
  &#125;
  onMounted(getUserRepositories)
  watch(getUserRepositories)
  return &#123;
    repositories,
    getUserRepositories
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">为什么要选择组合式api？</h3>
<p>我们在进行组件式编程，同一个组件内可能要写非常多的功能，比如弹框、getList、add、update之类，在vue2.0时代，我们的组件代码可能会这么写：</p>
<h4 data-id="heading-5">vue2.0</h4>
<pre><code class="copyable">export default &#123;
  name: '',
  components: &#123;
  &#125;,
  props: &#123;
  &#125;,
  data() &#123;
    return &#123;
      // 踢足球
      football: '',
      // 打篮球
      basketball: '',
      // 打台球
      ....
    &#125;
  &#125;,
  created() &#123;
    // 踢足球
    // 打篮球
  &#125;,
  methods: &#123;
    // 踢足球
    playFootball() &#123;
      console.log(this.football)
    &#125;,
    // 打篮球
    playBasketball() &#123;
      console.log(this.basketball)
    &#125;
    // 打台球
    ....
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分散在各个地方的逻辑片段，使我们的组件越来越难以阅读，经常为了看一个功能要疯狂上下滑动屏幕，在各个区块里翻找和修改。</p>
<h4 data-id="heading-6">mixins</h4>
<p>在vue2.0中还可以用mixins来进行抽象，但是用的时间长了，mixins就没那么香了</p>
<h5 data-id="heading-7">Mixins的优点：</h5>
<p>可以将代码按照功能组织区分</p>
<h5 data-id="heading-8">Mixins的缺点：</h5>
<p>存在冲突隐患，你有可能在使用过程中出现属性或函数的重名冲突</p>
<p>依赖关系不清晰，特别是在多个Mixins存在交流的情况下。</p>
<p>逻辑复用不够灵活，如果你需要在不同的组件间差异化或配置化使用Mixins的话。</p>
<h4 data-id="heading-9">vue3.0</h4>
<p>那么vue3.0的组合式 API应该怎么写呢：</p>
<pre><code class="copyable"><script>
export default &#123;
  setup(props, ctx) &#123;
    // 踢足球
    const useFootball = function()&#123;
    &#125;
    // 打篮球
    const useBasketball = function()&#123;
    &#125;
    return &#123;
      useFootball,
      useBasketball
    &#125;
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没有了各种分散的区块，我们可以写更少的代码，也更容易将可以复用的逻辑从组件里抽出到函数里。</p>
<h3 data-id="heading-10">Composition API的基础语法</h3>
<h4 data-id="heading-11">ref或者reactive代替data中的变量</h4>
<p>在Vue2.x中通过组件data的方法来定义一些当前组件的数据：</p>
<pre><code class="copyable">data() &#123;
  return &#123;
    name: 'test',
    list: [],
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在Vue3中通过ref或者reactive创建响应式对象：</p>
<pre><code class="copyable">import &#123;ref,reactive&#125; from 'vue'
...
setup()&#123;
  const name = ref('test')
  const state = reactive(&#123;
    list: []
  &#125;)
  return &#123;
      name,
      state
  &#125;
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ref将给定的值创建一个响应式的数据对象并赋值初始值（int或者string），reactive可以直接定义复杂响应式对象。为什么reactive可以定义复杂的响应式对象这个后面会有说明。</p>
<h4 data-id="heading-12">setup()中使用props和this:</h4>
<p>在Vue2.x中，组件的方法中可以通过this获取到当前组件的实例，并执行data变量的修改，方法的调用，组件的通信等等</p>
<p>但是在Vue3中，setup()在beforeCreate和created时机就已调用，无法使用和Vue2.x一样的this，但是可以通过接收setup(props,ctx)的方法，获取到当前组件的实例和props：</p>
<pre><code class="copyable">export default &#123;
  props: &#123;
    name: String,
  &#125;,
  setup(props,ctx) &#123;
    console.log(props.name)
    ctx.emit('event')
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">二、vue3.0的优化（更快、更小）</h2>
<h3 data-id="heading-14">PatchFlag(静态标记)、hoistStatic(静态提升)</h3>
<p>vue2.0的源码在处理虚拟DOM时，选择的是将template模板内的所有内容遍历，生成虚拟DOM，当有内容发生变化的时候，通过diff算法进行更新。但是HTML中除了双向绑定的动态数据，还有非常多的静态内容，每次都要参与遍历就会非常浪费性能。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04e2947e0cc64721b5f9b529223080c5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到vue3.0在生成虚拟DOM的时候，第二个 div 标签为绑定的变量，所以打上了 1 标签，代表的是 TEXT（文字），从而会将内容分为静态资源和动态内容，从而更新的时候只diff动态的部分。</p>
<p>具体的请看源码</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61e51545146347c1aff8ecfef32f62b6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们平时在开发过程中写函数的时候，定义一些写死的变量时，都会将变量提升出去定义，Vue 3.0 在这方面也做了同样的优化</p>
<p>这代表了这个变量只会被创建一次，而后只需要引用就好了，从而提升性能</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5d2f70cb34348cc89f625d0dbeffc90~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">cacheHandler(事件缓存)</h3>
<p>默认情况下 @click 事件被认为是动态变量，所以每次更新视图的时候都会追踪它的变化。</p>
<p>但是正常情况下，我们的 @click 事件在视图渲染前和渲染后，都是同一个事件，基本上不需要去追踪它的变化，所以 Vue 3.0 对此作出了相应的优化叫事件监听缓存。</p>
<p>由此可见， 设置了cacheHandler后，静态标记为8的的动态节点变成了静态节点，从而不参与diff，提升了性能。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb574d7747bf48f48c99ad8c440e9943~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e193bf749674d449d59e47b9a863acb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">响应式对象(Proxy对象与reactive)</h3>
<p>从字面意思来理解，Proxy对象是目标对象的一个代理器，任何对目标对象的操作（实例化，添加/删除/修改属性等等），都必须通过该代理器。因此我们可以把来自外界的所有操作进行拦截和过滤或者修改等操作。</p>
<p>引用大佬的例子来展示下Proxy对象的功能：</p>
<pre><code class="copyable">let foo = &#123;
    a:1,
    b:2
&#125;
let handler = &#123;
    set:(obj,key,value)=>&#123;
        console.log('set')
        obj[key] = value
        return true
    &#125;
&#125;

let p = new Proxy(foo,handler)

p.a = 3 // 打印出console.log('set')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相信所有的前端面试的时候都被问过这个问题，vue的双向数据绑定是怎么实现的？</p>
<p>标准答案应该都差不多：</p>
<p>Vue实现数据双向绑定主要利用的就是: 数据劫持和发布订阅模式。所谓数据劫持，就是利用JavaScript的访问器属性，即Object.defineProperty()方法，当对对象的属性进行赋值时，Object.defineProperty就可以通过set方法劫持到数据的变化，然后通知发布者(主题对象)去通知所有观察者，观察者收到通知后，就会对视图进行更新。</p>
<p>在Vue2.x中，使用Object.defineProperty()来实现响应式对象，对于一些复杂的对象，还需要循环递归的给每个属性增加上getter/setter监听器，这使得组件的初始化非常耗时。vue3中，composition-api提供了一种创建响应式对象的方法reactive，其内部就是利用了Proxy API来实现的，这样就可以不用针对每个属性来一一进行添加，减少开销提升性能。</p>
<h4 data-id="heading-17">reactive的源码</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0539ce164da642888b000fbbfdc09b6c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>vue3.0更新的核心功能除了上面的内容，还包括Tree shaking支持、以及对typescript的支持，以及Fragments、等等小的东西，当然还有最重要的vite，都是值得了解一下的。</p></div>  
</div>
            