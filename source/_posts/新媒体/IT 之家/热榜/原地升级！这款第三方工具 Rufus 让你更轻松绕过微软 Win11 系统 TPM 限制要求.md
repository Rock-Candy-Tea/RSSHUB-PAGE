
---
title: '原地升级！这款第三方工具 Rufus 让你更轻松绕过微软 Win11 系统 TPM 限制要求'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/3/9ff2b9f9-b910-4def-911b-5865d02e338d.jpg'
author: IT 之家
comments: false
date: Sat, 05 Mar 2022 02:28:02 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/3/9ff2b9f9-b910-4def-911b-5865d02e338d.jpg'
---

<div>   
<p data-vmark="08bc"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 3 月 5 日消息，据 Windows Latest 报道，微软 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Windows 11</a> 在发布时，由于其严格的硬件要求而引起了大量的混乱和批评。Windows 11 正式版要求第八代或更新的英特尔酷睿处理器，4GB 内存，64GB 存储设备，TPM 2.0 UEFI 和安全启动功能启用。</p><p data-vmark="5bb4" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/9ff2b9f9-b910-4def-911b-5865d02e338d.jpg" w="696" h="364" title="原地升级！这款第三方工具 Rufus 让你更轻松绕过微软 Win11 系统 TPM 限制要求" width="696" height="364" referrerpolicy="no-referrer"></p><p data-vmark="820d">虽然 TPM 2.0 对大多数用户来说不是一个大问题，但 Windows 11 的 CPU 要求使许多设备无法接受升级到新的操作系统。</p><p data-vmark="4411">理由是微软要提高最新操作系统的性能和安全性。问题是，很多相对现代的、强大的硬件不符合 CPU 要求，这意味着只有最新一代处理器才最有资格正式升级。</p><p data-vmark="5047">此前已经有许多方法可以绕过 Windows 11 对 CPU、TPM 甚至是内存的要求。微软还发布了一份指南，说明如何绕过要求，将现有的 <a class="s_tag" href="https://win10.ithome.com/" target="_blank">Windows 10</a> 设备升级到 Windows 11，而不需要正式满足所需的规格。</p><p data-vmark="d972">官方程序要求用户手动修改注册表。如果你不想自己修改注册表，现在你可以使用 Rufus 来执行原地升级到 Windows 11。</p><p data-vmark="154c">Rufus 是一个第三方工具，可以轻松创建 USB 驱动器来安装 Windows。此外，也可以使用 Rufus 来执行原地升级到任何版本的 Windows。</p><p data-vmark="63fd">从 Rufus 3.18 开始，你可以创建一个可启动的 Windows 11 媒体，并轻松绕过 TPM 2.0 或 TPM 本身。</p><p data-vmark="b45d">要开始使用，从 <a href="https://github.com/pbatard/rufus/releases/download/v3.18_BETA/rufus-3.18_BETA.exe" target="_blank">Github</a> 下载安装 Rufus 3.18 Beta 测试版，下载 Windows 11 ISO 镜像，插入一个 USB 设备，如果配置中包含 TPM，可以选择“标准 Windows 11 安装（TPM 2.0 + 安全启动）”选项，或者在没有 TPM 的设备上选择第二个选项。</p><p data-vmark="c848" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/717ff54f-20aa-4cd7-ba38-4a0e33721e5f.jpg" w="570" h="841" title="原地升级！这款第三方工具 Rufus 让你更轻松绕过微软 Win11 系统 TPM 限制要求" width="570" height="841" referrerpolicy="no-referrer"></p><p data-vmark="6e6a">Rufus 3.18 Beta 测试版还修复了另一个与 Windows 11 有关的 Bug，该 Bug 破坏了“ISO → ESP 创建”功能。该 Bug（#1855）会阻止在 Windows 11 设备上创建 EFI 系统分区（ESP），并抛出错误代码 0xC00305B4。</p><h3 data-vmark="0e8b">绕过 Windows 11 的 CPU 要求</h3><p data-vmark="f3eb">如果你想绕过这些要求而不使用 Rufus 等第三方应用程序，注册表破解程序也很简单。</p><ul class=" list-paddingleft-2"><li><p data-vmark="0474">执行 Win+r 并输入 regedit。</p></li><li><p data-vmark="7552">导航到 HKEY_LOCAL_MACHINE\SYSTEM\Setup\MoSetup</p></li><li><p data-vmark="11a6">右键单击左侧并创建一个新的 DWORD（32 位）值。</p></li><li><p data-vmark="8a3f">将其名称设为 AllowUpgradesWithUnsupportedTPMOrCPU。</p></li><li><p data-vmark="63ce">将值切换为 1。</p></li></ul><p data-vmark="3537">Rufus 或注册表破解方法可以帮助用户在不支持的硬件上安装操作系统。对于注册表破解，无论如何都需要满足 TPM 要求。如果没有 TPM，请确保遵循第一种方法，其中涉及 Rufus 等第三方工具。</p>
          
</div>
            