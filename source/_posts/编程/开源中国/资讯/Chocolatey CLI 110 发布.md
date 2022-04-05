
---
title: 'Chocolatey CLI 1.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8118'
author: 开源中国
comments: false
date: Tue, 05 Apr 2022 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8118'
---

<div>   
<div class="content">
                                                                                            <p>Chocolatey 是一个基于 CLI 的 Windows 软件包管理器，有点像 apt-get。Chocolatey CLI 1.1.0 发布，更新内容如下：</p> 
<h3>错误修复</h3> 
<ul> 
 <li>修复--Python 备用源不能正确处理 <code>all</code> 关键词</li> 
 <li>修复--当 chocolatey.config 损坏时，会显示不正确的错误信息</li> 
 <li>修复--当运行 <code>choco outdated</code> 命令时，如果有一个被钉住的软件包，并且正在使用 <code>-ignore-pinned</code> 选项，则会显示错误的退出代码</li> 
 <li>修复--如果它是一个单一的换行符，Windows PowerShell 错误地将带有 BOM 的 UTF8 编码的 PowerShell 文件识别为已签名</li> 
 <li>修复--无法使用 PowerShell Core 安装 Chocolatey</li> 
</ul> 
<h3>改进</h3> 
<ul> 
 <li>当运行 <code>choco upgrade chocolatey</code> 时，支持对不兼容的 Licensed Extension 的安装检查</li> 
 <li>支持运行时检查不兼容的 Chocolatey CLI 和 Chocolatey Licensed Extension 的版本 
  <ul> 
   <li>当被触发时，这些检查将在命令执行的开始和结束时输出一个警告。</li> 
  </ul> </li> 
 <li>在 Chocolatey 安装中包含最新版本的 7zip（v21.07）</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchocolatey%2Fchoco%2Freleases%2Ftag%2F1.1.0" target="_blank">https://github.com/chocolatey/choco/releases/tag/1.1.0</a></p>
                                        </div>
                                      
</div>
            