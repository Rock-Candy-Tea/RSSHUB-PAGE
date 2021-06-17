
---
title: 'Vue项目性能优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://www.auroras.top/_img/build/build-1.1.png'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 19:23:41 GMT
thumbnail: 'https://www.auroras.top/_img/build/build-1.1.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Vue-CLI 性能优化</h1>
<h2 data-id="heading-1">问题</h2>
<blockquote>
<p>是否有首屏加载时间过长的问题.?</p>
<p>为什么会出现这样的问题.?</p>
<p>解决方法是什么.?</p>
<p>下面方法都可以大程度的优化项目结构, 进而减少首屏加载的时间</p>
</blockquote>
<p>首先得知道 Webpack 的 build 是如何打包分割代码的</p>
<p>目前代码打包分割有三个规则</p>
<ol>
<li>入口起点, 根据<code>entry</code>配置来分割代码</li>
<li>动态导入: 通过模块引入<code>import()</code>分割代码</li>
<li><code>splitChunks</code>: 代码分割配置规则, 根据规则分割代码</li>
</ol>
<hr>
<p>以下使用<code>vue create</code>创建一个新项目, <code>build</code>后输出的文件为以下</p>
<img src="https://www.auroras.top/_img/build/build-1.1.png" alt="build-1.1" loading="lazy" referrerpolicy="no-referrer">
<p><strong>Q1: 为什么是打包出这几个文件.?</strong></p>
<p>这里就要查看一下<code>Vue CLI</code>的默认打包配置了</p>
<p>以下贴出关键代码</p>
<pre><code class="copyable">&#123;
  // 入口配置
  entry: &#123;
    app: [
      './src/main.js'
    ]
  &#125;,
  // 出口配置
  output: &#123;
    path: 'E:\\demo\\vue-cli-vue2-async-components-demo\\dist',
    filename: 'js/[name].[contenthash:8].js',
    publicPath: '/',
    chunkFilename: 'js/[name].[contenthash:8].js'
  &#125;,
  // 代码分割配置
  optimization: &#123;
    splitChunks: &#123;
      cacheGroups: &#123;
        vendors: &#123;
          name: 'chunk-vendors',
          test: /[\\/]node_modules[\\/]/,
          priority: -10,
          chunks: 'initial'
        &#125;,
        common: &#123;
          name: 'chunk-common',
          minChunks: 2,
          priority: -20,
          chunks: 'initial',
          reuseExistingChunk: true
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里可以看到:</p>
<p>清楚知道<code>app.[contenthash:8].js</code>是由于 规则1 的分割规则, 通过入口配置<code>entry</code>分割出来的</p>
<p>那么<code>about.[contenthash:8].js </code>呢?</p>
<p>这时候就要查看<code>Vue Router</code>的路由懒加载了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'../views/Home.vue'</span>

Vue.use(VueRouter)

