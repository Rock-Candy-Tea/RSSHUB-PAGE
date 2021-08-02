
---
title: '_vite_大型react项目从webpack迁移到vite到底能快多少'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a778678079934ebfa20eda99e6bc79b1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 01:46:05 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a778678079934ebfa20eda99e6bc79b1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>自从尤大vite2.x写完后，好评如潮，我想尝试下vite，看看在本地到底能比webpack快多少，所以拿手头一个比较大的react项目改造下来测试。本文不包含vite原理，vite相关介绍请看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/" ref="nofollow noopener noreferrer">vite官方文档</a>，只记录在改造过程中遇到的问题和解决方案。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a778678079934ebfa20eda99e6bc79b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">开搞</h1>
<h2 data-id="heading-2">准备工作</h2>
<p>首先，在项目中安装vite并且生成一个最简单的<code>vite.config.js</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//vite.config.js</span>
<span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> reactRefresh <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-react-refresh'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [reactRefresh()]
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>vite.config.js</code>与<code>index.html</code>都必须在根路径下，<code>index.html</code>内引用入口文件。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b8fac354c5341cf841cb31275415b12~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在<code>package.json</code>增加vite启动命令。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1322d40008445ecb6eafe46b186324e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>ok,准备工作已经完成，现在开始我们的改造（趟坑）之路。</p>
<h2 data-id="heading-3">给vite增加基本配置</h2>
<p>首先，让我怀着必死的决心启动vite，果然，数不清的报错（根本不敢看好么。。。）</p>
<h3 data-id="heading-4">error:fsevents.watch is not a function .</h3>
<p>解决：删掉package.lock.json 和yarn.lock，重新install。</p>
<h3 data-id="heading-5">error: [vite:dep-scan] Failed to resolve entry</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a46974e53a9341dc9afd55d642c2d888~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是一个私有的npm包，错误原因是无法加载这个本地库，需要修改这个本地库的<code>package.json</code>的<code>module</code>属性.</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e5b515659004061acb8a76ae561df42~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>module属性修改为正确路径，错误解决。</p>
<h3 data-id="heading-6">增加css样式预处理器</h3>
<p>sass和一些自定义配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//vite.config.js</span>
<span class="hljs-keyword">import</span> autoprefixer <span class="hljs-keyword">from</span> <span class="hljs-string">'autoprefixer'</span>
<span class="hljs-keyword">import</span> postcssFlexbugsFixes <span class="hljs-keyword">from</span> <span class="hljs-string">'postcss-flexbugs-fixes'</span>
<span class="hljs-keyword">import</span> postcssPresetEnv <span class="hljs-keyword">from</span> <span class="hljs-string">'postcss-preset-env'</span>

