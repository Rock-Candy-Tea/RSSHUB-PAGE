
---
title: 'vue实现自己的ui组件并发布到npm'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/334cb62fc9ff49d484a8202a4f9b2413~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 22:57:08 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/334cb62fc9ff49d484a8202a4f9b2413~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>很多时候我们不需要自己造轮子，但是也可能有某些特殊情况，我们希望有自定义的ui组件。这里我用vue做一个基础的button组件并发布到npm，接着尝试使用这个ui组件。</p>
</blockquote>
<h3 data-id="heading-0">需要前置</h3>
<ul>
<li>vue-cl3</li>
<li>npm账号密码</li>
</ul>
<pre><code class="copyable">npm install -g @vue/cli
# OR
yarn global add @vue/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">创建项目</h3>
<p>执行<code>vue curete bkyz-ui</code><br>
手动选择功能模块<code>Manually select features</code></p>
<pre><code class="copyable"> (*) Babel
 ( ) TypeScript
 ( ) Progressive Web App (PWA) Support
 ( ) Router
 ( ) Vuex
 (*) CSS Pre-processors
 (*) Linter / Formatter
 ( ) Unit Testing
 ( ) E2E Testing
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按空格是选择，回车就进入下一步了。</p>
<p>剩下的选择项我的选择是：</p>
<p>代码风格--》 ESLint + Standard config<br>
格式检测--》 Lint on Save<br>
配置文件生成方式--》 In package.json<br>
是否保存预配置--》否</p>
<p>配置看个人喜好，然后按回车，生成一个完整的项目。</p>
<p>在根目录中创建一个packages目录用来存放我们要开发的UI组件；在根目录创建一个local目录,用于测试引用我们自己开发的UI组件的效果。 由于我们更改了原项目的目录结构，使得系统本地运行以及打包找不到对应的目录，我们需要在项目的根目录中创建一个vue.config.js文件夹手动的去修改webpack配置，使得系统本地运行和打包正常。</p>
<pre><code class="copyable">// vue.config.js
const path = require('path');
module.exports = &#123;
    pages: &#123;
        index: &#123;
            entry: 'local/main.js',
            template: 'public/index.html',
            filename: 'index.html'
        &#125;
    &#125;,
    chainWebpack: config => &#123;
        config.module
        .rule('js')
        .include.add(path.resolve(__dirname, 'packages')).end()
        .use('babel')
        .loader('babel-loader')
        .tap(options => &#123;
            return options;
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">制作组件</h3>
<p>在packages文件夹内新建两个文件夹button，fonts和一个index.js文件。
编辑<code>packages/index.js</code></p>
<pre><code class="copyable">// packages/index.js
import Button from './button'

import './fonts/font.scss'
// 存储组件列表
const components = [
  Button
]

// 定义 install 方法，接收 Vue 作为参数。如果使用 use 注册插件，则所有的组件都将被注册
const install = function (Vue) &#123;
  // 遍历注册全局组件
  components.forEach(component => &#123;
    Vue.component(component.name, component)
  &#125;)
&#125;

// 判断是否是直接引入文件
if (typeof window !== 'undefined' && window.Vue) &#123;
  install(window.Vue)
&#125;
export default &#123;
// 导出的对象必须具有 install，才能被 Vue.use() 方法安装
  install,
  Button
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>button文件夹内新建index.js用于导出组件</p>
<pre><code class="copyable">import Button from './src/button.vue'
// 为组件提供 install 安装方法，供按需引入
Button.install = function (Vue) &#123;
  Vue.component(Button.name, Button)
&#125;
export default Button
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编辑<code>packages/button/src/button.vue</code></p>
<pre><code class="copyable"><template>
  <button
    class="mc-button">
    <!-- 如果没有传入插槽的时候才显示 -->
    <span v-if="$slots.default"><slot></slot></span>
  </button>
</template>
export default &#123;
  name: 'McButton',
  props: &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后新建src文件夹，放button组件，这就是个普通的vue文件，后续会持续加入一些属性来完善这个组件。</p>
<h4 data-id="heading-3">button type</h4>
<p>常见的类型有：primary / success / warning / danger / info / text</p>
<p>我们采用动态类型绑定的数组形式</p>
<pre><code class="copyable"><template>
<button 
    class="mc-button" 
    :class="[
      `mc-button--$&#123;type&#125;`
    ]">
    ...
</button>
</template>
<script>
export default &#123;
  ...
  props: &#123;
    type: &#123;
      type: String,
      default: 'default'
    &#125;
  &#125;
&#125;
</script>
<style lang="scss'>
.mc-button &#123;
  display: inline-block;
  line-height: 1;
  white-space: nowrap;
  cursor: pointer;
  background: #fff;
  border: 1px solid #dcdfe6;
  color: #606266;
  -webkit-appearance: none;
  text-align: center;
  box-sizing: border-box;
  outline: none;
  margin: 0;
  transition: 0.1s;
  font-weight: 500;
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
  padding: 12px 20px;
  font-size: 14px;
  border-radius: 4px;
  &:hover,
  &:focus &#123;
    color: #409eff;
    border-color: #c6e2ff;
    background-color: #ecf5ff;
  &#125;
  &--primary &#123;&#125;
  &--success &#123;&#125;
  &--warning &#123;&#125;
  &--info &#123;&#125;
  &--danger &#123;&#125;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就实现了不同type的button样式</p>
<h4 data-id="heading-4">添加圆角</h4>
<pre><code class="copyable"><button 
    class="mc-button" 
    :class="[
      `mc-button--$&#123;type&#125;`,
      &#123;
            ...
            'is-round': round
       &#125;
    ]">
    ...
