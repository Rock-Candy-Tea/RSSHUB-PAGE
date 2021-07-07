
---
title: '我给我讲GIT，并成功把我得罪了'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/898256587bf1468d89eec3133e8797f5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 00:08:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/898256587bf1468d89eec3133e8797f5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<hr>
<h1 data-id="heading-0">工作中如何使用GIT开发项目？（看到最后更精彩）</h1>
<blockquote>
<p><strong>注意：如果你熟悉Linux操作系统，那么这篇文章阅读速度会加倍</strong></p>
</blockquote>
<blockquote>
<p><strong>另外：如果你熟悉SVN，那么Git只是一个更高级的版本管理工具而已</strong></p>
</blockquote>
<blockquote>
<p><strong>But：如果你不熟悉Linux，也不知道SVN，那么没关系，至少你使用过云盘来管理你日常的文件。</strong></p>
</blockquote>
<blockquote>
<p><strong>如果你连云盘都没用过。那么你还是早点回火星吧，地球很危险的。</strong></p>
</blockquote>
<hr>
<h2 data-id="heading-1">为啥需要版本管理？</h2>
<p><strong>假设:</strong></p>
<p>下周就要做年终工作汇报了，你打算今天把PPT做完。</p>
<p>反反复复用了一上午的时间，总算是完成了一半。</p>
<p>中午吃饭的时候，你依然在思考后半部分该怎么完成。</p>
<p>然后你突然间觉得，上午的方案有些问题，还需要再改一改下午5点20分.....</p>
<p>在你反复阅读自己的方案后， 仍然觉得，还是上午的方案更好</p>
<p><code>可这个时候麻烦来了</code> , 上午的方案早就被改的面目全非了</p>
<p>当时写的话术，使用的图片动画等等，都已经被你删除了</p>
<p>想用<code>Ctrl + Z</code>解决？ 可惜PPT最多只支持150次操作回退，默认设置好像只有80次</p>
<p>这个时候，是不是特别想来一瓶后悔药？</p>
<blockquote>
<p>朋友，是时候了解一下<strong>X度云盘会员</strong>了。
不要998！ 不要998！ ，只要96元，就可享受包年服务</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/898256587bf1468d89eec3133e8797f5~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210624161137535" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>好了，刚才是个玩笑</strong> , 但X度云盘真的有记录文件版本的功能</p>
<p><strong>因此，我们认为，一个好用的云盘软件，应该具备以下几个功能：</strong></p>
<ol>
<li>用户A和B之间能够方便的进行文件共享</li>
<li>用户A和B可以修改同一个文件，云盘能够及时解决冲突问题</li>
<li>用户A对文件的修改提交后会同步给用户B</li>
<li>所有用户对文件的每一次提交都会有记录保存，操作失误时，可以还原之前的版本</li>
</ol>
<p><strong>版本管理</strong> , 不正是因此而得名么？</p>
<hr>
<h2 data-id="heading-2">SVN的优势</h2>
<h3 data-id="heading-3">在使用git之前，你必须了解一下SVN</h3>
<p>说起来，SVN可是曾经风靡全球的版本管理工具</p>
<p>SVN软件的使用，确实非常简单</p>
<p>它有两个安装包</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2db0ff2993045968adf9394bb6c882c~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"> <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/903c4d80d946411ab430516e604cdb6b~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二个安装包是服务器端，也就是说，你可以通过安装这个服务器端的软件，很轻易的在公司内部搭建一个SVN服务器</p>
<p>这样大家就可以在公司内网进行文件或是 代码的共享了</p>
<p>程序员在写代码时，经常需要协同开发（多个人维护一个项目）</p>
<p>SVN带来的方便，自然不言而喻，几乎所有的主流开发工具，都会配有SVN的插件</p>
<p>SVN的具体用法，这里不再详细描述。请读者自行百度</p>
<hr>
<h2 data-id="heading-4">有了SVN，为什么会出现Git？</h2>
<p>git这个软件的作者，是大名鼎鼎的Linus(Linux系统内核的发明人，编程界神话级的程序员)</p>
<p>不得不说，git这个软件，在易用性上，跟SVN差了不是一个数量级</p>
<p>但毕竟是专门给程序员用的，谁还考虑用户体验？？</p>
<p>由于linus严重的个人兴趣倾向，他非常不喜欢文件集中式的管理</p>
<p>于是git软件打一开始就是分布式的</p>
<p><strong>简单的说：</strong><code>就是任何人都可以向任何人的电脑上提交代码，任何人也可以从任何人的电脑上下载代码，任何人都可以被看作服务器端</code></p>
<p>再加上linus这种崇尚命令行主导一切的思维，git这个软件，打一开始就没有图形界面 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2180e681971473f9e9c40c9f5b608ff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以使用git的时候，特别有种当黑客的感觉，有木有？ <img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1d68abdc4764723a93305a705a6b86c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49842cf471184cbea079873ac6ca246c~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>尽管，git率先发明了分支的设计，但是，这糟糕的用户体验，并没能使它在全球范围迅速流行起来，直到 <code>github</code>的出现.....</p>
<hr>
<h2 data-id="heading-5">git和github是啥关系？</h2>
<p>github, 这个被大家戏称为全球最大的同性交友网站</p>
<p>它是如何崛起的呢？</p>
<p><strong>github网站提供了如下的服务：</strong></p>
<ol>
<li>你可以到这个网站注册一个账号</li>
<li>通过这个账号，你可以建立自己的仓库</li>
<li>使用你本地的git软件将你的代码提交到github服务器</li>
<li>如果你的同事也注册了github账号，那你可以一键转载分享给他</li>
<li>github上面的项目都是可以公开分享给其他人看的</li>
<li>我们不提供交友，只能提供代码分享及管理</li>
</ol>
<p><strong>你可以看到，github给我们带来了两个巨大的好处</strong></p>
<p><code>第一</code> github让我们似乎又回到了SVN的服务器时代，方便。</p>
<p><code>第二</code> 全世界所有知名的开源代码，都提交到了github上面并公开，这样一来，所有人都可以向这个开源项目提交自己的修改建议</p>
<p><strong>它带动了git软件的流行，这就是今天你不得不学git的原因</strong></p>
<hr>
<h2 data-id="heading-6">git到底咋用？</h2>
<p>首先，下个一个git软件 <code>https://git-scm.com/downloads</code>，并安装</p>
<p>在github上，建立一个空的<code>project</code></p>
<p>建好项目后，会看到项目的地址</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e61f3f47f26453797461eeb179eae66~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在，把项目的下载地址复制好了</p>
<p>找到一个合适的目录，例如E盘，在该目录下点击右键选择<code>git bash here</code></p>
<p>输入命令 <code>git clone https://github.com/ay8yt/teach.git</code></p>
<p>项目就会自动下载，这时E盘会多出一个<code>teach</code>目录</p>
<p><strong>好了，你现在可以打开你的开发工具，到这个目录下，编写你的代码了</strong></p>
<h3 data-id="heading-7"><strong>项目写完了，咋提交呢？</strong></h3>
<p>在命令行使用 <code>cd teach</code> ,进入teach目录</p>
<p>输入命令： <code>git add -A</code> , 将所有文件添加至缓存区，准备提交</p>
<p>然后，输入 <code>git commit -m '这里可以做一些描述，本次做了哪些修改'</code></p>
<p><strong>提交成功！</strong></p>
<hr>
<h2 data-id="heading-8">可能还需要一些准备工作</h2>
<p>如果你第一次使用git，提交时，系统会提示你先设置用户信息，那我们就设置一下：</p>
<p><code>git config --global user.email "随便邮箱"</code></p>
<p><code>git config --global user.name "随便用户名"</code></p>
<p>另外，由于项目通常是多人开发，你必须建立一个自己的分支</p>
<p><strong><code>我知道你一定想问</code>, 啥是分支？ 。。。。。这个说来有点话长了</strong></p>
<p>假设张三和李四要共同开发一个项目</p>
<p>虽然，他们俩负责的是不同的模块</p>
<p><code>但是</code>，张三的模块如果出了BUG或者错误，会导致李四的项目也无法启动</p>
<p>为了避免冲突和互相干扰</p>
<p>张三和李四在开发之前，都把项目进行了一次克隆拷贝</p>
<p>接下来，他们分别在自己克隆的副本上进行修改和提交</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b85b5d774a574e789941cd03e9b79efd~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来，张三就可以在自己的副本上进行修改和提交，和李四不会产生任何冲突</p>
<p>这就是 <strong><code>分支</code></strong> 的概念了</p>
<p>当然，张三的所有操作都是在自己的电脑本地进行的</p>
<p>如果本地电脑出了问题，本地记录的版本依然会全部丢失</p>
<p>所以，张三可以把自己本地的全部版本都推送到远程github服务器上</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/216b18c637004a669c2ad5cb5abcee52~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同样，李四也可以把自己本地的全部版本都推送到远程github服务器上</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/324f45ed5f014675976751d379ed361a~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong><code>这时，我们查看github远程，会发现变成了这样：</code></strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93ddc6cd39c94205a28212da25ef665b~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>这样一来，我们不仅把所有人的版本做了记录，而且整个开发过程中，张三和李四没有任何交集，也不会产生任何冲突</strong></p>
<p>怎么样？有没有感觉这个分支的发明特别的帅气？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3da8db3e3b748a290869c3305c47640~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>尽管SVN后来也迅速的推出了分支的功能，但它没有一个像github这么流行并统一的服务器。</p>
<p>github不仅提供了代码的托管，现在已经演变成了全球最大的代码分享社区</p>
<p>并在2018年6月份，以75亿美元的价格，卖给了微软</p>
<p>留给SVN的，只有一首<code>《凉凉》</code></p>
<hr>
<h2 data-id="heading-9">了解了基本原理，还是得学学具体如何使用</h2>
<p><strong>第一个我：</strong> 哎， 在工作中如何使用GIT开发项目？</p>
<p>第二个我： 你就不会说个hello，你好吗？或者，请问~之类的话吗？</p>
<p><strong>第一个我：</strong> 我发现你事儿挺多的！</p>
<p>第二个我： 请 ~ 把你的问题具体化好吗？</p>
<p><strong>第一个我：</strong> 那，这位（伪）大神，进入公司后怎么把gibhub上新建的项目down下来？</p>
<p>第二个我： 请不要称呼我大神，我只是比你强很多，虽然我也有那么一瞬间觉得自己确实是个大神</p>
<p><strong>第一个我：</strong> 是哪些瞬间让你误会了自己呢？</p>
<p>第二个我： 喝醉的瞬间，清醒过来就好了！ 好了回答你的问题，</p>
<p>如果你还有这样的疑问，显然你没有好好听课，因为上面已经讲过了。</p>
<p>算了，再说一次，下不为例。<code>git clone https://github.com/ay8yt/teach.git</code></p>
<p><strong>第一个我：</strong> 怎么在本地克隆一个副本，也就是创建一个分支？</p>
<p>第二个我： 使用branch命令。<code>git branch yintao01</code></p>
<p><strong>第一个我：</strong> 怎么进入这个分支呢？</p>
<p>第二个我： <code>git checkout yintao01</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb9cc710509248b2a0538fc45be93549~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，你现在应该能很明显的看到，你已经切换到了自己的分支，接下来的所有操作，都在这个副本上进行。</p>
<p><strong>第一个我：</strong> 写了一部分功能，想保存一个版本，怎么做？</p>
<p>第二个我： 第一步，<code>git add -A</code>, 所有文件提交到缓存区</p>
<p><strong>第一个我：</strong> 等等！ 我有些文件不想提交，例如 node_modules文件夹，怎么忽略它？</p>
<p>第二个我： 你要在项目的根目录下，创建一个叫做<code>.gitignore</code>的文件，内容如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b6a12f50b714402a5917d4eecb83713~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>第一个我：</strong> 可是我刚才已经把不需要的文件提交到缓存区了，怎么撤销？</p>
<p>第二个我： 很简单，重置一下，<code>git reset</code>,然后就可以提交了。</p>
<p><strong>第一个我：</strong> 等等！我想在正式提交之前，先查看一下，都有哪些文件提交到了缓存区？</p>
<p>第二个我： 你TM事儿真多！好吧，你可以使用<code>git status</code>命令查看，都做了哪些改动，以及所有文件的状态。</p>
<p><strong>第一个我：</strong> 好了，那正式提交是不是commit命令？</p>
<p>第二个我： 没错！使用<code>git commit -m '这里一定要把做了什么修改写清楚'</code></p>
<p><strong>第一个我：</strong> 每次提交一个版本都得写啊？ 那多麻烦？ 不写清楚行吗？</p>
<p>第二个我： 你可以试试，把你肠子悔青。</p>
<p><strong>第一个我：</strong> 刚提交完，就后悔了，感觉提交错了，想撤销这次提交，或覆盖这次提交，怎么做？</p>
<p>第二个我： 版本管理的好处，就是允许你后悔，首先你把错误的内容先修复好</p>
<p>然后再次add添加缓存，但这次提交时，注意使用<code>git commit --amend -m '刚才的提交就覆盖了'</code></p>
<p><strong>第一个我：</strong> 我想直接还原到上一个版本，怎么做？</p>
<p>第二个我： 使用<code>git reset head^</code></p>
<p><strong>第一个我：</strong> 我想直接还原到前两个版本，怎么做？</p>
<p>第二个我： 使用<code>git reset head^^</code></p>
<p><strong>第一个我：</strong> 那还原到前N个版本呢？</p>
<p>第二个我： <code>git reset head^^^^^^^^^^...</code></p>
<p><strong>第一个我：</strong> 你逗我呢？ 这么麻烦？</p>
<p>第二个我： 没开玩笑，就是这样，当然你可以指定版本号直接还原</p>
<p><code>git reset --hard 7e2ec0f51e9ae2e7cbc7c4deca18b77b242148d6</code></p>
<p><strong>第一个我：</strong> 版本号是个哈希值？ 这么长咋记得住？</p>
<p>第二个我： 你可以用<code>git log</code>查看所有版本</p>
<p><strong>第一个我：</strong> 我查了，可是每个版本都改了什么看不到啊，这aaaaa,bbbb,cccc,dddd都是什么鬼？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/836abafe3e3549a89d501ce5651fe5ab~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二个我： 这不都是你自己提交时写的注释么？ 不认真写注释的下场就是这样。活该。</p>
<p>另外，任何时候写代码，一定要想清楚了，测试通过了再提交，这是程序员的基本素质。</p>
<p>回滚操作虽然好用，但它不应该成为你的日常命令。如果一个程序员把各种回滚操作用的特别熟</p>
<p>通常表明他的代码水平不怎么样。</p>
<p><strong>第一个我：</strong> 我看你用的就挺熟的呀</p>
<p>第二个我： 滚~~~~~~</p>
<p><strong>第一个我：</strong> 如果本地我已经测试完并提交了，怎么推送到远程github上面？</p>
<p>第二个我： 为了方便做远程推送，通常我们会给远程仓库地址做个快捷方式。</p>
<p><code>git remote add miaodong https://git.oschina.net/ay8yt/test.git</code></p>
<p>这个<code>miaodong</code>就是快捷名称，接下来你提交时，就可以这样写：</p>
<p><code>git push -u miaodong yintao01</code> 这句话的意思就是把yintao01这个分支推送到miaodong这个仓库地址</p>
<p><code>-u</code> 的意思就是把yintao01设为默认分支</p>
<p>下次再推送，就可以直接写<code>git push miaodong</code></p>
<p><strong>第一个我：</strong> 我的模块已经开发完成，并测试通过，也推送到了github上，怎么把我的分支合并回主分支</p>
<p>第二个我： 在github上合并分支非常简单，找到Pull request，自己看说明去吧</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6064f17e48c645aba3cecdd99ef2b041~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>第一个我：</strong> 就这？我都会！</p>
<p>第二个我： 有种你别跑！！！</p>
<h3 data-id="heading-10">至此，我成功的把我得罪了。你成功的掌握了日常工作中git的基本使用</h3></div>  
</div>
            