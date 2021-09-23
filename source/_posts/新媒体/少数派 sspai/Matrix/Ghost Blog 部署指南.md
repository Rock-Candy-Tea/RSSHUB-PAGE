
---
title: 'Ghost Blog 部署指南'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2021/09/17/article/47487b7bd1617cc59f0d6d4e7e217177?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Fri, 17 Sep 2021 05:36:52 GMT
thumbnail: 'https://cdn.sspai.com/2021/09/17/article/47487b7bd1617cc59f0d6d4e7e217177?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-6a669db8><div class="content wangEditor-txt minHeight" data-v-6a669db8><h3 style="margin-left:0px;"><strong>Matrix 首页推荐</strong></h3><p style="margin-left:0px;"><a href="https://sspai.com/matrix">Matrix</a> 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。</p><p style="margin-left:0px;">文章代表作者个人观点，少数派仅对标题和排版略作修改</p><hr><h2>为什么会选择 Ghost？</h2><p>折腾博客将近 6 年了，尝试过 WordPress、Typecho、Ghost、Hexo、Gridea 等不少的博客程序。这些程序各有优缺点，WordPress 的高度个性化与可玩性值得称赞，但也给站点优化带来了问题；基于 Node.js 的 Hexo 搭配上 GitHub Pages，降低了博客搭建的门槛，但渲染速度、npm、跨平台都是逃不过的问题。</p><p>从体验上来说，我更偏向自托管的静态博客，数据在自己的服务器上，一定程度上保证用户对内容的所有权。因为对 Git 平台的操作不熟悉，加上 访问速度不佳，我将博客从 Hexo 迁移到了 Gridea，但后者长时间停更，以及主题数量偏少，我开始寻找下一个适合的博客程序。</p><p>3 月 16 日，Ghost 发布 4.0 版本，与先前 1.0、2.0 版本不同，Ghost 4.0 版本中新增了后台面板、订阅支持，同时也继承先前版本优秀的设计。或许，可以试试？</p><h2>搭建前的准备</h2><h3>域名</h3><p>通过自己的服务器搭建博客，通常需要绑定域名，关于选购与注册方面，在这里不做过多阐述。注册好域名后，在域名解析设置中，将域名解析至服务器 IP。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/09/17/article/47487b7bd1617cc59f0d6d4e7e217177?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/09/17/article/47487b7bd1617cc59f0d6d4e7e217177" referrerpolicy="no-referrer"><figcaption>域名解析</figcaption></figure><h3>服务器</h3><p>由于 Ghost 是动态博客，因此需要准备一台服务器。官方文档中推荐使用 RAM ≥ 1G、运行在 Ubuntu 16.04 / 18.04 / 20.04 系统的服务器上。除了基于 Node.js 运行，Ghost 官方还提供<a href="https://ghost.org/docs/install/docker/" target="_blank">基于 Docker</a> 运行的 Ghost Blog。</p><h2>本机直接部署</h2><blockquote><p>系统：Ubuntu 21.04、Debian 11.0</p><p>Nginx：nginx/1.18.0</p><p>MySQL：8.0.26</p><p>Node.js：v14.17.6</p><p>Ghost：v4.9.4</p></blockquote><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/09/17/16c18e2fe55944df8cf83d45c4678f6e.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/09/17/16c18e2fe55944df8cf83d45c4678f6e.jpg" referrerpolicy="no-referrer"><figcaption>安装流程</figcaption></figure><h3>初步配置</h3><p>通过 SSH 或终端登入服务器，并切换至 root 用户，然后新增一个普通用户，用于安装 Ghost。</p><p>运行更新服务器中的软件。</p><pre class="language-shell"><code># 更新系统软件包
apt update && apt upgrade -y</code></pre><p>运行 adduser 命令添加新普通权限的 Linux 用户，根据提示输入用户密码与其它信息。</p><pre class="language-shell"><code># 新增普通用户，用户名需自行设定（除 ghost）
adduser 用户名</code></pre><p>为新增用户添加 sudo 权限，并将当前身份切换为该用户。</p><pre class="language-shell"><code># 赋予用户 sudo 权限
usermod -aG sudo 用户名

