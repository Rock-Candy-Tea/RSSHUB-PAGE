
---
title: '新手0基础如何轻松部署vue项目到服务器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/557a480048484415af07f9161d3dd778~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 19:03:03 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/557a480048484415af07f9161d3dd778~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<blockquote>
<p>嗨~，大家好，我是彪彪，又快要到金九银十的日子了，很多小伙伴应该和我一样，为了让自己的简历更加亮眼一点而选择写一个项目吧，结果我发现最难的不是写项目，而是如何把项目部署到服务器上，苦于没有关于这方面的知识，这期间我踩了不少坑，为了防止有和我一样的同学，我决定写这样一篇教学，从购买好服务器后，如何一步步把项目部署上去。本教程只要你有一个可以在本地允许的项目，那么跟着教程一步步操作即可。</p>
</blockquote>
<p>再次声明，本教程属于新手类的，怎么简单怎么方便就怎么来，里面会配有大量的图片，目的只有一个：让和我一样的新手可以轻易的项目部署的服务器，所以步骤看着会很繁琐，大神看个乐就行。</p>
<p>先说一下我这个项目所用的技术栈是前端：vue，后端：node.js，数据库：MongoDB，下面大部分内容其实都是讲解如何安装所用到的软件，如果不需要可以通过目录跳转到需要的地方。</p>
<h1 data-id="heading-1">前期准备工作</h1>
<h2 data-id="heading-2">1.服务器的选型</h2>
<blockquote>
<p>这里我是用了阿里云服务器，（腾讯云我已经部署好了，为了模拟第一次这次选用阿里云，其实操作都差不多），系统选用的是Windows Server 2019 数据中心版 64位中文版，这里也是为了更加方便的部署，毕竟让自己项目能从服务器中跑起来才是最主要的。<del>其实主要是因为我不懂Linux命令</del></p>
</blockquote>
<h2 data-id="heading-3">2.远程链接</h2>
<blockquote>
<p>系统安装好了我们就开始链接服务器吧，这个时候用Windows做服务器的优势就出来了，我们可以利用Windows的远程桌面连接来进入服务器和上传文件，用Mac的我在网上找了一份百度教程里面可以看看能不能用,<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjingyan.baidu.com%2Farticle%2F851fbc3772b1f33e1f15ab8c.html" target="_blank" rel="nofollow noopener noreferrer" title="https://jingyan.baidu.com/article/851fbc3772b1f33e1f15ab8c.html" ref="nofollow noopener noreferrer">mac如何远程连接windows</a>，教程里用到的软件<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmac.softpedia.com%2Fget%2FUtilities%2FMicrosoft-Remote-Desktop-Connection.shtml" target="_blank" rel="nofollow noopener noreferrer" title="https://mac.softpedia.com/get/Utilities/Microsoft-Remote-Desktop-Connection.shtml" ref="nofollow noopener noreferrer">官网地址</a>，或者用我下好上传到蓝奏云的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwwr.lanzoui.com%2FimMd5slcqbi" target="_blank" rel="nofollow noopener noreferrer" title="https://wwr.lanzoui.com/imMd5slcqbi" ref="nofollow noopener noreferrer">文件</a></p>
</blockquote>
<p>Win+r快捷键打开运行，输入mstsc 按下回车，之后这里会让你输入你服务器的公网ip地址
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/557a480048484415af07f9161d3dd778~tplv-k3u1fbpfcp-watermark.image" alt="ip地址.png" loading="lazy" referrerpolicy="no-referrer">
之后还有你服务器的用户名和密码，默认的用户名是Administrator，密码是你购买时设置的。链接时如果出现证书提醒不用管它，直接确定就行
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98258b3215b84b79b28a689f116caea5~tplv-k3u1fbpfcp-watermark.image" alt="链接1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/284a1d1685e24b3790c95421e1d5d2da~tplv-k3u1fbpfcp-watermark.image" alt="链接2.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c0718ca1a4e4446bb15e3a62358d64b~tplv-k3u1fbpfcp-watermark.image" alt="证书认证.png" loading="lazy" referrerpolicy="no-referrer">
如果出现连接失败说明你阿里/腾讯云的安全组没有设置80端口的访问，设置下就行，具体位置如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/351a7ce856d4427cb0c3a0f33397d0a5~tplv-k3u1fbpfcp-watermark.image" alt="链接失败.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91a93d2997fb45a189a649dc9966526e~tplv-k3u1fbpfcp-watermark.image" alt="安全组.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6b6e1f3c55149229ce5450830459fc4~tplv-k3u1fbpfcp-watermark.image" alt="设置安全组.png" loading="lazy" referrerpolicy="no-referrer">
这里为了方便我们就把之后要用到的端口都给它设置了，设置的规则是根据你后端服务器用到的端口决定的，比如说我这里用到了4000这个本地端口，那个我把他部署到服务器上的时候就要在安全组里添加4000这个端口开放</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c11190224a2147d6974bad6e00bc7237~tplv-k3u1fbpfcp-watermark.image" alt="服务器端口.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>之后没有意外我们就能看到服务器的操作界面了，初次进入的时候需要等它加载一会儿，就此我们的前期准备工作完成</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb08bb1c7afc45fba9c48c80cf90d3bb~tplv-k3u1fbpfcp-watermark.image" alt="远程服务器界面.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">安装所需软件</h1>
<h2 data-id="heading-5">1. 安装Node.js</h2>
<blockquote>
<p>之后我们先从node的安装开始，这是官网的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fen%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/en/" ref="nofollow noopener noreferrer">地址</a>，这是我提前下好的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwwr.lanzoui.com%2FiZ9t7slcqna" target="_blank" rel="nofollow noopener noreferrer" title="https://wwr.lanzoui.com/iZ9t7slcqna" ref="nofollow noopener noreferrer">文件</a>看需求使用就行，使用远程链接上传文件很简单，ctrl+c 选择你要上传的文件进行复制，然后到服务器的操作界面里 ctrl+v 进行粘贴就可以了  <del>没错这就是传说中的面向cv编程</del></p>
</blockquote>
<p>之后一路Next即可，完成后我们来检查下是否安装成功了，win+r 输入cmd进入命令行窗口（这里注意要最大化远程桌面链接，不然你操作的是本机），或者点击搜索菜单，输入cmd并按下回车键</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac3b57934f9e41b0a0a2c507bf8a55a6~tplv-k3u1fbpfcp-watermark.image" alt="搜索菜单进入cmd.png" loading="lazy" referrerpolicy="no-referrer">
依次输入</p>
<pre><code class="hljs language-js copyable" lang="js">node -v
npm -v 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果出现这样的问题不要慌
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ddf6e155c574914bd10f4e79b2f124b~tplv-k3u1fbpfcp-watermark.image" alt="npm没有.png" loading="lazy" referrerpolicy="no-referrer">
进入C:\Program Files\nodejs里，在点击npm.cmd在里面再试一次
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8ad3b77c77040d3a1e3e8863a0e40ab~tplv-k3u1fbpfcp-watermark.image" alt="npm成功.png" loading="lazy" referrerpolicy="no-referrer">
就此node安装完成</p>
<h2 data-id="heading-6">2.数据库安装并配置</h2>
<h3 data-id="heading-7">安装MongoDB</h3>
<blockquote>
<p>MongoDB官网下载<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.mongodb.com%2Ftry%2Fdownload%2Fcommunity" target="_blank" rel="nofollow noopener noreferrer" title="https://www.mongodb.com/try/download/community" ref="nofollow noopener noreferrer">地址</a>，嫌慢可以用我下载好的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwwr.lanzoui.com%2FiNdQ2slcovg" target="_blank" rel="nofollow noopener noreferrer" title="https://wwr.lanzoui.com/iNdQ2slcovg" ref="nofollow noopener noreferrer">密码1111</a>，但我这个版本是3.2.4，因为怕和当时写的版本不一样导致冲突</p>
<p>下载好之后和node一样Next即可，然后选择complete让它完整安装，接着一路Next，就此完成mongodb的安装</p>
</blockquote>
<h3 data-id="heading-8">配置MongoDB</h3>
<p><em>这样的好处配置一次以后都不需要用命令来启动了，更加方便</em></p>
<h4 data-id="heading-9">1.配置环境变量</h4>
<p>安装完成后我们来添加mongodb的环境变量，将MongoDB的bin目录添加到path下，首先我们在远程桌面上点击开始菜单，接着点击控制面板——系统与安全———系统——高级系统设置——环境变量——path——编辑——新建，输入<code>C:\Program Files\MongoDB\Server\3.2\bin</code> 确定即可。这一步的目的是为了在任何地方打开cmd窗口都可以使mongodb的命令。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3823b1a4147547d0909f15b9dca31a80~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fee9e753e46e4d2586ba46addc701b99~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90611755ee9a4dd09cfbb65988ca7dec~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/258858c6ac604bc6b142aa2900c42b14~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/223c8d80ed634c6aa087e94a83d03348~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/880d8ec4aea443c1adbca03a53e442de~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5303fa93843462ab34d4c01c8d9fd72~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">2.将MongoDB设置为windows系统服务</h4>
<p>这一步的目的是为了省去每次启动都需要输入数据路径</p>
<p>首先在c盘根目录创建如下文件夹:</p>
<pre><code class="hljs language-js copyable" lang="js">C:\data\log
<span class="hljs-attr">C</span>:\data\db
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ad8ef167e5248c98d9d720b87ca64c6~tplv-k3u1fbpfcp-watermark.image" alt="创建db文件.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>之后在MongoDB的bin目录下创建一个名为mongod.config的文件
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88a24a60115f4e249a85ecd9b137bf0c~tplv-k3u1fbpfcp-watermark.image" alt="cfg.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">systemLog:
    destination: file
    <span class="hljs-attr">path</span>: c:\data\log\mongod.log
