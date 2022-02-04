
---
title: 'Slackware 15.0​发布：历史最久且在维护的Linux发行版本'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0204/da7aa08018ea8f1.webp'
author: cnBeta
comments: false
date: Fri, 04 Feb 2022 05:06:53 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0204/da7aa08018ea8f1.webp'
---

<div>   
<strong>Slackware 14.0 于 2012 年发布，在经过了数年的等待之后 <a href="http://www.slackware.com/announce/15.0.php" target="_blank">Slackware 15.0 发行版本</a>于今天正式发布。</strong>Slackware 于 1993 年发布，是目前历史最悠久、且仍在维护的 Linux 发行版本。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0204/da7aa08018ea8f1.webp" alt="4b2kq60k.webp" referrerpolicy="no-referrer"></p><p>Slackware 15.0 在去年进入测试阶段，在发布几个候选版本之后终于在今天发布了稳定版本。考虑到和 Slackware 14.0 相隔如此长时间，因此 Slackware 15.0 引入了大量的变化。</p><p>Slackware 15.0 的开发工作继续由项目创始人 Patrick Volkerding 领导，他将 v15.0 总结为：</p><blockquote><p>我们需要放弃对纯影子密码的支持，经过多方考量之后最终选择了 PAM。我们从 ConsoleKit2 迁移到 elogind，使其更容易支持以其他初始系统为目标的软件，并使我们与 XDG 标准保持同步。</p><p>我们增加了对 PipeWire 的支持，以替代 PulseAudio，并添加了对 X11 之外的 Wayland 会话的支持。新版本抛弃了 Qt4，完全转移到 Qt5。带来了 Rust 和 Python 3。在系统中添加了许多新的库，以帮助支持所有不同的新增功能。</p><p>我们已经升级到当今最好的两个桌面环境。Xfce 4.16，一个快速、轻量级但视觉上吸引人且易于使用的桌面环境，以及KDE Plasma 5图形工作区环境，版本5.23.5（Plasma 25周年纪念版）。这也支持在Wayland或X11下运行"。</p><p>Slackware 的 pkgtools（软件包管理工具）也得到了大幅改进。我们实施了文件锁定，以防止并行安装或升级发生冲突，并尽量减少写入存储的数据量，以避免对 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a> 设备的额外写入。</p><p>我们有史以来第一次包含了一个“make_world.sh”脚本，允许从源代码自动重建整个操作系统。在整个开发周期中，我们始终将其作为优先事项推进，从而确保创建过程中不会出现故障。所有的源代码都经过了测试，并发现可以正常构建。特别感谢 nobodino 带头进行这项工作。</p></blockquote><p><strong>下载：</strong></p><p>推荐使用 Slackware64（64位）版本，可以获得尽可能好的性能。</p><p><a href="ftp://ftp.slackware.com/pub/slackware/slackware64-15.0/" target="_blank">ftp://ftp.slackware.com/pub/slackware/slackware64-15.0/</a></p><p>32 位 x86 版本可以在这里找到。</p><p><a href="ftp://ftp.slackware.com/pub/slackware/slackware-15.0/" target="_blank">ftp://ftp.slackware.com/pub/slackware/slackware-15.0/</a></p><p>如果你正在寻找一个可启动的安装程序，ISO镜像是可用的，可以写入DVD或（使用dd）到U盘。</p><p><a href="ftp://ftp.slackware.com/pub/slackware-iso/slackware64-15.0-iso" target="_blank">ftp://ftp.slackware.com:/pub/slackware-iso/slackware64-15.0-iso</a></p><p><a href="ftp://ftp.slackware.com/pub/slackware-iso/slackware-15.0-iso" target="_blank">ftp://ftp.slackware.com:/pub/slackware-iso/slackware-15.0-iso</a></p><p>如果这些网站无法访问，请看这里的官方镜像网站的列表。</p><p><a href="http://mirrors.slackware.com/" target="_blank">http://mirrors.slackware.com</a></p>   
</div>
            