# 切换到普通用户
su - 用户名</code></pre><h3>安装网站环境</h3><p>Ghost 未限制网站环境的安装方式，你可以使用 Nginx 或 Apache 运行前端，下文以官方文档介绍的安装方式为主。如需使用 LAMP 环境包 / LNMP 环境包 / OneinStack / 面板，需留意在安装 Ghost 环节，跳过 ghost-cli 自动配置 Nginx 与 SSL 环节，并手动建立网站，将反向代理部分的配置写入网站配置文件中。</p><p>从 Ubuntu 仓库安装 Nginx 与 MySQL 数据库。</p><pre class="language-shell"><code># 从 Ubuntu 仓库中安装 Nginx 与 MySQL-Server
sudo apt install nginx mysql-server -y</code></pre><p>MySQL 安装完成后，需要重设数据库 root 用户密码。</p><pre class="language-shell"><code># 重置 MySQL root 密码
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '新密码';
quit;</code></pre><p>从 <a href="https://github.com/nodesource/distributions" target="_blank">NodeSource</a> 安装 Node.js。如果通过其它方式安装，需要留意 Node.js 版本 Ghost 只支持运行在 Node.js 12.x、14.x 两个大版本中。</p><pre class="language-shell"><code># 通过 NodeSource 安装指定版本的 Node.js
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash
sudo apt install nodejs -y

# 安装 Yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update && sudo apt install yarn -y

# 假如服务器位于大陆区域，需要借助 cnpm 镜像提高 npm 与 yarn 依赖的安装速度，否则 ghost install 时，无法下载依赖会导致安装失败
sudo npm install -g cnpm --registry=https://registry.npm.taobao.org
sudo yarn config set registry https://registry.npm.taobao.org/</code></pre><h3>安装 Ghost</h3><p>建立文件夹，配置好文件夹权限，下文以 <code>/var/www/ghost</code> 作为 Ghost 数据目录。</p><pre class="language-shell"><code># 新建 Ghost 数据目录文件夹
mkdir -p /var/www/ghost

# 设置文件夹权限
chown 用户名:用户名 -R /var/www/ghost
chmod 0775 -R /var/www/ghost

# 前往文件夹
cd /var/www/ghost</code></pre><p>安装 Ghost-CLI。</p><pre class="language-shell"><code># 未配置 cnpm 加速源
sudo npm install ghost-cli@latest -g

# 配置了 cnpm 加速源
sudo cnpm install ghost-cli@latest -g</code></pre><p>前往网站文件夹安装 Ghost。</p><pre class="language-shell"><code># 安装 Ghost
ghost install</code></pre><p>进入安装流程。</p><pre class="language-shell"><code># 进入 Ghost 安装流程

# 检查系统环境
✔ Checking system Node.js version - found v14.17.6
✔ Checking logged in user
✔ Checking current folder permissions

# 此处如系统版本非 Ghost 官方文档推荐的，会询问是否继续安装，这里选择 Yes
? Continue anyway? Yes
System stack check skipped

# 检查软件环境
ℹ Checking system compatibility [skipped]
✔ Checking for a MySQL installation
✔ Checking memory availability
✔ Checking free space
✔ Checking for latest Ghost version
✔ Setting up install directory

# 下载 Ghost 本体、npm 与 yarn 依赖
# 假如服务器位于大陆区域，需要借助 cnpm 镜像提高 npm 与 yarn 依赖的安装速度，否则 ghost install 时，无法下载依赖会导致安装失败
✔ Downloading and installing Ghost v4.14.0

# 进入网站域名、MySQL 数据库、系统服务设置
✔ Finishing install process

