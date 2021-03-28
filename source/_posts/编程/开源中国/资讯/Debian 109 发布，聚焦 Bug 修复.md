
---
title: 'Debian 10.9 发布，聚焦 Bug 修复'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8283'
author: 开源中国
comments: false
date: Sun, 28 Mar 2021 07:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8283'
---

<div>   
<div class="content">
                                                                                            <p>Debian 正式发布其稳定发行版 Debian 10（代号为buster）的第九次更新。这个版本主要增加了对安全问题的修正，以及一些严重问题的调整。</p> 
<p>本次更新内容如下：</p> 
<ul> 
 <li>avahi：删除不再需要的 avahi-daemon-check-dns 机制；</li> 
 <li>base-files ：更新 /etc/debian_version 以适应10.9点版本的需要；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Acloud-init" target="_blank">cloud-init</a>：避免将生成的密码记录到全局可读的日志文件 [CVE-2021-3429]；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Adebian-archive-keyring" target="_blank">debian-archive-keyring</a>：添加 bullseye keys; 删除 jessie keys；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Adebian-installer" target="_blank">debian-installer</a>：使用 4.19.0-16 Linux 内核 ABI；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Adebian-installer-netboot-images" target="_blank">debian-installer-netboot-images</a>：根据建议的更新进行重建；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Aexim4" target="_blank">exim4</a>：修复 GnuTLS 下并发 TLS 连接的使用；修复 CNAMEs 的 TLS 证书验证；README.Debian：记录默认配置中服务器证书验证的限制/范围；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Afetchmail" target="_blank">fetchmail</a>：在 SSL_connect() 过程中不再报告系统错误；移除 OpenSSL 版本检查；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Afwupd" target="_blank">fwupd</a>：增加 SBAT 支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Afwupd-amd64-signed" target="_blank">fwupd-amd64-signed</a>：增加 SBAT 支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Afwupd-arm64-signed" target="_blank">fwupd-arm64-signed</a>：增加 SBAT 支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Afwupd-armhf-signed" target="_blank">fwupd-armhf-signed</a>：增加 SBAT 支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Afwupd-i386-signed" target="_blank">fwupd-i386-signed</a>：增加 SBAT 支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Afwupdate" target="_blank">fwupdate</a>：增加 SBAT 支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Afwupdate-amd64-signed" target="_blank">fwupdate-amd64-signed</a>：增加 SBAT 支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Afwupdate-arm64-signed" target="_blank">fwupdate-arm64-signed</a>：增加 SBAT 支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Afwupdate-armhf-signed" target="_blank">fwupdate-armhf-signed</a>：增加 SBAT 支持；</li> 
 <li>fwupdate-i386-signed：增加 SBAT 支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Agdnsd" target="_blank">gdnsd</a>：修复 IPv6 地址过大的堆栈溢出[CVE-2019-13952]；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Ahwloc-contrib" target="_blank">hwloc-contrib</a>：启用对 ppc64el 架构的支持；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Aintel-microcode" target="_blank">intel-microcode</a>：更新各种微码；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Aiputils" target="_blank">iputils</a>：修正 ping 四舍五入错误；修正 tracepath 目标损坏；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Ajquery" target="_blank">jquery</a>：修复不受信任的代码执行漏洞[CVE-2020-11022 CVE-2020-11023]；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Alibbsd" target="_blank">libbsd</a>：修复越界读取问题 [CVE-2019-20367]；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Alibpano13" target="_blank">libpano13</a>：修复格式字符串漏洞；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Alibreoffice" target="_blank">libreoffice</a>：不会从当前的目录加载 encodings.py；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.debian.org%2FNews%2F2021%2F20210327" target="_blank">https://www.debian.org/News/2021/20210327</a></p>
                                        </div>
                                      
</div>
            