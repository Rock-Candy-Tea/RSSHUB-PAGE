
---
title: 'vite2 常用插件篇（二）- 优化插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9155'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 00:41:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=9155'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0"><code>vite2</code>常用插件篇（二）- 优化插件</h1>
<p>上一篇文章<a href="https://juejin.cn/post/6993699163263221797" target="_blank" title="https://juejin.cn/post/6993699163263221797">vite2 常用插件篇（一）- 基础插件</a>主要讲了<code>vite</code>插件集成的准备和几个基础插件，这篇文章讲下另外几个常用的基础插件</p>
<h2 data-id="heading-1">一、<code>vite-plugin-html</code></h2>
<h3 data-id="heading-2">1.说明</h3>
<p><code>npm</code>: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvite-plugin-html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/vite-plugin-html" ref="nofollow noopener noreferrer">vite-plugin-html</a></p>
<p><code>git</code>: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fanncwb%2Fvite-plugin-html" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/anncwb/vite-plugin-html" ref="nofollow noopener noreferrer">vite-plugin-html</a></p>
<p>原文：</p>
<p>一个为<code>index.html</code>提供<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fhtml-minifier-terser" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/html-minifier-terser" ref="nofollow noopener noreferrer">minify</a>和基于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fejs.bootcss.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ejs.bootcss.com/" ref="nofollow noopener noreferrer">EJS</a>模板功能的Vite插件。</p>
<ul>
<li>minify：压缩<code>index.html</code>代码。</li>
<li>EJS：给<code>index.html</code>提供访问变量的能力。</li>
</ul>
<p>详情看配置和使用。</p>
<p>另外这个插件可以在 在 <code>index.html</code> 中增加 <code>EJS</code> 标签，例如：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"icon"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/favicon.ico"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span><%- title %><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <%- injectScript %>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>title</code> 和 <code>injectScript</code> 就是可以注入的数据</p>
<h3 data-id="heading-3">2.安装</h3>
<pre><code class="hljs language-bash copyable" lang="bash">yarn add vite-plugin-html --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3.创建配置文件</h3>
<p><code>build/vite/plugin/html.ts</code></p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> <span class="hljs-keyword">type</span> &#123; Plugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>;
<span class="hljs-keyword">import</span> html <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-html'</span>;
<span class="hljs-keyword">import</span> &#123; GLOB_CONFIG_FILE_NAME &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../../constant'</span>;
<span class="hljs-keyword">import</span> pkg <span class="hljs-keyword">from</span> <span class="hljs-string">'../../../package.json'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configHtmlPlugin</span>(<span class="hljs-params">env: ViteEnv, isBuild: <span class="hljs-built_in">boolean</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">VITE_GLOB_APP_TITLE</span>: appTitle, <span class="hljs-attr">VITE_PUBLIC_PATH</span>: publicPath = <span class="hljs-string">'./'</span> &#125; = env;

  <span class="hljs-keyword">const</span> path = publicPath.endsWith(<span class="hljs-string">'/'</span>) ? publicPath : <span class="hljs-string">`<span class="hljs-subst">$&#123;publicPath&#125;</span>/`</span>;

  <span class="hljs-keyword">const</span> getAppConfigSrc = <span class="hljs-function">() =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;path || <span class="hljs-string">'/'</span>&#125;</span><span class="hljs-subst">$&#123;GLOB_CONFIG_FILE_NAME&#125;</span>?v=<span class="hljs-subst">$&#123;pkg.version&#125;</span>-<span class="hljs-subst">$&#123;<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()&#125;</span>`</span>;

  <span class="hljs-keyword">const</span> htmlPlugin: Plugin[] = html(&#123;
    <span class="hljs-attr">minify</span>: isBuild,
    <span class="hljs-attr">inject</span>: &#123;
      <span class="hljs-comment">// Inject data into ejs template</span>
      <span class="hljs-attr">injectData</span>: &#123;
        <span class="hljs-attr">title</span>: appTitle,
      &#125;,
      <span class="hljs-comment">// Embed the generated app.config.js file</span>
      <span class="hljs-attr">tags</span>: isBuild
        ? [
          &#123;
            <span class="hljs-attr">tag</span>: <span class="hljs-string">'script'</span>,
            <span class="hljs-attr">attrs</span>: &#123;
              <span class="hljs-attr">src</span>: getAppConfigSrc(),
            &#125;,
          &#125;,
        ]
        : [],
    &#125;,
  &#125;);
  <span class="hljs-keyword">return</span> htmlPlugin;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">4.配置Vite插件</h3>
<p><code>build/vite/plugin/index.ts</code></p>
<pre><code class="copyable">// ...
import &#123; configHtmlPlugin &#125; from './html';

export function createVitePlugins(viteEnv: ViteEnv, isBuild: boolean) &#123;
  // ...
  // vite-plugin-html
  vitePlugins.push(configHtmlPlugin(viteEnv, isBuild));
  // ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">二、<code>vite-plugin-svg-icon</code></h2>
<h3 data-id="heading-7">1.说明</h3>
<p><code>npm</code>： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvite-plugin-html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/vite-plugin-html" ref="nofollow noopener noreferrer">vite-plugin-svg-icons</a></p>
<p><code>git</code>： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fanncwb%2Fvite-plugin-svg-icons" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/anncwb/vite-plugin-svg-icons" ref="nofollow noopener noreferrer">vite-plugin-svg-icons</a></p>
<p>当我们遇到首屏需要性能优化时，比如有很多<code>http</code>请求场景下，用这个插件就不会再产生<code>http</code>请求来渲染出<code>svg</code>图片。</p>
<h4 data-id="heading-8">怎么做到的呢？</h4>
<p>使用该插件时，插件会自动将所有<code>svg</code>图片加载到<code>HTML</code>中。并且每一个<code>svg</code>将会被过滤去无用的信息数据。让<code>svg</code>达到最小的值。之后使用<code>svg</code>图片就只需要操作<code>DOM</code>即可，而不需要发送<code>http</code>请求。</p>
<p>当使用该插件的时候，指定好存放<code>svg</code>的文件夹。再按照指定的方式去访问<code>svg</code>图片。</p>
<h3 data-id="heading-9">2.安装</h3>
<pre><code class="hljs language-bash copyable" lang="bash">yarn add vite-plugin-svg-icons --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">3.创建配置</h3>
<p><code>build/vite/plugin/svgSprite.ts</code></p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> SvgIconsPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-svg-icons'</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configSvgIconsPlugin</span>(<span class="hljs-params">isBuild: <span class="hljs-built_in">boolean</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> svgIconsPlugin = SvgIconsPlugin(&#123;
    <span class="hljs-attr">iconDirs</span>: [path.resolve(process.cwd(), <span class="hljs-string">'src/assets/svg'</span>)],
    <span class="hljs-attr">svgoOptions</span>: isBuild,
    <span class="hljs-comment">// default</span>
    <span class="hljs-attr">symbolId</span>: <span class="hljs-string">'icon-[dir]-[name]'</span>,
  &#125;);
  <span class="hljs-keyword">return</span> svgIconsPlugin;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>选项<code>svgOptions</code>的<code>boolean</code>类型不太清楚是干什么的。但是对象类型是控制<code>svg</code>过滤无用信息的选项。使用<code>true</code>是使用默认选项，<code>false</code>时不知道做什么的但是也没什么影响。</p>
</blockquote>
<h3 data-id="heading-11">4.用于配置</h3>
<p><code>build/vite/plugin/index.ts</code></p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// ...</span>
<span class="hljs-keyword">import</span> &#123; configSvgIconsPlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./svgSprite'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createVitePlugins</span>(<span class="hljs-params">viteEnv: ViteEnv, isBuild: <span class="hljs-built_in">boolean</span></span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// vite-plugin-svg-icons</span>
  vitePlugins.push(configSvgIconsPlugin(isBuild));
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">return</span> vitePlugins;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">5.main导入</h3>
<p><code>src/main.ts</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'vite-plugin-svg-icons/register'</span>;
<span class="hljs-comment">// ...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">6.创建Svg组件</h3>
<pre><code class="hljs language-bash copyable" lang="bash">src/components/Icon/src/SvgIcon.vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有一个样式，是全局上下文注入的</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"svgClass"</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"$attrs"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123; color: color &#125;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">:xlink:href</span>=<span class="hljs-string">"iconName"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; computed, defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">name</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>,
    &#125;,
    <span class="hljs-attr">color</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>,
    &#125;,
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-keyword">const</span> iconName = computed(<span class="hljs-function">() =></span> <span class="hljs-string">`#icon-<span class="hljs-subst">$&#123;props.name&#125;</span>`</span>);
    <span class="hljs-keyword">const</span> svgClass = computed(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (props.name) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`svg-icon icon-<span class="hljs-subst">$&#123;props.name&#125;</span>`</span>;
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'svg-icon'</span>;
    &#125;);
    <span class="hljs-keyword">return</span> &#123;
      iconName,
      svgClass,
    &#125;;
  &#125;,
&#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span>></span><span class="css">
<span class="hljs-selector-class">.svg-icon</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">1em</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">1em</span>;
  <span class="hljs-attribute">vertical-align</span>: middle;
  fill: currentColor;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">三、<code>vite-plugin-style-import</code></h2>
<h3 data-id="heading-15">1.说明</h3>
<p><code>npm</code>: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvite-plugin-style-import" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/vite-plugin-style-import" ref="nofollow noopener noreferrer">vite-plugin-style-import</a></p>
<p><code>git</code>: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fanncwb%2Fvite-plugin-style-import" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/anncwb/vite-plugin-style-import" ref="nofollow noopener noreferrer">vite-plugin-style-import</a></p>
<p>该插件可按需导入组件库样式，由于 <code>vite</code> 本身已按需导入了组件库，然后目前 <code>element-plus</code> 按需加载使用的插件方式不太优雅，其实就仅仅样式不是按需导入的，因此只需按需导入样式即可。</p>
<h3 data-id="heading-16">2.安装</h3>
<pre><code class="hljs language-bash copyable" lang="bash">yarn add vite-plugin-style-import --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">3.配置插件</h3>
<p><code>build/vite/plugin/styleImport.ts</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> styleImport <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-style-import'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configStyleImportPlugin</span>(<span class="hljs-params">isBuild: boolean</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!isBuild) <span class="hljs-keyword">return</span> [];
  <span class="hljs-keyword">const</span> styleImportPlugin = styleImport(&#123;
    <span class="hljs-attr">libs</span>: [
      <span class="hljs-comment">// 按需加载 element-plus</span>
      &#123;
        <span class="hljs-attr">libraryName</span>: <span class="hljs-string">'element-plus'</span>,
        <span class="hljs-attr">esModule</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">ensureStyleFile</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">resolveStyle</span>: <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
          <span class="hljs-keyword">const</span> cssName: string = name.slice(<span class="hljs-number">3</span>);
          <span class="hljs-keyword">return</span> <span class="hljs-string">`element-plus/packages/theme-chalk/src/<span class="hljs-subst">$&#123;cssName&#125;</span>.scss`</span>;
        &#125;,
        <span class="hljs-attr">resolveComponent</span>: <span class="hljs-function"><span class="hljs-params">name</span> =></span> <span class="hljs-string">`element-plus/lib/<span class="hljs-subst">$&#123;name&#125;</span>`</span>,
      &#125;,
    ],
  &#125;);
  <span class="hljs-keyword">return</span> styleImportPlugin;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">4.配置Vite</h3>
<p><code>build/vite/plugin/index.ts</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
<span class="hljs-keyword">import</span> &#123; configStyleImportPlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./styleImport'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createVitePlugins</span>(<span class="hljs-params">viteEnv: ViteEnv, isBuild: boolean, pkg: any</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// vite-plugin-style-import</span>
  vitePlugins.push(configStyleImportPlugin(isBuild));

  <span class="hljs-keyword">return</span> vitePlugins;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">四、<code>vite-plugin-compression</code></h2>
<h3 data-id="heading-20">1.说明</h3>
<p><code>vite-plugin-compress</code>的增强版，压缩用的。</p>
<p><code>npm</code>: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvite-plugin-compression" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/vite-plugin-compression" ref="nofollow noopener noreferrer">vite-plugin-compression</a></p>
<p><code>git</code>: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fanncwb%2Fvite-plugin-compression" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/anncwb/vite-plugin-compression" ref="nofollow noopener noreferrer">vite-plugin-compression</a></p>
<h3 data-id="heading-21">2.安装</h3>
<pre><code class="hljs language-bash copyable" lang="bash">yarn add vite-plugin-compression --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">3.配置插件</h3>
<p><code>build/vite/plugin/compress.ts</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> type &#123; Plugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>;
<span class="hljs-keyword">import</span> compressPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-compression'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configCompressPlugin</span>(<span class="hljs-params">
  compress: <span class="hljs-string">'gzip'</span> | <span class="hljs-string">'brotli'</span> | <span class="hljs-string">'none'</span> = <span class="hljs-string">'none'</span>,
  deleteOriginFile = <span class="hljs-literal">false</span>,
</span>): <span class="hljs-title">Plugin</span> | <span class="hljs-title">Plugin</span>[] </span>&#123;
  <span class="hljs-keyword">const</span> compressList = compress.split(<span class="hljs-string">','</span>);

  <span class="hljs-keyword">const</span> plugins: Plugin[] = [];

  <span class="hljs-keyword">if</span> (compressList.includes(<span class="hljs-string">'gzip'</span>)) &#123;
    plugins.push(compressPlugin(&#123;
      <span class="hljs-attr">ext</span>: <span class="hljs-string">'.gz'</span>,
      deleteOriginFile,
    &#125;));
  &#125;
  <span class="hljs-keyword">if</span> (compressList.includes(<span class="hljs-string">'brotli'</span>)) &#123;
    plugins.push(compressPlugin(&#123;
      <span class="hljs-attr">ext</span>: <span class="hljs-string">'.br'</span>,
      <span class="hljs-attr">algorithm</span>: <span class="hljs-string">'brotliCompress'</span>,
      deleteOriginFile,
    &#125;));
  &#125;
  <span class="hljs-keyword">return</span> plugins;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">4.配置Vite</h3>
<p><code>build/vite/plugin/index.ts</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
<span class="hljs-keyword">import</span> &#123; configCompressPlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./compress'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createVitePlugins</span>(<span class="hljs-params">viteEnv: ViteEnv, isBuild: boolean, pkg: any</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">const</span> &#123;
    <span class="hljs-attr">VITE_BUILD_COMPRESS</span>: compressType,
    <span class="hljs-attr">VITE_BUILD_COMPRESS_DELETE_ORIGIN_FILE</span>: shouldBuildCompressDeleteFile,
  &#125; = viteEnv;
  <span class="hljs-comment">// 生产环境使用插件</span>
  <span class="hljs-keyword">if</span> (isBuild) &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-comment">// rollup-plugin-gzip</span>
    vitePlugins.push(configCompressPlugin(compressType, shouldBuildCompressDeleteFile));
  &#125;

  <span class="hljs-keyword">return</span> vitePlugins;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            