# 输入网站绑定域名
? Enter your blog URL: http://xavier.wang

# 输入 MySQL 数据库服务器地址、用户名、密码、数据库名称
? Enter your MySQL hostname: localhost
? Enter your MySQL username: root
? Enter your MySQL password: [hidden]
? Enter your Ghost database name: db_ghost
✔ Configuring Ghost
✔ Setting up instance
+ sudo chown -R ghost:ghost /var/www/ghost/content
✔ Setting up "ghost" system user

# 如先前使用 MySQL root 用户登录，此处可以让 ghost-cli 自动创建一个属于 Ghost 数据库的用户
? Do you wish to set up "ghost" mysql user? Yes
✔ Setting up "ghost" mysql user

# 如果本机先前已有其它网站或需要使用自定义的网站环境，需要跳过自动配置 Nginx 与 SSL 证书
? Do you wish to set up Nginx? Yes
+ sudo mv /tmp/xavier-wang/xavier.wang.conf /etc/nginx/sites-available/xavier.wang.conf
+ sudo ln -sf /etc/nginx/sites-available/xavier.wang.conf /etc/nginx/sites-enabled/xavier.wang.conf
+ sudo nginx -s reload
✔ Setting up Nginx
# 选择是否通过 acme.sh 自动配置 SSL 证书
? Do you wish to set up SSL? Yes
ℹ Setting up SSL [skipped]

# 将 Ghost 绑定到 Systemctl 上
? Do you wish to set up Systemd? Yes
+ sudo mv /tmp/xavier-wang/ghost_xavier-wang.service /lib/systemd/system/ghost_xavier-wang.service
+ sudo systemctl daemon-reload
✔ Setting up Systemd
+ sudo systemctl is-active ghost_xavier-wang

# 启动 Ghost
? Do you want to start Ghost? Yes
+ sudo systemctl start ghost_xavier-wang
+ sudo systemctl is-enabled ghost_xavier-wang
+ sudo systemctl enable ghost_xavier-wang --quiet
✔ Starting Ghost

Ghost uses direct mail by default. To set up an alternative email method read our docs at https://ghost.org/docs/config/#mail

------------------------------------------------------------------------------

# 当显示这条信息时，表示 Ghost 已完成安装流程
Ghost was installed successfully! To complete setup of your publication, visit: http://xavier.wang/ghost/</code></pre><p>在设置过程中，按照提示设置域名、数据库连接信息、SSL 证书、系统服务。使用「LAMP 环境包 / LNMP 环境包 / OneinStack / 面板」的用户需留意在安装 Ghost 环节，跳过 ghost-cli 自动配置 Nginx 与 SSL 环节，并手动建立网站，将反向代理部分的配置写入网站配置文件中。</p><pre class="language-shell"><code># Nginx 反向代理配置

