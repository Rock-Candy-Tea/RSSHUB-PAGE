
---
title: '开源项目丨 ChengYing 1.1 版本重磅发布：新增超多功能，全新优化体验！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-24d482b50d141b2495caf02a06aef1e662e.png'
author: 开源中国
comments: false
date: Tue, 13 Sep 2022 19:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-24d482b50d141b2495caf02a06aef1e662e.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">ChengYing 是一站式全自动化全生命周期大数据平台运维管家，提供大数据产品的一站式部署、运维、监控服务，其可实现产品部署、产品升级、版本回滚、扩缩节点、日志诊断、集群监控、实时告警等功能，致力于最大化节省运维成本，降低线上故障率与运维难度，为客户提供安全稳定的产品部署与监控。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">ChengYing 脱胎于袋鼠云数栈自主研发的一站式运维管家 EasyManager，承袭袋鼠云开源项目名剑家族的概念，取自十大名剑之承影剑，1.0 版本于 2022 年 5 月 30 日在 github 上线。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2022 年 9 月 13 日，ChengYing1.1 版本正式发布！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">ChengYing1.1 版本在 1.0 的版本上，对之前的 UI 做了全面升级，并新增平台管理中心，包含：备份配置、安装目录、脚本管理、集群巡检等功能；在运维中心及部署中心原有的基础上做了全面升级优化，新增超多功能，进一步提高了运维及部署能力。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次发布的 1.1 版本带来如下新亮点：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">● 普通升级</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">用户在升级组件包时自动备份数据库，回滚时能自动还原数据库，方便用户进行数据备份及运维升级回滚。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">● 平滑升级</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">实现组件包的滚动发布，可以先升级一部分应用，等测试完成后，再全部更新应用。能够减少因升级环境带来的硬件需求，方便用户运维升级、回滚应用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">● 产品线自动部署</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">产品可以根据组件包的角色信息，自动编排服务器，自动解决组件包的部署依赖问题，自动部署，大大减少了运维时间。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新版本已在 Github 与 Gitee 上线，同时使用文档也在社区推送，大家可以随时下载查阅，欢迎大家前往体验（喜欢我们的项目欢迎大家点个 Star），体验地址：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Github:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDTStack%2Fchengying" target="_blank">https://github.com/DTStack/chengying</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gitee：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dtstack_dev_0/chengying">https://gitee.com/dtstack_dev_0/chengying</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官方文档：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtstack.github.io%2Fchengying-web%2F" target="_blank">https://dtstack.github.io/chengying-web/</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">ChengYing 1.1 版本详解</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">● 整体优化</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">优化 sql 注入漏洞处理</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">优化主机下架清除历史健康检查脚本</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">优化高版本系统主机安装包解压失败</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">优化审计日志</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">优化脚本管理</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">告警恢复处于 pause 状态</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">● 运维中心</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.【服务】新增配置下发的预览功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-24d482b50d141b2495caf02a06aef1e662e.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.【诊断】新增巡检报告功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-17753d61bc24b0222c26b590e2ca5fe2a6e.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">● 部署中心</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.【组件管理】组件安装时，新增产品线级别部署。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-c5f4ae72f75101347a9201bb30c5659e73a.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.【部署组件】新增主机编排冲突校验。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-6c9e81f89bca786be94f79138051f2605fb.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3.【已部署组件】新增产品包回滚功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-5551d27302d389d8861686935ab77447227.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">4.【部署服务】新增在修改服务配置参数时，可以指定文件修改。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-dfb30bc4a2a0c6cade4be9de73d95860b73.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">5.【组件升级】新增平滑升级。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-6931480c99b56f5f03630cc77789bfe4481.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">6.【监控告警】新增点击告警仪表盘跳转 grafana 后选中 ip；grafana 规则列表批量启停。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-527e3e5976835f56f420e378f7517f07fe3.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-2603c66e8dd87c4604e0201625785f25329.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">7.【监控告警】告警模块新增搜索功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-c4e3b69080918b5ba918daeda2afe78a20f.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">● 平台管理</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.【备份配置】新增自定义备份路径目录，组件包卸载时，可以将当前组件快照移动到自定义的目录下。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-df630c2b3971d08d52abded5f74de5f6a4a.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.【脚本管理】新增脚本管理。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-b3080b02531931b5147830e84b5f907eb43.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">● 系统配置</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.【全局配置】新增全局配置页面，支持组件安装超时，自动化测试超时设置。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-4b4ad8933b3502ca621285f3d923fd010db.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2.【平台安全】新增未操作会自动登出。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-efcbc80981b3cb4f6f9e09cacb553126fb4.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3.【平台安全】新增 sm2 国密认证。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">4.【平台安全】新增初始密码强制修改，登陆错误次数锁定。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">● 用户中心</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.【部署信息下载】新增集群部署信息下载功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-e24a8d868f78ad1ca160e5926b17fa373b9.png" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">ChengYing 1.2 版本规划</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">目前 ChengYing1.1 版本已顺利发布，1.2 版本我们也正在规划中，新版本我们将会重点围绕如下关键点：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">● Hadoop 安全管理，票据自动化管理</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">● ChengYing 适配 ARM 架构</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">● ChengYing 对接 Ldap</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">除了保持产品的持续更新外，ChengYing 将持续保持每月一次开源技术直播，帮助 ChengYing 开发者们更好的使用产品，欢迎有兴趣的小伙伴们加入我们的交流社群（钉钉群：30537511），一起交流 ChengYing 的技术问题及难点，一起建设 ChengYing！</p> 
<p> </p>
                                        </div>
                                      
</div>
            