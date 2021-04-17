
---
title: '「今日份BUG」ElementUI 图标乱码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f84226a8b5634ab2905618f816456325~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 23:41:05 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f84226a8b5634ab2905618f816456325~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">发现并面对 BUG</h2>
<p>最近写PC端控台项目，模板用的是 <a href="https://github.com/PanJiaChen/vue-element-admin" target="_blank" rel="nofollow noopener noreferrer">vue-element-adamin</a>。遇到一个问题：项目部署到线上，偶尔会出现 ElementUI 图标显示乱码，刷新一下又好了，本地未出现该情况。</p>
<pre><code class="hljs language-txt copyable" lang="txt">问题项目模板和相关依赖的版本信息
vue-element-adamin 4.4.0
element-ui 2.13.2
sass 1.26.8
sass-loader 8.0.2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之前以为是字体图标文件加载问题，加上工作繁忙 😃，就没管它。今天做另一个控台项目，突然想起这事儿，为什么这个控台项目就没出现这个问题呢？ 看来这是个 BUG 呀，得找原因！</p>
<h2 data-id="heading-1">着手解决 BUG</h2>
<h3 data-id="heading-2">先网上寻求帮助</h3>
<p>先 google/baidu 一下，大部分的解释都是 ElementUI 使用的是 node-sass， 你的项目中使用 dart-sass 就会出现这个问题。</p>
<p>解决方案：卸载 sass 装 node-sass 即可。</p>
<p>可是Sass 官方都弃用了 node-sass ，推荐使用 sass (dart-sass) 。为啥我们还要换回去呢？有没有别的解决方案呢？</p>
<h3 data-id="heading-3">还是得靠自己</h3>
<p>对比了手上的两个控台项目，都是用的 dart-sass 呀？ 为什么一个有问题，一个没有问题呢？看来另有隐情。不想用过时的 node-sass，咋办呢？</p>
<h4 data-id="heading-4">第一步：看看各种状态下图标元素到底渲染的啥？</h4>
<p>打开「问题控台」，咦！刚好，icon 又乱码了。右键检查元素，查看结果如下：</p>
<p><img alt="icon-乱码.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f84226a8b5634ab2905618f816456325~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>咦！这个 icon 伪元素的 content 是 乱码。why？</p>
<p>刷新一下「问题控台」试试：</p>
<p><img alt="icon-刷新好了.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a64506c986b24a84855f33584ba3a33a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>刷新后图标正常显示了，但是伪元素的 content 怎么有点看不懂呢？</p>
<p>试试另一个「正常控台」：</p>
<p><img alt="另一个控台.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ac14f9d7b6a4da786ecf245f9f5ea6e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里的 content 正常。咦！为什么 el-icon 元素 css 样式在 chunk-elementUI.68c70ad5.css 文件里，而之前出问题的控台 el-icon 元素 css 样式在 app.ca199f0d.css 里。难道是打包的锅？ 对比一下两个项目的  vue.config.js ，关于 elementUI 的打包没有差异呀！</p>
<p><img alt="why.jpeg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d640de5dbc54a2ba59bf33b07b9c61e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">第二步：本地运行「问题控台」，定位问题</h4>
<p>找一个 el-icon 元素，查看元素 style：</p>
<p><img alt="icon-style.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86ef0fd6ae674a449dd0deec2ef595ba~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>点击右侧  ，跳转到对应的 css 样式文件：
</p><p><img alt="icon-style2.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92bbef8b553c493ebd93c82d177857af~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这是什么👻？让我来项目源代码，全局搜索 <code>I think ElementUI</code> 一下：</p>
<p><img alt="icon-style3.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3976f85e5884a0c8f3142c03d34cb12~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>哈哈，罪魁祸首难道就是你？</p>
<p><code>element-variable.scss</code>文件是<code> vue-element-adamin</code> 模板中用于 "在项目中改变SCSS变量 "。<code>vue-element-adamin</code> 的 <code>main.js</code> 和 <code>store/modules/settings.js</code> 都引用了这个文件。</p>
<p>现在尝试把两处的引用注释掉， main.js 改引用默认样式 <code>import 'ElementUI/lib/theme-chalk/index.css'</code>。页面刷新，检查元素：</p>
<p><img alt="icon-正常了.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08b952986e4345fcaf90fe68b39ef116~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>🤩正常了，问题解决了！此处有掌声 👏👏👏 ！</p>
<h4 data-id="heading-6">第三步：对比「问题控台」和「正常控台」</h4>

























