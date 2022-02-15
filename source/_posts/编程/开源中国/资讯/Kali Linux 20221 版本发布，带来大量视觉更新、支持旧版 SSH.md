
---
title: 'Kali Linux 2022.1 版本发布，带来大量视觉更新、支持旧版 SSH'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0215/075834_2oZx_5430600.png'
author: 开源中国
comments: false
date: Tue, 15 Feb 2022 07:57:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0215/075834_2oZx_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p>Kali Linux 2022.1 是新一年的第一个 Kali Linux 版本，正好赶上情人节。此版本为现有功能带来了各种视觉更新和调整。</p> 
<p>自 2021 年 12 月 2021.4 版本以来的主要变更如下：</p> 
<h2 style="text-align:start">视觉更新：主题更新</h2> 
<p>从这个版本 (2022.1) 开始，每年的 20xx.1 版本将是唯一具有大量视觉更新的版本，视觉更新包括用于桌面、登录和启动显示的新壁纸，以及更新后的安装程序主题，这样可以更容易地识别不同版本的 Kali Linux。</p> 
<p><img alt height="395" src="https://static.oschina.net/uploads/space/2022/0215/075834_2oZx_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p><img alt height="394" src="https://static.oschina.net/uploads/space/2022/0215/075850_3Fpj_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p>此外，ISO 映像中存在的启动菜单的功能、主题和布局也得到了改进，使主题保持一致性：</p> 
<p><img alt height="263" src="https://static.oschina.net/uploads/space/2022/0215/075904_dJ1n_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">Shell 提示更改</h2> 
<p>在编写专业的渗透测试报告，或共享终端以协作调试代码时，<strong>右侧提示</strong> （包含退出代码和后台进程的数量）可能会妨碍工作。因此它<strong>已从默认 shell</strong> <strong>ZSH 中删除。</strong>此外，根提示符中的头骨已被替换为普通的 K 符号：</p> 
<p><img height="160" src="https://static.oschina.net/uploads/space/2022/0215/075725_43YS_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>新的浏览器登陆页面</h2> 
<p>为 Kali 中提供的默认登录页面带来了全新的外观，利用更新的文档站点（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kali.org%2Fdocs%2F" target="_blank">Kali-Docs</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kali.org%2Ftools%2F" target="_blank">Kali-Tools</a>），搜索功能可以搜索到 Kali 所需的任何内容。</p> 
<p><img alt height="513" src="https://static.oschina.net/uploads/space/2022/0215/080022_msjS_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>“kali-linux-everything” ISO 映像</h2> 
<p>这个版本迎来一个新的 Kali 安装版本：“kali-linux-everything”镜像，这是一个完整的离线独立映像(ISO)，其中预安装 Kali 的所有工具包。使用这个版本安装 Kali，在 Kali 的设置过程中，用户不需要通过网络映像下载“kali-linux-everything”包，在无网络的区域亦能安装 Kali 所有专业工具。但由于有更多的软件包，安装该该本 Kali 也需要更长的时间。</p> 
<p><strong>由于已知限制，目前</strong> <strong>“kali-linux-everything”</strong><strong>不包括 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kali.org%2Fblog%2Fintroducing-kaboxer%2F" target="_blank">Kaboxer 应用程序。</a></strong></p> 
<h2 style="text-align:start">Kali-Tweaks：让传统 SSH 变得简单</h2> 
<p>kali-tweaks 强化部分有一个新设置：现在可以将 Kali 的 SSH 客户端配置为宽兼容性，意味着启用旧算法和密码。连接到使用它们的旧服务器变得很简单，无需在命令行上显式传递其他选项。此设置的目的是更容易发现易受攻击的 SSH 服务器，这会打开更多潜在的攻击面。</p> 
<p>注意：与 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kali.org%2Fblog%2Fkali-linux-2021-3-release%2F" target="_blank">OpenSSL</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kali.org%2Fblog%2Fkali-linux-2021-4-release%2F" target="_blank">Samba </a>不同，SSH 是一个足够敏感的组件，应当在默认情况下保持它的安全，所以默认情况下 kali-tweaks 这种弱化行为 不会启用 ，如果你对此设置感兴趣，必须运行<code>kali-tweaks</code>，进入 <em>Hardening </em>部分并在其中启用它。</p> 
<p><img alt height="248" src="https://static.oschina.net/uploads/space/2022/0215/080043_wFpO_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p>该版本还包含其他的修复项和新软件包，详情可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kali.org%2Fblog%2Fkali-linux-2022-1-release%2F" target="_blank">官方公告</a>中查看。</p>
                                        </div>
                                      
</div>
            