
---
title: 'Vue路由'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5321'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 06:41:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=5321'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Vue路由-基本使用</h1>
<ul>
<li>1.引入vue-router
<pre><code class="hljs language-js copyable" lang="js"><script src=<span class="hljs-string">"./lib/vue-router.js"</span>></script>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>2.定义路由组件
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> Login = &#123;
   <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>Login组件</div>'</span>
 &#125;
 <span class="hljs-keyword">const</span> Register = &#123;
   <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>Register组件</div>'</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>3.实例化路由对象 new VueRouter
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// router 路由</span>
<span class="hljs-comment">// route 规则</span>
<span class="hljs-keyword">const</span> routerobj = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-comment">// 4. 配置路由的规则   </span>
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
      <span class="hljs-attr">component</span>: Login
    &#125;,
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/register'</span>,
      <span class="hljs-attr">component</span>: Register
    &#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>4.配置路由的规则（如上）</li>
<li>5.挂载路由</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Vue(&#123;
     <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
     <span class="hljs-comment">// 5. 挂载路由  </span>
     <span class="hljs-attr">router</span>:routerobj
   &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>6.渲染路由</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#/login"</span>></span>登录<span class="hljs-tag"></<span class="hljs-name">a</span>></span></span>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#/register"</span>></span>注册<span class="hljs-tag"></<span class="hljs-name">a</span>></span></span>
   <!-- <span class="hljs-number">6.</span> 渲染路由  -->
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span></span>
 </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">Vue路由-路由高亮</h1>
<ul>
<li>1.引入vue-router （必须先引入vue.js，在引入vue-router.js，因为先有vue再有vue-router）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><script src=<span class="hljs-string">"./lib/vue.js"</span>></script>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./lib/vue-router.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<ol start="2">
<li></li>
</ol>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><script>
   <span class="hljs-comment">// 2. 定义路由组件</span>
   <span class="hljs-keyword">const</span> Login = &#123;
     <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>Login组件</div>'</span>
   &#125;
   <span class="hljs-keyword">const</span> Register = &#123;
     <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>Register组件</div>'</span>
   &#125;
   <span class="hljs-comment">// 3. 实例化路由对象 new VueRouter   </span>
   <span class="hljs-comment">// router 路由</span>
   <span class="hljs-comment">// route 规则</span>
   <span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
     <span class="hljs-comment">// 4. 配置路由的规则   </span>
     <span class="hljs-attr">routes</span>: [
       &#123;
         <span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
         <span class="hljs-attr">component</span>: Login
       &#125;,
       &#123;
         <span class="hljs-attr">path</span>: <span class="hljs-string">'/register'</span>,
         <span class="hljs-attr">component</span>: Register
       &#125;
     ],
     <span class="hljs-attr">linkActiveClass</span>: <span class="hljs-string">'active'</span>
   &#125;)
   <span class="hljs-keyword">new</span> Vue(&#123;
     <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
     <span class="hljs-comment">// 5. 挂载路由  </span>
     router
   &#125;)
 </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3.渲染</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
   <!-- tag=<span class="hljs-string">"div"</span> 设置为指定的标签 默认为 a标签 -->
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/login"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"div"</span>></span>登录<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span></span>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/register"</span>></span>注册<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span></span>
   <!-- <span class="hljs-number">6.</span> 渲染路由  -->
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span></span>
 </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>4.样式</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><style>
   .router-link-active &#123;
     font-size: 50px;
     color: pink;
   &#125;

   <span class="hljs-comment">/* 模拟第三方 提供好的选中 样式 */</span>
   .active &#123;
     font-size: 50px;
     color: yellow;
   &#125;
 </style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">vue路由-路由传参</h1>
<pre><code class="hljs language-js copyable" lang="js"><body>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
   <span class="hljs-comment"><!-- <a href="#/login">登录</a>
   <a href="#/register">注册</a> --></span>
   <span class="hljs-comment"><!-- tag="div" 设置为指定的标签 默认为 a标签 --></span>
   <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/login?name=fly&age=18"</span>></span>登录<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/register/zs/18"</span>></span>注册<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
   <span class="hljs-comment"><!-- 6. 渲染路由  --></span>
   <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
   <span class="hljs-comment">// 2. 定义路由组件</span>
   <span class="hljs-keyword">const</span> Login = &#123;
     <span class="hljs-comment">// template: '<div>Login组件---&#123;&#123;$route.query.name&#125;&#125;----&#123;&#123;$route.query.age&#125;&#125;</div>',</span>
     <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>Login组件---&#123;&#123;name&#125;&#125;----&#123;&#123;age&#125;&#125;</div>'</span>,
     <span class="hljs-comment">// data() &#123;</span>
     <span class="hljs-comment">//   return &#123;</span>
     <span class="hljs-comment">//     name: this.$route.query.name,</span>
     <span class="hljs-comment">//     age: this.$route.query.age</span>
     <span class="hljs-comment">//   &#125;</span>
     <span class="hljs-comment">// &#125;,</span>
     <span class="hljs-attr">data</span>: <span class="hljs-function">() =></span> (&#123;
       <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
       <span class="hljs-attr">age</span>: <span class="hljs-string">''</span>
     &#125;),
     <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
       <span class="hljs-comment">// console.log(this.$route.query.name)</span>
       <span class="hljs-comment">// console.log(this.$route.query.age)</span>
       <span class="hljs-built_in">this</span>.name = <span class="hljs-built_in">this</span>.$route.query.name
       <span class="hljs-built_in">this</span>.age = <span class="hljs-built_in">this</span>.$route.query.age
     &#125;
   &#125;
   <span class="hljs-keyword">const</span> Register = &#123;
     <span class="hljs-attr">props</span>: [<span class="hljs-string">'name'</span>, <span class="hljs-string">'age'</span>],
     <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>Register组件</div>'</span>,
     <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name, <span class="hljs-built_in">this</span>.age)
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$route.params.name)
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$route.params.age)
       <span class="hljs-comment">// this.name = this.$route.query.name</span>
       <span class="hljs-comment">// this.age = this.$route.query.age</span>
     &#125;
   &#125;
   <span class="hljs-comment">// 3. 实例化路由对象 new VueRouter   </span>
   <span class="hljs-comment">// router 路由</span>
   <span class="hljs-comment">// route 规则</span>
   <span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
     <span class="hljs-comment">// 4. 配置路由的规则   </span>
     <span class="hljs-attr">routes</span>: [
       &#123;
         <span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
         <span class="hljs-attr">component</span>: Login
       &#125;,
       &#123;
         <span class="hljs-attr">path</span>: <span class="hljs-string">'/register/:name/:age'</span>,
         <span class="hljs-attr">component</span>: Register,
         <span class="hljs-attr">props</span>: <span class="hljs-literal">true</span>
       &#125;
     ],
     <span class="hljs-attr">linkActiveClass</span>: <span class="hljs-string">'active'</span>
   &#125;)
   <span class="hljs-keyword">new</span> Vue(&#123;
     <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
     <span class="hljs-comment">// 5. 挂载路由  </span>
     router
   &#125;)
 </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">编程式导航路由</h1>
<pre><code class="hljs language-js copyable" lang="js"><body>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"goDetail"</span>></span>goDetail<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
   <span class="hljs-keyword">const</span> Login = &#123;
     <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>Login组件</div>'</span>,
     <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$route.query.name)
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$route.query.age)

       <span class="hljs-comment">// console.log(this.$route.params.name)</span>
       <span class="hljs-comment">// console.log(this.$route.params.age)</span>
     &#125;
   &#125;

   <span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
     <span class="hljs-attr">routes</span>: [
       &#123;
         <span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
         <span class="hljs-attr">component</span>: Login
       &#125;,
       &#123;
         <span class="hljs-attr">name</span>: <span class="hljs-string">'login'</span>,
         <span class="hljs-attr">path</span>: <span class="hljs-string">'/login/:name/:age'</span>,
         <span class="hljs-attr">component</span>: Login
       &#125;
     ],
     <span class="hljs-attr">linkActiveClass</span>: <span class="hljs-string">'active'</span>
   &#125;)
   <span class="hljs-comment">//解决只能点击一次的报错，设置后可以多次点击</span>
   <span class="hljs-keyword">const</span> originalPush = VueRouter.prototype.push
   VueRouter.prototype.push = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">push</span>(<span class="hljs-params">location</span>) </span>&#123;
     <span class="hljs-keyword">return</span> originalPush.call(<span class="hljs-built_in">this</span>, location).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> err)
   &#125;
   <span class="hljs-keyword">new</span> Vue(&#123;
     <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
     router,
     <span class="hljs-attr">methods</span>: &#123;
       <span class="hljs-function"><span class="hljs-title">goDetail</span>(<span class="hljs-params"></span>)</span> &#123;
         <span class="hljs-comment">// $route 参数使用</span>
         <span class="hljs-comment">// $router 路由调转</span>
         <span class="hljs-comment">// console.log(this.$router)</span>
         <span class="hljs-comment">// 字符串   用query</span>
         <span class="hljs-comment">// this.$router.push('/login')</span>
         <span class="hljs-comment">// this.$router.push('/login?name=fly&age=18')</span>
         <span class="hljs-comment">// this.$router.push('/login/fly/18')</span>
         <span class="hljs-comment">// 对象写法</span>
         <span class="hljs-comment">// this.$router.push(&#123; path: '/login', query: &#123; name: 'fly', age: 18 &#125; &#125;)//用query</span>
         <span class="hljs-built_in">this</span>.$router.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'login'</span>, <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'fly'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125; &#125;)<span class="hljs-comment">//用query</span>

         <span class="hljs-comment">// back</span>

         <span class="hljs-comment">// forware  </span>

         <span class="hljs-comment">// go  </span>
       &#125;
     &#125;
   &#125;)
 </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">嵌套路由</h1>
<pre><code class="hljs language-js copyable" lang="js"><body>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/account"</span>></span>Account<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
   <span class="hljs-keyword">const</span> Account = &#123;
     <span class="hljs-attr">template</span>: <span class="hljs-string">`
       <div>
         <div>Account组件</div>
         <router-link to="/account/login">login</router-link>  
         <router-link to="/account/register">register</router-link>  
         <router-view></router-view>
       </div>
     `</span>
   &#125;
   <span class="hljs-keyword">const</span> Login = &#123;
     <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>Login组件</div>'</span>
   &#125;
   <span class="hljs-keyword">const</span> Register = &#123;
     <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>Register组件</div>'</span>
   &#125;
   <span class="hljs-comment">// 3. 实例化路由对象 new VueRouter   </span>
   <span class="hljs-comment">// router 路由</span>
   <span class="hljs-comment">// route 规则</span>
   <span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
     <span class="hljs-comment">// 4. 配置路由的规则   </span>
     <span class="hljs-attr">routes</span>: [
       &#123;
         <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
         <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/account/register'</span>
       &#125;,
       &#123;
         <span class="hljs-attr">path</span>: <span class="hljs-string">'/account'</span>,
         <span class="hljs-attr">component</span>: Account,
         <span class="hljs-attr">children</span>: [
           &#123;
             <span class="hljs-attr">path</span>: <span class="hljs-string">'/account/login'</span>,
             <span class="hljs-attr">component</span>: Login
           &#125;,
           &#123;
             <span class="hljs-attr">path</span>: <span class="hljs-string">'/account/register'</span>,
             <span class="hljs-attr">component</span>: Register
           &#125;
         ]
       &#125;
     ]
   &#125;)
   <span class="hljs-keyword">new</span> Vue(&#123;
     <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
     <span class="hljs-comment">// 5. 挂载路由  </span>
     router
   &#125;)
 </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
</body>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            