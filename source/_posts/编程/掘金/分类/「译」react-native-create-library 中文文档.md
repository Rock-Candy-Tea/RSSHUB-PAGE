
---
title: '「译」react-native-create-library 中文文档'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8565'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 07:31:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=8565'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<p>react-native-create-library 使你可以使用一个命令创建 React Native 原生库的工具</p>
<h3 data-id="heading-0">一、你为什么需要这个？</h3>
<p>如果您要为 React Native 创建原生模块，则需要为要支持的每个平台提供一些原生代码，然后和一些 JavaScript 代码绑定在一起。自己设置可能非常耗时。</p>
<p>这就是这个工具的用武之地。它创建了一个包含所有当前最佳实践的样板。为什么不用 <code>react-native new-library</code>？不幸的是，该命令不会创建一个最新的库，需要一个已经初始化的 React Native 项目，并且只设置 iOS 方面的东西。</p>
<blockquote>
<p>警告：这仅创建没有视图组件的原生模块。</p>
</blockquote>
<h3 data-id="heading-1">二、安装</h3>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm install -g react-native-create-library
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个命令将会创建一个 <code>MyFancyLibrary</code> 文件夹，现在可以执行 <code>yarn install</code> 来为你新创建的 <code>Library</code> 安装依赖。</p>
<h3 data-id="heading-2">三、命令</h3>
<blockquote>
<p><code>react-native-create-library [options] <name></code></p>
</blockquote>
<p><strong>选项：</strong></p>
<ul>
<li><code>-h</code>、<code>--help</code>: 输入有用的信息</li>
<li><code>-V</code>、<code>--version</code>: 输出版本号</li>
<li><code>-p</code>、<code>--prefix <prefix></code>: 库的前缀（默认：<code>RN</code>）</li>
<li><code>--module-prefix <modulePrefix></code>: 库的模块前缀（npm）（默认<code>react-native</code>）</li>
<li><code>--package-identifier <packageIdentifier></code>: (Android only!) The package name for the Android module (Default: <code>com.reactlibrary</code>)</li>
<li><code>--namespace <namespace></code>: (Windows only!) The namespace for the Windows module(Default: The name as PascalCase)</li>
<li><code>--platforms <platforms></code>: 支持的平台（用逗号隔开，默认：<code>ios,android,windows</code>）</li>
<li><code>--github-account <github_account></code>: 托管库的 github 账号（默认：<code>github_account</code>）</li>
<li><code>--author-name <name></code>: 作者的名字（默认：<code>Your Name</code>）</li>
<li><code>--author-name <email></code>: 作者的邮箱（默认：<code>yourname@email.com</code>）</li>
<li><code>--license <license></code>: The license type of this library (Default: <code>Apache-2.0</code>)</li>
<li><code>--generate-example <shouldGenerate></code>: 会生成一个 RN 例子并且 <code>link</code> 刚生成的库（默认：<code>false</code>）</li>
</ul>
<h3 data-id="heading-3">四、程序化使用</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> createLibrary = <span class="hljs-built_in">require</span>(<span class="hljs-string">'react-native-create-library'</span>)

createLibrary(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'MyFancyLibrary'</span>,
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Oh yay! My library has been created!'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">选项</h4>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span>, <span class="hljs-comment">/* The name of the library (Default: Library) */</span>
  <span class="hljs-attr">prefix</span>: <span class="hljs-built_in">String</span>, <span class="hljs-comment">/* The prefix for the library (Default: RN) */</span>
  <span class="hljs-attr">modulePrefix</span>: <span class="hljs-built_in">String</span>, <span class="hljs-comment">/* The module prefix for the library (Default: react-native) */</span>
  <span class="hljs-attr">platforms</span>: <span class="hljs-built_in">Array</span>, <span class="hljs-comment">/* Platforms the library will be created for. (Default: ['ios', 'android', 'windows']) */</span>
  <span class="hljs-attr">packageIdentifier</span>: <span class="hljs-built_in">String</span>, <span class="hljs-comment">/* (Android only!) The package name for the Android module (Default: com.reactlibrary) */</span>
  <span class="hljs-attr">namespace</span>: <span class="hljs-built_in">String</span>, <span class="hljs-comment">/* (Windows only!) The namespace for the Windows module (Default: The package identifier as PascalCase, which is `Com.Reactlibrary`) */</span>
  <span class="hljs-attr">githubAccount</span>: <span class="hljs-built_in">String</span>, <span class="hljs-comment">/* The github account where the library is hosted (Default: `github_account`) */</span>
  <span class="hljs-attr">authorName</span>: <span class="hljs-built_in">String</span>, <span class="hljs-comment">/* The author's name (Default: `Your Name`) */</span>
  <span class="hljs-attr">authorEmail</span>: <span class="hljs-built_in">String</span>, <span class="hljs-comment">/* The author's email (Default: `yourname@email.com`) */</span>
  <span class="hljs-attr">license</span>: <span class="hljs-built_in">String</span>, <span class="hljs-comment">/* The license type of this library (Default: `Apache-2.0`) */</span>
  <span class="hljs-attr">generateExample</span>: <span class="hljs-built_in">Boolean</span>, <span class="hljs-comment">/* Will generate a RN example project and link the new library to it (Default: `false`) */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            