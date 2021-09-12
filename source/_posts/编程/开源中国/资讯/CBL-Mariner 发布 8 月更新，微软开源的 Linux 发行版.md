
---
title: 'CBL-Mariner 发布 8 月更新，微软开源的 Linux 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1335'
author: 开源中国
comments: false
date: Sun, 12 Sep 2021 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1335'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>CBL-Mariner（CBL 即 Common Base Linux）是微软内部使用的 Linux 发行版，它不是桌面 Linux 而是服务器端 Linux，它被用于微软的云基础设施以及边缘产品和服务。CBL-Mariner 旨在为这些设备和服务提供一致的平台，并增强微软在 Linux 更新方面与时俱进的能力。</p> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">CBL-Mariner 的设计理念是通过提供一组小的通用核心软件包来满足云和边缘服务的普遍需求，同时允许各团队在通用核心之上根据需要引入额外的软件包。它是轻量级的发行版，只消耗非常小的磁盘和内存资源，可作为容器或容器主机使用。</p> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">CBL-Mariner 遵循“默认安全(secure-by-default)”原则，操作系统的大多数方面都以安全为重点。它包含加固内核、签名更新、ASLR、基于编译器的加固和防篡改日志等众多功能。所有 CBL-Mariner 安全功能都已罗列在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FCBL-Mariner%2Fblob%2F1.0%2Ftoolkit%2Fdocs%2Fsecurity%2Fsecurity-features.md" rel="nofollow" target="_blank">GitHub repo</a> 中。</p> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">8 月份的 1.0 更新内容有：</p> 
 <ul> 
  <li>将内核更新至 5.10.60.1 以修复 CVE</li> 
  <li>ISO 现已发布供公众下载。添加了 ISO 的下载说明</li> 
  <li>在 OpenSSL 中启用对 TLS 1 和 TLS 1.1 的支持。</li> 
  <li>将“openvswitch”更新到 2.15.1 版。</li> 
  <li>对 toolchain sources 使用 sha256sum</li> 
  <li>添加 etcd-tools</li> 
  <li>添加 cockpit</li> 
  <li>添加 <span style="color: rgb(36, 41, 47); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI Variable", "Segoe UI", system-ui, ui-sans-serif, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji"; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;">aide</span></li> 
  <li>添加 tini 包</li> 
  <li>添加 ca-certificates 文件和文件夹链接以增加兼容性</li> 
  <li>添加 fipscheck 包</li> 
  <li>添加自动软件包更新和 Dnf-Automatic</li> 
  <li>删除 brp-strip-debug-symbols 和 brp-strip-unneeded</li> 
  <li>从 ca-certificates 中删除了 ca-legacy 脚本和它的 artifacts。</li> 
  <li>从 CBL-Mariner 存储库中删除 Dotnet 和 aspnetcore SPEC 文件。这些包现在由 dotnet 团队构建，并且自 2021 年 7 月 12 日起，这些二进制文件已在 Packages.Microsoft.Com 上的新 Microsoft Repo 中提供。</li> 
  <li>修复公钥为空时的用户 ssh 目录权限</li> 
  <li>更新 nodejs 以修复 CVE</li> 
  <li>修复损坏的 openssl 手册页符号链接</li> 
  <li>修复了前几个月 mysql 升级中损坏的 mysql 包测试。</li> 
  <li>修复 perl-CPAN-Meta-Check 的测试</li> 
  <li>修复 ManualPartitionWidget 中的显示更新问题</li> 
  <li>添加补丁以修复 HyperV 中的 VDSO</li> 
  <li>修复 qt5-qtbase 版本号测试问题</li> 
  <li>移至 golang 1.16.7 并针对安全发现增加依赖项。</li> 
  <li>将 github.com/sirupsen/logrus 从 1.6.0 升级到 1.8.1</li> 
  <li>将 github.com/gdamore/tcell 从 1.3.0 升级到 1.4.0</li> 
  <li>将 gonum.org/v1/gonum 从 0.6.2 升级到 0.9.3</li> 
  <li>将 github.com/stretchr/testify 从 1.4.0 升级到 1.7.0</li> 
  <li>将 github.com/muesli/crunchy 从 0.3.0 升级到 0.4.0</li> 
  <li>将 github.com/ulikunitz/xz 从 0.5.8 升级到 0.5.10</li> 
  <li>将 github.com/ulikunitz/xz 从 0.5.7 升级到 0.5.8</li> 
  <li>更新 swig 到 4.0.2</li> 
  <li>修复 Httpd: CVE-2021-33193</li> 
  <li>修补 OpenSSL CVE-2021-3711 和 CVE-2021-3712</li> 
  <li>修复 ctags CVE-2014-7204</li> 
  <li>修复 zstd CVE-2021-24031</li> 
  <li>修复荨麻 CVE-2021-3580</li> 
  <li>修复 tpm2-tss CVE-2020-24455</li> 
  <li>修复 qemu-kvm CVE-2021-3682</li> 
  <li>修复 ruby​​ CVE-2021-32066</li> 
  <li>修复 util-linux CVE 2021-37600</li> 
  <li>将 python-psutil 更新到 5.6.7 以修复 CVE-2019-1887、CVE-2021-28957</li> 
  <li>修复 qt5-qtbase CVE-2015-9541、CVE-2020-0570 和 CVE-2020-13962</li> 
  <li>更新 python-lxml 以修复 CVE-2018-19787、CVE-2020-27783，</li> 
  <li>将 ruby​​gem-addressable 更新至 2.8.0 以修复 CVE-2021-3274</li> 
  <li>修复 glibc CVE-2021-35942</li> 
  <li>将 squashfs-tools 更新至 4.4 版以解决 CVE 2015 4646</li> 
  <li>将 python-twisted 升级到 20.3.0 以修复CVE-2020-10108、CVE-2020-10109</li> 
  <li>将 mysql 升级到 8.0.26：CVE-2021-2339、CVE-2021-2340、CVE-2021-2352、CVE-2021-2354、CVE-2021-2356、CVE-2021-2357</li> 
 </ul> 
 <p>详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FCBL-Mariner%2Freleases%2Ftag%2F1.0.20210901-1.0" rel="nofollow" target="_blank">更新说明</a>。</p> 
</div>
                                        </div>
                                      
</div>
            