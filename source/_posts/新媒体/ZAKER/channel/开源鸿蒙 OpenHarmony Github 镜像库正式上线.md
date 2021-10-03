
---
title: '开源鸿蒙 OpenHarmony Github 镜像库正式上线'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202110/61596a79b15ec04e296e9012_1024.jpg'
author: ZAKER
comments: false
date: Sun, 03 Oct 2021 01:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202110/61596a79b15ec04e296e9012_1024.jpg'
---

<div>   
<p>IT 之家 10 月 3 日消息 据开放原子 OpenHarmony 官方发布，开源项目 OpenHarmony 是每个人的 OpenHarmony，OpenHarmony Github 镜像库已正式上线。</p><p>访问地址：https://github.com/openharmony</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202110/61596a79b15ec04e296e9012_1024.jpg" data-height="300" data-width="1080" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202110/61596a79b15ec04e296e9012_1024.jpg" referrerpolicy="no-referrer"></div></div>GitHub 有超过 4000 万注册用户和 1.9 亿代码库（包括至少 2800 万开源代码库），是世界上最大的代码托管平台。开发者可以通过如下 repo 命令，从 Github 下载 OpenHarmony 镜像库代码。<p></p><p><strong>方式一</strong></p><p>通过 repo + ssh 下载（需注册公钥，请参考 GitHub 帮助中心）</p><p>repo init -u git@github.com:openharmony/manifest.git -b master --no-repo-verify repo sync -c repo forall -c 'git lfs pull'</p><p><strong>方式二</strong></p><p>通过 repo + https 下载</p><p>repo init -u https://github.com/openharmony/manifest.git -b master --no-repo-verify repo sync -c repo forall -c 'git lfs pull'</p><p>OpenHarmony 的代码主库地址依旧托管在 Gitee （https://gitee.com/openharmony）。</p><p>IT 之家获悉，通过 Github Action 及自动化脚本，OpenHarmony Github 镜像仓每天 UTC 23:00 定时从 Gitee 主库同步更新代码，方便海外开发者通过 Github 访问及下载 OpenHarmony 开源代码。Github 镜像库不直接处理 issue 及 PR，开发者在 Github 提交的 issue 及 PR 将自动关闭，请直接访问 OpenHarmony Gitee 主库提交 issue 及 PR 。</p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres1.myzaker.com/202110/61596a79b15ec04e296e9013_1024.jpg" data-height="424" data-width="820" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202110/61596a79b15ec04e296e9013_1024.jpg" referrerpolicy="no-referrer"></div></div><p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            