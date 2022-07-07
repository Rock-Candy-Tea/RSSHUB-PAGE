
---
title: 'Bacula 13.0 发布，开源备份系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2351'
author: 开源中国
comments: false
date: Thu, 07 Jul 2022 07:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2351'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Bacula 是一套开源的计算机备份系统，允许系统管理员在不同种类的计算机网络中管理计算机数据的备份、恢复和验证。管理员和操作员可以通过命令行、GUI 或 Web 界面配置系统；其后端是由 MySQL、PostgreSQL 或 SQLite 存储的信息目录。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">由于它的模块化设计，Bacula 可以从小型单机系统扩展到由位于大型网络上的数百台计算机组成的系统。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Bacula 13.0 版本日前在 Bacula 官方网站（<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.bacula.org%2F" target="_blank">www.bacula.org</a>）和 SourceForge 上发布。这是一个重要的新版本，有许多新功能和变化。虽然新功能已经过测试，但它们还没有在生产环境中运行，因此在投入生产前请仔细测试这些代码。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">兼容性</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">与以往一样，必须同时升级 Director 和 Storage 守护程序。较早的 File 守护程序应与 13.0 Director 和 Storage 守护程序兼容，因此不需要升级旧的 File 守护程序。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">13.0 及以上版本的新目录格式</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">这个版本的 Bacula 使用一个新的目录格式，Bacula 提供了一套脚本，允许从 9.x 和早期版本转换到新的 13.0 格式。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">在运行这个脚本之前，请做好备份，并注意运行该脚本（取决于你的数据库大小）可能需要一些时间。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新功能：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Kubernetes 插件</li> 
 <li>新增 Accurate 选项，只保存文件的 ACL 和元数据</li> 
 <li>支持 Windows CSV</li> 
 <li>在 Job 日志输出中对守护进程<->守护进程连接的更多日志记录</li> 
 <li>对目录对象的标签支持</li> 
 <li>在 FileSet 中支持 SHA256 和 SHA512 签名</li> 
 <li>外部 LDAP Console 认证</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">其他功能</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Windows 安装程序的 "Silent Mode"选项</li> 
 <li>在 bconsole'llist job' 输出中添加 PriorJob</li> 
 <li>在验证 TLS 证书时检查 IP SANs</li> 
 <li>在 macOS 和 Windows 中删除废弃的 sbrk</li> 
 <li>添加 bconsole.jlist 命令，从常规列表命令中获得 JSON 输出</li> 
 <li>确保 Director 将拒绝来自 FD 的目录更新</li> 
 <li>在更多的操作系统中尊重 "nodump" 标志，而不仅仅是 BSD 系统</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">主要修复内容：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复客户端初始备份时 Director 崩溃的问题</li> 
 <li>修复 .status 客户端命令的不正确输出</li> 
 <li>跳过大于 MaximumNetworkBuffer 的 XATTR</li> 
 <li>修复使用配置不当的目录启动 Director 时的死锁问题</li> 
 <li>修复由 BAT 引起的 Director 崩溃</li> 
 <li>修复关于 Director 在 Copy Jobs 和资源重命名时崩溃的问题</li> 
 <li>修复用 ACL 生成的 SQL 查询</li> 
 <li>alist: 修复内存溢出的访问</li> 
 <li>修复关于 SQLite 迁移脚本问题</li> 
 <li>快照：采用 BTRFS 5.17</li> 
 <li>快照：修复关于快照不能正确存储在目录中的问题</li> 
 <li>快照：增加对新 LVM 2.03.15 的支持</li> 
 <li>rpms：修复关于 Centos7 上未创建日志目录的问题</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">GUI：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>baculum: 修复保持原始 FileSet 选项的顺序</li> 
 <li>baculum: 修复在安全页面上测试 API 连接后清除 OAuth2 属性的问题</li> 
 <li>baculum: 修复非管理员角色的用户登录后指向默认页面的问题</li> 
 <li>baculum: 为 FreeBSD 和旧版 Debian/Ubuntu 的安装向导添加预定义的 b*json 工具路径</li> 
 <li>baculum: 修复在 PHP 8.0 上需要参数的 PHP 错误</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bacula.org%2Fbacula-release-13-0-0%2F" target="_blank">https://www.bacula.org/bacula-release-13-0-0/</a></p>
                                        </div>
                                      
</div>
            