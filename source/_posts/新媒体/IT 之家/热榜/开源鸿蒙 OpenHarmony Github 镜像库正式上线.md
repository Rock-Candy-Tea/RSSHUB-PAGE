
---
title: '开源鸿蒙 OpenHarmony Github 镜像库正式上线'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/10/ff0c9341-afd5-482c-a753-ed9eef3d56fd.png'
author: IT 之家
comments: false
date: Sun, 03 Oct 2021 08:20:34 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/10/ff0c9341-afd5-482c-a753-ed9eef3d56fd.png'
---

<div>   
<p data-vmark="b39b"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 10 月 3 日消息 据开放原子 OpenHarmony 官方发布，开源项目 OpenHarmony 是每个人的 OpenHarmony，OpenHarmony Github 镜像库已正式上线。</p><p data-vmark="5ceb">访问地址：https://github.com/openharmony</p><p data-vmark="738c"><img src="https://img.ithome.com/newsuploadfiles/2021/10/ff0c9341-afd5-482c-a753-ed9eef3d56fd.png" w="1080" h="300" title="开源鸿蒙 OpenHarmony Github 镜像库正式上线" width="1080" height="228" referrerpolicy="no-referrer"></p><p data-vmark="a06c">GitHub 有超过 4000 万注册用户和 1.9 亿代码库（包括至少 2800 万开源代码库），是世界上最大的代码托管平台。开发者可以通过如下 repo 命令，从 Github 下载 OpenHarmony 镜像库代码。</p><p data-vmark="8c9f"><strong>方式一</strong></p><p data-vmark="8e69">通过 repo + ssh 下载（需注册公钥，请参考 GitHub 帮助中心）</p><pre class="brush:javascript;toolbar:false">repo init -u <a href="https://www.ithome.com/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="492e203d092e203d213c2b672a2624">[email protected]</a>:openharmony/manifest.git -b master --no-repo-verify
repo sync -c
repo forall -c 'git lfs pull'</pre><p data-vmark="48d6"><strong>方式二</strong></p><p data-vmark="35b2">通过 repo + https 下载</p><pre class="brush:javascript;toolbar:false ai-word-checked">repo init -u https://github.com/openharmony/manifest.git -b master --no-repo-verify
repo sync -c
repo forall -c 'git lfs pull'</pre><p data-vmark="2742">OpenHarmony 的代码主库地址依旧托管在 Gitee （https://gitee.com/openharmony）。</p><p data-vmark="8875">IT之家获悉，通过 Github Action 及自动化脚本，OpenHarmony Github 镜像仓每天 UTC  23:00 定时从 Gitee 主库同步更新代码，方便海外开发者通过 Github 访问及下载 OpenHarmony 开源代码。Github 镜像库不直接处理 issue 及 PR，开发者在 Github 提交的 issue 及 PR 将自动关闭，请直接访问 OpenHarmony Gitee 主库提交 issue 及 PR 。</p><p data-vmark="4ac5"><img src="https://img.ithome.com/newsuploadfiles/2021/10/893c3d3c-e25e-4673-854b-3095eace48a0.jpg@s_2,w_820,h_424" w="1080" h="558" title="开源鸿蒙 OpenHarmony Github 镜像库正式上线" srcset="https://img.ithome.com/newsuploadfiles/2021/10/893c3d3c-e25e-4673-854b-3095eace48a0.jpg 2x" width="1080" height="424" referrerpolicy="no-referrer"></p><p data-vmark="e0d5"><strong>OpenHarmony 网站</strong></p><p data-vmark="c428">https://www.openharmony.cn/（建议国内用户访问）</p><p data-vmark="4bee">https://www.openharmony.io/ (建议海外用户访问)</p><p data-vmark="f77f">OpenHarmony 主库组织地址</p><p data-vmark="69a9">https://gitee.com/openharmony</p><p data-vmark="d5dd">OpenHarmony SIG 组织地址</p><p data-vmark="01eb">https://gitee.com/openharmony-sig</p><p data-vmark="17f6">OpenHarmony 三方库组织地址</p><p data-vmark="f6ac">https://gitee.com/openharmony-tpc</p><p data-vmark="bdcf">OpenHarmony 在线交流平台</p><p data-vmark="24a6">https://zulip.openharmony.cn/</p><p data-vmark="3128">OpenHarmony 社区贡献指南</p><p data-vmark="53fe">https://gitee.com/openharmony/docs/blob/master/zh-cn/contribute/%E5%8F%82%E4%B8%8E%E8%B4%A1%E7%8C%AE.md</p><p data-vmark="dcc2">OpenHarmony Dev 邮件列表</p><p data-vmark="949e"><a href="https://www.ithome.com/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="0662637046697663686e67746b69687f286f69">[email protected]</a></p><p data-vmark="61dc">订阅链接</p><p data-vmark="c74e">https://lists.openatom.io/postorius/lists/dev.openharmony.io/</p>
          
</div>
            