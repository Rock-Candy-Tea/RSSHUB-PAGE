
---
title: '版本动态 _ DataSphere Studio 1.0.1 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6bff341ce9fd8e62d25dd0ea9a6ea1cbe33.png'
author: 开源中国
comments: false
date: Tue, 01 Mar 2022 18:46:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6bff341ce9fd8e62d25dd0ea9a6ea1cbe33.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#021eaa">DataSphere Studio简介</span></p> 
<p><span>DataSphere Studio（简称 DSS）是微众银行自研的数据应用开发管理集成框架。</span></p> 
<p><span>基于插拔式的集成框架设计，及计算中间件 Linkis ，可轻松接入上层各种数据应用系统，让数据开发变得简洁又易用。</span></p> 
<p><span>在统一的 UI 下，DataSphere Studio 以工作流式的图形化拖拽开发体验，将满足从数据交换、脱敏清洗、分析挖掘、质量检测、可视化展现、定时调度到数据输出应用等，数据应用开发全流程场景需求。</span></p> 
<p><span>DSS 通过插拔式的集成框架设计，让用户可以根据需要，简单快速替换 DSS 已集成的各种功能组件，或新增功能组件。</span></p> 
<p><span>借助于 Linkis 计算中间件的连接、复用与简化能力，DSS 天生便具备了金融级高并发、高可用、多租户隔离和资源管控等执行与调度能力。</span></p> 
<p><strong><span>GitHub</span></strong><span>：https://github.com/WeBankFinTech/DataSphereStudio</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#021eaa">已集成的数据应用组件</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:justify"><span>DSS 通过实现多个 AppConn，已集成了丰富多样的各种上层数据应用系统，基本可满足用户的数据开发需求。</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:justify"><span>已集成的组件列表如下：（最新详情见GitHub）</span></p> 
<p><img height="1414" src="https://oscimg.oschina.net/oscnet/up-6bff341ce9fd8e62d25dd0ea9a6ea1cbe33.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#021eaa">1.0.1 版本说明</span></p> 
<p><span>DSS-1.0.1版本包含所有 Project DSS-1.0.1。</span></p> 
<p><span>该版本主要包含了以下三个改进和增强：</span></p> 
<p><span>1、适配 Apache Linkis 1.0.3 版本。</span></p> 
<p><span>2、http restful api风格使用spring mvc替换jersey。</span></p> 
<p><span>3、优化全家桶一键安装部署脚本的日志打印。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#021eaa">新特性</span></p> 
<p><span>- [DSS-444] 适配 Apache Linkis 1.0.3 版本。</span></p> 
<p><span>- [DSS-445] http restful api风格使用spring mvc替换jersey。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#021eaa">功能增强</span></p> 
<p><span>-<span> </span></span><span>[DSS-448] 优化全</span><span>家桶一键安装部署脚本的日志打印。</span><span>         </span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#021eaa">BUG修复</span></p> 
<p><span>- [DSS-499] [DSS-Execution] 修改appconn引擎复用配置参数，解决appconn引擎不能复用问题。</span></p> 
<p><span>- [DSS-516] [DSS-Execution] 添加一个kill接口，解决工作流停止失败问题。</span></p> 
<p><span>- [DSS-470] [DSS-Apiservice]修改apiservcice模块引用的日志打印类，解决模块编译错误问题。</span></p> 
<p><span>- [DSS-448] [DSS-Package]更新dss应用组件ddl语句，解决组件列表数据错误问题。</span></p> 
<p><span>- [DSS-448] [DSS-AppConn] 调整AppConnEngineConnExecutor接口参数，解决工作流节点删除异常问题。</span></p> 
<p><span>- [DSS-448] [DSS-Standard] 优化SSO复用登录态的判断逻辑，解决登录不跳转问题。</span></p> 
<p><span>- [DSS-476] [DSS-workflow] 修改原接口请求参数格式，解决工作空间创建报错问题。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#021eaa">贡献者</span></p> 
<p><span>DSS 1.0.1发布离不开DSS社区的贡献者，感谢所有的社区贡献者！</span></p>
                                        </div>
                                      
</div>
            