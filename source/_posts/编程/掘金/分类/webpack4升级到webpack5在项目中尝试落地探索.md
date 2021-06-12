
---
title: 'webpack4升级到webpack5在项目中尝试落地探索'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/132543a2d50e45798550a918ba8658ad~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 04:40:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/132543a2d50e45798550a918ba8658ad~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>有些老项目的包长时间没有更新，导致项目中有些性能问题，在项目迭代中考虑升级包，开始查找相关资料；</p>
<h1 data-id="heading-0">简单“粗暴”的升级方式</h1>
<p>当然包升级后带来的一些问题，需要更全面的思考，此处先省略...
直接进入主题：
npm包升级工具：
npm-check-updates
<a href="https://github.com/dylang/npm-check" target="_blank" rel="nofollow noopener noreferrer">npm-check</a>
在本地执行安装命令如下：</p>
<pre><code class="copyable">npm install -g npm-check-updates
// 升级npm包
ncu -u
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对<code>package.json</code>所有的包进行统一升级，执行情况如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/132543a2d50e45798550a918ba8658ad~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>包安装升级完成，但是项目跑不起来。。</p>
<ol>
<li>首先第一个问题来了</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcfee37e2efd4a4b84c3625fc8702be6~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">仔细查看错误信息，是webpack报错了；
看了下，之前的webpack包版本是4.12.0，升级后包版本5.37.1
查看webpack官方升级版本说明后，是因为启动方式发生了变化，</p>
<pre><code class="copyable">// 之前的命令
webpack-dev-server XXX
//新版本
webpack serve
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>第二个问题</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e9d5b775db9486294d92f707697ceac~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
webpack.NamedModulesPlugin is not a constructor
webpack包4.XX需要配置</p>
<pre><code class="copyable">new webpack.NamedModulesPlugin(),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack 5默认内置了该配置功能，不需要再配置</p>
<ol start="3">
<li>第三个问题</li>
</ol>
<p>webpack版本4.12.0
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8fcaf07f8804a2c89ff4fbecafe9387~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
webpack版本5，对象形式获取
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33ee501a88a94880ad2505be3a637ddc~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
第四个问题
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f37b362fb354f0d96eb0ead34ec9561~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
找了很多网上资料，应该是webpack5的问题，但不确定，卡在了这一步，没有进行下去；
由于时间关系，暂时先不做升级，后续有时间再继续</p>
<h1 data-id="heading-1">优雅细致的升级方式</h1>
<pre><code class="copyable">npm install -g npm-check
// 查看选择升级包
npm-check -u
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选择相应版本升级
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10871db04d0148acabd6124b542380ac~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            