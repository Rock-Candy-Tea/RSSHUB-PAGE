
---
title: 'SpringBoot + Vue前后端项目分离后台管理系统 笔记 （以及错误总结） 第一篇 前端笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/371374fdd94348a4a533236f566dfd27~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 18:09:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/371374fdd94348a4a533236f566dfd27~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第25天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">学习视频的来源（链接）</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1af4y1s7Wh%3Fp%3D1" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1af4y1s7Wh?p=1" ref="nofollow noopener noreferrer">B站的 博主 </a> ps (讲的很不错)</p>
<h2 data-id="heading-1">前端的学习笔记记录</h2>
<h3 data-id="heading-2">安装前端的Vue 环境 ，新建 Vue 项目</h3>
<h4 data-id="heading-3">安装node.js</h4>
<p><strong>官网 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.cn%2Fdownload%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://nodejs.cn/download/" ref="nofollow noopener noreferrer">地址</a></strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/371374fdd94348a4a533236f566dfd27~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
安装后傻瓜操作就可以
检查是否安装完成 （命令）
下面是我的版本
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79597fc4cf6b4adc88db307d524487fc~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<em>出现上面的版本信息说明安装成功</em></p>
<h4 data-id="heading-4">安装vue 的环境</h4>
<p><strong>命令</strong></p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装淘宝的 npm 也可以不安装，不过安装了国内的镜像会快</span>
npm install -g cnpm --registry=https://registry.npm.taobao.org
<span class="hljs-comment"># vue - cli 安装依赖包</span>
cnpm install --g vue-cli
<span class="hljs-comment"># 打开 vue 的可视化 管理界面 这个可以用可视化创建 vue 的项目，也可以不用 ，我用的命令行创建 vue 的项目</span>
vue ui
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h4 data-id="heading-5">创建 vue 的环境</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea55efa9717f490eb13a06029f64ea2c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c72ad05ea0c4aac865c2392bf488847~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e994de34a01240ef83c223a0ca161520~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/806e43c74912480c8ddaff84106e5685~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/706e1cf0f3d54a74bd6765696cf54245~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>剩下的一直下一步就可以了</strong>
在项目的目录下 运行就可以看到
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40d2365a936246b0b98c6e47396f72e8~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d3a4eeb948749ed97c15184d63c77d4~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>设置在IDEA 里面输入命令访问</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee39251c7639432ebeb8d4cd40099652~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>把项目导入到 IDEA</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb10cd8eb252443db75c1a04fc5087f5~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6944931f6ff44ecd91c3ae3fdc16c602~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>我的另一篇安装Vue 的博客</strong>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fm0_46937429%2Farticle%2Fdetails%2F112199664%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/m0_46937429/article/details/112199664?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">Vue 笔记</a></p>
<h4 data-id="heading-6">安装 element-ui,axios、qs、mockjs</h4>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#  安装 element-ui</span>
cnpm install element-ui --save
<span class="hljs-comment">#  安装 axios</span>
cnpm install axios --save
<span class="hljs-comment"># 安装 cnpm install qs --save</span>
cnpm install qs --save
<span class="hljs-comment"># 安装 mockjs </span>
cnpm install mockjs --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>axios：一个基于 promise 的 HTTP 库,ajax</li>
<li>qs：查询参数序列化和解析库</li>
<li>mockjs：为我们生成随机数据的工具</li>
</ol>
<p>**Mockjs **
在 src 目录下创建 mock.js 文件，用来编写随机的api 现在还没有和后端交互，所以先用假的数据
同时在main.js 中引入这个文件
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36fd54a831b446dfb400fb61e5477527~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>main.js 文件</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>;
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>;
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">"./store"</span>;
<span class="hljs-comment">//引入mock数据，关闭则注释该行</span>
<span class="hljs-built_in">require</span>(<span class="hljs-string">"./mock"</span>) 
Vue.config.productionTip = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  store,
  <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h</span>) =></span> h(App),
&#125;).$mount(<span class="hljs-string">"#app"</span>);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>引入 element-ui ，axios</strong>
然后我们打开项目src目录下的main.js，引入element-ui依赖 引入axios。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> Element from <span class="hljs-string">'element-ui'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"element-ui/lib/theme-chalk/index.css"</span>
<span class="hljs-keyword">import</span> axios from <span class="hljs-string">'axios'</span>
Vue.use(Element)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">页面路由</h3>
<h4 data-id="heading-8">登录和首页的创建</h4>
<p><strong>Router</strong>
WebApp 的链路路径管理系统，就是建立起url 和页面之间的映射关系
主要在 src\router\index.js 就是来配置路由的
<strong>创建我们的登录页面和首页页面</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36c13369fa114cd4921a2dddf83dc303~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>在路由中心配置 url 与Vue 页面的映射关系 可以参考原来默认的写法    ./src/router/index.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-router"</span>;
<span class="hljs-keyword">import</span> Login <span class="hljs-keyword">from</span> <span class="hljs-string">"../views/Login"</span>;
Vue.use(VueRouter);
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/"</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Home"</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/Home.vue'</span>),
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/login"</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Login"</span>,
    <span class="hljs-attr">component</span>: Login
  &#125;,
];
<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">base</span>: process.env.BASE_URL,
  routes
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>修改完 index.js 页面后 我们 启动vue 的项目</strong></p>
<pre><code class="hljs language-java copyable" lang="java">npm run serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动完成后访问 localhost:8081/login 页面发现页面如下所示 ，出现了 Home | About</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad35e9c11df1417e95e58d024ef5f940~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>原因：</strong>
新建的vue 项目没有其他配置，默认就是一个单页面应用，就是说这个应用是由一个外壳页面，和多个页面，组成在跳转的时候没有离开外壳的页面，这个的外壳压面就是App.vue   登录的页面就是一个片段而已，我们应该修改我们的 App.vue 页面
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80148a603e304be48ce383a13178d29e~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
修改 后的App.vue</p>
<pre><code class="hljs language-java copyable" lang="java"><template>
  <div id=<span class="hljs-string">"app"</span>>
    <router-view/>
  </div>
</template>
<style lang=<span class="hljs-string">"less"</span>>
#app &#123;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
&#125;
#nav &#123;
  padding: 30px;
  a &#123;
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active &#123;
      color: #42b983;
    &#125;
  &#125;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**修改完成后在次查看 **
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65f7c31ac94b4e7bb7d3de8bbcffee08~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">登录开发</h3>
<h4 data-id="heading-10">登录的开发流程</h4>
<p>需要去element-ui 上找到 表单的组件，简单的登录页面，但是登录页面的验证码需要与后台进行交互
主要登录与后台交互的有两个
1，获取登录的验证码
2，提交登录表单完成登录
由于还没有写后端的代码，所以先在我们的mock.js 里写数据，完成交互。开发api
<strong>交互的过程</strong>
1，打开登录的界面
2，动态加载登录验证码，前后端分离的项目，我们不在使用session 进行交互，所以后端警用session 后端可以随机生成一个验证码的同时生成一个随机码，把随机码作为 key,验证码为value 保存到redis 中，然后把随机码和验证码图片的Base64 字符串码发送到前端
3，前端提交用户名，密码，验证码，还有随机码
4，后台验证是否正确
<strong>大概的流程图</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/253bb3343ae547599ed6fc35de41db0a~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">登录的页面</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>

  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-row</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"flex"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row-bg"</span> <span class="hljs-attr">justify</span>=<span class="hljs-string">"center"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-col</span> <span class="hljs-attr">:xl</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:lg</span>=<span class="hljs-string">"7"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>欢迎来到fjj 管理系统<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-image</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"require('@/assets/img.png')"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"height: 180px; width: 180px;"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-image</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>扫码二维码，添加个人微信<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">el-col</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"1"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-divider</span> <span class="hljs-attr">direction</span>=<span class="hljs-string">"vertical"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-divider</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-col</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span> <span class="hljs-attr">:lg</span>=<span class="hljs-string">"7"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:model</span>=<span class="hljs-string">"loginForm"</span> <span class="hljs-attr">:rules</span>=<span class="hljs-string">"rules"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"loginForm"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"80px"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"用户名"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"username"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 380px;"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"loginForm.username"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"密码"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"password"</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 380px;"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"loginForm.password"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"验证码"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"code"</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 380px;"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"loginForm.code"</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 172px; float: left"</span> <span class="hljs-attr">maxlength</span>=<span class="hljs-string">"5"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-image</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"captchaImg"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"captchaImg"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"getCaptcha"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-image</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitForm('loginForm')"</span>></span>立即创建<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"resetForm('loginForm')"</span>></span>重置<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-col</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-row</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Login"</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">loginForm</span>: &#123;
        <span class="hljs-attr">username</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">password</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">code</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">token</span>: <span class="hljs-string">''</span>
      &#125;,
      <span class="hljs-attr">rules</span>: &#123;
        <span class="hljs-attr">username</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入用户名'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">password</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入密码'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">code</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入验证码'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;,
          &#123; <span class="hljs-attr">min</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">max</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'长度为 5 个字符'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ]
      &#125;,
      <span class="hljs-attr">captchaImg</span>: <span class="hljs-literal">null</span>

    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    submitForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].validate(<span class="hljs-function">(<span class="hljs-params">valid</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (valid) &#123;
          <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/login?'</span> ,<span class="hljs-built_in">this</span>.loginForm).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
           
          &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'错误的提交'</span>)
          <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125;
      &#125;)
    &#125;,
    resetForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].resetFields()
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.el-row</span> &#123;
  <span class="hljs-comment">/*background-color: #fafafa;*/</span>
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">10%</span>;
&#125;

<span class="hljs-selector-class">.el-divider</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
&#125;

<span class="hljs-selector-class">.captchaImg</span> &#123;
  <span class="hljs-attribute">float</span>: left;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">8px</span>;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">4px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果</strong>
我们的验证码还没有显示出来效果
这个图片二维码是在这里引入的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4c5cd37d1034ac09791b4931dc545c2~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/daf75ddf46a9427e9be9f66b601fa9b3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">验证码</h4>
<p><strong>此时我们的验证码还没有显示出来，没有与后台交互先用mock 做验证码</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36a3ff35bf4d43a7a29ae9b79df9d60a~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>先在data 里面设置为 null
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54e7ded1dbfa4176a26ca33284517694~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
** getCaptcha () 的方法。调用创建图片的方法**</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    getCaptcha () &#123;
      <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/captcha'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.loginForm.token = res.data.data.token
        <span class="hljs-built_in">this</span>.captchaImg = res.data.data.captchaImg
      &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4228ae7600b340aeaafba01e0e533da3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