<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
    <span class="hljs-attr">component</span>: Home
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'About'</span>,
    <span class="hljs-comment">// route level code-splitting</span>
    <span class="hljs-comment">// this generates a separate chunk (about.[hash].js) for this route</span>
    <span class="hljs-comment">// which is lazy-loaded when the route is visited.</span>
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "about" */</span> <span class="hljs-string">'../views/About.vue'</span>) <span class="hljs-comment">// 关键代码</span>
  &#125;
]

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">base</span>: process.env.BASE_URL,
  routes
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是初始化项目的路由配置</p>
<p>关键代码<code>component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')</code></p>
<blockquote>
<p><code>webpackChunkName</code>是什么.?</p>
<p>Webpack的魔法注释, 作用: 分割到哪个chunk内</p>
</blockquote>
<p>最后的<code>chunk-vendors.[contenthash:8].js</code>就是因为<code>splitChunks</code>的分割规则切割出来
主要就是包含<code>node_modules</code>内引用的插件的包了</p>
<h2 data-id="heading-2">代码分割</h2>
<p>在Vue项目中, 除了第一个路由页面, 其他路由都是使用 <code>import()</code>引入, 进行路由懒加载, 当路由被访问的时候才加载对应组件，这样就更加高效了</p>
<p>这其实是利用了Vue 的<a href="https://cn.vuejs.org/v2/guide/components-dynamic-async.html#%E5%BC%82%E6%AD%A5%E7%BB%84%E4%BB%B6" target="_blank" rel="nofollow noopener noreferrer">异步组件 (opens new window)</a>和 Webpack 的<a href="https://doc.webpack-china.org/guides/code-splitting-async/#require-ensure-/" target="_blank" rel="nofollow noopener noreferrer">代码分割功能 (opens new window)</a>，轻松实现路由组件的懒加载</p>
<p>其中有个重要的点, 就是Webpack的<strong>魔法注释</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Foo = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "group-foo" */</span> <span class="hljs-string">'./Foo.vue'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Webpack 会根据这个魔法注释的名字进行代码分隔, 如上配置之后, 会有一个命名的<code>group-foo</code>的chunk被单独打包出来一个文件
这个效果不仅仅可应用于路由懒加载, 也可以使用到单文件组件中</p>
<h3 data-id="heading-3">组件分割</h3>
<p>在父组件中, 需要点击按钮后弹出一个弹窗
一般会把这个弹窗封装为单独一个单文件组件, 一般如下:</p>
<p>直接引入组件, 直接注册到<code>components</code>中</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <el-button @click="$refs.homeAdd.dialogVisible = true">显示</el-button>
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <HomeAdd ref="homeAdd"></HomeAdd>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import HomeAdd from './HomeAdd.vue'

export default &#123;
  name: 'Home',
  mounted() &#123;
    console.log('Home')
  &#125;,
  components: &#123;
    HelloWorld,
    HomeAdd
  &#125;
&#125;
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样编写代码后的打包是这样的:</p>
<img src="https://www.auroras.top/_img/build/build-1.2.png" alt="build-1.2" loading="lazy" referrerpolicy="no-referrer">
<p>能看到<code>app.[contenthash:8].js</code>从之前的<code>6.57kb</code>增加到了<code>6.86kb</code></p>
<p>因为打包把引入的组件也打包进去了, 当页面越来越多, 就会一直增加该主包的体积</p>
<p>其实可以这样写:</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <el-button @click="$refs.homeAdd.dialogVisible = true">按钮</el-button>
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <HomeAdd ref="homeAdd"></HomeAdd>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default &#123;
  name: 'Home',
  mounted() &#123;
    console.log('Home')
  &#125;,
  components: &#123;
    HelloWorld,
    HomeAdd: () => import(/* webpackChunkName: "home.add" */ './HomeAdd.vue')
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://www.auroras.top/_img/build/build-1.3.png" alt="build-1.3" loading="lazy" referrerpolicy="no-referrer">
<p>通过这样, 可以把弹窗单独打包成<code>home.add</code>的chunk, 使得该业务分隔成更多更小的包, 避免某个包过大导致的加载时候耗费过多时间</p>
<h3 data-id="heading-4">插件分割</h3>
<p>如果我们需要使用<code>lodash</code>内的一个方法, 那么我们就会引入该包, 然后调用, 看看这样引入后, 打包后的项目是什么样的.?</p>
<pre><code class="hljs language-vue copyable" lang="vue">![build-1.4](E:\project\MyNote\_img\build\build-1.4.png)<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    &#123;&#123; value &#125;&#125;
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <HomeAdd ref="homeAdd"></HomeAdd>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import _ from 'lodash' // 引入lodash

export default &#123;
  name: 'Home',
  mounted() &#123;
    this.compute()
    console.log('Home')
  &#125;,
  data() &#123;
    return &#123;
      value: ''
    &#125;
  &#125;,
  methods: &#123;
    compute() &#123;
      const arr = ['Turtle', 'Hello', 'World']
      this.value = _.join(arr, '-') // 调用loadsh的join方法
    &#125;
  &#125;,
  components: &#123;
    HelloWorld,
    HomeAdd: () => import(/* webpackChunkName: "home.add" */ './HomeAdd.vue')
  &#125;
