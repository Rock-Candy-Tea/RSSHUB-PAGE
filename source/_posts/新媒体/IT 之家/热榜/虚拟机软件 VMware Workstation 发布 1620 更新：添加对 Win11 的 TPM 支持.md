
---
title: '虚拟机软件 VMware Workstation 发布 16.2.0 更新：添加对 Win11 的 TPM 支持'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/10/283dc189-ed60-4077-ba8c-39b6c47031c0.png'
author: IT 之家
comments: false
date: Sun, 17 Oct 2021 14:01:47 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/10/283dc189-ed60-4077-ba8c-39b6c47031c0.png'
---

<div>   
<p data-vmark="9edb"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 10 月 17 日消息，据 Neowin 报道，在几天前，VMWare 发布了 16.2.0 版本更新，但是黑暗模式出现了问题，VMWare 已经承认了这一点，并将很快发布修复程序。</p><p data-vmark="7703">值得一提的是，官方的更新日志并没有提到，<span class="accentTextColor">在更新中，VMWare 还添加了对 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Win11</a> 软件级别 TPM 的支持</span>。</p><p data-vmark="b792"><img src="https://img.ithome.com/newsuploadfiles/2021/10/283dc189-ed60-4077-ba8c-39b6c47031c0.png" w="540" h="340" title="虚拟机软件 VMware Workstation 发布 16.2.0 更新：添加对 Win11 的 TPM 支持" width="540" height="340" referrerpolicy="no-referrer"></p><p data-vmark="a523">此前，如果用户一直在启用 TPM 的 VMware Workstation Pro 中使用 Win11 虚拟机，用户必须为每个加密的 VM 设置和输入密码。但是本次更新之后，用户可以移除加密，并加入软件级 TPM 标志来代替，<span class="accentTextColor">不必每次都要输入密码</span>。</p><p data-vmark="55f6">如果你在 Windows 中用 BitLocker 进一步加密虚拟机，可能需要在执行下面的步骤前先解密驱动器。</p><p data-vmark="b7ed">如果你已经在 <a class="s_tag" href="https://win10.ithome.com/" target="_blank">Windows 10</a> 或 11 中添加了 TPM：</p><ul class=" list-paddingleft-2"><li><p data-vmark="b2f0">确保你已经更新到 16.2.0 版本。</p></li><li><p data-vmark="8740">打开编辑虚拟机设置。</p></li><li><p data-vmark="6703">在“硬件”选项卡中删除 TPM。</p></li><li><p data-vmark="e3be">在选项标签中，点击访问控制，然后删除加密功能。</p></li></ul><p data-vmark="f42c"><img src="https://img.ithome.com/newsuploadfiles/2021/10/901c6f18-cef4-44d7-8bf8-172e5c528720.png" w="753" h="515" title="虚拟机软件 VMware Workstation 发布 16.2.0 更新：添加对 Win11 的 TPM 支持" width="753" height="515" referrerpolicy="no-referrer"></p><p data-vmark="cd4c">这将需要一些时间，取决于你的虚拟机有多大，当它完成后，你可以退出虚拟机设置。</p><p data-vmark="8583">向 Workstation Pro 和 Workstation Player 添加软件级 TPM：</p><ul class=" list-paddingleft-2"><li><p data-vmark="85d6">确保你已经更新到 16.2.0 版本。</p></li><li><p data-vmark="3e1c">确保 VMware（管理器）没有运行。</p></li><li><p data-vmark="4cc6">进入存储虚拟机的目录（例如 D:\VM\<a class="s_tag" href="https://win11.ithome.com/" target="_blank">Windows 11</a> Dev）。</p></li><li><p data-vmark="5c95">用记事本打开扩展名为.vmx 的文件。</p></li><li><p data-vmark="2716">添加一行 managedvm.autoAddVTPM = "software" 。</p></li><li><p data-vmark="2fb9">通过关闭文件来保存该文件。</p></li><li><p data-vmark="403d">双击它以在 VMware Workstation Pro 或 Player 中打开它。</p></li><li><p data-vmark="8a9e">启动你的虚拟机。</p></li></ul><p data-vmark="beb5"><img src="https://img.ithome.com/newsuploadfiles/2021/10/51c82b1d-bacf-467b-9071-28768c84712b.png" w="779" h="447" title="虚拟机软件 VMware Workstation 发布 16.2.0 更新：添加对 Win11 的 TPM 支持" width="779" height="447" referrerpolicy="no-referrer"></p><p data-vmark="b85e">你可以通过右键单击“开始”图标并在“运行”命令中输入 tpm.msc 命令来确认 TPM 是否存在。</p><p data-vmark="ac86"><img src="https://img.ithome.com/newsuploadfiles/2021/10/b97b256b-3cbf-43e8-a0bd-a7671ff7d7ba.png" w="754" h="498" title="虚拟机软件 VMware Workstation 发布 16.2.0 更新：添加对 Win11 的 TPM 支持" width="754" height="498" referrerpolicy="no-referrer"></p><p data-vmark="fdf6">如上图显示，在免费的 VMware Workstation Player 中存在一个兼容的 TPM。此外，你还会发现，在虚拟机设置中再次出现了 TPM 模块，不要删除该模块。</p><p data-vmark="bc23">IT之家了解到，此前，VMware Fusion 已适配苹果 M1 Mac，先提供私有技术预览版，用户可以通过在线表格请求访问。</p>
          
</div>
            