
---
title: 'Win11下锐龙游戏性能暴跌15%_AMD新驱动已解决问题：快升级'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211022/54fb3eec-daf3-46ce-a8a5-3bfbf6252a43.png'
author: 快科技（原驱动之家）
comments: false
date: Fri, 22 Oct 2021 16:28:46 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211022/54fb3eec-daf3-46ce-a8a5-3bfbf6252a43.png'
---

<div>   
<p class="MsoNormal">微软的<span lang="EN-US">Win11</span>系统系统发布两周了，很多玩家已经升级，不过<span lang="EN-US">AMD</span>锐龙平台的玩家有个糟心的问题，那就是<span lang="EN-US">Win11</span>下锐龙的兼容性问题，<a class="f14_link" href="https://news.mydrivers.com/1/787/787440.htm" target="_blank">之前消息称游戏性能最多可下降<span lang="EN-US">15%</span>，</a>虽然实测并不明显。</p>
<p class="MsoNormal">最近微软及<span lang="EN-US">AMD</span>都在解决这个麻烦，但这事实际上牵涉两个问题，修复的手段也不同。</p>
<p class="MsoNormal">具体来说，<span lang="EN-US">AMD</span>处理器在<span lang="EN-US">Windows 11</span>系统中的两个兼容性问题，都会导致性能不同程度地下跌。</p>
<p class="MsoNormal"><strong><span lang="EN-US">1</span>、三级缓存延迟可能增加<span lang="EN-US">3</span>倍之多</strong></p>
<p class="MsoNormal">这将影响对缓存、内存子系统敏感的应用，性能或损失<span lang="EN-US">3-5</span>％，部分电竞网游可能高达<span lang="EN-US">10-15</span>％。</p>
<p class="MsoNormal"><strong><span lang="EN-US">2</span>、<span lang="EN-US">UEFI CPPC2</span>无法优先将进程调度到最快核心上</strong></p>
<p class="MsoNormal">只需单核心或者少量核心的应用会出现性能下降，特别是核心数超过<span lang="EN-US">8</span>个、热设计功耗超过<span lang="EN-US">65W</span>的型号会更明显。</p>
<p class="MsoNormal">针对<span lang="EN-US">L3</span>缓存延迟的问题，<strong>微软已经发布了<span lang="EN-US">Windows Build 22000.282</span>（<span lang="EN-US">KB5006746</span>）</strong>，修复了延迟问题。</p>
<p class="MsoNormal">针对<span lang="EN-US">CPPC2</span>的问题，这个需要<span lang="EN-US">AMD</span>发布补丁，今天<span lang="EN-US">AMD</span>也正式推出了锐龙芯片组驱动<span lang="EN-US">3.10.08.506</span>，主要升级内容有两点：</p>
<p class="MsoListParagraph" style="margin-left:18.0pt;text-indent:-18.0pt;
mso-char-indent-count:0;mso-list:l0 level1 lfo1">1、修复了<span lang="EN-US">OpenGL</span>报错弹出的问题</p>
<p class="MsoListParagraph" style="margin-left:18.0pt;text-indent:-18.0pt;
mso-char-indent-count:0;mso-list:l0 level1 lfo1">2、在<span lang="EN-US">Windows11 build 22000.189</span>及之后的版本中，<strong><span lang="EN-US">AMD</span>处理器的<span lang="EN-US">UEFI CPP2</span>功能及操作恢复正常。</strong></p>
<p class="MsoNormal">简单来说，<span style="color:#ff0000;"><strong>锐龙处理器用户升级了微软最新的<span lang="EN-US">Windows Build 22000.282</span>之后，再升级<span lang="EN-US">AMD</span>锐龙芯片组驱动<span lang="EN-US">3.10.08.506</span>，<span lang="EN-US">Win11</span>下性能下降的两个问题才算完整修复。</strong></span></p>
<p class="MsoNormal">此外，锐龙芯片组驱动<span lang="EN-US">3.10.08.506</span>还存在以下问题：</p>
<p class="MsoListParagraph" style="margin-left:18.0pt;text-indent:-18.0pt;
mso-char-indent-count:0;mso-list:l1 level1 lfo2">1、有时候自定义安装更新<span lang="EN-US">AMD</span>驱动会失败</p>
<p class="MsoListParagraph" style="margin-left:18.0pt;text-indent:-18.0pt;
mso-char-indent-count:0;mso-list:l1 level1 lfo2">2、在俄语中可能会出现文本对齐问题</p>
<p class="MsoListParagraph" style="margin-left:18.0pt;text-indent:-18.0pt;
mso-char-indent-count:0;mso-list:l1 level1 lfo2">3、安装驱动之后在非英语系统上可能要手动重启系统</p>
<p class="MsoListParagraph" style="margin-left:18.0pt;text-indent:-18.0pt;
mso-char-indent-count:0;mso-list:l1 level1 lfo2">4、安装过程中可能会出现<span lang="EN-US">Windows Installer</span>弹出消息</p>
<p class="MsoListParagraph" style="margin-left:18.0pt;text-indent:-18.0pt;
mso-char-indent-count:0;mso-list:l1 level1 lfo2">5、卸载摘要日志可能会在非英语操作系统上错误地显示卸载失败</p>
<p class="MsoListParagraph" style="margin-left:18.0pt;text-indent:-18.0pt;
mso-char-indent-count:0;mso-list:l1 level1 lfo2">6、安装程序启动并且点击<span lang="EN-US">UI</span>界面之后可能会弹出“<span lang="EN-US">AMD</span>芯片组软件没有响应”的消息</p>
<p class="MsoNormal"><strong>锐龙芯片组驱动<span lang="EN-US">3.10.08.506</span>下载页面</strong></p>
<p class="MsoNormal"><a class="f14_link" href="https://drivers.mydrivers.com/drivers/560_224045.htm" target="_blank"><span lang="EN-US">AMD Ryzen Chipset Drivers</span>主板芯片组驱动<span lang="EN-US">3.10.08.506</span>版<span lang="EN-US">For Win10-64/Win11</span></a></p>
<p class="MsoNormal" style="text-align: center;"><img alt="Win11下锐龙游戏性能暴跌15%?AMD新驱动已解决问题：快升级" h="397" src="https://img1.mydrivers.com/img/20211022/54fb3eec-daf3-46ce-a8a5-3bfbf6252a43.png" style="text-align: center; border: 1px solid black;" w="600" referrerpolicy="no-referrer"></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/amd.htm"><i>#</i>AMD</a><a href="https://news.mydrivers.com/tag/cpuchuliqi.htm"><i>#</i>CPU处理器</a><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     
<span>责任编辑：宪瑞</span>
</p>
        
</div>
            