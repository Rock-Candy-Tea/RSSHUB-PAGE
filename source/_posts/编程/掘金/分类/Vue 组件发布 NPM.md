
---
title: 'Vue 组件发布 NPM'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1363c92b67e94ab7b2e6f1e60c42a1ef~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 02:11:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1363c92b67e94ab7b2e6f1e60c42a1ef~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">基于Vue-cli4.x二次封装Element-ui组件并发布到npm</h1>
<p>转载自：<a href="https://www.yuque.com/homacheuk/dmqta3/mbro9z#bS1LQ" target="_blank" rel="nofollow noopener noreferrer">www.yuque.com/homacheuk/d…</a></p>
<p>其他： <a href="https://blog.csdn.net/shidouyu/article/details/111640871" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/shidouyu/ar…</a></p>
<pre><code class="copyable">  https://juejin.cn/post/6844904000655998984#heading-19
  
  https://juejin.cn/post/6844903926941089806#heading-29
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">需求</h1>
<p>由于需要重新做一套基于el组件的公用组件，并且提供给多个子系统使用，因此这次选择将组件封装并发布到npm上。</p>
<h1 data-id="heading-2">正文</h1>
<p>封装组件库的方式有很多，但我们从简单入手，直接使用vue-cli来创建，虽然有点冗余但是胜在方便调试组件。</p>
<h3 data-id="heading-3">安装vue-cli4并创建一个组件库项目</h3>
<pre><code class="hljs language-shell copyable" lang="shell">//安装脚手架
yarn global add @vue/cli
// 创建项目
vue create jz-vue-ui
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>创建完成项目后（对创建流程不熟的小伙伴可以自行百度）我们就有了以下的项目目录。包含了基本项目需要的vuex、router等，这个因为我项目后期需要所以就增加了，可以看个人需要来确定是不是加上。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1363c92b67e94ab7b2e6f1e60c42a1ef~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>调整为</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/344b5abdc55146baa05657d7c9ecf713~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目录的结构我们参考下element的项目结构，需要将src重命名为examples, 并添加packages目录,用来存放我们的自定义组件.</p>
<p>但是cli默认会启动src下的服务,如果目录名变了,我们需要手动修改配置,vue-cli3中提供自定义打包配置项目的文件,我们只需要手动创建vue.config.js即可.我们具体修改如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span>首先修改入口文件地址为examples下的main.js,
<span class="hljs-number">2.</span>其次将packages加入打包编译任务中
<span class="hljs-number">3.</span>将@等路径昵称修改掉
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>) <span class="hljs-comment">// 引入path模块</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span> (<span class="hljs-params">dir</span>) </span>&#123;
  <span class="hljs-keyword">return</span> path.join(__dirname, dir) <span class="hljs-comment">// path.join(__dirname)设置绝对路径</span>
