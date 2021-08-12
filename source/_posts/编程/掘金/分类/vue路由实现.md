
---
title: 'vue路由实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd5102e9d4464fb39e619c88ae86679d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 05:29:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd5102e9d4464fb39e619c88ae86679d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">动态路由</h1>
<p>路由规则填写props为true，在组件内部通过props获取对应路由参数，这里的路由参数理解为组件的属性
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd5102e9d4464fb39e619c88ae86679d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">嵌套路由</h1>
<p>将公共部分抽离需要渲染的部用router-view展示,Layout组件</p>

    

<h1 data-id="heading-2">编程式导航</h1>
<pre><code class="hljs language-js copyable" lang="js">$router.push(<span class="hljs-string">'/'</span>) <span class="hljs-comment">//不传参数</span>
$router.push(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'login'</span>,<span class="hljs-attr">id</span>:<span class="hljs-number">1</span>&#125;) <span class="hljs-comment">//传参数</span>
$router.replace() <span class="hljs-comment">//不记录历史</span>
$router.go(-<span class="hljs-number">1</span>) <span class="hljs-comment">//返回上一级</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">hash模式和history模式区别</h1>
<h2 data-id="heading-4">hash模式</h2>
<ul>
<li>url#后面内容作为路径地址</li>
<li>监听hashchange事件</li>
<li>根据当前路由地址找到对应法组件进行渲染</li>
</ul>
<h2 data-id="heading-5">history模式</h2>
<ul>
<li>通过history的pushState改变地址栏</li>
<li>监听popstate事件</li>
<li>根据当前路由地址找到对应的组件进行渲染</li>
</ul>
<p><strong>注意</strong></p>
<ol>
<li>history模式下刷新浏览器会向服务端发送请求,在后端需要配置基于history模式支持</li>
<li>nginx配置history</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e30fbd12c7ec431f823ae8fda5eeeb8f~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-08-08 115242.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">vue-router模拟实现</h1>
<h2 data-id="heading-7">类图</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9efc88f2f5564bc48a5adecb38fe5905~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-08-08 122333.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">分步拆解</h3>
<ol>
<li>创建install方法</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af73f3d6ac56468e8cf9305e8739da4f~tplv-k3u1fbpfcp-watermark.image" alt="router1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>创建构造函数</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc44b3824fd1480c847d9caa8cbe3451~tplv-k3u1fbpfcp-watermark.image" alt="router2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//创建响应式对象</span>
Vue.observable(&#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>创建routeMap</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdd2a89238c94345a5d671c49a77b6ad~tplv-k3u1fbpfcp-watermark.image" alt="route3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>创建router-link</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23ef8fa3829c48e98e05b0c4ced2595b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>4.1 vue的构建版本</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/065f21d6c37e4bab96dfb1dab6841c2a~tplv-k3u1fbpfcp-watermark.image" alt="vue-build.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>4.2 运行时版本Vue通过render函数渲染template</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29926d68d64845fbaaffb25ac967d58f~tplv-k3u1fbpfcp-watermark.image" alt="render.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>4.3 阻止浏览器的默认行为,渲染对应组件</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cd1e43df7994bf8b98becc4c60015de~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>创建router-view</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5592290066754987a8286e96a29343c6~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="6">
<li>initEvent函数,浏览器前进后退渲染对应视图</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24045bfd4fe643bda02be9c25773d1cb~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">完整版vue-router</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> _Vue = <span class="hljs-literal">null</span>
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">install</span>(<span class="hljs-params">Vue</span>)</span> &#123;
    <span class="hljs-comment">//1.判断当前插件是否已经被安装</span>
    <span class="hljs-keyword">if</span> (VueRouter.install.installed) &#123;
      <span class="hljs-keyword">return</span>
    &#125;
    VueRouter.install.installed = <span class="hljs-literal">true</span>
    <span class="hljs-comment">//2. 将Vue构构造函数记录到全局变量</span>
    _Vue = Vue
    <span class="hljs-comment">//3.将传入的router对象注入Vue实例</span>
    _Vue.mixin(&#123;
      <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$options.router) &#123;
          _Vue.prototype.$router = <span class="hljs-built_in">this</span>.$options.router
          <span class="hljs-built_in">this</span>._init()
        &#125;
      &#125;
    &#125;)
  &#125;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.options = options
    <span class="hljs-built_in">this</span>.routeMap = &#123;&#125;
    <span class="hljs-built_in">this</span>.data = _Vue.observable(&#123;
      <span class="hljs-attr">current</span>: <span class="hljs-string">'/'</span>
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">_init</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.createRouteMap()
    <span class="hljs-built_in">this</span>.initComponents()
    <span class="hljs-built_in">this</span>.initEvent()
  &#125;
  <span class="hljs-function"><span class="hljs-title">createRouteMap</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.options.router.forEach(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.routeMap[route.path] = route.component
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">initComponents</span>(<span class="hljs-params">Vue</span>)</span> &#123;
    <span class="hljs-keyword">const</span> that = <span class="hljs-built_in">this</span>
    Vue.component(<span class="hljs-string">'router-link'</span>, &#123;
      <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">to</span>: <span class="hljs-built_in">String</span>
      &#125;,
      <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
        <span class="hljs-keyword">return</span> h(
          <span class="hljs-string">'a'</span>,
          &#123;
            <span class="hljs-attr">attrs</span>: &#123;
              <span class="hljs-attr">href</span>: <span class="hljs-built_in">this</span>.to
            &#125;,
            <span class="hljs-attr">on</span>: &#123;
              <span class="hljs-attr">click</span>: <span class="hljs-built_in">this</span>.clickHandler
            &#125;
          &#125;,
          [<span class="hljs-built_in">this</span>.$slots.default]
        )
      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">clickHandler</span>(<span class="hljs-params">e</span>)</span> &#123;
          history.pushState(&#123;&#125;, <span class="hljs-string">''</span>, <span class="hljs-built_in">this</span>.to)
          <span class="hljs-built_in">this</span>.$router.data.current = <span class="hljs-built_in">this</span>.to
          e.preventDefault()
        &#125;
      &#125;
    &#125;)
    Vue.component(<span class="hljs-string">'router-view'</span>, &#123;
      <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
        <span class="hljs-keyword">const</span> component = that.routeMap[that.data.current]
        <span class="hljs-keyword">return</span> h(component)
      &#125;
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">initEvent</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'popstate'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.data.current = <span class="hljs-built_in">window</span>.location.pathname
    &#125;)
  &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            