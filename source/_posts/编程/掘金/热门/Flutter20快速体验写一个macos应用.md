
---
title: 'Flutter2.0快速体验写一个macos应用'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e892e25e13884e65a8feaf82d1e6ac53~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 11 Mar 2021 05:40:19 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e892e25e13884e65a8feaf82d1e6ac53~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.简介</h2>
<p>Flutter2.0将桌面端的开发支持加入到了<code>stable</code>分支中，这对于我一个移动开发小码农，产生了巨大的兴趣（/手动狗头）,于是开始了我的第一个<code>macos</code>应用的开发(<code>FTools</code>)，简单的说：开发桌面应用真的不要太简单了吧！下面是应用的截图，多图警告</p>
<h2 data-id="heading-1">2.屏幕截图</h2>
<ul>
<li>明亮模式：</li>
</ul>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e892e25e13884e65a8feaf82d1e6ac53~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bc2743e68ca435598ae8bf2655d4364~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8196fb28366f4868b7d23d7af9a1950a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42a74c694bfa43cdb6ed1de0bdbe1f88~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>深色模式：</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37ef0fe7f17d4015876c633ec8b57eae~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15f3ef6189424ccbbdc321619de08f2e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65d4c644b08a4e679044eace17af4bf6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7663d6eb71d4eb8959951fb26784806~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">3.MacOS应用开发</h2>
<p>看到上面，是不是也是像我一样，想自己也写一个macos的工具应用，不要着急，下面来教大家如何创建和生成MacOS应用</p>
<h3 data-id="heading-3">1.配置环境</h3>
<p>首先，确保你的FlutterSDK为2.0，我使用的是beta分支，也可以在stable分支下面查看到相同的版本号，至于Flutter的环境搭建，网上已经有很多相关的文章了，这里就直接省略了
<img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd07182625d648e0b6a4e032f8e3a6c6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">2.配置可开发MacOS应用</h3>
<p>运行下面命令即可</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">flutter config --enable-macos-deaktop
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">3.创建项目</h3>
<p>我一般使用的是<code>Android Studio</code>，所以，按照步骤：</p>
<p><code>Create New Flutter Project</code></p>
<p>->选择 <code>Flutter Application</code> -> 点击 <code>Next</code></p>
<p>->输入项目名<code>Project Name</code> -> 点击<code>Next</code></p>
<p>->输入包名<code>Package Name</code> -> 点击<code>Finish</code></p>
<p>-> 等待创建完毕（如果卡住了，可以试试设置代理，百度搜索：Flutter设置国内镜像）</p>
<p>-> 因为<code>Android Studio</code> 给我们创建的项目只能运行<code>Android</code>和<code>IOS</code>，我们需要再命令行下切换到项目的根目录下，运行<code>flutter create .</code>命令即可，完成后，可以看到macos文件夹</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/994c2cedca1946f9843f2b641a065e45~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">4.运行项目</h3>
<p>这里，我们需要给<code>Android Studio</code> 升级<code>Flutter</code>插件到最新的版本,然后选择macOS点击绿色三角按钮进行运行即可</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a157600071a64a54a674676723cab6a8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6602344721e445ebbc1c08c1be2b48de~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c233d623ab8048f7ad68c88730634143~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">4.FTools后续开发</h2>
<p>这个应用目前只耗时了两天，后续还会继续维护并免费上架到AppStore，如果你想这个应用有哪些功能(用户面向于开发者)，欢迎评论区留言给我，在能够实现并且时间充足的话会安排在开发计划当中。目前计划安排!</p>
<ol>
<li>Json To Table （JSON 转表格）</li>
<li>Json To Create SQLite (JSON 转Sqlite创建)</li>
<li>App Icon Make (应用图标制作)</li>
<li>...欢迎留言</li>
</ol>
<ul>
<li>
<p>下载地址：<a href="http://image.rhyme95.cn/FTools1.0.2-Installer.dmg" target="_blank" rel="nofollow noopener noreferrer">image.rhyme95.cn/FTools1.0.2…</a></p>
</li>
<li>
<p>后续开发交流加Q群：<code>129380453</code> 或 公号：<code>Dart客栈</code></p>
</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            