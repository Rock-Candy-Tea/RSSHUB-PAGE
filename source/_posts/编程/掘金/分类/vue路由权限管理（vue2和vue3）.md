
---
title: 'vue路由权限管理（vue2和vue3）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5045'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 22:20:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=5045'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 14 天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h1 data-id="heading-0">vue路由权限管理（vue2和vue3）</h1>
<h2 data-id="heading-1">1. Vue 路由权限控制一般有2种方法</h2>
<ul>
<li>a、路由元信息(meta)</li>
<li>b、动态加载菜单和路由(addRoutes)</li>
</ul>
<h2 data-id="heading-2">2 路由元信息（meta）来进行路由权限控制</h2>
<h3 data-id="heading-3">2.1 在vue2种的实现</h3>
<p>如果一个网站有不同的角色，比如 管理员 和 普通用户 ，要求不同的角色能访问的页面是不一样的</p>
<p>这个时候我们就可以 把所有的页面都放在路由表里 ，只要 在访问的时候判断一下角色权限 。如果有权限就让访问，没有权限的话就拒绝访问，跳转到404页面</p>
<p>vue-router 在构建路由时提供了元信息 meta 配置接口，我们可以在元信息中添加路由对应的权限，然后在路由守卫中检查相关权限，控制其路由跳转。</p>
<p>可以在每一个路由的 meta 属性里，将能访问该路由的角色添加到 roles 里。用户每次登陆后，将用户的角色返回。然后在访问页面时，把路由的 meta 属性和用户的角色进行对比，如果用户的角色在路由的 roles 里，那就是能访问，如果不在就拒绝访问。</p>
<p>以下是vue2的实现方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>;
Vue.use(VueRouter)
...
<span class="hljs-attr">routes</span>: [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'login'</span>,
    <span class="hljs-attr">meta</span>: &#123;
      <span class="hljs-attr">roles</span>: [<span class="hljs-string">'admin'</span>, <span class="hljs-string">'user'</span>]
    &#125;,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/Login.vue'</span>)
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'home'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>,
    <span class="hljs-attr">meta</span>: &#123;
      <span class="hljs-attr">roles</span>: [<span class="hljs-string">'admin'</span>]
    &#125;,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/Home.vue'</span>)
  &#125;,
]

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  routes
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在app.vue文件下引入，注册全局的路由守卫</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//假设有两种角色：admin 和 user </span>
<span class="hljs-comment">//从后台获取的用户角色</span>
<span class="hljs-keyword">const</span> role = <span class="hljs-string">'user'</span>
<span class="hljs-comment">//当进入一个页面是会触发导航守卫 router.beforeEach 事件</span>
router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to,<span class="hljs-keyword">from</span>,next</span>)=></span>&#123;
 <span class="hljs-keyword">if</span>(to.meta.roles.includes(role))&#123;
 next() <span class="hljs-comment">//放行</span>
 &#125;esle&#123;
 next(&#123;<span class="hljs-attr">path</span>:<span class="hljs-string">"/404"</span>&#125;) <span class="hljs-comment">//跳到404页面</span>
 &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自此基本上路由的权限控制就完成了
题外话 在路由守卫中也能很好的解决匹配不到路由转404页面的业务需求,实现如下：</p>
<pre><code class="copyable">import router from ‘./router‘
router.beforeEach((to, from, next) => &#123;
   // ...
    if (to.matched.length === 0) &#123;
        next('/404')
    &#125; else &#123;
        next()
    &#125;
    //console.log(to, from, next, '路由守卫')
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2.2 在vue3种的实现</h3>
<p>其实思路都是差不多的，只是要注意的是vue3中使用路由的方式和vue2有一些细微的差异，使用我用更简单的404去创建vue3的实例，关于vue3的路由权限控制可以按vue2和下面代码依葫芦画瓢，实现代码如下：</p>
<p>创建路由：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createRouter, createWebHashHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>;
...
<span class="hljs-attr">routes</span>: [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'login'</span>,
    <span class="hljs-attr">meta</span>: &#123;
      <span class="hljs-attr">roles</span>: [<span class="hljs-string">'admin'</span>, <span class="hljs-string">'user'</span>]
    &#125;,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/Login.vue'</span>)
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'home'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>,
    <span class="hljs-attr">meta</span>: &#123;
      <span class="hljs-attr">roles</span>: [<span class="hljs-string">'admin'</span>]
    &#125;,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/Home.vue'</span>)
  &#125;,
]
<span class="hljs-keyword">const</span> router = createRouter(&#123;
    <span class="hljs-attr">history</span>: createWebHashHistory(),
    <span class="hljs-attr">routes</span>: routers
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>路由守卫（在App.vue里面进行全局注册）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;
    useRouter
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> router = useRouter();
        router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
            <span class="hljs-comment">// ...</span>
            <span class="hljs-keyword">if</span> (to.matched.length === <span class="hljs-number">0</span>) &#123;
                next(<span class="hljs-string">'/404'</span>)
            &#125; <span class="hljs-keyword">else</span> &#123;
                next()
            &#125;
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">4 . 动态加载菜单和路由(addRoutes)</h2>
<p>根据用户权限或者是用户属性去动态的添加菜单和路由表，可以实现对用户的功能进行定制，vue-router 提供了 addRoutes() 方法，可以动态注册路由， 需要注意的是，动态添加路由是在路由表中 push 路由，由于路由是按顺序匹配的，因此需要将诸如404页面这样的路由放在动态添加的最后</p>
<h2 data-id="heading-6">5.总结</h2>
<p>不管是vue2还是vue3，其实实现思想都差不多，只是使用接口细节会有少许的不一样，使用对我们来说学习的重点千万不能放在某一个框架上，而是要训练自己的思维</p></div>  
</div>
            