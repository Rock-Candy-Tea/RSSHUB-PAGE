
---
title: '华为云POC的权限控制是如何做的？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9aa64d4524774dfaac3202547f04c244~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 05:23:37 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9aa64d4524774dfaac3202547f04c244~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近一段时间一直投入于对接合作伙伴的POC项目，虽然不是主要的开发人员，但是我需要对整个项目进行把控，涉及到的一些核心功能点也需要我去做一个把关。我们这边需要做一个OCR 文字识别的自定义模板配置平台，本不涉及到用户权限这块的内容，奈何客户爸爸执意要加，那好吧，我们就来做一个权限控制吧......</p>
<h2 data-id="heading-0">权限控制设计</h2>
<p>其实大体上权限设计都是通过前后台协作一起完成，这个过程我们细致的分为：api访问权限控制 和 页面权限控制，进一步的细粒度区分，页面权限控制又包含页面是否能访问、页面中的按钮权限等等。我们一起看看这块功能的实现吧。</p>
<h2 data-id="heading-1">api 访问权限控制</h2>
<p>实际上就是对用户信息的校验。在用户登录时服务器需要给前台返回一个Token，以后前台每次调用接口时都需要带上这个Token，服务端获取到这个Token后进行比对，如果通过则可以访问。现有的通常做法就是在登陆成功之后将后台返回的 Token  存储在前端缓存中，例如 sessionStorage，在请求时将 Token 取出来放在请求头 headers 中传给后台。下图以一个正常的请求数据接口作为示例代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.httpRequest(&#123;
          <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,
          <span class="hljs-attr">url</span>: <span class="hljs-string">'test/query?id=llz'</span>,
          <span class="hljs-attr">withCredentials</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">headers</span>: &#123;
            <span class="hljs-attr">token</span>: sessionStorage.getItem(<span class="hljs-string">'tokenKey'</span>)   <span class="hljs-comment">// 每次请求时都在headers 塞入 Token 信息</span>
          &#125;
        &#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
          <span class="hljs-comment">//请求成功后的操作</span>
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后来axios 中可以在拦截器中直接塞入，作为全局传入，方便了很多（注意此时的Token 信息是同vuex 缓存中取到的，我们将在下一步展开）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//main.js  </span>

<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>

<span class="hljs-comment">// 实例化Axios，并进行超时设置</span>
<span class="hljs-keyword">const</span> instance = axios.create(&#123;
    <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span>
&#125;)
axios.defaults.baseURL = <span class="hljs-string">'https://api.xxx.com'</span>;

<span class="hljs-comment">// 每次请求都为http头增加Authorization字段，其内容为token;</span>
instance.interceptors.request.use(
    <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (store.state.user.token) &#123;
            config.headers.Authorization = <span class="hljs-string">`token <span class="hljs-subst">$&#123;store.state.user.token&#125;</span>`</span>;  <span class="hljs-comment">// vuex 缓存的Token信息塞入请求头</span>
        &#125;
        <span class="hljs-keyword">return</span> config
    &#125;,
    <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(err)
    &#125;
);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> instance
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">页面权限控制</h2>
<p>我们针对页面访问权限展开讨论，我们希望实现一个效果：只显示当前用户能访问的权限内的菜单，当用户通过URL强制访问会直接进入 404 页面。针对此效果我们首先要做的就是配置好路由表信息。因为涉及到有些页面需要访问权限，有些页面不需要访问权限，所以我们将登录、404、维护等非权限操作页面写在默认路由，将其他权限操作页面写到一个变量中。（404 页面一定要最后加载，如果放在 constantRouterList 一同声明了404，后面的所以页面都会被拦截到404）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// router/index.js</span>

<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'@/App'</span>
Vue.use(Router);

<span class="hljs-comment">// 默认不需要权限的页面</span>
<span class="hljs-keyword">const</span> constantRouterList = [&#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'登录'</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> <span class="hljs-built_in">require</span>([<span class="hljs-string">'@/components/login'</span>], resolve)
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/index'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'主页'</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> <span class="hljs-built_in">require</span>([<span class="hljs-string">'@/components/index'</span>], resolve)
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/template'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'模板页面'</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> <span class="hljs-built_in">require</span>([<span class="hljs-string">'@/components/Template/template'</span>], resolve)
    &#125;
]

<span class="hljs-comment">// 注册路由</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> Router(&#123;
  <span class="hljs-attr">routes</span>: constantRouterList
&#125;);

<span class="hljs-comment">// 需要权限控制的页面</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> asyncRouterList = [
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/resource'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Resource'</span>,
        <span class="hljs-attr">meta</span>: &#123;
            <span class="hljs-attr">permission</span>: []
        &#125;,
        <span class="hljs-attr">component</span>: <span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> <span class="hljs-built_in">require</span>([<span class="hljs-string">'@/components/Resource/resource'</span>], resolve)
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Log'</span>,
        <span class="hljs-attr">component</span>: App,
        <span class="hljs-attr">children</span>: [&#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">'/userLog'</span>,
                <span class="hljs-attr">name</span>: <span class="hljs-string">'UserLog'</span>,
                <span class="hljs-attr">meta</span>: &#123;
                    <span class="hljs-attr">permission</span>: []
                &#125;,
                <span class="hljs-attr">component</span>: <span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> <span class="hljs-built_in">require</span>([<span class="hljs-string">'@/components/Log/userLog'</span>], resolve),
            &#125;,
            &#123;
                <span class="hljs-attr">path</span>: <span class="hljs-string">'/operatingLog'</span>,
                <span class="hljs-attr">name</span>: <span class="hljs-string">'operatingLog'</span>,
                <span class="hljs-attr">meta</span>: &#123;
                    <span class="hljs-attr">permission</span>: []
                &#125;,
                <span class="hljs-attr">component</span>: <span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> <span class="hljs-built_in">require</span>([<span class="hljs-string">'@/components/Log/operatingLog'</span>], resolve),
            &#125;,
        ]
    &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面访问的的大致流程我们可以用一下流程图表示：</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph LR
用户登录 --> 获取用户的信息并缓存 --> 根据用户的权限渲染对应权限的菜单 --> 点击菜单进入到制定权限页面 
</code></pre>
<p>通过请求后台接口，我们拿到所有的权限数据并将数据缓存在 vuex 中，然后再利用返回的数据匹配之前写的异步路由表 asyncRouterList，最终得到实际路由表。下面是 vuex 中的缓存数据的逻辑代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// store/index.js</span>

<span class="hljs-keyword">import</span> Axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex);
<span class="hljs-keyword">const</span> axios = Axios.create();

<span class="hljs-keyword">const</span> state = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'login'</span>,
    <span class="hljs-attr">list</span>: []
&#125;;

<span class="hljs-keyword">const</span> getters = &#123;&#125;;

<span class="hljs-keyword">const</span> mutations = &#123;
    <span class="hljs-attr">setMode</span>: <span class="hljs-function">(<span class="hljs-params">state, data</span>) =></span> &#123;
        state.mode = data
    &#125;,
    <span class="hljs-attr">setList</span>: <span class="hljs-function">(<span class="hljs-params">state, data</span>) =></span> &#123;
        state.list = data
    &#125;
&#125;;

<span class="hljs-keyword">const</span> actions = &#123;
    <span class="hljs-comment">// 获取权限列表</span>
    <span class="hljs-function"><span class="hljs-title">getPermission</span>(<span class="hljs-params">&#123;commit&#125;</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            axios(&#123;
                <span class="hljs-attr">url</span>: <span class="hljs-string">'/xxx/getInfo?id='</span> + sessionStorage.getItem(<span class="hljs-string">'privId'</span>),
                <span class="hljs-attr">methods</span>: <span class="hljs-string">'get'</span>,
                <span class="hljs-attr">headers</span>: &#123;
                    <span class="hljs-attr">token</span>: sessionStorage.getItem(<span class="hljs-string">'token'</span>),
                &#125;
            &#125;).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
                <span class="hljs-comment">// 存储权限列表</span>
                commit(<span class="hljs-string">'setList'</span>, res.data);
                resolve(res.data);
            &#125;).catch(<span class="hljs-function">() =></span> &#123;
                reject()
            &#125;)
        &#125;)
    &#125;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    state,
    mutations,
    actions,
    getters
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们刚才说过需要将后台数据和前端的异步路由对象进行匹配，其实这个过程就是一个路由动态加载的过程，此处我们提供一个路由匹配的函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// router/index.js</span>

<span class="hljs-comment">/**
 * 根据权限匹配路由
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;array&#125;</span> </span>permission 权限列表（菜单列表）
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;array&#125;</span> </span>asyncRouter 异步路由对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">routerMatch</span>(<span class="hljs-params">permission, asyncRouter</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> routers = [];
        <span class="hljs-comment">// 创建路由</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRouter</span>(<span class="hljs-params">permission</span>) </span>&#123;
            <span class="hljs-comment">// 根据路径匹配到的router对象添加到routers中即可</span>
            permission.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
                <span class="hljs-keyword">if</span> (item.children && item.children.length) &#123;
                    createRouter(item.children)
                &#125;
                <span class="hljs-keyword">let</span> path = item.path;
                <span class="hljs-comment">// 循环异步路由，将符合权限列表的路由加入到routers中</span>
                asyncRouter.find(<span class="hljs-function">(<span class="hljs-params">s</span>) =></span> &#123;
                    <span class="hljs-keyword">if</span> (s.path === <span class="hljs-string">''</span>) &#123;
                        s.children.find(<span class="hljs-function">(<span class="hljs-params">y</span>) =></span> &#123;
                            <span class="hljs-keyword">if</span> (y.path === path) &#123;
                                y.meta.permission = item.permission;
                                routers.push(s);
                            &#125;
                        &#125;)
                    &#125;
                    <span class="hljs-keyword">if</span> (s.path === path) &#123;
                        s.meta.permission = item.permission;
                        routers.push(s);
                    &#125;
                &#125;)
            &#125;)
        &#125;
        createRouter(permission)
        resolve([routers])
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于路由匹配的函数调用，可以放在路由守卫中，即在每一次路由跳转的时候，都会进行一次动态路由匹配：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// router/index.js</span>

router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, form, next</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (sessionStorage.getItem(<span class="hljs-string">'token'</span>)) &#123;
        <span class="hljs-keyword">if</span> (to.path === <span class="hljs-string">'/'</span>) &#123;
            router.replace(<span class="hljs-string">'/index'</span>)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">if</span> (store.state.list.length === <span class="hljs-number">0</span>) &#123;
                <span class="hljs-comment">//如果没有权限列表，将重新向后台请求一次</span>
                store.dispatch(<span class="hljs-string">'getPermission'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                    <span class="hljs-comment">//调用权限匹配的方法</span>
                    routerMatch(res, asyncRouterList).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                        <span class="hljs-comment">//将匹配出来的权限列表进行addRoutes</span>
                        router.addRoutes(res[<span class="hljs-number">0</span>]);
                        next(&#123;
                            ...to,
                            <span class="hljs-attr">replace</span>: <span class="hljs-literal">true</span>
                        &#125;)
                    &#125;)
                &#125;).catch(<span class="hljs-function">() =></span> &#123;
                    router.replace(<span class="hljs-string">'/'</span>)
                &#125;)
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">if</span> (to.matched.length) &#123;
                    next()
                &#125; <span class="hljs-keyword">else</span> &#123;
                    router.replace(<span class="hljs-string">'/'</span>)
                &#125;
            &#125;
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">if</span> (whiteList.indexOf(to.path) >= <span class="hljs-number">0</span>) &#123;
            next()
        &#125; <span class="hljs-keyword">else</span> &#123;
            router.replace(<span class="hljs-string">'/'</span>)
        &#125;
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于此，我们完成了对页面访问权限的控制。我们可以总结出一条完整的权限控制流程图。</p>
<h2 data-id="heading-3">路由权限控制的完整流程图</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9aa64d4524774dfaac3202547f04c244~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            