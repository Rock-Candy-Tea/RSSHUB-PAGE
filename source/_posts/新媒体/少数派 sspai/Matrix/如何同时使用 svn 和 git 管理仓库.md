
---
title: '如何同时使用 svn 和 git 管理仓库'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/editor/u_JamesHopbourn/16172821997345.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Thu, 01 Apr 2021 13:04:32 GMT
thumbnail: 'https://cdn.sspai.com/editor/u_JamesHopbourn/16172821997345.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-e1f0100a><div class="content wangEditor-txt minHeight" data-v-e1f0100a><p><strong>背景</strong>：为什么会有这么奇怪的一个需求？这是由于仓库内容来源不同导致的。如下图所示，我在 GitHub 上创建了一个图片仓库，原先设计是全部用于保存 OmniGraffle 的原稿。但是最近想把 iThoughtsX 的思维导图也上传上去，这时候就出现了一个问题：如果我把 iCloud 云盘上的思维导图都剪切到 diagram 目录下完全交由 git 管理，在 iPhone 上就无法直接通过文件 App 阅览这些照片。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_JamesHopbourn/16172821997345.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="图片仓库" data-original="https://cdn.sspai.com/editor/u_JamesHopbourn/16172821997345.png" referrerpolicy="no-referrer"><figcaption>图片仓库</figcaption></figure><p>那么有什么完美的方案既能把思维导图的文件夹上传到 GitHub 仓库又可以让它保留在 iCloud 云盘上吗？有，下面就来介绍使用 svn 和 git 协作实现这个功能。</p><h2>整体思路</h2><ol><li>剪切思维导图剪切到 git 文件夹</li><li>上传思维导图到 GitHub 仓库</li><li>svn checkout 到 iCloud 云盘</li><li>使用 svn 管理更新思维导图文件夹</li></ol><h2>配置 svn</h2><p>svn 的代理需要单独使用配置文件进行配置，具体方法如下：</p><pre class="language-text"><code>➜ vim ~/.subversion/servers
[global]
http-proxy-host = 127.0.0.1
http-proxy-port = 你的代理软件端口号
http-proxy-compression = no

:wq
</code></pre><h2>剪切思维导图剪切到 git 文件夹</h2><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_JamesHopbourn/16172821999187.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="截屏2021-04-01 下午8.14.29" data-original="https://cdn.sspai.com/editor/u_JamesHopbourn/16172821999187.png" referrerpolicy="no-referrer"></figure><h2>上传思维导图到 GitHub 仓库</h2><p><code>gaa gcsm gp</code> 行云流水地打完三条命令，上传完成</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_JamesHopbourn/16172821999210.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://cdn.sspai.com/editor/u_JamesHopbourn/16172821999210.jpg" referrerpolicy="no-referrer"></figure><h2>svn checkout 到 iCloud 云盘</h2><p>在终端里切换到 iThoughtsX iCloud 云盘目录，查询远程仓库目录</p><pre class="language-text"><code> → svn ls  https://github.com/JamesHopbourn/diagram/trunk
......
svg/
少数派/
桌面电源布置/
......
</code></pre><p>桌面电源布置就是需要 checkout 的子目录，将其 checkout 出来</p><pre class="language-text"><code>➜ svn checkout https://github.com/JamesHopbourn/diagram/trunk/桌面电源布置
A    桌面电源布置/LED 灯条.itmz
A    桌面电源布置/LED 灯条.png
A    桌面电源布置/OPSO 智能插座.itmz
A    桌面电源布置/OPSO 智能插座.png
A    桌面电源布置/公牛魔方插座.png
A    桌面电源布置/墙面插座.itmz
A    桌面电源布置/墙面插座.png
A    桌面电源布置/整体概览图.itmz
A    桌面电源布置/网络布局.itmz
A    桌面电源布置/网络布局.png
Checked out revision 106.
</code></pre><h2>使用 svn 管理更新思维导图文件夹</h2><p>如果思维导图内容发生改变，同样需要在 iCloud iThoughtsX 目录下使用 svn 更新</p><pre class="language-text"><code>➜ svn status
M       墙面插座.itmz

➜ svn add *
这条命令执行之后的报错都不需要理会

➜ svn commit -m "墙面插座"
Sending        墙面插座.itmz
Transmitting file data .done
Committing transaction...
Committed revision 107.
</code></pre><h2>其他：文件夹快速跳转</h2><p>因为文件夹是使用中文命名，所以 autojump 插件还需要切换到中文输入法才能快速跳转，这样非常地不方便。可以使用 wd 插件解决这个问题，编辑 zshrc 配置文件添加自带的 wd 插件</p><pre class="language-text"><code>➜ vim ~/.zshrc
plugins=(... wd)

:wq

