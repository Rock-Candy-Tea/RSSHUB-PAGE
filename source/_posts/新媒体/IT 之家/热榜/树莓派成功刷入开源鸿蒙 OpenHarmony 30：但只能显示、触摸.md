
---
title: '树莓派成功刷入开源鸿蒙 OpenHarmony 3.0：但只能显示、触摸'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/11/f40203d9-7f19-49d6-90ee-a475f806007d.gif'
author: IT 之家
comments: false
date: Tue, 23 Nov 2021 11:11:05 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/11/f40203d9-7f19-49d6-90ee-a475f806007d.gif'
---

<div>   
<p data-vmark="f936"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 11 月 23 日消息，<a class="s_tag" href="https://hmos.ithome.com/" target="_blank">鸿蒙</a>技术社区今天发文称，开发者终于在树莓派 4B 上刷入 OpenHarmony 3.0 并将其运行了起来，虽然目前功能还不完整，只能实现显示和触摸两种操作，但作为第三方设备对于鸿蒙系统的支持来看具有重大意义。</p><p data-vmark="28c7"><img src="https://img.ithome.com/newsuploadfiles/2021/11/f40203d9-7f19-49d6-90ee-a475f806007d.gif" w="448" h="314" title="树莓派成功刷入开源鸿蒙 OpenHarmony 3.0：但只能显示、触摸" width="448" height="314" referrerpolicy="no-referrer"></p><p data-vmark="ae79">IT之家了解到，华为已经把鸿蒙 <a class="s_tag" href="https://hmos.ithome.com/" target="_blank">HarmonyOS</a> 的基础能力全部捐献给开放原子开源基金会，由后者整合其他参与者的贡献最终形成了 OpenAtom OpenHarmony（简称“OHOS”）的开源项目，并获得了数个厂商的支持，目前最新版本是 3.0。</p><p data-vmark="8132">开放原子开源基金会是致力于推动全球开源产业发展的非营利机构，由阿里巴巴、百度、华为、浪潮、360、腾讯、招商银行等多家龙头科技企业联合发起，于 2020 年 6 月登记成立，“立足中国、面向世界”，是我国在开源领域的首个基金会。</p><p data-vmark="6343">OpenHarmony 定位是一款面向全场景的开源分布式操作系统，各个厂家都可以平等地在“开放原子开源基金会”获得代码，根据不同的业务诉求来做产品。</p><p data-vmark="bac2">根据介绍，OpenHarmony 在传统单设备系统能力的基础上，创造性地提出了基于同一套系统能力适配多种终端形态的理念，支持多种终端设备上运行，第一个版本支持 128K-128M 设备上运行，开发者将获得模拟器、SDK 包以及 IDE 工具。</p><p data-vmark="7978"><img src="https://img.ithome.com/newsuploadfiles/2021/11/020745bc-1efe-42df-8a02-73dd79d76878.png" w="761" h="771" title="树莓派成功刷入开源鸿蒙 OpenHarmony 3.0：但只能显示、触摸" width="761" height="771" referrerpolicy="no-referrer"></p><p data-vmark="94f5">据称，这次为树莓派刷入 OHOS 的方法比较并不算太难，他直接使用了树莓派 Linux rpi-5.10.y 内核，然后通过编译 OHOS 3.0 文件系统进而补充 Linux 缺失的文件。</p><p data-vmark="5512">目前 OHOS 似乎采用内核→DRM→libdrm→wayland→weston 的模式，所以树莓派的 DRM 正常，再加上树莓派的生态比较开放，资料容易获取，所以总体来看并不算太难，只是 OHOS 的根文件系统使用的是 Toybox 对于大多数工具来说并不友好。</p><p data-vmark="0760"><img src="https://github.com/fenwii/OpenHarmony/raw/master/assets/img/architecture.png" title="树莓派成功刷入开源鸿蒙 OpenHarmony 3.0：但只能显示、触摸" referrerpolicy="no-referrer"></p><p data-vmark="8b74">树莓派 4B 配备了一颗博通 BCM2711 处理器，28nm 工艺，集成四核 A72 1.5GHz，内置 GPU 频率为 500MHz，性能比上代树莓派 3B + 提升了近 50％，搭配 1/2/4GB LPDDR4 内存、千兆网卡、蓝牙 5.0、USB 3.0 接口、microHDMI 接口。</p><p data-vmark="72be"><img src="https://img.ithome.com/newsuploadfiles/2021/11/dea6aafa-076a-4852-b593-19f5798397d1.jpg" w="700" h="500" title="树莓派成功刷入开源鸿蒙 OpenHarmony 3.0：但只能显示、触摸" width="700" height="500" referrerpolicy="no-referrer"><img src="https://img.ithome.com/newsuploadfiles/2021/11/b269ee2c-16dd-4ba1-b476-4d26701c0fe8.jpg" w="750" h="1103" title="树莓派成功刷入开源鸿蒙 OpenHarmony 3.0：但只能显示、触摸" width="750" height="1103" referrerpolicy="no-referrer"></p>
          
</div>
            