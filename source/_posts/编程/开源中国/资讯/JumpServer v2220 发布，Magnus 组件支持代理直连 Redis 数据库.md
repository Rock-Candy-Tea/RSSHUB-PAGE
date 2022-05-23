
---
title: 'JumpServer v2.22.0 发布，Magnus 组件支持代理直连 Redis 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic2.zhimg.com/80/v2-044de74e456fedcc6852d28a6668aad9_1440w.jpg'
author: 开源中国
comments: false
date: Mon, 23 May 2022 10:20:00 GMT
thumbnail: 'https://pic2.zhimg.com/80/v2-044de74e456fedcc6852d28a6668aad9_1440w.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img src="https://pic2.zhimg.com/80/v2-044de74e456fedcc6852d28a6668aad9_1440w.jpg" width="817" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">2022年5月23日，JumpServer开源堡垒机正式发布v2.22.0版本。在这一版本中，Magnus数据库连接组件新增支持代理直连Redis数据库。同时，LDAP新增支持同步用户组，目前仅支持Windows AD，这一功能极大地方便了大中型企业进行用户和用户组的同步操作。在Elasticsearch命令存储方面，支持根据日期建立索引。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">X-Pack增强包方面，在这一版本中，JumpServer支持企业微信、钉钉直接审批工单。同时，KoKo组件新增⽀持代理直连PostgreSQL数据库。云同步功能模块，新增⽀持Fusion Compute私有云资产同步。另外，这一版本还⽀持AIX系统平台的批量改密功能，以满足企业多样化系统平台的需求。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">新增功能</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>1. Magnus组件支持代理直连Redis数据库</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">在JumpServer v2.22.0版本中，Magnus组件新增支持代理直连Redis数据库。用户可以使用命令行方式连接JumpServer纳管的Redis数据库，也可以使用Redis客户端管理工具，例如RDM等图形界面化工具进行连接。目前，Magnus组件支持的数据库有MySQL、MariaDB、Redis以及PostgreSQL（X-Pack增强包内）。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">用户可通过Web终端点击Redis数据库，选择“DB Client”连接方式，获取数据库连接信息。用户可以点击“拉起客户端”按钮，直连数据库；也可以复制命令行连接信息，到Terminal执行命令去连接数据库；还可以使用数据库客户端工具（例如RedisClient、RDM等）连接数据库。</p> 
<p><img src="https://pic4.zhimg.com/80/v2-7df5660dffe3d3cd322a89414732ed27_1440w.jpg" width="2092" referrerpolicy="no-referrer"></p> 
<p>          ▲ 图1 点击客户端执行方式，拉起本地客户端连接数据库</p> 
<p><img src="https://pic3.zhimg.com/80/v2-be20e96fd902324a52ecfdd25183953e_1440w.jpg" width="2096" referrerpolicy="no-referrer"></p> 
<p>                    ▲ 图2 使用RDM工具，输入数据库连接信息</p> 
<p><img src="https://pic3.zhimg.com/80/v2-afab94911d8399bdb22cd7729698b91a_1440w.jpg" width="2344" referrerpolicy="no-referrer"></p> 
<p>             ▲ 图3 使用RDM工具成功连接数据库，并进行操作</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>2. LDAP新增支持同步用户组（Windows AD）</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">在JumpServer v2.22.0版本中，LDAP（轻型目录访问协议）新增支持同步用户组，目前仅支持Windows AD，极大地方便了大中型企业进行用户和用户组的同步操作。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">管理员在“系统设置”→“认证设置”→“LDAP”中配置好LDAP相关信息。其中，用户属性映射中需增加用户组的属性映射，例如 “groups”:"memberOf"。配置完成后，刷新LDAP用户信息，即可点击“同步”按钮。LDAP用户及用户组同步成功后，用户组会以AD开头，即：AD+原用户组名。</p> 
<p><img src="https://pic1.zhimg.com/80/v2-224e0739b532ef4e4a25b089774c36dc_1440w.jpg" width="2878" referrerpolicy="no-referrer"></p> 
<p>       ▲ 图4 管理员需配置好LDAP信息，并添加用户组映射属性</p> 
<p><img src="https://pic3.zhimg.com/80/v2-777ebf34ca7b5a0acca42372eb99ca62_1440w.jpg" width="2852" referrerpolicy="no-referrer"></p> 
<p>  ▲ 图5 用户组同步成功后，用户组名以AD开头：AD+原用户组名</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>3. Elasticsearch支持根据日期建立索引</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">在JumpServer v2.22.0版本中，Elasticsearch支持根据日期建立索引，索引名为: JumpServer填写的索引名+当天日期，以方便用户根据日期进行查询和管理。</p> 
<p><img src="https://pic4.zhimg.com/80/v2-bbc8b471107181bb16e43e1abb602b4f_1440w.jpg" width="2878" referrerpolicy="no-referrer"></p> 
<p>                  ▲ 图6 Elasticsearch支持根据日期建立索引</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>4. 支持企业微信、钉钉直接审批工单（X-Pack增强包内）</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">在JumpServer v2.22.0版本中，新增支持企业微信、钉钉直接审批工单功能。当用户的企业微信、钉钉收到工单审批消息时，如果是登录状态，则可直接审批该工单；如果是未登录状态，登录后即可再次直接审批工单。</p> 
<p><img src="https://pic2.zhimg.com/80/v2-027fbcc4b7bfd35f49f98dec962fe5d9_1440w.jpg" width="2090" referrerpolicy="no-referrer"></p> 
<p>                         ▲ 图7 企业微信收到工单审批信息</p> 
<p><img src="https://pic3.zhimg.com/80/v2-6402c301a67cb120745d06738f537fd6_1440w.jpg" width="2086" referrerpolicy="no-referrer"></p> 
<p>                                ▲ 图8 钉钉收到工单审批信息</p> 
<p><img src="https://pic2.zhimg.com/80/v2-6d746f106d465183365188d568c2c43d_1440w.jpg" width="1496" referrerpolicy="no-referrer"></p> 
<p>                         ▲ 图9 用户可直接审批该工单</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>5. KoKo组件新增⽀持代理直连PostgreSQL数据库（X-Pack增强包内）</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">JumpServer v2.21.0版本发布了Magnus组件，支持用户以数据库代理直连的方式连接数据库，用户可以使用任意数据库管理工具（例如Navicat、SQLyog等）进行直连操作。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">在JumpServer v2.22.0版本中，KoKo组件新增⽀持代理直连PostgreSQL数据库。用户可以通过Web终端，连接PostgreSQL时选择Web CLI连接方式；也可以通过Terminal终端登录JumpServer，直接连接PostgreSQL数据库。</p> 
<p><img src="https://pic3.zhimg.com/80/v2-b2f2a1057ffb976822dba8a67f71f606_1440w.jpg" width="2086" referrerpolicy="no-referrer"></p> 
<p>  ▲ 图10 通过Web终端，连接PostgreSQL时选择Web CLI连接方式</p> 
<p><img src="https://pic4.zhimg.com/80/v2-56f34b6ee919b08c2b3337fa8f847107_1440w.jpg" width="2090" referrerpolicy="no-referrer"></p> 
<p>▲ 图11 通过Terminal终端登录JumpServer，可直连PostgreSQL数据库</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>6. 新增⽀持Fusion Compute私有云资产同步（X-Pack增强包内）</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">JumpServer v2.22.0版本在云同步功能模块中，新增⽀持Fusion Compute私有云资产同步，以满足企业在多云应用方面的实际需求，方便企业用户实现对私有云、公有云资产的统一纳管。</p> 
<p><img src="https://pic4.zhimg.com/80/v2-af968916c605d2e6ee0bb34a554b2ac3_1440w.jpg" width="2870" referrerpolicy="no-referrer"></p> 
<p>              ▲ 图12 ⽀持Fusion Compute私有云资产同步</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><strong>7. ⽀持AIX系统平台的批量改密功能（X-Pack增强包内）</strong></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">在JumpServer v2.22.0版本中，⽀持AIX系统平台的批量改密功能，以满足企业多样化系统平台的需求。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">功能优化</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ ⽀持审计资源账号密码查看⽇志功能；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 优化前后端敏感信息传输时，使⽤AES（Advanced Encryption Standard，高级加密标准）进⾏加密传输；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 优化⽇志记录中登录IP城市查询不准确的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 优化⽤户Session在浏览器关闭后失效的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 优化SAML2 metadata⽂件内容及属性映射后台处理逻辑的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ OpenID认证可以选择认证⽅式，例如client_secret_basic、client_secret_post；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ ⽀持资产账号管理进⾏批量删除；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 解决Luna页⾯ESC快捷键冲突的问题，⽀持长按ESC键可退出全屏模式；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 优化通过Web GUI/CLI⽅式连接Windows、Linux资产右侧操作菜单的样式（KoKo、Lion）；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 优化开启http2（Installer）；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ ⼯单审批⼈中排除当前⼯单的申请⼈（X-Pack增强包内）；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 资产数量超过License数量限制后进⾏提⽰（X-Pack增强包内）；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 通过原⽣客户端连接Windows资产时，⽀持控制是否记录录像功能（XRDP）（X-Pack增强包内）。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">Bug修复</h2> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复Windows执⾏Ansible任务显⽰sudo命令执⾏失败的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复开源版登录后页⾯跳转的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复指定系统/组织⾓⾊获取关联⽤户失败的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复获取类型为null的命令存储⽇志中显⽰不⽀持的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复LDAP同步⽤户后，仪表盘总数没有更新的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复兼容AWS上Redis（SSL）⽆证书⽆法部署的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复未开启MFA⼆次认证时，企业微信、钉钉、飞书登录跳转的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复组织资源统计时，org为None的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复公钥情况下，通过VSCode连接Linux资产失败的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复SSH终端登录后，数据库列表不显⽰IP问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复SSH共享会话在线⼈数不准确的问题；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复⽇志级别不⽣效的问题（Magnus）；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复Kill命令执⾏不⽣效的问题（Magnus）；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复Azure MySQL⽆法认证的问题（Magnus）；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复组织管理员⽆查看系统平台权限的问题（X-Pack增强包内）；</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">■ 修复⼯单详情跳转资产授权、应⽤授权权限位判断的问题（X-Pack增强包内）。</p> 
<p> </p>
                                        </div>
                                      
</div>
            