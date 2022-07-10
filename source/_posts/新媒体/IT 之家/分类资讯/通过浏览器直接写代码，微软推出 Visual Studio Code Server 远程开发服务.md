
---
title: '通过浏览器直接写代码，微软推出 Visual Studio Code Server 远程开发服务'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/7/6e8eb1bb-9bf8-461d-9a60-af24b0caf8c6.png'
author: IT 之家
comments: false
date: Sun, 10 Jul 2022 07:48:15 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/7/6e8eb1bb-9bf8-461d-9a60-af24b0caf8c6.png'
---

<div>   
<p data-vmark="a27c"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 7 月 10 日消息，早在 2019 年，微软就发布了远程开发扩展，让用户可以通过本地 VS Code 在 Windows 11/10 的 Linux 子系统 (WSL)、Docker 容器、SSH 管理的远程物理或虚拟机上远程开发应用。</p><p data-vmark="e2bf">2020 年，微软 GitHub Codespaces 又做出了进一步的升级，支持在浏览器中通过 VS Code 远程在虚拟机上开发应用。</p><p data-vmark="6127">近日，微软官方<a href="https://code.visualstudio.com/blogs/2022/07/07/vscode-server" target="_blank">宣布</a>了一项新的后端服务 —— <span class="accentTextColor">Visual Studio Code Server</span>，以及一个可以轻松安装、更新、管理和连接到服务的 CLI。</p><p style="text-align: center;" data-vmark="82e4"><img src="https://img.ithome.com/newsuploadfiles/2022/7/6e8eb1bb-9bf8-461d-9a60-af24b0caf8c6.png" w="1440" h="631" title="通过浏览器直接写代码，微软推出 Visual Studio Code Server 远程开发服务" width="1440" height="359" referrerpolicy="no-referrer"></p><p data-vmark="ac8b">据介绍，用户可以将服务器安装在任何位置（本地开发机器、云中的 VM 等），并使用 VS Code for Web（也称为 vscode.dev）通过浏览器安全访问，<span class="accentTextColor">而无需设置 SSH 或 https</span>。</p><p data-vmark="df9c">IT之家了解到，Visual Studio Code Server 目前处于<span class="accentTextColor">私人预览阶段</span>，因此用户需要填写一个<a href="https://aka.ms/vscode-server-signup" target="_blank">注册表单</a>来申请访问权限。如果通过申请，将在几周内收到邮件。</p><h2 data-vmark="0da5">使用方法如下：</h2><p data-vmark="c4d9">1、将 VS Code Server 安装在远程机器上，在终端中运行以下命令：</p><pre class="shiki">wget -O- https://aka.ms/install-vscode-server/setup.sh | sh</pre><p data-vmark="52d5">2、通过在终端中运行以下命令来启动 VS Code Server：</p><pre class="shiki ai-word-checked">code-server</pre><p data-vmark="140d">3、用户的远程机器将通过安全隧道与 vscode.dev 通信，无论在哪个网络上，都允许用户从 vscode.dev 连接到计算机。用户将获得一个设备代码和 URL，并验证 GitHub 帐户。</p><pre class="shiki">Please enter the code 7644-1186 on https://github.com/login/device</pre><p data-vmark="6a8d">4、如果是第一次启动 VS Code Server，系统将提示用户输入连接名称。</p><pre class="shiki ai-word-checked"> What would you like to call this machine? (elegant-pitta)</pre><p data-vmark="b078">5、在验证并提供机器名称后，CLI 会启动服务器实例并生成 vscode.dev URL。接着，<span class="accentTextColor">用户就可以在任意设备上打开此 URL 来写代码了</span>。</p>
          
</div>
            