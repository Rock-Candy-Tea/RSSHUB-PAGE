
---
title: 'Zadig V1.3.1 针对社区用户反馈的若干优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ed0c6049e45edfa924aee637591d667b677.png'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 02:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ed0c6049e45edfa924aee637591d667b677.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://oscimg.oschina.net/oscnet/up-ed0c6049e45edfa924aee637591d667b677.png" referrerpolicy="no-referrer"></p> 
<p>Zadig V1.3.1 来啦！这次版本主要针对开源社区用户的反馈做小版本的升级，足足包含 22 个问题的修复和优化。</p> 
<h4><strong>Zadig V1.3.1 Release Note</strong></h4> 
<p>工作流优化：</p> 
<ul> 
 <li> <p>工作流 webhook 触发器添加命名规范校验（@江山如此多娇）</p> </li> 
 <li> <p>工作流搜索交互体验优化（@jiangpeipei327）</p> </li> 
</ul> 
<p>云主机场景优化：</p> 
<ul> 
 <li> <p>主机名称添加命名规范校验（@江山如此多娇）</p> </li> 
 <li> <p>修复工作流任务部署步骤标识缺失的问题（@all）</p> </li> 
 <li> <p>修复删除服务时，更新环境步骤缺失的问题（@all）</p> </li> 
 <li> <p>修复 onboarding 过程，创建主机按钮无效问题（@all）</p> </li> 
</ul> 
<p>服务管理优化：</p> 
<ul> 
 <li> <p>服务名称支持项目级别唯一（@江山如此多娇）</p> </li> 
 <li> <p>修复创建 K8s Yaml 服务时，解析失败后，加载 icon 一直在 loading（@曼小魔）</p> </li> 
 <li> <p>修复 codehub 服务批量导入功能（@all）</p> </li> 
 <li> <p>导入 Helm 服务去除 dry-run 校验（@A一朝醒来已是秋）</p> </li> 
 <li> <p>创建 K8s Yaml 服务，编辑区域添加提示（@瑾言）</p> </li> 
 <li> <p>优化 K8s Yaml 校验报错信息（@wuke7126）</p> </li> 
</ul> 
<p>系统配置优化：</p> 
<ul> 
 <li> <p>镜像仓库支持集成 Harbor（@all）</p> </li> 
 <li> <p>LDAP 用户名称格式优化（@绿毛、@Gary）</p> </li> 
 <li> <p>添加默认镜像仓库交互优化（@江山如此多娇）</p> </li> 
</ul> 
<p>其他问题：</p> 
<ul> 
 <li> <p>登录页面增加系统版本号（@all）</p> </li> 
 <li> <p>切换代码平台时拥有者一栏清空的体验优化（@lesterhnu）</p> </li> 
 <li> <p>修复 docker build maven 拉依赖报错问题（@LGJ @刘小浩）</p> </li> 
 <li> <p>更新 Helm 类型的集成环境时，避免重复更新优化（@all）</p> </li> 
 <li> <p>修复华为镜像仓库 SWR 拉取不精准问题（@all）</p> </li> 
 <li> <p>修复测试统计数据不展示问题（@始于初见）</p> </li> 
 <li> <p>修复用 service 方式集成 Minio 方式报错（@就差一点点@cyberity）</p> </li> 
</ul> 
<p>更多详情请参见：https://docs.koderover.com/zadig/release-notes/v1.3.1</p> 
<h4><strong>关于 Zadig</strong></h4> 
<p>Zadig 是基于 Kubernetes 设计、研发的开源分布式持续交付 (Continuous Delivery) 产品，为开发者提供云原生运行环境，支持开发者本地联调、微服务并行构建和部署、集成测试等。Zadig 内置了面向 Kubernetes、Helm、云主机、大体量微服务等复杂业务场景的最佳实践，为工程师一键生成自动化工作流 。</p> 
<p>欢迎大家 Star、Fork、 Watch！和众多开发者一起探讨、交流，共建开源社区！</p>
                                        </div>
                                      
</div>
            