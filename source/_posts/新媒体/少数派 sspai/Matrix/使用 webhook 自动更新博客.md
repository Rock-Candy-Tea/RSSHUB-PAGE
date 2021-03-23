
---
title: '使用 webhook 自动更新博客'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2021/03/21/f46ea858a7914d702d36a9586ea858d8.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Sun, 21 Mar 2021 04:18:46 GMT
thumbnail: 'https://cdn.sspai.com/2021/03/21/f46ea858a7914d702d36a9586ea858d8.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-7b50faf7><div class="content wangEditor-txt minHeight" data-v-7b50faf7><p>因为之前实在受不了 <code>Coding Page</code> 的速度（现在的 Coding Page 服务已经变成新版，使用腾讯云提供的服务，应该还行，不过不太想折腾了），几年前腾讯云的 CDN 感觉也很不好用，所以将自己的博客挂在了自己的服务器上。但是每次在写完之后都需要到服务器上执行 <code>git pull</code>过于麻烦，所以使用了 GitHub 上面的开源项目 <a href="https://github.com/adnanh/webhook">webhook</a>，<strong>当然 webhook 的作用不仅仅是自动更新部署博客啊，啥都能干 O__O …</strong></p><h2>使用 webhook 自动更新博客</h2><p>对于 webhook 来说，可以自己写一个脚本来接受信息，思路很简单，运行一个 <code>HTTP Server</code>，监听服务器的某个端口，如果有消息传递过来，那么就运行事先写好的脚本，来完成 webhook 的功能即可。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/03/21/f46ea858a7914d702d36a9586ea858d8.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/03/21/f46ea858a7914d702d36a9586ea858d8.png" referrerpolicy="no-referrer"></figure><p>但是为了方便使用和维护，还是选择了开源的项目</p><h3>什么是 webhook？</h3><p>webhook 的目标只是做他应该做的事</p><ol><li>接受 request</li><li>解析 HTTP 首部，负载内容和请求变量</li><li>检测是否满足钩子的特定条件</li><li>通过命令行参数或环境变量将指定的参数传递给指定的命令</li></ol><p>其他所有的事情都是 <code>命令作者</code> 的责任</p><h3>如何使用</h3><p>我的博客是 hexo 构建，构建出来的结果都是静态文件，使用 Nginx 挂在服务器上的，以下的内容都需要在服务器上执行</p><h4>安装 webhook</h4><p>这里推荐三种安装方法,使用其中一种方法即可，<strong>github 下载速度可能很慢</strong>，推荐使用系统源安装的方式</p><p>法一：使用系统源的安装方式</p><p>如果是 Ubuntu 系统，可以直接使用下面的命令进行安装：</p><pre class="language-text"><code>$ sudo apt-get update
$ sudo apt-get install webhook
</code></pre><p>法二：使用 github 下载</p><p>webhook 的 <a href="https://github.com/adnanh/webhook/releases">release 链接</a>，找到对应的选项 <code>webhook-linux-amd64.tar.gz</code> 右键复制链接 ，当前写博客时的最新版本链接为 <a href="https://github.com/adnanh/webhook/releases/download/2.6.11/webhook-linux-amd64.tar.gz">https://github.com/adnanh/webhook/releases/download/2.6.11/webhook-linux-amd64.tar.gz</a></p><p>具体操作如下：</p><pre class="language-text"><code>// 下载对应的软件
$ wget https://github.com/adnanh/webhook/releases/download/2.6.11/webhook-linux-amd64.tar.gz
// 解压进入
$ tar -zxf tar -zxf webhook-linux-amd64.tar.gz && cd webhook-linux-amd64/
$ ./webhook
[webhook] 2020/02/23 22:44:43 couldn't load any hooks from file!
aborting webhook execution since the -verbose flag is set to false.
If, for some reason, you want webhook to start without the hooks, either use -verbose flag, or -nopanic
</code></pre><p>法三：Golang 环境下安装</p><p>首先安装 Golang 环境（这里略过），然后安装 webhook，&#123;% label info@这里注意需要已经设置了 GOPATH %&#125;</p><pre class="language-text"><code>// 安装对应的工具
$ go get github.com/adnanh/webhook
// 安装完成之后可以在 $GOPATH/bin 下找到对应的执行文件
$ echo $GOPATH
/root/go
$ ls /root/go/bin
webhook
// 将路径写入到 shell 可以直接执行
$ vi ~/.bash_profile
// 在文件最后一行加入对应内容
export PATH="/root/go/bin:$PATH"
// 更新文件使其生效
$ source ~/.bash_profile
// 测试命令是否已经成功安装，得到输出说明安装完成
$ webhook
[webhook] 2020/02/23 22:44:43 couldn't load any hooks from file!
aborting webhook execution since the -verbose flag is set to false.
If, for some reason, you want webhook to start without the hooks, either use -verbose flag, or -nopanic
</code></pre><h4>配置 webhook</h4><p>下一步是定义您希望 <a href="https://github.com/adnanh/webhook">webhook</a> 提供的一些钩子，新建一个 <code>hook.json</code> 文件<br>该文件将包含 webhook 将提供的一系列钩子。检查 <a href="https://github.com/adnanh/webhook/blob/master/docs/Hook-Definition.md">Hook 定义页面</a> 以查看钩子可以包含的属性的详细描述以及如何使用它们。</p><h4>定义和部署</h4><p>下面的内容在 <code>~/notes-hooks</code> 文件夹下执行<br>让我们定义一个名为 <code>redeploy-webhook</code> 的简单钩子，新建一个 <code>redeploy.sh</code> 文件，确保你的 bash 脚本在顶部有 <code>#!/bin/sh</code></p><pre class="language-bash"><code>#!/bin/sh
git pull
</code></pre><p>写完之后注意需要给文件增加执行权限<br><code>$ chmod a+x redeploy.sh</code><br>然后新建一个 <code>hooks.json</code> 文件，看代码就可以知道意思了</p><pre class="language-javascript"><code>[
  &#123;
    "id": "redeploy-blog",
    "execute-command": "/home/ubuntu/notes-hooks/redeploy.sh",
    "command-working-directory": "/home/ubuntu/blog.cugxuan.cn"
  &#125;
]
</code></pre><p>这个 <code>hooks.json</code> 文件中各项的作用一看便知，&#123;% label info@注意 id 和监听的 URL 对应 %&#125;，webhook 默认监听的端口是 9000，根据上面写的可知监听的 URL 为 <code>http://yoursite.com:9000/hooks/redeploy-blog</code>，接下来执行命令部署即可</p><pre class="language-zsh"><code># 前台运行的方法，可以方便测试
$ ./webhook -hooks hooks.json -verbose
# 守护进程简单运行，这样就可以部署了
$ nohup ./webhook -hooks hooks.json -verbose &

