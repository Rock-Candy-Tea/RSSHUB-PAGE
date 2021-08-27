
---
title: 'FISCO BCOS v2.8.0 发布，新增硬件安全模块接入能力'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4658'
author: 开源中国
comments: false
date: Fri, 27 Aug 2021 09:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4658'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:justify"><span style="background-color:#ffffff">FISCO BCOS v2.8.0 已于近日发布。</span><span style="background-color:#ffffff">此版本新增</span><span style="background-color:#ffffff">了硬件</span><span style="background-color:#ffffff">安全模块（</span><span style="background-color:#ffffff">Hardware Secure Module</span><span style="background-color:#ffffff">，简称</span><span style="background-color:#ffffff">HSM)</span><span style="background-color:#ffffff">的接入能力，保障私钥安全，提高密码运算速度</span><span style="background-color:#ffffff">。</span></p> 
<p style="text-align:justify"><span style="background-color:#ffffff">HSM</span><span style="background-color:#ffffff">是用于保障和管理强认证系统所使用的密钥，提供相关密码学操作的计算机硬件设备，在应用程序与基础设施的安全中扮演关键角色。FISCO BCOS </span><span style="background-color:#ffffff">v2.8.0</span><span style="background-color:#ffffff">以及</span><span style="background-color:#ffffff">Java SDK</span><span style="background-color:#ffffff">支持接入符合《</span><span style="background-color:#ffffff">GMT00</span><span style="background-color:#ffffff">18-2012</span><span style="background-color:#ffffff">密码设备应用接口规范》的密码卡和密码机。</span><span style="background-color:#ffffff">用户可以将国密运算委托给</span><span style="background-color:#ffffff">HSM</span><span style="background-color:#ffffff">，用</span><span style="background-color:#ffffff">HSM</span><span style="background-color:#ffffff">进行签名、验签、加解密、哈希运算等。</span></p> 
<p style="text-align:justify"><span style="background-color:#194ea0; color:#194ea0"><strong> </strong></span><span style="background-color:#ffffff; color:#194ea0"><strong> 新特性</strong></span></p> 
<ul> 
 <li> <p>新增使用硬件安全模块进行密码运算的功能</p> </li> 
 <li> <p>支持使用符合国密《GMT0018-2012密码设备应用接口规范》标准的密码机/密码卡进行SM2、SM3、SM4等算法运算，支持使用密码机内部密钥</p> </li> 
 <li> <p>新增哈希计算、签名验证、VRFproof验证相关的Precompiled合约，提供了sm3, keccak256Hash, sm2Verify, curve25519VRFVerify等方法</p> </li> 
</ul> 
<p style="text-align:justify"><span style="background-color:#194ea0; color:#194ea0"><strong> </strong></span><span style="background-color:#ffffff; color:#194ea0"><strong> </strong></span><span style="background-color:#ffffff"><span style="background-color:#ffffff; color:#194ea0"><strong>升级</strong></span></span></p> 
<ul> 
 <li> <p>升级boost版本到1.76</p> </li> 
</ul> 
<p style="text-align:justify"><span style="background-color:#194ea0; color:#194ea0"><strong> </strong></span><span style="background-color:#ffffff; color:#194ea0"><strong> 修复</strong></span></p> 
<ul> 
 <li> <p>修复节点接收非法P2P消息包异常崩溃的问题</p> </li> 
 <li> <p>修复在极端异常情况下，共识模块死锁的问题</p> </li> 
 <li> <p>修复节点通过证书解析机构名错误的问题</p> </li> 
 <li> <p>修复在ARM机器上LevelDB编译失败的问题 </p> </li> 
</ul> 
<p style="text-align:justify"><strong>代码仓库：</strong></p> 
<p style="text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFISCO-BCOS%2FFISCO-BCOS" target="_blank"><span style="color:#1e53a4">https://github.com/FISCO-BCOS/FISCO-BCOS</span></a></p> 
<p style="text-align:justify"><strong>技术文档：</strong></p> 
<p style="text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffisco-bcos-documentation.readthedocs.io%2Fzh_CN%2Flatest%2F" target="_blank"><span style="color:#1e53a4">https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/</span></a></p> 
<p style="text-align:justify"><strong>《兼容性描述》文档：</strong></p> 
<p style="text-align:justify"><span style="background-color:#ffffff">用户如需体验v2.8.0，在升级已有版本或首次搭建节点前，可参考：</span></p> 
<p style="text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffisco-bcos-documentation.readthedocs.io%2Fzh_CN%2Flatest%2Fdocs%2Fchange_log%2F2_8_0.html" target="_blank"><span style="color:#1e53a4">https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/change_log/2_8_0.html</span></a></p> 
<p style="text-align:justify"><strong>《普通版2.8.0安装》文档：</strong></p> 
<p style="text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffisco-bcos-documentation.readthedocs.io%2Fzh_CN%2Flatest%2Fdocs%2Finstallation.html" target="_blank"><span style="color:#1e53a4">https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/installation.html</span></a></p> 
<p style="text-align:justify"><strong>《构建使用硬件密码模块的国密链》文档：</strong></p> 
<p style="text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffisco-bcos-documentation.readthedocs.io%2Fzh_CN%2Flatest%2Fdocs%2Ftutorial%2Fuse_hsm.html" target="_blank"><span style="color:#1e53a4">https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/tutorial/use_hsm.html</span></a></p> 
<p style="text-align:justify"><strong>《使用基于硬件加密模块的Java SDK》文档：</strong></p> 
<p style="text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffisco-bcos-documentation.readthedocs.io%2Fzh_CN%2Flatest%2Fdocs%2Ftutorial%2Fuse_hsm_java_sdk.html" target="_blank"><span style="color:#1e53a4">https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/tutorial/use_hsm_java_sdk.html</span></a></p> 
<p style="text-align:justify"><span style="background-color:#ffffff">在开源社区的协力推动下，FISCO BCOS 在功能、性能、操作体验上不断取得突破。感谢FISCO BCOS开源社区所有成员的参与、支持，欢迎大家持续反馈意见与建议，一起建设更好的开源联盟链社区。</span></p>
                                        </div>
                                      
</div>
            