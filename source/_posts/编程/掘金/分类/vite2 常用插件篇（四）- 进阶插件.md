
---
title: 'vite2 常用插件篇（四）- 进阶插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8834'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 23:41:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=8834'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p><a href="https://juejin.cn/post/6996176490148659231/" target="_blank" title="https://juejin.cn/post/6996176490148659231/">上一篇文章</a>主要讲了<code>vite</code>日常开发常用的几个进阶插件，这篇文章讲下另外几个常用的进阶插件</p>
<h2 data-id="heading-1">一、<code>vite-plugin-theme</code></h2>
<h3 data-id="heading-2">1.说明</h3>
<p>这个是用于动态更改界面主题色的 vite 插件</p>
<ul>
<li>npm：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvite-plugin-theme" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/vite-plugin-theme" ref="nofollow noopener noreferrer">vite-plugin-theme</a></li>
<li>git：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fanncwb%2Fvite-plugin-theme" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/anncwb/vite-plugin-theme" ref="nofollow noopener noreferrer">vite-plugin-theme</a></li>
</ul>
<h3 data-id="heading-3">2.安装</h3>
<pre><code class="hljs language-bash copyable" lang="bash">yarn add vite-plugin-theme --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3.配置插件</h3>
<p><code>build/vite/plugin/theme.ts</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 网站主题颜色切换的Vite插件
 * https://github.com/anncwb/vite-plugin-theme
 */</span>
