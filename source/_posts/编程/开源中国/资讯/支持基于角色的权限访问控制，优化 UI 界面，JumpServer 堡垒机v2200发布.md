
---
title: '支持基于角色的权限访问控制，优化 UI 界面，JumpServer 堡垒机v2.20.0发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4a6034684870d7e0b8c60224f07dcf4f0bd.png'
author: 开源中国
comments: false
date: Mon, 21 Mar 2022 05:46:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4a6034684870d7e0b8c60224f07dcf4f0bd.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-4a6034684870d7e0b8c60224f07dcf4f0bd.png" width="1138" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">2022年3月18日，JumpServer开源堡垒机正式发布v2.20.0版本。在这一版本中，JumpServer新增支持基于角色的权限访问控制（Role-Based Access Control，即RBAC）。通过用户关联角色、角色关联权限的方法来间接地赋予用户权限，从而方便进行权限管理。同时，在这一版本中，JumpServer的UI界面进行了重要优化，我们将视图划分为：控制台、审计台和工作台，进一步提升了用户的使用体验。</p> 
<p style="margin-left:0; margin-right:0">另外，在录像存储方面，JumpServer除了支持Amazon S3、Ceph、Swift、阿里云OSS、Azure、华为云OBS以外，新增支持腾讯云对象存储（COS），进一步满足了用户的使用需求。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">1. 支持基于角色的权限访问控制（RBAC）</span></strong></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.20.0版本中，新增支持基于角色的权限访问控制（Role-Based Access Control，即RBAC）。在用户与权限之间添加角色层，权限与角色相关联，用户可以通过与角色绑定赋予该角色权限，从而方便进行权限管理。</p> 
<p><span><img alt height="718" src="https://oscimg.oschina.net/oscnet/up-68a35ac4a33271abd22e7ffeff95702c5cb.png" width="1570" referrerpolicy="no-referrer"></span></p> 
<p><span>                                    ▲ 图1 用户、角色与权限的关系</span></p> 
<p style="margin-left:0; margin-right:0"><span>基于角色的权限访问控制在JumpServer社区版和企业版中具有一定的区别：</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> <strong>JumpServer社区版</strong></span></p> 
<p style="margin-left:0; margin-right:0"><span>JumpServer社区版的角色列表是系统角色列表。默认保留原有的三种系统角色：系统管理员、系统审计员和用户，兼容用户旧版本的角色体系，同时支持系统管理员自定义角色。</span></p> 
<p style="margin-left:0; margin-right:0"><span>系统管理员可以通过选择“用户管理”→“角色列表”→“系统角色”，创建一个自定义系统角色。进入详情页即可赋予该角色权限，并授权给用户，用户则拥有该角色的权限。</span></p> 
<p><img alt height="605" src="https://oscimg.oschina.net/oscnet/up-f35da332fd7c05fa2f9289021994567289c.png" width="1930" referrerpolicy="no-referrer"></p> 
<p><span>▲ 图2 在JumpServer社区版中选择“用户管理”→ “角色列表”→ “系统角色”，创建自定义系统角色</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> <strong>JumpServer企业版（X-Pack增强包内）</strong></span></p> 
<p style="margin-left:0; margin-right:0"><span>在X-Pack增强包内，JumpServer的角色列表包含系统角色列表和组织角色列表。在社区版的基础上，企业版保留了默认的系统角色，同时也保留了默认的组织角色，即组织管理员、组织审计员、组织用户，兼容用户旧版本的组织角色体系。同时企业版不仅支持自定义系统角色，还支持自定义组织角色。</span></p> 
<p style="margin-left:0; margin-right:0"><span>在自定义系统角色方面，系统管理员可以通过选择“用户管理”→“角色列表”→“系统角色”，创建一个自定义的系统角色。进入详情页即可赋予该角色权限，并授权给用户，用户即可拥有该角色的权限。企业版系统角色的授权用户，可以切换至任意组织，操作其有权限的功能模块。</span></p> 
<p><img alt height="665" src="https://oscimg.oschina.net/oscnet/up-cb7f13679c86dc30e7395262f0f350bfe49.png" width="2073" referrerpolicy="no-referrer"></p> 
<p><span>▲ 图3 在JumpServer企业版中选择“用户管理”→ “角色列表”→ “系统角色”中，创建自定义系统角色</span></p> 
<p style="margin-left:0; margin-right:0"><span>自定义组织角色方面，系统管理员可以通过选择“用户管理”→“角色列表”→“组织角色”，创建一个自定义组织角色。进入详情页即可赋予该角色权限，切换组织，并授权给组织用户，组织用户则拥有该角色的权限。用户可以在该组织操作其拥有权限的模块功能。</span></p> 
<p><img alt height="582" src="https://oscimg.oschina.net/oscnet/up-edee0e6a3cbd291b8988202e9eaca2ba063.png" width="1925" referrerpolicy="no-referrer"></p> 
<p>▲ 图4 在JumpServer企业版中选择“用户管理”→ “角色列表”→ “组织角色”，创建自定义组织角色</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1083" src="https://oscimg.oschina.net/oscnet/up-e6fc188f87b4924b5109edffc5a9edacdd1.png" width="2062" referrerpolicy="no-referrer"></p> 
<p>                            ▲ 图5 在自定义系统角色详情页中，赋予角色权限</p> 
<p style="margin-left:0; margin-right:0"><img alt height="852" src="https://oscimg.oschina.net/oscnet/up-d35778aa3cd95b407e3307b18378e1d835b.png" width="1930" referrerpolicy="no-referrer"></p> 
<p>                                 ▲ 图6 自定义系统角色详情页中，添加授权用户</p> 
<p style="margin-left:0; margin-right:0"><img alt height="948" src="https://oscimg.oschina.net/oscnet/up-ec08e6704dcf1150cbf02e2d7a9d6370bdd.png" width="1983" referrerpolicy="no-referrer"></p> 
<p><span>                                   ▲ 图7 授权用户登录，可以看到其有权限的模块</span></p> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#28937c"><strong><span>2. 新增支持腾讯云对象存储（COS）</span></strong></span></p> 
<p style="margin-left:0; margin-right:0"><span>在JumpServer v2.20.0版本中，新增支持腾讯云对象存储（COS）。目前，JumpServer支持的对象存储有Amazon S3、Ceph、Swift、阿里云OSS、Azure、华为云OBS和腾讯云COS，满足了更多用户的使用需求。</span></p> 
<p style="margin-left:0; margin-right:0"><span>系统管理员可以选择“系统设置”→ “终端设置”→ “录像存储”，创建COS对象存储进行使用。</span></p> 
<p style="margin-left:0; margin-right:0"><span><img alt height="754" src="https://oscimg.oschina.net/oscnet/up-eb438c3f169774c209c4308c7e2d509c19f.png" width="1851" referrerpolicy="no-referrer"></span></p> 
<p><span>                 ▲ 图8 选择“系统设置”→ “终端设置”→ “录像存储”，创建COS对象存储</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c"><strong><span>3. UI界面重要优化</span></strong></span></p> 
<p style="margin-left:0; margin-right:0"><span>在JumpServer v2.20.0版本中，我们对UI界面进行了重要优化，将视图划分为：控制台、审计台和工作台，进一步提升了用户的使用体验。</span></p> 
<p><img alt height="1216" src="https://oscimg.oschina.net/oscnet/up-fdd44ed22434d14da2b0f0f50a52e496329.png" width="1842" referrerpolicy="no-referrer"></p> 
<p>                                              ▲ 图9 新版JumpServer控制台视图</p> 
<p style="margin-left:0; margin-right:0"> <img alt height="1214" src="https://oscimg.oschina.net/oscnet/up-ac91c118a41d7962f87884bf206891a33a2.png" width="1843" referrerpolicy="no-referrer"></p> 
<p>                                          ▲ 图10 新版JumpServer审计台视图</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1216" src="https://oscimg.oschina.net/oscnet/up-43f38179b2fb08212cba1e5fbf7be86bd10.png" width="1851" referrerpolicy="no-referrer"></p> 
<p>                                         ▲ 图11 新版JumpServer工作台视图</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1215" src="https://oscimg.oschina.net/oscnet/up-9c2413a39e97a838d8921d263432b83be77.png" width="1850" referrerpolicy="no-referrer"></p> 
<p><span>                                          ▲ 图12 新版JumpServer系统设置视图</span></p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 优化资产授权创建时，默认选中点击的资产和节点的问题；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 优化命令过滤器关联的系统用户包含RDP/VNC协议的问题 ；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 优化命令过滤器关联的应用不包含Kubernetes的问题；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 优化通过XRDP连接的Windows资产默认全屏打开的问题（X-Pack增强包内）。</span></p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 修复通过手动登录的系统用户登录失败的问题；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 修复用户页面点击资产树节点，提示“对象找不到”的问题；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 修复通过API创建节点不能指定ID的问题；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 修复Keycloak配置转换为OpenID不生效的问题；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 修复资产账号列表点击更新时，弹窗不出现的问题；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 修复AWS未立即释放的实例获取私有IP失败的问题（X-Pack增强包内）；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 修复云管中心同步任务详情时，同步实例状态不准确的问题（X-Pack增强包内）；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 修复改密计划执行显示失败，实际已经修改成功的问题（安全模式关闭的情况下）（X-Pack增强包内）；</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> 修复XRDP会话录像记录时间显示不准确的问题（X-Pack增强包内）。</span></p>
                                        </div>
                                      
</div>
            