location / &#123;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        proxy_pass http://127.0.0.1:2368;
    &#125;</code></pre><p>当提示 <code>Ghost was installed successfully</code> 时，表示 Ghost 安装成功，点击下方域名进入博客后台设置。</p><h2>站点配置</h2><h3>初始化网站</h3><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/09/17/article/c3001c60b0a2c4c404171def0c50b477?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/09/17/article/c3001c60b0a2c4c404171def0c50b477" referrerpolicy="no-referrer"><figcaption>Ghost 博客首页</figcaption></figure><p>在浏览器中输入域名，比如我绑定的是 xavier.wang，那么就输入 https://xavier.wang/ghost/ 进入 Ghost 后台，进入配置环节。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/09/17/article/81bf0c2ea438b975ba6c5572f978f1ae?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/09/17/article/81bf0c2ea438b975ba6c5572f978f1ae" referrerpolicy="no-referrer"><figcaption>Ghost 博客配置 - 第一步</figcaption></figure><p>设置网站信息、管理员用户名与密码。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/09/17/article/0be501b6fa02f9e59937a96e0a5db025?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/09/17/article/0be501b6fa02f9e59937a96e0a5db025" referrerpolicy="no-referrer"><figcaption>Ghost 博客配置 - 第二步</figcaption></figure><p>完成设置，进入博客后台。</p><h3>后台设置</h3><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/09/17/article/fe1e35c006a9708ed5e16a07f7cf656e?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/09/17/article/fe1e35c006a9708ed5e16a07f7cf656e" referrerpolicy="no-referrer"><figcaption>Ghost 博客后台面板</figcaption></figure><p>后台大致分为两个版块，左侧菜单栏与右侧面板。点击左下方的齿轮按钮，可以看到博客设置，如站点信息、主题、导航链接、用户、高级功能等。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/09/17/article/fcb632a547cfa5c49e8278c94117c997?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/09/17/article/fcb632a547cfa5c49e8278c94117c997" referrerpolicy="no-referrer"><figcaption>Ghost 博客后台设置</figcaption></figure><h2>关于 Ghost 的一些看法</h2><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/09/17/article/7e567bf920b0bdd9d8417f7f5fddb201?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/09/17/article/7e567bf920b0bdd9d8417f7f5fddb201" referrerpolicy="no-referrer"><figcaption>Ghost 后台面板</figcaption></figure><p>Ghost 4.0 版本中首次集成了原生的会员管理与订阅功能，通过连接第三方支付服务，可以向注册用户提供付费内容、邮件订阅服务。在博客后台的 Dashboard 上，直观展示了当前的文章收入、注册会员数量、付费会员比例、邮件打开率等数据。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/09/17/article/369d4d61122a41387ec736079ddc72aa?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/09/17/article/369d4d61122a41387ec736079ddc72aa" referrerpolicy="no-referrer"><figcaption>Ghost 博客文章编辑</figcaption></figure><p>Ghost 的编辑器原生支持实时渲染 Markdown 语法，并且还有与 Notion 编辑器类似的「Type '/' for commands」功能，可快捷插入多媒体内容，如图片、YouTube 视频、Twitter 推文等卡片。</p><p>在编辑器的文章发布设置中，可以直接设置文章摘录、分享样式、邮件订阅，这个功能点对于自媒体 / Newsletter 运营者十分友好，在发布文章的同时，可以完成社交媒体分享、邮件订阅发送、文章发布等动作，减少工作程序。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/09/17/article/ccdaf85b26e8ec38c7e35ca46dd1be3d?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/09/17/article/ccdaf85b26e8ec38c7e35ca46dd1be3d" referrerpolicy="no-referrer"><figcaption>Ghost 博客插件拓展（Integrations）</figcaption></figure><p>与 WordPress、Hexo 等博客平台相比，Ghost 会更注重写作与阅读，它在插件拓展、博客样式的个性化方面上会显得比较简陋，支持的插件（Integrations）会更多来自成熟的外部服务，以丰富读者阅读的内容。</p><p>但也有不足的地方，对于拓展博客自身的功能性上，更多要靠后期开发，比如文章搜索、云储存、图片压缩，对的，Ghost 没有默认搜索功能。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/09/17/article/36ef298b973e074c427e1d3c01064b01?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/09/17/article/36ef298b973e074c427e1d3c01064b01" referrerpolicy="no-referrer"><figcaption>Ghost 博客主题自定义</figcaption></figure><p>主题自定义方面，默认设置中只给到了站点 Logo、焦点颜色、Banner 底图的设置，更深层次的个性化修改，则需要修改主题的相关文件。GitHub、ThemeForest 上有一些比较好看的第三方主题，如 <a href="https://github.com/zutrinken/attila" target="_blank">Attila</a>、<a href="https://github.com/eddiesigner/liebling" target="_blank">Liebling</a>、<a href="https://github.com/ChrisW-B/london-grid" target="_blank">London-Grid</a>，官方的主题商城内提供了 24 款免费主题，付费主题价格较高，相对来说 Ghost 的主题数量仍然偏少。</p><p>Ghost 博客相对于 WordPress 而言会更加简约，同时优秀的设计风格也会让人耳目一新。但 Ghost 是否值得推荐呢？</p><p>如果是对平台运行追求稳定的自媒体、Newsletter 运营团队来说，Ghost 或许是一个不错的选择，文章编辑器、会员管理、第三方服务可圈可点，Ghost 也提供了官方的付费托管服务 —— <a href="https://ghost.org/pricing/" target="_blank">Ghost Pro</a>，让你专注于内容创作，以及加强与读者互动。</p><p>就我个人的需求来说，我认为不值得。一是 Ghost 的主题、插件拓展生态圈还未发展起来；其次，Ghost 数据导出仅支持 json 格式，相关的迁移工具如 <a href="https://www.npmjs.com/package/oghost" target="_blank">oghost</a>、<a href="https://github.com/jasonslyvia/hexo-migrator-ghost" target="_blank">hexo-migrator-ghost</a> 停更已久，迁移至 <a href="https://github.com/amayem/GhostJSON-to-WPXML" target="_blank">WordPress</a>、<a href="https://www.pgrs.net/2018/11/25/migrating-blog-from-ghost-to-jekyll/" target="_blank">Jekyll</a>、<a href="https://github.com/jbarone/ghostToHugo" target="_blank">Hugo</a> 的工具虽然有更新，但跨程序之间的搬运并不是一件轻松事。第三点，也是最头疼的一点，Node.js 和 npm 的报错，看到密密麻麻的报错我都不想处理了。</p><h2>相关阅读</h2><ul><li><a href="https://sspai.com/post/65602" target="_blank">WordPress 有力竞争者，高颜值全能平台：Ghost</a></li><li><a href="https://iiong.com/gost-blog-install-notes/" target="_blank">Ghost 安装笔记</a></li><li><a href="https://ghost.org/docs/install/ubuntu" target="_blank">How to install Ghost on Ubuntu</a></li><li><a href="https://sspai.com/post/47479" target="_blank">Ghost 博客数据自动备份和图片自动压缩</a></li><li><a href="https://github.com/JaxsonWang/Ghost-Theme" target="_blank">JaxsonWang / Ghost-Theme</a></li></ul><p style="margin-left:0px;">> 下载少数派 <a href="https://sspai.com/page/client">客户端 </a>、关注 <a href="https://sspai.com/s/J71e">少数派公众号 </a>，了解更妙的数字生活 🍃</p><p style="margin-left:0px;">> 想申请成为少数派作者？<a href="https://sspai.com/apply/writing" target="_blank">冲！</a></p></div><!----></div><div style="border:1px solid transparent;" data-v-6a669db8></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-6a669db8><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>27</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>28</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-6525" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90Ghost%20Blog%20%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97%E3%80%9121.09.10-GhostBlog%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BC%9A%E9%80%89%E6%8B%A9Ghost%EF%BC%9F%E6%8A%98%E8%85%BE%E5%8D%9A%E5%AE%A2%E5%B0%86%E8%BF%916%E5%B9%B4%E4%BA%86%EF%BC%8C%E5%B0%9D%E8%AF%95%E8%BF%87WordPress%E3%80%81Typecho%E3%80%81Ghost%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2021%2F09%2F17%2F50a198654b574c4969c79dc7aff96609.jpg%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-533" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90Ghost%20Blog%20%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97%E3%80%9121.09.10-GhostBlog%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BC%9A%E9%80%89%E6%8B%A9Ghost%EF%BC%9F%E6%8A%98%E8%85%BE%E5%8D%9A%E5%AE%A2%E5%B0%86%E8%BF%916%E5%B9%B4%E4%BA%86%EF%BC%8C%E5%B0%9D%E8%AF%95%E8%BF%87WordPress%E3%80%81Typecho%E3%80%81Ghost%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            