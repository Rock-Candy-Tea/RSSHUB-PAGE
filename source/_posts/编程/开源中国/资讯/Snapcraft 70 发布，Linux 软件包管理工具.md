
---
title: 'Snapcraft 7.0 发布，Linux 软件包管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6787'
author: 开源中国
comments: false
date: Thu, 26 May 2022 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6787'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px">Snapcraft 是一个用于 Linux 系统上的打包、分发与更新工具，由于绑定了依赖项，所以不需要修改就可以在所有主要 Linux 系统上运行。目前 Snapcraft 7.0 已正式发布，更新内容如下：</p> 
<h3 style="margin-left:0px">支持 core22 </h3> 
<p style="margin-left:0px">在引入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcraft-parts.readthedocs.io%2Fen%2Flatest%2F" target="_blank">craft-parts</a> 之后，对 core22 的支持进入了一个新的周期。主要有以下变更：</p> 
<ul> 
 <li>添加 craftctl 工具替换 snapcraftctl</li> 
 <li>在步骤执行期间定义 CRAFT_* 环境变量，替换 SNAPCRAFT_* 变量。</li> 
 <li>在 snapcraft.yaml 中使用重复键时出错。</li> 
 <li>不再支持根级构建包</li> 
 <li>Snapcraft 现在使用全局环境关键字而不是命令链（允许轻松覆盖）</li> 
</ul> 
<p style="margin-left:0px">请查阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.snapcraft.io%2Ft%2Fmicro-howto-migrate-from-core20-to-core22%2F30188" target="_blank">迁移指南</a>获取更多信息。</p> 
<h3 style="margin-left:0px">构建提供者</h3> 
<p style="margin-left:0px">随着转向 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcraft-providers.readthedocs.io%2Fen%2Flatest%2F" target="_blank">craft-providers</a>，Snapcraft 现在默认使用 LXD 作为构建环境。</p> 
<h3 style="margin-left:0px">使用外部生成的凭据存储操作</h3> 
<p style="margin-left:0px">Snapcraft 已迁移到使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcraft-store.readthedocs.io%2Fen%2Flatest%2F" target="_blank">craft-store</a>，因此身份验证机制也发生了变化，主要影响了那些与 CI/CD 集成的人。snapcraft login --with 命令结构不再受支持， export login 的值需要导出到相应的环境变量中（比如 <span style="color:#24292f">SNAPCRAFT_STORE_CREDENTIALS</span>）。</p> 
<h3 style="margin-left:0px">新版本缺少的功能</h3> 
<p style="margin-left:0px">注意，7.0 版本缺少如下功能，如有需要，请先不要升级：</p> 
<ul> 
 <li>架构关键字支持</li> 
 <li>自动经典快照构建支持（ORIGIN 路径和链接器加载程序设置）</li> 
 <li>插件：ROS, crystal, qmake</li> 
 <li>一些源代码处理程序：7zip、mercurial、bazaar、deb、rpm</li> 
 <li>用户定义的插件支持</li> 
</ul> 
<p> </p> 
<p>更多内容可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnapcore%2Fsnapcraft%2Freleases%2Ftag%2F7.0" target="_blank">更新公告</a>中查阅。</p>
                                        </div>
                                      
</div>
            