&#125;
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://www.auroras.top/_img/build/build-1.4.png" alt="build-1.4" loading="lazy" referrerpolicy="no-referrer">
<p>发现<code>chunk-vendors.[contenthash:8].js</code>从<code>133kb</code>增加到了<code>212kb</code></p>
<p>分割也可以应用于 javascript 插件的引用</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <button @click="compute">计算</button>
    &#123;&#123; value &#125;&#125;
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <HomeAdd ref="homeAdd"></HomeAdd>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default &#123;
  name: 'Home',
  mounted() &#123;
    console.log('Home')
  &#125;,
  data() &#123;
    return &#123;
      value: ''
    &#125;
  &#125;,
  methods: &#123;
    async compute() &#123;
      const &#123; default: _ &#125; = await import(/* webpackChunkName: "lodash" */ 'lodash')
      const arr = ['Turtle', 'Hello', 'World']
      this.value = _.join(arr, '-')
    &#125;
  &#125;,
  components: &#123;
    HelloWorld,
    HomeAdd: () => import(/* webpackChunkName: "home.add" */ './HomeAdd.vue')
  &#125;
&#125;
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://www.auroras.top/_img/build/build-1.5.png" alt="build-1.5" loading="lazy" referrerpolicy="no-referrer">
<p>这里就会把<code>lodash</code>单独打包出来, 减少了<code>chunk-vendors.[contenthash:8].js</code>的体积</p>
<p>可以仔细查看DevTools的输出看到点击之后才请求该 js 资源</p>
<h3 data-id="heading-5">代码分割</h3>
<p>在 Vue 项目中, 会把公用的 js 打包进一个<code>chunk-vendors.[hash]:8.js</code>的文件中, 当引用的插件或者项目业务代码多的时候, 该文件会越来越大, 在浏览器加载的时候, 就会耗费更多时间, 导致页面首屏白屏时间过长
解决方案: 通过定向代码分隔, 把某些插件从该文件抽离, 单独成文件</p>
<p>技术点: 需要利用 Webpack 自带的 <code>splitChunks</code> 功能, 进行配置分割</p>
<p>配置项<code>vue.config.js</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-function"><span class="hljs-title">chainWebpack</span>(<span class="hljs-params">config</span>)</span> &#123;
    config.when(process.env.NODE_ENV !== <span class="hljs-string">'development'</span>, <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
      config.optimization.splitChunks(&#123;
        <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>,
        <span class="hljs-attr">cacheGroups</span>: &#123;
          <span class="hljs-attr">elementUI</span>: &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'chunk-elementUI'</span>,
            <span class="hljs-attr">priority</span>: <span class="hljs-number">20</span>,
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]_?element-ui(.*)/</span>
          &#125;
        &#125;
      &#125;)
    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般的项目都会全量引入一个UI, 举例子为<code>elementUI</code>,</p>
<p>以上配置会把<code>elementUI</code>单独打包出来, 生成一个<code>chunk-elementUI.[hash]:8.js</code>文件</p>
<p>大概会有<code>600kb</code>的大小, 所以可以为主包减少这么多的体积</p>
<h4 data-id="heading-6"><code>splitChunks</code> 代码分割配置项详解</h4>
<p>此配置对象代表<code>SplitChunksPlugin</code>的默认配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">splitChunks: &#123;
    <span class="hljs-attr">chunks</span>: <span class="hljs-string">"async"</span>,
    <span class="hljs-attr">minSize</span>: <span class="hljs-number">30000</span>,
    <span class="hljs-attr">minChunks</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">maxAsyncRequests</span>: <span class="hljs-number">5</span>,
    <span class="hljs-attr">maxInitialRequests</span>: <span class="hljs-number">3</span>,
    <span class="hljs-attr">automaticNameDelimiter</span>: <span class="hljs-string">'~'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">cacheGroups</span>: &#123;
        <span class="hljs-attr">vendors</span>: &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]/</span>,
            priority: -<span class="hljs-number">10</span>
        &#125;,
    <span class="hljs-attr">default</span>: &#123;
            <span class="hljs-attr">minChunks</span>: <span class="hljs-number">2</span>,
            <span class="hljs-attr">priority</span>: -<span class="hljs-number">20</span>,
            <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里对于每一项进行解释</p>
