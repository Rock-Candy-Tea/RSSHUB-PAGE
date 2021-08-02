
---
title: '【Vitejs源码学习】Debug ViteJS,走进学习源码的第一步'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a575805166ee4adcaab985eb26c75b09~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 08:04:28 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a575805166ee4adcaab985eb26c75b09~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;position:relative;background-image:linear-gradient(90deg,rgba(217,234,251,.25) 3%,transparent 0),linear-gradient(1turn,rgba(217,234,251,.25) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;padding-left:8px;padding-bottom:0;margin-top:35px;margin-bottom:10px;font-weight:900;font-family:serif;letter-spacing:1px;color:#000&#125;.markdown-body h1:hover,.markdown-body h2:hover,.markdown-body h3:hover,.markdown-body h4:hover,.markdown-body h5:hover,.markdown-body h6:hover&#123;background-color:#fff&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;font-size:24px;position:relative&#125;.markdown-body h2:after&#123;content:"";left:0;bottom:0;width:100%;height:1px;position:absolute&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-size:4px 1px;background-image:linear-gradient(270deg,#37b2ff 0,#37b2ff 25%,transparent 50%)&#125;.markdown-body code&#123;margin:0 4px;word-break:break-word;overflow-x:auto;background-color:#fff7f7;color:#f06;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:-apple-system,system-ui,Menlo,Monaco,Consolas,Courier New;position:relative&#125;.markdown-body pre&#123;margin:15px 8px;border:1px solid #f5f5f7;line-height:1.75&#125;.markdown-body pre:before&#123;top:-4px;left:-4px;border-top:8px solid #feea1e;border-left:8px solid #feea1e&#125;.markdown-body pre:after,.markdown-body pre:before&#123;width:20px;height:20px;content:"";z-index:10;position:absolute&#125;.markdown-body pre:after&#123;right:-4px;bottom:-4px;border-right:8px solid #37b2ff;border-bottom:8px solid #37b2ff&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;overflow-x:auto;margin:0;word-break:normal;display:block;color:#333;background-color:#fff;background-image:linear-gradient(135deg,hsla(0,0%,87.8%,.1),hsla(0,0%,87.8%,.1) 25%,transparent 0,transparent 50%,hsla(0,0%,87.8%,.1) 0,hsla(0,0%,87.8%,.1) 75%,transparent 0,transparent)!important;background-size:10px 10px!important;position:unset!important&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#37b2ff;transition:.3s;border-bottom:1px dashed #37b2ff;position:relative;display:inline-block;vertical-align:bottom&#125;.markdown-body a:before&#123;bottom:90%;width:120px;max-width:0;content:"READ MORE +";color:#fff;background-color:#1fb3ff;position:absolute;white-space:nowrap;transition:.3s;box-sizing:border-box;pointer-events:none;overflow:hidden&#125;.markdown-body a:active:before,.markdown-body a:hover:before&#123;max-width:120px;padding-left:14px&#125;.markdown-body table&#123;width:100%;max-width:100%;font-size:12px;background-color:#fff;overflow:auto;border-collapse:collapse&#125;.markdown-body table tr:hover td,.markdown-body table tr:hover th&#123;border-bottom:1px solid #feea1e&#125;.markdown-body thead&#123;text-align:left&#125;.markdown-body th&#123;font-size:1.2em;border-bottom:1px dashed #eee&#125;.markdown-body tr:nth-child(2n)&#123;background-color:hsla(0,0%,87.8%,.1);border-bottom:1px solid #fff&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px;border-bottom:1px dashed #fff&#125;.markdown-body blockquote&#123;color:#666;padding:12px 23px 2px;border:1px solid #37b2ff;background-color:#fff;margin:22px 0;position:relative&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body blockquote:after&#123;content:"FROM";left:0;width:40px;color:#fff;background-color:#37b2ff;text-align:center&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;top:0;line-height:1;padding:2px 0;font-size:12px;font-weight:lighter;position:absolute;pointer-events:none&#125;.markdown-body blockquote:before&#123;content:"CITATION";left:44px;color:#37b2ff&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;line-height:2em;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol ol li,.markdown-body ol ul li,.markdown-body ul ol li,.markdown-body ul ul li&#123;border-bottom:none&#125;.markdown-body ol li&#123;padding-left:6px;list-style:decimal-leading-zero&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;.markdown-body input[type=checkbox i]:disabled&#123;background-color:#6cf&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li>开发工具 vscode</li>
<li>node 版本：node expected version "^10.13.0 || ^12.13.0 || ^14.15.0 || >=15.0.0".</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a575805166ee4adcaab985eb26c75b09~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">Debug ViteJS,走进学习源码的第一步</h1>
<h2 data-id="heading-1"><code>fork</code> 源仓库到你的仓库</h2>
<p>从仓库<code>fork</code>最新源码到您的仓库有便于向项目提交<code>PR</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93afa6b2829c472787fbde891c94538c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2"><code>clone</code> :clone 项目到你的本地，这里以我的clone仓库为例</h2>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 克隆项目</span>
<span class="hljs-comment"># cnpmjs</span>
git <span class="hljs-built_in">clone</span> https://github.com.cnpmjs.org/GeekQiaQia/vite.git

<span class="hljs-comment"># or</span>
git <span class="hljs-built_in">clone</span> https://github.com/GeekQiaQia/vite.git


<span class="hljs-comment"># 进入项目目录</span>
<span class="hljs-built_in">cd</span> vite

<span class="hljs-comment"># 安装依赖</span>
yarn / npm install

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3"><code>link vite</code>  :cd到vite根目录下 link vite</h2>
<p><code>mono-repo</code> 需要通过link的方式公用多repo项目资源</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># vite 根目录</span>
yarn/npm link
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09e0388e6d114295bcd03930eed6b3c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4"><code>启动playground</code> : palyground 用于测试vite所有功能</h2>
<pre><code class="copyable"># vite/packages/playground
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1dbd1d453e74d8bbae0afb577475d0c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">我们选择测试vue的测试目录</h4>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># vite/packages/playground/vue</span>

<span class="hljs-comment"># 安装vue项目依赖</span>
yarn/ npm install 

<span class="hljs-comment"># 启动测试项目</span>
yarn / npm run dev

<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动vue3.0测试项目：<a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A3000%2F%25EF%25BC%258C%25E5%258F%25AF%25E9%2592%2588%25E5%25AF%25B9vite%25E5%25AF%25B9vue3.0%25E7%259A%2584%25E5%2590%2584%25E9%25A1%25B9%25E5%258A%259F%25E8%2583%25BD%25E6%25B5%258B%25E8%25AF%2595%25EF%25BC%259B" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:3000/%EF%BC%8C%E5%8F%AF%E9%92%88%E5%AF%B9vite%E5%AF%B9vue3.0%E7%9A%84%E5%90%84%E9%A1%B9%E5%8A%9F%E8%83%BD%E6%B5%8B%E8%AF%95%EF%BC%9B" ref="nofollow noopener noreferrer">http://localhost:3000/，可针对vite对vue3.0的各项功能测试；</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d19a7bfa5e1748f9bff8ffe9991cb64d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff8eaae662054301a4a9b738b7087eac~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">启动vite 项目</h2>
<pre><code class="copyable"># node 版本：node expected version "^10.13.0 || ^12.13.0 || ^14.15.0 || >=15.0.0". 
yarn / npm  install 
# 启动 rollup 
yarn / npm dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时vite项目生成dist目录：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea3b2d3fe0c7414cbfb793fc9f881476~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>client</code>文件的内容比较简单清晰，并且我们在启动的<code>palygrund</code>项目中可以直接调试；我们主要以node服务文件debug调试为主；</p>
<p>我们以node服务端文件vite的入口文件<code>cli.ts</code>文件为例，我们在createServer创建开发服务处打<code>debug</code>断点调试；</p>
<ul>
<li>开启vscode 调试模块，选择node.js环境；</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4b4b03327241ba8ae7e28e0a2cd18c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>此时即可进入debug模式，可以根据需要单步断点调试；</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f20586b6e6314057898d42ebe1f74079~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>通过调用栈，我们可以很清楚的知道vitejs的执行流程；</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b4ce37ca7244ff38ae811338449d981~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">开启你的<code>debug ViteJS</code> 源码调试之旅吧</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/203d2a57a66440d1882d71493730d3f4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            