<span class="hljs-keyword">const</span> loder_presetEnv=postcssPresetEnv(&#123;
  <span class="hljs-attr">autoprefixer</span>: &#123;
    <span class="hljs-attr">flexbox</span>: <span class="hljs-string">'no-2009'</span>,
  &#125;,
  <span class="hljs-attr">stage</span>: <span class="hljs-number">3</span>,
&#125;)


<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
   <span class="hljs-comment">//......</span>
    <span class="hljs-attr">css</span>: &#123;
      <span class="hljs-attr">modules</span> :&#123;
        <span class="hljs-attr">scopeBehaviour</span>:<span class="hljs-string">'local'</span>
      &#125;,
      <span class="hljs-attr">postcss</span>:&#123;
        <span class="hljs-attr">plugins</span>:[
          autoprefixer,
          postcssFlexbugsFixes,
          loder_presetEnv
        ]
      &#125;,
        <span class="hljs-attr">preprocessorOptions</span>: &#123;
          <span class="hljs-attr">less</span>: &#123;
            <span class="hljs-attr">javascriptEnabled</span>: <span class="hljs-literal">true</span>,
          &#125;,
          <span class="hljs-attr">scss</span>: &#123;
            <span class="hljs-comment">// 引入scss全局变量 给导入的路径最后加上; </span>
            <span class="hljs-attr">additionalData</span>: <span class="hljs-string">`@import "./src/common/styles/base.scss";`</span>,
          &#125;,  
        &#125;
    &#125;,
    <span class="hljs-comment">//....</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> styles <span class="hljs-keyword">from</span> <span class="hljs-string">'./index.module.scss'</span>

<div className=&#123;styles.root&#125;>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果项目中样式是modules写法的话，必须在vite.config中加入css.modules<code>，</code>并把所有.scss改为.module.scss。</p>
<p>将全局样式文件修改后缀，写一个改名的小脚本即可。</p>
<pre><code class="copyable">/*
 * @Description: 批量重命名
 */
const glob = require('glob')
const fs = require('fs');
const files = glob.sync('src/**/*.scss')

files.forEach(oldPath => &#123;
  const newPath = oldPath.replace('.scss','.module.scss')
  fs.rename(oldPath, newPath, (err) => &#123;
    if (err) &#123;
      console.log('err',oldPath)
    &#125;
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次启动项目，发现更改的一些全局主题色消失了，加入全局主题配置。</p>
<pre><code class="copyable">//vite.config.js
       less: &#123;
              //请移除 lessOptions 这一级直接配置选项。
              modifyVars: &#123;
                'primary-color': '#19B5A5',
                'link-color': '#19B5A5',
                'border-color': '#E0E0E0', //全局分隔线
                'border-radius-base': '2px',
                'success-color': '#19B5A5', // 成功色
                'warning-color': '#faad14', // 警告色
                'error-color': '#f5222d', // 错误色
              &#125;,
          
            javascriptEnabled: true,
          &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体配置规则查看less配置项。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/964feda5113843ec9959ef328a42e177~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>样式打包后太大，改成antd按需加载试试。</p>
<p>将全局引入的antd样式注掉。</p>
<pre><code class="copyable">// import 'antd/dist/antd.less'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>增加antd按需加载插件</p>
<pre><code class="hljs language-js copyable" lang="js">npm i vite-plugin-imp -D
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//vite.config.js
import vitePluginImp from 'vite-plugin-imp'
export default defineConfig(&#123;
 //.....
    plugins: [
        reactRefresh(),
        vitePluginImp(&#123;
          libList: [
            &#123;
              libName: "antd",
              style: (name) => `antd/es/$&#123;name&#125;/style/`,
            &#125;,
          ],
        &#125;)
      ]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49b90f2efe724c9b941eeddb21448a9b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按需加载后打包效果还是很nice的。</p>
<p>样式的修改告一段落，再看其他的问题。</p>
<h3 data-id="heading-7">webpack原来注入的一些环境变量全部消失</h3>
<p>vite有自己的环境变量配置。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2Fguide%2Fenv-and-mode.html%23env-files" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/guide/env-and-mode.html#env-files" ref="nofollow noopener noreferrer">地址</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6b2aa44ceb04af09ea83d295dcca8bc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>自定义vite 配置文件的位置，在vite.config设置 envDir:'./config'。前端文件中获取系统配置直接import.meta.env.VITE_xxx即可，很方便有木有。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b113d2f074c348839ac1e2f2771bf4c6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>在vite.config.js中是不能直接通过import.meta.env.VITE_xxx来获取env内的配置的</code>，那我们怎么区分本地还是生产环境来加载不同的vite插件呢？</p>
<p>不要着急，vite的Issuse内有机智的老哥已经给出了解决办法。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb8c5e35a7c04d2c9ef7d5e970bf49b0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">压缩图片</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5cac9f739294aa8a84acbb71c110be1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>项目打包时需要优化的点vite都会给你提示，不过怎么项目里会有这么大的图片_(:зゝ∠)，压缩图片的插件加一个。</p>
<pre><code class="hljs language-js copyable" lang="js">npm i vite-plugin-imagemin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//vite.config.js</span>
<span class="hljs-keyword">import</span> viteImagemin <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-imagemin'</span>;
 <span class="hljs-comment">//....</span>
   plugins: [
        <span class="hljs-comment">//....</span>
        viteImagemin(&#123;
          <span class="hljs-attr">gifsicle</span>: &#123;
            <span class="hljs-attr">optimizationLevel</span>: <span class="hljs-number">7</span>,
            <span class="hljs-attr">interlaced</span>: <span class="hljs-literal">false</span>,
          &#125;,
          <span class="hljs-attr">optipng</span>: &#123;
            <span class="hljs-attr">optimizationLevel</span>: <span class="hljs-number">7</span>,
          &#125;,
          <span class="hljs-attr">mozjpeg</span>: &#123;
            <span class="hljs-attr">quality</span>: <span class="hljs-number">20</span>,
          &#125;,
          <span class="hljs-attr">pngquant</span>: &#123;
            <span class="hljs-attr">quality</span>: [<span class="hljs-number">0.8</span>, <span class="hljs-number">0.9</span>],
            <span class="hljs-attr">speed</span>: <span class="hljs-number">4</span>,
          &#125;,
          <span class="hljs-attr">svgo</span>: &#123;
            <span class="hljs-attr">plugins</span>: [
              &#123;
                <span class="hljs-attr">name</span>: <span class="hljs-string">'removeViewBox'</span>,
              &#125;,
              &#123;
                <span class="hljs-attr">name</span>: <span class="hljs-string">'removeEmptyAttrs'</span>,
                <span class="hljs-attr">active</span>: <span class="hljs-literal">false</span>,
              &#125;,
            ],
          &#125;,
        &#125;),
      ],
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d61a9d06740420d8b972e1c8c269d54~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>效果很明显。</p>
<blockquote>
<p>提供一下vite插件社区地址 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fawesome-vite%23plugins" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/awesome-vite#plugins" ref="nofollow noopener noreferrer">github.com/vitejs/awes…</a> ，插件很全，可以按照自己优化的需要来选择。</p>
</blockquote>
<h1 data-id="heading-9">vite与webpack时间对比</h1>
<p>启动时间</p>
<p>webpack 启动时间</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80293082a162451396139efa52f63e44~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>vite 启动时间</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cef6fa07ae224e609cf3cebada32884c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>webpack HMR</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/916c13ce36734df7b9793df96038b577~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>vite模块热更新在100～200ms左右，在热更新方面，webpack是完完全全被吊打，模块越多差距越大。
Vite 以原生ESM方式服务源码，只需要在浏览器请求源码时先进行转换再返回转换后的源码。基于这种方式，vite hmr的实现要比webpack的hrm实现更简单更快速。</p>
<p>webpack打包时间</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68a255f784784278a3ef314f7f9a31ec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>vite打包时间</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecd3c1e860c041af88d42cf950716f3f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-10">总结</h1>
<p>在启动和热更新方面，vite有无与伦比的优势。</p>
<p>但毕竟vite目前的社区生态还不如webpack完善，项目迁移还是要按实际情况和潜在风险来考虑。</p>
<p>期待vite社区和影响力进一步扩大。</p>
<p>最后，</p>
<p>点个赞吧</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f607a602ea834951be5db8205b34b442~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            