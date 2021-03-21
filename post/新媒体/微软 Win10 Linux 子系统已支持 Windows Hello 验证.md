
---
title: 微软 Win10 Linux 子系统已支持 Windows Hello 验证
categories: 
    - 新媒体
    - ZAKER - channel
author: ZAKER - channel
comments: false
date: Sun, 21 Mar 2021 07:41:49 GMT
thumbnail: http://zkres1.myzaker.com/202103/605729b6b15ec0510d2dbcef_1024.jpg
---

<div>   
<p>IT 之家 3 月 21 日消息 微软 Win10 中的一项重要功能，就是 Linux 子系统，也叫 WSL，该功能可以让用户同时使用 Win10 和 Linux 系统。</p><p>据外媒 XDA 报道，近日一位日本开发者在 GitHub 发布了一个开源项目，可使 Linux 子系统支持 Windows Hello 功能。</p><p>从图中可以看出，当用户在 Ubuntu-20.04 子系统中输入 sudo 进行超级用户提权时，Win10 自动弹出了 Windows Hello 人脸识别，识别成功后就可以正确提权。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div"><img class="lazy opacity_0 zaker_gif_cache" id="img_0" data-original="http://zkres1.myzaker.com/202103/605729b6b15ec0510d2dbcef_1024.jpg" data-gif-url="http://zkres1.myzaker.com/202103/605729b6b15ec0510d2dbcef_raw.gif" data-height="432" data-width="700" src="http://zkres1.myzaker.com/202103/605729b6b15ec0510d2dbcef_1024.jpg" referrerpolicy="no-referrer"></div></div>IT 之家了解到，该项目由可插拔身份验证模块（PAM）以及负责调用 Windows Hello 的伴随 Windows 应用程序组成，PAM 模块负责将 Linux 用户的身份验证请求映射到相应的 Windows 10 用户的 Windows Hello 签名。<p></p><p>由于采用模块化设计，该项目不仅可用于 WSL2，也可用于上一代的 WSL。用户需要下载预编译的二进制文件，在 Linux 子系统下执行 install.sh 脚本，然后通过 PAM 模块配置进程。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            