
---
title: 'Win11升级全教程get！并不是你的配置不够'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210710/Sbd05e6f8-9e65-4a72-a04d-fd8def3caeec.jpg'
author: 快科技（原驱动之家）
comments: false
date: Sat, 10 Jul 2021 17:04:24 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210710/Sbd05e6f8-9e65-4a72-a04d-fd8def3caeec.jpg'
---

<div>   
<p>微软于6月24日发布Win11操作系统，虽然目前还没有进行全面覆盖升级，但想先体验的用户肯定早已按耐不住。</p>
<p>不过此次Win11升级的条件也是异常苛刻，不仔细研究一番还真无从下手，今天笔者就把自己升级Win11的过程和步骤列出来，看看你遇到的问题是不是也在其中。</p>
<p><strong>【注意：升级有风险！数据无价！升级有风险！数据无价！升级有风险！数据无价！】</strong></p>
<p>对于笔记本用户来说升级可能相对轻松，因为并不需要更改太多配置，并且大部分新的笔记本都可以直升Win11，如果手中正好有可以一试。</p>
<p><strong>Win11升级系统检测工具</strong></p>
<p>但对于PC机来说，首先大家遇到最多的问题应该就是：你的电脑不满足Windows11的最低硬件要求。<span style="color:#ff0000;"><strong>其实并不是配置不够，而是软件方面的问题。</strong></span></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/bd05e6f8-9e65-4a72-a04d-fd8def3caeec.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="450" src="https://img1.mydrivers.com/img/20210710/Sbd05e6f8-9e65-4a72-a04d-fd8def3caeec.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>本次升级Win11对于配置还是有一定要求的，用户可以自行下载一个检测工具，看看哪些不符合，上图笔者以自己的电脑检测为例，如果都符合则可以直接升级，下面我们直接来看升级步骤，并在过程中详细解决遇到的问题。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/89a29b1c-c068-45dc-aa17-2161a5e6dd88.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="328" src="https://img1.mydrivers.com/img/20210710/S89a29b1c-c068-45dc-aa17-2161a5e6dd88.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>第一步在系统菜单中选择【更新和安全】→【Windows预览体验计划】，在这里点击开始按照步骤即可参与体验。</p>
<p><strong>修改注册表加入【Windows预览体验计划】</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/7ea44b50-3b68-40c5-8c68-a1d2e2ca31da.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="512" src="https://img1.mydrivers.com/img/20210710/S7ea44b50-3b68-40c5-8c68-a1d2e2ca31da.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>这第一步，其实也阻挡了大部分用户，如果点击【Windows预览体验计划】出现一片空白的情况，需要唤出Windows PowerShell(管理员)（A）。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/f2a5d3c4-3e94-40c6-ba24-ee919b674678.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="405" src="https://img1.mydrivers.com/img/20210710/Sf2a5d3c4-3e94-40c6-ba24-ee919b674678.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>右键单击【开始】→【Windows PowerShell(管理员)（A）】，如果弹出是否的对话框，选择【是】。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/36db1841-257b-483a-be32-493d146f0746.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="512" src="https://img1.mydrivers.com/img/20210710/S36db1841-257b-483a-be32-493d146f0746.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>分别输入五条命令符</p>
<p>\$path = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection"</p>
<p># Telemetry level: 1 - basic, 3 - full</p>
<p>\$value = "3"</p>
<p>New-ItemProperty -Path \$path -Name AllowTelemetry -Value \$value -Type Dword -Force</p>
<p>New-ItemProperty -Path \$path -Name MaxTelemetryAllowed -Value \$value -Type Dword -Force</p>
<p>逐条复制上面这五段命令代码并按回车，最终执行结果如上图所示。这一段操作是在注册表中更改参数，如果手动在注册表中查找也可以达到同样效果。</p>
<p>命令输入后就可以关闭【管理员Windows PowerShell】命令框，再次查看【Windows预览体验计划】即可出现开始选项。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/e0a09ddd-64c0-4fb9-858a-b3f85de794b8.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="328" src="https://img1.mydrivers.com/img/20210710/Se0a09ddd-64c0-4fb9-858a-b3f85de794b8.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>点击开始后需要关联微软账户，没有的直接注册一个即可，接下来一直确认确认直到最后一步重启电脑。</p>
<p><strong>【Hard】【Normal】【Easy】模式</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/a9934b0e-11f3-4290-bf26-a4b11d2584d7.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="423" src="https://img1.mydrivers.com/img/20210710/Sa9934b0e-11f3-4290-bf26-a4b11d2584d7.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
点击灰色区域</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/cf9f380a-ff1e-4b7a-8282-852e3455ed1c.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="416" src="https://img1.mydrivers.com/img/20210710/Scf9f380a-ff1e-4b7a-8282-852e3455ed1c.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
【Hard】【Normal】【Easy】模式</p>
<p>重启后，再回到【Windows预览体验计划】会出现一个灰色的对话框，点击之后会让用户选择三种不同的模式。</p>
<p>Dev渠道：主要针对开发者，会包含目前Win11大部分内容，但相应的BUG较多；</p>
<p>Beta渠道：主要针对普通参与测试的内部人员，会包含较为稳定的少部分内容；</p>
<p>Release Preview渠道：主要针对商业用户，只包含一些新的修复和补丁；</p>
<p>由于我们此次的测试就是为了体验Win11的更多功能，所以选择了Dev渠道，如果是普通用户可以选择Beta渠道。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/7aa980e0-ee98-42e0-bfda-e01b42548186.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="375" src="https://img1.mydrivers.com/img/20210710/S7aa980e0-ee98-42e0-bfda-e01b42548186.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>选择完成直接关闭即可，现在回到【Windows更新】会出现Windows11的新系统下载。但是，到了这一步仍然会出现很多问题，首先是TPM（可信平台模块）。</p>
<p><strong>开启TPM</strong></p>
<p style="text-align: center"><img alt="WIN11升级全教程 并不是你的配置不够" h="228" src="https://img1.mydrivers.com/img/20210710/85267cb5-8b9f-4598-908e-30b0df0307c2.jpg" style="border: black 1px solid" w="396" referrerpolicy="no-referrer"><br>
运行【tpm.msc】</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/72ec862f-2782-4f8e-9844-54996b44595e.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="427" src="https://img1.mydrivers.com/img/20210710/S72ec862f-2782-4f8e-9844-54996b44595e.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>想要更新Win11首先电脑要支持TPM 2.0，检查的方法也很简单，首先【Win+R】调出“运行”对话框，输入【tpm.msc】点击确定，如果尚未支持会显示上图内容。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/fba19136-b4c4-40df-8181-ac5385ef6c6e.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="450" src="https://img1.mydrivers.com/img/20210710/Sfba19136-b4c4-40df-8181-ac5385ef6c6e.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
【安全】</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/cb23c5b2-a96f-4411-87a4-2c62a886af89.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="450" src="https://img1.mydrivers.com/img/20210710/Scb23c5b2-a96f-4411-87a4-2c62a886af89.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
【Trusted Computing】</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/c58111f7-d9a1-4a66-8bcc-8247f4d1815f.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="450" src="https://img1.mydrivers.com/img/20210710/Sc58111f7-d9a1-4a66-8bcc-8247f4d1815f.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
【Security Device Support】</p>
<p>不过目前部分主板已经可以支持手动打开该选项，我们以微星主板为例，开机进入BIOS，选择【设置】→【安全】→【Trusted Computing】→【Security Device Support】→【Enable】。执行完该操作后按【F10】保存并重启，此时可再次执行【tpm.msc】命令查看效果。</p>
<p><strong>磁盘分区形式</strong></p>
<p>解决完TPM的问题后，还有磁盘分区形式和UEFI的问题，UEFI比较好说，我们同样在BIOS【安全启动】选项中，选择仅UEFI进行引导。</p>
<p style="text-align: center"><img alt="WIN11升级全教程 并不是你的配置不够" h="280" src="https://img1.mydrivers.com/img/20210710/fa0abb09-f8eb-411d-adc7-3c837834a431.jpg" style="border: black 1px solid" w="443" referrerpolicy="no-referrer"></p>
<p>但我们默认装系统的磁盘分区形式基本为“MBR”类型，修改后主板会识别不到启动文件，需要手动转换为“GPT”类型。为此笔者也是付出了惨痛代价，由于测试平台为MBR类型分区，使用U盘进入系统后手动更改分区模式，导致系统崩溃，最终只能重装系统。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210710/4215ff9a-dd8d-4fa4-bb50-d0660883da25.jpg" target="_blank"><img alt="WIN11升级全教程 并不是你的配置不够" h="384" src="https://img1.mydrivers.com/img/20210710/S4215ff9a-dd8d-4fa4-bb50-d0660883da25.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>在重装系统时，打开分区工具，进入分区界面后，点击“快速分区”，在弹出的窗口中勾选“GUID”和“对齐分区到此扇区数的整数倍”，选择4K对其，最后点击“确定”。</p>
<p>至此，基本已经解决了所有Win11升级问题，接下来就是等待下载完成，重启自动进入新系统了。至于新系统的使用情况如何，BUG多不多，笔者会在后续体验一段时间之后再告诉大家。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210710/b7aab1398857455c98b4e2159df8d810.jpg" target="_blank"><img alt="Win11升级全教程get！并不是你的配置不够" h="400" src="https://img1.mydrivers.com/img/20210710/s_b7aab1398857455c98b4e2159df8d810.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windows.htm"><i>#</i>Windows</a><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     <span>原文链接：<a href="https://diy.zol.com.cn/772/7721332.html">中关村在线</a></span>
<span>责任编辑：振亭</span>
</p>
        
</div>
            