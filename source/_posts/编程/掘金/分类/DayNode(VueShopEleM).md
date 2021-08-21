
---
title: 'DayNode(VueShopEleM)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45d815137d6a4af3a89f0b107a423461~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 02:21:17 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45d815137d6a4af3a89f0b107a423461~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前期配置-后端</h1>
<h2 data-id="heading-1">vue脚手架</h2>
<h3 data-id="heading-2">基于ui界面创建Vue项目</h3>
<p>终端输入：</p>
<pre><code class="hljs language-js copyable" lang="js">vue ui
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">Vue脚手架的自定义配置</h3>
<pre><code class="hljs language-js copyable" lang="js">A.通过 package.json 进行配置 [不推荐使用]
    <span class="hljs-string">"vue"</span>:&#123;
        <span class="hljs-string">"devServer"</span>:&#123;
            <span class="hljs-string">"port"</span>:<span class="hljs-string">"9990"</span>,
            <span class="hljs-string">"open"</span>:<span class="hljs-literal">true</span>
        &#125;
    &#125;
B.通过单独的配置文件进行配置，创建vue.config.js
    <span class="hljs-built_in">module</span>.exports = &#123;
        <span class="hljs-attr">devServer</span>:&#123;
            <span class="hljs-attr">port</span>:<span class="hljs-number">8888</span>,
            <span class="hljs-attr">open</span>:<span class="hljs-literal">true</span>
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">Element-UI</h2>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Felement-cn.eleme.io%2F%23%2Fzh-CN" target="_blank" rel="nofollow noopener noreferrer" title="http://element-cn.eleme.io/#/zh-CN" ref="nofollow noopener noreferrer">官网</a></p>
<pre><code class="hljs language-js copyable" lang="js">A.安装： --终端
npm install element-ui -S 

B.导入使用： --main.js
<span class="hljs-keyword">import</span> ElementUI <span class="hljs-keyword">from</span> <span class="hljs-string">"element-ui"</span>; 
<span class="hljs-keyword">import</span> <span class="hljs-string">"element-ui/lib/theme-chalk/index.css"</span>;

<span class="hljs-comment">// 全局注册</span>
Vue.use(ElementUI)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">后台配置</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45d815137d6a4af3a89f0b107a423461~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-11 下午4.44.52.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">配置mysql文件</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68626416c7224e7da7676085b249b889~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-11 下午4.21.39.png" loading="lazy" referrerpolicy="no-referrer">
代码运行完后，点左侧右上角 刷新 按钮</p>
<h3 data-id="heading-7">启动后台 app.js</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2311a83062aa46ae9adb07631b4ab572~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-11 下午4.37.01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4850a03a05c4bddb976c46322fe8f34~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-11 下午4.40.57.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">postman测试数据</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40991ea54a7e427393caa6822d52ca0f~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-11 下午4.45.44.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">项目配置-前端</h1>
<h2 data-id="heading-10">登录token</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ddd7497c0e54615b92a2eaeb8d7e04f~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-11 下午6.38.15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">登录状态</h3>
<p>如果服务器和客户端同源，建议可以使用cookie或者session来保持登录状态</p>
<p>如果客户端和服务器跨域了，建议使用token进行维持登录状态。</p>
<h2 data-id="heading-12">路由router</h2>
<ol>
<li>下载插件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">yarn add vue-router
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>新建<code>scr/router/index.js</code> 文件，配置路由并导出</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-comment">// 导入组件</span>
<span class="hljs-keyword">import</span> Login <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/Login.vue'</span>
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/Home.vue'</span>
<span class="hljs-keyword">import</span> Welcome <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/Welcome.vue'</span>
<span class="hljs-keyword">import</span> Users <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/user/Users.vue'</span>
<span class="hljs-keyword">import</span> Rights <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/right/Rights.vue'</span>
<span class="hljs-keyword">import</span> Roles <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/right/Roles.vue'</span>

<span class="hljs-comment">// 全局 注册路由组件</span>
Vue.use(VueRouter)

<span class="hljs-comment">//  创建路由规则</span>
<span class="hljs-keyword">const</span> routes = [&#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/login'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
        <span class="hljs-attr">component</span>: Login
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
        <span class="hljs-attr">component</span>: Home,
        <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/welcome'</span>,
        <span class="hljs-attr">children</span>: [&#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">'/welcome'</span>, <span class="hljs-comment">//根路径</span>
                <span class="hljs-attr">component</span>: Welcome
            &#125;,
            &#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">'/users'</span>,
                <span class="hljs-attr">component</span>: Users
            &#125;,
            &#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">'/rights'</span>,
                <span class="hljs-attr">component</span>: Rights
            &#125;,
            &#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">'/roles'</span>,
                <span class="hljs-attr">component</span>: Roles
            &#125;
        ]
    &#125;
]
<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
    routes
&#125;)

<span class="hljs-comment">//挂载路由导航守卫,to表示将要访问的路径，from表示从哪里来，next是下一个要做的操作</span>
router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (to.path == <span class="hljs-string">'/login'</span>) <span class="hljs-keyword">return</span> next()

    <span class="hljs-comment">// 获取token</span>
    <span class="hljs-keyword">const</span> tokenStr = sessionStorage.getItem(<span class="hljs-string">'token'</span>)

    <span class="hljs-comment">// 如果没有token</span>
    <span class="hljs-keyword">if</span> (!tokenStr) <span class="hljs-keyword">return</span> next(<span class="hljs-string">'/login'</span>)

    next()
&#125;)

<span class="hljs-comment">// 创建 并导出 路由管理器对象</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在<code>main.js</code>中引入并挂在路由</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>

<span class="hljs-comment">// 导入路由管理器</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'@/router'</span>

