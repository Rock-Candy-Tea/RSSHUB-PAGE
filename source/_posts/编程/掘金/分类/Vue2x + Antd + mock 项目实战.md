
---
title: 'Vue2.x + Antd + mock 项目实战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b6b52f0524b49aaa73f47ef7db4a1fe~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 02:33:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b6b52f0524b49aaa73f47ef7db4a1fe~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">项目说明</h1>
<p><a href="https://download.csdn.net/download/Wang_Si_D/17544034" target="_blank" rel="nofollow noopener noreferrer">下载</a></p>
<h2 data-id="heading-1">介绍</h2>
<ol>
<li>环境
<code>"vue-cli": 3.0</code></li>
<li>涉及主要插件</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"ant-design-vue"</span>: <span class="hljs-string">"^1.7.2"</span>,
    <span class="hljs-string">"axios"</span>: <span class="hljs-string">"^0.21.1"</span>,
    <span class="hljs-string">"core-js"</span>: <span class="hljs-string">"^3.6.5"</span>,
    <span class="hljs-string">"crypto-js"</span>: <span class="hljs-string">"^4.0.0"</span>,
    <span class="hljs-string">"echarts"</span>: <span class="hljs-string">"^5.0.2"</span>,
    <span class="hljs-string">"lodash"</span>: <span class="hljs-string">"^4.17.21"</span>,
    <span class="hljs-string">"moment"</span>: <span class="hljs-string">"^2.29.1"</span>,
    <span class="hljs-string">"nprogress"</span>: <span class="hljs-string">"^0.2.0"</span>,
    <span class="hljs-string">"resize-observer-polyfill"</span>: <span class="hljs-string">"^1.5.1"</span>,
    <span class="hljs-string">"vue"</span>: <span class="hljs-string">"^2.6.11"</span>,
    <span class="hljs-string">"vue-cookie"</span>: <span class="hljs-string">"^1.1.4"</span>,
    <span class="hljs-string">"vue-i18n"</span>: <span class="hljs-string">"^8.24.1"</span>,
    <span class="hljs-string">"vue-infinite-scroll"</span>: <span class="hljs-string">"^2.0.2"</span>,
    <span class="hljs-string">"vue-router"</span>: <span class="hljs-string">"^3.2.0"</span>,
    <span class="hljs-string">"vuex"</span>: <span class="hljs-string">"^3.4.0"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>内置组件