&#125;
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'./'</span>,
  <span class="hljs-comment">// 1.更改入口和出口文件名</span>
  <span class="hljs-attr">pages</span>: &#123;
    <span class="hljs-attr">index</span>: &#123;
      <span class="hljs-attr">entry</span>: <span class="hljs-string">'examples/main.js'</span>,<span class="hljs-comment">//修改入口</span>
      <span class="hljs-attr">template</span>: <span class="hljs-string">'public/index.html'</span>,
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'index.html'</span>
    &#125;

  &#125;,
  <span class="hljs-comment">// 2.扩展 webpack 配置，使 packages 加入编译</span>
  <span class="hljs-attr">chainWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    config.resolve.alias
      .set(<span class="hljs-string">'@'</span>, resolve(<span class="hljs-string">'./examples'</span>)) <span class="hljs-comment">//3.修改快捷路径</span>
      .set(<span class="hljs-string">'components'</span>, resolve(<span class="hljs-string">'./examples/components'</span>))
      .set(<span class="hljs-string">'views'</span>, resolve(<span class="hljs-string">'./examples/views'</span>))
      .set(<span class="hljs-string">'assets'</span>, resolve(<span class="hljs-string">'./examples/assets'</span>))
    config.module
      .rule(<span class="hljs-string">'js'</span>)
      .include
      .add(<span class="hljs-string">'/packages/'</span>)
      .end()
      .use(<span class="hljs-string">'babel'</span>)
      .loader(<span class="hljs-string">'babel - loader'</span>)
      .tap(<span class="hljs-function"><span class="hljs-params">options</span> =></span> &#123;
        <span class="hljs-comment">// 修改它的选项...</span>

        <span class="hljs-keyword">return</span> options
      &#125;)
  &#125;,
  <span class="hljs-comment">/* 输出文件目录：在npm run build时，生成文件的目录名称 */</span>
  <span class="hljs-attr">outputDir</span>: <span class="hljs-string">'jz-vue-ui'</span>,
  <span class="hljs-comment">/* 放置生成的静态资源 (mixin、css、img、fonts) 的 (相对于 outputDir 的) 目录 */</span>
  <span class="hljs-attr">assetsDir</span>: <span class="hljs-string">'assets'</span>,
  <span class="hljs-comment">/* 是否在构建生产包时生成 sourceMap 文件，false将提高构建速度 */</span>
  <span class="hljs-attr">productionSourceMap</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-comment">/* 默认情况下，生成的静态资源在它们的文件名中包含了 hash 以便更好的控制缓存，你可以通过将这个选项设为 false 来关闭文件名哈希。(false的时候就是让原来的文件名不改变) */</span>
  <span class="hljs-attr">filenameHashing</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-comment">/* 代码保存时进行eslint检测 */</span>
  <span class="hljs-attr">lintOnSave</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-comment">/* webpack-dev-server 相关配置 */</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-comment">/* 自动打开浏览器 */</span>
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">/* 设置为0.0.0.0则所有的地址均能访问 */</span>
    <span class="hljs-attr">host</span>: <span class="hljs-string">'192.168.0.142'</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-number">8080</span>,
    <span class="hljs-attr">https</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">hotOnly</span>: <span class="hljs-literal">false</span>

  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">编写基于el的组件</h3>
<ul>
<li>由于我们需要基于el来封装组件，因此我们先装下element-ui，按照网上说的直接在vue ui 上点击装也可以，这里我们使用传统的方式</li>
</ul>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add element-ui -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后编写组件的时候直接使用按需引入会相对节省空间，因此我们按照官网的说法引入</p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add babel-plugin-component -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并在babel.config.js中添加</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">presets</span>: [
    <span class="hljs-string">'@vue/cli-plugin-babel/preset'</span>
  ],
  <span class="hljs-attr">plugins</span>: [
    [
      <span class="hljs-string">'component'</span>,
      &#123;
        <span class="hljs-attr">libraryName</span>: <span class="hljs-string">'element-ui'</span>,
        <span class="hljs-attr">styleLibraryName</span>: <span class="hljs-string">'theme-chalk'</span>
      &#125;
    ]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>下面我们拿一个Button组件来示范，这里只实现一个比较简单的组件。</p>
<pre><code class="copyable">首先我们先在packages目录下新建一个Button目录，然后src里存放组件的源代码
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>测试q<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Button</span>></span>el-button<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span><span class="hljs-comment">//按需引入</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'jz-button'</span>,
  <span class="hljs-attr">components</span>: &#123; Button &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Button的index.js里编写如下代码来作为vue的组件安装：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Button <span class="hljs-keyword">from</span> <span class="hljs-string">'./src/index.vue'</span>

Button.install = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">Vue</span>) </span>&#123;
  Vue.component(Button.name, Button)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Button
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们在packages的入口文件中导入组件并安装导出)</p>
<p><strong>这里需要注意，因为由于el有样式的css，且我们用的按需引入，因此要在这里去引入下</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-string">'element-ui/lib/theme-chalk/index.css'</span><span class="hljs-comment">//引入el的样式</span>
<span class="hljs-keyword">import</span> Button <span class="hljs-keyword">from</span> <span class="hljs-string">'./Button/index'</span>
<span class="hljs-keyword">import</span> Input <span class="hljs-keyword">from</span> <span class="hljs-string">'./Input/index'</span>
<span class="hljs-comment">// 存储组件列表</span>
<span class="hljs-keyword">const</span> components = [Button]
<span class="hljs-comment">// 定义 install 方法，接收 Vue 作为参数。如果使用 use 注册插件，则所有的组件都将被注册</span>

