
---
title: '一文你带快速认识 Vue-Router 路由'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6790e241c3f447e1a842546317b6866e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 23:12:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6790e241c3f447e1a842546317b6866e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>摘要：VueRouter 是 Vue.js 官方的路由管理器。它和 Vue.js 的核心深度集成，可以非常方便的用于 SPA 应用程序的开发。</p>
</blockquote>
<p>本文分享自华为云社区<a href="https://bbs.huaweicloud.com/blogs/277421?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">《Vue-Router路由快速了解与应用》</a>，原文作者：北极光之夜。</p>
<h2 data-id="heading-0">一.速识概念：</h2>
<h3 data-id="heading-1">1. 后端路由：</h3>
<p>1.根据<strong>不同</strong>的用户 URL 请求,<strong>返回不同</strong>的内容,本质上是 URL 请求地址与服务器资源之间的对应关系。</p>
<p>2.但是呢，后端渲染存在<strong>性能问题</strong>。</p>
<h3 data-id="heading-2">2. 前端路由：</h3>
<p>3.所以出现了 <strong>Ajax 前编渲染</strong> ，前端渲染能提高性能，但是不支持浏览器的前进后退操作。</p>
<p>4.这时又出现了 <strong>SPA</strong> (Single Page Application)单页面应用程序，整个网站只有一个页面，内容的变化通过 Ajax <strong>局部更新</strong>实现、同时支持浏览器地址栏的前进和后退操作。</p>
<p>5.SPA 实现原理之一就是基于 URL 地址的 <strong>hash</strong> (hash 的变化会导致浏览器记录访问历史的变化、但是 hash 的变化不会触发新的 URL 请求) 。在实现 SPA 过程中， 其中最核心的技术点就是<strong>前端路由</strong>。</p>
<p>6.<strong>前端路由</strong>就是根据不同的用户事件，显示不同的页面内容。本质就是用户事件与事件处理函数之间的对应关系。</p>
<h3 data-id="heading-3">3.Vue Router：</h3>
<p>这是官方使用文档链接：<br>
<a href="https://router.vuejs.org/zh/guide/#javascript" target="_blank" rel="nofollow noopener noreferrer">router.vuejs.org/zh/guide/#j…</a></p>
<p>Vue Router 是 Vue.js 官方的路由管理器。它和 Vue.js 的核心深度集成，可以非常方便的用于 SPA 应用程序的开发。</p>
<p>它的功能如下：</p>
<p>1.支持 HTML5 历史模式或 hash 模式。2.支持嵌套路由。3.支持路由参数。4.支持编程式路由。5.支持命名路由。</p>
<h2 data-id="heading-4">二.基本使用:</h2>
<h3 data-id="heading-5">前提：</h3>
<p>下面将会以一个 HTML 单页面演示 Vue Router 的基本使用步骤。在 vue 项目里也是一样的原理。当前单页面基本代码：</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="app">


    </div>
    <script>
        const app = new Vue(&#123;
            el:"#app",
            data: &#123;&#125;
        &#125;)
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到什么都没有：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6790e241c3f447e1a842546317b6866e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面开始使用的具体步骤：</p>
<h3 data-id="heading-6">1.引入相关的文件：</h3>
<p>单页面肯定得先导入 vue 文件与 vue-router 文件，这样我们才能够使用路由。</p>
<pre><code class="copyable"><script src="https://unpkg.com/vue/dist/vue.js"></script>
<script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2.添加路由链接：</h3>
<p>以下是一个 vue 提供的标签，默认会被渲染为 a 标签。其中有一个 to 属性，这个 to 属性会被渲染为 href 属性，默认值被渲染为 # 开头的 hash 地址。简单来说就是当用户点击不同时跳转不同内容，而这个标签就是用户要点击的东西，相当于 a 标签嘛。</p>
<pre><code class="copyable"><router-link to="/..." >...</router-link>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给我们的单页面上加一个 page1 和一个 page2 的链接：</p>
<pre><code class="copyable"><div id="app">
       <router-link to="/page1">Page1</router-link>
       <router-link to="/page2">Page2</router-link>
    </div
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">3.添加路由填充位：</h3>
<p>下面这个标签叫路由填充位，就是说未来通过我们的路由规则匹配到的组件，将会被渲染到 router-view 所在位置。简单来说，就是用户点击路由链接，那得跳转内容吧，我们知道的是肯定不是整个页面都跳转，只是页面内相关的局部发生内容改变，这个局部就是 router-view 所在显示的区域。</p>
<pre><code class="copyable"><router-view></router-view>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给我们的页面添加：</p>
<pre><code class="copyable"> <div id="app">
        <router-link to="/page1">Page1</router-link>
       <router-link to="/page2">Page2</router-link>
       <router-view></router-view>
    </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">4.定义路由组件：</h3>
<p>既然要显示不同的内容，那肯定是用一个组件保存一份内容。下面我们给单页面定义 page1，page2 这两个组件。</p>
<pre><code class="copyable"><script>
        const Page1 = &#123;
            template: '<h1>我是北极光之夜1号</h1>'
        &#125;
        const Page2 = &#123;
            template: '<h1>我是北极光之夜2号</h1>'
        &#125;
        const app = new Vue(&#123;
            el:"#app",
            data: &#123;&#125;
        &#125;)
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">5.配置路由规则井创建路由实例：</h3>
<p>routes 是路由规则数组。每个路由规则都是一个配置对象， 其中至少包含 path 和 component 两个属性，path 表示当前路由规则匹配的 hash 地址，component 表示当前路由规则对应要展示的组件。简单来说就是你点击那个链接对应的地址要对应的是哪个内容的组件。path 跟 router-link 标签里的地址要一样，别写错了。</p>
<pre><code class="copyable">const router = new VueRouter(&#123;
            routes: [
                &#123;path:'/page1',component:Page1 &#125;,
                &#123;path:'/page2',component:Page2 &#125;
            ]
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">6.把路由挂载到 Vue 根实例中：</h3>
<p>为了能够让路由规则生效，必须把路由对象挂载到 vue 实例对象上。</p>
<pre><code class="copyable">const app = new Vue(&#123;
            el:"#app",
            data: &#123;&#125;,
            router
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">7.效果与单页面代码：</h3>
<p>以上我们就大工告成~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7566b88cdf2646bab565388f038d4b83~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面的完整代码：</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 导入vue文件 -->
    <script src="https://unpkg.com/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>
</head>
<body>
    <div id="app">
       <router-link to="/page1">Page1</router-link>
       <router-link to="/page2">Page2</router-link>
       <router-view></router-view>
    </div>
    <script>
        const Page1 = &#123;
            template: '<h1>我是北极光之夜1号</h1>'
        &#125;
        const Page2 = &#123;
            template: '<h1>我是北极光之夜2号</h1>'
        &#125;
        const router = new VueRouter(&#123;
            routes: [
                &#123;path:'/page1',component:Page1 &#125;,
                &#123;path:'/page2',component:Page2 &#125;
            ]
        &#125;)
        const app = new Vue(&#123;
            el:"#app",
            data: &#123;&#125;,
            router
        &#125;)
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">三.路由重定向：</h2>
<p>路由重定向指的是用户在访问地址 A 的时候,强制用户跳转到地址 B，从而展示特定的组件页面。通过路由规则的 redirect 属性,指定一个新的路由地址，可以很方便地设置路由的重定向。</p>
<pre><code class="copyable">&#123;path:'/..',redirect: '/...'&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 path 表示重定向的原地址，redirect 表示新地址。</p>
<p>比如第二大点的案例中，刚打开的页面如下，在根目录，但我们想一进入就显示 page1，那就给根目录重定向。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/376ac537f9c14d4ea93ee8abc1f19fea~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改路由规则如下：</p>
<pre><code class="copyable">const router = new VueRouter(&#123;
            routes: [             
                &#123;path:'/page1',component:Page1 &#125;,
                &#123;path:'/page2',component:Page2 &#125;,
                &#123;path:'/',redirect:'/page1'&#125;
            ]
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看效果，我没点击就默认进入 page1 了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7cef344cb8b4d0ba1f74473155eb959~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">四.嵌套路由：</h2>
<p>功能如下：</p>
<p>1. 点击父级路由链接显示模板内容。</p>
<p>2. 模板内容中又有子级路由链接。</p>
<p>3. 点击子级路由链接显示子级模板内容。</p>
<p>比如我们改进第二大点的案例，当点击 page2 显示 page2 内容时，page2 里又有两个子路由连接，star 和 moon，当点击其中一个链接时又能显示对应的 star 或 moon 内容。</p>
<h3 data-id="heading-15">1.首先给 page2 组件添加两个子路由链接：</h3>
<pre><code class="copyable">const Page2 = &#123;
            template: `
                 <div>
                 <h1>我是北极光之夜2号</h1>
                 <hr/>
                 <router-link to="/page2/star">Star</router-link>
                 <router-link to="/page2/moon">Moon</router-link>
                 <hr/>
                 </div>`
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时页面也把显示子路由链接出来了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6ed619f0315490e977f46beda0a738d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">2.给两个子路由链接添加路由填充位：</h3>
<pre><code class="copyable">const Page2 = &#123;
const Page2 = &#123;
            template: `
                 <div>
                 <h1>我是北极光之夜2号</h1>
                 <hr/>
                 <router-link to="/page2/star">Star</router-link>
                 <router-link to="/page2/moon">Moon</router-link>
                 <hr/>
                 <router-view></router-view>
                 </div>`
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">3.设置两个子组件 star 与 moon 的内容：</h3>
<pre><code class="copyable"> const Star = &#123;
            template: '<h2>我是北极光之夜2号下的star</h2>'
        &#125;
        const Moon = &#123;
            template: '<h2>我是北极光之夜2号下的Moon</h2>'
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">4.配置路由规则：</h3>
<p>page2 的规则除了 path 和 component 属性外，再添加一个 <strong>children</strong> 属性，这个属性以数组表示，<strong>数组里存放其子路由的规则</strong>，其规则也是一样的，套娃套娃。</p>
<pre><code class="copyable">const router = new VueRouter(&#123;
            routes: [
                &#123;path:'/page1',component:Page1 &#125;,
                &#123;
                    path:'/page2',
                    component:Page2, 
                    children: [
                        &#123;path: '/page2/star',component:Star&#125;,
                        &#123;path: '/page2/moon',component:Moon&#125;
                    ]
                &#125;
            ]
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">5.效果与单页面代码：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eab82c18ac204778acea1817c103ac22~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>完整代码：</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 导入vue文件 -->
    <script src="https://unpkg.com/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>
</head>
<body>
    <div id="app">
       <router-link to="/page1">Page1</router-link>
       <router-link to="/page2">Page2</router-link>
       <router-view></router-view>
    </div>
    <script>
        const Page1 = &#123;
            template: '<h1>我是北极光之夜1号</h1>'
        &#125;
        const Page2 = &#123;
            template: `
                 <div>
                 <h1>我是北极光之夜2号</h1>
                 <hr/>
                 <router-link to="/page2/star">Star</router-link>
                 <router-link to="/page2/moon">Moon</router-link>
                 <hr/>
                 <router-view></router-view>
                 </div>`
        &#125;
        const Star = &#123;
            template: '<h2>我是北极光之夜2号下的star</h2>'
        &#125;
        const Moon = &#123;
            template: '<h2>我是北极光之夜2号下的Moon</h2>'
        &#125;
        const router = new VueRouter(&#123;
            routes: [
                &#123;path:'/page1',component:Page1 &#125;,
                &#123;
                    path:'/page2',
                    component:Page2, 
                    children: [
                        &#123;path: '/page2/star',component:Star&#125;,
                        &#123;path: '/page2/moon',component:Moon&#125;
                    ]
                &#125;
            ]
        &#125;)
        const app = new Vue(&#123;
            el:"#app",
            data: &#123;&#125;,
            router
        &#125;)
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">五. 动态路由匹配：</h2>
<h3 data-id="heading-21">1.动态匹配路由基本使用：</h3>
<p>如果某些路由规则的一部分是一样的，只有另一部分是动态变化的，那我们可以把这些动态变化的部分形成路由参数，这些参数就叫做动态路由匹配。 </p>
<p>简单来说，你先看下面这些路由链接，它们都有/page/，就是后面不一样：</p>
<pre><code class="copyable"><router-link to="/page/1">Page1</router-link>
   <router-link to="/page/2">Page2</router-link>
   <router-link to="/page/3">Page3</router-link>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那该咋配置路由呢？这样吗：</p>
<pre><code class="copyable">const router = new VueRouter(&#123;
            routes: [
                &#123;path:'/page/1',component:Page&#125;,
                &#123;path:'/page/2',component:Page&#125;,
                &#123;path:'/page/3',component:Page&#125;
            ]
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样万一有很多一个个写岂不是太麻烦了，所以引入参数，在动态改变的部分定义为参数，参数前面有一个冒号,那上面可简写成如下，动态部分设为参数 <strong>：id</strong> 。</p>
<pre><code class="copyable">const router = new VueRouter(&#123;
            routes: [
                &#123;path:'/page/:id',component:Page &#125;,
            ]
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件可以通过以下语法获取当前路由的参数：</p>
<pre><code class="copyable">$router.params.参数名称
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好，再次修改第二大点的案例完成动态路由匹配：</p>
<p>1.定义路由链接：</p>
<pre><code class="copyable"><div id="app">
   <router-link to="/page/1">Page1</router-link>
   <router-link to="/page/2">Page2</router-link>
   <router-link to="/page/3">Page3</router-link>
   <router-view></router-view>
   </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.动态配置路由，参数 id：</p>
<pre><code class="copyable">const router = new VueRouter(&#123;
    routes: [
        &#123;path:'/page/:id',component:Page1 &#125;,
    ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.设置组件内容，并显示当前路由的参数：</p>
<pre><code class="copyable">const Page1 = &#123;
    template: '<h1>我是北极光之夜1号,当前id为：&#123;&#123;$route.params.id&#125;&#125;</h1>'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c456c35d5d0d4eecbb648fdc00a7ebc2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-22">2.路由组件传参：</h3>
<p>上面的 $route 与对应路由形成高度耦合，不够灵活啊，所以可以使用 props 将组件和路由解耦。简单来说，好像也没什么说的，直接看下面实例就能理解了。</p>
<h3 data-id="heading-23">2.1 当 props 为布尔类型：</h3>
<pre><code class="copyable">const router = new VueRouter(&#123;
            routes: [
 // 设置props，如果props为true，router.params会被设置为组件属性
                &#123;path:'/page/:id',component:Page1,props: true &#125;,
            ]
        &#125;)  
              
        const Page1 = &#123;
// 这时就通过props接收参数，快速简洁的接收参数id和使用它
                    props: ['id'],
                    template: '<h1>我是北极光之夜1号,当前id为：&#123;&#123;id&#125;&#125;</h1>'
                &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>能达到一样的效果，且更灵活了，上面记得反过来，先定义组件才配置路由规则，只是为了直观才这样写：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c258dc5eb2fd4fe194d5e3c9013469a2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-24">2.2 当 props 为对象类型：</h3>
<pre><code class="copyable">const Page1 = &#123;
        // 这时就通过props接收参数，快速简洁的接收参数对象 并显示
                props: ['name','age'],
                template: `<h1>我是北极光之夜1号,当前id为：&#123;&#123;id&#125;&#125;
                            <hr/>
                           姓名为：&#123;&#123;name&#125;&#125; ，年龄为：&#123;&#123;age&#125;&#125; </h1>`
                &#125;
             const router = new VueRouter(&#123;
                routes: [
            // props为一个参数对象，它会原样设置为组件属性，
            // 里面的自定义的参数都能传过去，但是id传不了了
                    &#123;path:'/page/:id',component:Page1 , props: &#123;name:'auroras',age: 18&#125; &#125;
                ]
             &#125;)  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果，对象 props 对象里的能获取，id 就不行了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1b16d94c8d7494d9a058c806762f4a6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-25">2.3 当 props 为函数类型：</h3>
<p>这个就什么都能获取。</p>
<pre><code class="copyable">const Page1 = &#123;
// 这时就通过props接收参数，快速简洁的接收参数
        props: ['name','age','id'],
        template: `<h1>我是北极光之夜1号,当前id为：&#123;&#123;id&#125;&#125;
                    <hr/>
                   姓名为：&#123;&#123;name&#125;&#125; ，年龄为：&#123;&#123;age&#125;&#125; </h1>`
        &#125;
     const router = new VueRouter(&#123;
        routes: [
    // props为函数，这个对象接收router对象为自己形参，
    // 里面的自定义的参数和id都能传过去
            &#123;path:'/page/:id',
            component:Page1 , 
            props: router => (&#123;id: router.params.id,name:'auroras',age: 18&#125;) &#125;
        ]
     &#125;)  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f90965a72f6a4bf9a2bad64edd665320~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当前完整代码：</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 导入vue文件 -->
    <script src="https://unpkg.com/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>
</head>
<body>
    <div id="app">
        <router-link to="/page/1">Page1</router-link>
        <router-link to="/page/2">Page2</router-link>
        <router-link to="/page/3">Page3</router-link>
        <router-view></router-view>
        </div>   
         <script>
            const Page1 = &#123;
        // 这时就通过props接收参数，快速简洁的接收参数对象 
                props: ['name','age','id'],
                template: `<h1>我是北极光之夜1号,当前id为：&#123;&#123;id&#125;&#125;
                            <hr/>
                           姓名为：&#123;&#123;name&#125;&#125; ，年龄为：&#123;&#123;age&#125;&#125; </h1>`
                &#125;
             const router = new VueRouter(&#123;
                routes: [
            // props为函数，这个对象接收router对象为自己形参，
            // 里面的自定义的参数和id都能传过去
                    &#123;path:'/page/:id',
                    component:Page1 , 
                    props: router => (&#123;id: router.params.id,name:'auroras',age: 18&#125;) &#125;
                ]
             &#125;)  
        const app = new Vue(&#123;
            el:"#app",
            data: &#123;&#125;,
            router
        &#125;)
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">六.Vue-Router 命名路由：</h2>
<p>为更加方便的表示路由的路径，可以给路由规则起一个别名，即为“命名路由”。 </p>
<p>继续改进上面的案例讲解用法：</p>
<p>1.首先给路由规则加一个 name 属性，这个就是别名：</p>
<pre><code class="copyable">const router = new VueRouter(&#123;
    routes: [
        &#123;
        name: 'user',
        path:'/page/:id',
        component:Page1 , 
        props: router => (&#123;id: router.params.id,name:'auroras',age: 18&#125;) &#125;
    ]
 &#125;)  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.在路由链接中使用：</p>
<pre><code class="copyable"><div id="app">
    <router-link :to="&#123;name:'user',params: &#123;id: 1&#125;&#125;">Page1</router-link>
    <router-link to="/page/2">Page2</router-link>
    <router-link to="/page/3">Page3</router-link>
    <router-view></router-view>
    </div>   
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们把第一个路由链接改进，to 前面加上冒号，其中 name 表示匹配的是哪个路由规则，params 表示要传递的参数，看下面是一样的效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee69ed133c524e66afc72d41e673241f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-27">七.编程式导航：</h2>
<p>1. 声明式导航：首先声明式导航是指用户通过点击链接完成导航的方式，比如点击 a 标签或者路由链接这些完成的跳转。</p>
<p>2. 编程式导航：编程式导航就是说跳转是因为我点击它，它不是链接，但是它在 JavaScript 里调用了某个 API 也实现了跳转。</p>
<p>3. 常用的编程式导航 API 如下：</p>
<pre><code class="copyable">this.$router.push('要跳转的hash地址')
this.$router.go(n)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>push 里直接放要跳转的哈希地址，go 方法实现前进和后退，n 代表数组，若 n 为 1 代表在历史记录中前进一位，-1 代表在历史记录中后退一位。</p>
<h3 data-id="heading-28">1. this.$router.push(’ ')：</h3>
<p>重写一个案例，有 page1、page2、page3 三个路由链接，而在 page3 里有一个按钮，这个按钮的作用是点击后返回显示 page1 的内容。这个按钮可不是声明式导航里的链接，就是一个按钮。</p>
<p>1.定义普通的路由链接：</p>
<pre><code class="copyable"> <div id="app">
    <router-link :to="/page/1">Page1</router-link>
    <router-link to="/page/2">Page2</router-link>
    <router-link to="/page/3">Page3</router-link>
    <router-view></router-view>
    </div>   
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.定义 3 个组件内容，其中给 page3 组件里放一个按钮，并绑定点击事件，在事件里通过 API 导航到 page1：</p>
<pre><code class="copyable">const Page1 = &#123;
    template: `<h1>我是北极光之夜1号</h1>`
&#125;
const Page2 = &#123;
    template: `<h1>我是北极光之夜2号</h1>`
&#125;
const Page3 = &#123;
    template: `<div>
            <h1>我是北极光之夜3号</h1>
            <button @click="goPage1">返回page1</button>
               </div>`,
    methods: &#123;
        goPage1()&#123;
            this.$router.push('/page/1')
        &#125;
    &#125;,
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.路由规则：</p>
<pre><code class="copyable">const router = new VueRouter(&#123;
                routes: [
                    &#123;path:'/page/1',component: Page1&#125;,
                    &#123;path:'/page/2',component: Page2&#125;,
                    &#123;path:'/page/3',component: Page3&#125;
                ]
             &#125;)  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​4.看效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b377b7304bfa4cc8aa5e78e34b9b2fec~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>5.完整代码：</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 导入vue文件 -->
    <script src="https://unpkg.com/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>
</head>
<body>
    <div id="app">
        <router-link to="/page/1">Page1</router-link>
        <router-link to="/page/2">Page2</router-link>
        <router-link to="/page/3">Page3</router-link>
        <router-view></router-view>
    </div>   
         <script>
            const Page1 = &#123;
                template: `<h1>我是北极光之夜1号</h1>`
            &#125;
            const Page2 = &#123;
                template: `<h1>我是北极光之夜2号</h1>`
            &#125;
            const Page3 = &#123;
                template: `<div>
                        <h1>我是北极光之夜3号</h1>
                        <button @click="goPage1">返回page1</button>
                           </div>`,
                methods: &#123;
                    goPage1()&#123;
                        this.$router.push('/page/1')
                    &#125;
                &#125;,
                
            &#125;
             const router = new VueRouter(&#123;
                routes: [
                    &#123;path:'/page/1',component: Page1&#125;,
                    &#123;path:'/page/2',component: Page2&#125;,
                    &#123;path:'/page/3',component: Page3&#125;
                ]
             &#125;)  


        const app = new Vue(&#123;
            el:"#app",
            data: &#123;&#125;,
            router
        &#125;)
    </script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不止 href 路径，还可以有以下操作：</p>
<pre><code class="copyable">//字符串形式（路径的名称）
router.push('/page1')
//对象的形式
router.push(&#123;path: '/page1'&#125;)
//也可以传递参数，命名的路由
router.push(&#123;name: '/page1',parmas:&#123;id: 1&#125;&#125;)
//带查询参数，变成  /page1?p=id 
//这个挺实用的，比如在某些音乐网页，点击歌单后要导航到另一个该歌单详细界面，此时要带id，详细界面靠此id重新发送请求，请求详细信息
router.push(&#123;parh: '/page1',query:&#123;p: 'id' &#125;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">2. this.$router.go(n)：</h3>
<p>改进第 1 小点的案例，当我 page3 跳到 page1 时，page1 里又有一个返回的按钮。我们把 n 设置为-1，他就会在历史记录中后退一位，后退一位就是 page3.修改 page1 组件内容：</p>
<pre><code class="copyable">  const Page1 = &#123;
                template: `<div>
                        <h1>我是北极光之夜1号</h1>
                        <button @click="goBack">返回</button>
                           </div>`,
                  methods: &#123;
                    goBack()&#123;
                        this.$router.go(-1)
                    &#125;
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29a5e0b2263044e4adf9222c9314f8fe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://bbs.huaweicloud.com/blogs?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">点击关注，第一时间了解华为云新鲜技术~</a></p></div>  
</div>
            