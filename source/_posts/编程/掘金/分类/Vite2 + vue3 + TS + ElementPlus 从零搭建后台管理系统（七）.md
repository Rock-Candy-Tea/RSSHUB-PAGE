
---
title: 'Vite2 + vue3 + TS + ElementPlus 从零搭建后台管理系统（七）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7051'
author: 掘金
comments: false
date: Wed, 19 May 2021 22:29:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=7051'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>上一章主要完成了 添加 mockjs模拟数据 <a href="https://juejin.cn/post/6963469358936883231" target="_blank">Vite2 + vue3 + TS + ElementPlus 从零搭建后台管理系统（六）</a></p>
<p>这一章将完善配置文件，以及添加常用插件</p>
<h3 data-id="heading-0">1. 获取 .env 配置的环境变量</h3>
<p>在项目中可以通过 import.meta.env 来获取到 .env.*文件中的环境变量</p>
<p>但是 import.meta.env 在 vite.config.ts 配置文件中使用不了</p>
<p>这里先在 vite.config.ts 中拿到环境变量参数</p>
<ul>
<li>修改 .env.development 文件:</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts">
VITE_PORT = <span class="hljs-number">60001</span>

VITE_USE_MOCK = <span class="hljs-literal">true</span>

VITE_GLOB_APP_TITLE = Vue3-ElementPlus-Vite2

VITE_GLOB_API_URL = /basic-api

VITE_PUBLIC_PATH = /

VITE_BUILD_COMPRESS = <span class="hljs-string">'none'</span>

VITE_BUILD_COMPRESS_DELETE_ORIGIN_FILE = <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>.env.production 文件 后面同 .env.development文件做相应修改</p>
<ul>
<li>新增 src/utils/env.ts 文件 处理环境变量</li>
</ul>
<p>env.ts：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrapperEnv</span>(<span class="hljs-params">envConf: Recordable</span>): <span class="hljs-title">ViteEnv</span> </span>&#123;
  <span class="hljs-keyword">const</span> ret: <span class="hljs-built_in">any</span> = &#123;&#125;;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> envName <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.keys(envConf)) &#123;
    <span class="hljs-keyword">let</span> realName = envConf[envName].replace(<span class="hljs-regexp">/\\n/g</span>, <span class="hljs-string">'\n'</span>);
    realName = realName === <span class="hljs-string">'true'</span> ? <span class="hljs-literal">true</span> : realName === <span class="hljs-string">'false'</span> ? <span class="hljs-literal">false</span> : realName;

    <span class="hljs-keyword">if</span> (envName === <span class="hljs-string">'VITE_PORT'</span>) &#123;
      realName = <span class="hljs-built_in">Number</span>(realName);
    &#125;
    ret[envName] = realName;
    process.env[envName] = realName;
  &#125;
  <span class="hljs-keyword">return</span> ret;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 vite.config.ts 文件中引入 wrapperEnv，并且从'vite'中引入 loadEnv ：</p>
