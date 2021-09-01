
---
title: 'vue配置文件自动生成路由和菜单'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ffdda02658449afa22d929f1495faba~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 01:26:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ffdda02658449afa22d929f1495faba~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">写在前面</h3>
<p>每次重复写路由的时候是不是会觉得很烦，特别是项目大的时候，路由会有特别多，看都看不过来，所以这里我是有了一个router.json的配置文件来对路由做一些简单的配置，然后让路由和左侧菜单栏可以同时自动生成。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ffdda02658449afa22d929f1495faba~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">router.json</h3>
<p>主要配置项如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cc017e47cf74fc799f8f09cd87521cd~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"routerConfig"</span>,
  <span class="hljs-attr">"menu"</span>: [&#123;
    <span class="hljs-attr">"id"</span>: <span class="hljs-string">"1"</span>, <span class="hljs-comment">//路由id，不能重复</span>
    <span class="hljs-attr">"name"</span>: <span class="hljs-string">"home"</span>,<span class="hljs-comment">//路由名字</span>
    <span class="hljs-attr">"path"</span>: <span class="hljs-string">"/homePage"</span>,<span class="hljs-comment">//路由路径</span>
    <span class="hljs-attr">"label"</span>: <span class="hljs-string">"首页"</span>,<span class="hljs-comment">//菜单标题</span>
    <span class="hljs-attr">"selected"</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">//默认选中</span>
    <span class="hljs-attr">"icon"</span>: <span class="hljs-string">"el-icon-monitor"</span>,<span class="hljs-comment">//菜单显示图标</span>
    <span class="hljs-attr">"open"</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">//默认打开</span>
    <span class="hljs-attr">"component"</span>: <span class="hljs-string">"homePage/homePage.vue"</span>,<span class="hljs-comment">//组件路由</span>
    <span class="hljs-attr">"children"</span>: [ <span class="hljs-comment">//子菜单</span>
      &#123;
        <span class="hljs-attr">"id"</span>: <span class="hljs-string">"3"</span>,
        <span class="hljs-attr">"name"</span>: <span class="hljs-string">"getCover"</span>,
        <span class="hljs-attr">"path"</span>: <span class="hljs-string">"/getCover"</span>,
        <span class="hljs-attr">"label"</span>: <span class="hljs-string">"封面截取"</span>,
        <span class="hljs-attr">"selected"</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">"icon"</span>: <span class="hljs-string">"el-icon-scissors"</span>,
        <span class="hljs-attr">"open"</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">"component"</span>: <span class="hljs-string">"getCover/getCover.vue"</span>,
        <span class="hljs-attr">"children"</span>: []
      &#125;
    ]
  &#125;,&#123;
    <span class="hljs-attr">"id"</span>: <span class="hljs-string">"2"</span>,
    <span class="hljs-attr">"name"</span>: <span class="hljs-string">"testPage"</span>,
    <span class="hljs-attr">"path"</span>: <span class="hljs-string">"/testPage"</span>,
    <span class="hljs-attr">"label"</span>: <span class="hljs-string">"测试"</span>,
    <span class="hljs-attr">"selected"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"icon"</span>: <span class="hljs-string">"el-icon-setting"</span>,
    <span class="hljs-attr">"open"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"component"</span>: <span class="hljs-string">"test/test.vue"</span>,
    <span class="hljs-attr">"children"</span>: []
  &#125;,&#123;
    <span class="hljs-attr">"id"</span>: <span class="hljs-string">"5"</span>,
    <span class="hljs-attr">"name"</span>: <span class="hljs-string">"testMenu"</span>,
    <span class="hljs-attr">"path"</span>: <span class="hljs-string">"/testMenu"</span>,
    <span class="hljs-attr">"label"</span>: <span class="hljs-string">"菜单测试"</span>,
    <span class="hljs-attr">"selected"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"icon"</span>: <span class="hljs-string">"el-icon-setting"</span>,
    <span class="hljs-attr">"open"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"component"</span>: <span class="hljs-string">"testMenu/testMenu.vue"</span>,
    <span class="hljs-attr">"children"</span>: []
  &#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置主要分为两部分，一部分由于菜单生成，一部分用于路由生成，当然两者也有共用的部分</p>
<h3 data-id="heading-2">路由生成</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> ro <span class="hljs-keyword">from</span> <span class="hljs-string">"element-ui/src/locale/lang/ro"</span>;
Vue.use(VueRouter)
<span class="hljs-comment">//引入配置文件router.json</span>
<span class="hljs-keyword">let</span> routerMenu = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@/config/router.json'</span>);
routerMenu = routerMenu.menu;
<span class="hljs-keyword">let</span> menu = [];
<span class="hljs-comment">//配置路由</span>
<span class="hljs-keyword">let</span> formatRoute = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">routerMenu,menu</span>)</span>&#123;
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < routerMenu.length; i++)&#123;
    <span class="hljs-keyword">let</span> temp = &#123;
      <span class="hljs-attr">path</span>: routerMenu[i].path,
      <span class="hljs-attr">name</span>: routerMenu[i].name,
      <span class="hljs-comment">//这块要注意</span>
      <span class="hljs-comment">//用require这种方式引入的时候，会将你的component分别打包成不同</span>
      <span class="hljs-comment">//的js，加载的时候也是按需加载，只用访问这个路由网址时才会加载</span>
      <span class="hljs-comment">//这个js</span>
      <span class="hljs-attr">component</span>: <span class="hljs-function"><span class="hljs-params">resolve</span> =></span> <span class="hljs-built_in">require</span>([<span class="hljs-string">`@/views/<span class="hljs-subst">$&#123;routerMenu[i].component&#125;</span>`</span>], resolve)
    &#125;;
    menu.push(temp);
    <span class="hljs-keyword">if</span>(routerMenu[i].children && routerMenu[i].children.length > <span class="hljs-number">0</span>)&#123;
    <span class="hljs-comment">//递归生成子菜单的路由</span>
      formatRoute(routerMenu[i].children,menu);
    &#125;
  &#125;
