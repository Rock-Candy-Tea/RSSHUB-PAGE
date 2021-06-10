
---
title: '09.ElementUI 2.X 源码学习_源码剖析之工程化(四)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7c724b7007f49078ba370566bbe42c0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 06:13:35 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7c724b7007f49078ba370566bbe42c0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>🎏 这是我参与更文挑战的第4天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<h1 data-id="heading-0">0x.00 📢 前言</h1>
<p>👇 项目工程化系列文章链接如下，推荐按照顺序阅读文章 👇。</p>
<p>1️⃣ <a href="https://juejin.cn/post/6969258163136626725" target="_blank">源码剖析之工程化(一)：项目概览、package.json、npm script</a><br>
2️⃣ <a href="https://juejin.cn/post/6969933702759940133" target="_blank">源码剖析之工程化(二)：项目构建、MD解析</a><br>
3️⃣ <a href="https://juejin.cn/post/6970691644114862111/" target="_blank">源码剖析之工程化(三)：打包配置</a><br>
4️⃣ <a href="https://juejin.cn/post/6971054455139598366/" target="_blank">源码剖析之工程化(四)：发布部署、持续集成</a></p>
<p>本系列文章主要通过解析element项目源码，从结构、功能、源码方面逐一解析，学习其模块化、组件化、规范化、自动化等多维度优秀实践。主要内容包含项目结构、npm script、项目构建、文档解析、打包配置、发布部署等。</p>
<p>本文是第四篇,介绍项目的发布部署、持续集成。</p>
<h1 data-id="heading-1">0x.01 🚀 发布部署</h1>
<p>执行命令 <code>npm run pub</code> 实现发布部署流程：</p>
<ul>
<li>本地代码检查合并，push到远程分支；</li>
<li>组件构建发布(npm pulish)；</li>
<li>官网发布部署。</li>
</ul>
<p>接下来详细介绍各 <code>shell</code> 脚本功能。</p>
<h2 data-id="heading-2">build/git-release.sh</h2>
<p>检查本地代码 <code>dev</code> 分支是否与线上分支存在冲突。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7c724b7007f49078ba370566bbe42c0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">build/release.sh</h2>
<p>主要作用代码分支合并push远程分支、版本号确认更新、组件主题发布(npm pulish)。</p>
<ol>
<li>合并 dev 分支到 master</li>
<li>通过 <code>select-version-cli</code> 确认发布版本号。</li>
<li>执行命令 <code>npm run dist</code>  打包构建组件。</li>
<li>运行ssr测试 <code>node test/ssr/require.test.js</code>。</li>
<li>发布主题，更新版本号，与组件库保持一致。</li>
<li>提交代码并更新package.json中的版本号 。</li>
<li>master 和 dev 分支push 到远程分支。</li>
<li>发布组件。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59550d03381d46e8ba5841bf6bc5da2c~tplv-k3u1fbpfcp-watermark.image" alt="carbon (92).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>select-version-cli</code> 提供选择发布版本选择。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4feea1adb27445b082e11842e06884ce~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择确认后，继续执行 <code>release.sh</code> 执行发布部署流程。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c1797177ab347db9385a94bab55b9cd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">🚧 build/deploy-faas.sh</h2>
<p>网站发布部署， 用于<code>faas deploy</code> 配置。在2.15版本之后移除了<code>pub</code>命令 <code>sh build/deploy-faas.sh</code>调用，集成至CI，详见<code>build/deploy-ci.sh</code>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7a7413a978c41a4b48e43dfacf2434d~tplv-k3u1fbpfcp-watermark.image" alt="carbon (93).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">0x.02 持续集成</h1>
<p>持续集成（Continuous Integration，简称 CI）指的是只要代码有变更，就自动运行构建和测试，反馈运行结果。确保符合预期以后，再将新代码"集成"到主干。持续集成的好处在于，每次代码的小幅变更，就能看到运行结果，从而不断累积小的变更，而不是在开发周期结束时，一下子合并一大块代码。</p>
<h3 data-id="heading-6">.travis.yml</h3>
<p>使用Travis CI 提供的是持续集成服务，项目的根目录下面必须有一个.travis.yml文件。这是配置文件，指定了 Travis 的行为。该文件必须保存在 Github 仓库里面，一旦代码仓库有新的 Commit，Travis 就会去找这个文件，执行里面的命令(执行测试、构建、部署等操作)。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cba5805cc37418d80f99c6e11f50137~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">build/deploy-ci.sh</h3>
<p>主要作用构建发行版本和开发版本内容。</p>
<ol>
<li>git config定义user.name和user.email。</li>
<li>发行版本构建(组件库、主题<code>theme-chalk</code>、项目网站)、打新标签。</li>
<li>开发分支的 主题<code>theme-chalk</code>、项目网构建提交到master分支。</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cd2483135e64096b50956e6e1e4983c~tplv-k3u1fbpfcp-watermark.image" alt="carbon (43).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">0x.03 makefile</h1>
<p><code>makefile</code>带来的好处就是<strong>自动化构建</strong>，一旦写好，只需要一个<code>make</code>命令，整个工程完全自动化，极大的提高了软件开发的效率。</p>
<blockquote>
<p>在软件开发中，<code>make</code> 是一个工具程序（Utility software），经由读取叫做 <code>makefile</code> 的文件，自动化建构软件。它是一种转化文件形式的工具，转换的目标称为 <code>target</code> ；与此同时，它也检查文件的依赖关系，如果需要的话，它会调用一些外部软件来完成任务。它使用叫做 <code>makefile</code> 的文件来确定一个 <code>target</code> 文件的依赖关系，然后把生成这个 <code>target</code> 的相关命令传给 <code>shell</code> 去执行。</p>
</blockquote>
<p>mac/linux 中直接可以执行 make 命令的(terminal bash)。 Windows下载 make 的 GUN 工具<a href="http://gnuwin32.sourceforge.net/packages/make.htm" target="_blank" rel="nofollow noopener noreferrer">Make for Windows</a></p>
<blockquote>
<p><strong>配置环境变量 Win</strong></p>
<p>右键<code>我的电脑</code>-><code>属性</code>-><code>高级</code>-><code>环境变量</code>-><code>系统变量</code>-><code>变量path</code>,然后在<code>path</code>中新建环境变量，目录定位到<code>make for windows</code>安装目录(默认路径 C:\Program Files (x86)\GnuWin32\bin\ )即可。</p>
</blockquote>
<p>若目录下没有 <code>makefile</code>,执行显示“没有指明目标并且找不到makefile ”，终止命令。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/674486e5d7664c2482f60e29efdc1083~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行 <code>make</code> 命令可以看到详细的使用说明。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/915ae59a64a64132a29145c7e14843f0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行<code> make target</code> 命令后，找到 <code>target</code> 对应的 <code>commonds</code>并执行。 查看源文件,每个<code>commonds</code>都是npm script，具体功能详见前文。(make help 输出文本存在转义字符，win系统无法支持)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/797f044c9b834682827409b7633a9a14~tplv-k3u1fbpfcp-watermark.image" alt="carbon (44).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">0x.04 🔖 链接汇总</h1>
<p>点击以下链接，可以快速查看本系列其他文章：</p>
<p><a href="https://juejin.cn/post/6950907020069306399" target="_blank">ElementUI源码学习:从零开始搭建Vue组件库汇总</a></p>
<h1 data-id="heading-10">0x.05 📚 参考</h1>
<p><a href="http://www.ruanyifeng.com/blog/2017/12/travis_ci_tutorial.html" target="_blank" rel="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2017/1…</a><br>
<a href="https://juejin.cn/post/6844903775912591368" target="_blank">juejin.cn/post/684490…</a></p></div>  
</div>
            