
---
title: '工作中如何使用GULP构建项目？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7841cdcfb90b43ce91f122410e58849e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 19:35:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7841cdcfb90b43ce91f122410e58849e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<hr>
<h1 data-id="heading-0">工作中如何使用GULP构建项目？</h1>
<blockquote>
<p>注意：这篇文章假定你具备较好的JS基础，可以独立完成小规模的项目</p>
<p>你甚至应该知道，常见的各种JS函数库和插件</p>
<p>同时，你应该具备一定的项目部署的常识，例如知道真正部署在服务器上的文件，跟开发的时候编写的文件是不同的
再同时，你必须要具备nodeJS的一些最基本知识。例如使用npm命令安装软件等，知道nodeJS如何加载模块</p>
<p>如果你用过sass或者less那就更好不过了。</p>
<p>最重要的，就是你需要知道常见的命令行操作，例如 <code>cd、cd..</code></p>
<p>假设你没听说过sass甚至不知道node为何物，JQuery不熟，甚至没用JS写过项目。</p>
<p>没关系，请点击浏览器右上角的叉号，整个世界都会恢复往日的美好</p>
</blockquote>
<hr>
<h1 data-id="heading-1">项目构建是什么？</h1>
<p>比如说吧，当项目部署上线时，你所有的JS文件，要不要进行压缩减小体积，以便于加载的时候速度更快？</p>
<p><strong>嗯，这个确实需要。</strong></p>
<p>图片要不要压缩处理，以获得更好的加载速度？</p>
<p><strong>嗯嗯，这个确实需要。</strong></p>
<p>你编写的JS代码使用了ES6语法，为了避免浏览器兼容，要不要转换成ES5？</p>
<p><strong>嗯嗯嗯，这个确实需要。</strong></p>
<p>你编写的scss源文件，要不要编译生成css？</p>
<p><strong>嗯嗯嗯嗯，这个确实需要。</strong></p>
<p>你的CSS是不是也要压缩？</p>
<p><strong>嗯嗯嗯嗯嗯，这个确实需要。</strong></p>
<p>开发过程中，你的页面跟后台服务器不在一台电脑上，你是否需要在本地搭建一个代理服务器以便于解决临时的跨域问题？</p>
<p><strong>嗯嗯嗯嗯嗯嗯，这个确实需要。</strong></p>
<h4 data-id="heading-2"><strong>以上这些类似的问题，Gulp可以很轻松把它们放在一起完成。</strong></h4>
<hr>
<h1 data-id="heading-3">Gulp是一个windows系统下的软件么？</h1>
<p><strong>很显然它不是。它是一个NodeJS编写的软件，需要我们先安装NodeJS的运行环境。</strong></p>
<p>这是nodeJS windows版网盘地址：</p>
<pre><code class="copyable">https://pan.baidu.com/s/1taPXX2Y01tVcqFUd3eATQQ 密码：bwf9
<span class="copy-code-btn">复制代码</span></code></pre>
<p>版本号： v8.9.3</p>
<hr>
<h1 data-id="heading-4">安装好NodeJS环境，接下来做什么？</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7841cdcfb90b43ce91f122410e58849e~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>安装Gulp v3.9.1</strong></p>
<p>我们需要使用node提供的一个叫做npm的命令</p>
<p><strong>需要我打开命令行吗？</strong></p>
<p>不然呢？ 难不成你想用QQ给NodeJS发个消息？</p>
<p><strong>打开后是不是像这样？</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22e14088fdc34c21993fec9744c26c09~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来进入你项目的根目录，然后输入命令 <code>npm install gulp</code></p>
<p><strong>安装时为什么要进入项目根目录？难道每个需要gulp的项目都要装一遍吗？</strong></p>
<p>没错，是这样的。因为每个项目使用gulp的功能不同，版本可能也不一样。这样每个项目的gulp相互独立。</p>
<p><code>注意 ！</code>在安装过程中，由于网速问题，经常导致安装失败。 多尝试几次就好</p>
<p>如果安装过程没有出现任何 <code>Error </code>提示，那就没有问题了。</p>
<p><strong>项目中多出了一个</strong> <strong><code>node_modules</code>文件夹，这就是我下载的gulp软件？</strong></p>
<p>是的，不要修改、移动或删除这个文件夹</p>
<hr>
<h1 data-id="heading-5">开始编写gulp任务文件</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c980aca19d984052ae90bf1acca9931f~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>这个任务文件是干什么的？？</strong></p>
<p>简单的说，就是写一个任务列表，告诉gulp具体要做什么。</p>
<p><strong>比如我现在要压缩我的js文件，该怎么编写gulp任务文件？</strong></p>
<p>现在，我们假定项目的目录结构是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a8637375b544faa91a9a60be8c0c5fd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>src </code>目录存放我们的源文件，<code>dist </code>目录存放我们压缩后的文件</p>
<p>接下来我们要在项目的根目录，创建一个 <code>gulpfile.js </code>文件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8f83a7a5ff549ac9353ca22c426bdcc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>gulpfile.js </code>文件内容如下：</p>
<p><code>如果你熟悉 nodeJS </code>那么下面的代码理解起来将会非常容易：</p>
<p><code>如果你不熟悉 nodeJS </code>那么下面的代码理解起来将会非常吃力：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6be99b9f6b284adaa58b5b95c27724a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，一切准备就绪，准备启动gulp执行压缩任务</p>
<p>我们回到命令行，仍然在项目的根目录下，输入命令 <code>gulp minifyJS</code></p>
<p><strong>我执行了这个命令，但是碰见了错误：</strong></p>
<p><code>Error: Cannot find module 'gulp-uglify'</code></p>
<p>因为找不到<code>'gulp-uglify'</code>这个模块。所以接下来我们安装它，输入命令<code>npm install gulp-uglify</code></p>
<p><strong>等等，不是已经安装过gulp了吗？ 为什么压缩文件的模块还要单独安装？</strong></p>
<p>gulp本身不具备压缩文件的功能。它的主要工作，是定义并执行任务。</p>
<p>而任务的具体内容是我们自己定的，就像gulpfile.js文件里写的那样。</p>
<p><strong>为什么gulp不把压缩js的功能集成进来，这样看来gulp其实没什么用了？</strong></p>
<p>恰恰相反， 你仔细想，如果Gulp把功能集成进来，那么它能提供的功能无论如何是有限的</p>
<p>那样做还会让软件体积变大，不需要的功能也必须强制安装。并没有好处。</p>
<p>正是因为gulp可以借助任何其它软件来执行任务。理论上来说，gulp的功能是无限的。</p>
<p><strong>好像有点道理。</strong></p>
<p>好了，接下来我们再次执行命令<code>gulp minifyJS</code></p>
<p><strong>执行了，但又碰见了错误：</strong></p>
<p><code>'gulp' 不是内部或外部命令，也不是可运行的程序或批处理文件。</code></p>
<p>这是因为我们之前把gulp安装在了项目里面。NodeJS运行环境并不能识别gulp命令</p>
<p><strong>那怎么办呢？</strong></p>
<p>再把gulp全局安装一次<code>npm install gulp -g</code></p>
<p>好了，我们来看看最后生成的效果</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8f38535dbf54ba1b26495d8b24205c8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>dist</code>目录中的文件全部都是压缩过的。</p>
<hr>
<h4 data-id="heading-6">目前，你已经掌握了Gulp的原理和最基本用法</h4>
<p>Gulp可以借助其它模块产生无穷无尽的用法，篇幅有限，今天暂时只能介绍到这里</p>
<p>如果大家有什么建议，可以给我留言</p>
<p>我相信，万事“开头难······</p>
<p>中间难，结尾难！”
大家共同加油！！！</p></div>  
</div>
            