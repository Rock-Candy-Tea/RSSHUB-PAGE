
---
title: 'Vite + TypeScript + Ant Design Vue 搭建后台管理系统（四）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d65d648e40647ac923b79ccefa55001~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 19:28:02 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d65d648e40647ac923b79ccefa55001~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<p>在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzptime%2Fshanglv-vite-antdv%2Fblob%2Fmain%2Freadme%2FTHIRD.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zptime/shanglv-vite-antdv/blob/main/readme/THIRD.md" ref="nofollow noopener noreferrer">（三）</a>的基础上，进行侧栏菜单功能完善，完成了侧栏菜单的基本展示，还有一些可完善、可优化的地方。此分支路由表有更新，具体查看源码。</p>
</blockquote>
<blockquote>
<p>主要功能概括：路由导航(router-link)；唯一子菜单处理；动态路由刷新白屏；菜单状态保存</p>
</blockquote>
<blockquote>
<p>Gihub 地址[开发分支：4-dev-menu]：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzptime%2Fshanglv-vite-antdv%2Ftree%2F4-dev-menu" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zptime/shanglv-vite-antdv/tree/4-dev-menu" ref="nofollow noopener noreferrer">github.com/zptime/shan…</a></p>
</blockquote>
<h2 data-id="heading-0">侧栏菜单路由导航(router-link)</h2>
<blockquote>
<p>之前只是完成了菜单的展示，但是对应的路由功能没有实现，现在使用 routerLink 实现路由导航，主要使用 to 属性控制目标路由的链接。</p>
</blockquote>
<blockquote>
<p>官方 API 文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fapi%2F%23router-link" target="_blank" rel="nofollow noopener noreferrer" title="https://router.vuejs.org/zh/api/#router-link" ref="nofollow noopener noreferrer">router.vuejs.org/zh/api/#rou…</a></p>
</blockquote>
<ol>
<li>修改 layout/sider/menu.vue 文件</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a-menu</span> <span class="hljs-attr">mode</span>=<span class="hljs-string">"inline"</span> <span class="hljs-attr">theme</span>=<span class="hljs-string">"dark"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in menus"</span>></span>
      <span class="hljs-comment"><!-- 一级菜单 --></span>
      <span class="hljs-tag"><<span class="hljs-name">a-menu-item</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!item.children"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.name"</span>></span>
        <span class="hljs-comment"><!-- 注意：此处to属性中用的是name值，而不是path；如果用path,
        router/index.ts中的子菜单path应该定义为“/父菜单路由/子菜单路由”，例如：将“role”改为“/system/role”。 --></span>
        <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; name: item.name &#125;"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; item.meta && item.meta.title &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">a-menu-item</span>></span>
       <span class="hljs-comment"><!-- 子级菜单 --></span>
      <span class="hljs-tag"><<span class="hljs-name">SubMenu</span> <span class="hljs-attr">v-else</span> <span class="hljs-attr">:menu-info</span>=<span class="hljs-string">"item"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.name"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">a-menu</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts>
