
---
title: '代号_monet_的Google壁纸主题引擎有望在Android 12.1中开源'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0923/524f25253e18453.jpg'
author: cnBeta
comments: false
date: Thu, 23 Sep 2021 05:56:24 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0923/524f25253e18453.jpg'
---

<div>   
不会出现在 Android 12 开源代码中的一个主要功能，就是代号为“monet”的壁纸主题引擎。<strong>不过这种非开源似乎只是暂时的，有证据表明“monet”将随着 Android 12.1 的发布而被完全开源。</strong><br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0923/524f25253e18453.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0923/524f25253e18453.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0923/ea415d366376569.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0923/ea415d366376569.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">自 Android 5.0 Lollipop 在 2014 年引入 Material Design 以来，Android 12 在用户界面上的变化最为明显。Google的设计语言经过多年的发展，为了反映最新的迭代对个性化的强调，Google已经将其重新命名为“Material You”。</p><p style="text-align: left;">Material You 设计语言的特点之一就是上文提及的“monet”主题系统，该系统根据用户的壁纸自动生成一个调色板。Google 称，一个采用聚类算法的颜色提取引擎与 Material 的颜色目标确定了用户壁纸的主导颜色和次主导颜色。</p><p style="text-align: left;">然后，调色板生成算法创建了一个由5种颜色组成的丰富调色板--2种中性色和3种重点色--以及12种材料色的色调，用来确定最接近用户壁纸的色调。这些颜色值被保存在一个索引中，应用程序可以通过 API 调用，让他们也能为自己的用户界面做主题。</p><p style="text-align: left;">早在今年早些时候的 I/O 开发者大会上，Google首次公布其“monet”主题系统时，该公司表示，它将在秋季首先出现在Google Pixel <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>上。</p><p style="text-align: left;">然而，目前还不清楚Google是否只是声称“monet”的首发排他性，还是该功能将完全为运行 Android 12 的 Pixel 手机所独有。换句话说，我们不知道像<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://samsung.jd.com/" target="_blank">三星</a>、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&aid=450&euid=&t=http%3A%2F%2Fwww.mi.com%2F" target="_blank">小米</a>、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://oppo.jd.com/" target="_blank">OPPO</a> 或 OnePlus 这样的设备制造商是否能在他们自己的操作系统中完全使用“monet”。</p><p style="text-align: left;">幸运的是，Google似乎已经准备好发布这一算法的源代码。两个消息来源证实，Google最近提交了一个名为“在AOSP中添加monet”的代码修改。这个补丁最初只在 Android 13 “Tiramisu”的 AOSP 内部分支中提供，但最近被挑到了 Android 12-sv2 内部分支中。</p><p style="text-align: left;">Android 12-sv2 将是一个维护更新，伴随着 API 级别的提升，所以我们暂且称之为 Android 12.1。除了一张新的壁纸，该更新还将为可折叠手机的体验带来一些小的改进，包括任务栏功能。当然，这显然将是第一个包含"monet"源代码的版本。</p><p style="text-align: left;">下面的截图取自运行 Android 12.1 内部 AOSP 版本的设备，显示“monet”已经在开源版本中实现。只是目前尚不清楚 Google 何时会发布 Android 12.1.</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0923/5819756a0e42d5a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0923/5819756a0e42d5a.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0923/20c2298c8b91630.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0923/20c2298c8b91630.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;"><a href="https://static.cnbetacdn.com/article/2021/0923/c24655adfa4faf9.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0923/c24655adfa4faf9.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            