&#125;
<span class="hljs-comment">//初始化</span>
formatRoute(routerMenu,menu);
<span class="hljs-comment">//重定向设置</span>
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/homePage'</span>
  &#125;,
]
<span class="hljs-comment">//将生成的路由文件push进去</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < menu.length; i++)
  routes.push(menu[i]);
  
<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  routes
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">菜单生成</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"leftMenu"</span>></span>

  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"left"</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span>&#123;
      <span class="hljs-attr">menu</span>:[]
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>:&#123;
  <span class="hljs-comment">//通过路由id来找节点</span>
    <span class="hljs-function"><span class="hljs-title">findNodeById</span>(<span class="hljs-params">node,id</span>)</span>&#123;
      <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < node.length; i++)&#123;
        <span class="hljs-keyword">if</span>(id == node[i].id)&#123;
          node[i].selected = <span class="hljs-literal">true</span>;
          <span class="hljs-keyword">if</span>(node[i].children && node[i].children.length > <span class="hljs-number">0</span>)&#123;
            <span class="hljs-built_in">this</span>.findNodeById(node[i].children,id);
          &#125;
          node[i].open = !node[i].open;
          <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.$route.path !== node[i].path) <span class="hljs-built_in">this</span>.$router.push(node[i].path);
        &#125;<span class="hljs-keyword">else</span>&#123;
          node[i].selected = <span class="hljs-literal">false</span>;
          <span class="hljs-keyword">if</span>(node[i].children && node[i].children.length > <span class="hljs-number">0</span>)&#123;
            <span class="hljs-built_in">this</span>.findNodeById(node[i].children,id);
          &#125;<span class="hljs-keyword">else</span>&#123;

          &#125;
        &#125;
      &#125;
    &#125;,
    <span class="hljs-comment">//选中菜单节点</span>
    <span class="hljs-function"><span class="hljs-title">chooseNode</span>(<span class="hljs-params">id</span>)</span>&#123;
      <span class="hljs-built_in">this</span>.findNodeById(<span class="hljs-built_in">this</span>.menu,id);
      <span class="hljs-keyword">let</span> domTree = <span class="hljs-built_in">this</span>.generatorMenu(<span class="hljs-built_in">this</span>.menu,<span class="hljs-string">''</span>,<span class="hljs-number">0</span>)
      <span class="hljs-keyword">let</span> leftMenu = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'leftMenu'</span>);
      leftMenu.innerHTML = domTree;
    &#125;,
    <span class="hljs-comment">//动态生成菜单目录</span>
    <span class="hljs-function"><span class="hljs-title">generatorMenu</span>(<span class="hljs-params">menu,temp,floor</span>)</span>&#123;
      <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < menu.length; i++)&#123;
        temp += <span class="hljs-string">`<div style="width: max-content">
                    <div class="menuOption" onclick="chooseNode(<span class="hljs-subst">$&#123;menu[i].id&#125;</span>)"
                            style="text-indent: <span class="hljs-subst">$&#123;floor&#125;</span>em;
                            background-color: <span class="hljs-subst">$&#123;menu[i].selected?<span class="hljs-string">'aquamarine'</span>:<span class="hljs-string">''</span>&#125;</span>;
                            cursor: pointer;
                            margin-top: 0.3rem;">
                        <i class="<span class="hljs-subst">$&#123;menu[i].icon&#125;</span>"></i>
                        <span class="hljs-subst">$&#123;menu[i].label&#125;</span>`</span>
        <span class="hljs-keyword">if</span>(!menu[i].open && menu[i].children && menu[i].children.length > <span class="hljs-number">0</span>)&#123;
          temp += <span class="hljs-string">`<i style="margin-left: 1rem" class="el-icon-arrow-down"></i>`</span>
        &#125;<span class="hljs-keyword">else</span>&#123;
          <span class="hljs-keyword">if</span>(menu[i].open && menu[i].children && menu[i].children.length > <span class="hljs-number">0</span>)&#123;
            temp += <span class="hljs-string">`<i style="margin-left: 1rem" class="el-icon-arrow-up"></i>`</span>
          &#125;
        &#125;
        temp += <span class="hljs-string">`</div>`</span>
        <span class="hljs-keyword">if</span>(menu[i].open && menu[i].children && menu[i].children.length != <span class="hljs-number">0</span>)&#123;
          temp = <span class="hljs-built_in">this</span>.generatorMenu(menu[i].children,temp,floor+<span class="hljs-number">1</span>);
        &#125;
        temp += <span class="hljs-string">`</div>`</span>
      &#125;
      <span class="hljs-keyword">return</span> temp;
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;

  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">window</span>.chooseNode = <span class="hljs-built_in">this</span>.chooseNode;
    <span class="hljs-keyword">let</span> menu = [];
    <span class="hljs-comment">//获取路由菜单配置文件</span>
    <span class="hljs-keyword">const</span> router = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@/config/router.json'</span>);
    menu = router.menu;
    <span class="hljs-built_in">this</span>.menu = menu;
    <span class="hljs-keyword">let</span> domTree = <span class="hljs-built_in">this</span>.generatorMenu(menu,<span class="hljs-string">''</span>,<span class="hljs-number">0</span>)
    <span class="hljs-keyword">let</span> leftMenu = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'leftMenu'</span>);
    leftMenu.innerHTML = domTree;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
  <span class="hljs-selector-id">#leftMenu</span>&#123;
    <span class="hljs-attribute">min-height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">100vh</span> - <span class="hljs-number">44px</span> - <span class="hljs-number">1rem</span>);
    <span class="hljs-attribute">background-color</span>: cornflowerblue;
    <span class="hljs-attribute">text-align</span>: left;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0.5rem</span> <span class="hljs-number">1rem</span>;
    <span class="hljs-attribute">font-size</span>: large;
    <span class="hljs-attribute">font-weight</span>: bold;
  &#125;
  <span class="hljs-selector-class">.selectedM</span>&#123;
    <span class="hljs-attribute">background-color</span>: aquamarine;
  &#125;
  <span class="hljs-selector-class">.menuOption</span>&#123;
    <span class="hljs-attribute">cursor</span>: pointer;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">效果</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3643fc0981242ec89c82ac12d11d238~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82b8abf9efa64a88a2a615b2d05c1a05~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>左侧菜单便是自动生成的，点击菜单栏也会跳转到对应的路由地址，当然，样式有点丑，但样式的话可以自己后续再调整。
这样的话，我们新加菜单的时候只需要在配置文件中配置好，就可以直接写编写页面，这样也给我们省下了很多时间。</p></div>  
</div>
            