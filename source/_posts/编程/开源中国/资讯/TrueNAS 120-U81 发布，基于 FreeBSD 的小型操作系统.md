
---
title: 'TrueNAS 12.0-U8.1 发布，基于 FreeBSD 的小型操作系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1778'
author: 开源中国
comments: false
date: Sat, 16 Apr 2022 07:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1778'
---

<div>   
<div class="content">
                                                                                            <p>TrueNAS 12.0-U8.1 现已发布。对于系统上安装了 FreeNAS 的用户，官方建议先升级到 FreeNAS 11.3-U5，然后再一键升级到 TrueNAS 12.0-U8 以保留回滚选项。虽然这是一个简单的 Web 更新，但官方建议用户等待更新系统的 zpool 功能标志，直到完成对性能和功能的验证。对于那些拥有 TrueNAS HA 系统和支持合同的人，建议联系 iXsystems 支持以安排升级。</p> 
<p>具体更新内容包括：</p> 
<p><strong>Bug</strong></p> 
<ul> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.ixsystems.com%2Fbrowse%2FNAS-114724" target="_blank">NAS-114724</a> ] - Minio 服务未从 UI 启动</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.ixsystems.com%2Fbrowse%2FNAS-115143" target="_blank">NAS-115143</a> ] - 在 Hyper-V 中通过 LSI HBA 启动挂起。</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.ixsystems.com%2Fbrowse%2FNAS-115532" target="_blank">NAS-115532</a> ] - net/netatalk3 - 修复多个 CVE</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.ixsystems.com%2Fbrowse%2FNAS-115556" target="_blank">NAS-115556</a> ] - 合并 FreeBSD SA-22:02-03 EN-22:08</li> 
</ul> 
<p><strong>Known Issues </strong></p> 
<table border="1" cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; border:1px solid black; box-sizing:inherit; color:#343a40; display:table; font-family:"Liberation Sans",sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:0.33px; margin-bottom:1rem; margin-top:1rem; orphans:2; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:919.333px; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>Key</th> 
   <th>Summary    </th> 
   <th>Workaround</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.ixsystems.com%2Fbrowse%2FNAS-113284" target="_blank">NAS-113284</a></span></span></td> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span>Samba CVE-2021-20316：Symlink race error可能允许在导出共享之外读取和修改元数据。</span></span></td> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span>不要启用 SMB1（在 TrueNAS 11.2 及更高版本中默认禁用此功能）。如果必须启用 SMB1 以实现向后兼容性，那么在 Services > SMB 配置表中添加辅助参数：<code>unix extensions = no</code>，并重新启动服务。<br> 对于 TrueNAS 13.0 之前的版本，建议仅通过 SMB2 或 NFS 导出文件系统的区域<em>，</em>而不是两者。</span></span></td> 
  </tr> 
  <tr> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fminio%2Fminio%2Fissues%2F10490" target="_blank">Minio Project：使用 docker compose 在分布式模式下出现证书错误</a></span></span></td> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span>通配符证书不适用于 Minio</span></span></td> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span>当 Minio SAN/CN 配置为空（通配符域除外）时，将 Minio 域配置重置为 localhost。</span></span></td> 
  </tr> 
  <tr> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"> </td> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span>Asigra 插件升级</span></span></td> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span><strong>运行14.2.0.2 或更早</strong>版本的 Asigra 用户需要 TrueNAS CLI 升级程序才能更新到新的插件版本。在 TrueNAS Web 界面中，打开 **Shell** 并输入<code>iocage upgrade asigra-plugin-name</code>，替换<code>asigra-plugin-name</code>为插件创建的任何唯一名称。</span></span></td> 
  </tr> 
  <tr> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.ixsystems.com%2Fbrowse%2FNAS-106992" target="_blank">NAS-106992</a></span></span></td> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span>默认情况下禁用持久 L2ARC。</span></span></td> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span>虽然基本问题已得到修复，但默认情况下仍会禁用此设置以进行额外的性能调查。要手动重新激活持久 L2ARC，请登录 TrueNAS Web 界面，转到 <strong>System ></strong> Tunables ，然后使用以下值添加新的可调参数：</span></span> 
    <ul> 
     <li>Type =<span> </span><code>sysctl</code></li> 
     <li>Variable =<span> </span><code>vfs.zfs.l2arc.rebuild_enabled</code></li> 
     <li>Value =<span> </span><code>1</code></li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"> </td> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span>TrueNAS “root”用户帐户不能是 SMB 用户。</span></span></td> 
   <td style="background-color:#ffffff; border-collapse:collapse; border-color:black; border-style:solid; border-width:1px"><span><span>这是为了提高软件安全性和在各种环境中部署的适用性而进行的有意更改。更新 SMB 配置以使用不同的用户帐户。</span></span></td> 
  </tr> 
 </tbody> 
</table> 
<p>详情查看更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.truenas.com%2Fdocs%2Freleasenotes%2Fcore%2F12.0u8.1" target="_blank">https://www.truenas.com/docs/releasenotes/core/12.0u8.1</a></p>
                                        </div>
                                      
</div>
            