<span class="hljs-keyword">import</span> &#123; viteThemePlugin, mixLighten, mixDarken, tinycolor &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-theme'</span>;
<span class="hljs-keyword">import</span> &#123; getThemeColors, generateColors &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../../config/themeConfig'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configThemePlugin</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> colors = generateColors(&#123;
    mixDarken,
    mixLighten,
    tinycolor,
  &#125;);

  <span class="hljs-keyword">const</span> plugin = viteThemePlugin(&#123;
    <span class="hljs-comment">// 生成的很多个颜色方法</span>
    <span class="hljs-attr">colorVariables</span>: [...getThemeColors(), ...colors],
  &#125;);
  <span class="hljs-keyword">return</span> plugin;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">4.配置Vite</h3>
<p><code>build/vite/plugin/index.ts</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
<span class="hljs-keyword">import</span> &#123; configThemePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./theme'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createVitePlugins</span>(<span class="hljs-params">viteEnv: ViteEnv, isBuild: boolean, pkg: any</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">//vite-plugin-theme</span>
  vitePlugins.push(configThemePlugin());

  <span class="hljs-keyword">return</span> vitePlugins;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">5.修改主题方法</h3>
<p>之后要修改主题，直接调用一下这个方法即可。</p>
<p><code>src/theme/index.ts</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; getThemeColors, ThemeMode, generateColors &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../../build/config/themeConfig'</span>;

<span class="hljs-keyword">import</span> &#123; replaceStyleVariables &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-theme/es/client'</span>;
<span class="hljs-keyword">import</span> &#123; mixLighten, mixDarken, tinycolor &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-theme/es/colorUtils'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">changeTheme</span>(<span class="hljs-params">color: string, theme?: ThemeMode</span>) </span>&#123;
  <span class="hljs-keyword">const</span> colors = generateColors(&#123;
    mixDarken,
    mixLighten,
    tinycolor,
    color,
  &#125;);

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> replaceStyleVariables(&#123;
    <span class="hljs-attr">colorVariables</span>: [...getThemeColors(color, theme), ...colors],
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">二、vite-plugin-imagemin</h2>
<h3 data-id="heading-8">1.说明</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvite-plugin-imagemin" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/vite-plugin-imagemin" ref="nofollow noopener noreferrer">vite-plugin-imagemin</a>：一个压缩图片资源的 vite 插件。</p>
<h3 data-id="heading-9">2.配置镜像</h3>
<p><code>package.json</code>：</p>
<blockquote>
<p>官方建议：用于安装imagemin的依赖关系，因为中国可能没有安装imagemin</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"resolutions"</span>: &#123;
  <span class="hljs-attr">"bin-wrapper"</span>: <span class="hljs-string">"npm:bin-wrapper-china"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">3.安装</h3>
<pre><code class="hljs language-bash copyable" lang="bash">yarn add vite-plugin-imagemin --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">4.配置插件</h3>
<p><code>build/vite/plugin/imagemin.ts</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 用于压缩生产环境输出的图片资源
 * https://github.com/anncwb/vite-plugin-imagemin
 */</span>

<span class="hljs-keyword">import</span> viteImagemin <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-imagemin'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configImageminPlugin</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> plugin = viteImagemin(&#123;
    <span class="hljs-attr">gifsicle</span>: &#123;
      <span class="hljs-attr">optimizationLevel</span>: <span class="hljs-number">7</span>,
      <span class="hljs-attr">interlaced</span>: <span class="hljs-literal">false</span>,
    &#125;,
    <span class="hljs-attr">optipng</span>: &#123;
      <span class="hljs-attr">optimizationLevel</span>: <span class="hljs-number">7</span>,
    &#125;,
    <span class="hljs-attr">mozjpeg</span>: &#123;
      <span class="hljs-attr">quality</span>: <span class="hljs-number">8</span>,
    &#125;,
    <span class="hljs-attr">pngquant</span>: &#123;
      <span class="hljs-attr">quality</span>: [<span class="hljs-number">0.8</span>, <span class="hljs-number">0.9</span>],
      <span class="hljs-attr">speed</span>: <span class="hljs-number">4</span>,
    &#125;,
    <span class="hljs-attr">svgo</span>: &#123;
      <span class="hljs-attr">plugins</span>: [
        &#123;
          <span class="hljs-attr">removeViewBox</span>: <span class="hljs-literal">false</span>,
        &#125;,
        &#123;
          <span class="hljs-attr">removeEmptyAttrs</span>: <span class="hljs-literal">false</span>,
        &#125;,
      ],
    &#125;,
  &#125;);
  <span class="hljs-keyword">return</span> plugin;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>详细的配置信息可以看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fanncwb%2Fvite-plugin-imagemin%23options" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/anncwb/vite-plugin-imagemin#options" ref="nofollow noopener noreferrer">options</a></p>
<h3 data-id="heading-12">5.配置Vite</h3>
<p><code>build/vite/plugin/index.ts</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
<span class="hljs-keyword">import</span> &#123; configImageminPlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./imagemin'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createVitePlugins</span>(<span class="hljs-params">viteEnv: ViteEnv, isBuild: boolean, pkg: any</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">const</span> &#123;
    <span class="hljs-attr">VITE_USE_IMAGEMIN</span>: shouldUseImagemin
  &#125; = viteEnv;
  <span class="hljs-comment">// 生产环境使用插件</span>
  <span class="hljs-keyword">if</span> (isBuild) &#123;
    <span class="hljs-comment">// vite-plugin-imagemin</span>
    shouldUseImagemin && vitePlugins.push(configImageminPlugin());
  &#125;

  <span class="hljs-keyword">return</span> vitePlugins;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">三、vite-plugin-pwa</h2>
<h3 data-id="heading-14">1.说明</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvite-plugin-pwa" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/vite-plugin-pwa" ref="nofollow noopener noreferrer">vite-plugin-pwa</a>：PWA一些技术集成。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F768be2733872" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/768be2733872" ref="nofollow noopener noreferrer">Service Worker-参考链接</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FProgressive_web_apps" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps" ref="nofollow noopener noreferrer">PWA-MDN说明</a></li>
</ul>
<p>如果你还不清楚<code>PWA</code>是什么也没关系。直接配置即可。不影响应用在网页端的运行。</p>
<h3 data-id="heading-15">2.安装</h3>
<pre><code class="hljs language-bash copyable" lang="bash">yarn add vite-plugin-pwa --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">3.配置插件</h3>
<p><code>build/vite/plugin/pwa.ts</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * vite pwa 0 配置插件
 * https://github.com/antfu/vite-plugin-pwa
 */</span>

<span class="hljs-keyword">import</span> &#123; VitePWA &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-pwa'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">configPwaConfig</span>(<span class="hljs-params">env: ViteEnv</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">VITE_USE_PWA</span>: shouldUsePwa, <span class="hljs-attr">VITE_GLOB_APP_TITLE</span>: appTitle, <span class="hljs-attr">VITE_GLOB_APP_SHORT_NAME</span>: shortName &#125; = env;

  <span class="hljs-keyword">if</span> (shouldUsePwa) &#123;
    <span class="hljs-comment">// vite-plugin-pwa</span>
    <span class="hljs-keyword">const</span> pwaPlugin = VitePWA(&#123;
      <span class="hljs-attr">manifest</span>: &#123;
        <span class="hljs-attr">name</span>: appTitle,
        <span class="hljs-attr">short_name</span>: shortName,
        <span class="hljs-attr">icons</span>: [
          &#123;
            <span class="hljs-attr">src</span>: <span class="hljs-string">'./resource/img/pwa-192x192.png'</span>,
            <span class="hljs-attr">sizes</span>: <span class="hljs-string">'192x192'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'image/png'</span>,
          &#125;,
          &#123;
            <span class="hljs-attr">src</span>: <span class="hljs-string">'./resource/img/pwa-512x512.png'</span>,
            <span class="hljs-attr">sizes</span>: <span class="hljs-string">'512x512'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'image/png'</span>,
          &#125;,
        ],
      &#125;,
    &#125;);
    <span class="hljs-keyword">return</span> pwaPlugin;
  &#125;
  <span class="hljs-keyword">return</span> [];
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">4.配置Vite</h3>
<p><code>build/vite/plugin/index.ts</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
<span class="hljs-keyword">import</span> &#123; configPwaConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./pwa'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createVitePlugins</span>(<span class="hljs-params">viteEnv: ViteEnv, isBuild: boolean, pkg: any</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 生产环境使用插件</span>
  <span class="hljs-keyword">if</span> (isBuild) &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-comment">// vite-plugin-pwa</span>
    vitePlugins.push(configPwaConfig(viteEnv));
  &#125;

  <span class="hljs-keyword">return</span> vitePlugins;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            