<span class="hljs-attr">storage</span>:
    dbPath: c:\data\db
<span class="hljs-attr">net</span>:
    port: <span class="hljs-number">27017</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/075a906e42074340b8492c94f066fa68~tplv-k3u1fbpfcp-watermark.image" alt="cfg设置.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>或者用我给你们准备好的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwwr.lanzoui.com%2Fipyk3slcqda" target="_blank" rel="nofollow noopener noreferrer" title="https://wwr.lanzoui.com/ipyk3slcqda" ref="nofollow noopener noreferrer">mongod.config</a>
，防止出错。</p>
<p>以管理员身份打开命令行窗口执行以下指令（打开命令行窗口在右键以管理员身份打开的才行，不然有可能提示你权限不够）</p>
<pre><code class="hljs language-js copyable" lang="js">sc.exe create MongoDB binPath= <span class="hljs-string">"\"C:\Program Files\MongoDB\Server\3.2\bin\mongod.exe\" --service --config=\"C:\Program Files\MongoDB\Server\3.2\mongod.cfg\""</span> DisplayName= <span class="hljs-string">"MongoDB"</span> start= <span class="hljs-string">"auto"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c3c5108281047bfae8ee5df927e6cc5~tplv-k3u1fbpfcp-watermark.image" alt="管理员命令行.png" loading="lazy" referrerpolicy="no-referrer">
这样子就说明你成功创建了一个服务项
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9489feda1f56426fa89dcd10aeb44b2a~tplv-k3u1fbpfcp-watermark.image" alt="管理员命令行成功.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着我们打开系统服务器，启动名为MongoDB的服务</p>
<p>右击任务栏打开任务管理器，这里有一个服务，点进去按下m键，找到MongoDB，右键启动即可。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9ca3d173aae4ae492385a51c4f83238~tplv-k3u1fbpfcp-watermark.image" alt="启动服务1.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d343a0be5104e68985b323e8629cc46~tplv-k3u1fbpfcp-watermark.image" alt="启动服务2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/383bacb17de84025b8f07768969fb9c6~tplv-k3u1fbpfcp-watermark.image" alt="启动服务3.png" loading="lazy" referrerpolicy="no-referrer">
如果无法启动服务，在管理员的命令行窗口中输入如下指令</p>
<p>sc delete MongoDB</p>
<p>然后从第一步重新开始，以上我们就完成了MongoDB的安装与配置</p>
<h3 data-id="heading-11">安装Nginx并上传项目到服务器</h3>
<blockquote>
<p>Nginx官网下载<a href="https://link.juejin.cn/?target=http%3A%2F%2Fnginx.org%2Fen%2Fdownload.html" target="_blank" rel="nofollow noopener noreferrer" title="http://nginx.org/en/download.html" ref="nofollow noopener noreferrer">地址</a>，这是我提前下<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwwr.lanzoui.com%2FiMvhZslcqfc" target="_blank" rel="nofollow noopener noreferrer" title="https://wwr.lanzoui.com/iMvhZslcqfc" ref="nofollow noopener noreferrer">好的</a>，然后上传解压就完成了Nginx的安装（官网给的就是免安装版）</p>
</blockquote>
<p>之后把本地项目上传到服务器，要注意后端文件夹里的node_modules删除掉，不然上传会很慢, 把打包好的前端dist文件放到Nginx的html文件夹内，后端文件放到桌面，方便直接启动，或者随便你放在哪里，只要能找到</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29fd02ebd3ba444b92454553cc511609~tplv-k3u1fbpfcp-watermark.image" alt="位置1.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67e791cd5bb6400f8e11775dd8b022f8~tplv-k3u1fbpfcp-watermark.image" alt="位置2.png" loading="lazy" referrerpolicy="no-referrer">
然后我们把删除掉的依赖在重新下回来，在你的后端文件夹内点击路径输入cmd然后回车，这样的好处就是不用自己去找路径了，然后输入<code>npm install</code>，等它补全依赖后输入 <code>node server.js</code>启动后台服务器（这个命令主要看你启动页面叫什么名字，或者看package.json里的scripts命令）</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/981c358a75f54ea3a2f388964f2d50a1~tplv-k3u1fbpfcp-watermark.image" alt="scripts.png" loading="lazy" referrerpolicy="no-referrer">
之后没有报错一般就说明服务器启动成功了，具体的还要后台代码是怎么写的</p>
<h1 data-id="heading-12">Nginx配置</h1>
<h2 data-id="heading-13">配置Nginx路径</h2>
<p>终于到了我们的重头戏，如何来配置Nginx来使用户访问服务器时能看到页面，首先打开Nginx文件里面的conf文件夹，里面有一个nginx.conf文件，双击用记事本打开，找到location，把root的指定路径填写为 html/dist</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d97d7688b224e90a8f2028b44db3558~tplv-k3u1fbpfcp-watermark.image" alt="配置Nginx1.png" loading="lazy" referrerpolicy="no-referrer">
这里的路径就是你打包生成的前端文件夹路径，而index是用来指定网站的初始页，这里我的打包文件默认也是index.html所以就没更改配置。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a6ff5a3458442b7a681570945c288d3~tplv-k3u1fbpfcp-watermark.image" alt="默认样式.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">配置Nginx反向代理</h2>
<p>这一步非常重要，没有配置好你的所有请求服务器都不会响应的，这里的反向代理和你配置正向代理的逻辑是一样的，比方说我在devServer里配置了遇到/api开头的，就把他转到本地端口4000上，并且把路径里的/api删掉，那么我Nginx的配置也是一样的，只不过语法有些不同
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbbf397d3dca44c4ac5d05eea013fc6d~tplv-k3u1fbpfcp-watermark.image" alt="正向代理.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd7686758c934c48834b96973ba21d45~tplv-k3u1fbpfcp-watermark.image" alt="配置Nginx2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我的话是在nginx.conf里添加一个新的location配置，这个具体配置还是要看你前端代理是怎么写的，然后转换成Nginx的语法就行，详细语法我就不讲了，有需要的同学可以自行搜索，毕竟我对这个也是一知半解</p>
<pre><code class="hljs language-js copyable" lang="js">location /api &#123;     
         rewrite  <span class="hljs-string">"^/api/(.*)$"</span> /$<span class="hljs-number">1</span> <span class="hljs-keyword">break</span>;  
         proxy_pass http:<span class="hljs-comment">//你服务器的IP地址:你后台所用到的端口;</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置并保存好了就可以运行Nginx了，直接双击nginx.exe，然后查看任务管理器中是否有这个进程，如果没有说明你在配置nginx.conf有错误，可能是语法错误，或者是切换到全角状态下输入了逗号，建议删掉重新配置。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9f70de5e77f48a6abc6da0c81ad8f95~tplv-k3u1fbpfcp-watermark.image" alt="查看Nginx是否运行.png" loading="lazy" referrerpolicy="no-referrer">
