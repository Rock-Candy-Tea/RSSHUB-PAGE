
---
title: '30 分钟完成 iOS monorepo 化改造 _ iOS 组件化复盘'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=3997'
author: 掘金
comments: false
date: Fri, 02 Sep 2022 07:50:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=3997'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" target="_blank" title="https://s.juejin.cn/ds/jooSN7t">点击查看活动详情</a></p>
<h2 data-id="heading-0">背景</h2>
<p>代码<strong>解耦和复用</strong>是一个非常重要的问题。早期我们会以合理划分目录，提取公共组件的方式解决问题。</p>
<p>随着项目增大，项目编译速度变慢（调试成本变大），同时有了代码共享的需求，组件化开发是一个不错的选择，既能单个模块独立开发调试，又能多项目共享代码，看上去十分不错，研发效率提升也很明显（特别是调 UI 样式的时候）。</p>
<p>模块越来越多，涉及多模块同时改动的可能性急剧增加，终于在一次大规模重构中你吃到了组件化开发的第一个苦。怎么在壳工程同时修改多个模块并提交到对应仓库？怎么发 MR 让队友 Review 你的代码？各模块版本怎么管理？等一系列问题让人头大。本文带你深刻复盘 iOS 组件化之路。</p>
<p><strong>阅读本文你将了解：</strong></p>
<ul>
<li>什么是 monorepo</li>
<li>为什么要 monorepo</li>
<li>iOS 怎么实现 monorepo</li>
<li>monorepo 最佳实践</li>
</ul>
<h2 data-id="heading-1">单体应用阶段</h2>
<p>项目起步阶段，团队规模非常小，此时适合「单体应用」。不过切记，一定要合理划分目录，提取公共组件，尽可能做到不同功能/业务间解耦。为将来低成本迁移到组件化方案留足空间。</p>
<p>此时你的目录结构大概是这样的：</p>
<pre><code class="hljs language-erlang copyable" lang="erlang">└── monorepo-demo
  ├── monorepo-demo
  │   ├── AppDelegate.swift
  │   ├── Assets.xcassets
  │   ...
  │   ├── SceneDelegate.swift
  │   └── ViewController.swift
  └── monorepo-demo.xcodeproj
      ├── project.pbxproj
      ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>优点</strong>：</p>
<ul>
<li>代码管理成本低</li>
<li>不需要额外的学习成本</li>
<li>对 <code>Merge Request</code> 更友好</li>
</ul>
<p><strong>缺点</strong>：</p>
<ul>
<li>代码质量容易失控</li>
<li>项目规模太大时，开发调试效率开始显著降低（构建时间比较长，调一个 UI 问题要等全量构建完才能看到效果）</li>
<li>跨项目复用代码受到局限（不是不能跨项目复用代码）</li>
<li>git 无法根据目录划分访问权限，仓库内全部代码开放给每个团队成员</li>
</ul>
<h2 data-id="heading-2">组件化 + multirepo（多仓多模块）阶段</h2>
<p>团队规模变大，人员分工开始明确，此时单体应用的缺点愈发突出，此时 multirepo 更适合我们。multirepo 可以等效理解为把部分组件或模块当做三方库开发和使用，这样可以使人员分工更明确，队员只需关心自己模块所在的仓库，并在自己的模块内进行开发和调试，甚至可以独立提测单个模块。</p>
<p><strong>此时你的目录结构大概是这样的：</strong></p>
<pre><code class="hljs language-csharp copyable" lang="csharp">├── Podfile <span class="hljs-comment">// 新增，用以配置依赖</span>
├── Podfile.<span class="hljs-keyword">lock</span> <span class="hljs-comment">// 新增，用来锁定依赖版本，使团队内依赖的三方库版本一致，强烈建议纳入 git 版本管理</span>
├── Pods <span class="hljs-comment">// 新增</span>
│   ├── ModuleA <span class="hljs-comment">// 我们依赖的二方库</span>
│   │   ├── LICENSE
│   │   ├── README.md
│   │   └── Source
│   │       ├── ModulA.swift
│   │   ...
│   ├── Headers
│   ├── Local Podspecs
│   ├── Manifest.<span class="hljs-keyword">lock</span>
│   ├── Pods.xcodeproj
│   │   ├── project.pbxproj
│   │   ...
<span class="hljs-comment">// 原有部分</span>
├── monorepo-demo
│   ├── AppDelegate.swift
│   ...
│   ├── Info.plist
│   ├── SceneDelegate.swift
│   └── ViewController.swift
├── monorepo-demo.xcodeproj
│   ...
└── monorepo-demo.xcworkspace <span class="hljs-comment">// 新增，后面我们要在 Xcode 中打开该文件进行开发而不再是 monorepo-demo.xcodeproj</span>
  └── ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>组件化开发的意义</strong>：</p>
