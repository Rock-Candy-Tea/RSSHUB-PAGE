
---
title: 'uni-app多环境配置｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff40924adb1e4c4fad9baf3d529b6b77~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 00:22:36 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff40924adb1e4c4fad9baf3d529b6b77~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>  uniapp自身的配置只区分了生产<code>（NODE_ENV=production）</code>和非生产<code>(NODE_ENV=development)</code>环境，两者是uniapp内置的用来区分行为的。比如在小程序使用不同的环境变量时会在 dist文件夹下生成对应的 dev目录或者 build目录。但是在实际开发以及部署时还需要区分多套环境api配置。</p>
<hr>
<h5 data-id="heading-0">1. 通过cli方式构建uniapp项目</h5>
<p>uniapp提供两种方式创建项目：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.io%2Fquickstart-hx" target="_blank" rel="nofollow noopener noreferrer" title="https://uniapp.dcloud.io/quickstart-hx" ref="nofollow noopener noreferrer">1.通过HbuilderX编辑器创建</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.io%2Fquickstart-cli" target="_blank" rel="nofollow noopener noreferrer" title="https://uniapp.dcloud.io/quickstart-cli" ref="nofollow noopener noreferrer">2.通过vue-cli创建</a></p>
<p>第一方式只能通过Hbuilderx进行开发运行发布没有对外暴露配置文件，区分多环境想到的办法只能是手动切换变量去加载不同的api。而第二种方式就可以使用自己顺手的编辑器开发(vscode yyds)，只要修改一下webpack的配置，使用不同的运行打包命令，就可以区分对应的环境配置，也方便jenkins自动打包部署。</p>
<p>如图，通过cli创建项目后 <code>package.json</code>文件中会有对应的运行和打包命令：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff40924adb1e4c4fad9baf3d529b6b77~tplv-k3u1fbpfcp-watermark.image" alt="uniapp1.png" loading="lazy" referrerpolicy="no-referrer">
需要注意的是命令中的<code>NODE_ENV</code>变量是不能修改的，上面已经介绍过了它属于uniapp内置的，可以创建其他变量来区分环境。</p>
<h5 data-id="heading-1">2. 创建对应环境文件</h5>
<p>假如需要区分出 开发测试环境、uat环境和生产环境，需要在根目录下创建对应的环境文件，命名方式：<code>.env.环境名</code></p>
<p>.env.dev</p>
<pre><code class="copyable"># 开发环境配置
VUE_APP_ENV='dev'
VUE_APP_BASE_API = 'https://dev.com'

<span class="copy-code-btn">复制代码</span></code></pre>
<p>.env.uat</p>
<pre><code class="copyable"># uat环境配置
VUE_APP_ENV='uat'
VUE_APP_BASE_API = 'https://uat.com'

<span class="copy-code-btn">复制代码</span></code></pre>
<p>.env.pro</p>
<pre><code class="copyable"># 生产环境配置
VUE_APP_ENV='pro'
VUE_APP_BASE_API = 'https://pro.com'

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">3. 修改package.json</h5>
<p>以h5环境下为例(为了简洁其他终端先删除)，在每个环境的命令下增加 <code>--mode xxx</code>参数，名称与创建的环境文件对应</p>
<p>修改前：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db11f09c423e4f1183358ded2a089137~tplv-k3u1fbpfcp-watermark.image" alt="uniapp2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改后：</p>
<pre><code class="copyable">"scripts": &#123;
    "dev:h5-dev": "cross-env NODE_ENV=development UNI_PLATFORM=h5 vue-cli-service uni-serve --mode dev",
    "dev:h5-uat": "cross-env NODE_ENV=development UNI_PLATFORM=h5 vue-cli-service uni-serve --mode uat",
    "dev:h5-pro": "cross-env NODE_ENV=development UNI_PLATFORM=h5 vue-cli-service uni-serve --mode pro",
    "build:h5-dev": "cross-env NODE_ENV=production UNI_PLATFORM=h5 vue-cli-service uni-build --mode dev",
    "build:h5-uat": "cross-env NODE_ENV=production UNI_PLATFORM=h5 vue-cli-service uni-build --mode uat",
    "build:h5-pro": "cross-env NODE_ENV=production UNI_PLATFORM=h5 vue-cli-service uni-build --mode pro"
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>此时我们再执行对应的命令，打印一下<code>process.env</code>,会发现不同的环境文件内的变量加载成功了</p>
<p>npm run dev:h5-dev/yarn dev:h5-dev
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cf643784dd2428cb1b2de478d183656~tplv-k3u1fbpfcp-watermark.image" alt="uniapp3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>npm run build:h5-pro/yarn build:h5-pro
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d1caaf436c64fda8b9e84655ff02737~tplv-k3u1fbpfcp-watermark.image" alt="uniapp4.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            