<ul>
<li>SvgIcon 支持Svg图标引入</li>
<li>Ellipsis 文本省略</li>
<li>PageScrollable 过长收缩滚动组件</li>
<li>EditTable 基于Antd Table 的简单编辑表格</li>
</ul>
</li>
</ol>
<h2 data-id="heading-2">目录结构</h2>
<ul>
<li>build（构建配置目录）</li>
<li>public（公共资源目录）</li>
<li>src（项目目录）
<ul>
<li>api（项目api接口目录）</li>
<li>assets（项目资源目录）</li>
<li>components（项目组件目录）</li>
<li>config（全局配置目录）</li>
<li>directives（自定义指令目录）</li>
<li>layouts（页面布局文件目录）</li>
<li>i18n（多语言配置）</li>
<li>mock（mock目录-本地环境开启）</li>
<li>plugins（插件目录）</li>
<li>router（路由树目录）</li>
<li>store（store目录）</li>
<li>styles（全局样式目录）</li>
<li>utils（工具方法目录）</li>
<li>views （项目页面目录）</li>
<li>App.vue （项目App）- 提供单页面路由视图 router-view</li>
<li>main.js（构建入口 - 加载插件、插件全局配置）</li>
</ul>
</li>
</ul>
<h2 data-id="heading-3">api 目录（封装接口调用）</h2>
<blockquote>
<p>提供项目涉及的接口配置信息，封装成通用方法 <code>$api</code> ，方便接口调用。</p>
</blockquote>
<ul>
<li>index 文件 -解析 <code>modules</code> 目录，获取相关模块接口配置，然后封装成 <code>$api</code> 全局方法。</li>
<li>modules 目录（存放模块接口配置文件，必须是 <code>*.js</code> 文件，暴露相应配置对象）</li>
</ul>
<p><strong>使用 <code>require.context()</code> 方法一次性引入目录文件模块</strong></p>
<h3 data-id="heading-4">接口配置</h3>
<ul>
<li>key: 作为接口配置的键值，同时也是 $api 调用方法的键值。</li>
<li>url: 指定接口地址，支持 restful 接口，地址带有的参数（:key）会从 <code>data</code> 中读取，自动进行数值替换，<strong>因此data中必须包含参数字段，否则会导致接口地址错误。</strong></li>
<li>method: 接口请求方式</li>
<li>description: 接口描述 - 不作为请求参数</li>
<li>data: 接口参数列表，所有参数必须填写，包括url上的参数（:key)，自动过滤列表以外的参数。<em>配置字段参数不作为默认值，只是作为数据类型使用。</em></li>
</ul>
<h3 data-id="heading-5">$api 方法</h3>
<blockquote>
<p>$api['modules/key'](data, config)</p>
</blockquote>
<ul>
<li>modules: modules目录的对应文件名</li>
<li>key: 接口键值</li>
<li>data: 接口参数</li>
<li>config: 额外的接口配置</li>
</ul>
<h2 data-id="heading-6">mock 目录（本地接口数据模拟）</h2>
<blockquote>
<p>本地 <code>.dev</code> 才执行，拦截接口请求，返回mock数据。需要按结构定义相应接口路由及mock数据。</p>
</blockquote>
<ul>
<li>index 文件 -mock启用文件</li>
<li>utils 文件 -定义mock相关工具方法</li>
<li>services 目录（定义模块接口）</li>
</ul>
<p><strong>使用 <code>require.context()</code> 方法一次性引入目录文件模块</strong></p>
<p><em>扩展：</em>
<code>require.context(directory, useSubdirectories, regExp): function</code></p>
<ul>
<li>irectory: 要查找的文件路径</li>
<li>useSubdirectories: 是否查找子目录</li>
<li>regExp: 要匹配文件的正则</li>
<li>return: 返回一个函数，通过 <code>.keys()</code> 返回匹配的所有模块地址，传入对应key值，获取对应模块内容。通过正则可解析文件名称作为模块名称。</li>
</ul>
<h2 data-id="heading-7">routes 目录（支持动态路由）</h2>
<blockquote>
<p>定义项目路由配置。</p>
</blockquote>
<ul>
<li>index 文件 -最终路由配置对象。</li>
<li>staticRoutes 文件 -配置公共路由，不需要用户权限验证</li>
<li>asyncRoutes 文件 -根据接口返回权限码返回动态路由配置 或者 需要根据权限（permitCode）动态计算的路由</li>
</ul>
<p><strong>注意：</strong> 可通过meta的新增字段 <code>menu</code> 指定所属菜单 路由，值为 path路径，用于渲染选中的菜单项。</p>
<p><em>备注</em> 目前登录页由项目提供，需要登录后才能获取路由权限，不建议使用动态路由，而直接根据路由的permitCode 在全局路由守卫拦截。如果在index.html可以获取账号权限（登录页由其他项目管理）则建议使用动态路由。asyncRoutes 文件提供 <code>getRoutes</code> 方法返回动态路由配置。</p>
<h2 data-id="heading-8">store 目录（按模块）</h2>
<ul>
<li>index 文件 -根store</li>
<li>types 文件 -定义mutations、actions名称常量</li>
<li>modules 目录（定义store模块）</li>
</ul>
<p><strong>注意</strong> modules 如果启用 命名空间（namespaced: true），dispatch、commit 要加模块名称前缀，但mapState可以传入<code>模块名称(1参)</code>以及直接使用<code>字符串数组(2参)</code>就能得到模块state，如果禁用 命名空间，dispatch、commit 不需要加模块前缀，但是模块state需要在 mapState 使用<code>对象(1参)</code>参数建立映射关系([string]: (state) => any)。</p>
<h2 data-id="heading-9">styles 目录</h2>
<blockquote>
<p>定义全局样式，避免 <code>.vue</code> 文件嵌套复杂的样式，只需要专注页面结构以及页面逻辑。</p>
</blockquote>
<ul>
<li>index -根样式</li>
<li>base 文件 -基础样式</li>
<li>common 目录（存放公共内容）
<ul>
<li>index 文件 -定义类结构变量</li>
<li>mixins 文件 -混合类</li>
<li>variable 文件 -定义公共变量</li>
</ul>
</li>
<li>components 目录（定义组件样式）</li>
<li>layouts 目录（定义布局组件样式）</li>
<li>views 目录（定义模块页面样式）</li>
</ul>
<h2 data-id="heading-10">i18n 目录（支持国际化）</h2>
<blockquote>
<p>定义多语言配置文件，目前只设置中文、英文两个语言版本</p>
</blockquote>
<ul>
<li>index 文件 -解析语言配置，创建<code>i18n</code>对象</li>
<li>language 目录 -存放对应语言配置，文件名作为语言，并需要在各个语言文件内配置对应名称的文案配置，这一步是为了顶部多语言切换能够正确显示可切换的语言文案。</li>
</ul>
<h2 data-id="heading-11">config 目录</h2>
<blockquote>
<p>定义项目需要使用的或者需要多处使用的静态内容。</p>
</blockquote>
<ul>
<li>index 文件 - 定义左侧菜单树，权限菜单控制，以及权限控制开关字段。</li>
<li>cookies 文件 -定义项目涉及的所有cookie的名称。</li>
<li>charts 文件 -定义图标配置项默认配置，方便风格统一。</li>
<li>router 文件 -定义路由创建所需要的默认配置项，以及全局路由守卫，路由守涉及路由权限控制。</li>
<li>axios 文件 -定义axios创建所需要的默认配置项，以及axios全局拦截器，包括interceptor.request 和 interceptor.response</li>
</ul>
<h2 data-id="heading-12">权限控制（待优化）</h2>
<blockquote>
<p>权限控制包括 路由访问权限控制 、 左侧菜单权限控制 、 功能码权限控制
主要涉及文件 <code>routes/asyncRoutes</code>、<code>config/index</code>、<code>config/router</code>、<code>utils/permission</code>、<code>directives/permit</code></p>
</blockquote>
<ul>
<li>路由访问权限控制
<ul>
<li>目前通过在 meta 字段中配置 permitCode 字段，在全局路由前置守卫中根据权限数组（接口返回）匹配 permitCode 字段来控制对应路由访问控制。如果路由配置未设置 permitCode 字段，则不校验权限。同时在 <code>config/index</code> 设置是否开启验证路由权限开关字段 <code>PERMIT_ROUTE_OPEN</code>，方便关闭路由权限控制。</li>
<li>同时，也设置另一种权限路由控制方式，在 <code>routes/asyncRouters</code> 文件中暴露 <code>getRoutes</code> 方法用来过滤有权限路由，通过传入 <code>权限数组</code> 参数，返回对应路由配置，在动态添加到router路由对象。（此方法需要进入页面就有路由权限，否则需要控制首次进入路由跳转前完成接口请求以及动态路由添加）</li>
</ul>
</li>
<li>左侧菜单权限控制
左侧菜单权限控制，通过 <code>config/index</code> 文件暴露的 <code>getPermitMenus</code> 方法，传入菜单权限码数组进行过滤，返回对应菜单数据，以供全局左侧菜单栏显示。同时，在 <code>config/index</code> 设置是否开启菜单权限控制开关字段 <code>PERMIT_MENU_OPEN</code> ，方便关闭菜单权限控制。</li>
<li>功能码权限控制
功能码权限控制，主要用来控制按钮以及部分信息展示，根据接口返回功能码集合 <code>func</code> ，全局提供 <code>$havePermission</code> 方法，通过传入权限码（支持单个或者多个）进行权限校验，方法实现位于 <code>utils/permission</code> 文件。同时提供自定义指令 <code>v-permit</code> 控制内容展示。</li>
</ul>
<h2 data-id="heading-13">页面展示</h2>
<h3 data-id="heading-14">布局</h3>
<ul>
<li>登陆/注册/忘记密码页面
只有内容栏，内容左右，一边是背景，一边是主要表单内容
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b6b52f0524b49aaa73f47ef7db4a1fe~tplv-k3u1fbpfcp-zoom-1.image" alt="登录页面" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/378b3e37b0874ac8975f381befe56e66~tplv-k3u1fbpfcp-zoom-1.image" alt="注册页面" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>异常页面（403、500）
只有内容栏（Content）。直接使用Antd 的 Result组件渲染<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c039f2ba6b5475da1bcbfc74934ee59~tplv-k3u1fbpfcp-zoom-1.image" alt="403页面" loading="lazy" referrerpolicy="no-referrer"></li>
<li>主要页面
顶部（Header）-侧边布局（Sider）-内容栏（Content），侧边栏支持收缩</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0372112b8ee4812a8fc867b548f580b~tplv-k3u1fbpfcp-zoom-1.image" alt="首页" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a7b6e70ee044af4a391252eeed8858f~tplv-k3u1fbpfcp-zoom-1.image" alt="侧边栏收缩效果" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">其他展示</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53a0e666aa5f42489b0a128e5bcd9f51~tplv-k3u1fbpfcp-zoom-1.image" alt="侧边信息页" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e6764a27c4346f2a0464f3ef3d8ae3e~tplv-k3u1fbpfcp-zoom-1.image" alt="分布表单页面" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0da811aeb4264151a7d49155f2a1412c~tplv-k3u1fbpfcp-zoom-1.image" alt="高级表单页面" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81bf1ab2669646618dc31557cb376592~tplv-k3u1fbpfcp-zoom-1.image" alt="基础表格页面" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7d673dc265f40279e8b286738aa70a4~tplv-k3u1fbpfcp-zoom-1.image" alt="基础列表页" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5b2ffc6a6b54ceca402ebc592eb634b~tplv-k3u1fbpfcp-zoom-1.image" alt="基础详情页" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            