<blockquote>
<p>import &#123; wrapperEnv &#125; from './src/utils/env'</p>
</blockquote>
<blockquote>
<p>import &#123; defineConfig, ConfigEnv, UserConfigExport, loadEnv &#125; from 'vite'</p>
</blockquote>
<p>然后通过 loadEnv 和 wrapperEnv 最终可获取到环境变量的组成的对象 viteEnv ：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (&#123; command, mode &#125;: ConfigEnv): <span class="hljs-function"><span class="hljs-params">UserConfigExport</span> =></span> &#123;
  <span class="hljs-keyword">const</span> isBuild = command === <span class="hljs-string">'build'</span>

  <span class="hljs-keyword">const</span> root = process.cwd() <span class="hljs-comment">// 新增</span>
  <span class="hljs-keyword">const</span> env = loadEnv(mode, root) <span class="hljs-comment">// 新增</span>
  <span class="hljs-keyword">const</span> viteEnv = wrapperEnv(env) <span class="hljs-comment">// 新增</span>
  <span class="hljs-keyword">const</span> &#123;
    VITE_PORT,
    VITE_USE_MOCK,
    VITE_BUILD_COMPRESS,
    VITE_BUILD_COMPRESS_DELETE_ORIGIN_FILE
  &#125; = viteEnv <span class="hljs-comment">// 新增</span>

  <span class="hljs-keyword">return</span> defineConfig(&#123;
    ......
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2. 添加 vite-plugin-svg-icons</h3>
<ul>
<li>vite-plugin-svg-icons：处理 svg/icon 图片插件</li>
</ul>
<p>之前 svgBuilder 也实现了 处理 svg/icon 图片插件，实现的比较粗糙，但是能了解到vite 插件开发的思路。这里可以先删除 src/plugins/svgBuilder.js</p>
<ul>
<li>安装</li>
</ul>
<blockquote>
<p>npm install vite-plugin-svg-icons -D</p>
</blockquote>
<ul>
<li>在 src/plugins目录下新增：configSvgIconsPlugin.ts</li>
</ul>
<p>configSvgIconsPlugin.ts：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 *  Vite Plugin for fast creating SVG sprites.
 * https://github.com/anncwb/vite-plugin-svg-icons
 */</span>
 <span class="hljs-keyword">import</span> <span class="hljs-keyword">type</span> &#123; Plugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>;
<span class="hljs-keyword">import</span> SvgIconsPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-svg-icons'</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configSvgIconsPlugin</span>(<span class="hljs-params">isBuild: <span class="hljs-built_in">boolean</span></span>):<span class="hljs-title">Plugin</span> </span>&#123;
  <span class="hljs-keyword">const</span> svgIconsPlugin:Plugin = SvgIconsPlugin(&#123;
    <span class="hljs-attr">iconDirs</span>: [path.resolve(process.cwd(), <span class="hljs-string">'src/assets/icons'</span>)],
    <span class="hljs-attr">svgoOptions</span>: isBuild,
    <span class="hljs-comment">// default</span>
    <span class="hljs-attr">symbolId</span>: <span class="hljs-string">'icon-[dir]-[name]'</span>,
  &#125;);
  <span class="hljs-keyword">return</span> svgIconsPlugin;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 vite.config.ts 文件中引入 configSvgIconsPlugin ，在 plugins 中使用</p>
<blockquote>
<p>import &#123; configSvgIconsPlugin &#125; from './src/plugins/configSvgIconsPlugin'</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts">plugins:[
  ...
  configSvgIconsPlugin(isBuild)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>插件使用文档看这里：<a href="https://github.com/anncwb/vite-plugin-svg-icons" target="_blank" rel="nofollow noopener noreferrer">vite-plugin-svg-icons</a></p>
<h3 data-id="heading-2">3. 完善 vite-plugin-style-import</h3>
<ul>
<li>vite-plugin-style-import：按需加载组件库插件</li>
</ul>
<p>目前 element-plus 按需加载使用的插件 vite-plugin-style-import的方式不太优雅，这里优化一下</p>
<ul>
<li>
<p>先删除 styleImport 相关代码</p>
</li>
<li>
<p>安装</p>
</li>
</ul>
<blockquote>
<p>npm install vite-plugin-style-import -D</p>
</blockquote>
<ul>
<li>再在 src/plugins目录下新增：configStyleImportPlugin.ts</li>
</ul>
<p>configStyleImportPlugin.ts：</p>
<pre><code class="hljs language-ts copyable" lang="ts"> <span class="hljs-keyword">import</span> <span class="hljs-keyword">type</span> &#123; Plugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>;
 <span class="hljs-keyword">import</span> styleImport <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-style-import'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configStyleImportPlugin</span>(<span class="hljs-params">isBuild?: <span class="hljs-built_in">boolean</span></span>):<span class="hljs-title">Plugin</span></span>&#123;
  <span class="hljs-keyword">return</span> styleImport(&#123;
    <span class="hljs-attr">libs</span>: [
      &#123;
        <span class="hljs-attr">libraryName</span>: <span class="hljs-string">'element-plus'</span>,
        <span class="hljs-attr">esModule</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">ensureStyleFile</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">resolveStyle</span>: <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
          name = name.slice(<span class="hljs-number">3</span>)
          <span class="hljs-keyword">return</span> <span class="hljs-string">`element-plus/packages/theme-chalk/src/<span class="hljs-subst">$&#123;name&#125;</span>.scss`</span>
        &#125;,
        <span class="hljs-attr">resolveComponent</span>: <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-string">`element-plus/lib/<span class="hljs-subst">$&#123;name&#125;</span>`</span>
        &#125;
      &#125;
    ]
  &#125;) 
&#125; 

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 vite.config.ts 文件中引入 configStyleImportPlugin ，在 plugins 中使用</p>
<blockquote>
<p>import &#123; configStyleImportPlugin &#125; from './src/plugins/configStyleImportPlugin'</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts">plugins:[
  ...
  configStyleImportPlugin(isBuild)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>插件使用文档看这里：<a href="https://github.com/anncwb/vite-plugin-style-import" target="_blank" rel="nofollow noopener noreferrer">vite-plugin-style-import</a></p>
<h3 data-id="heading-3">4. 添加 vite-plugin-html</h3>
<ul>
<li>vite-plugin-html： html 中 EJS 标签处理</li>
</ul>
<p>这个 插件可以在 在 index.html 中增加 EJS 标签，例如：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"icon"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/favicon.ico"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span><%- title %><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <%- injectScript %>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 title 和 injectScript 就是可以注入的数据</p>
<ul>
<li>安装</li>
</ul>
<blockquote>
<p>npm install vite-plugin-html -D</p>
</blockquote>
<ul>
<li>在 src/plugins目录下新增： configHtmlPlugin.ts</li>
</ul>
<p>configHtmlPlugin.ts：</p>
<pre><code class="hljs language-ts copyable" lang="ts"> <span class="hljs-keyword">import</span> <span class="hljs-keyword">type</span> &#123; Plugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>;

 <span class="hljs-keyword">import</span> html <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-html'</span>;
 
 <span class="hljs-keyword">import</span> pkg <span class="hljs-keyword">from</span> <span class="hljs-string">'../../package.json'</span>;


 <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configHtmlPlugin</span>(<span class="hljs-params">env: ViteEnv, isBuild: <span class="hljs-built_in">boolean</span></span>) </span>&#123;
   <span class="hljs-keyword">const</span> &#123; VITE_GLOB_APP_TITLE, VITE_PUBLIC_PATH &#125; = env;
 
   <span class="hljs-keyword">const</span> path = VITE_PUBLIC_PATH.endsWith(<span class="hljs-string">'/'</span>) ? VITE_PUBLIC_PATH : <span class="hljs-string">`<span class="hljs-subst">$&#123;VITE_PUBLIC_PATH&#125;</span>/`</span>;
 
   <span class="hljs-keyword">const</span> getAppConfigSrc = <span class="hljs-function">() =></span> &#123;
     <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;path || <span class="hljs-string">'/'</span>&#125;</span>_app.config.js?v=<span class="hljs-subst">$&#123;pkg.version&#125;</span>-<span class="hljs-subst">$&#123;<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()&#125;</span>`</span>;
   &#125;;

   <span class="hljs-keyword">const</span> htmlPlugin: Plugin[] = html(&#123;
     <span class="hljs-attr">minify</span>: isBuild,
     <span class="hljs-attr">inject</span>: &#123;
       <span class="hljs-comment">// Inject data into ejs template</span>
       <span class="hljs-attr">injectData</span>: &#123;
         <span class="hljs-attr">title</span>: VITE_GLOB_APP_TITLE,
       &#125;,
       <span class="hljs-comment">// Embed the generated app.config.js file</span>
       <span class="hljs-attr">tags</span>: isBuild?[
            &#123;
            <span class="hljs-attr">tag</span>: <span class="hljs-string">'script'</span>,
            <span class="hljs-attr">attrs</span>: &#123;
              <span class="hljs-attr">src</span>: getAppConfigSrc(),
            &#125;,
          &#125;,
        ]:[]
     &#125;,
   &#125;);
   <span class="hljs-keyword">return</span> htmlPlugin;
 &#125;
 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 vite.config.ts 文件中引入 configHtmlPlugin ，在 plugins 中使用</p>
<blockquote>
<p>import &#123; configHtmlPlugin &#125; from './src/plugins/configHtmlPlugin'</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts">plugins:[
  ...
  configHtmlPlugin(viteEnv, isBuild),
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>插件使用文档看这里：<a href="https://github.com/anncwb/vite-plugin-html" target="_blank" rel="nofollow noopener noreferrer">vite-plugin-html</a></p>
<h3 data-id="heading-4">5. 添加 vite-plugin-compression</h3>
<ul>
<li>vite-plugin-compression： 资源压缩插件</li>
</ul>
<ul>
<li>安装</li>
</ul>
<blockquote>
<p>npm install vite-plugin-compression -D</p>
</blockquote>
<ul>
<li>在 src/plugins目录下新增： configCompressPlugin.ts</li>
</ul>
<p>configCompressPlugin.ts：</p>
<pre><code class="hljs language-ts copyable" lang="ts"> <span class="hljs-keyword">import</span> <span class="hljs-keyword">type</span> &#123; Plugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>;

 <span class="hljs-keyword">import</span> compressPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-compression'</span>;
 
 <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configCompressPlugin</span>(<span class="hljs-params">
   compress: <span class="hljs-string">'gzip'</span> | <span class="hljs-string">'brotli'</span> | <span class="hljs-string">'none'</span>,
   deleteOriginFile: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>
 </span>): <span class="hljs-title">Plugin</span> | <span class="hljs-title">Plugin</span>[] </span>&#123;
   <span class="hljs-keyword">const</span> compressList = compress.split(<span class="hljs-number">0</span>);
 
   <span class="hljs-keyword">const</span> plugins: Plugin[] = [];
 
   <span class="hljs-keyword">if</span> (compressList.includes(<span class="hljs-string">'gzip'</span>)) &#123;
     plugins.push(
       compressPlugin(&#123;
         <span class="hljs-attr">ext</span>: <span class="hljs-string">'.gz'</span>,
         deleteOriginFile,
       &#125;)
     );
   &#125;
   <span class="hljs-keyword">if</span> (compressList.includes(<span class="hljs-string">'brotli'</span>)) &#123;
     plugins.push(
       compressPlugin(&#123;
         <span class="hljs-attr">ext</span>: <span class="hljs-string">'.br'</span>,
         <span class="hljs-attr">algorithm</span>: <span class="hljs-string">'brotliCompress'</span>,
         deleteOriginFile,
       &#125;)
     );
   &#125;
   <span class="hljs-keyword">return</span> plugins;
 &#125;
 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 vite.config.ts 文件中引入 configCompressPlugin ，在 plugins 中使用</p>
<blockquote>
<p>import &#123; configCompressPlugin &#125; from './src/plugins/configCompressPlugin'</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts">plugins:[
  ...
  configCompressPlugin( VITE_BUILD_COMPRESS, VITE_BUILD_COMPRESS_DELETE_ORIGIN_FILE)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>插件使用文档看这里：<a href="https://github.com/anncwb/vite-plugin-compression" target="_blank" rel="nofollow noopener noreferrer">vite-plugin-compression</a></p>
<h3 data-id="heading-5">6. 添加全局 TS 类型声明</h3>
<p>在configHtmlPlugin.ts 文件中使用了 ViteEnv 类型声明但是未声明，现在来添加</p>
<ul>
<li>在根目录下新增： types/global.d.ts</li>
</ul>
<p>global.d.ts：</p>
<pre><code class="hljs language-ts copyable" lang="ts">
<span class="hljs-keyword">declare</span> <span class="hljs-keyword">type</span> Recordable<T = <span class="hljs-built_in">any</span>> = Record<<span class="hljs-built_in">string</span>, T>

<span class="hljs-keyword">interface</span> ImportMetaEnv <span class="hljs-keyword">extends</span> ViteEnv &#123;
  <span class="hljs-attr">__</span>: unknown
&#125;

<span class="hljs-keyword">declare</span> <span class="hljs-keyword">interface</span> ViteEnv &#123;
  <span class="hljs-attr">VITE_GLOB_APP_TITLE</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">VITE_PUBLIC_PATH</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">VITE_GLOB_API_URL</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">VITE_PORT</span>: <span class="hljs-built_in">number</span>
  <span class="hljs-attr">VITE_USE_MOCK</span>: <span class="hljs-built_in">boolean</span>
  <span class="hljs-attr">VITE_BUILD_COMPRESS</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">VITE_BUILD_COMPRESS_DELETE_ORIGIN_FILE</span>: <span class="hljs-built_in">boolean</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是会发现使用了 ViteEnv 地方还是有错误提示：
解决办法：修改 tsconfig.json 配置项 typeRoots 和 include</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  compilerOptions:&#123;
    ...
     <span class="hljs-attr">"typeRoots"</span>: [<span class="hljs-string">"./node_modules/@types/"</span>, <span class="hljs-string">"./types"</span>],<span class="hljs-comment">// 声明文件目录，默认时node_modules/@types</span>
     <span class="hljs-attr">"include"</span>: [
      <span class="hljs-string">"src/**/*.ts"</span>,
      <span class="hljs-string">"src/**/*.d.ts"</span>,
      <span class="hljs-string">"src/**/*.tsx"</span>,
      <span class="hljs-string">"src/**/*.vue"</span>, 
      <span class="hljs-string">"mock/**/*.ts"</span>,
      <span class="hljs-string">"types/**/*.d.ts"</span>,
      <span class="hljs-string">"types/**/*.ts"</span>,
    ]
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如此就可以在 global.d.ts 中写一些全局的类型声明了</p>
<h3 data-id="heading-6">最后</h3>
<p>到目前为止，基本完善了后台管理系统环境配置。</p>
<p>欢迎大家的指点，期待你的点赞哦。😄😄😄</p></div>  
</div>
            