<table><thead><tr><th></th><th>问题控台</th><th>正常控台</th></tr></thead><tbody><tr><td>模板</td><td>vue-element-adamin</td><td>vue-adamin-template</td></tr><tr><td>是否改变SCSS变量</td><td>是</td><td>否</td></tr><tr><td>相关依赖</td><td>element-ui 2.13.2<br>sass 1.26.8<br>sass-loader 8.0.2</td><td>element-ui 2.13.2<br>sass 1.26.8<br>sass-loader 8.0.2</td></tr></tbody></table>
<p>两个控台项目主要的差异是模板不同，vue-element-adamin 修改了 ElementUI 默认 SCSS变量，el-icon 相关的样式使用 dart-sass 重新打包到 app.css 文件，打包结果中 el-icon 元素的伪元素 content 属性异常。而vue-adamin-template 未修改默认样式，会直接采用 elementUI 打包好的样式文件，不再重新打包，也就不会出现乱码。</p>
<h3 data-id="heading-7">解决办法汇总</h3>
<ol>
<li>不去自定义 SCSS 变量，直接使用 ElementUI 打包好的样式文件。【我选的这个】</li>
<li>卸载 sass ，安装 node-sass。</li>
</ol>
<h2 data-id="heading-8">关于 node-sass 和 dart-sass</h2>
<p>SASS 官方团队，在2020年10月26号宣布弃用 Libsass （包括基于它构建的 node-sass  <a href="https://sass-lang.com/blog/libsass-is-deprecated" target="_blank" rel="nofollow noopener noreferrer">点击查看原文</a>） ，转向 dart-sass 。</p>
<p>为什么弃用 libSass， 因为 libSass 底层语言是C/C++，添加新功能变得困难。</p>
<p>Node-sass 存在的问题：npm 下载时间长， 安装时容易出错。目前，node-sass 已停止更新，只持续维护。</p>
<p>其他方面的对比：</p>






























<table><thead><tr><th></th><th>node-sass</th><th>dart-sass</th></tr></thead><tbody><tr><td>编译主体</td><td>用 node(调用 cpp 编写的 libsass)</td><td>drat VM</td></tr><tr><td>编译时机</td><td>自动实时编译</td><td>保存后</td></tr><tr><td>编译速度</td><td>快</td><td>比 node-sass 慢点</td></tr><tr><td>下载速度</td><td>慢</td><td>快（被编译为纯js）</td></tr></tbody></table>
<p>Vue 项目，node-sass 和 dart-sass 部分语法不兼容。dart-sass  支持 ::v-deep ，不支持 /deep/ 。</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.foo</span> /deep/ <span class="hljs-selector-class">.bar</span> &#123; <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>; &#125;
<span class="hljs-comment">// 使用 dart-sass 需改为</span>
<span class="hljs-selector-class">.foo</span> ::v-deep .b &#123; width: <span class="hljs-number">100px</span>; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说到深度选择器，<a href="https://github.com/vuejs/rfcs/blob/scoped-styles-changes/active-rfcs/0023-scoped-styles-changes.md" target="_blank" rel="nofollow noopener noreferrer">vue 官方 rfc</a> 给出新的写法。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-comment">/* DEPRECATED  >>> 和 /deep/ 也废弃了 */</span>
::v-deep .bar &#123;&#125;
  
<span class="hljs-comment">/* deep selectors */</span>
::<span class="hljs-built_in">v-deep</span>(.foo) &#123;&#125;

<span class="hljs-comment">/* targeting slot content 子组件内修改 slot 样式 */</span>
::<span class="hljs-built_in">v-slotted</span>(.foo) &#123;&#125;

<span class="hljs-comment">/* one-off global rule  全局范围 */</span>
::<span class="hljs-built_in">v-global</span>(.foo) &#123;&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">彩蛋</h2>
<p>基于Vue 3 的<a href="https://github.com/element-plus/element-plus/blob/dev/package.json" target="_blank" rel="nofollow noopener noreferrer">Element Plus</a> 使用的是 dart-sass！等等，我来看下<a href="https://element-plus.org/#/zh-CN/component/icon" target="_blank" rel="nofollow noopener noreferrer">Element Plus文档</a>的图标。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913a330597d14586908fa82ae3e26c5f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>为什么这里 el-icon 伪元素的 content 也是这样？为什么官方文档就没有出现乱码呢？那我上面一通分析个啥？我的解决方法太鸡肋了？呜呜！肯定 Element Plus 做了其他调整，心累！！！！！！！！！</p>
<p><img alt="崩溃.jpeg" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcc23e2f4d5741afb32d420bb670353e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            