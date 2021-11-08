
---
title: 'Win11本月大规模推送 教你一招阻止Win10升级'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211108/s_651c11f169a44d2f86bdba393d6b6087.jpg'
author: 快科技（原驱动之家）
comments: false
date: Mon, 08 Nov 2021 15:34:02 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211108/s_651c11f169a44d2f86bdba393d6b6087.jpg'
---

<div>   
<p class="MsoNormal">微软的<span lang="EN-US">Win11</span>正式推送一个月有余，有些人已经收到了<span lang="EN-US">Win11</span>的推送升级，虽然<span lang="EN-US">bug</span>还是断断续续出现，但微软之前已经表态，<span lang="EN-US">Win11</span>可用性已经没啥问题，<span lang="EN-US">11</span>月份就要大规模推送升级了。</p>
<p class="MsoNormal">考虑到现在<span lang="EN-US">Win10</span>的份额是最多的，那<span lang="EN-US">Win11</span>肯定要从<span lang="EN-US">Win10</span>用户中抢份额，如果现在的<span lang="EN-US">Win10</span>系统用得还很顺手，不想升级怎么办？现在可以自己修改下注册表或者组策略，阻止<span lang="EN-US">Win10</span>接收<span lang="EN-US">Win11</span>推送。</p>
<p class="MsoNormal">如果是<span lang="EN-US">Win10</span>的家用版、专业版，这个过程需要修改注册表，过程如下：</p>
<p class="MsoNormal"><span lang="EN-US">1</span>、定位注册表位置：</p>
<p class="MsoNormal"><span lang="EN-US">Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate</span></p>
<p class="MsoNormal"><span lang="EN-US">2</span>、创建（<span lang="EN-US">DWORD (32-bit)</span>）项，<strong>并命名为<span lang="EN-US">TargetReleaseVersion</span>，值设置为<span lang="EN-US">1</span>。</strong></p>
<p class="MsoNormal"><span lang="EN-US">3</span>、接着创建另一个（<span lang="EN-US">DWORD (32-bit)</span>）项，<strong>并命名为<span lang="EN-US">TargetReleaseVersionInfo</span>，值设置为<span lang="EN-US">21H1</span>。</strong></p>
<p class="MsoNormal">相比家用版及专业版，<span lang="EN-US">Win10</span>企业版用户阻止升级的操作更简单一些，不用修改注册表，通过组策略即可。</p>
<p class="MsoNormal">找到<span style="color:#ff0000;"><strong>本地计算机策略<span lang="EN-US">></span>计算机配置<span lang="EN-US">> </span>管理模板<span lang="EN-US">> Windows</span>组件<span lang="EN-US">> Windows</span>更新<span lang="EN-US">> </span>适用于企业的<span lang="EN-US">Windows </span>更新，</strong></span>然后双击在弹出的对话框中输入<span lang="EN-US">21H1</span>确定，重启之后就不会收到<span lang="EN-US">Win11</span>推送了。</p>
<p class="MsoNormal">以上方法都是暂时的，在微软没有强制升级<span lang="EN-US">Win11</span>之前可行。</p>


<p align="center"><a href="https://img1.mydrivers.com/img/20211108/651c11f169a44d2f86bdba393d6b6087.jpg" target="_blank"><img alt="Win11本月大规模推送 教你一招阻止Win10升级" h="400" src="https://img1.mydrivers.com/img/20211108/s_651c11f169a44d2f86bdba393d6b6087.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/weiruan.htm"><i>#</i>微软</a><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a><a href="https://news.mydrivers.com/tag/windows_10.htm"><i>#</i>Windows 10</a></p>
<p class="url">
     
<span>责任编辑：宪瑞</span>
</p>
        
</div>
            