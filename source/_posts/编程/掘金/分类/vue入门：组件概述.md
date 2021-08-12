
---
title: 'vue入门：组件概述'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1327'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 16:46:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=1327'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>组件这是我参与 8 月更文挑战的第 12 天，活动详情查看： 8月更文挑战</p>
<p>是一个自定义元素或称为一个模块，包括所需的模板、逻辑和样式。在HTML模板中，组件以一个自定义标签的形式存在，起到占位符的功能。通过Vue.js的声明式渲染后，占位符将会被替换为实际的内容。我们可以在一个通过 <code>new Vue</code> 创建的 Vue 根实例中，把这个组件作为自定义元素来使用。\</p>
<h3 data-id="heading-0">1.组件的生命周期</h3>
<p>通过运行以下代码，可以清晰的看到组件的生命周期日志。建议执行，了解一下。</p>
<pre><code class="copyable"><template>
<div>
    <button v-on:click = "clickButton" name = "button" type = "button">按钮</button>
    &#123;&#123;message&#125;&#125;
</div>
</template>

<script>
export default &#123;
name: 'ComponentDemo',
data () &#123;
  return &#123;
    message:"改变之前"
&#125;
&#125;,
methods: &#123;
    clickButton()&#123;
      this.message = "改变之后"
    &#125;
&#125;,
//组件被创建之前
beforeCreate() &#123;
    console.log("组件被创建之前")
&#125;,
created() &#123;
    console.log("组件被创建之后")
&#125;,
beforeMount() &#123;
    console.log("组件被渲染之前")
&#125;,
mounted() &#123;
    console.log("组件被渲染之后")
&#125;,
beforeUpdate() &#123;
    console.log("数据改变渲染之前")
&#125;,
updated() &#123;
    console.log("数据改变渲染之后")
&#125;,
beforeDestroy() &#123;
    console.log("销毁之前")
&#125;,
destroyed() &#123;
    console.log("销毁之后")
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2.简单组件使用</h3>
<p>组件可以理解为在一个页面引用另一个页面，以下介绍简单的组件使用方式。</p>
<pre><code class="copyable">组件
<template>
<div>
  我是组件啊
</div>
</template>

<script>
export default &#123;
name: 'demoOne',
el: '#app',
data () &#123;
  return &#123;
&#125;
&#125;
&#125;
</script>

<style scoped>
</style>

主页
<template>
<div>
  我是主页
  <demoOne/>
</div>
</template>

<script>
import demoOne from './demoOne.vue'

export default &#123;
name: 'HelloWorld',
el: '#app',
data () &#123;
  return &#123;
&#125;
&#125;,
components:&#123;
  demoOne
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">4.父传子</h3>
<p>prop 是子组件用来接受父组件传递过来的数据的一个自定义属性。
父组件的数据需要通过 props 把数据传给子组件，子组件需要显式地用 props 选项声明 "prop"：</p>
<pre><code class="copyable">app.vue
<template>
  <div id="app">
    <parent/>
  </div>
</template>

<script>
import parent from './components/parent.vue'

export default &#123;
  name: 'App',
  components:&#123;
   parent
  &#125;
&#125;
</script>

<style>

</style>

parent.vue
<template>
<div>
  <p>我是父亲</p>
  <son title="你好儿子" v-bind:thing = "thing"/>
</div>
</template>

<script>
import son from './son.vue'
export default &#123;
name: 'parent',
data () &#123;
  return &#123;
      thing:"给你钱"
&#125;
&#125;,
components:&#123;
    son
&#125;
&#125;
</script>

<style>
</style>


son.vue
<template>
<div>
  我是儿子
  父亲对我说&#123;&#123;title&#125;&#125;-&#123;&#123;thing&#125;&#125;-&#123;&#123;age&#125;&#125;
</div>
</template>

<script>
export default &#123;
name: 'son',
data () &#123;
  return &#123;
&#125;
&#125;,
props:&#123;
    title:String,
    thing:String,
    age: &#123;
      type: Number,
      default: 100
    &#125;
&#125;
&#125;
</script>

<style scoped>
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">5.父传子的值验证</h3>
<p>组件可以为 props 指定验证要求。
为了定制 prop 的验证方式，你可以为 props 中的值提供一个带有验证需求的对象，而不是一个字符串数组。</p>
<pre><code class="copyable">props: &#123;
    // 基础的类型检查 (`null` 和 `undefined` 会通过任何类型验证)
    propA: Number,
    // 多个可能的类型
    propB: [String, Number],
    // 必填的字符串
    propC: &#123;
      type: String,
      required: true
    &#125;,
    // 带有默认值的数字
    propD: &#123;
      type: Number,
      default: 100
    &#125;,
    // 带有默认值的对象
    propE: &#123;
      type: Object,
      // 对象或数组默认值必须从一个工厂函数获取
      default: function () &#123;
        return &#123; message: 'hello' &#125;
      &#125;
    &#125;,
    // 自定义验证函数
    propF: &#123;
      validator: function (value) &#123;
        // 这个值必须匹配下列字符串中的一个
        return ['success', 'warning', 'danger'].indexOf(value) !== -1
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">6.子传父</h3>
<p>与上文相反，子组件传递值到父组件。</p>
<pre><code class="copyable">app.vue
<template>
  <div id="app">
    <parent/>
  </div>
