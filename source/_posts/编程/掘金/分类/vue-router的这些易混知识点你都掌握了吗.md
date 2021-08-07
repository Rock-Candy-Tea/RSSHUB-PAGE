
---
title: 'vue-router的这些易混知识点你都掌握了吗'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9a0e3143e43454290de037ee03995af~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 00:13:50 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9a0e3143e43454290de037ee03995af~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第3天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a>” 。</p>
<h3 data-id="heading-0">1. Vue中router和routes和route的区别</h3>
<p>在Vue中，router指向的是大路由，routes是路由配置数组， route指向的是当前活跃的路由。下面我们详细了解一下这三者。</p>
<p><strong>1.1 router</strong>：是VueRouter的一个实例对象，通过Vue.use(VueRouter)和VueRouter构造函数得到一个router的实例对象。例如<code>$router</code>,它是一个全局路由对象，包含了路由跳转的方法、钩子函数等。在组件内可通过 <code>this.$router</code> 访问整个<strong>路由器</strong>。</p>
<p>在项目中的应用有：</p>
<ul>
<li>router的index.js</li>
</ul>
<pre><code class="copyable">import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)
const router = new VueRouter(&#123;
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>路由导航守卫router.beforeEach和router.afterEach</li>
</ul>
<pre><code class="copyable">router.beforeEach((to, from, next) => &#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>关于$router</li>
</ul>
<p><code>$router</code>常用于编程式导航中，首先打印一下$router的内容。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9a0e3143e43454290de037ee03995af~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>this.$router.push方法</p>
<p>该方法的参数可以是一个字符串，也可以是一个描述地址的对象。</p>
<pre><code class="copyable">// 字符串 
this.$router.push('home') ;

//对象 
this.$ruter.push(&#123;path:'home'&#125;) 

//命名路由 
this.$router.push(&#123;name:'Detail',params:&#123;id:1&#125;&#125;) 

//携带参数
this.$router.push(&#123;
  path: '/product/edit-basic-info',
  query: &#123; from_type: 'add' &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>this.$router.replace方法</p>
<p><code>this.$router.push</code>和<code>this.$router.replace</code>方法很像，写法是一样的，但是实际的效果是不一样的。push是向history里添加新记录，而replace是直接将当前浏览器history记录替换掉。</p>
<ul>
<li>用push方法，页面A跳转到页面B，使用浏览器的后退可以回到页面A。</li>
<li>用replace方法，页面1被替换成页面B，使用浏览器的后退，就回不到页面A，只能回到页面B的前一页面。</li>
</ul>
<p>在项目中的应用场景常用于权限验证，验证之后不想让用户回退到之前的页面，比如:
购物车页面需要用户登录，如果用户没有登录即跳转到登录页面，登录之后使用replace回到购物车页面，当然也可以使用router.go(-1)方法回退到上一页面。</p>
</li>
</ul>
<p><strong>1.2 routes</strong>：是路由的集合，类型是一个数组，用来配置多个route路由对象。在项目中的应用如下：</p>
<pre><code class="copyable">const routes = [
  &#123;
    path: '/login',
    name: 'Login',
    component: AccountLogin,
    hidden: true
  &#125;,
  &#123;
    path: '/',
    component: Home,
    redirect: '/product/list',
    meta: &#123;
      // pageTitle: 'xxxxx管理系统'
    &#125;,
    children: [
      &#123;
        path: '/product/list',
        name: 'ProductManagement',
        component: ProductManagement,
        redirect: '/product/list',
        meta: &#123;
          title: '产品管理',
          icon: 'iconfont icon-chanpinguanli',
          // pageTitle: 'xxxxx管理系统',
          dropDown: true
        &#125;
    ]
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1.3 route</strong>:是路由信息对象，每一个路由都会有一个route对象，是一个局部对象，例如：$route指的就是当前路由对象。route包含path,params,hash,query,fullPath,matched,name等路由信息参数。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7566bd724f2407ca2371f70a69aad3d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
首先简单介绍下常用的路由对象属性，方便之后的应用。在组件内可以通过<code>this.$route</code>(切记切记不是<code>this.$router</code>哦!)进行访问。
\</p>
<ul>
<li><code>$route.path</code> 类型: <code>string</code>字符串，对应当前路由的路径，总是解析为绝对路径，如 <code>"/shop/layout"</code>。</li>
<li><code>$route.params</code> 类型: <code>Object</code> 一个 key/value 对象，包含了动态片段和全匹配片段，如果没有路由参数，就是一个空对象。</li>
<li><code>$route.query</code> 类型: <code>Object</code> 一个 key/value 对象，表示 URL 查询参数。例如，对于路径 <code>/detail?id=1</code>，则有 <code>this.$route.query.id == 1</code>，如果没有查询参数，则是个空对象。</li>
<li><code>$route .name</code> 类型: <code>string</code>字符串， 当前路由的名称，如果有的话。这里建议最好给每个路由对象命名，方便以后编程式导航使用。特别要注意的是name必须唯一!</li>
<li><code>$route.hash</code> 类型: <code>string</code> 当前路由的 hash 值 (带 <code>#</code>) ，如果没有 hash 值，则为空字符串。</li>
<li><code>$route.fullPath</code> 类型: <code>string</code> 完成解析后的 URL，包含查询参数和 hash 的完整路径。</li>
<li><code>$route.matched</code> 类型: <code>Array<RouteRecord></code> 一个数组，包含当前路由的所有嵌套路径片段的路由记录。路由记录就是 <code>routes</code> 配置数组中的对象副本 (还有在 <code>children</code> 数组)。$route.redirectedFrom 如果存在重定向，即为重定向来源的路由的名字。</li>
</ul>
<p>在组件内可通过<code>this.$route</code> 访问 <strong>当前路由</strong>。</p>
<pre><code class="copyable">this.$route.path
this.$route.query
this.$route.params
this.$route.meta
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2. vue-router传参</h3>
<ul>
<li>params</li>
</ul>
<p>参数不会显示在URL地址栏中，当用户刷新页面后，params参数就会被清空。只能使用name，不能使用path。在编程式导航中<code>path</code>和<code>params</code>是不能同时生效的，使用了path，params就会被忽略掉。所以使用对象写法进行params传参时，可以使用<code>path</code>加冒号<code>:</code>，或者通过name和params进行传参。</p>
<pre><code class="copyable">// 传递参数
this.$router.push(&#123;
    name:'Detail',
    params:&#123;
        id:1
    &#125;
&#125;)
this.$router.push(&#123;
    path:'/detail',
    params:&#123;id:1&#125; //此时这个params是无效的
&#125;)
// 接收参数
let id=this.$route.params.id
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>query</li>
</ul>
<p>参数会显示在路URl地址栏中，用户刷新页面之后参数也不会丢失，可以使用name，也可以使用path。</p>
<pre><code class="copyable">// 传递参数
this.$router.push(&#123;
    name:'Detail',
    query:&#123;
        id:1
    &#125;
&#125;)
this.$router.push(&#123;
    path:'/detail:id',
&#125;)
this.$router.push(&#123;
    path:'/detail',
    query:&#123;
        id:1
    &#125;
&#125;)
// 接收参数
let id=this.$route.query.id
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. vue-router响应路由参数的变化</h3>
<p>在用动态路由匹配时，例如从/detail/1到detail/2,两个路由都渲染同一个组件，原来的组件实例会被复用，此时如果想在路由改变时做些什么操作，或者想对参数的变化做出响应的话，我们可以通过监听$route来实现这个需求。</p>
<ul>
<li>用watch监测</li>
</ul>
<pre><code class="copyable">watch:&#123;
    $route(to,from)&#123;
        console.log(to,from)
        // TODO SOMETHING
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>组件内导航钩子函数</li>
</ul>
<pre><code class="copyable">beforeRouteUpdate(to,from,next)&#123;
    console.log(to,from,next)
    // TODO SOMETHING
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4. beforeRouteEnter与this</h3>
<p>组件的导航守卫中<code>beforeRouteEnter</code>守卫不能通过<code>this</code>访问组件实例，因为守卫在导航确认前被调用，因此即将登场的新组建还没有被创建。可以通过传一个回调给<code>next</code>来访问组件实例，在导航被确认的时候执行回调，并且把组件实例作为回调方法的参数。</p>
<pre><code class="copyable">beforeRouteEnter(to, from, next) &#123;
    next(vm => &#123;
      //vm.fromRoute即this.fromRoute
      vm.fromRoute = from
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5. 打开新的窗口</h3>
<p>在项目中，我们的应用是一个单页面应用，有时某个页面想要以新窗口的方式打开，我们就可以使用下面的方式实现。</p>
<ul>
<li>第一种方式</li>
</ul>
<pre><code class="copyable">const &#123; href &#125; = this.$router.resolve(&#123;
path:'/detail'
query:&#123;id:'1'&#125;
&#125;)
window.open(href, '_blank')
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第二种方式</li>
</ul>
<pre><code class="copyable"><router-link target="_blank" :to="&#123;path:'/detail',query:&#123;id:'1'&#125;&#125;">打开新页面</router-link>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第三种方式</li>
</ul>
<pre><code class="copyable"><a :href="`http://$&#123;domain&#125;`" target="_black">打开新页面</a>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            