</button>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>再增加一个round入参,此处略过，再增加圆角的样式</p>
<pre><code class="copyable">&.is-round &#123;
    border-radius: 20px;
    padding: 12px 23px;
 &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>类似的可以实现圆形按钮，是否禁用，添加图标，这里就不细写。</p>
<pre><code class="copyable"><template>
  <button
    class="mc-button"
    :disabled="disabled"
    @click="handleClick"
    :class="[
      `mc-button--$&#123;type&#125;`,
      &#123;
        'is-plain': plain,
        'is-round': round,
        'is-circle': circle,
        'is-disabled': disabled
      &#125;
    ]">
    <i :class="icon" v-if="icon"></i>
    <!-- 如果没有传入插槽的时候才显示 -->
    <span v-if="$slots.default"><slot></slot></span>
  </button>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">运行项目</h3>
<p>现在本地跑起来，看看效果。完善之前的local文件夹内容，新增App.vue，man.js，TestButton.vue三个文件。<br>
<code>App.vue</code>从testButton中引入了McButton组件并展示</p>
<pre><code class="copyable">// local/App.vue
<template>
  <div id="app">
    <test-buttons></test-buttons>
  </div>
</template>

<script>
import TestButtons from './TestButton'
export default &#123;
  name: 'app',
  components: &#123;
    TestButtons
  &#125;
&#125;
</script>

<style lang="scss">
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>main.js</code>是入口文件</p>
<pre><code class="copyable">// local/main.js
import Vue from 'vue'
import App from './App.vue'
// 导入组件库
import BkyzUI from '../packages'

Vue.config.productionTip = false

Vue.use(BkyzUI)