<span class="hljs-keyword">new</span> Vue(&#123;
    router, <span class="hljs-comment">// 注册路由</span>
    <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">api接口配置</h2>
<ol>
<li>下载<code>axios</code>插件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">yarn add axios
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>新建<code>src/utils/request.js</code>文件，进行请求基本配置</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 导入axios</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-comment">// 设置请求的根路径</span>
axios.defaults.baseURL = <span class="hljs-string">'http://127.0.0.1:8888/api/private/v1/'</span>

<span class="hljs-comment">//请求在到达服务器之前，先会调用use中的这个回调函数来添加请求头信息</span>
axios.interceptors.request.use(<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    <span class="hljs-comment">//为请求头对象，添加token验证的Authorization字段</span>
    config.headers.Authorization = <span class="hljs-built_in">window</span>.sessionStorage.getItem(<span class="hljs-string">'token'</span>)
    <span class="hljs-keyword">return</span> config
&#125;)

<span class="hljs-comment">// 导出</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> axios
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>新建<code>src/api/Login.js</code>，配置登录相关的api请求，并导出</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 提供登录 注册 相关的api方法</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/request.js'</span>

<span class="hljs-comment">// 导出login请求</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> login = <span class="hljs-function"><span class="hljs-params">data</span> =></span>
    axios(&#123;
        <span class="hljs-attr">url</span>: <span class="hljs-string">'login'</span>,
        <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
        data
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>新建<code>src/api/index.js</code>，汇总所有请求</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; login &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api/Login.js'</span>
<span class="hljs-keyword">import</span> &#123; getMenus &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api/Home.js'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> loginAPI = login
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getMenusAPI = getMenus
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>在 <code>src/components/Login.vue</code>组件中 按需导入组件并使用api</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-comment">// 按需导入 api中的方法</span>
<span class="hljs-keyword">import</span> &#123; loginAPI &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">Element UI</h1>
<h2 data-id="heading-15">按需引入</h2>
<ol>
<li>下载插件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">npm i element-ui -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.新建 <code>src/plugs/element.js</code> 文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-comment">// 按需导入  组件</span>
<span class="hljs-keyword">import</span> &#123; Button, Form, FormItem, Input, Message &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>

Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)

<span class="hljs-comment">// 进行全局挂载：</span>
Vue.prototype.$message = Message
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在<code>main.js</code>中引入 样式</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>

<span class="hljs-comment">// 引入elementUI组件和样式文件</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'element-ui/lib/theme-chalk/index.css'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'@/plugs/element.js'</span>

<span class="hljs-comment">// 引入其他样式</span>
<span class="hljs-comment">// 引入全局样式</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'@/assets/css/global.css'</span>
<span class="hljs-comment">// 引入字体样式</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'@/assets/fonts/iconfont.css'</span>
<span class="hljs-comment">// 导入 第三方插件vue-table-with-tree-grid 展示插件</span>
<span class="hljs-keyword">import</span> TreeTable <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-table-with-tree-grid'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">Container 布局容器</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5f50ced8afa46dfa21661ce99c006f3~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-20 上午11.14.40.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>后台api请求数据</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-string">"data"</span>:
        &#123;
            <span class="hljs-string">"id"</span>: <span class="hljs-number">101</span>,
            <span class="hljs-string">"authName"</span>: <span class="hljs-string">"商品管理"</span>,
            <span class="hljs-string">"path"</span>: <span class="hljs-literal">null</span>,
            <span class="hljs-string">"children"</span>: [
                &#123;
                    <span class="hljs-string">"id"</span>: <span class="hljs-number">104</span>,
                    <span class="hljs-string">"authName"</span>: <span class="hljs-string">"商品列表"</span>,
                    <span class="hljs-string">"path"</span>: <span class="hljs-literal">null</span>,
                    <span class="hljs-string">"children"</span>: []
                &#125;
            ]
        &#125;
    <span class="hljs-string">"meta"</span>: &#123;
        <span class="hljs-string">"msg"</span>: <span class="hljs-string">"获取菜单列表成功"</span>,
        <span class="hljs-string">"status"</span>: <span class="hljs-number">200</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>Home.vue</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-container</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"home-container"</span>></span>
      <span class="hljs-comment"><!-- 头部区域 --></span>
      <span class="hljs-tag"><<span class="hljs-name">el-header</span>></span>
        <span class="hljs-comment"><!-- 左侧logo --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"logo"</span>></span>J.<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">span</span>></span>Jeanhome<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-comment"><!-- 右侧 退出登录button --></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"info"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"logout"</span> <span class="hljs-attr">plain</span> <span class="hljs-attr">round</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span>></span>退出<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-header</span>></span>
      <span class="hljs-comment"><!-- 页面主体区域 --></span>
      <span class="hljs-tag"><<span class="hljs-name">el-container</span>></span>
        <span class="hljs-comment"><!-- 侧边栏 ------------------------------------------------------- --></span>
        <span class="hljs-tag"><<span class="hljs-name">el-aside</span> <span class="hljs-attr">:width</span>=<span class="hljs-string">"isCollapse?'64px':'200px'"</span>></span>
          <span class="hljs-comment"><!-- 伸缩侧边栏按钮 --></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"toggle-button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"isCollapse=!isCollapse"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"isCollapse?'el-icon-moon-night':'el-icon-cloudy-and-sunny'"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-comment"><!-- 侧边栏菜单 --></span>
          <span class="hljs-tag"><<span class="hljs-name">el-menu</span>
            <span class="hljs-attr">background-color</span>=<span class="hljs-string">"#fafafa"</span>
            <span class="hljs-attr">text-color</span>=<span class="hljs-string">"#B4B4B4"</span>
            <span class="hljs-attr">active-text-color</span>=<span class="hljs-string">"#f7d182"</span>
            <span class="hljs-attr">unique-opened</span>
            <span class="hljs-attr">:collapse</span>=<span class="hljs-string">"isCollapse"</span>
            <span class="hljs-attr">:collapse-transition</span>=<span class="hljs-string">"false"</span>
            <span class="hljs-attr">:router</span>=<span class="hljs-string">"true"</span>
            <span class="hljs-attr">:default-active</span>=<span class="hljs-string">"this.activePath"</span>
          ></span>
            <span class="hljs-comment"><!-- 一级菜单 --></span>
            <span class="hljs-comment"><!-- 注意：绑定的index必须是 字符串 --></span>
            <span class="hljs-tag"><<span class="hljs-name">el-submenu</span>
              <span class="hljs-attr">:index</span>=<span class="hljs-string">"item.id.toString()"</span>
              <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.id"</span>
              <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in menuList"</span>
              <span class="hljs-attr">class</span>=<span class="hljs-string">"first-item"</span>
              <span class="hljs-attr">active-background-color</span>=<span class="hljs-string">"#fff"</span>
            ></span>
              <span class="hljs-comment"><!-- 一级菜单模板 --></span>
              <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span>
                <span class="hljs-comment"><!-- 图标 --></span>
                <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"item.iconclass"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
                <span class="hljs-comment"><!-- 文本 --></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;item.authName&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
              <span class="hljs-comment"><!-- 二级子菜单 --></span>
              <span class="hljs-tag"><<span class="hljs-name">el-menu-item</span>
                <span class="hljs-attr">:index</span>=<span class="hljs-string">"'/'+subItem.path"</span>
                <span class="hljs-attr">:key</span>=<span class="hljs-string">"subItem.id"</span>
                <span class="hljs-attr">v-for</span>=<span class="hljs-string">"subItem in item.children"</span>
                @<span class="hljs-attr">click</span>=<span class="hljs-string">"changePath('/'+subItem.path)"</span>
              ></span>
                <span class="hljs-comment"><!-- 二级菜单模板 --></span>
                <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span>
                  <span class="hljs-comment"><!-- 图标 --></span>
                  <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-set-up"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
                  <span class="hljs-comment"><!-- 文本 --></span>
                  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;subItem.authName&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">el-menu-item</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">el-submenu</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-menu</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-aside</span>></span>
        <span class="hljs-comment"><!-- 主体结构 --></span>
        <span class="hljs-tag"><<span class="hljs-name">el-main</span>></span>
          <span class="hljs-comment"><!-- 路由占位符 --></span>
          <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-main</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-container</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-container</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; getMenusAPI &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 左侧菜单数据</span>
      <span class="hljs-attr">menuList</span>: [],
      <span class="hljs-attr">isCollapse</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否合并左侧菜单栏，false-展开，true-合并</span>
      <span class="hljs-attr">activePath</span>: <span class="hljs-literal">null</span> <span class="hljs-comment">// 当前激活菜单的path</span>
    &#125;
  &#125;,
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 获取 菜单列表的数据</span>
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: res &#125; = <span class="hljs-keyword">await</span> getMenusAPI()
    <span class="hljs-keyword">if</span> (res.meta.status !== <span class="hljs-number">200</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$message.error(res.meta.msg)

    <span class="hljs-built_in">this</span>.menuList = res.data

    <span class="hljs-comment">// 读取本地缓存的菜单path</span>
    <span class="hljs-built_in">this</span>.activePath = <span class="hljs-built_in">window</span>.sessionStorage.getItem(<span class="hljs-string">'activePath'</span>)
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">// 点击退出 button</span>
    <span class="hljs-function"><span class="hljs-title">logout</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">window</span>.sessionStorage.clear()
      <span class="hljs-built_in">this</span>.$router.push(<span class="hljs-string">'/login'</span>)
    &#125;,
    <span class="hljs-comment">// 点击菜单，切换并保存 当前点击菜单 的index（path）</span>
    <span class="hljs-function"><span class="hljs-title">changePath</span>(<span class="hljs-params">path</span>)</span> &#123;
      <span class="hljs-built_in">window</span>.sessionStorage.setItem(<span class="hljs-string">'activePath'</span>, path)
      <span class="hljs-built_in">this</span>.activePath = path <span class="hljs-comment">// 让当前菜单栏高亮</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">'less'</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">Dialog+Form 表单</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb87114a453042bb9d7fd4c06f792338~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-20 上午10.32.37.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 新增对话框------------------------------------------------ --></span>
    <span class="hljs-tag"><<span class="hljs-name">el-dialog</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"添加新用户"</span> <span class="hljs-attr">:visible.sync</span>=<span class="hljs-string">"isShowAdd"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"50%"</span> <span class="hljs-attr">:before-close</span>=<span class="hljs-string">"handleClose"</span> @<span class="hljs-attr">close</span>=<span class="hljs-string">"addDialogClosed"</span>></span>
      <span class="hljs-comment"><!-- 对话框主体区域 --></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:model</span>=<span class="hljs-string">"addForm"</span> <span class="hljs-attr">:rules</span>=<span class="hljs-string">"addFormRules"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"addFormRef"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"70px"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"用户名"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"username"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"addForm.username"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"密码"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"password"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"addForm.password"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"邮箱"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"email"</span> <span class="hljs-attr">required</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"addForm.email"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"电话"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"mobile"</span> <span class="hljs-attr">required</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"addForm.mobile"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>
      <span class="hljs-comment"><!-- 对话框底部--------- --></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"footer"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dialog-footer"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"isShowAdd= false"</span>></span>取 消<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"addUser"</span>></span>确 定<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; addUserAPI &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">//验证邮箱的规则</span>
    <span class="hljs-keyword">var</span> checkEmail = <span class="hljs-function">(<span class="hljs-params">rule, value, cb</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (value.trim().length == <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> cb(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请输入邮箱'</span>))
      <span class="hljs-keyword">const</span> regEmail = <span class="hljs-regexp">/^\w+@\w+(\.\w+)+$/</span>
      <span class="hljs-keyword">if</span> (regEmail.test(value)) &#123;
        <span class="hljs-keyword">return</span> cb()
      &#125;
      <span class="hljs-comment">//返回一个错误提示</span>
      cb(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请输入合法的邮箱'</span>))
    &#125;
    <span class="hljs-comment">//验证手机号码的规则</span>
    <span class="hljs-keyword">var</span> checkMobile = <span class="hljs-function">(<span class="hljs-params">rule, value, cb</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (!value) <span class="hljs-keyword">return</span> cb(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请输入手机号'</span>))

      <span class="hljs-keyword">const</span> regMobile = <span class="hljs-regexp">/^1[34578]\d&#123;9&#125;$/</span>
      <span class="hljs-keyword">if</span> (regMobile.test(value)) &#123;
        <span class="hljs-keyword">return</span> cb()
      &#125;
      <span class="hljs-comment">//返回一个错误提示</span>
      cb(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请输入合法的手机号码'</span>))
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">isShowAdd</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 是否显示 添加用户 对话框</span>
      <span class="hljs-comment">// 添加用户的表单数据</span>
      <span class="hljs-attr">addForm</span>: &#123;
        <span class="hljs-attr">username</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">password</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">email</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">mobile</span>: <span class="hljs-string">''</span>
      &#125;,
      <span class="hljs-comment">// 添加表单的验证规则对象</span>
      <span class="hljs-attr">addFormRules</span>: &#123;
        <span class="hljs-attr">username</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入用户名称'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;,
          &#123;
            <span class="hljs-attr">min</span>: <span class="hljs-number">3</span>,
            <span class="hljs-attr">max</span>: <span class="hljs-number">10</span>,
            <span class="hljs-attr">message</span>: <span class="hljs-string">'用户名在3~10个字符之间'</span>,
            <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span>
          &#125;
        ],
        <span class="hljs-attr">password</span>: [
          &#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入密码'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;,
          &#123;
            <span class="hljs-attr">min</span>: <span class="hljs-number">6</span>,
            <span class="hljs-attr">max</span>: <span class="hljs-number">15</span>,
            <span class="hljs-attr">message</span>: <span class="hljs-string">'用户名在6~15个字符之间'</span>,
            <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span>
          &#125;
        ],
        <span class="hljs-attr">email</span>: [
          <span class="hljs-comment">//   &#123; required: true, message: '请输入邮箱', trigger: 'blur' &#125;,</span>
          &#123; <span class="hljs-attr">validator</span>: checkEmail, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ],
        <span class="hljs-attr">mobile</span>: [
          <span class="hljs-comment">//   &#123; required: true, message: '请输入手机号码', trigger: 'blur' &#125;,</span>
          &#123; <span class="hljs-attr">validator</span>: checkMobile, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;
        ]
      &#125;
    &#125;
  &#125;,

  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">handleSizeChange</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-comment">//以最新的pagesize来请求数据并展示数据</span>
      <span class="hljs-built_in">this</span>.queryInfo.pagesize = val
      <span class="hljs-built_in">this</span>.getUserList()
    &#125;,
    <span class="hljs-function"><span class="hljs-title">handleCurrentChange</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-comment">//以最新的val页码来请求数据并展示数据</span>
      <span class="hljs-built_in">this</span>.queryInfo.pagenum = val
      <span class="hljs-built_in">this</span>.getUserList()
    &#125;,

    <span class="hljs-comment">// 添加用户</span>
    <span class="hljs-function"><span class="hljs-title">addUser</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 点击 确定按钮时，调用validate进行表单验证</span>
      <span class="hljs-built_in">this</span>.$refs.addFormRef.validate(<span class="hljs-keyword">async</span> valid => &#123;
        <span class="hljs-keyword">if</span> (!valid) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">'请填写完整用户信息'</span>)

        <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: res &#125; = <span class="hljs-keyword">await</span> addUserAPI(<span class="hljs-built_in">this</span>.addForm)

        <span class="hljs-comment">//判断如果添加失败，就做提示</span>
        <span class="hljs-keyword">if</span> (res.meta.status !== <span class="hljs-number">201</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">'添加用户失败'</span>)
        <span class="hljs-comment">//添加成功的提示</span>
        <span class="hljs-built_in">this</span>.$message.success(<span class="hljs-string">'添加用户成功'</span>)
        <span class="hljs-comment">//关闭对话框</span>
        <span class="hljs-built_in">this</span>.isShowAdd = <span class="hljs-literal">false</span>
      &#125;)
    &#125;,
    <span class="hljs-comment">//对话框关闭之后，重置表单</span>
    <span class="hljs-function"><span class="hljs-title">addDialogClosed</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$refs.addFormRef.resetFields()
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">'less'</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">Table+Tree</h2>
<p><strong>table</strong>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2c9284bf3df4658b9ec5c67cc4b46c6~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-20 上午10.30.40.png" loading="lazy" referrerpolicy="no-referrer">
<strong>tree 树形控件</strong>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7857de37231042f5b8668a1a22ec5e31~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-20 上午10.31.10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 卡片容器区域--------------------------------- --></span>
    <span class="hljs-tag"><<span class="hljs-name">el-card</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box-card"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text item"</span>></span>
        <span class="hljs-comment"><!-- 角色列表区域 -----------------------------------------></span>
        <span class="hljs-tag"><<span class="hljs-name">el-table</span> <span class="hljs-attr">:data</span>=<span class="hljs-string">"roleList"</span> <span class="hljs-attr">border</span>></span>
          <span class="hljs-comment"><!-- !!!添加展开列 -------------------></span>
          <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"expand"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
              <span class="hljs-comment"><!-- 渲染一级权限 --></span>
              <span class="hljs-comment"><!-- 只有第一行 需要加上边框 --></span>
              <span class="hljs-tag"><<span class="hljs-name">el-row</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"['bottomBorder',i1==0?'topBorder':'']"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item1.id"</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item1,i1) in scope.row.children"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">el-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"5"</span>></span>
                  <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">closable</span> @<span class="hljs-attr">close</span>=<span class="hljs-string">"removeRightById(scope.row,item1.id)"</span>></span>&#123;&#123;item1.authName&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
                  <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-caret-right"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">el-col</span>></span>
                <span class="hljs-comment"><!-- 渲染二，三级权限 --></span>
                <span class="hljs-tag"><<span class="hljs-name">el-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"19"</span>></span>
                  <span class="hljs-comment"><!-- 通过for循环嵌套渲染二级权限  --></span>
                  <span class="hljs-comment"><!-- 除了第一行 加上边框 --></span>
                  <span class="hljs-tag"><<span class="hljs-name">el-row</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"[i2!=0?'topBorder':'']"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item2.id"</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item2,i2) in item1.children"</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">el-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"6"</span>></span>
                      <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span> <span class="hljs-attr">closable</span> @<span class="hljs-attr">close</span>=<span class="hljs-string">"removeRightById(scope.row,item2.id)"</span>></span>&#123;&#123;item2.authName&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
                      <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-caret-right"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
                    <span class="hljs-tag"></<span class="hljs-name">el-col</span>></span>
                    <span class="hljs-comment"><!-- 三级权限 --></span>
                    <span class="hljs-tag"><<span class="hljs-name">el-col</span> <span class="hljs-attr">:span</span>=<span class="hljs-string">"18"</span>></span>
                      <span class="hljs-tag"><<span class="hljs-name">el-tag</span>
                        <span class="hljs-attr">closable</span>
                        @<span class="hljs-attr">close</span>=<span class="hljs-string">"removeRightById(scope.row,item3.id)"</span>
                        <span class="hljs-attr">type</span>=<span class="hljs-string">"warning"</span>
                        <span class="hljs-attr">:key</span>=<span class="hljs-string">"item3.id"</span>
                        <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item3 in item2.children"</span>
                      ></span>&#123;&#123;item3.authName&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
                    <span class="hljs-tag"></<span class="hljs-name">el-col</span>></span>
                  <span class="hljs-tag"></<span class="hljs-name">el-row</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">el-col</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">el-row</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"index"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"#"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"角色名称"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"roleName"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"角色描述"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"roleDesc"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"操作"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300px"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-edit"</span>></span>编辑<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-delete"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-setting"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"showSetRightDialog(scope.row)"</span>></span>分配权限<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-card</span>></span>
    <span class="hljs-comment"><!-- 分配权限对话框------------------------------------------ --></span>
    <span class="hljs-tag"><<span class="hljs-name">el-dialog</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"分配权限"</span> @<span class="hljs-attr">close</span>=<span class="hljs-string">"setRightDialogClose"</span> <span class="hljs-attr">:visible.sync</span>=<span class="hljs-string">"isShowSetRight"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"50%"</span>></span>
      <span class="hljs-comment"><!-- 树形组件
    show-checkbox:显示复选框
    node-key:设置选中节点对应的值
    default-expand-all:是否默认展开所有节点
    :default-checked-keys 设置默认选中项的数组
      ref:设置引用--></span>
      <span class="hljs-tag"><<span class="hljs-name">el-tree</span>
        <span class="hljs-attr">:data</span>=<span class="hljs-string">"rightsList"</span>
        <span class="hljs-attr">:default-checked-keys</span>=<span class="hljs-string">"defKeys"</span>
        <span class="hljs-attr">show-checkbox</span>
        <span class="hljs-attr">default-expand-all</span>
        <span class="hljs-attr">node-key</span>=<span class="hljs-string">"id"</span>
        <span class="hljs-attr">ref</span>=<span class="hljs-string">"treeRef"</span>
        <span class="hljs-attr">highlight-current</span>
        <span class="hljs-attr">:props</span>=<span class="hljs-string">"treeProps"</span>
      ></span><span class="hljs-tag"></<span class="hljs-name">el-tree</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"footer"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dialog-footer"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"isShowSetRight = false"</span>></span>取 消<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"changeRoleRights"</span>></span>确 定<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; getRolesAPI, delRoleRightAPI, getRightsTreeAPI, changeRoleRightAPI &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">roleList</span>: [], <span class="hljs-comment">//角色列表数据</span>
      <span class="hljs-attr">isShowSetRight</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 是否显示 分配权限 的弹出框</span>
      <span class="hljs-attr">rightsList</span>: [], <span class="hljs-comment">//权限树 数据</span>
      <span class="hljs-comment">//树形控件的属性绑定对象</span>
      <span class="hljs-attr">treeProps</span>: &#123;
        <span class="hljs-comment">//通过label设置树形节点文本展示authName</span>
        <span class="hljs-attr">label</span>: <span class="hljs-string">'authName'</span>,
        <span class="hljs-comment">//设置通过children属性展示子节点信息</span>
        <span class="hljs-attr">children</span>: <span class="hljs-string">'children'</span>
      &#125;,
      <span class="hljs-attr">defKeys</span>: [], <span class="hljs-comment">//默认勾选的节点的 key 的数组，三级节点的id</span>
      <span class="hljs-attr">roleId</span>: <span class="hljs-literal">null</span> <span class="hljs-comment">// 当前正在编辑的项 的id</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.getRoleList()
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getRoleList</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: res &#125; = <span class="hljs-keyword">await</span> getRolesAPI()
      <span class="hljs-comment">//如果返回状态为异常状态则报错并返回</span>
      <span class="hljs-keyword">if</span> (res.meta.status !== <span class="hljs-number">200</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">'获取角色列表失败'</span>)
      <span class="hljs-comment">// //如果返回状态正常，将请求的数据保存在data中</span>
      <span class="hljs-built_in">this</span>.roleList = res.data
    &#125;,
    <span class="hljs-comment">// 删除权限</span>
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">removeRightById</span>(<span class="hljs-params">role, rightId</span>)</span> &#123;
      <span class="hljs-comment">//弹窗提示用户是否要删除</span>
      <span class="hljs-keyword">const</span> confirmResult = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.$confirm(<span class="hljs-string">'请问是否要删除该权限'</span>, <span class="hljs-string">'删除提示'</span>, &#123;
        <span class="hljs-attr">confirmButtonText</span>: <span class="hljs-string">'确认删除'</span>,
        <span class="hljs-attr">cancelButtonText</span>: <span class="hljs-string">'取消'</span>,
        <span class="hljs-attr">type</span>: <span class="hljs-string">'warning'</span>
      &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> err)
      <span class="hljs-comment">//如果用户点击确认，则confirmResult 为'confirm'</span>
      <span class="hljs-comment">//如果用户点击取消, 则confirmResult获取的就是catch的错误消息'cancel'</span>
      <span class="hljs-keyword">if</span> (confirmResult != <span class="hljs-string">'confirm'</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$message.info(<span class="hljs-string">'已经取消删除'</span>)

      <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: res &#125; = <span class="hljs-keyword">await</span> delRoleRightAPI(role.id, rightId)
      <span class="hljs-keyword">if</span> (res.meta.status !== <span class="hljs-number">200</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">'删除角色权限失败'</span>)

      <span class="hljs-comment">//无需再重新加载所有权限</span>
      <span class="hljs-comment">//只需要对现有的角色权限进行更新即可</span>
      role.children = res.data
    &#125;,
    <span class="hljs-comment">// 点击设置分配权限</span>
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">showSetRightDialog</span>(<span class="hljs-params">role</span>)</span> &#123;
      <span class="hljs-comment">// 弹出 对话框时，就保存当前项的id</span>
      <span class="hljs-built_in">this</span>.roleId = role.id
      <span class="hljs-comment">//获取所有权限的数据</span>
      <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: res &#125; = <span class="hljs-keyword">await</span> getRightsTreeAPI()
      <span class="hljs-comment">//如果返回状态为异常状态则报错并返回</span>
      <span class="hljs-keyword">if</span> (res.meta.status !== <span class="hljs-number">200</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">'获取权限树失败'</span>)
      <span class="hljs-comment">//如果返回状态正常，将请求的数据保存在data中</span>
      <span class="hljs-built_in">this</span>.rightsList = res.data

      <span class="hljs-comment">// role是当前用户的信息，children里面就是权限</span>
      <span class="hljs-comment">//调用getLeafKeys进行递归，将三级权限添加到数组中</span>
      <span class="hljs-built_in">this</span>.getLeafKeys(role, <span class="hljs-built_in">this</span>.defKeys)
      <span class="hljs-comment">// 显示对话框</span>
      <span class="hljs-built_in">this</span>.isShowSetRight = <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-comment">// 通过递归的形式，获取角色下所有三级权限的id，并保存到defKeys中</span>
    <span class="hljs-function"><span class="hljs-title">getLeafKeys</span>(<span class="hljs-params">node, arr</span>)</span> &#123;
      <span class="hljs-comment">// 如果当前节点不包含children属性，则表示node为三级权限</span>
      <span class="hljs-keyword">if</span> (!node.children) <span class="hljs-keyword">return</span> arr.push(node.id)
      <span class="hljs-comment">//递归调用 当前子节点每一个元素</span>
      node.children.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> <span class="hljs-built_in">this</span>.getLeafKeys(item, arr))
    &#125;,
    <span class="hljs-comment">// 当用户关闭树形权限对话框的时候</span>
    <span class="hljs-function"><span class="hljs-title">setRightDialogClose</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 需要清除掉所有选中状态</span>
      <span class="hljs-built_in">this</span>.defKeys = []
    &#125;,
    <span class="hljs-comment">//当用户在树形权限对话框中点击确定，将用户选择的 权限发送请求进行更新</span>
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">changeRoleRights</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">//获取所有选中及半选的 所有id</span>
      <span class="hljs-keyword">const</span> keys = [...this.$refs.treeRef.getCheckedKeys(), ...this.$refs.treeRef.getHalfCheckedKeys()]
      <span class="hljs-comment">//将数组转换为 , 拼接的字符串</span>
      <span class="hljs-keyword">const</span> rids = keys.join(<span class="hljs-string">','</span>)
      <span class="hljs-built_in">console</span>.log(rids)
      <span class="hljs-comment">//发送请求完成更新</span>
      <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: res &#125; = <span class="hljs-keyword">await</span> changeRoleRightAPI(<span class="hljs-built_in">this</span>.roleId, rids)
      <span class="hljs-keyword">if</span> (res.meta.status !== <span class="hljs-number">200</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">'分配权限失败'</span>)
      <span class="hljs-built_in">this</span>.$message.success(<span class="hljs-string">'分配权限成功'</span>)
      <span class="hljs-comment">// 更新整个角色列表</span>
      <span class="hljs-built_in">this</span>.getRoleList()
      <span class="hljs-comment">// 关闭对话框</span>
      <span class="hljs-built_in">this</span>.isShowSetRight = <span class="hljs-literal">false</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">'less'</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">Table+Pagination 分页</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5653d585f0744ff9c3374a73b6e2f68~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-20 上午10.48.16.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 卡片容器 --></span>
    <span class="hljs-tag"><<span class="hljs-name">el-card</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box-card"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text item"</span>></span>
        <span class="hljs-comment"><!-- 数据表格区域-------------------------------------------------- --></span>
        <span class="hljs-comment"><!-- 用户列表(表格)区域 --></span>
        <span class="hljs-tag"><<span class="hljs-name">el-table</span> <span class="hljs-attr">:data</span>=<span class="hljs-string">"userList"</span> <span class="hljs-attr">border</span> <span class="hljs-attr">stripe</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"index"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"姓名"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>&#123;&#123;scope.row.username&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
          <span class="hljs-comment"><!-- <el-table-column label="姓名" prop="username"></el-table-column> --></span>
          <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"邮箱"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"email"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"电话"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"mobile"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"角色"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"role_name"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"状态"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
              <span class="hljs-comment"><!-- scope.row---每条数据,还有 scope.$index--index，scope.column参数 --></span>
              <span class="hljs-tag"><<span class="hljs-name">el-switch</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"scope.row.mg_state"</span> @<span class="hljs-attr">change</span>=<span class="hljs-string">"changeStatus(scope.row)"</span> <span class="hljs-attr">active-color</span>=<span class="hljs-string">"#f7d182"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-switch</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"操作"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"180px"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
              <span class="hljs-comment"><!-- 修改 --></span>
              <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"showEditDialog(scope.row.id)"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-edit"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
              <span class="hljs-comment"><!-- 删除 --></span>
              <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"delUser(scope.row.id)"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-delete"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
              <span class="hljs-comment"><!-- 分配角色 --></span>
              <span class="hljs-tag"><<span class="hljs-name">el-tooltip</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span> <span class="hljs-attr">effect</span>=<span class="hljs-string">"light"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"分配角色"</span> <span class="hljs-attr">placement</span>=<span class="hljs-string">"top"</span> <span class="hljs-attr">:enterable</span>=<span class="hljs-string">"false"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-setting"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"setRole(scope.row)"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">el-tooltip</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>
        <span class="hljs-comment"><!--  分页导航区域 --></span>
        <span class="hljs-tag"><<span class="hljs-name">el-pagination</span>
          @<span class="hljs-attr">size-change</span>=<span class="hljs-string">"handleSizeChange"</span>
          @<span class="hljs-attr">current-change</span>=<span class="hljs-string">"handleCurrentChange"</span>
          <span class="hljs-attr">:current-page</span>=<span class="hljs-string">"queryInfo.pagenum"</span>
          <span class="hljs-attr">:page-sizes</span>=<span class="hljs-string">"[1, 2, 5, 10]"</span>
          <span class="hljs-attr">:page-size</span>=<span class="hljs-string">"queryInfo.pagesize"</span>
          <span class="hljs-attr">layout</span>=<span class="hljs-string">"total, sizes, prev, pager, next, jumper"</span>
          <span class="hljs-attr">:total</span>=<span class="hljs-string">"total"</span>
        ></span><span class="hljs-tag"></<span class="hljs-name">el-pagination</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-card</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; getUsersAPI &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">//获取查询用户信息的参数</span>
      <span class="hljs-attr">queryInfo</span>: &#123;
        <span class="hljs-attr">query</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">pagenum</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 当前页码</span>
        <span class="hljs-attr">pagesize</span>: <span class="hljs-number">1</span> <span class="hljs-comment">// 每页显示行数</span>
      &#125;,
      <span class="hljs-comment">//保存请求回来的用户列表数据</span>
      <span class="hljs-attr">userList</span>: [],
      <span class="hljs-attr">total</span>: <span class="hljs-number">0</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.getUserList()
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">//发送请求获取用户列表数据</span>
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getUserList</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: res &#125; = <span class="hljs-keyword">await</span> getUsersAPI(<span class="hljs-built_in">this</span>.queryInfo)
      <span class="hljs-comment">//如果返回状态为异常状态则报错并返回</span>
      <span class="hljs-keyword">if</span> (res.meta.status != <span class="hljs-number">200</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$message.error(res.meta.msg)
      <span class="hljs-comment">//如果返回状态正常，将请求的数据保存在data中</span>
      <span class="hljs-built_in">this</span>.userList = res.data.users

      <span class="hljs-built_in">this</span>.total = res.data.total
    &#125;,
    <span class="hljs-comment">// 切换 每页的数量</span>
    <span class="hljs-function"><span class="hljs-title">handleSizeChange</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-comment">//以最新的pagesize来请求数据并展示数据</span>
      <span class="hljs-built_in">this</span>.queryInfo.pagesize = val
      <span class="hljs-built_in">this</span>.getUserList()
    &#125;,
    <span class="hljs-comment">// 切换 当前页码</span>
    <span class="hljs-function"><span class="hljs-title">handleCurrentChange</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-comment">//以最新的val页码来请求数据并展示数据</span>
      <span class="hljs-built_in">this</span>.queryInfo.pagenum = val
      <span class="hljs-built_in">this</span>.getUserList()
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">'less'</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">Cascader 级联选择器</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/864b39e8e4a048d79ce494e156690155~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-20 上午11.11.07.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 添加分类对话框 -----------------------------------------------></span>
    <span class="hljs-tag"><<span class="hljs-name">el-dialog</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"添加分类"</span> <span class="hljs-attr">:visible.sync</span>=<span class="hljs-string">"isShowAddCate"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"50%"</span> @<span class="hljs-attr">close</span>=<span class="hljs-string">"addCateDialogClosed"</span>></span>
      <span class="hljs-comment"><!-- 添加分类表单 --></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">:model</span>=<span class="hljs-string">"addCateForm"</span> <span class="hljs-attr">:rules</span>=<span class="hljs-string">"addCateFormRules"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"addCateFormRef"</span> <span class="hljs-attr">label-width</span>=<span class="hljs-string">"100px"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"分类名称"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"cat_name"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"addCateForm.cat_name"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"父级分类"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"cat_pid"</span>></span>
          <span class="hljs-comment"><!-- expandTrigger='hover'(鼠标悬停触发级联) v-model(设置级联菜单绑定数据) 
          :options(指定级联菜单数据源)  :props(用来配置数据显示的规则) 
          clearable(提供“X”号完成删除文本功能) change-on-select(是否可以选中任意一级的菜单)--></span>
          <span class="hljs-tag"><<span class="hljs-name">el-cascader</span>
            <span class="hljs-attr">:options</span>=<span class="hljs-string">"parentCateList"</span>
            <span class="hljs-attr">:props</span>=<span class="hljs-string">"cascaderProps"</span>
            <span class="hljs-attr">v-model</span>=<span class="hljs-string">"selKeys"</span>
            @<span class="hljs-attr">change</span>=<span class="hljs-string">"parentCateChange"</span>
            <span class="hljs-attr">clearable</span>
            <span class="hljs-attr">style</span>=<span class="hljs-string">"width:100%"</span>
          ></span><span class="hljs-tag"></<span class="hljs-name">el-cascader</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"footer"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dialog-footer"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"isShowAddCate = false"</span>></span>取 消<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"addCate"</span>></span>确 定<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; getGoodCatesAPI, addGoodCateAPI &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">isShowAddCate</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 是否显示添加分类对话框</span>
      <span class="hljs-comment">//添加分类的表单数据对象</span>
      <span class="hljs-attr">addCateForm</span>: &#123;
        <span class="hljs-comment">//分类名称</span>
        <span class="hljs-attr">cat_name</span>: <span class="hljs-string">''</span>,
        <span class="hljs-comment">//添加分类的父级id，0则表示父级为0.添加一级分类</span>
        <span class="hljs-attr">cat_pid</span>: <span class="hljs-number">0</span>,
        <span class="hljs-comment">//添加分类的等级，0则表示添加一级分类</span>
        <span class="hljs-attr">cat_level</span>: <span class="hljs-number">0</span>
      &#125;,
      <span class="hljs-comment">//添加分类校验规则</span>
      <span class="hljs-attr">addCateFormRules</span>: &#123;
        <span class="hljs-comment">//验证规则</span>
        <span class="hljs-attr">cat_name</span>: [&#123; <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入分类名称'</span>, <span class="hljs-attr">trigger</span>: <span class="hljs-string">'blur'</span> &#125;]
      &#125;,
      <span class="hljs-attr">parentCateList</span>: [], <span class="hljs-comment">// 有一二级分类的 分类列表数据</span>
      <span class="hljs-attr">selKeys</span>: [], <span class="hljs-comment">// 父级分类下拉框选中的 keys</span>
      <span class="hljs-attr">cascaderProps</span>: &#123;
        <span class="hljs-attr">value</span>: <span class="hljs-string">'cat_id'</span>,
        <span class="hljs-attr">label</span>: <span class="hljs-string">'cat_name'</span>,
        <span class="hljs-attr">children</span>: <span class="hljs-string">'children'</span>,
        <span class="hljs-attr">expandTrigger</span>: <span class="hljs-string">'hover'</span>, <span class="hljs-comment">//鼠标悬停触发级联</span>
        <span class="hljs-attr">checkStrictly</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 是否可以选中任意一级的菜单</span>
      &#125;
    &#125;
  &#125;,

  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">// 点击添加分类按钮</span>
    <span class="hljs-function"><span class="hljs-title">showAddCateDialog</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.isShowAddCate = <span class="hljs-literal">true</span>
      <span class="hljs-built_in">this</span>.getParentCateList()
    &#125;,
    <span class="hljs-comment">//获取父级分类数据列表</span>
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getParentCateList</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: res &#125; = <span class="hljs-keyword">await</span> getGoodCatesAPI(&#123; <span class="hljs-attr">type</span>: <span class="hljs-number">2</span> &#125;)
      <span class="hljs-keyword">if</span> (res.meta.status !== <span class="hljs-number">200</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">'获取商品分类列表数据失败'</span>)
      &#125;
      <span class="hljs-built_in">this</span>.parentCateList = res.data
    &#125;,
    <span class="hljs-comment">//级联菜单中选择项发生变化时触发</span>
    <span class="hljs-function"><span class="hljs-title">parentCateChange</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.selKeys)
      <span class="hljs-comment">// 如果两级都选了，则this.selKeys有两个id，最后一个id即为我们要添加分类 的父级id</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.selKeys.length >= <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">this</span>.addCateForm.cat_pid = <span class="hljs-built_in">this</span>.selKeys[<span class="hljs-built_in">this</span>.selKeys.length - <span class="hljs-number">1</span>]
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 没有选择，则表示要添加0级分类</span>
        <span class="hljs-built_in">this</span>.addCateForm.cat_pid = <span class="hljs-number">0</span>
      &#125;
      <span class="hljs-built_in">this</span>.addCateForm.cat_level = <span class="hljs-built_in">this</span>.selKeys.length
    &#125;,
    <span class="hljs-comment">// 点击 添加分类对话框 的确定按钮</span>
    <span class="hljs-function"><span class="hljs-title">addCate</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$refs.addCateFormRef.validate(<span class="hljs-keyword">async</span> valid => &#123;
        <span class="hljs-keyword">if</span> (!valid) <span class="hljs-keyword">return</span>

        <span class="hljs-comment">// 发送添加分类的请求</span>
        <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">data</span>: res &#125; = <span class="hljs-keyword">await</span> addGoodCateAPI(<span class="hljs-built_in">this</span>.addCateForm)
        <span class="hljs-keyword">if</span> (res.meta.status !== <span class="hljs-number">201</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">'添加分类失败'</span>)
        <span class="hljs-built_in">this</span>.$message.success(<span class="hljs-string">'添加分类成功'</span>)
        <span class="hljs-built_in">this</span>.getCateList()
        <span class="hljs-comment">// 关闭弹出对话框</span>
        <span class="hljs-built_in">this</span>.isShowAddCate = <span class="hljs-literal">false</span>
      &#125;)
    &#125;,
    <span class="hljs-comment">// 关闭 添加分类对话框</span>
    <span class="hljs-function"><span class="hljs-title">addCateDialogClosed</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">//当关闭添加分类对话框时，重置表单</span>
      <span class="hljs-built_in">this</span>.$refs.addCateFormRef.resetFields()
      <span class="hljs-built_in">this</span>.selKeys = []
      <span class="hljs-built_in">this</span>.addCateForm.cat_level = <span class="hljs-number">0</span>
      <span class="hljs-built_in">this</span>.addCateForm.cat_pid = <span class="hljs-number">0</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">Upload 上传</h2>
<h4 data-id="heading-22">完成图片上传</h4>
<blockquote>
<p>因为upload组件进行图片上传的时候并不是使用axios发送请求 所以，我们需要手动为上传图片的请求添加<code>token</code>，即为upload组件添加<code>headers</code>属性</p>
</blockquote>
<pre><code class="copyable">//在页面中添加upload组件，并设置对应的事件和属性
<el-tab-pane label="商品图片" name="3">
  <!-- 商品图片上传
  action:指定图片上传api接口
  :on-preview ： 当点击图片时会触发该事件进行预览操作,处理图片预览
  :on-remove : 当用户点击图片右上角的X号时触发执行
  :on-success：当用户点击上传图片并成功上传时触发
  list-type ：设置预览图片的方式
  :headers ：设置上传图片的请求头 -->
  <el-upload :action="uploadURL" :on-preview="handlePreview" :on-remove="handleRemove" :on-success="handleSuccess" list-type="picture" :headers="headerObj">
    <el-button size="small" type="primary">点击上传</el-button>
  </el-upload>
</el-tab-pane>
//在el-card卡片视图下面添加对话框用来预览图片
<!-- 预览图片对话框 -->
<el-dialog title="图片预览" :visible.sync="previewVisible" width="50%">
  <img :src="previewPath" class="previewImg" />
</el-dialog>

//在data中添加数据
data()&#123;
  return &#123;
    ......
    //添加商品的表单数据对象
    addForm: &#123;
      goods_name: '',
      goods_price: 0,
      goods_weight: 0,
      goods_number: 0,
      goods_cat: [],
      //上传图片数组
      pics: []
    &#125;,
    //上传图片的url地址
    uploadURL: 'http://127.0.0.1:8888/api/private/v1/upload',
    //图片上传组件的headers请求头对象
    headerObj: &#123; Authorization: window.sessionStorage.getItem('token') &#125;,
    //保存预览图片的url地址
    previewPath: '',
    //控制预览图片对话框的显示和隐藏
    previewVisible:false
  &#125;
&#125;,
//在methods中添加事件处理函数
methods:&#123;
  .......
  handlePreview(file) &#123;
    //当用户点击图片进行预览时执行，处理图片预览
    //形参file就是用户预览的那个文件
    this.previewPath = file.response.data.url
    //显示预览图片对话框
    this.previewVisible = true
  &#125;,
  handleRemove(file) &#123;
    //当用户点击X号删除时执行
    //形参file就是用户点击删除的文件
    //获取用户点击删除的那个图片的临时路径
    const filePath = file.response.data.tmp_path
    //使用findIndex来查找符合条件的索引
    const index = this.addForm.pics.findIndex(item => item.pic === filePath)
    //移除索引对应的图片
    this.addForm.pics.splice(index, 1)
  &#125;,
  handleSuccess(response) &#123;
    //当上传成功时触发执行
    //形参response就是上传成功之后服务器返回的结果
    //将服务器返回的临时路径保存到addForm表单的pics数组中
    this.addForm.pics.push(&#123; pic: response.data.tmp_path &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-23">其他插件</h1>
<h2 data-id="heading-24">vue-table-with-tree-grid</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMisterTaki%2Fvue-table-with-tree-grid%23readme" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MisterTaki/vue-table-with-tree-grid#readme" ref="nofollow noopener noreferrer">官网</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/010e1cd4b8884479999f0a6dead2a674~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-20 上午11.05.53.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-25">基本配置</h3>
<ol>
<li>下载插件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">yarn add vue-table-<span class="hljs-keyword">with</span>-tree-grid
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>全局注册 main.js</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//全局注册组件</span>
Vue.component(<span class="hljs-string">'tree-table'</span>, TreeTable)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>vue组件中使用</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 卡片视图区域 --></span>
    <span class="hljs-tag"><<span class="hljs-name">el-card</span>></span>
      <span class="hljs-comment"><!-- 分类表格------------------------------------------------------------  --></span>
      <span class="hljs-comment"><!-- :data(设置数据源) :columns(设置表格中列配置信息) :selection-type(是否有复选框) 
      :expand-type(是否展开数据) show-index(是否设置索引列) index-text(设置索引列头)
      border(是否添加纵向边框) :show-row-hover(是否鼠标悬停高亮)--></span>
      <span class="hljs-tag"><<span class="hljs-name">tree-table</span>
        <span class="hljs-attr">:data</span>=<span class="hljs-string">"cateList"</span>
        <span class="hljs-attr">:columns</span>=<span class="hljs-string">"columns"</span>
        <span class="hljs-attr">:selection-type</span>=<span class="hljs-string">"false"</span>
        <span class="hljs-attr">:expand-type</span>=<span class="hljs-string">"false"</span>
        <span class="hljs-attr">show-index</span>
        <span class="hljs-attr">index-text</span>=<span class="hljs-string">"#"</span>
        <span class="hljs-attr">border</span>
        <span class="hljs-attr">:show-row-hover</span>=<span class="hljs-string">"false"</span>
      ></span>
        <span class="hljs-comment"><!-- 是否有效区域， 设置对应的模板列： slot="isok"(与columns中设置的template一致) --></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> #<span class="hljs-attr">isok</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-success"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"scope.row.cat_deleted === false"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color:lightgreen"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"el-icon-error"</span> <span class="hljs-attr">v-else</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color:red"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
        <span class="hljs-comment"><!-- 排序 --></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"order"</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"scope.row.cat_level===0"</span>></span>一级<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"scope.row.cat_level===1"</span>></span>二级<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"warning"</span> <span class="hljs-attr">v-else</span>></span>三级<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
        <span class="hljs-comment"><!-- 操作 --></span>
        <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"opt"</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"scope"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-edit"</span>></span>编辑<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"danger"</span> <span class="hljs-attr">icon</span>=<span class="hljs-string">"el-icon-delete"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">tree-table</span>></span>

      <span class="hljs-comment"><!-- 分页------------------------------------------------------------ --></span>
      <span class="hljs-tag"><<span class="hljs-name">el-pagination</span>
        @<span class="hljs-attr">size-change</span>=<span class="hljs-string">"handleSizeChange"</span>
        @<span class="hljs-attr">current-change</span>=<span class="hljs-string">"handleCurrentChange"</span>
        <span class="hljs-attr">:current-page</span>=<span class="hljs-string">"queryInfo.pagenum"</span>
        <span class="hljs-attr">:page-sizes</span>=<span class="hljs-string">"[3, 5, 10, 15]"</span>
        <span class="hljs-attr">:page-size</span>=<span class="hljs-string">"queryInfo.pagesize"</span>
        <span class="hljs-attr">layout</span>=<span class="hljs-string">"total, sizes, prev, pager, next, jumper"</span>
        <span class="hljs-attr">:total</span>=<span class="hljs-string">"total"</span>
      ></span><span class="hljs-tag"></<span class="hljs-name">el-pagination</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-card</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; getGoodCatesAPI &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 商品分类数据列表</span>
      <span class="hljs-attr">cateList</span>: [],
      <span class="hljs-comment">//查询分类数据的条件</span>
      <span class="hljs-attr">queryInfo</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-number">3</span>,
        <span class="hljs-attr">pagenum</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">pagesize</span>: <span class="hljs-number">5</span>
      &#125;,
      <span class="hljs-comment">//保存总数据条数</span>
      <span class="hljs-attr">total</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">columns</span>: [
        &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'分类名称'</span>, <span class="hljs-attr">prop</span>: <span class="hljs-string">'cat_name'</span> &#125;,
        <span class="hljs-comment">//type:'template'(将该列设置为模板列)，template:'isok'(设置该列模板的名称为isok)</span>
        &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'是否有效'</span>, <span class="hljs-attr">prop</span>: <span class="hljs-string">''</span>, <span class="hljs-attr">type</span>: <span class="hljs-string">'template'</span>, <span class="hljs-attr">template</span>: <span class="hljs-string">'isok'</span> &#125;,
        &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'排序'</span>, <span class="hljs-attr">prop</span>: <span class="hljs-string">''</span>, <span class="hljs-attr">type</span>: <span class="hljs-string">'template'</span>, <span class="hljs-attr">template</span>: <span class="hljs-string">'order'</span> &#125;,
        &#123; <span class="hljs-attr">label</span>: <span class="hljs-string">'操作'</span>, <span class="hljs-attr">prop</span>: <span class="hljs-string">''</span>, <span class="hljs-attr">type</span>: <span class="hljs-string">'template'</span>, <span class="hljs-attr">template</span>: <span class="hljs-string">'opt'</span> &#125;
      ]
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.getCateList()
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getCateList</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">//获取商品分类数据</span>
      <span class="hljs-keyword">let</span> &#123; <span class="hljs-attr">data</span>: res &#125; = <span class="hljs-keyword">await</span> getGoodCatesAPI(<span class="hljs-built_in">this</span>.queryInfo)
      <span class="hljs-keyword">if</span> (res.meta.status !== <span class="hljs-number">200</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">'获取商品列表数据失败'</span>)
      <span class="hljs-comment">//将数据列表赋值给cateList</span>
      <span class="hljs-built_in">this</span>.cateList = res.data.result
      <span class="hljs-comment">//保存总数据条数</span>
      <span class="hljs-built_in">this</span>.total = res.data.total
    &#125;,
    <span class="hljs-function"><span class="hljs-title">handleSizeChange</span>(<span class="hljs-params">newSize</span>)</span> &#123;
      <span class="hljs-comment">//当pagesize发生改变时触发</span>
      <span class="hljs-built_in">this</span>.queryInfo.pagesize = newSize
      <span class="hljs-built_in">this</span>.getCateList()
    &#125;,
    <span class="hljs-function"><span class="hljs-title">handleCurrentChange</span>(<span class="hljs-params">newPage</span>)</span> &#123;
      <span class="hljs-comment">//当pagenum发生改变时触发</span>
      <span class="hljs-built_in">this</span>.queryInfo.pagenum = newPage
      <span class="hljs-built_in">this</span>.getCateList()
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">vue-<code>quill</code>-editor富文本</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsurmon-china%2Fvue-quill-editor" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/surmon-china/vue-quill-editor" ref="nofollow noopener noreferrer">官网</a>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b639163fff94ceebfbc2f0a2a84f9e5~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-20 下午3.20.56.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>下载插件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">yarn add vue-quill-editor
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在<code>main.js</code>中引入</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//导入vue-quill-editor（富文本编辑器）</span>
<span class="hljs-keyword">import</span> VueQuillEditor <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-quill-editor'</span>
<span class="hljs-comment">//导入vue-quill-editor的样式</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'quill/dist/quill.core.css'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'quill/dist/quill.snow.css'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'quill/dist/quill.bubble.css'</span>
......
<span class="hljs-comment">//全局注册组件</span>
Vue.component(<span class="hljs-string">'tree-table'</span>, TreeTable)
<span class="hljs-comment">//全局注册富文本组件</span>
Vue.use(VueQuillEditor)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在<code>src/components/goods/Add.vue</code>中使用</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><!-- 富文本编辑器组件 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-tab-pane</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"商品内容"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"4"</span>></span>
  <span class="hljs-comment"><!-- 富文本编辑器组件 --></span>
  <span class="hljs-tag"><<span class="hljs-name">quill-editor</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"addForm.goods_introduce"</span>></span><span class="hljs-tag"></<span class="hljs-name">quill-editor</span>></span>
  <span class="hljs-comment"><!-- 添加商品按钮 --></span>
  <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btnAdd"</span>></span>添加商品<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">el-tab-pane</span>></span></span>

<span class="hljs-comment">//在数据中添加goods_introduce</span>
<span class="hljs-comment">//添加商品的表单数据对象</span>
addForm: &#123;
  <span class="hljs-attr">goods_name</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">goods_price</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">goods_weight</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">goods_number</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">goods_cat</span>: [],
  <span class="hljs-comment">//上传图片数组</span>
  <span class="hljs-attr">pics</span>: [],
  <span class="hljs-comment">//商品的详情介绍</span>
  <span class="hljs-attr">goods_introduce</span>:<span class="hljs-string">''</span>
&#125;
<span class="hljs-comment">//在global.css样式中添加富文本编辑器的最小高度</span>
.ql-editor&#123;
    min-height: 300px;
&#125;
<span class="hljs-comment">//给添加商品按钮添加间距</span>
.btnAdd&#123;
  margin-top:15px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">lodash 深拷贝</h2>
<ol>
<li>下载依赖</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">npm i --save lodash
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在.vue文件中 导入lodash并使用</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-comment">//官方推荐将lodash导入为_</span>
<span class="hljs-keyword">import</span> _ <span class="hljs-keyword">from</span> <span class="hljs-string">'lodash'</span>

...其他代码

<span class="hljs-keyword">const</span> form = _.cloneDeep(<span class="hljs-built_in">this</span>.addForm)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-28">项目优化</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b46fe6d7b8b4c1298a232f0ce62eccf~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-21 上午9.10.00.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-29">添加进度条--nprogress</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frstacruz%2Fnprogress" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rstacruz/nprogress" ref="nofollow noopener noreferrer">官网</a></p>
<ol>
<li>下载插件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">yarn add nprogress
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在src/utils/request.js路由处理器中配置</li>
</ol>
<ul>
<li>在请求在到达服务器之前--开启进度条</li>
<li>在服务器的响应结束后--结束进度条</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2019adbc33374a25997f47e5488d2245~tplv-k3u1fbpfcp-watermark.image" alt="2741629449142_.pic_hd.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 导入axios</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-comment">// 设置请求的根路径</span>
axios.defaults.baseURL = <span class="hljs-string">'http://127.0.0.1:8888/api/private/v1/'</span>

<span class="hljs-comment">//导入进度条插件</span>
<span class="hljs-keyword">import</span> NProgress <span class="hljs-keyword">from</span> <span class="hljs-string">'nprogress'</span>
<span class="hljs-comment">//导入进度条样式</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'nprogress/nprogress.css'</span>

<span class="hljs-comment">//请求在到达服务器之前，先会调用use中的这个回调函数来添加请求头信息</span>
axios.interceptors.request.use(<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    <span class="hljs-comment">//当进入request拦截器，表示发送了请求，我们就开启进度条</span>
    NProgress.start()

    <span class="hljs-comment">//为请求头对象，添加token验证的Authorization字段</span>
    config.headers.Authorization = <span class="hljs-built_in">window</span>.sessionStorage.getItem(<span class="hljs-string">'token'</span>)
    <span class="hljs-keyword">return</span> config
&#125;)

<span class="hljs-comment">//在response拦截器中，服务器响应结束后，隐藏进度条</span>
axios.interceptors.response.use(<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    <span class="hljs-comment">//当进入response拦截器，表示请求已经结束，我们就结束进度条</span>
    NProgress.done()
    <span class="hljs-keyword">return</span> config
&#125;)

<span class="hljs-comment">// 导出</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> axios
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-30">解决自动换行的问题</h2>
<p>根据ESLint的警告提示更改对应的代码</p>
<p>在<code>.prettierrc</code>文件中更改设置<code>"printWidth":200</code>, 将每行代码的文字数量更改为200</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-string">"semi"</span>:<span class="hljs-literal">false</span>,
    <span class="hljs-string">"singleQuote"</span>:<span class="hljs-literal">true</span>,
    <span class="hljs-string">"printWidth"</span>:<span class="hljs-number">200</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-31">在build前移除所有的console.log</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbc7e020461b4ee1ab0e1f3d8c4aeb73~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-21 上午9.18.49.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>下载插件（开发依赖）</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">yarn add babel-plugin-transform-remove-<span class="hljs-built_in">console</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在<code>babel.config.js</code>中配置，需要只在<code>项目发布</code>阶段 再移除</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 开发阶段：程序员 测试 共同完成 项目的过程 ， 不要 移除 console 的输出</span>
<span class="hljs-comment">// 生成阶段；普通用户可以通过浏览器来使用项目网站 ， 要 移除 console的输出</span>
<span class="hljs-keyword">const</span> proPlugs = []
<span class="hljs-keyword">if</span> (process.env.NODE_ENV === <span class="hljs-string">'production'</span>) &#123;
  proPlugs.push(<span class="hljs-string">"transform-remove-console"</span>)
&#125;
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">presets</span>: [
    <span class="hljs-string">'@vue/cli-plugin-babel/preset'</span>
  ],
  <span class="hljs-string">"plugins"</span>: [...proPlugs]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-32">生成打包报告</h2>
<ol>
<li>
<p>命令行形式生成打包报告 <code>vue-cli-service build --report </code></p>
</li>
<li>
<p>在vue控制台生成打包报告 点击“任务”=>“build”=>“运行” 运行完毕之后点击右侧“分析”，“控制台”面板查看报告</p>
</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aad5ced0ed8c42aa87cc1ef7dbfd2b36~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-21 上午9.26.17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-33">修改webpack的默认配置</h2>
<blockquote>
<p>默认情况下，vue-cli 3.0生成的项目，隐藏了webpack配置项，如果我们需要配置webpack 需要通过vue.config.js来配置。</p>
</blockquote>
<h3 data-id="heading-34">配置不同的 入口文件</h3>
<blockquote>
<p>原因：针对 开发时，我们可能需要一些工具模块辅助</p>
<p>而部署到线上时，我们并不需要那些工具模块了</p>
</blockquote>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fconfig%2F%23chainwebpack" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/config/#chainwebpack" ref="nofollow noopener noreferrer">chainWebpack</a>可以通过<code>链式编程</code>的形式，修改webpack配置</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fconfig%2F%23configurewebpack" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/config/#configurewebpack" ref="nofollow noopener noreferrer">configureWebpack</a>可以通过<code>操作对象</code>的形式，修改webpack配置</p>
</li>
</ul>
<p>在项目根目录中创建<code>vue.config.js</code>文件</p>
<pre><code class="hljs language-js copyable" lang="js">- 设置生产环境production的 入口文件为 main-prod.js
- 设置开发模式 development的 入口文件为 main-dev.js
<span class="hljs-comment">// webpack不能识别高版本语法，所以需要用老的 Common JS语法导出</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">chainWebpack</span>:<span class="hljs-function"><span class="hljs-params">config</span>=></span>&#123;
        <span class="hljs-comment">//发布模式</span>
        config.when(process.env.NODE_ENV === <span class="hljs-string">'production'</span>,<span class="hljs-function"><span class="hljs-params">config</span>=></span>&#123;
            <span class="hljs-comment">//entry找到默认的打包入口，调用clear则是删除默认的打包入口</span>
            <span class="hljs-comment">//add添加新的打包入口</span>
            config.entry(<span class="hljs-string">'app'</span>).clear().add(<span class="hljs-string">'./src/main-prod.js'</span>)
        &#125;)
        <span class="hljs-comment">//开发模式</span>
        config.when(process.env.NODE_ENV === <span class="hljs-string">'development'</span>,<span class="hljs-function"><span class="hljs-params">config</span>=></span>&#123;
            config.entry(<span class="hljs-string">'app'</span>).clear().add(<span class="hljs-string">'./src/main-dev.js'</span>)
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-35">大文件访问优化</h2>
<h3 data-id="heading-36">通过external加载外部CDN资源</h3>
<blockquote>
<p>默认情况下，依赖项的所有第三方包都会被打包到js/chunk-vendors. ****** .js文件中，导致该js文件过大</p>
<p>那么我们可以通过externals排除这些包，使它们不被打包到js/chunk-vendors. ****** .js文件中</p>
</blockquote>
<p>！！待补充cdn图和笔记</p>
<ol>
<li>修改<code>vue.config.js</code>文件的配置，在生产环境下使用externals排除包</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">chainWebpack</span>:<span class="hljs-function"><span class="hljs-params">config</span>=></span>&#123;
        <span class="hljs-comment">//发布模式</span>
        config.when(process.env.NODE_ENV === <span class="hljs-string">'production'</span>,<span class="hljs-function"><span class="hljs-params">config</span>=></span>&#123;
            <span class="hljs-comment">//entry找到默认的打包入口，调用clear则是删除默认的打包入口</span>
            <span class="hljs-comment">//add添加新的打包入口</span>
            config.entry(<span class="hljs-string">'app'</span>).clear().add(<span class="hljs-string">'./src/main-prod.js'</span>)

            <span class="hljs-comment">//！！使用externals设置排除项，编译时，遇到这些模块不要打包</span>
            config.set(<span class="hljs-string">'externals'</span>,&#123;
                <span class="hljs-attr">vue</span>:<span class="hljs-string">'Vue'</span>,
                <span class="hljs-string">'vue-router'</span>:<span class="hljs-string">'VueRouter'</span>,
                <span class="hljs-attr">axios</span>:<span class="hljs-string">'axios'</span>,
                <span class="hljs-attr">lodash</span>:<span class="hljs-string">'_'</span>,
                <span class="hljs-attr">echarts</span>:<span class="hljs-string">'echarts'</span>,
                <span class="hljs-attr">nprogress</span>:<span class="hljs-string">'NProgress'</span>,
                <span class="hljs-string">'vue-quill-editor'</span>:<span class="hljs-string">'VueQuillEditor'</span>,
                <span class="hljs-string">'element-ui'</span>: <span class="hljs-string">'ElementUI'</span>
            &#125;)
        &#125;)
        <span class="hljs-comment">//开发模式</span>
        config.when(process.env.NODE_ENV === <span class="hljs-string">'development'</span>,<span class="hljs-function"><span class="hljs-params">config</span>=></span>&#123;
            config.entry(<span class="hljs-string">'app'</span>).clear().add(<span class="hljs-string">'./src/main-dev.js'</span>)
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在public/index.js文件下，让外部CDN引入这些排除掉的资源</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">    <!-- 引入 CDN外部静态资源 -->
    <!-- nprogress 的样式表文件 -->
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://cdn.staticfile.org/nprogress/0.2.0/nprogress.min.css"</span> /></span></span>
    <!-- 富文本编辑器 的样式表文件 -->
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://cdn.staticfile.org/quill/1.3.4/quill.core.min.css"</span> /></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://cdn.staticfile.org/quill/1.3.4/quill.snow.min.css"</span> /></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://cdn.staticfile.org/quill/1.3.4/quill.bubble.min.css"</span> /></span></span>
    <!-- element-ui 的样式表文件 -->
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://cdn.staticfile.org/element-ui/2.8.2/theme-chalk/index.css"</span> /></span></span>

    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.staticfile.org/vue/2.5.22/vue.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.staticfile.org/vue-router/3.0.1/vue-router.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.staticfile.org/axios/0.18.0/axios.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.staticfile.org/lodash.js/4.17.11/lodash.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.staticfile.org/echarts/4.1.0/echarts.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.staticfile.org/nprogress/0.2.0/nprogress.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
    <!-- 富文本编辑器的 js 文件 -->
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.staticfile.org/quill/1.3.4/quill.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue-quill-editor@3.0.4/dist/vue-quill-editor.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

    <!-- element-ui 的 js 文件 -->
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.staticfile.org/element-ui/2.8.2/index.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>打开开发入口文件main-prod.js,删除掉默认的引入代码</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>
<span class="hljs-comment">// import './plugins/element.js'</span>
<span class="hljs-comment">//导入字体图标</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./assets/fonts/iconfont.css'</span>
<span class="hljs-comment">//导入全局样式</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./assets/css/global.css'</span>
<span class="hljs-comment">//导入第三方组件vue-table-with-tree-grid</span>
<span class="hljs-keyword">import</span> TreeTable <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-table-with-tree-grid'</span>
<span class="hljs-comment">//导入进度条插件</span>
<span class="hljs-keyword">import</span> NProgress <span class="hljs-keyword">from</span> <span class="hljs-string">'nprogress'</span>
<span class="hljs-comment">//导入进度条样式</span>
<span class="hljs-comment">// import 'nprogress/nprogress.css'</span>
<span class="hljs-comment">// //导入axios</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-comment">// //导入vue-quill-editor（富文本编辑器）</span>
<span class="hljs-keyword">import</span> VueQuillEditor <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-quill-editor'</span>
<span class="hljs-comment">// //导入vue-quill-editor的样式</span>
<span class="hljs-comment">// import 'quill/dist/quill.core.css'</span>
<span class="hljs-comment">// import 'quill/dist/quill.snow.css'</span>
<span class="hljs-comment">// import 'quill/dist/quill.bubble.css'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">定制首页内容</h2>
<blockquote>
<p>开发环境的首页和发布环境的首页展示内容的形式有所不同 如开发环境中使用的是import加载第三方包，而发布环境则是使用CDN，</p>
<p>那么首页也需根据环境不同来进行不同的实现 我们可以通过插件的方式来定制首页内容，</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b87ac13832834442b8c5f9989a69ba4a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>在<code>vue.config.js</code>进行配置isProd变量（生产模式-true，开发模式-false）</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">chainWebpack</span>:<span class="hljs-function"><span class="hljs-params">config</span>=></span>&#123;
        config.when(process.env.NODE_ENV === <span class="hljs-string">'production'</span>,<span class="hljs-function"><span class="hljs-params">config</span>=></span>&#123;
            ......
            
            <span class="hljs-comment">//使用插件</span>
            config.plugin(<span class="hljs-string">'html'</span>).tap(<span class="hljs-function"><span class="hljs-params">args</span>=></span>&#123;
                <span class="hljs-comment">//添加参数isProd</span>
                args[<span class="hljs-number">0</span>].isProd = <span class="hljs-literal">true</span>
                <span class="hljs-keyword">return</span> args
            &#125;)
        &#125;)

        config.when(process.env.NODE_ENV === <span class="hljs-string">'development'</span>,<span class="hljs-function"><span class="hljs-params">config</span>=></span>&#123;
            config.entry(<span class="hljs-string">'app'</span>).clear().add(<span class="hljs-string">'./src/main-dev.js'</span>)

            <span class="hljs-comment">//使用插件</span>
            config.plugin(<span class="hljs-string">'html'</span>).tap(<span class="hljs-function"><span class="hljs-params">args</span>=></span>&#123;
                <span class="hljs-comment">//添加参数isProd</span>
                args[<span class="hljs-number">0</span>].isProd = <span class="hljs-literal">false</span>
                <span class="hljs-keyword">return</span> args
            &#125;)
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>然后在<code>public/index.html</code>中使用插件判断是否为发布环境并定制首页内容</li>
</ol>
<ul>
<li>根据不同环境，设置不同的title</li>
<li>根据不同环境，判断是否要引入CDN外部静态资源，避免重复引用模块</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    
    <title><%= htmlWebpackPlugin.options.isProd ? '' : 'dev - ' %>电商后台管理系统</title>

    <% if(htmlWebpackPlugin.options.isProd)&#123; %>
    <!-- nprogress 的样式表文件 -->
    <link rel="stylesheet" href="https://cdn.staticfile.org/nprogress/0.2.0/nprogress.min.css" />
    ........
    <!-- element-ui 的 js 文件 -->
    <script src="https://cdn.staticfile.org/element-ui/2.8.2/index.js"></script>
    <% &#125; %>
  </head>
  .......
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-38">路由懒加载</h2>
<p>当路由被访问时才加载对应的路由文件，就是路由懒加载。</p>
<h3 data-id="heading-39">拆分chunks.js文件</h3>
<blockquote>
<p>由于默认webpack编译时，将所有的组件编译到 一个chunks.js文件中，体积会很大，浏览器首次加载时，比较耗时，所以将其拆分，优化用户体验</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34ccbed691534f9da0bda5fccf42672b~tplv-k3u1fbpfcp-watermark.image" alt="16471629530481_.pic_hd.jpg" loading="lazy" referrerpolicy="no-referrer">
1.安装开发依赖</p>
<pre><code class="hljs language-js copyable" lang="js">yarn add @babel/plugin-syntax-dynamic-<span class="hljs-keyword">import</span> -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在<code>babel.config.js</code>中声明该插件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@vue/cli-plugin-babel/preset'</span>],
    <span class="hljs-attr">plugins</span>: [
        ...其他代码
        
        <span class="hljs-comment">//配置路由懒加载插件</span>
        <span class="hljs-string">'@babel/plugin-syntax-dynamic-import'</span>
    ]
&#125;<span class="hljs-string">`
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-40">项目上线配置</h2>
<h3 data-id="heading-41">通过node创建服务器</h3>
<p>在vue_shop同级创建一个文件夹vue_shop_server存放node服务器 使用终端打开vue_shop_server文件夹，</p>
<p>输入命令 npm init -y 初始化包之后，输入命令 npm i express -S 打开vue_shop目录，复制dist文件夹，粘贴到vue_shop_server中</p>
<p>在vue_shop_server文件夹中创建app.js文件,编写代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)

<span class="hljs-keyword">const</span> app = express()

app.use(express.static(<span class="hljs-string">'./dist'</span>))

app.listen(<span class="hljs-number">8998</span>,<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"server running at http://127.0.0.1:8998"</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再次在终端中输入 node app.js</p>
<h3 data-id="heading-42">开启gzip压缩</h3>
<p>打开vue_shop_server文件夹的终端，输入命令：</p>
<pre><code class="hljs language-js copyable" lang="js">npm i compression -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开app.js,编写代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)
<span class="hljs-comment">// 导入包</span>
<span class="hljs-keyword">const</span> compression = <span class="hljs-built_in">require</span>(<span class="hljs-string">'compression'</span>)

<span class="hljs-keyword">const</span> app = express()
<span class="hljs-comment">// 注册中间件</span>
app.use(compression())
app.use(express.static(<span class="hljs-string">'./dist'</span>))

app.listen(<span class="hljs-number">8998</span>,<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"server running at http://127.0.0.1:8998"</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            