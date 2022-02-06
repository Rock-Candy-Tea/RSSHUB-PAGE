
---
title: '虚拟机不支持 TPM，无法安装 Win11？教你一招解决'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/2/6f7bc832-0015-4432-b0e1-435eb745114c.png'
author: IT 之家
comments: false
date: Sat, 05 Feb 2022 11:09:05 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/2/6f7bc832-0015-4432-b0e1-435eb745114c.png'
---

<div>   
<p data-vmark="7e7b">很多犹豫要不要升级 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Win11</a> 的朋友，会选择用虚拟机先尝试 Win11。然而，当真正用虚拟机安装 Win11 的时候，就发现出问题了 ——Win11 根本安装不上。</p><p data-vmark="aa60">之所以如此，是因为 Win11 的默认安装流程，会检测用户设备<span class="accentTextColor">是否</span><span class="accentTextColor">支持 TPM 加密</span>，而很多虚拟机软件是没有此项设置的。怎么办？这就来为大家分享无需 TPM、在虚拟机中安装 Win11 的方法吧。</p><p data-vmark="b5eb">首先，我们按照常规步骤安装，会遇到一个这台 PC 不支持 Win11 的提示界面。</p><p data-vmark="af40" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/6f7bc832-0015-4432-b0e1-435eb745114c.png" w="700" h="362" alt="Win11虚拟机 虚拟机安装Win11" title="虚拟机不支持 TPM，无法安装 Win11？教你一招解决" width="700" height="362" referrerpolicy="no-referrer"></p><p data-vmark="b09f">在这个界面中，直接按住“<span class="accentTextColor">Shift+F10</span>”，来呼出 CMD。</p><p data-vmark="33cb" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/b94be048-8f9d-405a-a45f-7766179454b6.png" w="700" h="361" alt="Win11虚拟机 虚拟机安装Win11" title="虚拟机不支持 TPM，无法安装 Win11？教你一招解决" width="700" height="361" referrerpolicy="no-referrer"></p><p data-vmark="604a">接着，在 CMD 中输入以下命令，按下回车键运行。</p><pre class="brush:javascript;toolbar:false">REG ADD HKLM\SYSTEM\Setup\LabConfig /v BypassTPMCheck /t REG_DWORD /d 1</pre><p data-vmark="f202" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/82a84ab2-cce3-47b1-931e-6f78f0c53d2b.png" w="700" h="362" alt="Win11虚拟机 虚拟机安装Win11" title="虚拟机不支持 TPM，无法安装 Win11？教你一招解决" width="700" height="362" referrerpolicy="no-referrer"></p><p data-vmark="7288">关闭 CMD 后，在重新回到安装界面，走正常的安装流程，可以发现 Win11 的安装已经可以进行下去了！</p><p data-vmark="8351" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/a0426e14-a42d-4694-b706-0fed46bdb5f5.png" w="700" h="362" alt="Win11虚拟机 虚拟机安装Win11" title="虚拟机不支持 TPM，无法安装 Win11？教你一招解决" width="700" height="362" referrerpolicy="no-referrer"></p><p data-vmark="924d">最后，按照常规步骤安装即可。</p><p data-vmark="0d2a">如果你在安装时，依然遇到 PC 不支持 Win11 的提示，可以再次开启 CMD，再次输入：</p><pre class="brush:javascript;toolbar:false ai-word-checked">REG ADD HKLM\SYSTEM\Setup\LabConfig /v BypassTPMCheck /t REG_DWORD /d 1</pre><p data-vmark="716a">直到 Win11 的安装可以顺利进行为止。</p><p data-vmark="7dd3" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/454cac66-78c0-4e84-8871-a6f7467adacd.png" w="700" h="362" alt="Win11虚拟机 虚拟机安装Win11" title="虚拟机不支持 TPM，无法安装 Win11？教你一招解决" width="700" height="362" referrerpolicy="no-referrer"></p><p data-vmark="6f82">需要注意的是，一些虚拟机软件例如 VMware，是可以支持 TPM 启动需求的，但其他一些例如 Virtualbox 则不可以。如果你的虚拟机软件不支持 TPM，就试试本文的方法吧。</p><p data-vmark="df23">实际上，这行命令的真正作用，在于关闭 Win11 安装程序对 TPM 的检查。除了虚拟机外，实机安装 Win11 如果遇到类似问题，也可以使用这个方法，有需要的朋友不妨尝试一下吧。</p>
          
</div>
            