
---
title: 'qiankun使用webpack5 module federation实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d9058befff44eca89601cd2c4da420e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 22:02:40 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d9058befff44eca89601cd2c4da420e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">qiankun</h1>
<p>qiankun 是一个基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FCanopyTax%2Fsingle-spa" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/CanopyTax/single-spa" ref="nofollow noopener noreferrer">single-spa</a> 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmicro-frontends.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://micro-frontends.org/" ref="nofollow noopener noreferrer">微前端</a>实现库，微应用能够独立开发独立部署。</p>
<h2 data-id="heading-1">什么是微前端</h2>
<blockquote>
<p>Techniques, strategies and recipes for building a <strong>modern web app</strong> with <strong>multiple teams</strong> that can <strong>ship features independently</strong>. -- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmicro-frontends.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://micro-frontends.org/" ref="nofollow noopener noreferrer">Micro Frontends</a></p>
<p>微前端是一种多个团队通过独立发布功能的方式来共同构建现代化 web 应用的技术手段及方法策略。</p>
</blockquote>
<p>微前端架构具备以下几个核心价值：</p>
<ul>
<li>
<p>技术栈无关<br>
主框架不限制接入应用的技术栈，微应用具备完全自主权</p>
</li>
<li>
<p>独立开发、独立部署<br>
微应用仓库独立，前后端可独立开发，部署完成后主框架自动完成同步更新</p>
</li>
<li>
<p>增量升级</p>
<p>在面对各种复杂场景时，我们通常很难对一个已经存在的系统做全量的技术栈升级或重构，而微前端是一种非常好的实施渐进式重构的手段和策略</p>
</li>
<li>
<p>独立运行时<br>
每个微应用之间状态隔离，运行时状态不共享</p>
</li>
</ul>
<h2 data-id="heading-2">Module Federation（模块联邦）</h2>
<p>模块联邦也是一种微前端，可以颗粒化到单页应用或者组件。
每个字应用单独构建，主应用在运行时通过容器加载远程模块即子应用的构建。主应用自动使用子应用当前版本的最新资源。</p>
<h2 data-id="heading-3">实例，项目均接入qiankun</h2>
<h3 data-id="heading-4">项目mf1， 提供共享模块（qiankun子项目）</h3>
<h4 data-id="heading-5">mf1 共享模块为src/components/Button</h4>
<pre><code class="hljs language-1 copyable" lang="1">import React from 'react';
const Button =() => &#123;
  return (<div><button>我是mf1的button</button></div>);
&#125;
export default Button;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">mf1 的config 配置</h4>
<pre><code class="hljs language-1 copyable" lang="1">const &#123; ModuleFederationPlugin &#125; = require("webpack").container;
const &#123; REACT_APP_ENV, NODE_ENV &#125; = process.env;
const publicPath = NODE_ENV === 'production' ? '/publicPath' : '/'；

/**
 * dev 环境
 * publicPath： '/qiankun/zeusCI/', 则必须注释掉 memo.output.publicPath('auto')项目才能正确运行。 MF exposes不可用
 * publicPath： '/', 则无须注释掉 memo.output.publicPath('auto')。 MF exposes可用
 * 建议： dev 环境publicPath改为 '/'
 */
 
export default defineConfig(&#123;
  base: '/xxx',
  publicPath, 
  qiankun: &#123;
    slave: &#123;
    &#125;
  &#125;,
  antd: &#123;&#125;,
  dva: &#123;
    hmr: true,
  &#125;,
  history: &#123;
    type: 'hash',
  &#125;,
  dynamicImport: &#123;
    loading: '@/components/PageLoading/index',
  &#125;,
  mfsu:&#123;&#125;, // umi3.5.13版本引入，加速构建
  webpack5: &#123;&#125;,
  chainWebpack(memo) &#123;
    memo.output.publicPath('auto'); // 请看上面注释
    memo
      .plugin('mf')
      .use(ModuleFederationPlugin, [&#123;
        name: "mf1", // 该名称必须与入口名称相匹配

        filename: 'remoteEntry.js',
        exposes: &#123;
          "./Button": './src/components/Button/index', // 共享模块
        &#125;,
       
      &#125;]);
     
  &#125;,
  
  targets: &#123;
    ie: 11,
  &#125;,
  // umi routes: https://umijs.org/docs/routing
  routes,
  // Theme for antd: https://ant.design/docs/react/customize-theme-cn
  theme: &#123;
    'primary-color': defaultSettings.primaryColor,
  &#125;,
  title: false,
  ignoreMomentLocale: true,
  proxy: proxy[REACT_APP_ENV || 'dev'],
  manifest: &#123;
    basePath: '/xxx',
  &#125;,
  exportStatic: &#123;&#125;,
  esbuild: &#123;&#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">项目2，引入mf1共享模块并使用（qiankun子项目）</h3>
<h4 data-id="heading-8">项目2 page/index</h4>
<pre><code class="hljs language-1 copyable" lang="1">import styles from './index.less';
import React from 'react'
import &#123;Card&#125; from 'antd'
const Mf1Button = React.lazy(() => import("mf1/Button"));
export default function IndexPage() &#123;
  return (
    <div>
      <Card title="module federatino 应用">
       <React.Suspense fallback='loading'>
        <Mf1Button />
      </React.Suspense>
      </Card>
    </div>
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">项目2 config配置</h4>
<pre><code class="hljs language-1 copyable" lang="1">qiankun: &#123;
    slave: &#123;&#125;
  &#125;,
  antd: &#123;&#125;,
  dva: &#123;
    hmr: true,
  &#125;,
  plugins: [
  ],
  locale: &#123;
    // default zh-CN
    default: 'zh-CN',

    // default true, when it is true, will use `navigator.language` overwrite default
    baseNavigator: true,
  &#125;,
  dynamicImport: &#123;
    loading: '@/components/PageLoading/index',
  &#125;,
  
  webpack5: &#123;&#125;,
  chainWebpack(memo) &#123;
    memo.output.publicPath('auto');
    memo
      .plugin('mf')
      .use(ModuleFederationPlugin, [&#123;
        name: "submodule",
       
        filename: 'submodule.js',
        exposes:&#123;
          "./ProductList": './src/components/ProductList/index'
        &#125;,
        remotes: &#123; // 引用远程模块
        // dev环境 "mf1@//localhost:7001/remoteEntry.js"
          mf1: "mf1@//xxxx.com/publicPath/remoteEntry.js" 
        &#125;,
        
      &#125;])
  &#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">项目2启动</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d9058befff44eca89601cd2c4da420e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">注意⚠️</h2>
<blockquote>
<p>共享模块不允许使用hooks</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fda8de3783f47b9a60b61e6db55c30e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>remotes 不需要加https或者http</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7866dfd790f34f8bbf6035b4b3ee30ae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>exposes 必须为 <code>"./Button": "...."</code></p>
</blockquote>
<pre><code class="hljs language-1 copyable" lang="1">-   'Button': './src/components/Button'
+   './Button':'./src/components/Button'
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a29f8da5f79e4efeac4d33ddec920508~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">总结</h2>
<p>模块联邦提供单独构建单独部署，主应用只在运行时加载。主体应用程序将常用库定义为共享模块，以避免在页面构建中出现重复。相对npm包有很大的便捷性。 但是和qiankun混搭时，实操效果不佳。目前来看项目中采用MF，建议使用CRA初始化项目，或者emp架构。</p>
<p>以上个人拙见，欢迎指教。</p></div>  
</div>
            