<span class="hljs-keyword">const</span> install = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">Vue</span>) </span>&#123;
  <span class="hljs-comment">// 判断是否安装</span>

  <span class="hljs-keyword">if</span> (install.installed) <span class="hljs-keyword">return</span>
  <span class="hljs-comment">// 遍历注册全局组件</span>
  components.forEach(<span class="hljs-function"><span class="hljs-params">component</span> =></span> &#123;
    Vue.component(<span class="hljs-string">'jz-button'</span>, component)
  &#125;)
&#125;
<span class="hljs-comment">// 判断是否是直接引入文件</span>

<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span> !== <span class="hljs-string">'undefined'</span> && <span class="hljs-built_in">window</span>.Vue) &#123;
  install(<span class="hljs-built_in">window</span>.Vue)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;<span class="hljs-comment">//引入全部</span>
  <span class="hljs-comment">// 导出的对象必须具有 install，才能被 Vue.use() 方法安装</span>
  install

&#125;
<span class="hljs-keyword">export</span> &#123;<span class="hljs-comment">//局部引入</span>
  Button,
  Input
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">测试代码</h3>
<p>我们要想看到自己写的组件效果，可以将组件导入到examples目录下的main.js中，其本质就是一个项目的开发目录，我们只需要按照如下方式导入即可：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>
<span class="hljs-keyword">import</span> jzUI <span class="hljs-keyword">from</span> <span class="hljs-string">'../packages/index'</span>
Vue.config.productionTip = <span class="hljs-literal">false</span>
Vue.use(jzUI) <span class="hljs-comment">// 这里我们为了方便直接引入全部</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  store,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们就可以在项目中使用我们的组件了</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">jz-button</span>></span><span class="hljs-tag"></<span class="hljs-name">jz-button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nav"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span> |
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>About<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span>></span><span class="css">
<span class="hljs-selector-id">#app</span> &#123;
  <span class="hljs-attribute">font-family</span>: Avenir, Helvetica, Arial, sans-serif;
  -webkit-<span class="hljs-attribute">font-smoothing</span>: antialiased;
  -moz-osx-<span class="hljs-attribute">font-smoothing</span>: grayscale;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#2c3e50</span>;
&#125;

<span class="hljs-selector-id">#nav</span> &#123;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">30px</span>;

  <span class="hljs-selector-tag">a</span> &#123;
    <span class="hljs-attribute">font-weight</span>: bold;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#2c3e50</span>;

    &<span class="hljs-selector-class">.router-link-exact-active</span> &#123;
      <span class="hljs-attribute">color</span>: <span class="hljs-number">#42b983</span>;
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d6fe7aa9a5543e98e1d761951d02842~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">配置package.json文件</h3>
<p>作为一个组件库,我们必须按照npm的发包规则来编写我们的package.json, 正常情况下我们需要配置</p>
<p>package文件的description,keywords等,具体介绍如下:</p>
<ul>
<li>
<p>description 组件库的描述文本</p>
</li>
<li>
<p>keywords 组件库的关键词</p>
</li>
<li>
<p>license 许可协议</p>
</li>
<li>
<p>repository 组件库关联的git仓库地址</p>
</li>
<li>
<p>homepage 组件库展示的首页地址</p>
</li>
<li>
<p>main 组件库的主入口地址(在使用组件时引入的地址)</p>
</li>
<li>
<p>private 声明组件库的私有性,如果要发布到npm公网上,需删除该属性或者设置为false</p>
</li>
<li>
<p>publishConfig 用来设置npm发布的地址,这个配置作为团队内部的npm服务器来说非常关键,可以设置为私有的npm仓库</p>
</li>
</ul>
<p><strong>注意：由于我们使用的是不打包的模式，直接main入口路径修改为修改为jz-vue-ui/package，调用时的引入路径可以简化调用</strong></p>
<pre><code class="hljs language-json copyable" lang="json">  <span class="hljs-comment">//我们先使用最基础的这几个属性即可</span>
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"jz-vue-ui"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"0.1.9"</span>,
  <span class="hljs-string">"private"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">"jz前端公用组件库"</span>,
  <span class="hljs-string">"main"</span>: <span class="hljs-string">"jz-vue-ui/package"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其次是需要配置打包的命令，这个我们也先给他配上，虽然我们本次并不使用他</p>