创建完成之后不要忘记使用这个方法
在下面调用这个方法
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fc3fd5d65234c959d747c55c427719b~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
**代码 ，只放了export default 的内容 **</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Login"</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">loginForm</span>: &#123;
        <span class="hljs-attr">username</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">password</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">code</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">token</span>: <span class="hljs-string">''</span>
      &#125;,
      <span class="hljs-attr">rules</span>: &#123;
        <span class="hljs-attr">username</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入用户名'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">password</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入密码'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">code</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入验证码'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;,
          &#123; <span class="hljs-attr">min</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">max</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'长度为 5 个字符'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ]
      &#125;,
      <span class="hljs-attr">captchaImg</span>: <span class="hljs-literal">null</span>

    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    submitForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].validate(<span class="hljs-function">(<span class="hljs-params">valid</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (valid) &#123;
          <span class="hljs-comment">// eslint-disable-next-line no-unused-vars</span>
          <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/login?'</span> ,<span class="hljs-built_in">this</span>.loginForm).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;

          &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'错误的提交'</span>)
          <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125;
      &#125;)
    &#125;,
    resetForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].resetFields()
    &#125;,
    getCaptcha () &#123;
      <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/captcha'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-comment">// res 为结果 结果后的data 里面取到我们的 token 值</span>
        <span class="hljs-comment">// 其实就是我们 后台返回的一个结果，如果正确的话里面会有一个data 的值在</span>
        <span class="hljs-built_in">this</span>.loginForm.token = res.data.data.token
        <span class="hljs-comment">// 同理拿出来我们的图片</span>
        <span class="hljs-built_in">this</span>.captchaImg = res.data.data.captchaImg
      &#125;)
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.getCaptcha()
  &#125;
&#125;
</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.el-row</span> &#123;
  <span class="hljs-comment">/*background-color: #fafafa;*/</span>
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">10%</span>;
&#125;

<span class="hljs-selector-class">.el-divider</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
&#125;
<span class="hljs-selector-class">.captchaImg</span> &#123;
  <span class="hljs-attribute">float</span>: left;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">8px</span>;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">4px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在我们的mock.js 里面写数据</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建放回的对象</span>
<span class="hljs-keyword">const</span> Mock = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mockjs'</span>)
<span class="hljs-comment">// 获取随机的 Random</span>
<span class="hljs-keyword">const</span> Random = Mock.Random
<span class="hljs-comment">// 设置返回结果</span>
<span class="hljs-keyword">let</span> Result = &#123;
    <span class="hljs-attr">code</span>: <span class="hljs-number">200</span>,
    <span class="hljs-attr">msg</span>: <span class="hljs-string">'操作成功'</span>,
    <span class="hljs-attr">data</span>: <span class="hljs-literal">null</span>