以上这些如果都配置好了，那么恭喜你，你已经成功的把你的项目部署到服务器上了，输入你所绑定的域名或者你服务器的ip地址就可以查看了。当然，我强烈建议你把下面一步gzip压缩也配置下，因为真的很有用。</p>
<h1 data-id="heading-15">Nginx性能优化（gzip压缩）</h1>
<p>不说了直接让你们看看开启后和开启后的效果</p>
<h2 data-id="heading-16">效果对比</h2>
<p><em>这是没开启gzip压缩时：</em></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64e5820d16b64b238579268249dfffbe~tplv-k3u1fbpfcp-watermark.image" alt="未开启时1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b1dc3cd03634510b162bcf71ed16178~tplv-k3u1fbpfcp-watermark.image" alt="未开启时2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>这是开启后所花费的时间：</em></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6ca60869bef47988a5e2b4aa6121600~tplv-k3u1fbpfcp-watermark.image" alt="开启时1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaea1deae4c14be4b1d6564861a296c2~tplv-k3u1fbpfcp-watermark.image" alt="未启时2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没开前10到20秒，开了之后1到5秒左右，性能至少提高了4倍！虽然还是没有达到首屏1s的效果，但至少是达到了可以访问的程度。因此开启gzip压缩还是很有必要的。</p>
<h2 data-id="heading-17">开启gzip压缩</h2>
<p>开启gzip压缩首先我们要下载一个webpack的插件来帮助我们压缩js、css和我们需要压缩的文件，注意的是如果你使用的是vue-cli3脚手架搭建的项目下载要使用6.1.1，脚手架不支持最新版，在你的项目里打开cmd窗口，输入：</p>
<pre><code class="hljs language-js copyable" lang="js">npm install [compression-webpack-plugin]()@<span class="hljs-number">6.1</span><span class="hljs-number">.1</span> --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装成功之后在vue.config.js中进行配置如下信息 （对，这意味着你要重新打包一次）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> CompressionWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"compression-webpack-plugin"</span>);
<span class="hljs-keyword">const</span> productionGzipExtensions = [<span class="hljs-string">"js"</span>, <span class="hljs-string">"css"</span>];  <span class="hljs-comment">//你所需要压缩的文件</span>
<span class="hljs-built_in">module</span>.exports = &#123;
        <span class="hljs-attr">configureWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (process.env.NODE_ENV === <span class="hljs-string">"production"</span>) &#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-attr">plugins</span>: [
                        <span class="hljs-keyword">new</span> CompressionWebpackPlugin(&#123;                    
                            <span class="hljs-attr">algorithm</span>: <span class="hljs-string">"gzip"</span>,
                            <span class="hljs-attr">test</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">"\\.("</span> + productionGzipExtensions.join(<span class="hljs-string">"|"</span>) + <span class="hljs-string">")$"</span>),
                            <span class="hljs-attr">threshold</span>: <span class="hljs-number">10240</span>, <span class="hljs-comment">//对超过10k的数据进行压缩</span>
                            <span class="hljs-attr">minRatio</span>: <span class="hljs-number">0.6</span> <span class="hljs-comment">// 压缩比例，值为0 ~ 1</span>
                        &#125;)
                    ]
                &#125;;
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d976f4ddc5564df4aeb9e39d8ef55581~tplv-k3u1fbpfcp-watermark.image" alt="配置vueconfig.png" loading="lazy" referrerpolicy="no-referrer">
然后再Nginx服务器中配置，设置好了之后重启下Nginx就行</p>
<pre><code class="hljs language-js copyable" lang="js"> gzip on;
  # 检查是否存在请求静态文件的gz结尾的文件，如果有则直接返回该gz文件内容，不存在则先压缩再返回
  gzip_static on;
  # 设置允许压缩的页面最小字节数，页面字节数从header头中的Content-Length中进行获取。
  # 默认值是<span class="hljs-number">0</span>，不管页面多大都压缩。
  # 建议设置成大于10k的字节数，配合compression-webpack-plugin
  gzip_min_length 10k;
  # 对特定的MIME类型生效,其中text/html被系统强制启用
  gzip_types text/javascript application/javascript text/css application/json;
  # Nginx作为反向代理的时候启用，开启或者关闭后端服务器返回的结果
  # 匹配的前提是后端服务器必须要返回包含‘Via’的 header头
  # off(关闭所有代理结果的数据的压缩)
  # expired(启用压缩,如果header头中包括‘Expires’头信息)
  # no-cache(启用压缩,header头中包含Cache-Control:no-cache)
  # no-store(启用压缩,header头中包含‘Cache-Control:no-store’)
  # private(启用压缩,header头中包含‘Cache-Control:private’)
  # no_last_modefied(启用压缩,header头中不包含‘Last-Modified’)
  # no_etag(启用压缩,如果header头中不包含‘Etag’头信息)
  # auth(启用压缩,如果header头中包含‘Authorization’头信息)
  # any - 无条件启用压缩
  gzip_proxied any;
  # 请求加个 vary头，给代理服务器用的，有的浏览器支持压缩，有的不支持，所以避免浪费不支持的也压缩
  gzip_vary on;
  # 同 compression-webpack-plugin 插件一样，gzip压缩比（<span class="hljs-number">1</span>~<span class="hljs-number">9</span>），
  # 越小压缩效果越差，但是越大处理越慢，一般取中间值
  gzip_comp_level <span class="hljs-number">6</span>;
  # 获取多少内存用于缓存压缩结果，‘<span class="hljs-number">16</span>  8k’表示以8k*<span class="hljs-number">16</span> 为单位获得。
  # PS: 如果没有.gz文件，是需要Nginx实时压缩的
  gzip_buffers <span class="hljs-number">16</span> 8k;
  # 注：<span class="hljs-number">99.99</span>%的浏览器基本上都支持gzip解压了，所以可以不用设这个值,保持系统默认即可。
  gzip_http_version <span class="hljs-number">1.1</span>; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>注意这里的配置我是都是照搬沉末_大佬的 <a href="https://juejin.cn/post/6844904149633466376" target="_blank" title="https://juejin.cn/post/6844904149633466376">vue项目部署的最佳实践</a>中的服务器配置gzip压缩 ，具体的内容大家可以点进去看看，里面提供了很多优化方案,我也是在这里才学到要用gzip压缩来提高性能的。</em></p>
<h1 data-id="heading-18">总结</h1>
<p>以上这些步骤都完成了我们也就终于把vue项目部署到服务器了，下面进行总结：</p>
<p><em>1. 部署成功后，如果页面显示不出来，在排除代码写错的情况下，优先检查云服务的安全组有没有设置好，其次检查Nginx的反向代理有没有配置正确，Nginx的反向代理逻辑和正向代理一样，只不过语法有些不同。</em></p>
<p><em>2. 部署时记得配置Nginx的gzip压缩减少首屏打开时间，需要在本地下载compression-webpack-plugin 插件进行本地gzip压缩（服务器自动压缩消耗性能），用脚手架搭建的要下载6.1.1，最新版的脚手架不支持。</em></p>
<p><em>3. 记得站起来活动下身体，要是一口气从0部署到现在应该也用了不少时间了，活动下身体也是很有必要的。</em></p>
<hr>
<p>最后如果这个教程对你有帮助的话麻烦点个赞支持下，有什么问题欢迎在评论区留言，我看到了也会尽力去解答，本人也是个新手，所以有什么错误还请在评论区指正，最后感谢您的观看，我们下次再见，拜拜~</p></div>  
</div>
            