</template>

<script>
import parent from './components/parent.vue'

export default &#123;
  name: 'App',
  components:&#123;
   parent
  &#125;
&#125;
</script>

<style>

</style>


parent.vue
<template>
<div>
  <p>我是父亲</p>
  <son v-on:getMessage = "getMsg" title="你好儿子"/>
  儿子跟我说话了&#123;&#123;msg&#125;&#125;
</div>
</template>

<script>
import son from './son.vue'
export default &#123;
name: 'parent',
data () &#123;
  return &#123;
      msg:null
&#125;
&#125;,
components:&#123;
    son
&#125;,
methods: &#123;
    getMsg(data)&#123;
        this.msg = data
    &#125;
&#125;
&#125;
</script>

<style>
</style>


son.vue
<template>
<div>
  <button v-on:click = "sendMessage" name = 'button' type = "button">说话</button>
</div>
</template>

<script>
export default &#123;
name: 'son',
data () &#123;
  return &#123;
    message:"你好父亲"
&#125;
&#125;,
methods: &#123;
    sendMessage(event)&#123;
        this.$emit("getMessage",this.message);
    &#125;
&#125;
&#125;
</script>

<style scoped>
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">7.插槽</h3>
<p>插槽内可以是任意内容。如果子组件没有使用插槽，父组件如果需要往子组件中填充模板或者html, 是没法做到的。
下文介绍普通插槽和具名插槽的使用方法。</p>
<pre><code class="copyable">app.vue
<template>
  <div id="app">
    <HelloWorld>
          <!-- 依然在父组件中渲染 -->
          <!--普通插槽-->
          <!--   <p>我是父亲你好插槽</p>    -->
          <!-- 具名插槽 -->
          <div slot ="demo">
             <p>aaaa</p>
             <p>bbbb</p>
             <p>cccc</p>
          </div>
          <p slot = "demo2">&#123;&#123;message&#125;&#125;</p>
          <!-- 接收儿子传递的 -->
          <p slot = "demo3" slot-scope = "props">&#123;&#123;props.text&#125;&#125;</p>
    </HelloWorld>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default &#123;
  name: 'App',
  components:&#123;
   HelloWorld
  &#125;,
  data () &#123;
  return &#123;
    message:"this is message"
 &#125;
&#125;
&#125;
</script>

<style>

</style>

HelloWorld.vue
<template>
<div>
   <!--   父亲的数据在儿子中显示  -->
   <!--   <slot>普通插槽</slot>   -->
   <slot name= "demo">具名插槽1</slot>
   <slot name= "demo2">具名插槽2</slot>
   <!--   儿子传递给父亲  -->
   <slot name= "demo3" v-bind:text = "message">儿到父</slot>
</div>
</template>

<script>
import demoOne from './demoOne.vue'

export default &#123;
name: 'HelloWorld',
data () &#123;
  return &#123;
     message:"儿子到父亲"
&#125;
&#125;,
components:&#123;
  demoOne
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">8.缓存keep-alive</h3>
<p>重新创建动态组件的行为通常是非常有用的，但是在这个案例中，我们更希望那些标签的组件实例能够被在它们第一次被创建的时候缓存下来。为了解决这个问题，我们可以用一个 <code><keep-alive></code> 元素将其动态组件包裹起来。</p>
<pre><code class="copyable">app.vue
<template>
  <div id="app">
    <button v-on:click = "clickButton" name = "button" type = "button">切换</button>
    <!-- 可以尝试去掉keep-alive -->
    <keep-alive>
        <!-- 失活的组件将会被缓存！-->
        <component v-bind:is="stutas"></component>
    </keep-alive>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import HelloWorld2 from './components/HelloWorld2.vue'

export default &#123;
  name: 'App',
  components:&#123;
   HelloWorld,
   HelloWorld2
  &#125;,
  data () &#123;
  return &#123;
    stutas:HelloWorld
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


HelloWorld.vue
<template>
<div>
      <button v-on:click = "clickButton1" name = "button" type = "button">1组件切换</button>
      &#123;&#123;content&#125;&#125;
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld',
data () &#123;
  return &#123;
    content:"组件1"
    &#125;
&#125;,
methods:&#123;
  clickButton1(event)&#123;
         this.content = "我刚刚点击了"
  &#125;
&#125;
&#125;
</script>

HelloWorld2.vue
<template>
<div>
   HelloWorld2
</div>
</template>

<script>

export default &#123;
name: 'HelloWorld2',
data () &#123;
  return &#123;
&#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            