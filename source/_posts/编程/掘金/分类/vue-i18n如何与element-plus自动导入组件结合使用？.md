
---
title: 'vue-i18n如何与element-plus自动导入组件结合使用？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b99560cad8e040dd9b46472377735786~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Thu, 15 Sep 2022 01:34:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b99560cad8e040dd9b46472377735786~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第2篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<h1 data-id="heading-0">前言</h1>
<p>之前就想使用i18n国际化插件，但是一直没有使用的机会，正好这次要搭建一个vite+vue3的基础项目，使用了Element-plus框架，并设设置自动引入组件，刚好也需要设置国际化，所以打算将两者结合使用，通过结合Element-plus与<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue-i18n.intlify.dev" target="_blank" rel="nofollow noopener noreferrer" title="https://vue-i18n.intlify.dev" ref="nofollow noopener noreferrer">vue-i18n</a>的方式来实现多语言切换，废话不多说现在开始吧！<em>（注：之前已经搭好了基本的框架，详细可以参考<a href="https://juejin.cn/post/7142815651294511135" target="_blank" title="https://juejin.cn/post/7142815651294511135">vite+vue3如何配置ESLint与prettier？</a>）</em></p>
<h1 data-id="heading-1"><a href="https://link.juejin.cn/?target=https%3A%2F%2Felement-plus.gitee.io%2Fzh-CN%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://element-plus.gitee.io/zh-CN/" ref="nofollow noopener noreferrer">Element-Plus引入使用</a></h1>
<p>与Vue相配套的UI框架Element UI一定是不二之选，平时用Element也比较多，Vue3出来后，Element也正式升级为Element Plus，相比之前的框架，Element Plus采用Vue3的新特性，使用OptionsAPI、TS来重写，并且在之前的基础上加了很多新的组件和特性，而且官方文档也非常详细，按照给出的文档引入框架，使用起来非常顺利，本项目使用文档中的<a href="https://link.juejin.cn/?target=https%3A%2F%2Felement-plus.gitee.io%2Fzh-CN%2Fguide%2Fquickstart.html%23%25E6%258C%2589%25E9%259C%2580%25E5%25AF%25BC%25E5%2585%25A5" target="_blank" rel="nofollow noopener noreferrer" title="https://element-plus.gitee.io/zh-CN/guide/quickstart.html#%E6%8C%89%E9%9C%80%E5%AF%BC%E5%85%A5" ref="nofollow noopener noreferrer">自动导入</a>结合Vite来引入Element Plus框架。</p>
<h1 data-id="heading-2">下载Element-Plus╮(‵▽′)╭自动导入插件</h1>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-comment"># 下载Element Plus包</span>
npm install element-plus --save
<span class="hljs-comment"># 安装自动导入ElementPlus的两款插件</span>
npm install -D unplugin-vue-components unplugin-auto-import
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">配置vite.config.ts文件</h1>
<p>安装好插件后在配置文件中<code>vite.config.ts</code>编写自动导入Element-plus插件的代码。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; defineConfig, loadEnv &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>;
<span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-vue'</span>;
<span class="hljs-keyword">import</span> &#123; resolve &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-comment">// Element-plus自动导入</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">AutoImport</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'unplugin-auto-import/vite'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">Components</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'unplugin-vue-components/vite'</span>;
<span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">ElementPlusResolver</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'unplugin-vue-components/resolvers'</span>;

<span class="hljs-keyword">const</span> pathResolve = (<span class="hljs-attr">dir</span>: <span class="hljs-built_in">string</span>): <span class="hljs-function"><span class="hljs-params">any</span> =></span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-title function_">resolve</span>(__dirname, <span class="hljs-string">'.'</span>, dir);
&#125;;

