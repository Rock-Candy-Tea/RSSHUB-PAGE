
---
title: 'WordPress上的PHP Everywhere插件曝出三个高危RCE漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0212/b34f90e41f2a027.png'
author: cnBeta
comments: false
date: Sat, 12 Feb 2022 06:41:02 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0212/b34f90e41f2a027.png'
---

<div>   
Bleeping Computer 报道称：<strong>安全研究人员在 WordPress 的“PHP Everywhere”插件中发现了三个严重的远程代码执行（RCE）漏洞，导致全球超过 3 万个使用该插件的网站都受到了影响。</strong>据悉，该插件旨在方便管理员在页面、帖子、侧边栏、或任何 Gutenberg 块中插入 PHP 代码，并借此来显示基于评估的 PHP 表达式的动态内容。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0212/b34f90e41f2a027.png" referrerpolicy="no-referrer"></p><p>Wordfence 安全分析师指出，CVSS v3 评分高达 9.9 的这三个漏洞，可被贡献着或订阅者所利用，且波及 2.0.3 及以下的所有 WordPress 版本。</p><p><strong>首先是 CVE-2022-24663：</strong></p><blockquote><p>只需发送带有‘短代码’参数设置的 PHP Everywhere 请求，任何订阅者都可利用该 RCE 漏洞，并在站点上执行任何 PHP 代码。</p></blockquote><p><strong>其次是 CVE-2022-24664：</strong></p><blockquote><p>贡献者可借助插件的元框来利用该 RCE 漏洞，前提是创建一则帖子，添加一个 PHP 代码元框，然后进行预览。</p></blockquote><p><strong>然后是 CVE-2022-24665：</strong></p><blockquote><p>具有 edit_posts 权限、并可添加 PHP Everywhere Gutenberg 块的贡献者们，都可利用该 RCE 漏洞。</p><p>在易受攻击的插件版本中，PHP Everywhere 并未默认指定‘仅管理员权限’可用的安全设置，结果留下了这一隐患。</p></blockquote><p>尽管后两个漏洞因需要贡献者的权限级别而不那么容易被利用，但首个漏洞还是让业界感到惊诧不已。</p><blockquote><p>举个例子，只要某个用户在网站上以‘订阅者’的身份登录，便足以获得相应的权限来执行恶意 PHP 代码。</p><p>不论怎样，可在网站上执行任意代码，都可能导致整个站点被攻击者所接管 —— 这也是所有网站安全事故中最糟糕的一种情况。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0212/464bec5ee2d240b.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：<a href="https://www.wordfence.com/blog/2022/02/critical-vulnerabilities-in-php-everywhere-allow-remote-code-execution/" target="_self">Wordfence</a>）</p><p>在 2022 年 1 月 4 日发现了上述漏洞字后，Wordfence 团队很快就向 PHP Everywhere 作者通报了此事。</p><blockquote><p>厂商于 2022 年 1 月 10 日发布了 3.0.0 版安全更新，由于需要大量重写代码，所以版本号也发生了重大改变。</p></blockquote><p>尴尬的是，尽管开发者行动迅速，但网站管理员普遍不怎么会定期更新其 WordPress 网站和插件。</p><blockquote><p>由 WordPress.org 分享的<a href="https://api.wordpress.org/stats/plugin/1.0/downloads.php?slug=php-everywhere" target="_self">统计数据</a>可知，自 Bug 修复方案推出以来，3 万次安装中只有 1.5 万次更新了插件。</p></blockquote><p>有鉴于此，考虑到三个 RCE 漏洞的严重性，我们在此强烈建议所有 PHP Everywhere 用户确保其已升级到最新可用的 3.0.0 版本。</p><blockquote><p>需要注意的是，如果你在站点上使用了经典编辑器，则需要先卸载该插件、并找到替代解决方案，以在其组件上托管自定义的 PHP 代码。</p><p>因为 PHP Everywhere 的 3.0.0 版本仅支持基于 Block 编辑器的 PHP 片段，且作者不大可能致力于恢复落后的 Classic 功能。</p></blockquote>   
</div>
            