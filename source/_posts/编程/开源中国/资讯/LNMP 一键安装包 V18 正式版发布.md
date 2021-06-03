
---
title: 'LNMP 一键安装包 V1.8 正式版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6866'
author: 开源中国
comments: false
date: Thu, 03 Jun 2021 13:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6866'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flnmp.org%2Fnotice%2Flnmp-v-1-8.html" target="_blank">LNMP一键安装包 v1.8</a>主要是增加PHP 8.0支持、增加PHP扩展组件对8.0的支持、增加Oracle Linux的支持、优化WSL支持、增加BuyPass、ZeroSSL 免费SSL证书及各种优化。<br> <br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flnmp.org%2F" target="_blank">LNMP一键安装包</a>是一个用Linux Shell编写的可以为CentOS/RHEL/Fedora/Debian/Ubuntu/Raspbian/Deepin/Aliyun/Amazon/Mint Linux VPS或独立主机安装LNMP(Nginx/MySQL/PHP)、LNMPA(Nginx/MySQL/PHP/Apache)、LAMP(Apache/MySQL/PHP)生产环境的Shell程序。支持自定义Nginx、PHP编译参数及网站和数据库目录、支持生成LetseEcrypt证书、LNMP模式支持多PHP版本、支持单独安装Nginx/MySQL/MariaDB/Pureftpd服务器，同时提供一些实用的辅助工具如：虚拟主机管理、FTP用户管理、Nginx、MySQL/MariaDB、PHP的升级、常用缓存组件Redis/Xcache等的安装、重置MySQL root密码、502自动重启、日志切割、SSH防护DenyHosts/Fail2Ban、备份等许多实用脚本。<br> <br> <strong>问题反馈及使用交流论坛</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbbs.vpser.net%2Fforum-25-1.html" target="_blank">https://bbs.vpser.net/forum-25-1.html</a><br> <strong>打赏捐赠</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flnmp.org%2Fdonation.html" target="_blank">https://lnmp.org/donation.html</a><br> <br> <strong>V1.8正式版更新记录</strong></p> 
<blockquote>
 增加PHP 8.0支持；
 <br> 增加PHP 8.0支持；
 <br> 增加Oracle Linux支持；
 <br> 增加WSL优化支持；
 <br> 增加CentOS6源自动调整；
 <br> 增加BuyPass、ZeroSSL SSL证书；
 <br> 增加php-memcache支持PHP 8.0；
 <br> 增加imagick支持PHP 8.0；
 <br> 增加apcu支持PHP 8.0；
 <br> 优化时间同步；
 <br> 优化Aliyunx Linux优化；
 <br> 优化sudo下添加虚拟主机SSL；
 <br> 优化CentOS8 Stream支持；
 <br> 优化PHP下载；
 <br> 更新诸多软件版本；
 <br> 其他一些功能优化及调整......
 <br> ......更多更新信息请访问
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flnmp.org%2Fchangelog.html" target="_blank">lnmp官网更新记录</a>查看
</blockquote> 
<p>LNMP状态管理：<strong>lnmp &#123;start|stop|reload|restart|kill|status&#125;</strong><br> LNMP各个程序的状态管理：<strong>lnmp &#123;nginx|mysql|mariadb|php-fpm|pureftpd&#125; &#123;start|stop|reload|restart|kill|status&#125;</strong><br> 虚拟主机管理：<strong>lnmp vhost &#123;add|list|del&#125;</strong><br> 数据库管理：<strong>lnmp database &#123;add|list|edit|del&#125;</strong><br> FTP用户管理：<strong>lnmp ftp &#123;add|list|edit|del|show&#125;</strong><br> 已存在虚拟主机添加SSL：<strong>lnmp ssl add</strong><br> 通过DNS API方式生成证书并创建虚拟主机：<strong>lnmp dns &#123;cx|dp|ali|...&#125;</strong><br> 只通过DNS API方式生成SSL证书：<strong>lnmp onlyssl &#123;cx|dp|ali|...&#125;</strong><br> <br> <strong>关于升级到当前版本</strong><br> 目前1.8版本与1.7版本编译参数、管理脚本方面相差很小。一般只需要 upgrade1.x-1.8.sh 升级一下管理脚本；<br> 对于新增的BuyPass、ZeroSSL SSL证书，也是和之前一样在Let's Encrypt的同级菜单里按数字选择，两者区别不大，BuyPass 180天有效期，ZeroSSL 90天有效期，据我自己测试情况来看BuyPass要求较高有时候会因为莫名其妙的原因失败。<br> <br> 添加、删除虚拟主机及伪静态管理：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flnmp.org%2Ffaq%2Flnmp-vhost-add-howto.html" target="_blank">https://lnmp.org/faq/lnmp-vhost-add-howto.html</a><br> eAccelerator，xcache，memcached，imageMagick，ionCube、opcache、redis的安装：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flnmp.org%2Ffaq%2Faddons.html" target="_blank">https://lnmp.org/faq/addons.html</a><br> <br> <strong>问题反馈及使用交流论坛</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbbs.vpser.net%2Fforum-25-1.html" target="_blank">https://bbs.vpser.net/forum-25-1.html</a></p>
                                        </div>
                                      
</div>
            