<span class="hljs-keyword">const</span> <span class="hljs-attr">alias</span>: <span class="hljs-title class_">Record</span><<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>> = &#123;
<span class="hljs-string">'@'</span>: <span class="hljs-title function_">pathResolve</span>(<span class="hljs-string">'./src'</span>),
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title function_">defineConfig</span>(<span class="hljs-function">(<span class="hljs-params">&#123; mode &#125;</span>) =></span> &#123;
<span class="hljs-keyword">const</span> env = <span class="hljs-title function_">loadEnv</span>(mode, process.<span class="hljs-title function_">cwd</span>());
<span class="hljs-keyword">return</span> &#123;
<span class="hljs-attr">base</span>: env.<span class="hljs-property">VITE_PUBLIC_PATH</span>, <span class="hljs-comment">//配置基础部署路径</span>
<span class="hljs-attr">plugins</span>: [
<span class="hljs-title function_">vue</span>(),
<span class="hljs-title class_">AutoImport</span>(&#123;
<span class="hljs-attr">resolvers</span>: [<span class="hljs-title class_">ElementPlusResolver</span>()],
&#125;),
<span class="hljs-title class_">Components</span>(&#123;
<span class="hljs-attr">resolvers</span>: [<span class="hljs-title class_">ElementPlusResolver</span>()],
&#125;),
],
<span class="hljs-attr">resolve</span>: &#123;
<span class="hljs-comment">// 配置路径别名</span>
alias,
&#125;,
&#125;;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">按需引入的全局配置</h1>
<p>我们使用按需引入的导入方式，那么应该如何调整组件的默认尺寸和语言呢？（ps：官方插件默认配置语言是英语！）官方文档中也有介绍如何<a href="https://link.juejin.cn/?target=https%3A%2F%2Felement-plus.gitee.io%2Fzh-CN%2Fguide%2Fquickstart.html%23%25E5%2585%25A8%25E5%25B1%2580%25E9%2585%258D%25E7%25BD%25AE" target="_blank" rel="nofollow noopener noreferrer" title="https://element-plus.gitee.io/zh-CN/guide/quickstart.html#%E5%85%A8%E5%B1%80%E9%85%8D%E7%BD%AE" ref="nofollow noopener noreferrer">配置尺寸和层级</a>，以及如何<a href="https://link.juejin.cn/?target=https%3A%2F%2Felement-plus.gitee.io%2Fzh-CN%2Fguide%2Fi18n.html%23configprovider" target="_blank" rel="nofollow noopener noreferrer" title="https://element-plus.gitee.io/zh-CN/guide/i18n.html#configprovider" ref="nofollow noopener noreferrer">设置国际化</a>，我们这里需要设置默认语言为中文，组件尺寸和层级使用默认即可。</p>
<p>我们找到根组件<code>App.vue</code>，在顶层组件外面包上elemnt的全局配置注入组件，然后引入框架内置i18n的中文配置，按照下面代码就可以实现组件默认语言为中文了，后面我们会在这个基础上进行修改，结合vue-i18n来实现多语言切换。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> zhCn <span class="hljs-keyword">from</span> <span class="hljs-string">'element-plus/lib/locale/lang/zh-cn'</span>;
<span class="hljs-keyword">const</span> locale = zhCn;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">el-config-provider</span> <span class="hljs-attr">:locale</span>=<span class="hljs-string">"locale"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-view</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">el-config-provider</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">关于使用以及自动生成的文件</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b99560cad8e040dd9b46472377735786~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="auto_import.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用组件很简单，由于配置了自动导入插件，所以可以全局使用插件，我们在<code>LoginView.vue</code>的文件中，将之前的按钮改为element按钮组件，然后保存，之后插件就会自动添加引用到配置文件中（自动生成的文件），由于这两个文件是自动生成的（如上图所示），所以不需要提交到git中，我们在<code>.gitignore</code>文件中将两个文件名配置，不去记录这两个文件，也不需要上传，因为自动导出插件会帮我们生成配置文件，引用了那些组件就会按需加载那些组件配置，添加忽略的两个配置文件如下。</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-comment"># Logs</span>
logs
*.<span class="hljs-built_in">log</span>
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.<span class="hljs-built_in">local</span>

<span class="hljs-comment"># Editor directories and files</span>
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

<span class="hljs-comment">## Element自动导入配置文件忽略</span>
auto-imports.d.ts
components.d.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在使用自动导入插件的过程中，有几个需要注意的地方：</p>
<ol>
<li>如果在<code><template></template></code>模板内没有使用组件，而在<strong>JSX</strong>或是<strong>TSX</strong>中使用了，需要通过<code>import</code>的方式按需引入组件，自动导入插件不会扫描<strong>JSX</strong>或是<strong>TSX</strong>代码中的Element组件的。</li>
<li>如果使用了ElMessage组件或是通知类组件，自动导入插件也不会帮我们导入css样式文件，因为组件自动导入也伴随样式自动导入，所以我们需要在<code>main.ts</code>中添加<code>import 'element-plus/dist/index.css';</code>来完成element的样式导入，这些在TS或JS代码中引用了Element组件却没有自动导入样式就会导致Element组件不能使用或是渲染错误。</li>
</ol>
</blockquote>
<h1 data-id="heading-6"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue-i18n.intlify.dev" target="_blank" rel="nofollow noopener noreferrer" title="https://vue-i18n.intlify.dev" ref="nofollow noopener noreferrer">vue-i18n的安装与使用</a></h1>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-comment"># 国际化插件</span>
npm i vue-i18n
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">封装vue-i18n(语言配置)</h1>
<p>首先在./src文件夹下面创建一个i18n的文件夹，创建index.ts文件，然后写入下面代码配置。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// ./src/i18n/index.ts</span>
<span class="hljs-keyword">import</span> &#123; createI18n &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-i18n'</span>;
<span class="hljs-keyword">import</span> &#123; themeConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/config'</span>;
<span class="hljs-comment">// element-plus 的ui框架国际化语言配置</span>
<span class="hljs-keyword">import</span> zhCnLocale <span class="hljs-keyword">from</span> <span class="hljs-string">'element-plus/lib/locale/lang/zh-cn'</span>;
<span class="hljs-keyword">import</span> enLocale <span class="hljs-keyword">from</span> <span class="hljs-string">'element-plus/lib/locale/lang/en'</span>;
<span class="hljs-comment">// 自定义的语言配置</span>
<span class="hljs-keyword">import</span> nextZhCn <span class="hljs-keyword">from</span> <span class="hljs-string">'./lang/zh-cn'</span>;
<span class="hljs-keyword">import</span> nextEn <span class="hljs-keyword">from</span> <span class="hljs-string">'./lang/en'</span>;
<span class="hljs-comment">// 按照每个页面的语言配置</span>
<span class="hljs-keyword">import</span> loginZhcn <span class="hljs-keyword">from</span> <span class="hljs-string">'./pages/login/zh-cn'</span>;
<span class="hljs-keyword">import</span> loginEn <span class="hljs-keyword">from</span> <span class="hljs-string">'./pages/login/en'</span>;

<span class="hljs-comment">// 定义语言国际化内容 zh-cn en</span>
<span class="hljs-keyword">const</span> messages = &#123;
[zhCnLocale.<span class="hljs-property">name</span>]: &#123;
...zhCnLocale,
<span class="hljs-attr">ismsg</span>: &#123; ...nextZhCn, ...loginZhcn &#125;,
&#125;,
[enLocale.<span class="hljs-property">name</span>]: &#123;
...enLocale,
<span class="hljs-attr">ismsg</span>: &#123; ...nextEn, ...loginEn &#125;,
&#125;,
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> i18n = <span class="hljs-title function_">createI18n</span>(&#123;
<span class="hljs-attr">silentTranslationWarn</span>: <span class="hljs-literal">true</span>,
<span class="hljs-attr">missingWarn</span>: <span class="hljs-literal">false</span>,
<span class="hljs-attr">silentFallbackWarn</span>: <span class="hljs-literal">true</span>,
<span class="hljs-attr">fallbackWarn</span>: <span class="hljs-literal">false</span>,
<span class="hljs-attr">locale</span>: themeConfig.<span class="hljs-property">value</span>.<span class="hljs-property">globalI18n</span>, <span class="hljs-comment">// 采用全局参数配置初始化语言 项目中有`zh-cn`、`en`两种</span>
<span class="hljs-attr">fallbackLocale</span>: zhCnLocale.<span class="hljs-property">name</span>,
messages,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其余配置语言文件可以转到项目文件中查看配置，例如<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fzero-dg%2Fdeduction-frontend%2Fblob%2Fmain%2Fsrc%2Fi18n%2Flang%2Fzh-cn.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/zero-dg/deduction-frontend/blob/main/src/i18n/lang/zh-cn.ts" ref="nofollow noopener noreferrer">自定义的中文配置</a>，我们自定义的语言配置全部设置在<code>ismsg</code>下面，最后合并语言配置导出i18n实例化的对象，然后全局注册国际化插件，将i18n实例注册到vue app实例中。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// ./src/main.ts</span>
<span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'@/App.vue'</span>;
<span class="hljs-keyword">import</span> &#123; i18n &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/i18n'</span>;

<span class="hljs-keyword">const</span> app = <span class="hljs-title function_">createApp</span>(<span class="hljs-title class_">App</span>);

app.<span class="hljs-title function_">use</span>(i18n)
app.<span class="hljs-title function_">mount</span>(<span class="hljs-string">'#app'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">element-plus自动导入组件如何结合vue-i18n？</h1>
<p>因为项目中element-plus采用的是按需自动注册组件，网上找了一下没有找到element-plus结合vue-i18n的方法，查看了一下vue-i18n的实例内置方法属性，然后又参照element官网国际化的方法，结合了一下做了如下修改，在根组件使用 <code>ConfigProvider</code> 组件包裹页面入口的<code><router-view /></code>，这样就可以实现element-plus组件的全局统一默认配置。</p>
<p>代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, watchEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> &#123; themeConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./config'</span>;
<span class="hljs-keyword">import</span> &#123; useI18n &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-i18n'</span>;

<span class="hljs-comment">// 获取实例</span>
<span class="hljs-keyword">const</span> &#123; messages, locale &#125;: any = <span class="hljs-title function_">useI18n</span>();
<span class="hljs-keyword">const</span> localeLang = <span class="hljs-title function_">ref</span>(messages[themeConfig.<span class="hljs-property">value</span>.<span class="hljs-property">globalI18n</span>]); <span class="hljs-comment">// 默认语言</span>

<span class="hljs-comment">// 修改element 和 i18n 默认语言</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">changeLanguage</span> = (<span class="hljs-params"></span>) => &#123;
locale.<span class="hljs-property">value</span> = themeConfig.<span class="hljs-property">value</span>.<span class="hljs-property">globalI18n</span>;
localeLang.<span class="hljs-property">value</span> = messages.<span class="hljs-property">value</span>[locale.<span class="hljs-property">value</span>];
&#125;;
<span class="hljs-comment">// 监听修改语言</span>
<span class="hljs-title function_">watchEffect</span>(changeLanguage);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">el-config-provider</span> <span class="hljs-attr">:locale</span>=<span class="hljs-string">"localeLang"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-view</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">el-config-provider</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-keyword">@import</span> <span class="hljs-string">'./theme/index.css'</span>;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>themeConfig.value.globalI18n</code>的响应式不能直接作用于i18n的local设置，所以设置了监听属性，如果<code>themeConfig.value.globalI18n</code>发生修改，会触发<code>changeLanguage</code>方法，从而修改element-plus和自定义的国际化语言切换，从而实现通过监听一个变量变更来完成语言切换设置。</p>
<p>全局配置使用响应式的变量结构，目前只有语言设置这一个参数，默认中文。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//  ./src/config/index.js</span>
<span class="hljs-keyword">import</span> &#123; ref, watchEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> themeConfig = <span class="hljs-title function_">ref</span>(&#123;
<span class="hljs-comment">// 默认初始语言，可选值"<zh-cn|en>"，默认 zh-cn</span>
<span class="hljs-attr">globalI18n</span>: <span class="hljs-string">'zh-cn'</span>,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">在项目中使用</h1>
<p>下面是自定义的语言配置文件</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// ./src/i18n/lang/en.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
<span class="hljs-attr">router</span>: &#123;
<span class="hljs-attr">home</span>: <span class="hljs-string">'home'</span>,
<span class="hljs-attr">docsLink</span>: <span class="hljs-string">'System Docs '</span>,
&#125;,
<span class="hljs-attr">header</span>: &#123;
<span class="hljs-attr">userCenter</span>: <span class="hljs-string">'Personal Center'</span>,
<span class="hljs-attr">codeSource</span>: <span class="hljs-string">'Code Warehouse'</span>,
<span class="hljs-attr">systemGuide</span>: <span class="hljs-string">'System Guide'</span>,
<span class="hljs-attr">logOut</span>: <span class="hljs-string">'Log Out'</span>,
&#125;,
&#125;;
<span class="hljs-comment">// ./src/i18n/lang/zh-cn.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
<span class="hljs-attr">router</span>: &#123;
<span class="hljs-attr">home</span>: <span class="hljs-string">'首页'</span>,
<span class="hljs-attr">docsLink</span>: <span class="hljs-string">'系统指南'</span>,
&#125;,
<span class="hljs-attr">header</span>: &#123;
<span class="hljs-attr">userCenter</span>: <span class="hljs-string">'个人中心'</span>,
<span class="hljs-attr">codeSource</span>: <span class="hljs-string">'代码仓库'</span>,
<span class="hljs-attr">systemGuide</span>: <span class="hljs-string">'系统指南'</span>,
<span class="hljs-attr">logOut</span>: <span class="hljs-string">'退出登录'</span>,
&#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>$t</code>是i18n注入的一个函数，直接在模板中使用即可，ts脚本中需要使用useI18n获取到t(语言转换函数)，或者通过i18n实例下的global属性获取t函数。</p>
<p>在vue文件中使用方法如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; useI18n &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-i18n'</span>;
<span class="hljs-keyword">import</span> &#123; i18n &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/i18n'</span>;
<span class="hljs-comment">// 获取实例</span>
<span class="hljs-keyword">const</span> &#123; t &#125;: any = <span class="hljs-title function_">useI18n</span>();
<span class="hljs-comment">// 或者</span>
<span class="hljs-keyword">const</span> t = i18n.<span class="hljs-property">global</span>.<span class="hljs-property">t</span>;
<span class="hljs-comment">/* 
  这里为了举例都定义为t
  可以更改为别名，方法如下
  const &#123; t: otherT &#125;: any = useI18n();
  const otherT = i18n.global.t;
 */</span>
<span class="hljs-comment">// 在脚本中如下方法使用</span>
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-title function_">t</span>(<span class="hljs-string">'ismsg.router.home'</span>))
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
&#123;&#123; $t('ismsg.router.home') &#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>本项目编写过程中，在登录页面使用了国际化配置，对于element表单验证提示语采用语言转换时发现失效了，无法转换语言，使用了reactive、ref来定义的rules(表单规则结构)，猜测是因为没有对转换函数<code>t</code>实现响应式监听或是响应式失效了，根本原因不太清楚，将reactive或是ref替换为计算钩子函数(computed)即可，然后切换语言的时候提示语也可以正常切换了。</p>
</blockquote>
<p>本文可能讲述的不够清晰，只是简单的配置多语言，i18n还有很多种语言替换的方法都没有讲到，可自行查阅博文学习。配置国际化的方法最好自己动手实现一遍，可以结合本项目具体学习，以上讲解所用代码是在项目源码的基础上做了修改而来，具体实现过程可以查看本项目的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fzero-dg%2Fdeduction-frontend" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/zero-dg/deduction-frontend" ref="nofollow noopener noreferrer">源代码</a>。</p>
<h1 data-id="heading-10">结语</h1>
<p>本文是基于之前写的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzero-dg.gitee.io%2Fis-deduction-docs%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://zero-dg.gitee.io/is-deduction-docs/" ref="nofollow noopener noreferrer">集成系统教程</a>而来，后期在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fzero-dg%2Fdeduction-frontend" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/zero-dg/deduction-frontend" ref="nofollow noopener noreferrer">项目实践</a>中，对代码还做了许多修改的地方，可能与本文有所出入，但是结合使用的方法本质上还是一样的，本文内容全部基于亲自实践所得，如果对您有帮助，劳烦点赞支持一下作者，如果文章内有错误之处还望指正，希望大家可以共同进步٩(๑❛ᴗ❛๑)۶。</p></div>  
</div>
            