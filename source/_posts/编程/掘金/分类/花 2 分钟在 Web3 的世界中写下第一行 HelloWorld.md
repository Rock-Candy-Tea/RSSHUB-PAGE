
---
title: '花 2 分钟在 Web3 的世界中写下第一行 HelloWorld'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dce59f34bfd54242b2351b55c3728163~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 02:06:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dce59f34bfd54242b2351b55c3728163~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第6篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<p>要说如今互联网中最大的变数，毫无疑问就是 Web3。</p>
<p>不管是互联网大厂，还是互联网独角兽，都在 Web3 的市场存在大量空缺。</p>
<h1 data-id="heading-0">Web3 的市场</h1>
<p>先来看两张图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dce59f34bfd54242b2351b55c3728163~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>\</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4fa2e990bb941c19eff4ca2d7b8923b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>它们来自于我的朋友圈某位猎头。</p>
<p>从我的朋友圈中一些招聘上就可以看出来，尽管 2022 年的全球资本进入了寒冬期，但 Web3 的市场还处于蓝海期。</p>
<p>很多人想入门 Web3，但是又不知道该如何入门 Web3。</p>
<p>所以我打算写一些 Web3 开发相关的文章。</p>
<p>这篇文章适合那些从来没有写过 Web3 但又想体验一下 Web3 代码该如何写的新手，通过阅读本文，你可以在 Web3 的世界里写下一个 HelloWorld 程序。</p>
<h1 data-id="heading-1">编程语言 Solidity</h1>
<p>实际上 Web3 的范围很大，文中所指的，是用 Solidity 语言编写一个 ETH 的程序。</p>
<p>Solidity 是一种编程语言，是 Web3 首选语言。</p>
<h1 data-id="heading-2">代码编辑器 Remix</h1>
<p>大家在写 Web2 程序时，通常喜欢使用 VSCode 这类 IDE 在本地编写。与传统的 Web2 不一样，Web3 的代码编辑器 remix 是一个云端 IDE。我们可以通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fremix.ethereum.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://remix.ethereum.org/" ref="nofollow noopener noreferrer">remix</a> 在浏览器中编写代码。</p>
<p>打开之后是这个样子。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a450c5259e141eea799ae03ac87444e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">编写 HelloWorld.sol 代码</h1>
<p>默认情况下 remix 已经帮我们创建了一些模板文件。</p>
<p>我们创建一个新的 HelloWorld.sol 文件。sol 是 Solidity 语言所对应的文件后缀。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a233bbbae154441386eb65c4848b1ce3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后以下编写代码，solidity 的语法并不复杂，和主流编程语言很像。</p>
<pre><code class="hljs language-ini copyable" lang="ini">// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.7<span class="hljs-comment">;</span>

contract MyContract &#123;
    string public <span class="hljs-attr">hello</span> = <span class="hljs-string">"Hello World"</span><span class="hljs-comment">;</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我简单的解释一下它们的作用。</p>
<p>第一行是一句注释，表示采用 GPL-3.0 许可证。</p>
<p>第三行是指定 solidity 的版本，solidity 和 npm 的一样采用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsemver.org%2Flang%2Fzh-CN%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://semver.org/lang/zh-CN/" ref="nofollow noopener noreferrer">semver</a> 版本规范。</p>
<p>第五行是声明了 contract，它和传统语言中的 class 很相似。</p>
<p>第六行在 MyContract 中声明了一个公开的 hello 字段。</p>
<h1 data-id="heading-4">编译</h1>
<p>使用 solidity 编写的代码也需要编译。</p>
<p>最新版本的 remix 在文件保存后自动编译。</p>
<p>在 remix 左侧菜单栏的第三个按钮就是编译相关的设置。</p>
<p>我们不需要修改任何设置，点击 Compile HelloWorld.sol 即可。</p>
<p>编译成功后图标上会有一个绿色的对号。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b507eb7572d44eb291737606609bcdb8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">部署</h1>
<p>Remix 的强大之处在于它不仅仅将代码编辑器搬到了浏览器中，而且还集成了编译和部署的能力。基本上所有的事情都可以通过 Remix 在线完成。</p>
<p>右侧菜单栏第四个图标是部署相关的配置。</p>
<p>我们不需要修改任何参数，点击橙色按钮 Deploy 就可以了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f9337c62fc54d98b4e7b57219917f5a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">测试</h1>
<p>部署成功后，在 Deployed Contracts 中会有一个地址。</p>
<p>我们点开它，然后有一个 hello 按钮，再点击这个按钮，就可以看到它所对应的字符串“hello world”了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de797a16b58a449a9e45341c37f81b0c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            