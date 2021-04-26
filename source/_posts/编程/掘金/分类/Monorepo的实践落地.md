
---
title: 'Monorepo的实践落地'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3769'
author: 掘金
comments: false
date: Sun, 25 Apr 2021 19:14:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=3769'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文首发于 <a href="https://hjingren.cn/archives/" target="_blank" rel="nofollow noopener noreferrer">hzzly的博客</a></p>
<p>原文链接：<a href="https://hjingren.cn/2021/04/26/Monorepo%E7%9A%84%E5%AE%9E%E8%B7%B5%E8%90%BD%E5%9C%B0/" target="_blank" rel="nofollow noopener noreferrer">Monorepo的实践落地</a></p>
</blockquote>
<p><strong>前言</strong>：最近针对项目代码仓库进行了一次重构，之前代码管理缺少规范和模块化的思想，也是借着项目重构这次机会重新规划代码仓库，实践落地了一种新的项目管理方式——Monorepo，Monorepo的管理概念跟我们规划的项目代码管理非常贴合，再加上我们新增的组件库及工具库，打造了一套比较完整的工作流。</p>
<p>一些概念性的的东西这里就不多说了，不太了解 <code>Monorepo</code> 的可以自行 google 一下，这里就默认已经了解过了。</p>
<p>要想从零开始定制一套完善的 Monorepo 的工程化工具，还是一件比较有难度的事情。不过社区已经提供了一些比较成熟的方案，我们可以拿来进行定制。</p>
<p>在重构方案选择上，我们选择了业界比较成熟的 <strong><a href="https://lerna.js.org/" target="_blank" rel="nofollow noopener noreferrer">lerna</a></strong> 和 <strong>yarn workspaces</strong>，用 <code>yarn</code> 来处理依赖问题，用 <code>lerna</code> 来处理发布问题。</p>
<p><a href="https://github.com/hzzlyxx/lerna" target="_blank" rel="nofollow noopener noreferrer">仓库地址</a></p>
<h2 data-id="heading-0">lerna</h2>
<p>我们看一下 <code>lerna</code> 官方的定位：A tool for managing JavaScript projects with multiple packages（一个用来管理带有多个package的JavaScript项目）。</p>
<p>lerna不负责构建，测试等任务，它提出了一种集中管理package的目录模式，提供了一套自动化管理程序，让开发者不必再深耕到具体的组件里维护内容，在项目根目录就可以全局掌控，基于 npm scripts，使用者可以很好地完成组件构建，代码格式化等操作。</p>
<h3 data-id="heading-1">安装</h3>
<pre><code class="hljs language-bash copyable" lang="bash">npm install lerna –g
//
yarn add lerna global
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">基本命令</h3>
<pre><code class="hljs language-bash copyable" lang="bash">// lerna 项目初始化
lerna init // 固定模式
lerna init -i // 独立模式

// 创建子项目
lerna create [包名]

// 清除所有子项目的依赖
lerna clean

// 安装所有依赖
lerna bootstrap

// 发布
lerna publish
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">重构的价值</h2>
<p>之前的代码管理非常的混杂，还是比较传统的代码目录结构，一些公共基础服务无法扩展复用，如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">// 之前的代码目录
├── package.json
├── README.md
├── tool // 项目打包编译配置
├── release // 打包目标文件夹
└── src // 源代码
    ├── css
    ├── html
    ├── images
    ├── js
    └── sass
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重构后的代码结构无论是模块化还是复用性都很清晰，同时在代码规范上也比之前更规范了，如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">// 重构后的代码目录：
├── ... // 其它配置文件（代码规范）
├── package.json
├── README.md
├── lerna.json // lerna 配置文件
└── packages // 分割的小项目
    ├── components
    ├── utils
    ├── ... // 多个业务模块
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">总结</h2>
<ul>
<li>将之前混杂的代码库分割为独立版本控制的小项目（项目更清晰）</li>
<li>解决了包之间的依赖关系（新增了组件库以及工具库）</li>
<li>通过git仓库检查到改动并自动同步（公共基础库的发布）</li>
<li>根据提交的commit生成CHANGELOG版本日志文件（项目代码更规范）</li>
<li>TypeScript支持</li>
<li>统一技术栈</li>
<li>完善的工作流</li>
</ul>
<p>当然，<code>lerna</code> 还有更多的功能可以去发掘，还有很多可以结合 <code>lerna</code> 一起使用的工具。构建一套完善的仓库管理机制，可能它的收益不是一些量化的指标可以衡量出来的，也没有直接的价值输出，但它能在日常的工作中极大的提高工作效率，解放生产力，节省大量的人力成本。</p>
<p>下篇就来聊聊组件库的那些事。</p></div>  
</div>
            