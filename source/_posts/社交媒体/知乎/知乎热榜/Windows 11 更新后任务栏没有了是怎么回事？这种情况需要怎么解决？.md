
---
title: 'Windows 11 更新后任务栏没有了是怎么回事？这种情况需要怎么解决？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic2.zhimg.com/v2-39b745eaca8269b255e295b08abb885a_1440w.jpg'
author: 知乎
comments: false
date: Fri, 03 Sep 2021 04:11:13 GMT
thumbnail: 'https://pic2.zhimg.com/v2-39b745eaca8269b255e295b08abb885a_1440w.jpg'
---

<div>   
Ling Gao的回答<br><br><h2>「突发 & 紧急」关于 “开始菜单与任务栏无响应” 和 “部分系统功能无法加载” 问题的解决方案。</h2><p>各位 Windows 预览体验成员 (Insiders)，中午好！</p><p>2021 年 9 月 3 日，大量 <b>Dev</b> 和 <b>Beta</b> 渠道中的 Windows 预览体验成员报告称：<b>开始菜单与任务栏无响应、部分系统功能无法加载</b>。Microsoft 已经定位上述 Bug 成因，目前正在开展调查和处理工作，Windows 预览体验版本现已暂停更新部署。</p><p><b>如果您已经不幸遭受上述问题的困扰，请执行以下方案，将您的电脑恢复至正常状态：</b></p><ol><li>按下 <b>“Ctrl + Alt + Del”</b> 快捷键，启动<b>任务管理器</b>。</li><li>点击任务管理器<b>底部</b>的 <b>“详细信息”</b> 按钮，将界面展开。</li><li>点击任务管理器<b>顶部</b>的<b> “文件”>“运行新任务”</b> 按钮。</li><li>在对话框中输入<b> “cmd” (</b>不带引号)，敲击回车启动<b>命令提示符</b>。</li><li><b>复制</b>下方命令，<b>粘贴</b>至<b>命令提示符</b>：<b><i>reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\IrisService /f && shutdown -r -t 0</i></b></li><li>再次敲击回车，您的电脑将自动重启并恢复至正常状态。</li></ol><p>非常抱歉为您带来了糟糕的 Windows 预览体验版本使用体验！</p><p>顺祝时祺，</p><p><b>- 高楷修 (Ling Gao)  ‍ </b></p><p><b>Windows Insider 最有价值专家 (MVP)</b></p><figure data-size="normal"><img src="https://pic2.zhimg.com/v2-39b745eaca8269b255e295b08abb885a_1440w.jpg" data-rawwidth="1312" data-rawheight="1104" data-size="normal" data-default-watermark-src="https://pic2.zhimg.com/v2-ad62f05d529ff2b04f6c9d05807b309f_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic2.zhimg.com/v2-39b745eaca8269b255e295b08abb885a_r.jpg" referrerpolicy="no-referrer"><figcaption>Microsoft 中文社区 | 屏幕截图存档</figcaption></figure><a data-draft-node="block" data-draft-type="link-card" href="http://link.zhihu.com/?target=https%3A//answers.microsoft.com/zh-hans/insider/forum/all/%25e7%25aa%2581%25e5%258f%2591/55d32c53-5b40-4264-b9d5-caabd4058fa4" class=" wrap external" target="_blank" rel="nofollow noreferrer">「突发 & 紧急」关于 “开始菜单与任务栏无响应” 和 “部分系统功能无法加载” 问题的解决方案。</a><figure data-size="normal"><img src="https://pic4.zhimg.com/v2-65d68b4043f522076a5d587d9388535b_1440w.jpg" data-rawwidth="859" data-rawheight="412" data-size="normal" data-default-watermark-src="https://pic2.zhimg.com/v2-7a6569d36a15bd0f0023d5a6a7e84c13_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic4.zhimg.com/v2-65d68b4043f522076a5d587d9388535b_r.jpg" referrerpolicy="no-referrer"><figcaption>Windows Insider 最有价值专家 (MVP)</figcaption></figure><p></p>  
</div>
            