<pre><code class="hljs language-json copyable" lang="json"> <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"serve"</span>: <span class="hljs-string">"vue-cli-service serve"</span>,
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"vue-cli-service build"</span>,json
    <span class="hljs-attr">"lint"</span>: <span class="hljs-string">"vue-cli-service lint"</span>,
    <span class="hljs-comment">//包名 及打包入口</span>
    <span class="hljs-attr">"lib"</span>: <span class="hljs-string">"vue-cli-service build --target lib --name jz-vue-ui --dest lib packages/index.js"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们需要创建一个.npmignore忽略掉一些不需要上传的文件减少大小</p>
<pre><code class="copyable"># 忽略目录
examples/
#packages/
#public/

# 忽略指定文件
vue.config.js
babel.config.js
*.map
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">发布到npm</h3>
<ul>
<li>这次我们使用非打包发布，因为我们组件库可能还会用到很多第三方库及资源，使用这种方式可以避免资源加载错误</li>
</ul>
<p>打包发布和非打包发布对比如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c6f9e240ad640d1abe713aec92b016f~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>发布到npm的方法也很简单, 首先我们需要先注册去npm官网注册一个账号（<strong>记住要验证邮箱</strong>）, 然后控制台登录即可,最后我们执行npm publish即可.具体流程如下</li>
</ul>
<pre><code class="hljs language-shell copyable" lang="shell">// 登录，并按提示输入账号密码
 npm login
 // 发布 每次发布需要提高版本号
 npm publish 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发布之后效果如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d883c3049b1426e9bc083de0aca070c~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">在项目中使用</h3>
<ul>
<li>现在我们创建一个新的vue项目并引入我们的组件库</li>
</ul>
<pre><code class="hljs language-shell copyable" lang="shell">//安装组件库
yarn add jz-vue-ui 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>由于在配置main将引入路径修改为：<strong>jz-vue-ui/package，<strong>因此这里的引入可以直接使用</strong>jz-vue-ui</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">在main.js中引入
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>
<span class="hljs-keyword">import</span> &#123; Input &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'jz-vue-ui'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./css/index.scss'</span> <span class="hljs-comment">// 覆盖css需要放在后面</span>
Vue.config.productionTip = <span class="hljs-literal">false</span>
Vue.use(Input)
<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  store,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这里我们会注意到一个问题，<strong>引入的路径并不止我们的组件库名</strong>，这是因为我们是没打包直接发布，因此需要手动去找到<strong>库的入口js</strong>,实际上安装完成后的组件库在node_modules中是这样的：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdd0b08c1e534437b36f4fa4943e71c1~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>接下来我们来使用它，其实使用方法和调试的时候差不多</li>
</ul>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <jz-input></jz-input>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app &#123;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
&#125;

#nav &#123;
  padding: 30px;
&#125;

#nav a &#123;
  font-weight: bold;
  color: #2c3e50;
&#125;

#nav a.router-link-exact-active &#123;
  color: #42b983;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            