<ul>
<li>便于代码复用</li>
<li>模块独立开发、调试</li>
<li>人员分工更明确</li>
<li>源代码访问权限设置更灵活</li>
<li>强迫程序员降低代码耦合</li>
</ul>
<p><strong>需要注意的点</strong>：</p>
<ul>
<li>模块力度划分不太容易把握
<ul>
<li>划分模块原则：基础组件、功能组件和业务模块</li>
<li>不要划得太细，组件数量激增会增大维护成本</li>
</ul>
</li>
<li>各模块分支管理（比较影响开发体验）
<ul>
<li>问题：业务迭代往往需要同时修改多个模块，此时被修改的模块需要各自准备一个分支，并且需要一一对应</li>
<li>方案：被修改的模块版本与壳工程版本保持一致，拉出同名分支</li>
<li>仍然存在的问题：1. 为了模块版本统一，未改动的模块也要拉出同名分支，是多余的操作</li>
<li>分支管理需要借助脚本完成</li>
</ul>
</li>
<li>同时涉及多个模块的重构时需要在壳工程同时修改多个模块，并提交到各自仓库。
<ul>
<li>方案：使用 git submodule 实现本地依赖，以 git flow 方式管理分支，提供配套脚本完成分支管理任务。</li>
<li>仍然存在的问题：1. 脚本执行效率比较低，且会偶现失败</li>
</ul>
</li>
<li>同时涉及多个模块修改的 MR（Merge Request）需要在各自模块仓库发出，显得比较分散。</li>
</ul>
<h2 data-id="heading-3">组件化 + monorepo（单仓多模块）阶段</h2>
<p>monorepo（单仓多模块/项目），即把多个模块/项目源码放在同一个代码仓库管理，乍一听这并不是一个好的想法，甚至有点扯，但这确实能解决不少问题，提升了开发体验，真的让效率提升了不少。</p>
<p>随着组件/模块越来越多， multirepo 维护成本越来越大，意外情况也变得更频繁了（打包机打包失败更频繁了），于是我们意识到我们的方案是时候改进了。</p>
<p>此时你的目录结构大概是这样的：</p>
<pre><code class="hljs language-erlang copyable" lang="erlang">.
├── modules // 新增目录
│   ├── ModuleA // A 模块源码，该模块具备独立开发调试能力
│   │   ├── Example
│   │   │   ├── ModuleA
│   │   │   │   ├── AppDelegate.swift
│   │   │   │   ...
│   │   │   │   └── ViewController.swift
│...
│   ├── ModuleB // B 模块源码，该模块具备独立开发调试能力
│   │   ├── Example
│   │   │   ├── ModuleB
│   │   │   │   ├── AppDelegate.swift
│   │   │   │   ...
│   │   │   │   └── ViewController.swift
│...
│...
└── monorepo-demo
  ├── Podfile
  ├── Podfile.lock
  ├── Pods
  │   ├── Alamofire
│...
  │   └── Target Support Files
  │       ├── Alamofire
  │       │   ├── ...
  │       ├── ModuleA
  │       │   ├── ...
  │       ├── ModuleB
  │       │   ├── ...
│...
  ├── monorepo-demo
  │   ├── AppDelegate.swift
  │   ├── ...
  │   ├── SceneDelegate.swift
  │   └── ViewController.swift
  ├── monorepo-demo.xcodeproj
  │   ...
  └── monorepo-demo.xcworkspace
      └── ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>实操步骤</strong>：</p>