<p><strong><code>chunks</code></strong></p>
<ul>
<li>含义: 打包模式, 模式: <code>async</code>异步,<code>all</code>全部</li>
<li>默认值: <code>async</code>异步, 只对异步引入的模块进行分割</li>
<li><code>all</code>: 不管是异步还是同步导入的模块, 都进行代码分割</li>
</ul>
<p><strong><code>minSize</code></strong></p>
<ul>
<li>含义: 当导入的模块需要超过该值, 才会进行代码分割</li>
<li>默认值: 30000字节</li>
</ul>
<p><strong><code>minChunks</code></strong></p>
<ul>
<li>含义: 一个模块需要被导入多少次才会进行代码分割</li>
<li>默认值: 1</li>
<li>注意: 该配置项只适用于同步引入的模块, 异步模块都会进行代码分割</li>
</ul>
<p><strong><code>maxAsyncRequests</code></strong></p>
<ul>
<li>含义: 同时加载的模块数是几个</li>
<li>举例: 当我们异步引入了10个类库, 按照正常情况下, 每个类库都会进行代码分割成一个单独的js文件(脱离<code>main.js</code>), 即生成了除<code>main.js</code>外的10个分割js文件, 如果<code>maxAsyncRequests: 5</code> 则打包时, 前5个类库会进行代码分割, 生成对应的5个js文件, 后面的5个类库依然存在于<code>main.js</code>中,不进行代码分割</li>
<li>默认值: 5</li>
</ul>
<p><strong><code>maxInitialRequests</code></strong></p>
<ul>
<li>含义: 对入口文件<code>entry</code>进行分割的时候, 最多能分割出多少个文件, 超出之后不进行分割</li>
<li>默认值: 3</li>
</ul>
<p><strong><code>maxAsyncRequests</code>与<code>maxInitialRequests</code>区别</strong></p>
<ul>
<li><code>maxAsyncRequests</code>包含入口文件及其入口依赖文件(实际上也是模块)中所导入的模块的一起来统计是否超过<code>maxAsyncRequests</code>设置的值</li>
<li><code>maxInitialRequests</code>只是对入口文件中直接导入的模块进行统计</li>
</ul>
<p><strong><code>automaticNameDelimiter</code></strong></p>
<ul>
<li>含义: 文件名连接符号</li>
<li>默认值: <code>~</code></li>
</ul>
<p><strong><code>name</code></strong></p>
<ul>
<li>含义: 决定缓存组<code>cacheGroups</code>内的<code>name</code>是否生效</li>
<li>默认值: true</li>
</ul>
<p><strong><code>cacheGroups</code></strong></p>
<blockquote>
<p>缓存组</p>
<p>Q: 什么是缓存组.?</p>
<p>A:</p>
<ol>
<li>只对同步导入模块起作用, 把同步导入的模块根据相关配置进行分割缓存起来
<ol>
<li>没有设置缓存组, 那么会根据默认配置, 满足后才会分割</li>
<li>如果存在缓存组, 会把每个模块内符合缓存组配置项中模块先放到缓存组内, 等把全部模块都分析完毕, 再把符合缓存组配置项中模块全部打包在一起</li>
</ol>
</li>
<li>对异步导入模块不起作用, 因为异步导入的模块都会单独生成一个模块</li>
</ol>
</blockquote>
<p><code>cacheGroups</code> 继承 <code>splitChunks</code> 里的所有属性的值，如 <code>chunks</code>、<code>minSize</code>、<code>minChunks</code>、<code>maxAsyncRequests</code>、<code>maxInitialRequests</code>、<code>automaticNameDelimiter</code>、<code>name</code> ，我们还可以在 <code>cacheGroups</code> 中重新赋值，覆盖 <code>splitChunks</code> 的值</p>
<p>另外，还有一些属性只能在 <code>cacheGroups</code> 中使用：<code>test</code>、<code>priority</code> 、<code>reuseExistingChunk</code></p>
<ul>
<li><code>text</code>
<ul>
<li>含义: 正则匹配条件</li>
</ul>
</li>
<li><code>priority</code>
<ul>
<li>缓存组的优先级</li>
<li>数字越大, 等级越高</li>
</ul>
</li>
<li><code>reuseExistingChunk</code>
<ul>
<li>如果一个模块被打包了, 再遇上相同模块时会复用之前模块</li>
</ul>
</li>
</ul>
<h2 data-id="heading-7">开启<code>gzip</code>压缩</h2>
<p><code>gizp</code>压缩是一种<code>http</code>请求优化方式，通过减少文件体积来提高加载速度</p>
<p><code>html</code>、<code>js</code>、<code>css</code>文件甚至<code>json</code>数据都可以用它压缩，可以减小60%以上的体积</p>
<h3 data-id="heading-8"><code>compression-webpack-plugin</code></h3>
<p><code>webpack</code>在打包时可以借助 <a href="https://webpack.docschina.org/plugins/compression-webpack-plugin/" target="_blank" rel="nofollow noopener noreferrer">compression webpack plugin</a> 实现<code>gzip</code>压缩，首先需要安装该插件</p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add -D compression-webpack-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>vue.config.js</code>进行配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> CompressionPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'compression-webpack-plugin'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">configureWebpack</span>: <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV === <span class="hljs-string">'production'</span>) &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">plugins</span>: [
          <span class="hljs-keyword">new</span> CompressionPlugin(&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$|\.html$|\.css$|\.jpg$|\.jpeg$|\.png/</span>, <span class="hljs-comment">// 需要压缩的文件类型</span>
            threshold: <span class="hljs-number">10240</span>, <span class="hljs-comment">// 对10K以上的进行压缩</span>
            <span class="hljs-attr">deleteOriginalAssets</span>: <span class="hljs-literal">false</span> <span class="hljs-comment">// 是否删除原文件</span>
          &#125;)
        ]
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">安装后打包报错</h4>
<blockquote>
<p><code>TypeError: Cannot read property 'tapPromise' of undefined</code></p>
</blockquote>
<p>原因是因为<code>compression-webpack-plugin</code>这个版本高了，得降低点版本</p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add -D compression-webpack-plugin@6.1.1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10"><code>nginx</code>配置</h3>
<p>在配置完<code>Vue</code>部分后直接部署到<code>nginx</code>上是不会生效的，还必须打开<code>nginx</code>的<code>gzip</code>功能才可以</p>
<p>首先你要准备配置一下nginx，在 <code>http</code> 中：</p>
<pre><code class="hljs language-conf copyable" lang="conf">// nginx开启gzip服务
gzip on;
gzip_disable "msie6";
gzip_vary on;
gzip_proxied any;
gzip_comp_level 6;
gzip_buffers 16 8k;
gzip_http_version 1.1;
// 需要开启gzip的格式
gzip_types text/plain text/css application/json application/x-javascript text/xml 
  application/xml application/xml+rss text/javascript image/jpeg image/gif image/png image/jpg;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">CDN引入</h2>
<p>一般我们习惯于<code>npm</code>引入包, 但是引入的包, 会在打包时候打包进去, 进而增加打包后的体积</p>
<p>那么在浏览器加载时候, 某些包过大, 就会导致页面白屏时间过长, 体验感较差</p>
<p>这时候就可以把某些包用 <code>CDN</code>引入形式加载到项目内</p>
<p>配置如下:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> env = process.env.NODE_ENV === <span class="hljs-string">'development'</span> ? <span class="hljs-string">''</span> : <span class="hljs-string">'.min'</span>
<span class="hljs-keyword">const</span> cdn = &#123;
  <span class="hljs-attr">css</span>: [
    <span class="hljs-string">'//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css'</span>,
    <span class="hljs-string">'//cdn.bootcdn.net/ajax/libs/animate.css/3.5.1/animate.css'</span>,
    <span class="hljs-string">'/cdn/iconfont/1.0.0/index.css'</span>,
    <span class="hljs-string">'/cdn/avue/2.7.3/index.css'</span>
  ],
  <span class="hljs-attr">js</span>: [
    <span class="hljs-string">'/util/aes.js'</span>,
    <span class="hljs-string">`//cdn.jsdelivr.net/npm/vue@2.6.12/dist/vue<span class="hljs-subst">$&#123;env&#125;</span>.js`</span>,
    <span class="hljs-string">`//cdn.jsdelivr.net/npm/vuex@3.6.0/dist/vuex<span class="hljs-subst">$&#123;env&#125;</span>.js`</span>,
    <span class="hljs-string">`//cdn.jsdelivr.net/npm/vue-router@3.4.9/dist/vue-router<span class="hljs-subst">$&#123;env&#125;</span>.js`</span>,
    <span class="hljs-string">`//unpkg.com/axios@0.21.0/dist/axios<span class="hljs-subst">$&#123;env&#125;</span>.js`</span>,
    <span class="hljs-string">'//unpkg.com/element-ui@2.13.2/lib/index.js'</span>,
    <span class="hljs-string">'/cdn/avue/2.7.3/avue.min.js'</span>,
    <span class="hljs-string">'//cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.1/moment.min.js'</span>,
    <span class="hljs-string">'//cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js'</span>,
    <span class="hljs-string">'//unpkg.com/xlsx@0.16.9/dist/xlsx.min.js'</span>
  ]
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">pages</span>: &#123;
    <span class="hljs-attr">index</span>: &#123;
      <span class="hljs-attr">entry</span>: <span class="hljs-string">'src/main.js'</span>,
      <span class="hljs-attr">cdn</span>: cdn
    &#125;
  &#125;,
  <span class="hljs-attr">chainWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    <span class="hljs-comment">//忽略的打包文件</span>
    config.externals(&#123;
      <span class="hljs-attr">vue</span>: <span class="hljs-string">'Vue'</span>,
      <span class="hljs-string">'vue-router'</span>: <span class="hljs-string">'VueRouter'</span>,
      <span class="hljs-attr">vuex</span>: <span class="hljs-string">'Vuex'</span>,
      <span class="hljs-attr">axios</span>: <span class="hljs-string">'axios'</span>,
      <span class="hljs-string">'element-ui'</span>: <span class="hljs-string">'ELEMENT'</span>,
      <span class="hljs-attr">moment</span>: <span class="hljs-string">'moment'</span>,
      <span class="hljs-attr">lodash</span>: <span class="hljs-string">'_'</span>,
      <span class="hljs-attr">xlsx</span>: <span class="hljs-string">'XLSX'</span>
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"Content-Type"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"text/html; charset=utf-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"apple-mobile-web-app-capable"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"yes"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"apple-mobile-web-app-status-bar-style"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"black"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"format-detection"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"telephone=no"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"chrome=1"</span>/></span>
  <span class="hljs-comment"><!-- 关键遍历 --></span>
  <% for (let i in htmlWebpackPlugin.options.cdn.css) &#123; %>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"<%= htmlWebpackPlugin.options.cdn.css[i] %>"</span> /></span>
  <% &#125; %>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>XXX<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-comment"><!-- 关键遍历 --></span>
<% for (let i in htmlWebpackPlugin.options.cdn.js) &#123; %>
  <span class="hljs-tag"><<span class="hljs-name">script</span>
    <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>
    <span class="hljs-attr">src</span>=<span class="hljs-string">"<%= htmlWebpackPlugin.options.cdn.js[i] %>"</span>
  ></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<% &#125; %>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>关键点:</p>
<ol>
<li>
<p><code>config.externals</code>, 引入的包都会有全局注入的变量, 那么在页面引用该包时候, 指向引用该变量</p>
<p><code>'vue-router': 'VueRouter'</code></p>
<p>意思引入<code>vue-router</code>这个包时候, 去找<code>VueRouter</code>变量</p>
<p>如何查看包注入的是哪个变量? 只能通过去查看源码, 导出的变量是哪个</p>
</li>
<li>
<p><code>pages.index.cdn: cdn</code>, 把<code>CDN</code>引入放在一个变量内, 注入到``pages.index.cdn<code>, </code>index.名称`该名称可以随意, 只是个遍历标识</p>
</li>
</ol></div>  
</div>
            