import &#123; useRouter &#125; from "</span><span class="hljs-attr">vue-router</span>";
<span class="hljs-attr">export</span> <span class="hljs-attr">default</span> <span class="hljs-attr">defineComponent</span>(&#123;
  <span class="hljs-attr">setup</span>() &#123;
    // <span class="hljs-attr">vue-router</span>获取路由，查看路由方法
    <span class="hljs-attr">const</span> &#123; <span class="hljs-attr">options</span>, <span class="hljs-attr">getRoutes</span> &#125; = <span class="hljs-string">useRouter();</span>
    <span class="hljs-attr">console.log</span>("<span class="hljs-attr">getRoutes</span>", <span class="hljs-attr">getRoutes</span>());
    <span class="hljs-attr">console.log</span>("<span class="hljs-attr">options.routes</span>", <span class="hljs-attr">options.routes</span>);
  &#125;
&#125;)
</<span class="hljs-attr">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明：VueRouter 4.x 中获取路由，查看路由的方法为 useRouter()，useRouter().getRoutes()，useRouter().options.routes 等</p>
<ol start="2">
<li>修改 layout/sider/subMenu.vue 文件</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-comment"><!-- 不存在子级的菜单 --></span>
  <span class="hljs-tag"><<span class="hljs-name">a-menu-item</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!item.children"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.name"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; name: item.name &#125;"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Icon</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.meta && item.meta.icon"</span> <span class="hljs-attr">:icon</span>=<span class="hljs-string">"item.meta.icon"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; item.meta && item.meta.title &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">a-menu-item</span>></span>
  <span class="hljs-comment"><!-- 存在子级菜单 --></span>
  <span class="hljs-tag"><<span class="hljs-name">SubMenu</span> <span class="hljs-attr">v-else</span> <span class="hljs-attr">:menu-info</span>=<span class="hljs-string">"item"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.name"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">侧栏菜单子路由处理</h2>
<blockquote>
<p>之前的首页、权限测试页都只有一个子菜单，在这种情况展示两级，就不太合理了。对于这种情况，需要处理一下，只展示一级，父菜单路由直接取值子菜单的路由。</p>
</blockquote>
<p>判断条件：是否子菜单 && 子菜单个数 === 1</p>
<ol>
<li>修改 layout/sider/menu.vue 文件</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-comment"><!-- 一级菜单 --></span>
  <span class="hljs-tag"><<span class="hljs-name">a-menu-item</span>
    <span class="hljs-attr">v-if</span>=<span class="hljs-string">"
          !item.children ||
          (item.children && item.children.length && item.children.length === 1)
        "</span>
    <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.name"</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span>
      <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123;
            name:
              item.children &&
              item.children.length &&
              item.children.length === 1
                ? item.children[0].name
                : item.name,
          &#125;"</span>
    ></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; item.meta && item.meta.title &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">a-menu-item</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>修改 layout/sider/subMenu.vue 文件</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-comment"><!-- 不存在子级的菜单 --></span>
  <span class="hljs-tag"><<span class="hljs-name">a-menu-item</span>
    <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!item.children ||
          (item.children && item.children.length && item.children.length === 1)"</span>
    <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.name"</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span>
      <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123;
            name:
              item.children &&
              item.children.length &&
              item.children.length === 1
                ? item.children[0].name
                : item.name,
          &#125;"</span>
    ></span>
      <span class="hljs-tag"><<span class="hljs-name">Icon</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.meta && item.meta.icon"</span> <span class="hljs-attr">:icon</span>=<span class="hljs-string">"item.meta.icon"</span> /></span>
      <span class="hljs-comment"><!-- <component v-if="item.meta.icon" :is="item.meta.icon" /> --></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; item.meta && item.meta.title &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">a-menu-item</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">动态路由注册刷新白屏</h2>
<p>问题：点击刷新，vue-router 会重新初始化，之前动态 addRoute 的路由就不存在了，此时访问一个不存在的页面，就导致页面空白了。</p>
<p>解决：把加载菜单信息放在 router 的全局守卫 beforeEach 中。</p>
<p>注意：防止无限循环，要根据条件停止。我的停止条件就是 store.getters.routes.length > 3，因为默认的通用路由长度为 3，长度小于 3 时，需要加载动态路由表；长度大于 3，代表已经添加过了，无需再添加。</p>
<ol>
<li>修改 App.vue 文件</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">router-view</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  &#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>修改 router/index.ts 文件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">"store/index"</span>;

router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (to.path !== <span class="hljs-keyword">from</span>.path) &#123;
    <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`<span class="hljs-subst">$&#123;to.meta.title&#125;</span>`</span>;
  &#125;

  <span class="hljs-keyword">if</span> (to.path === <span class="hljs-string">"/login"</span> || to.path === <span class="hljs-string">"/register"</span>) &#123;
    next();
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (store.getters.routes.length <= <span class="hljs-number">3</span>) &#123;
    store.dispatch(<span class="hljs-string">"generateRoutes"</span>);
    <span class="hljs-comment">// @ts-ignore</span>
    next(&#123; ...to, <span class="hljs-attr">replace</span>: <span class="hljs-literal">true</span> &#125;);
  &#125; <span class="hljs-keyword">else</span> &#123;
    next();
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">菜单状态保存（展开、选中）</h2>
<p>每次刷新页面，菜单展开的状态和被选中的状态就丢失了，需要处理一下。我采用的是 localStorage 和 Vuex 结合使用</p>
<ol>
<li>修改 layout/sider/menu.vue 文件</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a-menu</span>
    @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleMenuClick"</span>
    <span class="hljs-attr">v-model:openKeys</span>=<span class="hljs-string">"openKeys"</span>
    <span class="hljs-attr">v-model:selectedKeys</span>=<span class="hljs-string">"selectedKeys"</span>
  ></span>
    // ...
  <span class="hljs-tag"></<span class="hljs-name">a-menu</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> R <span class="hljs-keyword">from</span> <span class="hljs-string">"ramda"</span>;
  <span class="hljs-keyword">import</span> &#123; defineComponent, toRefs, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
  <span class="hljs-keyword">import</span> &#123; useStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"store/index"</span>;

  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> store = useStore();
      <span class="hljs-comment">// 通过localStorage保存状态</span>
      <span class="hljs-keyword">const</span> state = reactive(&#123;
        <span class="hljs-attr">selectedKeys</span>: <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">"selectedMenu"</span>)
          ? [<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">"selectedMenu"</span>)]
          : [],
        <span class="hljs-attr">openKeys</span>: <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">"openMenu"</span>)
          ? R.split(<span class="hljs-string">","</span>, <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">"openMenu"</span>))
          : [],
      &#125;);

      <span class="hljs-keyword">const</span> handleMenuClick = <span class="hljs-function">(<span class="hljs-params">e: Event</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> &#123; key &#125; = e;
        <span class="hljs-comment">// 点击时，将状态保存到vuex和localStorage</span>
        store.commit(<span class="hljs-string">"SELECTED_MENU"</span>, key);
        store.commit(<span class="hljs-string">"OPEN_MENU"</span>, state.openKeys);
      &#125;;

      <span class="hljs-keyword">return</span> &#123;
        ...toRefs(state),
        handleMenuClick,
      &#125;;
    &#125;,
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>修改 store/modules/settings.ts 文件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> settings: Module<SettingsState, RootStateTypes> = &#123;
  <span class="hljs-function"><span class="hljs-title">state</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">selectedMenu</span>: [],
      <span class="hljs-attr">openMenu</span>: [],
    &#125;;
  &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-attr">selectedMenu</span>: <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> state.selectedMenu,
    <span class="hljs-attr">openMenu</span>: <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> state.openMenu,
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">SELECTED_MENU</span>(<span class="hljs-params">state, data</span>)</span> &#123;
      <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">"selectedMenu"</span>, data);
      state.selectedMenu = data;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">OPEN_MENU</span>(<span class="hljs-params">state, data</span>)</span> &#123;
      <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">"openMenu"</span>, data);
      state.openMenu = data;
    &#125;,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>![预览效果]</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d65d648e40647ac923b79ccefa55001~tplv-k3u1fbpfcp-watermark.image" alt="sider_status_keep.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            