</code></pre><p>然后将 <code>http://yoursite.com:9000/hooks/redeploy-blog</code> 填到你的 GitHub 网站对应项目页面 <code>Settings → Webhooks</code> 中即可</p><h3>测试</h3><p>写好博客然后 push，GitHub 收到你的更新之后就会触发 webhook 发送到服务器的监听位置，然后服务器完成更新部署<br>同时你可以在 GitHub 的 webhook 页面中看到发送的情况，还可以点击 Redeliver 重新测试</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/03/21/e1b415172fbcb78b3ea3ae807fc8c993.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/03/21/e1b415172fbcb78b3ea3ae807fc8c993.png" referrerpolicy="no-referrer"></figure><p> </p></div><!----></div><div style="border:1px solid transparent;" data-v-7b50faf7></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-7b50faf7><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>1</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>0</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-2165" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E4%BD%BF%E7%94%A8%20webhook%20%E8%87%AA%E5%8A%A8%E6%9B%B4%E6%96%B0%E5%8D%9A%E5%AE%A2%E3%80%91%E5%9B%A0%E4%B8%BA%E5%AE%9E%E5%9C%A8%E5%8F%97%E4%B8%8D%E4%BA%86CodingPage%E7%9A%84%E9%80%9F%E5%BA%A6%EF%BC%8C%E8%85%BE%E8%AE%AF%E4%BA%91%E7%9A%84CDN%E6%84%9F%E8%A7%89%E4%B9%9F%E5%BE%88%E4%B8%8D%E5%A5%BD%E7%94%A8%EF%BC%8C%E5%B0%86%E8%87%AA%E5%B7%B1%E7%9A%84%E5%8D%9A%E5%AE%A2%E6%8C%82%E5%9C%A8%E4%BA%86%E8%87%AA%E5%B7%B1%E7%9A%84%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E3%80%82%E4%BD%86%E6%98%AF%E6%AF%8F%E6%AC%A1%E5%9C%A8%E5%86%99%E5%AE%8C%E4%B9%8B%E5%90%8E%E9%83%BD%E9%9C%80%E8%A6%81%E5%88%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2021%2F03%2F21%2Fa5f93706a623a53fc1c82724c2cbb008.png%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="icon icon-article_weibo right-16"></i></a><span><div role="tooltip" id="el-popover-2032" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><i class="icon icon-article_weixin right-16"></i></span><a href="https://twitter.com/share?text=%E3%80%90%E4%BD%BF%E7%94%A8%20webhook%20%E8%87%AA%E5%8A%A8%E6%9B%B4%E6%96%B0%E5%8D%9A%E5%AE%A2%E3%80%91%E5%9B%A0%E4%B8%BA%E5%AE%9E%E5%9C%A8%E5%8F%97%E4%B8%8D%E4%BA%86CodingPage%E7%9A%84%E9%80%9F%E5%BA%A6%EF%BC%8C%E8%85%BE%E8%AE%AF%E4%BA%91%E7%9A%84CDN%E6%84%9F%E8%A7%89%E4%B9%9F%E5%BE%88%E4%B8%8D%E5%A5%BD%E7%94%A8%EF%BC%8C%E5%B0%86%E8%87%AA%E5%B7%B1%E7%9A%84%E5%8D%9A%E5%AE%A2%E6%8C%82%E5%9C%A8%E4%BA%86%E8%87%AA%E5%B7%B1%E7%9A%84%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E3%80%82%E4%BD%86%E6%98%AF%E6%AF%8F%E6%AC%A1%E5%9C%A8%E5%86%99%E5%AE%8C%E4%B9%8B%E5%90%8E%E9%83%BD%E9%9C%80%E8%A6%81%E5%88%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="icon icon-article_twitter right-16"></i></a></div></div><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            