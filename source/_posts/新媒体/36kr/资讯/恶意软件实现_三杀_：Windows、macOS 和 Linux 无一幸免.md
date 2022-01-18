
---
title: '恶意软件实现_三杀_：Windows、macOS 和 Linux 无一幸免'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220118/v2_b725340a78204be081c7b9f7d570f802_img_000'
author: 36kr
comments: false
date: Tue, 18 Jan 2022 13:35:59 GMT
thumbnail: 'https://img.36krcdn.com/20220118/v2_b725340a78204be081c7b9f7d570f802_img_000'
---

<div>   
<p>游戏中，“Triple Kill”通常意为“三杀”，即玩家在较短时间内连续消灭 3 个敌人的一种游戏表现。</p> 
<p>而近来，网络安全公司 Intezer 发现的一款后门恶意软件也实现了“Triple Kill”：同时攻击 Windows、macOS 和 Linux 三大操作系统，且几乎所有恶意软件扫描引擎都无法检测到它。</p> 
<h2><strong>安然无恙地“藏”了半年</strong></h2> 
<p>Intezer 将这个后门恶意软件命名为 SysJoker，由 C++ 编写，于 2021 年 12 月在一家教育机构基于 Linux 的 Web 服务器上主动攻击时才被首次发现——根据在线查毒网站 VirusTotal 发现的 C2（即 Command and Control，命令及控制）域名注册和样本，Intezer 推测早在 2021 年下半年 SysJoker 就已发起攻击，只是一直“藏”得很好。</p> 
<p>不仅 Linux，Intezer 发现 SysJoker 还有 Mach-O 和 Windows PE 版本，甚至每个版本都针对特定操作系统进行了“量身定制”，在 VirusTotal 上经 57 个不同反病毒扫描引擎检测都没有发现它的存在。</p> 
<p class="image-wrapper"><img data-img-size-val="497,256" src="https://img.36krcdn.com/20220118/v2_b725340a78204be081c7b9f7d570f802_img_000" referrerpolicy="no-referrer"></p> 
<p>对此，Intezer 将 SysJoker 定义为“针对 Windows、macOS 和 Linux 的新多平台后门”。</p> 
<h2><strong>隐秘的入侵过程</strong></h2> 
<p>据分析，SysJoker 入侵三大系统用的都是一个套路，为方便详细讲解该恶意软件的入侵过程，Intezer 以 Windows 为例。</p> 
<p>首先，为获取用户信任，SysJoker 会伪装成系统更新的一部分。一旦 SysJoker 程序被执行，它会随机休眠 90-120 秒，然后创建 C:\ProgramData\SystemData\ 目录，随后将自身复制至该目录并伪装成 igfxCUIService.exe，即<a class="project-link" data-id="3968654" data-name="英特尔" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968654" target="_blank">英特尔</a>图形通用用户界面服务。</p> 
<p>然后，SysJoker 就会通过离地攻击（Living off the Land，即LOtL）来收集 MAC 地址、用户名、物理序列号和 IP 地址等设备信息，并使用不同的临时文本文件来记录命令结果。完成使命后，这些文本文件会立即删除，存储在 JSON 对象中，编码并写入名为 microsoft_windows.dll 的文件中。</p> 
<p class="image-wrapper"><img data-img-size-val="1046,187" src="https://img.36krcdn.com/20220118/v2_824bf5f4c6794faa814045d4d1dd9416_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>SysJoker 在内存中构建的 JSON 对象</p> 
<p>为确保恶意行为持续不断，SysJoker 还会向注册表添加键值 HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run。不仅如此，SysJoker 的“反侦察”意识也很强——上述所有步骤之间，SysJoker 都会随机休眠一段时间以防被发现。</p> 
<p>在以上工作完成后，SysJoker 便会开始建立 C2 通信，通过解码从托管在 Google Drive 上的文本文件中检索到的字符串来生成其 C2。Google Drive 链接托管一个名为 domain.txt 的文本文件，该文件包含一个编码的 C2，SysJoker 将使用 CyberChef 解码 C2，并将收集到的用户信息发送到 C2 的 /api/attach 目录作为第一次握手。</p> 
<p>（更多细节可参见：https://www.intezer.com/blog/malware-analysis/new-backdoor-sysjoker/）</p> 
<p class="image-wrapper"><img data-img-size-val="895,746" src="https://img.36krcdn.com/20220118/v2_2a758d03740148dc827ab14462356929_img_000" referrerpolicy="no-referrer"></p> 
<p>据 Intezer 研究人员发现，C2 更改了 3 次，这意味着攻击者处于活动状态并正在监视受感染的设备。</p> 
<p>入侵完成后，SysJoker 可以从 C2 中接收包括 exe、cmd、 remove_reg 和 exit 在内的可执行文件（Intezer 补充道，当前版本中没能实现 remove_reg 和 exit。根据指令名称，Intezer 推测 remove_reg 和 exit 应该负责的是恶意软件的自我删除）。</p> 
<p class="image-wrapper"><img data-img-size-val="955,665" src="https://img.36krcdn.com/20220118/v2_ca86f2494b9f448c8a864e97b0623e29_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>SysJoker 与 C2 之间的通信流程</p> 
<p>最后，通过对 SysJoker 的种种细节分析，Intezer 发现该恶意软件很不寻常：</p> 
<p>代码是从头开始编写的，这在其他攻击中从未见过。最重要的是，通常在实时攻击中，很少有以前不曾发现的 Linux 恶意软件。</p> 
<p>攻击者注册了至少 4 个不同的域，并为三种不同的操作系统从头开始编写恶意软件。</p> 
<p>整个分析过程中，没有发现攻击者发送的第二阶段命令，这表明攻击是特定的。</p> 
<p>由此，Intezer 推断 SysJoker 的背后应是高级攻击者，且根据其功能，未来很可能用于间谍活动、横向移动或勒索软件攻击。</p> 
<h2><strong>如何检测并解决？</strong></h2> 
<p>虽然该恶意软件的检测目前还比较艰难，但 Intezer 还是给出了一些有效的检测方法：用内存扫描器检测内存中的 SysJoker 有效载荷，或利用检测内容在 EDR 或 SIEM 中进行搜索。</p> 
<p>如果发现系统已被入侵，可执行以下步骤：</p> 
<p>1、杀死与 SysJoker 相关的进程，删除相关的持久化机制，以及所有与 SysJoker 相关的文件；</p> 
<p>2、运行内存扫描程序，确保被入侵的设备已安全；</p> 
<p>3、调查恶意软件的初始入口点。</p> 
<p>参考链接：</p> 
<p><a href="https://www.intezer.com/blog/malware-analysis/new-backdoor-sysjoker/" _src="https://www.intezer.com/blog/malware-analysis/new-backdoor-sysjoker/">https://www.intezer.com/blog/malware-analysis/new-backdoor-sysjoker/</a></p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/3CgUe913-h6UHureGXR7XA">“CSDN”（ID:CSDNnews）</a>，整理：郑丽媛 ，36氪经授权发布。</p>  
</div>
            