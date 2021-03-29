
---
title: 'vue3 正式版开发体验心得！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4514'
author: 掘金
comments: false
date: Sun, 28 Mar 2021 19:26:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=4514'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近使用Vue3+elmentPlus 开发了项目，收获的体验心得。</p>
<h4 data-id="heading-0">1. 安装</h4>
<pre><code class="copyable">yarn install vue@3 vuex@4 vue-router@4
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2. Options API 和 Composition API</h4>
<h5 data-id="heading-2">Options API 问题</h5>
<ul>
<li>在特定的区域（data，methods，watch，computed...）编写负责相同功能的代码。
随着业务复杂度越来越高，代码量会不断的加大，后续维护非常的复杂，代码可复用性也不高。</li>
</ul>
<h5 data-id="heading-3">Composition API</h5>
<p>特点：使用 composition api 可以更加优雅的组织代码、函数，让相关功能的代码更加有序的组织在一起</p>
<ul>
<li>Vue 核心团队将 Composition API 描述为“一组基于功能的附加 API，可以灵活地组合组件逻辑”</li>
<li>使用 Composition API 编写的代码更易读，而且没有任何幕后的魔力，更容易阅读和学习</li>
</ul>
<h4 data-id="heading-4">3. 核心：setup()</h4>
<ul>
<li>执行时机：在 beforeCreate 钩子之前被调用</li>
<li>setup()中没有了 this，this 为 undefined</li>
<li>setup 的意义：让你对模块的逻辑进行细化提取，以便于让你的组件更为通用，更容易封装，从而减少代码量。</li>
</ul>
<h4 data-id="heading-5">5. 生命周期函数和响应式数据使用</h4>
<ul>
<li>1）原 data 中定义的属性，改为使用 ref() 和 reactive()</li>
<li>2）原 computed 中定义的属性，改为使用 computed()</li>
<li>3）原 methods 中定义的方法，改为使用 setup()中定义，并且由 setup()返回</li>
<li>4）原 watch 中定义的被观察属性，改为使用 watchEffect()</li>
</ul>
<pre><code class="copyable"><template>
  <div ref="content">test content</div>
</template>;

import &#123; ref, reactive, onBeforeUpdate, onUpdated, onMounted, onUnmounted, computed, watch, watchEffect &#125; from "vue";
export default &#123;
  props:&#123;
    status:&#123;
      type: Number,
      default:0
    &#125;
  &#125;,
  setup(props, context) &#123;
    console.log(this) // undefined
    // Attribute (非响应式对象)
    console.log(context.attrs)

    // 插槽 (非响应式对象)
    console.log(context.slots)

    // 触发事件 (方法)
    console.log(context.emit)

    let name = ref("ifredom")
    const contentDom = ref("content") // 获取dom
    const arr1 = ref([])
    const arr2 = reactive(&#123;
      arr: []
    &#125;)
    const arr3 = reactive([])
    const ceo = reactive(&#123;
      name: "雷军",
      sex: "man",
      age: 44,
    &#125;);

    // computed  使用
    const workAge = computed(() => &#123;
      console.log("工作十年后");
      return ceo.age + 10;
    &#125;);

    // 监听单一数据源，此处为 name
    watch(name, (newVal, oldVal) => &#123;
      console.log("name改变了")
      console.log(name.value)
    &#125;)

    // 监听函数内所有数据源
    const stop = watchEffect(() => &#123;
      console.log("name改变了")
      console.log(name.value)
    &#125;)

    // 调用，则选择停止监听
    // stop()

    // 生命周期函数
    onBeforeMount(() => &#123;
      console.log("onBeforeMount---")
    &#125;)

    onMounted(() => &#123;
      console.log('onMounted---')
    &#125;)

    onBeforeUpdate(() => &#123;
      console.log('onBeforeUpdate---')
    &#125;)

    onUpdated(() => &#123;
      console.log('onUpdated---')
    &#125;)

    onUnmounted(() => &#123;
      console.log('onUnmounted---')
    &#125;)

    // 捕获子孙组件被调用错误 （err, vm, info）
    onErrorCaptured(() => &#123;
      console.log('onErrorCaptured---')
    &#125;)

    // 捕获渲染栈异常
    onRenderTracked(() => &#123;
      console.log('onRenderTracked---')
    &#125;)

    // 渲染识别
    onRenderTriggered(() => &#123;
      console.log('onRenderTriggered---')
    &#125;)

    // 数组赋值 - object 对象赋值同理
    // 方法1
      arr1.value = [1, 2, 3]
    // 方法2
      arr2.arr = [1, 2, 3]
    // 方法3
      arr3.push(...[1, 2, 3])

    // methods 函数使用
    function fetchUserInfo()&#123;
      console.log("查询用户信息")
    &#125;


    return &#123;
      // 返回 (当你在template中用到此方法时才需要返回，否则不用)
      name,
      contentDom,
      arr1,
      arr2,
      arr3,
      ceo,
      fetchUserInfo,
    &#125;
  &#125;,
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">6. 全局属性 和 Vuex 使用</h4>
<pre><code class="copyable">import &#123; nextTick, inject, getCurrentInstance&#125; from "vue"
import &#123; useStore &#125; from "vuex"
import &#123; useRoute &#125; from "vue-router"

export default &#123;
  setup() &#123;
    // nextTick 使用
    nextTick(()=>&#123;
      console.log('Now DOM is updated')
    &#125;)

    const route = useRoute(); // route 使用
    const store = useStore()

    // vuex4中的定义方式与vuex3中一模一样
    // 获取 user 定义的 state 中的 roles 属性
    const roles = store.state.user.roles
    // 结合 computed 使用
    const sidebar = computed(() => store.state.app.sidebar)

    // 方法一：全局注入属性（provide）
    // 在 main.js 中 从 vue 导出 provide 再使用：app.provide('Platform', '移动端')
    // 组件中获取 Platform
    const platform = inject('Platform') // '移动端'

    // 方法二：挂载到全局实例属性上（globalProperties）
    //在 main.js 中： app.config.globalProperties.Platform = '移动端'
    const &#123; ctx &#125; = getCurrentInstance() // 获取当前实例
    // 与以前this获取原型上东西一样
    // ctx.$parent  父组件
    // ctx.$nextTick  组件更新完毕
    // ctx.$store  VueX
    // 组件中获取 Platform
    console.log(ctx.Platform)

    return &#123;
      roles,
      sidebar,
      platform
    &#125;;
  &#125;,
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            