<ol>
<li>主仓库新建 modules 目录，用以存放组件/模块源码，目录 monorepo-demo 存放壳工程源码</li>
<li>壳工程 Podfile 文件以本地依赖方式依赖各个模块</li>
<li>齐活了，就是那么简单</li>
</ol>
<p><strong>Podfile 示例</strong>：</p>
<pre><code class="hljs language-ruby copyable" lang="ruby"><span class="hljs-comment"># Uncomment the next line to define a global platform for your project</span>
<span class="hljs-comment"># platform :ios, '9.0'</span>
​
target <span class="hljs-string">'monorepo-demo'</span> <span class="hljs-keyword">do</span>
 <span class="hljs-comment"># Comment the next line if you don't want to use dynamic frameworks</span>
 use_frameworks!
 pod <span class="hljs-string">'Alamofire'</span>
​
 <span class="hljs-comment"># 以本地依赖方式依赖各二方库</span>
 pod <span class="hljs-string">'ModuleA'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../modules/moduleA'</span>
 pod <span class="hljs-string">'ModuleB'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../modules/moduleB'</span>
 pod <span class="hljs-string">'ModuleC'</span>, <span class="hljs-symbol">:path</span> => <span class="hljs-string">'../modules/moduleC'</span>
 <span class="hljs-comment"># Pods for monorepo-demo</span>
​
<span class="hljs-keyword">end</span>
​
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>monorepo 的优势</strong>：</p>
<ul>
<li>所有源码在同一个仓库，分支管理与单体应用一样简单</li>
<li>MR 在同一个仓库发出，队友阅读起来很顺畅</li>
<li>保留 multirepo 的主要优势
<ul>
<li>便于代码复用（单个组件/模块依然可以单独发布版本，跨应用共享代码与 mutirepo 无异）</li>
<li>模块独立开发、调试</li>
<li>人员分工更明确</li>
<li>强迫程序员降低代码耦合</li>
</ul>
</li>
</ul>
<p><strong>monorepo 的不足</strong>：</p>
<ul>
<li>git 无法根据目录划分访问权限，仓库内全部代码开放给每个团队成员</li>
<li>代码规模大到一定程度时 git 操作速度到达瓶颈，影响 git 操作体验（这个中小规模团队不用考虑）。</li>
</ul>
<blockquote>
<p><strong>提示</strong>：如果你要从 multirepo 方式迁移到 monorepo ，则只需把各模块仓库 clone 到 modules 目录下，并切换到最新代码所在分支，然后删掉各模块目录下的 <code>.git</code> 文件，并按照「实操步骤」完成迁移即可。</p>
</blockquote>
<h2 data-id="heading-4">组件化 + monorepo（单仓多模块） + multirepo（多仓多模块）</h2>
<p>我们各自的司情不同，再加上每种方案都有自己的局限和不足，为了能够满足我们现实的需求，我们继续探索。既然我们清楚的预见了 monorepo 的缺陷，那么解决它其实也并不难。</p>
<p>首先我们要知道 monorepo 与 multirepo 不是二选一的关系，而是主次的关系，既然是主次的关系，那么就是可以共存的。相信嘴角上扬的你已经悟了。</p>
<p><strong>monorepo 优化方案</strong>：</p>
<ul>
<li>稳定且独立的模块使用 multirepo 方式管理，像三方库一样</li>
<li>非常驻业务（临时性的需求）可以使用 multirepo 方式管理，接下来某个版本就可以干掉，也不会污染 monorepo 仓库（比如一个拉新的活动，只用几天，那么过了这几天，代码自然就没有存在的意义了）</li>
<li>需要较高权限的模块可以使用 multirepo 方式管理，提供二进制库依赖即可</li>
</ul>
<p>至此，我们似乎已经解决了所有已知痛点，也许接下来还会冒出新的痛点，不过请相信「办法总比困难多」。</p>
<h2 data-id="heading-5">小结</h2>
<p><strong>一点感悟分享给大家</strong>：</p>
<ol>
<li>没有最好的方案，只有当下最适合自己的方案</li>
<li>选方案不为追逐「潮流」，而是追逐「收益」</li>
<li>各方案的思想并非互相对立，相互结合往往有奇效</li>
<li>方案选型要为后期调整留足空间</li>
<li>要坚信「办法总比困难多」</li>
</ol></div>  
</div>
            