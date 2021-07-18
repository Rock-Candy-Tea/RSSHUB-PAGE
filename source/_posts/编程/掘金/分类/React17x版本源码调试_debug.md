
---
title: 'React17.x版本源码调试_debug'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4f61dbf311441618679fcd25b6cece0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 01:57:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4f61dbf311441618679fcd25b6cece0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>申明：本文所有操作均参考React的官方文档，结合自己的调试思路，梳理的文档。</p>
<blockquote>
<p>当前react版本为17.0.3，原官方文档链接~~ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh-hans.reactjs.org%2Fdocs%2Fhow-to-contribute.html%23development-workflow" target="_blank" rel="nofollow noopener noreferrer" title="https://zh-hans.reactjs.org/docs/how-to-contribute.html#development-workflow" ref="nofollow noopener noreferrer">zh-hans.reactjs.org/docs/how-to…</a>~~</p>
</blockquote>
<p>通过下载react源码，是不可以直接进行react的源码调试。需要对源码进行打包，生成react、react-dom打包后的代码，然后在自己creat-react-app创建的项目中link到打包后的react、react-dom文件。那么在your app中使用的react、react-dom，就是react源码打包后的文件。
<br>但是，打包后的文件依然保留着源码中的方法名，我们可以先阅读源码，如果想要在源码中需要对某个方法进行打断点，可以在打包后的代码中搜索该方法，然后进行断点调试。</p>
<ol>
<li>
<p>安装Nodev8.0.0+,<a href="https://link.juejin.cn/?target=https%3A%2F%2Fyarnpkg.com%2Fen%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://yarnpkg.com/en/" ref="nofollow noopener noreferrer">Yarn</a> v1.2.0+,<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oracle.com%2Ftechnetwork%2Fjava%2Fjavase%2Fdownloads%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oracle.com/technetwork/java/javase/downloads/index.html" ref="nofollow noopener noreferrer">JDK</a><br>yarn可以使用 npm yarn -g 全局安装，JDK可以去官网下载JDK安装包并自行安装。</p>
</li>
<li>
<p><code>git clone https://github.com/facebook/react.git</code><br>下载react项目到本地。</p>
</li>
<li>
<p>打包react项目 <br>  <code>cd ~/path_to_your_react_clone/</code>  // 进入到你本地react源码项目中<br><code>yarn build react/index,react/jsx,react-dom/index,scheduler --type=NODE</code> // 打包react项目</p>
</li>
<li>
<p>进入到build目录中，使用 <code>yarn link</code> 将react，react-dom指向本地文件夹的 <code>build</code> 目录。<br><code>cd build/node_modules/react</code><br><code>yarn link</code><br><code>cd build/node_modules/react-dom</code><br><code>yarn link</code></p>
</li>
<li>
<p>进入到你create-react-app创建的项目，将项目中使用的react、react-dom link到本地的build目录。<br><code>yarn link react react-dom</code></p>
</li>
</ol>
<p><br>** 需要注意的是，每次打完断点，都需要yarn start你创建的项目，断点才会生效。</p>
<h4 data-id="heading-0">接下来我们就开始尝试一下吧 =。=</h4>
<p>在react打包后源码中加上一行日志</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4f61dbf311441618679fcd25b6cece0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重新启动项目后，就可以在浏览器中生效了～</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ef56f1319f047119422b47230a56e5c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来，就可以开始我们的调试之旅了。</p></div>  
</div>
            