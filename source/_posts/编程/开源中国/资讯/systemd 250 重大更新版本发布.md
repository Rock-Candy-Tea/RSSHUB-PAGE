
---
title: 'systemd 250 重大更新版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6945'
author: 开源中国
comments: false
date: Sat, 25 Dec 2021 07:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6945'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#121212">systemd 250 正式版已发布，这是一个重大更新版本。它包含了过去半年多积累的许多新功能和改进，在发布多个候选版之后，systemd 250 终于在近日正式发布。</span></p> 
<p><strong>更新亮点</strong></p> 
<ul> 
 <li>支持加密和经过身份验证的凭据。这可以是存储在 /var/ 或系统上的 TPM2 芯片上的密钥，其中凭据将在服务启动时自动解密。还有一个名为 systemd-creds 的新工具用于处理凭据，可用于 SSL 证书、密码和其他类似数据。</li> 
 <li>扩展 GPT 可发现分区规范 (GPT Discoverable Partitions Specification)，支持 systemd 支持的大多数架构上的 root 和 /usr/ 分区，以及其他更改。</li> 
 <li>Systemd-logind 具有新的设置，可用于长按系统上的电源、重启或挂起键。如果想要控制行为，可以将长按（大于 5 秒）这些按钮配置为登录。</li> 
 <li>RestrictFileSystems= for 的新 per-service 设置用于限制服务可以根据其类型访问的文件系统。</li> 
 <li>服务还有一个新设置 RestrictNetworkInterfaces= for 用于限制对特定网络接口的服务访问。</li> 
 <li>默认的最大 inode 数已从 /dev 的 64k 增加到 1M，而 /tmp 从 400k 增加到 1M。</li> 
 <li>per-user 服务管理器现在支持与 systemd-oomd 通信以获取内存不足的终止信息。</li> 
 <li>各种 TPM 2.0 可信平台模块的支持改进。</li> 
 <li>支持使用新的 /etc/integritytab 文件在启动时激活 dm-integrity 卷。</li> 
 <li>用于信号分析仪和相机的新硬件数据库。摄像头硬件数据库会跟踪摄像头是否指向前/后以及不同类型（例如红外）</li> 
 <li>在使用 sd-boot 加载程序时添加了一个新单元 systemd-boot-update.service，以确保引导加载程序保持最新，并从 /usr 中的操作系统树信息自动传播。</li> 
 <li>更轻松地支持在运行 systemd-homed 时在系统之间迁移主目录。Systemd-homed 现在在支持的内核/文件系统上使用 UID 映射安装，其中文件现在由“nobody”内部拥有，然后通过 UID 映射安装接口映射到系统本地使用的 UID。这通过不再需要递归 chown 文件来改进系统之间的主目录迁移。</li> 
 <li>在 Fedora 最近决定这样做之后，Systemd-homed 现在默认为家庭区域使用 Btrfs Zstd 压缩。</li> 
 <li>对 LoongArch 架构的初步支持。</li> 
 <li>Systemd-journald 现在为支持的文件系统上的归档日志文件重新启用写时复制。</li> 
 <li>在 /etc/machine-info 中引入 KERNEL_INSTALL_MACHINE_ID= 支持。该值将优先于任何 /etc/machine-id 值。</li> 
 <li>支持从 /loader/credentials/*.cred 加载凭据，用于 SSH 密钥、rootfs 加密密钥、dm-integrity 密钥等凭据。这些用于非内核/initrd 特定的凭据，可加载任何内核映像。</li> 
 <li>自 Windows Vista 以来使用的 Microsoft Windows 启动数据的适当 BCD（启动配置数据）解析器。</li> 
 <li>systemd 网络生成器现在支持用于具有 IPv6 链路本地连接的 link6 网络配置。</li> 
 <li>允许使用新的“-Dlink-boot-shared=false”选项为 bootctl 和 systemd-bless-boot 静态链接构建。添加此支持是由 CentOS/RHEL 9 驱动的，CentOS/RHEL 9 具有除 bootctl/systemd-bless-boot 之外的完整 systemd 堆栈。</li> 
 <li>systemd 日志的打孔改进。</li> 
 <li>默认启用 systemd-network-generator</li> 
</ul> 
<p>详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsystemd%2Fsystemd%2Fblob%2Fmain%2FNEWS" target="_blank">https://github.com/systemd/systemd/blob/main/NEWS</a>。</p>
                                        </div>
                                      
</div>
            