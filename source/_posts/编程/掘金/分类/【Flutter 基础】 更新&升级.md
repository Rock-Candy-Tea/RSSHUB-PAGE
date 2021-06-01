
---
title: '【Flutter 基础】 更新&升级'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd5fb314ce29428db74f963c0e615971~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 31 May 2021 19:11:27 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd5fb314ce29428db74f963c0e615971~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第1天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><em>注：本文从个人公众号（岛前屿端）中迁移重新发布</em></p>
<blockquote>
<p>Flutter 是谷歌的移动 UI 框架，可以快速在 iOS 和 Android 上构建高质量的原生用户界面。 Flutter 可以与现有的代码一起工作。</p>
</blockquote>
<p>这里是直接从 <strong>Flutter github</strong> 上克隆的代码，所以操作会涉及到 <strong>git</strong>。因为尝试过直接安装 Flutter SDK 但是会有其他问题继而放弃。</p>
<h2 data-id="heading-0">更新&升级</h2>
<p><strong>Flutter</strong> SDK 的更新升级命令是 <strong>flutter upgrade</strong></p>
<pre><code class="hljs language-shell copyable" lang="shell">flutter upgrade
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当你想跃跃欲试的时候，请稍等一下，不要着急直接输入，<em>不然就会 Error 伺候……</em></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd5fb314ce29428db74f963c0e615971~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（flutter upgrade - error）</em></p>
<p>还记得上一篇中说到：<a href="https://juejin.cn/post/6963833618666340383#heading-4" target="_blank">添加阿里云（aliyun）提供的 maven 仓库镜像</a></p>
<p>对，没错！我们先要将这些镜像内容进行剔除，还原代码原来的亚子……</p>













<table><thead><tr><th align="center">还原前</th><th align="center">还原后</th></tr></thead><tbody><tr><td align="center"><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/962b8b42e65040218e6acc5fa8b96d38~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></td><td align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c083cbc956c94ae99daa05b331fec429~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></td></tr></tbody></table>
<p><em><strong>一定要记得噢，不要有前后空行或者空格，严格一致噢！！不然还是会 Error 伺候的。当然，你如果熟悉 git 操作的话，那么就可以使用 stash 来处理这个问题了。</strong></em></p>
<p>还原好后就可以在 <strong>Flutter SDK</strong> 文件夹下输入 <strong>git pull</strong> 等待文件传输完成。</p>
<pre><code class="hljs language-shell copyable" lang="shell">git pull
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文件传输完成后就可以执行 <code>flutter upgrade</code> 命令进行升级了，如果你的网络是正常的，那么稍微等一下就可以升级完成了。</p>
<h2 data-id="heading-1">切换分支</h2>
<p>升级完成后，我们可以根据 <strong>Flutter 中文网</strong> 的说明，建议我们追踪使用 stable 的分支，这是 Flutter 的稳定分支。</p>
<blockquote>
<p>建议跟踪 flutter 的 <strong>stable</strong> 分支，这是 <strong>Flutter 稳定分支</strong>。<br>
如果你需要查看最新的变化，你可以跟踪 <strong>master</strong> 分支，但注意这是开发分支，所以稳定性要低得多。<br>
要查看您当前使用的分支，请运行 <strong>flutter channel</strong> 查看。<br>
要切换分支，请使用 <strong>flutter channel beta</strong> 或 <strong>flutter channel master</strong></p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell">flutter channel
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b12a61021a134c4e8c3eefd9da2f9cc0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（flutter channel - master）</em></p>
<p>这表示当前的 <strong>flutter SKD</strong> 默认是 <strong>master</strong> 分支，<em>这是开发分支并不稳定</em>。</p>
<p>所以我们<strong>需要手动切换</strong>到 <strong>stable</strong> 的分支上。但是切换之前，我们需要做一个小小的改动。</p>
<p><strong>Flutter->bin->cache</strong> 删除文件夹内所有文件。</p>
<p>放心啦，不会出问题的，相信我没错的
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/669c44bdf28246bcb913d0794b0515fb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候我们就可以使用 <code>flutter channel stable</code> 进行分支切换了。</p>
<pre><code class="hljs language-shell copyable" lang="shell">flutter channel stable
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4906111c9b9e48a68a6525842510007f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（等待分支数据切换……）</em></p>
<p>完成后再次运行 <code>flutter channel</code> 命令就可以看到已经切换到 <strong>stable</strong> 分支了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/088cfc0c05fe4ca8bfa236dd7f057120~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（flutter channel - stable）</em></p>
<h2 data-id="heading-2">再次添加仓库镜像</h2>
<p><a href="https://juejin.cn/post/6963833618666340383#heading-4" target="_blank">添加阿里云（aliyun）提供的 maven 仓库镜像</a>再次添加上。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1a1be4b31e24181ac3f77363d5381d6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（替换仓库镜像）</em></p>
<p>添加完成后，我们就可以打开之前的 flutter 项目，打开虚拟机或者连接真机，然后 flutter run</p>
<pre><code class="hljs language-shell copyable" lang="shell">flutter run
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>注意：flutter SKD 和 flutter 项目不要弄混了，flutter SKD 是从 github clone 下来的，而 flutter 项目是由 flutter create 命令创建来的。</em></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7242b2fab5c747578a4ee732aed6f414~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>稍微等待一下……OK，依旧完美运行。</p>
<p>OK 恭喜你！你已经完成整个对 Flutter 的版本更新和升级了。</p>
<h2 data-id="heading-3">关于命令提示</h2>
<p>关于命令上的提示，我就简单说明一下：</p>
<ul>
<li>r - 重新载入代码运行</li>
<li>R - 重新运行（会重新编译）</li>
<li>o - 切换 Android / iOS 模式（真机（Android系统）不会显示这条信息，虚拟机的话会显示关于 o 的命令。但是 o 命令对真机（Android系统）依然有效</li>
<li>h - 更详细的帮助信息</li>
<li>d - 将应用和开发环境分离，设备上可以独立使用。</li>
<li>q - 退出，会将设备上的应用一同退出。</li>
</ul>
<h2 data-id="heading-4">最后</h2>
<p><strong>在未来有新版本发布的时候就你依然可以使用以上步骤进行更新和升级了</strong><br>
<em>（已经是 stable 分支的话切换分支的步骤可以免了）</em></p>
<p>当然，如果你在更新升级的时候碰到问题没法解决的话，可以给我留言，我会尽量帮助你解决问题。（前提是，你的操作步骤要记得，我才好复盘重现）</p>
<h2 data-id="heading-5">总结</h2>
<ul>
<li>多去尝试，但是要记录操作步骤</li>
</ul>
<h2 data-id="heading-6">参考</h2>
<ul>
<li><strong>【Flutter 中文网】<a href="https://flutterchina.club/" target="_blank" rel="nofollow noopener noreferrer">flutterchina.club</a></strong></li>
</ul></div>  
</div>
            