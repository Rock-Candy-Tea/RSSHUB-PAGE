
---
title: 'OpenCloudOS 社区稳定版 8.6 正式发布，支持直接部署应用至生产系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3215'
author: 开源中国
comments: false
date: Wed, 21 Sep 2022 09:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3215'
---

<div>   
<div class="content">
                                                                                            <p><strong>9月15日，开源操作系统社区OpenCloudOS宣布发布第二个社区稳定版 OpenCloudOS 8.6。</strong></p> 
<p>OpenCloudOS 8.6 版本采用了更加灵活的图形安装方式，支持业务场景的自定义分区、文件系统选择，支持多种国际语言的选择，支持多种不同场景软件组的选择安装等特性，也能支持自动脚本编写自动化安装，基本覆盖服务器场景的通用需求。</p> 
<p>OpenCloudOS 8.6 基于Linux内核5.4版本自主研发设计，支持多计算架构，其稳定性、安全性、兼容性和性能等核心能力均已得到长时间充分验证。作为可靠的企业级服务器Linux发行版，用户可根据需要将OpenCloudOS 8.6直接部署应用到生产系统，降低用户的系统运营成本。</p> 
<p><strong>主要更新</strong></p> 
<p><strong>01 安全</strong></p> 
<ul> 
 <li> <p>SELinux、fapolicyd框架和用于自动解锁LUKS加密硬盘的Policy-Based Decryption（PBD）支持SAP HANA数据库管理系统。</p> </li> 
 <li> <p>fapolicyd 的软件包已升级到上游版本 1.1。在其他改进中，现在可以使用新的 rules.d/ 和 trust.d/ 目录、fagenrules 脚本以及 fapolicyd-cli 命令的新选项。</p> </li> 
 <li> <p>OpenSSH 服务器现在支持插入式配置文件。</p> </li> 
 <li> <p>pcsc-lite 软件包已重新基于上游版本 1.9.5，提供了许多增强功能和错误修复。</p> </li> 
 <li> <p>现在可以使用 semodule 命令中新添加的 --checksum 选项来验证已安装 SELinux 策略模块的版本。</p> </li> 
 <li> <p>SCAP 安全指南 (SSG) 包已重新设置为上游版本 0.1.60，OpenSCAP 包已重新设置为上游版本 1.3.6。</p> </li> 
</ul> 
<p><strong>02 动态编程语言、网络和数据库服务器</strong></p> 
<p><strong>以下组件的更新版本现在作为新的模块流提供：</strong></p> 
<ul> 
 <li> <p>PHP 8.0</p> </li> 
 <li> <p>Perl 5.32</p> </li> 
</ul> 
<p><strong>编译器等工具链升级到 GCC Toolset 11</strong>、<strong>LLVM Toolset 13.0.1</strong>、<strong>Rust Toolset 1.58.1</strong>、<strong>Go Toolset 1.17.7</strong></p> 
<ul> 
 <li> <p>GCC Toolset 11</p> </li> 
 <li> <p>LLVM Toolset 13.0.1</p> </li> 
 <li> <p>Rust Toolset 1.58.1</p> </li> 
 <li> <p>GoToolset 1.17.7</p> </li> 
</ul> 
<p><strong>03 内核</strong></p> 
<ul> 
 <li> <p>tcp free skb时的use after free问题修复, virtio length长度问题修复,  virtio-net XDP  queues问题，飞腾架构acs问题、中断分发失败等问题修复。</p> </li> 
 <li> <p>bpf支持 nettrace功能, 允许开发者通过bpf进行网络丢包原因跟踪（内核也同时回合相关的丢包跟踪点）。</p> </li> 
 <li> <p>sli主动监控功能支持，允许通过sli接口设置性能监控指标，内核在检测到性能问题后会主动告知，从而减少用户态组件的周期性监控开销。</p> </li> 
 <li> <p>cgroup thp功能支持，可以通过该功能控制一个容器内所有进程的thp使用状态，让用户以容器粒度进行thp使能。</p> </li> 
</ul> 
<p><strong>问题管理</strong></p> 
<p>OpenCloudOS的bug追踪系统：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.opencloudos.tech%2F" target="_blank">https://bugs.opencloudos.tech/</a></p> 
<p><strong>源代码</strong></p> 
<p>所有 OpenCloudOS 8 的源代码均托管在gitee：</p> 
<ul> 
 <li><a href="https://gitee.com/src-opencloudos-rpms">https://gitee.com/src-opencloudos-rpms</a></li> 
 <li><a href="https://gitee.com/src-opencloudos-modules">https://gitee.com/src-opencloudos-modules</a></li> 
</ul> 
<p><strong>下载链接</strong></p> 
<p>下载 OpenCloudOS V8.6，请访问：</p> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmirrors.opencloudos.tech%2Fopencloudos%2F" target="_blank">https://mirrors.opencloudos.tech/opencloudos/</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmirrors.tencent.com%2Fopencloudos%2F" target="_blank">https://mirrors.tencent.com/opencloudos/</a></p> </li> 
</ul> 
<p>官网地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencloudos.org%2F" target="_blank">https://www.opencloudos.org/</a></p>
                                        </div>
                                      
</div>
            