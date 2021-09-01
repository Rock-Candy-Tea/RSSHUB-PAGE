
---
title: 'Windows电脑反编译微信小程序含分包详细操作'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e2ea2ebe726449f81cc975468b3ae35~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 01:10:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e2ea2ebe726449f81cc975468b3ae35~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>现在网上也有很多关于小程序反编译的教程，随时间的流逝或许随着微信的更新，有出现编译不成功的现象。</p>
<p>本篇文章总结一下最新的编译过程，已成功获得小程序源码（有分包的小程序）</p>
<h2 data-id="heading-0">环境准备</h2>
<h3 data-id="heading-1">1、 node 环境准备</h3>
<p>下载链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fen%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/en/" ref="nofollow noopener noreferrer">nodejs.org/en/</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e2ea2ebe726449f81cc975468b3ae35~tplv-k3u1fbpfcp-watermark.image" alt="image-20210901154759757" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装后将nodejs设置为环境变量。<br>
打开cmd，测试是否安装成功：在命令行输入node -v 出现版本号说明已经安装成功。</p>
<h3 data-id="heading-2">2、反编译工具</h3>
<p>项目地址来自于： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxuedingmiaojun%2FwxappUnpacker" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xuedingmiaojun/wxappUnpacker" ref="nofollow noopener noreferrer">github.com/xuedingmiao…</a></p>
<p><strong>通过下面链接下载：</strong></p>
<p>链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpan.baidu.com%2Fs%2F1p-wnX-mXr-Du0iJK_dT8RQ" target="_blank" rel="nofollow noopener noreferrer" title="https://pan.baidu.com/s/1p-wnX-mXr-Du0iJK_dT8RQ" ref="nofollow noopener noreferrer">pan.baidu.com/s/1p-wnX-mX…</a><br>
提取码：z06a</p>
<p><strong>下载下来解压到某个位置就可以了，一定要通过网盘下载，里面有解密包的工具和安装后的npm环境，直接使用即可</strong></p>
<h2 data-id="heading-3">具体操作</h2>
<h3 data-id="heading-4">1、微信PC获取小程序</h3>
<p><strong>在通过微信PC打开小程序前，我们最好先找到缓存到本地的小程序包路径，一般都是在 <code>微信PC安装目录\WeChat Files\WeChat Files\Applet</code></strong></p>
<p>比如我的就是安装到 <code>D盘根目录的</code>，所以路径为： <code>D:\WeChat\WeChat Files\WeChat Files\Applet</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc048796659949dca8c366d721804376~tplv-k3u1fbpfcp-watermark.image" alt="image-20210901160649022" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>上图中每个文件夹代表一个小程序，一般最新打开的小程序都是在第一个，如果不确定可以排序一下修改日期</strong></p>
<p>找到路径了我们就可以用微信PC打开小程序了，打开后就会发现当前目录新增了一个文件夹，里面存放的就是加密后的小程序包</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74cfbc7699424c21a108ef3f431beb9e~tplv-k3u1fbpfcp-watermark.image" alt="image-20210901161153138" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">2、解密包</h3>
<p>刚获取到的包我们还不能进行反编译，必须要通过 <code>解密软件</code> 修改一下才能反编译</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0dc8ec3596224194b811771c87aafb91~tplv-k3u1fbpfcp-watermark.image" alt="image-20210901161556010" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>本篇就演示一个主包和一个分包反编译的过程就可以了，先通过<code>解密软件</code>修改一下主包</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99fa270cf39947b3a420685c60041da4~tplv-k3u1fbpfcp-watermark.image" alt="image-20210901161936026" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>解密的主包自动到 <code>wxpack</code> 这个包里面来了，同样的步骤解密一个分包，下图是我解密好的两个，并且修改了一下名称，好区分</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7786c2a946fd494d807b33e44ed2aca6~tplv-k3u1fbpfcp-watermark.image" alt="image-20210901162219406" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">3、反编译</h3>
<p>进入 <code>wxpack</code> 的同级目录 <code>wxappUnpacker-master</code>，在路径栏输入 <code>cmd</code> 自动打开当前目录的 <strong>命令窗口了</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74627aaef6974437b1d3326ec9c50b5d~tplv-k3u1fbpfcp-watermark.image" alt="image-20210901162538413" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>先反编译一下主包，把反编译后的文件夹放到 <code>wxpack</code> 同级目录中</strong></p>
<pre><code class="copyable">node wuWxapkg.js ..\wxpack\master-app.wxapkg

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f8122d2778c4c8db2a7c0adc3f47a2f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210901163011475" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>再反编译分包，把反编译后的文件夹放到 <code>wxpack</code> 同级目录中</strong></p>
<pre><code class="copyable">node wuWxapkg.js -s=..\ ..\wxpack\_pages_app.wxapkg

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>-s</code> 表示分包</li>
<li>第一个<code>..\</code> 表示输出位置</li>
<li><code>..\wxpack\_pages_app.wxapkg</code> 需要反编译的分包位置</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abd25ea16721428d9515fe276fd81f73~tplv-k3u1fbpfcp-watermark.image" alt="image-20210901163627239" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了剩下的就是自己组合一下包的架构目录了~~~~</p>
<p>如果本篇文章给予了您一点帮助，还请点个赞收藏一下~~</p>
<p>谢谢您的支持！！！</p></div>  
</div>
            