&#125;
<span class="hljs-comment">// 图片的请求</span>
Mock.mock(<span class="hljs-string">'/captcha'</span>,<span class="hljs-string">'post'</span>,<span class="hljs-function">()=></span> &#123;
    Result.data = &#123;
        <span class="hljs-attr">token</span>: Random.string(<span class="hljs-number">32</span>),
        <span class="hljs-attr">captchaImg</span>: Random.dataImage(<span class="hljs-string">'120x40'</span>,<span class="hljs-string">'jikof'</span>)
    &#125;
    <span class="hljs-keyword">return</span> Result
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们的效果，现在的验证码是mock 随机生成 的 与后端交互的时候给成后端的api 接口就可以了
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0c50f26f9464d7aa5dfa65313a711eb~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">登录的请求</h4>
<p>**由于我们登录的时候要求把我们的后台的数据放在 localStorage 里面要在 ./src/store/index.js 里面写 这样就可以存到localStorage  **</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;

Vue.use(Vuex);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">token</span>: <span class="hljs-string">''</span>
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-attr">SET_TOKEN</span>: <span class="hljs-function">(<span class="hljs-params">state,token</span>) =></span> &#123;
      state.token = token
      <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">"token"</span>,token)
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;&#125;,
  <span class="hljs-attr">modules</span>: &#123;&#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在我们的 Login.vue 里，把我们的jwt 存到
设置登录成功后跳到首页
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/672ba2af66b642718a1ebb1d8dfd8a4d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>一样还是写我们的mock 的请求  测试数据 暂时没有办法把 jwt 给放入，所以测试的时候没有jwt 身份放入，先直接放入，等与后台交互的时候在放入里面</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbe695fee9404f959968ae2380968a12~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
登录后跳转到首页</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/676e1a9b547b4d01871ab1cabc1bedce~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
存到了 只是暂时没有与后台交互，所以 暂时是 undefined
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f28a89952a048d3bdd53e555b1f4c51~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-14">小小的错误记录总结 引入 axios   的错误</h5>
<p><del>这里出现了一个小小的错误记录一下</del>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae04f319214a4b688ce787519dcb7e9b~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
可是在 用 axios 请求的时候 报错
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dad22da3eacd45a99685c24585505342~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28176837f2b24310a030aa93b80dd2e1~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>解决方法</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c01dc0c5d7f8428ca2866a245c239cee~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
在Login.vue 里面也更换一下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b415449119c548958863dd999725850c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4a30aaa2b1a417788bdacd0484c8a35~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>请求就可以发送出去了</strong></p>
<h4 data-id="heading-15">设置登录时候的全局 axios</h4>
<p>这里要设置全局的原因是因为登录失败，我们是需要弹窗显示错误的，比如验证码错误，用户名或者密码不正确等，不仅仅是这个登录接口，所有的接口调用都会有这个情况，所有我们想做个拦截器，对返回的结果进行分析，如果是异常就直接弹出错误，这样我们就省下来每个接口都写一遍
<strong>在src目录下创建一个文件axios.js (与main.js 同级)</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>
<span class="hljs-keyword">import</span> Element <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>
axios.defaults.baseURL = <span class="hljs-string">'http://localhost:8081'</span>
<span class="hljs-keyword">const</span> request = axios.create(&#123;
    <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span>,
    <span class="hljs-attr">headers</span>: &#123;
        <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/json; charset=utf-8'</span>
    &#125;
&#125;)

request.interceptors.request.use(<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    config.headers.Authorization = <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'token'</span>)
    <span class="hljs-keyword">return</span> config
&#125;)

request.interceptors.response.use(
    <span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'response ->'</span> + response)

        <span class="hljs-keyword">const</span> res = response.data

        <span class="hljs-keyword">if</span> (res.code === <span class="hljs-number">200</span>) &#123;
            <span class="hljs-keyword">return</span> response
        &#125; <span class="hljs-keyword">else</span> &#123;
            Element.Message.error(!res.msg ? <span class="hljs-string">'系统异常'</span> : res.msg)
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(response.data.msg)
        &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(error)

        <span class="hljs-keyword">if</span> (error.response.data) &#123;
            error.massage = error.response.data.msg
        &#125;

        <span class="hljs-keyword">if</span> (error.response.status === <span class="hljs-number">401</span>) &#123;
            router.push(<span class="hljs-string">'/login'</span>)
        &#125;

        Element.Message.error(error.massage, &#123;<span class="hljs-attr">duration</span>: <span class="hljs-number">3000</span>&#125;)
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
    &#125;
)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> request

<span class="copy-code-btn">复制代码</span></code></pre>
<p>前置拦截，可以统一为所有权限的请求装配上header 的 token 的信息，后置拦截中，判断status.code 和 error.response.status 如果是401 未登录没权限的就调用登录页面，其他的就直接弹窗显示错误。
我们需要在原来的main.js 更改成我们自己的axios 的js
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f71c5262d4a450399c3611a37863654~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>测试检查一下，我们先在mock .js 里面输入错误的转态吗</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7bedc7669e8452fab9dcccaaabcb273~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>效果</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d7656a88c34495e944a47a660ecb95d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">后台界面开发</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9db3a67bb8c240e7a2b83d3f5782536a~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>这里我选择的是</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><el-container>
  <el-header>Header</el-header>
  <el-container>
    <el-aside width=<span class="hljs-string">"200px"</span>>Aside</el-aside>
    <el-main>Main</el-main>
  </el-container>
</el-container>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>创建一个Index 的页面 这里我们需要 先放在这里，一会可以把公共的抽离出来 记得复制样式</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a61c79b9331c4d5d8f18e26db9932634~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
添加到路由里面
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0b2d2817df6476a8382eb5094f28d45~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>效果</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fa1ecbe0b8c45d48134adf7d6256f87~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>添加一个样式设置一下高度</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fa8619c496e40158a655b23ace8a18a~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">头部导航栏的设置</h4>
<p><strong>Index.vue 页面</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-container</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-aside</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200px"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>菜单栏<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-aside</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-container</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-header</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"height: 55px;"</span>></span><span class="hljs-tag"><<span class="hljs-name">Strong</span>></span>ManHub后台管理系统<span class="hljs-tag"></<span class="hljs-name">Strong</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"header-avatar block"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-avatar</span>  <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-avatar</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-dropdown</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-dropdown-link"</span>></span>
            fjj<span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-arrow-down el-icon--right"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-dropdown-menu</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"dropdown"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/userCenter"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">el-dropdown-item</span>></span>个人中心<span class="hljs-tag"></<span class="hljs-name">el-dropdown-item</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-dropdown-item</span> @<span class="hljs-attr">click.native</span>=<span class="hljs-string">"logout"</span>></span>退出<span class="hljs-tag"></<span class="hljs-name">el-dropdown-item</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">el-dropdown-menu</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-dropdown</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://markerhub.com"</span>></span>网站<span class="hljs-tag"></<span class="hljs-name">el-link</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-header</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-main</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin: 0 15px;"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-main</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-container</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-container</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Index"</span>
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-comment">/*下拉框的css*/</span>
<span class="hljs-selector-class">.el-dropdown-link</span> &#123;
  <span class="hljs-attribute">cursor</span>: pointer;
  <span class="hljs-attribute">color</span>: black;
&#125;

<span class="hljs-selector-class">.el-icon-arrow-down</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">12px</span>;
&#125;

<span class="hljs-comment">/*设置头部导航的样式*/</span>
<span class="hljs-selector-class">.header-avatar</span> &#123;
  <span class="hljs-attribute">float</span>: right;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">210px</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: space-around;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">text-align</span>: center;
&#125;

<span class="hljs-comment">/*导航栏的css*/</span>
<span class="hljs-selector-class">.el-container</span> &#123;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0vh</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
&#125;

<span class="hljs-selector-class">.el-header</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#D3DCE6</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">60px</span>;
&#125;

<span class="hljs-selector-class">.el-aside</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#D3DCE6</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">200px</span>;
&#125;

<span class="hljs-selector-class">.el-main</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
  <span class="hljs-attribute">padding-left</span>: <span class="hljs-number">20px</span>;
&#125;

<span class="hljs-comment">/*取除a 标签的下划线*/</span>
<span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">text-decoration</span>: none;
&#125;

<span class="hljs-comment">/*设置 链接滑上去变成小手*/</span>
<span class="hljs-selector-class">.el-dropdown-link</span> &#123;
  <span class="hljs-attribute">cursor</span>: pointer;
  <span class="hljs-attribute">color</span>: black;
&#125;

<span class="hljs-comment">/*设置侧边栏的高度*/</span>
<span class="hljs-selector-class">.el-menu-vertical-demo</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
&#125;

<span class="hljs-comment">/*取除a 标签的下划线*/</span>
<span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">text-decoration</span>: none;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4c2bac23e4648a88392b7fbb1d63488~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">侧边导航栏的设置</h4>
<p>**差不多感觉是对的，在 element-ui 上找到菜单栏的组件，添加到Home .vue 里面，但是要做成动态的菜单，所以可以单独的拿出来，新建一个SideMenu.vue **
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bd43dff80884722b6ec52f120ea7805~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-menu</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-menu-vertical-demo"</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#545c64"</span> <span class="hljs-attr">text-color</span>=<span class="hljs-string">"#fff"</span> <span class="hljs-attr">active-text-color</span>=<span class="hljs-string">"#ffd04b"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/index"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-menu-item</span> <span class="hljs-attr">index</span>=<span class="hljs-string">"Index"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-s-home"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-menu-item</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-submenu</span> <span class="hljs-attr">index</span>=<span class="hljs-string">"1"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-s-operation"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span>></span>系统管理<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-menu-item</span> <span class="hljs-attr">index</span>=<span class="hljs-string">"1-1"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-s-custom"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span>用户管理<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-menu-item</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-menu-item</span> <span class="hljs-attr">index</span>=<span class="hljs-string">"1-2"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-rank"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span>角色管理<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-menu-item</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-menu-item</span> <span class="hljs-attr">index</span>=<span class="hljs-string">"1-3"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-menu"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span>菜单管理<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-menu-item</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-submenu</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-submenu</span> <span class="hljs-attr">index</span>=<span class="hljs-string">"2"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-s-tools"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span>></span>系统工具<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-menu-item</span> <span class="hljs-attr">index</span>=<span class="hljs-string">"2-2"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-s-order"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span>数字字典<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-menu-item</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-submenu</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-menu</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"SideMenu"</span>
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-comment">/*设置侧边栏的高度*/</span>
<span class="hljs-selector-class">.el-menu-vertical-demo</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
&#125;
<span class="hljs-comment">/*取除a 标签的下划线*/</span>
<span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">text-decoration</span>: none;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>此时SideMenu.vue 作为一个组件添加到Home.vue 中，我们需要导入，声明组件，才能使用标签，所以应该在Index.vue 中 声明就可以使用了</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c2440e8577d40d4939e808befd54ac7~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4475be88f35f40b6b188653576b8db72~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>效果</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60945473897f4626994353c6271f855d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>把整体的框架移除到Home.vue 里面，在Index 里面只留下中间的 内容</strong>
移除完之后的Home.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-container</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-aside</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200px"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">SideMenu</span>></span><span class="hljs-tag"></<span class="hljs-name">SideMenu</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-aside</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-container</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-header</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"height: 55px;"</span>></span><span class="hljs-tag"><<span class="hljs-name">Strong</span>></span>ManHub后台管理系统<span class="hljs-tag"></<span class="hljs-name">Strong</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"header-avatar block"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-avatar</span>  <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-avatar</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-dropdown</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-dropdown-link"</span>></span>
            fjj<span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-arrow-down el-icon--right"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-dropdown-menu</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"dropdown"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/userCenter"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">el-dropdown-item</span>></span>个人中心<span class="hljs-tag"></<span class="hljs-name">el-dropdown-item</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-dropdown-item</span> @<span class="hljs-attr">click.native</span>=<span class="hljs-string">"logout"</span>></span>退出<span class="hljs-tag"></<span class="hljs-name">el-dropdown-item</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">el-dropdown-menu</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-dropdown</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://markerhub.com"</span>></span>网站<span class="hljs-tag"></<span class="hljs-name">el-link</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-header</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-main</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin: 0 15px;"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-main</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-container</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-container</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> SideMenu <span class="hljs-keyword">from</span> <span class="hljs-string">"./inc/SideMenu"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Home"</span>,
  <span class="hljs-attr">components</span>: &#123;SideMenu&#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-comment">/*下拉框的css*/</span>
<span class="hljs-selector-class">.el-dropdown-link</span> &#123;
  <span class="hljs-attribute">cursor</span>: pointer;
  <span class="hljs-attribute">color</span>: black;
&#125;

<span class="hljs-selector-class">.el-icon-arrow-down</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">12px</span>;
&#125;

<span class="hljs-comment">/*设置头部导航的样式*/</span>
<span class="hljs-selector-class">.header-avatar</span> &#123;
  <span class="hljs-attribute">float</span>: right;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">210px</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: space-around;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">text-align</span>: center;
&#125;

<span class="hljs-comment">/*导航栏的css*/</span>
<span class="hljs-selector-class">.el-container</span> &#123;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0vh</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
&#125;

<span class="hljs-selector-class">.el-header</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#D3DCE6</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">60px</span>;
&#125;

<span class="hljs-selector-class">.el-aside</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#D3DCE6</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">200px</span>;
&#125;

<span class="hljs-selector-class">.el-main</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
  <span class="hljs-attribute">padding-left</span>: <span class="hljs-number">20px</span>;
&#125;

<span class="hljs-comment">/*取除a 标签的下划线*/</span>
<span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">text-decoration</span>: none;
&#125;

<span class="hljs-comment">/*设置 链接滑上去变成小手*/</span>
<span class="hljs-selector-class">.el-dropdown-link</span> &#123;
  <span class="hljs-attribute">cursor</span>: pointer;
  <span class="hljs-attribute">color</span>: black;
&#125;

<span class="hljs-comment">/*设置侧边栏的高度*/</span>
<span class="hljs-selector-class">.el-menu-vertical-demo</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
&#125;

<span class="hljs-comment">/*取除a 标签的下划线*/</span>
<span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">text-decoration</span>: none;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>移除完之后的index.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>中间部分<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Index"</span>

&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>


<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>这个时候当我们访问Index的时候只有中间的部分没有 整个框架是不行的</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4774cda7cc54c74bcf1411c93650ba1~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>应该把index.vue 作为 Home 的子路由 ，这样当我们访问index 的时候就会显示父级的路由了</strong>
第一步 修改路由
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15ff88472e8349d79cca8281e946d360~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
第二步，修改 Home.vue
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fec07247cab343df95bd911a72615f48~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>加上这句话，这个时候，我们在看效果的时候</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c28528ad86664630863b83aa10e8ddba~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-19">侧边导航栏的路由</h4>
<p>新建几个页面，先在views 下新建文件夹，然后再新建vue 页面。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24b1dffaab3c4c13ad29abe7f97cada8~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>添加路由到index.js 中
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8397ffdf1b148df96ef33672ed8b29c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>这个时候我们点击左边的用户管理都还不会点击到页面的链接修改Home 的页面</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f234bc897dbc467c8527749f2208c08e~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>效果</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ee48a9bafb84a7e84751ff250702781~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-20">用户登录信息展示,以及退出登录清除 浏览器缓存</h4>
<p>管理界面的右上角是被写死的，我们现在登录成功，所以可以通过接口去请求获取到当前的用户信息，这样就可以动态显示用户信息了
<strong>Home.vue</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8a74545d73b403998319277c1506cd9~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3f1c9a856f8425dbad88134029f0c34~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>在 mock.js 里面写请求以及测试数据</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 个人中心的测试数据</span>
Mock.mock(<span class="hljs-string">'/sys/userInfo'</span>,<span class="hljs-string">'get'</span>,() =>&#123;
    Result.data = &#123;
        id: <span class="hljs-string">'1'</span>,
        username :<span class="hljs-string">'冯娇娇'</span>,
        avatar: <span class="hljs-string">'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'</span>
    &#125;
    <span class="hljs-keyword">return</span> Result
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b929b5f8718495f978f7ed76a5ec1fa~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>退出登录的</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43cb3b8a61a84c97a59635779438557e~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>mock.js 数据</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 退出登录的</span>
Mock.mock(<span class="hljs-string">'/logout'</span>, <span class="hljs-string">'post'</span>, () => &#123;
    <span class="hljs-keyword">return</span> Result
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">个人中心的界面</h4>
<p>创建个人中心的vue
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fd6d1ae26ce4727bab6ad215f964856~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-align: center;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>你好！&#123;&#123; userInfo.username &#125;&#125; 同学<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:model</span>=<span class="hljs-string">"passForm"</span> <span class="hljs-attr">status-icon</span> <span class="hljs-attr">:rules</span>=<span class="hljs-string">"rules"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"passForm"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"旧密码"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"currentPass"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"passForm.currentPass"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"新密码"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"password"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"passForm.password"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"确认密码"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"checkPass"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"passForm.checkPass"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitForm('passForm')"</span>></span>提交<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"resetForm('passForm')"</span>></span>重置<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Login'</span>,
  data () &#123;
    <span class="hljs-keyword">var</span> validatePass = <span class="hljs-function">(<span class="hljs-params">rule, value, callback</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (value === <span class="hljs-string">''</span>) &#123;
        callback(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请再次输入密码'</span>))
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (value !== <span class="hljs-built_in">this</span>.passForm.password) &#123;
        callback(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'两次输入密码不一致!'</span>))
      &#125; <span class="hljs-keyword">else</span> &#123;
        callback()
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">userInfo</span>: &#123;

      &#125;,
      <span class="hljs-attr">passForm</span>: &#123;
        <span class="hljs-attr">password</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">checkPass</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">currentPass</span>: <span class="hljs-string">''</span>
      &#125;,
      <span class="hljs-attr">rules</span>: &#123;
        <span class="hljs-attr">password</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入新密码'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;,
          &#123; <span class="hljs-attr">min</span>: <span class="hljs-number">6</span>, <span class="hljs-attr">max</span>: <span class="hljs-number">12</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'长度在 6 到 12 个字符'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">checkPass</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">validator</span>: validatePass, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">currentPass</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入当前密码'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ]
      &#125;
    &#125;
  &#125;,
  created () &#123;
    <span class="hljs-built_in">this</span>.getUserInfo()
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    getUserInfo () &#123;
      <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/sys/userInfo'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.userInfo = res.data.data
      &#125;)
    &#125;,
    submitForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].validate(<span class="hljs-function">(<span class="hljs-params">valid</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (valid) &#123;
          <span class="hljs-keyword">const</span> _this = <span class="hljs-built_in">this</span>
          <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/sys/user/updatePass'</span>, <span class="hljs-built_in">this</span>.passForm).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            _this.$alert(res.data.msg, <span class="hljs-string">'提示'</span>, &#123;
              <span class="hljs-attr">confirmButtonText</span>: <span class="hljs-string">'确定'</span>,
              <span class="hljs-attr">callback</span>: <span class="hljs-function"><span class="hljs-params">action</span> =></span> &#123;
                <span class="hljs-built_in">this</span>.$refs[formName].resetFields()
              &#125;
            &#125;)
          &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error submit!!'</span>)
          <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125;
      &#125;)
    &#125;,
    resetForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].resetFields()
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.el-form</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">420px</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">50px</span> auto;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>需要在 Home .vue 里写这句话</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8a803096e97420e9fda28bf7492595d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
在index 里面设置我们的路由就可以了
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e75c95efc2243088a2ccf8875ba185c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a849d8022fe64e1682fdb1b2a1fe60e3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击之后
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d959d2818134bd7ae1e3c8e51927c54~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-22">动态菜单栏开发</h4>
<p>上面的代码中，左侧的菜单栏的数据是写死的，在实际情况中不应该是写死的，因为菜单是需要根据登录用户的权限动态显示菜单的，也就是用户看到的菜单栏可能是不一样的，这些数据需要去后端访问获取到
应该把数据简化成一个json 数组数据，然后for 循环展示出来，代码如下
<strong>SideMenu.vue</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-menu</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-menu-vertical-demo"</span> <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#545c64"</span> <span class="hljs-attr">text-color</span>=<span class="hljs-string">"#fff"</span> <span class="hljs-attr">active-text-color</span>=<span class="hljs-string">"#ffd04b"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/index"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-menu-item</span> <span class="hljs-attr">index</span>=<span class="hljs-string">"Index"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-s-home"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-menu-item</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-submenu</span> <span class="hljs-attr">:index</span>=<span class="hljs-string">"menu.name"</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"menu in menuList"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"menu.name"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"menu.icon"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;menu.title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"item.path"</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in menu.children"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.path"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-menu-item</span> <span class="hljs-attr">:index</span>=<span class="hljs-string">"item.name"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"selectMenu(item)"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"item.icon"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span>&#123;&#123;item.title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-menu-item</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-submenu</span>></span>

  <span class="hljs-tag"></<span class="hljs-name">el-menu</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"SideMenu"</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">menuList</span>: [&#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'SysManga'</span>,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'系统管理'</span>,
        <span class="hljs-attr">icon</span>: <span class="hljs-string">'el-icon-s-operation'</span>,
        <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">children</span>: [&#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">'SysUser'</span>,
          <span class="hljs-attr">title</span>: <span class="hljs-string">'用户管理'</span>,
          <span class="hljs-attr">icon</span>: <span class="hljs-string">'el-icon-s-custom'</span>,
          <span class="hljs-attr">path</span>: <span class="hljs-string">'/user'</span>,
          <span class="hljs-attr">children</span>: []
        &#125;]
      &#125;, &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'SysTools'</span>,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'系统工具'</span>,
        <span class="hljs-attr">icon</span>: <span class="hljs-string">'el-icon-s-tools'</span>,
        <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">children</span>: [&#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">'SysDict'</span>,
          <span class="hljs-attr">title</span>: <span class="hljs-string">'数字字典'</span>,
          <span class="hljs-attr">icon</span>: <span class="hljs-string">'el-icon-s-order'</span>,
          <span class="hljs-attr">path</span>: <span class="hljs-string">'/sys/dicts'</span>,
          <span class="hljs-attr">children</span>: []
        &#125;,]
      &#125;],
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-comment">/*设置侧边栏的高度*/</span>
<span class="hljs-selector-class">.el-menu-vertical-demo</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
&#125;

<span class="hljs-comment">/*取除a 标签的下划线*/</span>
<span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">text-decoration</span>: none;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>可以看到，用 for 循环显示数据，那么这样变动菜单栏的时候只需要修改data 中的menuList 即可，效果和之前的完全一样。现在menuList 的数据我们是直接写到页面data 上的，一般我们是要请求后端的，所以需要定义一个mock 的接口，应为是动态的菜单，我们也要考虑到权限问题，所以我们请求数据的时候一般出来动态菜单，还要权限的数据，比如菜单的添加，删除是否有权限，是否能显示等。。</strong>
<strong>Mock.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Mock.mock(<span class="hljs-string">'/sys/menu/nav'</span>, <span class="hljs-string">'get'</span>, <span class="hljs-function">() =></span> &#123;
<span class="hljs-comment">// 菜单json</span>
 <span class="hljs-keyword">let</span> nav = [     
  &#123;      
     <span class="hljs-attr">name</span>: <span class="hljs-string">'SysManga'</span>,
      ...
       &#125;,
     &#123;       
       <span class="hljs-attr">name</span>: <span class="hljs-string">'SysTools'</span>,    
            ...    
              &#125;   
          ]
          <span class="hljs-comment">// 权限数据</span>
          <span class="hljs-keyword">let</span> authoritys = [<span class="hljs-string">'SysUser'</span>, <span class="hljs-string">"SysUser:save"</span>]
          Result.data = &#123;&#125; 
          Result.data.nav = nav  
          Result.data.authoritys = authoritys  
          <span class="hljs-keyword">return</span> Result       
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义好导航菜单的接口，应该在登录成功完成之后调用，但是并不是每一次打开都需要登录，也就是浏览器已经存储到用户token 的时候我们不需要再去登录了所以我们不能放在登录完成的方法里了。
这里需要考虑一个问题，就是导航菜单的路由问题，当我们点击菜单之后路由到那个页面是需要在 router 中声明
<strong>解决方案： 动态渲染，把加载到导航菜单数据动态绑定路由</strong>
把加载菜单数据这个动作放在 router.js 中，Router 有个前缀拦截，就是在路由到页面之前我们可以做一些判断或者加载数据</p>
<p>在router.js中添加一下代码：
src/router/index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 动态导航栏的</span>
router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> hasRoute = store.state.menus.hasRoute
    <span class="hljs-keyword">const</span> token = <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'token'</span>)
    <span class="hljs-keyword">if</span> (to.path === <span class="hljs-string">'/login'</span>) &#123;
        next()
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!token) &#123;
        next(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span> &#125;)
    &#125;
    <span class="hljs-keyword">if</span> (token && !hasRoute) &#123;
        axios.get(<span class="hljs-string">'/sys/menu/nav'</span>, &#123;
            <span class="hljs-attr">headers</span>: &#123;
                <span class="hljs-attr">Authorization</span>: <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'token'</span>)
            &#125;
        &#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            <span class="hljs-built_in">console</span>.log(res.data.data)
            store.commit(<span class="hljs-string">'setMenuList'</span>, res.data.data.nav)
            store.commit(<span class="hljs-string">'setPermList'</span>, res.data.data.authoritys)
            <span class="hljs-comment">// 动态绑定路由</span>
            <span class="hljs-keyword">const</span> newRoutes = router.options.routes
            res.data.data.nav.forEach(<span class="hljs-function"><span class="hljs-params">menu</span> =></span> &#123;
                <span class="hljs-keyword">if</span> (menu.children) &#123;
                    menu.children.forEach(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
                        <span class="hljs-keyword">const</span> route = menuToRoute(e)
                        <span class="hljs-keyword">if</span> (route) &#123;
                            newRoutes[<span class="hljs-number">0</span>].children.push(route)
                        &#125;
                    &#125;)
                &#125;
            &#125;)
            <span class="hljs-built_in">console</span>.log(newRoutes)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'newRoutes'</span>)
            router.addRoutes(newRoutes)
            hasRoute = <span class="hljs-literal">true</span>
            store.commit(<span class="hljs-string">'changeRouteStatus'</span>, hasRoute)
        &#125;)
    &#125;

    next()
&#125;)
<span class="hljs-keyword">const</span> menuToRoute = <span class="hljs-function">(<span class="hljs-params">menu</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!menu.component) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-comment">// 复制到属性</span>
    <span class="hljs-keyword">const</span> route = &#123;
        <span class="hljs-attr">path</span>: menu.path,
        <span class="hljs-attr">name</span>: menu.name,
        <span class="hljs-attr">meta</span>: &#123;
            <span class="hljs-attr">icon</span>: menu.icon,
            <span class="hljs-attr">title</span>: menu.title
        &#125;
    &#125;
    route.component = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/'</span> + menu.component + <span class="hljs-string">'.vue'</span>)
    <span class="hljs-built_in">console</span>.log(route)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'route'</span>)
    <span class="hljs-keyword">return</span> route
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>可以看到，我们通过menuToRoute 就是把menu 数据 转换成路由对象，然后router.addRoutes(newRoutes)动态添加路由对象同时上面的menu对象中，有个menu.component，这个就是连接对应的组件，我们需要添加上去，比如说/sys/users链接对应到component(sys/User)。同时上面的menu对象中，有个menu.component，这个就是连接对应的组件，我们需要添加上去，比如说/sys/users链接对应到component(sys/User)。</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// 菜单的json</span>
    <span class="hljs-keyword">const</span> nav = [&#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'SysManga'</span>,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'系统管理'</span>,
        <span class="hljs-attr">icon</span>: <span class="hljs-string">'el-icon-s-operation'</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">children</span>: [
            &#123;
                <span class="hljs-attr">title</span>: <span class="hljs-string">'用户管理'</span>,
                <span class="hljs-attr">icon</span>: <span class="hljs-string">'el-icon-s-custom'</span>,
                <span class="hljs-attr">path</span>: <span class="hljs-string">'/sys/users'</span>,
                <span class="hljs-attr">name</span>: <span class="hljs-string">'SysUser'</span>,
                <span class="hljs-attr">component</span>: <span class="hljs-string">'sys/User'</span>,
                <span class="hljs-attr">children</span>: []
            &#125;,
            &#123;
                <span class="hljs-attr">name</span>: <span class="hljs-string">'SysRole'</span>,
                <span class="hljs-attr">title</span>: <span class="hljs-string">'角色管理'</span>,
                <span class="hljs-attr">icon</span>: <span class="hljs-string">'el-icon-rank'</span>,
                <span class="hljs-attr">path</span>: <span class="hljs-string">'/sys/roles'</span>,
                <span class="hljs-attr">component</span>: <span class="hljs-string">'sys/Role'</span>,
                <span class="hljs-attr">children</span>: []
            &#125;,
            &#123;
                <span class="hljs-attr">name</span>: <span class="hljs-string">'SysMenu'</span>,
                <span class="hljs-attr">title</span>: <span class="hljs-string">'菜单管理'</span>,
                <span class="hljs-attr">icon</span>: <span class="hljs-string">'el-icon-menu'</span>,
                <span class="hljs-attr">path</span>: <span class="hljs-string">'/sys/menus'</span>,
                <span class="hljs-attr">component</span>: <span class="hljs-string">'sys/Menu'</span>,
                <span class="hljs-attr">children</span>: []
            &#125;
        ]
    &#125;, &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'SysTools'</span>,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'系统工具'</span>,
        <span class="hljs-attr">icon</span>: <span class="hljs-string">'el-icon-s-tools'</span>,
        <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">children</span>: [
            &#123;
                <span class="hljs-attr">title</span>: <span class="hljs-string">'数字字典'</span>,
                <span class="hljs-attr">icon</span>: <span class="hljs-string">'el-icon-s-order'</span>,
                <span class="hljs-attr">path</span>: <span class="hljs-string">'/sys/dicts'</span>,
                <span class="hljs-attr">component</span>: <span class="hljs-string">''</span>,
                <span class="hljs-attr">children</span>: []
            &#125;]
    &#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>同时上面router中我们还通过判断是否登录页面，是否有token等判断提前判断是否能加载菜单，同时还做了个开关hasRoute来动态判断是否已经加载过菜单。还需要在store中定义几个方法用于存储数据，我们定义一个menu模块，所以在store中新建文件夹modules，然后新建menus.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">state</span>: &#123;      <span class="hljs-comment">// 菜单栏数据   </span>
        <span class="hljs-attr">menuList</span>: [],
        <span class="hljs-comment">// 权限数据  </span>
        <span class="hljs-attr">permList</span>: [],
        <span class="hljs-attr">hasRoute</span>: <span class="hljs-literal">false</span>
    &#125;, <span class="hljs-attr">mutations</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">changeRouteStatus</span>(<span class="hljs-params">state, hasRoute</span>)</span> &#123;
            state.hasRoute = hasRoute
            sessionStorage.setItem(<span class="hljs-string">"hasRoute"</span>, hasRoute)
        &#125;, <span class="hljs-function"><span class="hljs-title">setMenuList</span>(<span class="hljs-params">state, menus</span>)</span> &#123;
            state.menuList = menus
        &#125;, <span class="hljs-function"><span class="hljs-title">setPermList</span>(<span class="hljs-params">state, authoritys</span>)</span> &#123;
            state.permList = authoritys
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>记得在store中import这个模块，然后添加到modules：src/store/index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> menus <span class="hljs-keyword">from</span> <span class="hljs-string">"./modules/menus"</span>
...
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;  
...  modules:
 &#123;    menus  &#125;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们菜单的数据就可以加载了，然后再SideMenu.vue中直接获取store中的menuList数据即可显示菜单出来了。src/views/inc/SideMenu.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;   
 <span class="hljs-keyword">return</span> &#123;   
      <span class="hljs-attr">menuList</span>: <span class="hljs-built_in">this</span>.$store.state.menus.menuList, 
         &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果如下</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ced42d3228d94d1295b5bf5d01577afd~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-23">动态标签页开发</h4>
<p>1，当我们点击导航菜单，上方会添加一个对应的标签，注意不能重复添加，发现已存在标签直接切换到这标签就可以
2，删除当前标签的时候会自动切换到前一个标签页
3，点击标签的时候会调整到对应的内容页中
我们先和左侧菜单一样单独定义一个组件Tabs.vue放在views/inc文件夹内：
src/views/inc/Tabs.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-tabs</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editableTabsValue"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"card"</span> <span class="hljs-attr">closable</span> @<span class="hljs-attr">tab-remove</span>=<span class="hljs-string">"removeTab"</span> @<span class="hljs-attr">tab-click</span>=<span class="hljs-string">"clickTab"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-tab-pane</span>
      <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item) in editableTabs"</span>
      <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.name"</span>
      <span class="hljs-attr">:label</span>=<span class="hljs-string">"item.title"</span>
      <span class="hljs-attr">:name</span>=<span class="hljs-string">"item.name"</span>
    ></span>
    <span class="hljs-tag"></<span class="hljs-name">el-tab-pane</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-tabs</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Tabs'</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">editableTabsValue</span>: <span class="hljs-built_in">this</span>.$store.state.menus.editableTabsValue,
      <span class="hljs-attr">tabIndex</span>: <span class="hljs-number">2</span>
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-attr">editableTabs</span>: &#123;
      get () &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$store.state.menus.editableTabs
      &#125;,
      set (val) &#123;
        <span class="hljs-built_in">this</span>.$store.state.menus.editableTabs = val
      &#125;
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    removeTab (targetName) &#123;
      <span class="hljs-keyword">const</span> tabs = <span class="hljs-built_in">this</span>.editableTabs
      <span class="hljs-keyword">let</span> activeName = <span class="hljs-built_in">this</span>.editableTabsValue
      <span class="hljs-keyword">if</span> (targetName === <span class="hljs-string">'Index'</span>) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-keyword">if</span> (activeName === targetName) &#123;
        tabs.forEach(<span class="hljs-function">(<span class="hljs-params">tab, index</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (tab.name === targetName) &#123;
            <span class="hljs-keyword">const</span> nextTab = tabs[index + <span class="hljs-number">1</span>] || tabs[index - <span class="hljs-number">1</span>]
            <span class="hljs-keyword">if</span> (nextTab) &#123;
              activeName = nextTab.name
            &#125;
          &#125;
        &#125;)
      &#125;
      <span class="hljs-built_in">this</span>.editableTabsValue = activeName
      <span class="hljs-built_in">this</span>.editableTabs = tabs.filter(<span class="hljs-function"><span class="hljs-params">tab</span> =></span> tab.name !== targetName)
      <span class="hljs-built_in">this</span>.$router.push(&#123; <span class="hljs-attr">name</span>: activeName &#125;)
    &#125;,
    clickTab (target) &#123;
      <span class="hljs-built_in">this</span>.$router.push(&#123; <span class="hljs-attr">name</span>: target.name &#125;)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>computed 表示当其依赖的属性的值发生变化时，计算属性会重新计算，反之，则使用缓存中的属性值，其他clickTab removeTab 的逻辑就比较简单，特别是removeTab 注意考虑多种情况就可以，修改meun.js 添加editableTabsValue 和 editableTabs 然后把首页作为默认显示的页面
src/store/modules/menus.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  state: &#123;
    <span class="hljs-comment">// 菜单栏数据</span>
    <span class="hljs-attr">menuList</span>: [],
    <span class="hljs-comment">// 权限数据</span>
    <span class="hljs-attr">permList</span>: [],
    <span class="hljs-attr">hasRoute</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">editableTabsValue</span>: <span class="hljs-string">'Index'</span>,
    <span class="hljs-attr">editableTabs</span>: [&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'首页'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'Index'</span>
    &#125;]
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再Home.vue中引入我们Tabs.vue这个组件</p>
<pre><code class="hljs language-java copyable" lang="java"># 引入组件<span class="hljs-keyword">import</span> Tabs from <span class="hljs-string">"./inc/Tabs"</span>
# 声明组件
components: &#123;   
SideMenu, Tabs
&#125;,
<el-main> 
  # 使用组件 
    <Tabs></Tabs>   
    <div style=<span class="hljs-string">"margin: 0 15px;"</span>>  
        <router-view></router-view> 
          </div>
          </el-main>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>现在的效果</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ce1e008a4b246eebd998e10db1a6a5f~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
完成了第一步之后，现在我们需要点击菜单导航，然后tabs 列表中添加tab 标签页，那么我们应该修改sideMeun.vue 页面
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc5754ab9e90469d9afd7433ca4cef5c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
因为tabs标签列表我们是存储在store中的，因此我们需要commit提交事件，因此我们在menu.js中添加addTabs方法：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbf0ba26633c42ed81c16d399f4081eb~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
刷新浏览器之后链接/sys/users不变，内容不变，但是Tab却不见了，所以我们需要修补一下，当用户是直接通过输入链接形式打开页面的时候我们也能根据链接自动添加激活指定的tab。那么在哪里添加这个回显的方法呢？router中？其实可以，只不过我们需要做判断，因为每次点击导航都会触发router。有没有更简便的方法？有的！因为刷新或者打开页面都是一次性的行为，所以我们可以在更高层的App.vue中做这个回显动作，具体如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f931d225eb2c448fb9643ea6d635b823~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面代码可以看到，除了login页面，其他页面都会触发addTabs方法，这样我们就可以添加tab和激活tab了。</p>
<h3 data-id="heading-24">个人中心</h3>
<h4 data-id="heading-25">个人中心的页面</h4>
<p><strong>创建 UserCenCenter.vue</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7546cb931459482a96fa0a4d17824461~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-align: center;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>你好！&#123;&#123; userInfo.username &#125;&#125; 同学<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:model</span>=<span class="hljs-string">"passForm"</span> <span class="hljs-attr">status-icon</span> <span class="hljs-attr">:rules</span>=<span class="hljs-string">"rules"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"passForm"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"旧密码"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"currentPass"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"passForm.currentPass"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"新密码"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"password"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"passForm.password"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"确认密码"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"checkPass"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"passForm.checkPass"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitForm('passForm')"</span>></span>提交<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"resetForm('passForm')"</span>></span>重置<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Login'</span>,
  data () &#123;
    <span class="hljs-keyword">var</span> validatePass = <span class="hljs-function">(<span class="hljs-params">rule, value, callback</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (value === <span class="hljs-string">''</span>) &#123;
        callback(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请再次输入密码'</span>))
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (value !== <span class="hljs-built_in">this</span>.passForm.password) &#123;
        callback(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'两次输入密码不一致!'</span>))
      &#125; <span class="hljs-keyword">else</span> &#123;
        callback()
      &#125;
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">userInfo</span>: &#123;

      &#125;,
      <span class="hljs-attr">passForm</span>: &#123;
        <span class="hljs-attr">password</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">checkPass</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">currentPass</span>: <span class="hljs-string">''</span>
      &#125;,
      <span class="hljs-attr">rules</span>: &#123;
        <span class="hljs-attr">password</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入新密码'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;,
          &#123; <span class="hljs-attr">min</span>: <span class="hljs-number">6</span>, <span class="hljs-attr">max</span>: <span class="hljs-number">12</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'长度在 6 到 12 个字符'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">checkPass</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">validator</span>: validatePass, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">currentPass</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入当前密码'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ]
      &#125;
    &#125;
  &#125;,
  created () &#123;
    <span class="hljs-built_in">this</span>.getUserInfo()
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    getUserInfo () &#123;
      <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/sys/userInfo'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.userInfo = res.data.data
      &#125;)
    &#125;,
    submitForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].validate(<span class="hljs-function">(<span class="hljs-params">valid</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (valid) &#123;
          <span class="hljs-keyword">const</span> _this = <span class="hljs-built_in">this</span>
          <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/sys/user/updatePass'</span>, <span class="hljs-built_in">this</span>.passForm).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            _this.$alert(res.data.msg, <span class="hljs-string">'提示'</span>, &#123;
              <span class="hljs-attr">confirmButtonText</span>: <span class="hljs-string">'确定'</span>,
              <span class="hljs-attr">callback</span>: <span class="hljs-function"><span class="hljs-params">action</span> =></span> &#123;
                <span class="hljs-built_in">this</span>.$refs[formName].resetFields()
              &#125;
            &#125;)
          &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error submit!!'</span>)
          <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125;
      &#125;)
    &#125;,
    resetForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].resetFields()
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.el-form</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">420px</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">50px</span> auto;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">菜单界面</h3>
<h4 data-id="heading-27">菜单页面</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d311b2d9ceb4b6898944c3500fbea3a~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>菜单管理我们用到了Table表格组件的树形结构数据，我们只需要根据例子自己组装数据，就可以自动显示出来了
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45bc0a0ecd7e4a77bb55a9d1fb40e7f2~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
这里原来应该是一个 树形结构 但是elemenui 没有就加了 -
具体代码
src/views/sys/Menu.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:inline</span>=<span class="hljs-string">"true"</span> <span class="hljs-attr">:model</span>=<span class="hljs-string">"formInline"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"editForm"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"demo-form-inline"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"dialogVisible = true"</span>></span>新增<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-table</span>
    <span class="hljs-attr">:data</span>=<span class="hljs-string">"tableData"</span>
    <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%;margin-bottom: 20px;"</span>
    <span class="hljs-attr">row-key</span>=<span class="hljs-string">"id"</span>
    <span class="hljs-attr">border</span>
    <span class="hljs-attr">stripe</span>
    <span class="hljs-attr">default-expand-all</span>
    <span class="hljs-attr">:tree-props</span>=<span class="hljs-string">"&#123;children: 'children', hasChildren: 'hasChildren'&#125;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
      <span class="hljs-attr">prop</span>=<span class="hljs-string">"name"</span>
      <span class="hljs-attr">label</span>=<span class="hljs-string">"名称"</span>
      <span class="hljs-attr">sortable</span>
      <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
      <span class="hljs-attr">prop</span>=<span class="hljs-string">"perm"</span>
      <span class="hljs-attr">label</span>=<span class="hljs-string">"权限编码"</span>
      <span class="hljs-attr">sortable</span>
      <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
      <span class="hljs-attr">prop</span>=<span class="hljs-string">"icon"</span>
      <span class="hljs-attr">label</span>=<span class="hljs-string">"图标"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"type"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"类型"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"scope.row.type === 0"</span>></span>目录<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"scope.row.type === 1"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span>></span>菜单<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"scope.row.type === 2"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"info"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"path"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"菜单URL"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"component"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"菜单组件"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"orderNum"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"排序号"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"statu"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"状态"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"scope.row.statu === 1"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span>></span>正常<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"scope.row.statu === 0"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span>></span>禁用<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"icon"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"操作"</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"editHandle(scope.row.id)"</span>></span>编辑<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-divider</span> <span class="hljs-attr">direction</span>=<span class="hljs-string">"vertical"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-divider</span>></span>

          <span class="hljs-tag"><<span class="hljs-name">template</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-popconfirm</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"这是一段内容确定删除吗？"</span> @<span class="hljs-attr">confirm</span>=<span class="hljs-string">"delHandle(scope.row.id)"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"reference"</span>  ></span>删除<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">el-popconfirm</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span>

        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>

  <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>
<span class="hljs-comment"><!--    新增对话框--></span>
    <span class="hljs-tag"><<span class="hljs-name">el-dialog</span>
      <span class="hljs-attr">title</span>=<span class="hljs-string">"提示"</span>
      <span class="hljs-attr">:visible.sync</span>=<span class="hljs-string">"dialogVisible"</span>
      <span class="hljs-attr">width</span>=<span class="hljs-string">"600px"</span>
      <span class="hljs-attr">:before-close</span>=<span class="hljs-string">"handleClose"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:model</span>=<span class="hljs-string">"editForm"</span> <span class="hljs-attr">:rules</span>=<span class="hljs-string">"editFormRules"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"editForm"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"demo-editForm"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"上级菜单"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"parentId"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-select</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.parentId"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请选择上级菜单"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in tableData"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-option</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">"item.name"</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"item.id"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-option</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"chid in item.children"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-option</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">"chid.name"</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"chid.id"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-option</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; '-  ' + chid.name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-select</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"菜单名称"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"name"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.name"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"权限编码"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"perms"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.perms"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"图标"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"icon"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.icon"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"菜单URL"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"path"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.path"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"菜单组件"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"component"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.component"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"类型"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"type"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-radio-group</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.type"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">0</span>></span>目录<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">1</span>></span>菜单<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">2</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-radio-group</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"状态"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"statu"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-radio-group</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.statu"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">0</span>></span>禁用<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">1</span>></span>正常<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-radio-group</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"排序号"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"orderNum"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input-number</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.orderNum"</span> <span class="hljs-attr">:min</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"排序号"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">el-input-number</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitForm('editForm')"</span>></span>立即创建<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"resetForm('editForm')"</span>></span>重置<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Meun'</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">dialogVisible</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">editForm</span>: [],
      <span class="hljs-attr">editFormRules</span>: &#123;
        <span class="hljs-attr">parentId</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请选择上级菜单'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">name</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入名称'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">perms</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入权限编码'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">type</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请选择状态'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">orderNum</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请填入排序号'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">statu</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请选择状态'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ]
      &#125;,
      <span class="hljs-attr">tableData</span>: []
    &#125;
  &#125;,
  created () &#123;
    <span class="hljs-built_in">this</span>.getMenuTree()
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    getMenuTree () &#123;
      <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/sys/menu/list'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.tableData = res.data.data
      &#125;)
    &#125;,
    submitForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].validate(<span class="hljs-function">(<span class="hljs-params">valid</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (valid) &#123;
          <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/sys/menu/'</span> + (<span class="hljs-built_in">this</span>.editForm.id ? <span class="hljs-string">'update'</span> : <span class="hljs-string">'save'</span>), <span class="hljs-built_in">this</span>.editForm)
            .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
              <span class="hljs-built_in">this</span>.$message(&#123;
                <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">message</span>: <span class="hljs-string">'恭喜你，操作成功'</span>,
                <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
                <span class="hljs-attr">onClose</span>: <span class="hljs-function">() =></span> &#123;
                  <span class="hljs-built_in">this</span>.getMenuTree()
                &#125;
              &#125;)
              <span class="hljs-built_in">this</span>.dialogVisible = <span class="hljs-literal">false</span>
            &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error submit!!'</span>)
          <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125;
      &#125;)
    &#125;,
    editHandle (id) &#123;
      <span class="hljs-built_in">this</span>.dialogVisible = <span class="hljs-literal">true</span>
      <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/sys/menu/info/'</span> + id).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(res.data.data + <span class="hljs-string">'99999999'</span>)
        <span class="hljs-built_in">this</span>.editForm = res.data.data
      &#125;)
    &#125;,
    resetForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].resetFields()
      <span class="hljs-built_in">this</span>.dialogVisible = <span class="hljs-literal">false</span>
      <span class="hljs-built_in">this</span>.editForm = &#123;&#125;
    &#125;,
    handleClose () &#123;
      <span class="hljs-built_in">this</span>.resetForm(<span class="hljs-string">'editForm'</span>)
    &#125;,
    delHandle (id) &#123;
      <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/sys/menu/delete/'</span> + id).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.$message(&#123;
          <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">message</span>: <span class="hljs-string">'恭喜你，操作成功'</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
          <span class="hljs-attr">onClose</span>: <span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">this</span>.getMenuTree()
          &#125;
        &#125;)
      &#125;)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">角色管理</h3>
<h4 data-id="heading-29">角色页面</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1018844e1d8c4a62bae7f87537f2d443~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
角色需要和菜单权限做关联，菜单是个树形结构的，</p>
<p>src/views/sys/Role.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:inline</span>=<span class="hljs-string">"true"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-input</span>
          <span class="hljs-attr">v-model</span>=<span class="hljs-string">"searchForm.name"</span>
          <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"名称"</span>
          <span class="hljs-attr">clearable</span>
        ></span>
        <span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"getRoleList"</span>></span>搜索<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"dialogVisible = true"</span>></span>新增<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-popconfirm</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"这是确定批量删除吗？"</span> @<span class="hljs-attr">confirm</span>=<span class="hljs-string">"delHandle(null)"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"reference"</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"delBtlStatu"</span>></span>批量删除<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-popconfirm</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-table</span>
      <span class="hljs-attr">ref</span>=<span class="hljs-string">"multipleTable"</span>
      <span class="hljs-attr">:data</span>=<span class="hljs-string">"tableData"</span>
      <span class="hljs-attr">tooltip-effect</span>=<span class="hljs-string">"dark"</span>
      <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%"</span>
      <span class="hljs-attr">border</span>
      <span class="hljs-attr">stripe</span>
      @<span class="hljs-attr">selection-change</span>=<span class="hljs-string">"handleSelectionChange"</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">type</span>=<span class="hljs-string">"selection"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"55"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"name"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"名称"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"120"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"code"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"唯一编码"</span>
        <span class="hljs-attr">show-overflow-tooltip</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"remark"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"描述"</span>
        <span class="hljs-attr">show-overflow-tooltip</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"statu"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"状态"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"scope.row.statu === 1"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span>></span>正常<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"scope.row.statu === 0"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span>></span>禁用<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>

      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"icon"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"操作"</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"permHandle(scope.row.id)"</span>></span>分配权限<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-divider</span> <span class="hljs-attr">direction</span>=<span class="hljs-string">"vertical"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-divider</span>></span>

          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"editHandle(scope.row.id)"</span>></span>编辑<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-divider</span> <span class="hljs-attr">direction</span>=<span class="hljs-string">"vertical"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-divider</span>></span>

          <span class="hljs-tag"><<span class="hljs-name">template</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-popconfirm</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"这是一段内容确定删除吗？"</span> @<span class="hljs-attr">confirm</span>=<span class="hljs-string">"delHandle(scope.row.id)"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"reference"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">el-popconfirm</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span>

        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">el-pagination</span>
      @<span class="hljs-attr">size-change</span>=<span class="hljs-string">"handleSizeChange"</span>
      @<span class="hljs-attr">current-change</span>=<span class="hljs-string">"handleCurrentChange"</span>
      <span class="hljs-attr">layout</span>=<span class="hljs-string">"total, sizes, prev, pager, next, jumper"</span>
      <span class="hljs-attr">:page-sizes</span>=<span class="hljs-string">"[10, 20, 50, 100]"</span>
      <span class="hljs-attr">:current-page</span>=<span class="hljs-string">"current"</span>
      <span class="hljs-attr">:page-size</span>=<span class="hljs-string">"size"</span>
      <span class="hljs-attr">:total</span>=<span class="hljs-string">"total"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-pagination</span>></span>

    <span class="hljs-comment"><!--新增对话框--></span>
    <span class="hljs-tag"><<span class="hljs-name">el-dialog</span>
      <span class="hljs-attr">title</span>=<span class="hljs-string">"提示"</span>
      <span class="hljs-attr">:visible.sync</span>=<span class="hljs-string">"dialogVisible"</span>
      <span class="hljs-attr">width</span>=<span class="hljs-string">"600px"</span>
      <span class="hljs-attr">:before-close</span>=<span class="hljs-string">"handleClose"</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:model</span>=<span class="hljs-string">"editForm"</span> <span class="hljs-attr">:rules</span>=<span class="hljs-string">"editFormRules"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"editForm"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"demo-editForm"</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"角色名称"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"name"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.name"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"唯一编码"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"code"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.code"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"描述"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"remark"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.remark"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"状态"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"statu"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-radio-group</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.statu"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">0</span>></span>禁用<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">1</span>></span>正常<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-radio-group</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitForm('editForm')"</span>></span>立即创建<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"resetForm('editForm')"</span>></span>重置<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">el-dialog</span>
      <span class="hljs-attr">title</span>=<span class="hljs-string">"分配权限"</span>
      <span class="hljs-attr">:visible.sync</span>=<span class="hljs-string">"permDialogVisible"</span>
      <span class="hljs-attr">width</span>=<span class="hljs-string">"600px"</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:model</span>=<span class="hljs-string">"permForm"</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-tree</span>
          <span class="hljs-attr">:data</span>=<span class="hljs-string">"permTreeData"</span>
          <span class="hljs-attr">show-checkbox</span>
          <span class="hljs-attr">ref</span>=<span class="hljs-string">"permTree"</span>
          <span class="hljs-attr">:default-expand-all</span>=<span class="hljs-string">true</span>
          <span class="hljs-attr">node-key</span>=<span class="hljs-string">"id"</span>
          <span class="hljs-attr">:check-strictly</span>=<span class="hljs-string">true</span>
          <span class="hljs-attr">:props</span>=<span class="hljs-string">"defaultProps"</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-tree</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"footer"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dialog-footer"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"permDialogVisible = false"</span>></span>取 消<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitPermFormHandle('permForm')"</span>></span>确 定<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Role'</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">searchForm</span>: &#123;&#125;,
      <span class="hljs-attr">delBtlStatu</span>: <span class="hljs-literal">true</span>,

      <span class="hljs-attr">total</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">size</span>: <span class="hljs-number">10</span>,
      <span class="hljs-attr">current</span>: <span class="hljs-number">1</span>,

      <span class="hljs-attr">dialogVisible</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">editForm</span>: &#123;

      &#125;,

      <span class="hljs-attr">tableData</span>: [],

      <span class="hljs-attr">editFormRules</span>: &#123;
        <span class="hljs-attr">name</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入角色名称'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">code</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入唯一编码'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">statu</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请选择状态'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ]
      &#125;,

      <span class="hljs-attr">multipleSelection</span>: [],

      <span class="hljs-attr">permDialogVisible</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">permForm</span>: &#123;&#125;,
      <span class="hljs-attr">defaultProps</span>: &#123;
        <span class="hljs-attr">children</span>: <span class="hljs-string">'children'</span>,
        <span class="hljs-attr">label</span>: <span class="hljs-string">'name'</span>
      &#125;,
      <span class="hljs-attr">permTreeData</span>: []
    &#125;
  &#125;,
  created () &#123;
    <span class="hljs-built_in">this</span>.getRoleList()

    <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/sys/menu/list'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.permTreeData = res.data.data
    &#125;)
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    toggleSelection (rows) &#123;
      <span class="hljs-keyword">if</span> (rows) &#123;
        rows.forEach(<span class="hljs-function"><span class="hljs-params">row</span> =></span> &#123;
          <span class="hljs-built_in">this</span>.$refs.multipleTable.toggleRowSelection(row)
        &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>.$refs.multipleTable.clearSelection()
      &#125;
    &#125;,
    handleSelectionChange (val) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'勾选'</span>)
      <span class="hljs-built_in">console</span>.log(val)
      <span class="hljs-built_in">this</span>.multipleSelection = val

      <span class="hljs-built_in">this</span>.delBtlStatu = val.length === <span class="hljs-number">0</span>
    &#125;,

    handleSizeChange (val) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`每页 <span class="hljs-subst">$&#123;val&#125;</span> 条`</span>)
      <span class="hljs-built_in">this</span>.size = val
      <span class="hljs-built_in">this</span>.getRoleList()
    &#125;,
    handleCurrentChange (val) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`当前页: <span class="hljs-subst">$&#123;val&#125;</span>`</span>)
      <span class="hljs-built_in">this</span>.current = val
      <span class="hljs-built_in">this</span>.getRoleList()
    &#125;,

    resetForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].resetFields()
      <span class="hljs-built_in">this</span>.dialogVisible = <span class="hljs-literal">false</span>
      <span class="hljs-built_in">this</span>.editForm = &#123;&#125;
    &#125;,
    handleClose () &#123;
      <span class="hljs-built_in">this</span>.resetForm(<span class="hljs-string">'editForm'</span>)
    &#125;,

    getRoleList () &#123;
      <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/sys/role/list'</span>, &#123;
        <span class="hljs-attr">params</span>: &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-built_in">this</span>.searchForm.name,
          <span class="hljs-attr">current</span>: <span class="hljs-built_in">this</span>.current,
          <span class="hljs-attr">size</span>: <span class="hljs-built_in">this</span>.size
        &#125;
      &#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.tableData = res.data.data.records
        <span class="hljs-built_in">this</span>.size = res.data.data.size
        <span class="hljs-built_in">this</span>.current = res.data.data.current
        <span class="hljs-built_in">this</span>.total = res.data.data.total
      &#125;)
    &#125;,

    submitForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].validate(<span class="hljs-function">(<span class="hljs-params">valid</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (valid) &#123;
          <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/sys/role/'</span> + (<span class="hljs-built_in">this</span>.editForm.id ? <span class="hljs-string">'update'</span> : <span class="hljs-string">'save'</span>), <span class="hljs-built_in">this</span>.editForm)
            .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
              <span class="hljs-built_in">this</span>.$message(&#123;
                <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">message</span>: <span class="hljs-string">'恭喜你，操作成功'</span>,
                <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
                <span class="hljs-attr">onClose</span>: <span class="hljs-function">() =></span> &#123;
                  <span class="hljs-built_in">this</span>.getRoleList()
                &#125;
              &#125;)

              <span class="hljs-built_in">this</span>.dialogVisible = <span class="hljs-literal">false</span>
              <span class="hljs-built_in">this</span>.resetForm(formName)
            &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error submit!!'</span>)
          <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125;
      &#125;)
    &#125;,
    editHandle (id) &#123;
      <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/sys/role/info/'</span> + id).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.editForm = res.data.data

        <span class="hljs-built_in">this</span>.dialogVisible = <span class="hljs-literal">true</span>
      &#125;)
    &#125;,
    delHandle (id) &#123;
      <span class="hljs-keyword">var</span> ids = []

      <span class="hljs-keyword">if</span> (id) &#123;
        ids.push(id)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>.multipleSelection.forEach(<span class="hljs-function"><span class="hljs-params">row</span> =></span> &#123;
          ids.push(row.id)
        &#125;)
      &#125;

      <span class="hljs-built_in">console</span>.log(ids)

      <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/sys/role/delete'</span>, ids).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.$message(&#123;
          <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">message</span>: <span class="hljs-string">'恭喜你，操作成功'</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
          <span class="hljs-attr">onClose</span>: <span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">this</span>.getRoleList()
          &#125;
        &#125;)
      &#125;)
    &#125;,
    permHandle (id) &#123;
      <span class="hljs-built_in">this</span>.permDialogVisible = <span class="hljs-literal">true</span>

      <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/sys/role/info/'</span> + id).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.$refs.permTree.setCheckedKeys(res.data.data.menuIds)
        <span class="hljs-built_in">this</span>.permForm = res.data.data
      &#125;)
    &#125;,

    submitPermFormHandle (formName) &#123;
      <span class="hljs-keyword">var</span> menuIds = <span class="hljs-built_in">this</span>.$refs.permTree.getCheckedKeys()

      <span class="hljs-built_in">console</span>.log(menuIds)

      <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/sys/role/perm/'</span> + <span class="hljs-built_in">this</span>.permForm.id, menuIds).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.$message(&#123;
          <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">message</span>: <span class="hljs-string">'恭喜你，操作成功'</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
          <span class="hljs-attr">onClose</span>: <span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">this</span>.getRoleList()
          &#125;
        &#125;)
        <span class="hljs-built_in">this</span>.permDialogVisible = <span class="hljs-literal">false</span>
        <span class="hljs-built_in">this</span>.resetForm(formName)
      &#125;)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.el-pagination</span> &#123;
  <span class="hljs-attribute">float</span>: right;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">22px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">用户界面</h3>
<h4 data-id="heading-31">用户页面</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03c92172bec04f2d84c2039d8f9e3f56~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">用户管理有个操作叫分配角色，和角色添加权限差不多的操作</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:inline</span>=<span class="hljs-string">"true"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-input</span>
          <span class="hljs-attr">v-model</span>=<span class="hljs-string">"searchForm.username"</span>
          <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"用户名"</span>
          <span class="hljs-attr">clearable</span>
        ></span>
        <span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"getUserList"</span>></span>搜索<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"dialogVisible = true"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"hasAuth('sys:user:save')"</span>></span>新增<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-popconfirm</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"这是确定批量删除吗？"</span> @<span class="hljs-attr">confirm</span>=<span class="hljs-string">"delHandle(null)"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"reference"</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"delBtlStatu"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"hasAuth('sys:user:delete')"</span>></span>批量删除<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-popconfirm</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">el-table</span>
      <span class="hljs-attr">ref</span>=<span class="hljs-string">"multipleTable"</span>
      <span class="hljs-attr">:data</span>=<span class="hljs-string">"tableData"</span>
      <span class="hljs-attr">tooltip-effect</span>=<span class="hljs-string">"dark"</span>
      <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%"</span>
      <span class="hljs-attr">border</span>
      <span class="hljs-attr">stripe</span>
      @<span class="hljs-attr">selection-change</span>=<span class="hljs-string">"handleSelectionChange"</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">type</span>=<span class="hljs-string">"selection"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"55"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"头像"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"50"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-avatar</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"scope.row.avatar"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-avatar</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"username"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"用户名"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"120"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"code"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"角色名称"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"info"</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in scope.row.sysRoles"</span>></span>&#123;&#123;item.name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>

      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"email"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"邮箱"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"phone"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"手机号"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"statu"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"状态"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"scope.row.statu === 1"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span>></span>正常<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"scope.row.statu === 0"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span>></span>禁用<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>

      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"created"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"创建时间"</span>
      ></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"icon"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"260px"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"操作"</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"roleHandle(scope.row.id)"</span>></span>分配角色<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-divider</span> <span class="hljs-attr">direction</span>=<span class="hljs-string">"vertical"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-divider</span>></span>

          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"repassHandle(scope.row.id, scope.row.username)"</span>></span>重置密码<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-divider</span> <span class="hljs-attr">direction</span>=<span class="hljs-string">"vertical"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-divider</span>></span>

          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"editHandle(scope.row.id)"</span>></span>编辑<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-divider</span> <span class="hljs-attr">direction</span>=<span class="hljs-string">"vertical"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-divider</span>></span>

          <span class="hljs-tag"><<span class="hljs-name">template</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-popconfirm</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"这是一段内容确定删除吗？"</span> @<span class="hljs-attr">confirm</span>=<span class="hljs-string">"delHandle(scope.row.id)"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"reference"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">el-popconfirm</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span>

        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">el-pagination</span>
      @<span class="hljs-attr">size-change</span>=<span class="hljs-string">"handleSizeChange"</span>
      @<span class="hljs-attr">current-change</span>=<span class="hljs-string">"handleCurrentChange"</span>
      <span class="hljs-attr">layout</span>=<span class="hljs-string">"total, sizes, prev, pager, next, jumper"</span>
      <span class="hljs-attr">:page-sizes</span>=<span class="hljs-string">"[10, 20, 50, 100]"</span>
      <span class="hljs-attr">:current-page</span>=<span class="hljs-string">"current"</span>
      <span class="hljs-attr">:page-size</span>=<span class="hljs-string">"size"</span>
      <span class="hljs-attr">:total</span>=<span class="hljs-string">"total"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-pagination</span>></span>

    <span class="hljs-comment"><!--新增对话框--></span>
    <span class="hljs-tag"><<span class="hljs-name">el-dialog</span>
      <span class="hljs-attr">title</span>=<span class="hljs-string">"提示"</span>
      <span class="hljs-attr">:visible.sync</span>=<span class="hljs-string">"dialogVisible"</span>
      <span class="hljs-attr">width</span>=<span class="hljs-string">"600px"</span>
      <span class="hljs-attr">:before-close</span>=<span class="hljs-string">"handleClose"</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:model</span>=<span class="hljs-string">"editForm"</span> <span class="hljs-attr">:rules</span>=<span class="hljs-string">"editFormRules"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"editForm"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"用户名"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"username"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.username"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-alert</span>
            <span class="hljs-attr">title</span>=<span class="hljs-string">"初始密码为888888"</span>
            <span class="hljs-attr">:closable</span>=<span class="hljs-string">"false"</span>
            <span class="hljs-attr">type</span>=<span class="hljs-string">"info"</span>
            <span class="hljs-attr">style</span>=<span class="hljs-string">"line-height: 12px;"</span>
          ></span><span class="hljs-tag"></<span class="hljs-name">el-alert</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"邮箱"</span>  <span class="hljs-attr">prop</span>=<span class="hljs-string">"email"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.email"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"手机号"</span>  <span class="hljs-attr">prop</span>=<span class="hljs-string">"phone"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.phone"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"状态"</span>  <span class="hljs-attr">prop</span>=<span class="hljs-string">"statu"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-radio-group</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"editForm.statu"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">"0"</span>></span>禁用<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-radio</span> <span class="hljs-attr">:label</span>=<span class="hljs-string">"1"</span>></span>正常<span class="hljs-tag"></<span class="hljs-name">el-radio</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-radio-group</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>

      <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"footer"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dialog-footer"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"resetForm('editForm')"</span>></span>取 消<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitForm('editForm')"</span>></span>确 定<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span>

    <span class="hljs-comment"><!-- 分配权限对话框 --></span>
    <span class="hljs-tag"><<span class="hljs-name">el-dialog</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"分配角色"</span> <span class="hljs-attr">:visible.sync</span>=<span class="hljs-string">"roleDialogFormVisible"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"600px"</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:model</span>=<span class="hljs-string">"roleForm"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-tree</span>
          <span class="hljs-attr">:data</span>=<span class="hljs-string">"roleTreeData"</span>
          <span class="hljs-attr">show-checkbox</span>
          <span class="hljs-attr">ref</span>=<span class="hljs-string">"roleTree"</span>
          <span class="hljs-attr">:check-strictly</span>=<span class="hljs-string">checkStrictly</span>
          <span class="hljs-attr">node-key</span>=<span class="hljs-string">"id"</span>
          <span class="hljs-attr">:default-expand-all</span>=<span class="hljs-string">true</span>
          <span class="hljs-attr">:props</span>=<span class="hljs-string">"defaultProps"</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-tree</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"footer"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dialog-footer"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"roleDialogFormVisible=false"</span>></span>取 消<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitRoleHandle('roleForm')"</span>></span>确 定<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'SysUser'</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">searchForm</span>: &#123;&#125;,
      <span class="hljs-attr">delBtlStatu</span>: <span class="hljs-literal">true</span>,

      <span class="hljs-attr">total</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">size</span>: <span class="hljs-number">10</span>,
      <span class="hljs-attr">current</span>: <span class="hljs-number">1</span>,

      <span class="hljs-attr">dialogVisible</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">editForm</span>: &#123;

      &#125;,

      <span class="hljs-attr">tableData</span>: [],

      <span class="hljs-attr">editFormRules</span>: &#123;
        <span class="hljs-attr">username</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入用户名称'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">email</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入邮箱'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">statu</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请选择状态'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ]
      &#125;,

      <span class="hljs-attr">multipleSelection</span>: [],

      <span class="hljs-attr">roleDialogFormVisible</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">defaultProps</span>: &#123;
        <span class="hljs-attr">children</span>: <span class="hljs-string">'children'</span>,
        <span class="hljs-attr">label</span>: <span class="hljs-string">'name'</span>
      &#125;,
      <span class="hljs-attr">roleForm</span>: &#123;&#125;,
      <span class="hljs-attr">roleTreeData</span>: [],
      <span class="hljs-attr">treeCheckedKeys</span>: [],
      <span class="hljs-attr">checkStrictly</span>: <span class="hljs-literal">true</span>

    &#125;
  &#125;,
  created () &#123;
    <span class="hljs-built_in">this</span>.getUserList()

    <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/sys/role/list'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.roleTreeData = res.data.data.records
    &#125;)
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    toggleSelection (rows) &#123;
      <span class="hljs-keyword">if</span> (rows) &#123;
        rows.forEach(<span class="hljs-function"><span class="hljs-params">row</span> =></span> &#123;
          <span class="hljs-built_in">this</span>.$refs.multipleTable.toggleRowSelection(row)
        &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>.$refs.multipleTable.clearSelection()
      &#125;
    &#125;,
    handleSelectionChange (val) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'勾选'</span>)
      <span class="hljs-built_in">console</span>.log(val)
      <span class="hljs-built_in">this</span>.multipleSelection = val

      <span class="hljs-built_in">this</span>.delBtlStatu = val.length === <span class="hljs-number">0</span>
    &#125;,

    handleSizeChange (val) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`每页 <span class="hljs-subst">$&#123;val&#125;</span> 条`</span>)
      <span class="hljs-built_in">this</span>.size = val
      <span class="hljs-built_in">this</span>.getUserList()
    &#125;,
    handleCurrentChange (val) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`当前页: <span class="hljs-subst">$&#123;val&#125;</span>`</span>)
      <span class="hljs-built_in">this</span>.current = val
      <span class="hljs-built_in">this</span>.getUserList()
    &#125;,

    resetForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].resetFields()
      <span class="hljs-built_in">this</span>.dialogVisible = <span class="hljs-literal">false</span>
      <span class="hljs-built_in">this</span>.editForm = &#123;&#125;
    &#125;,
    handleClose () &#123;
      <span class="hljs-built_in">this</span>.resetForm(<span class="hljs-string">'editForm'</span>)
    &#125;,

    getUserList () &#123;
      <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/sys/user/list'</span>, &#123;
        <span class="hljs-attr">params</span>: &#123;
          <span class="hljs-attr">username</span>: <span class="hljs-built_in">this</span>.searchForm.username,
          <span class="hljs-attr">current</span>: <span class="hljs-built_in">this</span>.current,
          <span class="hljs-attr">size</span>: <span class="hljs-built_in">this</span>.size
        &#125;
      &#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.tableData = res.data.data.records
        <span class="hljs-built_in">this</span>.size = res.data.data.size
        <span class="hljs-built_in">this</span>.current = res.data.data.current
        <span class="hljs-built_in">this</span>.total = res.data.data.total
      &#125;)
    &#125;,

    submitForm (formName) &#123;
      <span class="hljs-built_in">this</span>.$refs[formName].validate(<span class="hljs-function">(<span class="hljs-params">valid</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (valid) &#123;
          <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/sys/user/'</span> + (<span class="hljs-built_in">this</span>.editForm.id ? <span class="hljs-string">'update'</span> : <span class="hljs-string">'save'</span>), <span class="hljs-built_in">this</span>.editForm)
            .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
              <span class="hljs-built_in">this</span>.$message(&#123;
                <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">message</span>: <span class="hljs-string">'恭喜你，操作成功'</span>,
                <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
                <span class="hljs-attr">onClose</span>: <span class="hljs-function">() =></span> &#123;
                  <span class="hljs-built_in">this</span>.getUserList()
                &#125;
              &#125;)

              <span class="hljs-built_in">this</span>.dialogVisible = <span class="hljs-literal">false</span>
            &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error submit!!'</span>)
          <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125;
      &#125;)
    &#125;,
    editHandle (id) &#123;
      <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/sys/user/info/'</span> + id).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.editForm = res.data.data

        <span class="hljs-built_in">this</span>.dialogVisible = <span class="hljs-literal">true</span>
      &#125;)
    &#125;,
    delHandle (id) &#123;
      <span class="hljs-keyword">var</span> ids = []

      <span class="hljs-keyword">if</span> (id) &#123;
        ids.push(id)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>.multipleSelection.forEach(<span class="hljs-function"><span class="hljs-params">row</span> =></span> &#123;
          ids.push(row.id)
        &#125;)
      &#125;

      <span class="hljs-built_in">console</span>.log(ids)

      <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/sys/user/delete'</span>, ids).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.$message(&#123;
          <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">message</span>: <span class="hljs-string">'恭喜你，操作成功'</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
          <span class="hljs-attr">onClose</span>: <span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">this</span>.getUserList()
          &#125;
        &#125;)
      &#125;)
    &#125;,

    roleHandle (id) &#123;
      <span class="hljs-built_in">this</span>.roleDialogFormVisible = <span class="hljs-literal">true</span>

      <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'/sys/user/info/'</span> + id).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.roleForm = res.data.data

        <span class="hljs-keyword">const</span> roleIds = []
        res.data.data.sysRoles.forEach(<span class="hljs-function"><span class="hljs-params">row</span> =></span> &#123;
          roleIds.push(row.id)
        &#125;)

        <span class="hljs-built_in">this</span>.$refs.roleTree.setCheckedKeys(roleIds)
      &#125;)
    &#125;,
    submitRoleHandle (formName) &#123;
      <span class="hljs-keyword">var</span> roleIds = <span class="hljs-built_in">this</span>.$refs.roleTree.getCheckedKeys()

      <span class="hljs-built_in">console</span>.log(roleIds)

      <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/sys/user/role/'</span> + <span class="hljs-built_in">this</span>.roleForm.id, roleIds).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">this</span>.$message(&#123;
          <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">message</span>: <span class="hljs-string">'恭喜你，操作成功'</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
          <span class="hljs-attr">onClose</span>: <span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">this</span>.getUserList()
          &#125;
        &#125;)

        <span class="hljs-built_in">this</span>.roleDialogFormVisible = <span class="hljs-literal">false</span>
      &#125;)
    &#125;,
    repassHandle (id, username) &#123;
      <span class="hljs-built_in">this</span>.$confirm(<span class="hljs-string">'将重置用户【'</span> + username + <span class="hljs-string">'】的密码, 是否继续?'</span>, <span class="hljs-string">'提示'</span>, &#123;
        <span class="hljs-attr">confirmButtonText</span>: <span class="hljs-string">'确定'</span>,
        <span class="hljs-attr">cancelButtonText</span>: <span class="hljs-string">'取消'</span>,
        <span class="hljs-attr">type</span>: <span class="hljs-string">'warning'</span>
      &#125;).then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.$axios.post(<span class="hljs-string">'/sys/user/repass'</span>, id).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
          <span class="hljs-built_in">this</span>.$message(&#123;
            <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">message</span>: <span class="hljs-string">'恭喜你，操作成功'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
            <span class="hljs-attr">onClose</span>: <span class="hljs-function">() =></span> &#123;
            &#125;
          &#125;)
        &#125;)
      &#125;)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">

<span class="hljs-selector-class">.el-pagination</span> &#123;
  <span class="hljs-attribute">float</span>: right;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">22px</span>;
&#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">按钮权限控制</h3>
<p>上面的菜单，角色，用户有的操作，不是每个用户都有的，没有权限的用户我们应该隐藏按钮。
我们再src下面新建一个js文件用于定义一个全局使用的方法：、
src/globalFun.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

Vue.mixin(&#123;
  <span class="hljs-attr">methods</span>: &#123;
    hasAuth (perm) &#123;
      <span class="hljs-keyword">var</span> authority = <span class="hljs-built_in">this</span>.$store.state.menus.permList

      <span class="hljs-keyword">return</span> authority.indexOf(perm) > -<span class="hljs-number">1</span>
    &#125;
  &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在架子啊菜单的时候 要同时架子啊权限数据，现在需要用到权限数据 这里数组，因此我们通过按钮的权限是否在权限列表内就可以了。mixin 的作用是多个组件可以共享数据和方法，在使用mixin 的组件中引入后，mixin 中的方法和属性也就并入到该组件中，可以直接使用，在已有的组件数据和方法进行扩充。在main.js 引入这个文件
src\main.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> gobal <span class="hljs-keyword">from</span> <span class="hljs-string">"./globalFun"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样全局就可以使用啦，比如我们在新增按钮这里做判断：
src/views/sys/Menu.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><el-button type=<span class="hljs-string">"primary"</span> @click=<span class="hljs-string">"dialogFormVisible = true"</span> v-<span class="hljs-keyword">if</span>=<span class="hljs-string">"hasAuth('sys:menu:save')"</span>>新增</el-button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过v-if来判断返回是否为true从而判断是否显示。
<strong>效果</strong>
当登录的是 test 的时候没有新增的按钮
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a962952c8d4408f9417c50ad3c960da~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
admin 的时候是有的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/853206b1c20e45e9b36fc7951c03c886~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            