new Vue(&#123;
  render: h => h(App)
&#125;).$mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在引入了packages的组件库后，TestButton.vue可以直接使用<code>mc-button</code></p>
<pre><code class="copyable"><template>
  <div class="app">
    <div class="row">
      <mc-button>按钮</mc-button>
      <mc-button type="primary">按钮</mc-button>
      <mc-button type="success">按钮</mc-button>
      <mc-button type="info">按钮</mc-button>
      <mc-button type="warning">按钮</mc-button>
//      ...
    </div>
  </div>
</template>

<script>
export default &#123;
  name: 'TestButtons'
  methods: &#123;
  &#125;
&#125;
</script>

<style lang="scss" scoped>
.app &#123;
    width: 600px;
    height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 100px;
&#125;
.row &#123;
  padding: 10px 0;
&#125;
.mc-button &#123;
  margin-left: 10px;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在执行<code>npm run serve</code>之后打开页面可以看到外面自定义的组件在项目内是可以正常使用了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/334cb62fc9ff49d484a8202a4f9b2413~tplv-k3u1fbpfcp-watermark.image" alt="Screen Shot 2021-08-12 at 2.28.44 PM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">打包</h3>
<p>在Vue-cli3的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2F" title="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2F" target="_blank">官方文档</a> 中有个<code>构建目标</code>有明确的说明怎么打包成一个应用或者一个库！此时，我们需要在package.json中添加一条打包命令</p>
<pre><code class="copyable">vue-cli-service build --target lib 指定打包的文件
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后控制台执行<code>yarn lib</code> 即可将外面的组件库包括字体图标一起打包生成一个dist文件夹。</p>
<p>由于我们开发的组件库是给别人用的，我们没有必要把所有的代码都发布到npm上。所以我们需要在项目的根目录创建一个.npmignore的文件，忽略那些文件上传</p>
<pre><code class="copyable">// .npmignore
# 忽略目录
local/
packages/
public/
 
# 忽略指定文件
vue.config.js
babel.config.js
*.map
.editorconfig.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编辑<code>package.json</code>,添加main方便其他人下载时找到对应打包的文件</p>
<pre><code class="copyable">&#123;
 "main": "dist/bkyz-ui.umd.min.js",
 ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>我的git仓库 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdzhiqin%2Fbkyz-ui.git" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dzhiqin/bkyz-ui.git" ref="nofollow noopener noreferrer">点击</a></p>
</blockquote>
<p><strong>注意点：</strong></p>
<ul>
<li>上传到npm上时，要将package.json中的private属性修改为false</li>
<li>包迭代时，要修改package.json里的版本号，再执行发布命令</li>
</ul>
<h3 data-id="heading-7">发布到npm</h3>
<p><strong>注意：由于我们是要上传的npm的，所以本地npm的源要使用原本的源，不能使用淘宝源或其他</strong></p>
<pre><code class="copyable">npm config get registry // 查看npm当前镜像源
npm config set registry https://registry.npmjs.org/ //设置为npm源
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在控制台执行<code>npm login</code>，登陆后执行<code>npm publish .</code>进行发布。</p>
<h3 data-id="heading-8">使用我们的自定义组件库</h3>
<p>发布完成后就可以拿来尝试使用了。这里仍然是用vue的web项目来尝试。新建一个vue101项目，过程略过，然后在main.js中引用它</p>
<pre><code class="copyable">import Vue from 'vue'
import App from './App.vue'
import BkyzUI from 'bkyz-ui'
Vue.config.productionTip = false
Vue.use(BkyzUI)
new Vue(&#123;
  render: h => h(App),
&#125;).$mount('#app')

<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改helloworld.vue文件</p>
<pre><code class="copyable"><template>
  <div class="hello">
    <mc-button plain @click="handleClick">字体</mc-button>
    <mc-button type="primary">按钮</mc-button>
    <mc-button icon="mc-icon-check" circle plain type="primary"></mc-button>
  </div>
</template>

<script>
import 'bkyz-ui/dist/bkyz-ui.css'
import Bkyz from 'bkyz-ui'

export default &#123;
  name: 'HelloWorld',
  methods: &#123;
    handleClick() &#123;
      console.log('click');
    &#125;
  &#125;,
  props: &#123;
    msg: String
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是按需引用：</p>
<pre><code class="copyable"><template>
  <div class="hello">
    <mc-button plain @click="handleClick">字体</mc-button>
    <mc-button type="primary">按钮</mc-button>
    <mc-button icon="mc-icon-check" circle plain type="primary"></mc-button>
  </div>
</template>

<script>
import 'bkyz-ui/dist/bkyz-ui.css'
import Bkyz from 'bkyz-ui'

export default &#123;
  name: 'HelloWorld',
  components: &#123;
    McButton: Bkyz.Button
  &#125;,

  methods: &#123;
    handleClick() &#123;
      console.log('click');
    &#125;
  &#125;,
  props: &#123;
    msg: String
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看下页面</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/406ff42a77794d0d856c7366d2bb8a20~tplv-k3u1fbpfcp-watermark.image" alt="Screen Shot 2021-08-12 at 2.53.22 PM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">参考</h3>
<p><a href="https://juejin.cn/post/6844904049259577351#heading-2" target="_blank" title="https://juejin.cn/post/6844904049259577351#heading-2">从零实现一套属于自己的UI框架-发布到npm</a></p></div>  
</div>
            