➜ source ~/.zshrc
</code></pre><p>切换到桌面电源布置的 iCloud 目录下，使用 <code>wd add 标签名</code> 对当前目录标记之后以后想要快速跳转到改目录只需要输入：<code>wd 标签名</code> 即可。</p><pre class="language-text"><code>➜ wd add pow
 * Warp point added

➜ wd list
wd list
 * All warp points:
   pow  ->  ~/Library/Mobile Documents/iCloud~com~toketaware~ios~ithoughts/Documents/桌面电源布置
</code></pre><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_JamesHopbourn/16172821999235.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://cdn.sspai.com/editor/u_JamesHopbourn/16172821999235.jpg" referrerpolicy="no-referrer"></figure><h2>其他：关于文件更新</h2><p>当 iCloud 云盘中的子目录更新之后，每次在需要对 git 管理的目录进行编辑操作之前都需要进行 <code>git pull</code> 同步子目录的内容，建议子目录的内容全部使用 svn 进行管理，其他目录仍旧使用 git 管理，避免造成混乱。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_JamesHopbourn/16172821999261.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://cdn.sspai.com/editor/u_JamesHopbourn/16172821999261.jpg" referrerpolicy="no-referrer"></figure><p> </p></div><!----></div><div style="border:1px solid transparent;" data-v-e1f0100a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-e1f0100a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>5</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>1</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-4937" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E5%A6%82%E4%BD%95%E5%90%8C%E6%97%B6%E4%BD%BF%E7%94%A8%20svn%20%E5%92%8C%20git%20%E7%AE%A1%E7%90%86%E4%BB%93%E5%BA%93%E3%80%91%E8%83%8C%E6%99%AF%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BC%9A%E6%9C%89%E8%BF%99%E4%B9%88%E5%A5%87%E6%80%AA%E7%9A%84%E4%B8%80%E4%B8%AA%E9%9C%80%E6%B1%82%EF%BC%9F%E8%BF%99%E6%98%AF%E7%94%B1%E4%BA%8E%E4%BB%93%E5%BA%93%E5%86%85%E5%AE%B9%E6%9D%A5%E6%BA%90%E4%B8%8D%E5%90%8C%E5%AF%BC%E8%87%B4%E7%9A%84%E3%80%82%E5%A6%82%E4%B8%8B%E5%9B%BE%E6%89%80%E7%A4%BA%EF%BC%8C%E6%88%91%E5%9C%A8GitHub%E4%B8%8A%E5%88%9B%E5%BB%BA%E4%BA%86%E4%B8%80%E4%B8%AA%E5%9B%BE%E7%89%87%E4%BB%93%E5%BA%93%EF%BC%8C%E5%8E%9F%E5%85%88%E8%AE%BE%E8%AE%A1%E6%98%AF%E5%85%A8%E9%83%A8%E7%94%A8%E4%BA%8E%E4%BF%9D%E5%AD%98%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=&appkey=3196502474#" target="_blank"><i class="icon icon-article_weibo right-16"></i></a><span><div role="tooltip" id="el-popover-5347" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><i class="icon icon-article_weixin right-16"></i></span><a href="https://twitter.com/share?text=%E3%80%90%E5%A6%82%E4%BD%95%E5%90%8C%E6%97%B6%E4%BD%BF%E7%94%A8%20svn%20%E5%92%8C%20git%20%E7%AE%A1%E7%90%86%E4%BB%93%E5%BA%93%E3%80%91%E8%83%8C%E6%99%AF%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BC%9A%E6%9C%89%E8%BF%99%E4%B9%88%E5%A5%87%E6%80%AA%E7%9A%84%E4%B8%80%E4%B8%AA%E9%9C%80%E6%B1%82%EF%BC%9F%E8%BF%99%E6%98%AF%E7%94%B1%E4%BA%8E%E4%BB%93%E5%BA%93%E5%86%85%E5%AE%B9%E6%9D%A5%E6%BA%90%E4%B8%8D%E5%90%8C%E5%AF%BC%E8%87%B4%E7%9A%84%E3%80%82%E5%A6%82%E4%B8%8B%E5%9B%BE%E6%89%80%E7%A4%BA%EF%BC%8C%E6%88%91%E5%9C%A8GitHub%E4%B8%8A%E5%88%9B%E5%BB%BA%E4%BA%86%E4%B8%80%E4%B8%AA%E5%9B%BE%E7%89%87%E4%BB%93%E5%BA%93%EF%BC%8C%E5%8E%9F%E5%85%88%E8%AE%BE%E8%AE%A1%E6%98%AF%E5%85%A8%E9%83%A8%E7%94%A8%E4%BA%8E%E4%BF%9D%E5%AD%98%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="icon icon-article_twitter right-16"></i></a></div></div><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            