
---
title: 'LNMP 一键安装包 V1.9 正式版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1265'
author: 开源中国
comments: false
date: Tue, 14 Jun 2022 18:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1265'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:1px; margin-right:0; text-align:start">LNMP一键安装包通常在每年1月发布测试版、每年6月1日发布正式版，今年也不例外，目前1.9正式版已经发布。</p> 
<p style="color:#333333; margin-left:1px; margin-right:0; text-align:start">LNMP 一键安装包<span style="background-color:#ffffff; color:#333333">是一个用 Linux Shell 编写的可以为 CentOS/RHEL/Fedora/Debian/Ubuntu/Raspbian/Deepin/Aliyun/Amazon/Mint Linux VPS 或独立主机安装 LNMP (Nginx/MySQL/PHP)、LNMPA (Nginx/MySQL/PHP/Apache)、LAMP (Apache/MySQL/PHP) 生产环境的 Shell 程序。支持自定义 Nginx、PHP 编译参数及网站和数据库目录、支持生成 LetseEcrypt 证书、LNMP 模式支持多 PHP 版本、支持单独安装 Nginx/MySQL/MariaDB/Pureftpd 服务器，同时提供一些实用的辅助工具如：虚拟主机管理、FTP 用户管理、Nginx、MySQL/MariaDB、PHP 的升级、常用缓存组件 Redis/Xcache 等的安装、重置 MySQL root 密码、502 自动重启、日志切割、SSH 防护 DenyHosts/Fail2Ban、备份等许多实用脚本。</span></p> 
<p style="color:#333333; margin-left:1px; margin-right:0; text-align:start">LNMP一键安装包 V1.9正式版主要增加了对rocky linux 、alma linux、CentOS Stream 9及国产Linux（UOS统信、银河麒麟、华为openEuler、龙蜥Anolis OS）的支持；增加了exif、fileinfo、ldap、bz2、sodium、imap和swoole PHP模块选项，安装前可通过修改lnmp.conf中的对应选项的值为y开启或安装完成后./addons.sh 进行单独安装。增加了MySQL 5.7、8.0 二进制安装选项；增加了目前最新版的PHP 8.1支持及PHP扩展组件对8.1的支持；lnmp.conf增加了nginx模块ngx_fancyindex安装选项；lnmp管理脚本增加301选项及IPv6开启选项，泛域名SSL证书增加ZeroSSL免费SSL选项及一些安装代码优化。<br> <br> <strong>安装教程</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flnmp.org%2Finstall.html" target="_blank">https://lnmp.org/install.html</a><br> <strong>问题反馈及使用交流论坛</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbbs.vpser.net%2Fforum-25-1.html" target="_blank">https://bbs.vpser.net/forum-25-1.html</a><br> <strong>打赏捐赠</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flnmp.org%2Fdonation.html" target="_blank">https://lnmp.org/donation.html</a><br> <br> <strong>V1.9正式版更新记录</strong></p> 
<blockquote>
 增加rocky linux 和alma linux支持；
 <br> 增加PHP 8.1支持；
 <br> 增加PHP模块exif、fileinfo、ldap、bz2、sodium、imap、swoole和SourceGuardian Loader的支持安装，安装lnmp前lnmp.conf 中开启后安装lnmp或 ./addons.sh 安装以上模块；
 <br> 增加ngx_fancyindex模块，lnmp.conf中开启后，安装lnmp或升级nginx；
 <br> 增加nginx模块--with-stream_ssl_preread_module，方便使用stream ssl相关配置；
 <br> 增加UOS统信桌面家庭版、桌面专业版、服务器版支持；
 <br> 增加银河麒麟服务器操作系统和桌面系统支持；
 <br> 增加华为openEuler支持；
 <br> 增加阿里巴巴龙蜥Anolis OS支持；
 <br> 增加CentOS Stream 9支持；
 <br> 增加Alma Linux 9支持；
 <br> 增加MySQL 5.7、8.0 二进制安装和升级方式；
 <br> 增加PHP 7.4+ webp支持；
 <br> lnmp管理脚本增加HTTP 301跳转HTTPS的选项；
 <br> lnmp管理脚本增加是否启用IPv6选项；
 <br> 移除mariadb 10.1, 10.2增加mariadb 10.5, 10.6；
 <br> 泛域名SSL增加了ZeroSSL支持；
 <br> 优化AlibabaCloud支持；
 <br> 优化部分SSL添加代码；
 <br> 优化FTP用户添加部分代码；
 <br> 优化离线安装；
 <br> 优化部分EOL Linux发行版的安装；
 <br> 优化OpenSSL支持；
 <br> 优化RHEL 9系下uw-imap支持情况；
 <br> 调整MariaDB升级下载地址；
 <br> 更新诸多软件版本；
 <br> 其他一些功能优化及调整......
 <br> ......更多更新信息请访问
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flnmp.org%2Fchangelog.html" target="_blank">lnmp官网更新记录</a>查看
</blockquote> 
<p style="color:#333333; margin-left:1px; margin-right:0; text-align:start">LNMP状态管理：<strong>lnmp &#123;start|stop|reload|restart|kill|status&#125;</strong><br> LNMP各个程序的状态管理：<strong>lnmp &#123;nginx|mysql|mariadb|php-fpm|pureftpd&#125; &#123;start|stop|reload|restart|kill|status&#125;</strong><br> 虚拟主机管理：<strong>lnmp vhost &#123;add|list|del&#125;</strong><br> 数据库管理：<strong>lnmp database &#123;add|list|edit|del&#125;</strong><br> FTP用户管理：<strong>lnmp ftp &#123;add|list|edit|del|show&#125;</strong><br> 已存在虚拟主机添加SSL：<strong>lnmp ssl add</strong><br> 通过DNS API方式生成证书并创建虚拟主机：<strong>lnmp dns &#123;ali|dp|cf|he|namesilo|namecom|namecheap|porkbun|...&#125;</strong><br> 通过DNS API方式只生成SSL证书：<strong>lnmp onlyssl &#123;ali|dp|cf|he|namesilo|namecom|namecheap|porkbun|...&#125;</strong><br> <br> <strong>关于升级到当前版本</strong><br> 目前1.9版本与1.8版本编译参数、管理脚本方面相差不大，如果没有对新功能的需求可以不用升级。./upgrade1.x-1.9.sh 只升级lnmp管理脚本及一些必要的依赖包，不对整体环境升级；可以根据自己需求进行单个升级。</p> 
<p style="color:#333333; margin-left:1px; margin-right:0; text-align:start">非lnmp1.9版本如需要安装exif、fileinfo、ldap、bz2、sodium、imap和swoole这些模块，可以下载lnmp1.9安装包，使用lnmp1.9里面的 ./addons.sh 进行安装。</p> 
<p style="color:#333333; margin-left:1px; margin-right:0; text-align:start">数据库一般不建议升级，升级毕竟有风险而且可能会有兼容性问题。</p> 
<p style="color:#333333; margin-left:1px; margin-right:0; text-align:start">免费SSL：Let's Encrypt和ZeroSSL 90天有效期支持通过DNS API认证生成泛域名SSL证书，BuyPass 180天有效期不支持泛域名SSL证书。<br> <br> 添加、删除虚拟主机及伪静态管理：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flnmp.org%2Ffaq%2Flnmp-vhost-add-howto.html" target="_blank">https://lnmp.org/faq/lnmp-vhost-add-howto.html</a><br> eAccelerator，xcache，memcached，imageMagick，ionCube、opcache、redis的安装：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flnmp.org%2Ffaq%2Faddons.html" target="_blank">https://lnmp.org/faq/addons.html</a><br> <br> <strong>问题反馈及使用交流论坛</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbbs.vpser.net%2Fforum-25-1.html" target="_blank">https://bbs.vpser.net/forum-25-1.html</a></p>
                                        </div>
                                      
</div>
            