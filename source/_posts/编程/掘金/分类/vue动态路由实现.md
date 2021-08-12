
---
title: 'vue动态路由实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2268'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 18:34:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=2268'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p>通常我们在vue项目中都是前端配置好路由的，但在一些项目中我们可能会遇到权限控制，这样我们就涉及到动态路由的设置了。</p>
<h3 data-id="heading-0">动态路由设置一般有两种：</h3>
<p>(1)、简单的角色路由设置： 比如只涉及到管理员和普通用户的权限。通常直接在前端进行简单的角色权限设置</p>
<p>(2)、复杂的路由权限设置： 比如OA系统、多种角色的权限配置。通常需要后端返回路由列表，前端渲染使用</p>
<h4 data-id="heading-1">1、简单的角色路由设置</h4>
<p>（1）配置项目路由权限</p>
<pre><code class="copyable">// router.js
import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/layout'
Vue.use(Router)
let asyncRoutes = [
    &#123;
        path: '/permission',
        component: Layout,
        redirect: '/permission/page',
        alwaysShow: true, 
        name: 'Permission',
        meta: &#123;
            title: 'Permission',
            roles: ['admin', 'editor'] // 普通的用户角色
        &#125;,
        children: [
            &#123;
                path: 'page',
                component: () => import('@/views/permission/page'),
                name: 'PagePermission',
                meta: &#123;
                    title: 'Page',
                    roles: ['editor']  //  editor角色的用户才能访问该页面
                &#125;
            &#125;,
            &#123;
                path: 'role',
                component: () => import('@/views/permission/role'),
                name: 'RolePermission',
                meta: &#123;
                    title: 'Role',
                    roles: ['admin']    //  admin角色的用户才能访问该页面
                &#125;
            &#125;
        ]
    &#125;,
 
]
let router = new Router(&#123;
    mode: 'history',
    scrollBehavior: () => (&#123; y: 0 &#125;),
    routes: asyncRoutes
&#125;)
export default router
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">（2）新建一个公共的asyncRouter.js文件</h4>
<pre><code class="copyable">// asyncRouter.js
//判断当前角色是否有访问权限
function hasPermission(roles, route) &#123;
  if (route.meta && route.meta.roles) &#123;
    return roles.some(role => route.meta.roles.includes(role))
  &#125; else &#123;
    return true
  &#125;
&#125;
// 递归过滤异步路由表，筛选角色权限路由
export function filterAsyncRoutes(routes, roles) &#123;
  const res = [];
  routes.forEach(route => &#123;
    const tmp = &#123; ...route &#125;
    if (hasPermission(roles, tmp)) &#123;
      if (tmp.children) &#123;
        tmp.children = filterAsyncRoutes(tmp.children, roles)
      &#125;
      res.push(tmp)
    &#125;
  &#125;)

  return res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">（3）创建路由守卫：创建公共的permission.js文件，设置路由守卫</h4>
<pre><code class="copyable">import router from './router'
import store from './store'
import NProgress from 'nprogress' // 进度条插件
import 'nprogress/nprogress.css' // 进度条样式
import &#123; getToken &#125; from '@/utils/auth' 
import &#123; filterAsyncRoutes &#125; from '@/utils/asyncRouter.js'

NProgress.configure(&#123; showSpinner: false &#125;) // 进度条配置

const whiteList = ['/login'] 

router.beforeEach(async (to, from, next) => &#123;
    // 进度条开始
    NProgress.start()
     // 获取路由 meta 中的title，并设置给页面标题
    document.title = to.meta.title
    // 获取用户登录的token
    const hasToken = getToken()
    // 判断当前用户是否登录
    if (hasToken) &#123;
        if (to.path === '/login') &#123;
            next(&#123; path: '/' &#125;)
            NProgress.done()
        &#125; else &#123;
            // 从store中获取用户角色
            const hasRoles = store.getters.roles && store.getters.roles.length > 0  
            if (hasRoles) &#123;
                next()
            &#125; else &#123;
                try &#123;
                    // 获取用户角色
                    const roles = await store.state.roles
                    // 通过用户角色，获取到角色路由表
                    const accessRoutes = filterAsyncRoutes(await store.state.routers,roles)
                    // 动态添加路由到router内
                    router.addRoutes(accessRoutes)
                    next(&#123; ...to, replace: true &#125;)
                &#125; catch (error) &#123;
                    // 清除用户登录信息后，回跳到登录页去
                    next(`/login?redirect=$&#123;to.path&#125;`)
                    NProgress.done()
                &#125;
            &#125;
        &#125;
    &#125; else &#123;
        // 用户未登录
        if (whiteList.indexOf(to.path) !== -1) &#123;
            // 需要跳转的路由是否是whiteList中的路由，若是，则直接条状
            next()
        &#125; else &#123;
            // 需要跳转的路由不是whiteList中的路由，直接跳转到登录页
            next(`/login?redirect=$&#123;to.path&#125;`)
            // 结束精度条
            NProgress.done()
        &#125;
    &#125;
&#125;)

router.afterEach(() => &#123;
    // 结束精度条
    NProgress.done()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">（4）在main.js中引入permission.js文件</h4>
<h4 data-id="heading-5">（5）在login登录的时候将roles存储到store中</h4>
<h3 data-id="heading-6">2、复杂的路由权限设置（后端动态返回路由数据）</h3>
<p>（1）配置项目路由文件，该文件中没有路由，或者存在一部分公共路由，即没有权限的路由</p>
<pre><code class="copyable">import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/layout';
Vue.use(Router)
// 配置项目中没有涉及权限的公共路由
export const constantRoutes = [
    &#123;
        path: '/login',
        component: () => import('@/views/login'),
        hidden: true
    &#125;,
    &#123;
        path: '/404',
        component: () => import('@/views/404'),
        hidden: true
    &#125;,
]

const createRouter = () => new Router(&#123;
    mode: 'history',
    scrollBehavior: () => (&#123; y: 0 &#125;),
    routes: constantRoutes
&#125;)
const router = createRouter()

export function resetRouter() &#123;
    const newRouter = createRouter()
    router.matcher = newRouter.matcher
&#125;

export default router
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">（2）新建一个公共的asyncRouter.js文件</h4>
<pre><code class="copyable">// 引入路由文件这种的公共路由
import &#123; constantRoutes &#125; from '../router';
// Layout 组件是项目中的主页面，切换路由时，仅切换Layout中的组件
import Layout from '@/layout';
export function getAsyncRoutes(routes) &#123;
    const res = []
    // 定义路由中需要的自定名
    const keys = ['path', 'name', 'children', 'redirect', 'meta', 'hidden']
    // 遍历路由数组去重组可用的路由
    routes.forEach(item => &#123;
        const newItem = &#123;&#125;;
        if (item.component) &#123;
            // 判断 item.component 是否等于 'Layout',若是则直接替换成引入的 Layout 组件
            if (item.component === 'Layout') &#123;
                newItem.component = Layout
            &#125; else &#123;
            //  item.component 不等于 'Layout',则说明它是组件路径地址，因此直接替换成路由引入的方法
                newItem.component = resolve => require([`@/views/$&#123;item.component&#125;`],resolve)
                
                // 此处用reqiure比较好，import引入变量会有各种莫名的错误
                // newItem.component = (() => import(`@/views/$&#123;item.component&#125;`));
            &#125;
        &#125;
        for (const key in item) &#123;
            if (keys.includes(key)) &#123;
                newItem[key] = item[key]
            &#125;
        &#125;
        // 若遍历的当前路由存在子路由，需要对子路由进行递归遍历
        if (newItem.children && newItem.children.length) &#123;
            newItem.children = getAsyncRoutes(item.children)
        &#125;
        res.push(newItem)
    &#125;)
    // 返回处理好且可用的路由数组
    return res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">（3）创建路由守卫：创建公共的permission.js文件，设置路由守卫</h4>
<pre><code class="copyable">//  进度条引入设置如上面第一种描述一样
import router from './router'
import store from './store'
import NProgress from 'nprogress' // progress bar
import 'nprogress/nprogress.css' // progress bar style
import &#123; getToken &#125; from '@/utils/auth' // get token from cookie
import &#123; getAsyncRoutes &#125; from '@/utils/asyncRouter'

const whiteList = ['/login'];
router.beforeEach( async (to, from, next) => &#123;
    NProgress.start()
    document.title = to.meta.title;
    // 获取用户token，用来判断当前用户是否登录
    const hasToken = getToken()
    if (hasToken) &#123;
        if (to.path === '/login') &#123;
            next(&#123; path: '/' &#125;)
            NProgress.done()
        &#125; else &#123;
            //异步获取store中的路由
            let route = await store.state.addRoutes;
            const hasRouters = route && route.length>0;
            //判断store中是否有路由，若有，进行下一步
            if ( hasRouters ) &#123;
                next()
            &#125; else &#123;
                //store中没有路由，则需要获取获取异步路由，并进行格式化处理
                try &#123;
                    const accessRoutes = getAsyncRoutes(await store.state.addRoutes );
                    // 动态添加格式化过的路由
                    router.addRoutes(accessRoutes);
                    next(&#123; ...to, replace: true &#125;)
                &#125; catch (error) &#123;
                    // Message.error('出错了')
                    next(`/login?redirect=$&#123;to.path&#125;`)
                    NProgress.done()
                &#125;
            &#125;
        &#125;
    &#125; else &#123;
        if (whiteList.indexOf(to.path) !== -1) &#123;
            next()
        &#125; else &#123;
            next(`/login?redirect=$&#123;to.path&#125;`)
            NProgress.done()
        &#125;
    &#125;
&#125;)

router.afterEach(() => &#123;
    NProgress.done()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">（4）在main.js中引入permission.js文件</h4>
<h4 data-id="heading-10">（5）在login登录的时候将路由信息存储到store中</h4>
<pre><code class="copyable">//  登录接口调用后，调用路由接口，后端返回相应用户的路由res.router，我们需要存储到store中，方便其他地方拿取
this.$store.dispatch("addRoutes", res.router);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>到这里，整个动态路由就可以走通了，但是页面跳转、路由守卫处理是异步的，会存在动态路由添加后跳转的是空白页面，这是因为路由在执行next()时，router里面的数据还不存在，此时，你可以通过<code>window.location.reload()</code>来刷新路由</p>
</blockquote>
<h2 data-id="heading-11">后端返回的路由格式：</h2>
<pre><code class="copyable">routerList = [
  &#123;
        "path": "/other",
        "component": "Layout",
        "redirect": "noRedirect",
        "name": "otherPage",
        "meta": &#123;
            "title": "测试",
        &#125;,
        "children": [
            &#123;
                "path": "a",
                "component": "file/a",
                "name": "a",
                "meta": &#123; "title": "a页面", "noCache": "true" &#125;
            &#125;,
            &#123;
                "path": "b",
                "component": "file/b",
                "name": "b",
                "meta": &#123; "title": "b页面", "noCache": "true" &#125;
            &#125;,
        ]
    &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：vue是单页面应用程序，所以页面一刷新数据部分数据也会跟着丢失，所以我们需要将store中的数据存储到本地，才能保证路由不丢失。关于vue页面刷新保存页面状态，可以查看 vue如何在页面刷新时保留状态信息</p>
</blockquote>
<h2 data-id="heading-12">最后</h2>
<blockquote>
<p>公众号：小何成长，佛系更文，都是自己曾经踩过的坑或者是学到的东西</p>
<p>有兴趣的小伙伴欢迎关注我哦，我是：<code>何小玍</code>。大家一起进步鸭</p>
</blockquote></div>  
</div>
            