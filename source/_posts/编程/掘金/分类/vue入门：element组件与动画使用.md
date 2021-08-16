
---
title: 'vue入门：element组件与动画使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5509'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 01:41:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=5509'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与 8 月更文挑战的第 15 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
</blockquote>
<p>本教程为入门教程，如有错误，请各位前端大佬指出。</p>
<h2 data-id="heading-0">1.什么是Element</h2>
<p>Element，一套为开发者、设计师和产品经理准备的基于 Vue 2.0 的桌面端组件库，封装很多常用组件，官网是<a href="https://link.juejin.cn/?target=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN%2Fcomponent%2Finstallation" target="_blank" rel="nofollow noopener noreferrer" title="https://element.eleme.cn/#/zh-CN/component/installation" ref="nofollow noopener noreferrer">element.eleme.cn/#/zh-CN/com…</a>，下面就简单介绍 element。</p>
<blockquote>
<p>当你访问官网，发现无数已经封装好了的页面，而且样式多样，一般可以满足大部分的业务需求，如果你是业务开发，直接复制粘贴，然后在复制好的代码上补充字段也填写业务即可了。</p>
</blockquote>
<h3 data-id="heading-1">1.安装和引入</h3>
<p>如果想使用Element，那么需要下载和安装element-ui的类库，否则会抛出异常。</p>
<pre><code class="copyable">npm i element-ui -S
npm install babel-plugin-component -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，将.babelrc文件修改为：</p>
<pre><code class="copyable">&#123;
  "presets": [
    ["env", &#123;
      "modules": false,
      "targets": &#123;
        "browsers": ["> 1%", "last 2 versions", "not ie <= 8"]
      &#125;
    &#125;],
    "stage-2"
  ],
  "plugins": ["transform-vue-jsx", "transform-runtime"],
  "env": &#123;
    "test": &#123;
      "presets": ["env", "stage-2"],
      "plugins": ["transform-vue-jsx", "transform-es2015-modules-commonjs", "dynamic-import-node", [
        "component",
        &#123;
          "libraryName": "element-ui",
          "styleLibraryName": "theme-chalk"
        &#125;
      ]]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2.使用</h3>
<p>接下来，如果你只希望引入部分组件，比如 Button 和 Select，那么需要在 main.js 中写入以下内容，证明你想使用引入的组件：</p>
<pre><code class="copyable">// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
//element组件相关配置
import &#123; Button, Select, Option &#125; from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(Button)
Vue.use(Select)
Vue.use(Option)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue(&#123;
    el: '#app',
    router,
    components: &#123; App &#125;,
    template: '<App/>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后将代码直接复制过来，将字段对应同时加入业务即可。</p>
<pre><code class="copyable"><template>
<el-select v-model="value" filterable placeholder="请选择">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
</template>

<script>

export default &#123;
name: 'HelloWorld2',
data() &#123;
      return &#123;
        options: [&#123;
          value: '选项1',
          label: '黄金糕'
        &#125;, &#123;
          value: '选项2',
          label: '双皮奶'
        &#125;, &#123;
          value: '选项3',
          label: '蚵仔煎'
        &#125;, &#123;
          value: '选项4',
          label: '龙须面'
        &#125;, &#123;
          value: '选项5',
          label: '北京烤鸭'
        &#125;],
        value: ''
      &#125;
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>通过element，我们就不用自己编写页面了，大大减少了工作量，同时方式也比较不错。上文仅仅使用按钮作为演示，其他组件请自行测试。</p>
</blockquote>
<h2 data-id="heading-3">2.动画</h2>
<p> Vue 在插入、更新或者移除 DOM 时，提供多种不同方式的应用过渡效果，在此过程中，就会形成动画。
动画使用包括以下工具：</p>
<ul>
<li>在 CSS 过渡和动画中自动应用 class</li>
<li>可以配合使用第三方 CSS 动画库，如 Animate.css</li>
<li>在过渡钩子函数中使用 JavaScript 直接操作 DOM</li>
<li>可以配合使用第三方 JavaScript 动画库，如 Velocity.js</li>
</ul>
<p>下面简单做一下动画的实例</p>
<h3 data-id="heading-4">1.隐藏显示</h3>
<p>点击一次字体隐藏，再次点击字体显示，以下附上代码。</p>
<pre><code class="copyable">app.vue
<template>
  <div id="app">
    <anim/>
  </div>
</template>

<script>
import anim from './components/anim.vue'

export default &#123;
  name: 'App',
  components:&#123;
   anim
  &#125;,
  data () &#123;
  return &#123;
 &#125;
&#125;,
  methods: &#123;
   clickButton(event)&#123;
     if(this.stutas ==HelloWorld)&#123;
         this.stutas = HelloWorld2
     &#125;else&#123;
         this.stutas = HelloWorld
     &#125;
   &#125;
&#125;,
&#125;
</script>

<style>

</style>

Anim.vue
<template>
<div id="demo">
  <button v-on:click="show = !show">
    Toggle
  </button>
  <!-- 动画必备 -->
  <transition name="demo">
    <p v-if="show">hello</p>
  </transition>
</div>
</template>

<script>
export default &#123;
name: 'anim',
data () &#123;
  return &#123;
    show: true
&#125;
&#125;,
methods: &#123;
    clickButton()&#123;
    &#125;
&#125;
&#125;
</script>

<style>
.demo-enter-active, .demo-leave-active &#123;
  transition: opacity 5s;
&#125;
.demo-enter, .demo-leave-to /* .fade-leave-active below version 2.1.8 */ &#123;
  opacity: 0;
&#125;

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.移动</h3>
<p>点击一次字体右移，再次点击字体左移。下文附上代码。</p>
<pre><code class="copyable"><template>
<div id="demo">
  <button v-on:click="show = !show">
    Toggle
  </button>
  <!-- 动画必备 -->
  <transition name="demo">
    <p class = "myDemo" v-if="show">hello</p>
  </transition>
</div>
</template>

<script>
export default &#123;
name: 'anim',
data () &#123;
  return &#123;
    show: true
&#125;
&#125;,
methods: &#123;
    clickButton()&#123;
    &#125;
&#125;
&#125;
</script>

<style>
.demo-enter-active, .demo-leave-active &#123;
    transition: all .5s ease;
&#125;

.demo-enter, .demo-leave-to /* .fade-leave-active below version 2.1.8 */ &#123;
  transform: translateX(100px);;
&#125;

.demo-enter-to, .demo-leave /* .fade-leave-active below version 2.1.8 */ &#123;
  transform: translateX(0px);;
&#125;

.myDemo&#123;
  position:absolute;
  left:50px
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在进入/离开的过渡中，会有 6 个 class 切换。</p>
<ul>
<li><code>v-enter</code>：定义进入过渡的开始状态。在元素被插入之前生效，在元素被插入之后的下一帧移除。</li>
<li><code>v-enter-active</code>：定义进入过渡生效时的状态。在整个进入过渡的阶段中应用，在元素被插入之前生效，在过渡/动画完成之后移除。这个类可以被用来定义进入过渡的过程时间，延迟和曲线函数。</li>
<li><code>v-enter-to</code>：<strong>2.1.8 版及以上</strong>定义进入过渡的结束状态。在元素被插入之后下一帧生效 (与此同时 <code>v-enter</code> 被移除)，在过渡/动画完成之后移除。</li>
<li><code>v-leave</code>：定义离开过渡的开始状态。在离开过渡被触发时立刻生效，下一帧被移除。</li>
<li><code>v-leave-active</code>：定义离开过渡生效时的状态。在整个离开过渡的阶段中应用，在离开过渡被触发时立刻生效，在过渡/动画完成之后移除。这个类可以被用来定义离开过渡的过程时间，延迟和曲线函数。</li>
<li><code>v-leave-to</code>：<strong>2.1.8 版及以上</strong>定义离开过渡的结束状态。在离开过渡被触发之后下一帧生效 (与此同时 <code>v-leave</code> 被删除)，在过渡/动画完成之后移除。</li>
</ul>
<h3 data-id="heading-6">3.使用第三方库</h3>
<p>这里推荐的第三方库为Animate。首页： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdaneden.github.io%2Fanimate.css%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://daneden.github.io/animate.css/" ref="nofollow noopener noreferrer">daneden.github.io/animate.css…</a>。
Animate.css是一个随时可用的跨浏览器动画库，可用于您的 Web 项目。非常适合强调、主页、滑块和注意力引导提示。下文将简单介绍animate.css的基础用法。</p>
<h4 data-id="heading-7">1.index.html引入组件</h4>
<p>相同道里，需要引入组件才能使用。</p>
<pre><code class="copyable"><!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/animate.css@3.5.1" rel="stylesheet" type="text/css">
    <title>project</title>
</head>

<body>
    <div id="app"></div>
    <!-- built files will be auto injected -->
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">2.引入div</h4>
<p>然后获取官网文档的样式，直接使用即可。</p>
<pre><code class="copyable"><template>
<div id="example-3">
  <button @click="show = !show">
    Toggle render
  </button>
  <transition
    name="custom-classes-transition"
    enter-active-class="animated zoomOutRight"
    leave-active-class="animated fadeInDownBig"
  >
    <p v-if="show">hello</p>
  </transition>
</div>
</template>

<script>
export default &#123;
name: 'anim',
data () &#123;
  return &#123;
    show: true
&#125;
&#125;,
methods: &#123;
&#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如有其他需要也可以参考文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fanimate.style%2F%23documentation" target="_blank" rel="nofollow noopener noreferrer" title="https://animate.style/#documentation" ref="nofollow noopener noreferrer">animate.style/#documentat…</a></p></div>  
</div>
            