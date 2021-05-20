
---
title: '重要更新丨完成前端重构，KubeOperator 开源容器平台 v3.7.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-75167af6627d932dd76a93bf8d8294d2983.png'
author: 开源中国
comments: false
date: Thu, 20 May 2021 11:06:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-75167af6627d932dd76a93bf8d8294d2983.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">5月17日，开源容器平台KubeOperator正式发布v3.7.0版本。在这一版本中，KubeOperator使用“Vue.js+FIT2CLOUD UI”重构了前端界面，同时完成若干功能优化和Bug修复。</p> 
<h2 style="text-align:left">重构Web前端界面</h2> 
<p style="text-align:left">相比上一次发布的KubeOperator v3.6.0版本，KubeOperator项目主要是在前端产生了重要变化，用户可以通过KubeOperator v3.x版本平滑升级至v3.7.0版本。</p> 
<p style="text-align:left">在v3.7.0版本中，KubeOperator开源容器平台通过前端重构向用户交付全新的应用体验。KubeOperator上一版本前端架构于2019年启用，已经使用了两年的时间。伴随着前后端分离的重要技术趋势，以及开源项目整体发展的实际需要，FIT2CLOUD飞致云将统一其旗下所有开源项目的前端框架。</p> 
<p style="text-align:left">上一版本的前端架构采用的是“Angular+Clarity”的技术组合，应用体验与用户的实际需求存在落差，并且相关组件更新较慢，部分功能实现成本较高，无法满足项目快速演进的需要。</p> 
<p style="text-align:left"><strong><span style="color:#fc6554">KubeOperator项目组自2021年1月正式启动前端重构工作，选择的是“Vue.js+FIT2CLOUD UI”的技术路线。</span></strong>在进行技术路线选择时，在Angular和Vue.js中选择了具有更加快捷开发模式的Vue.js。</p> 
<p style="text-align:left">UI框架方面，为了满足产品战略发展的需要，研发团队对UI框架进行了统一，选择了FIT2CLOUD UI开源项目，与FIT2CLOUD的其他产品线保持一致。FIT2CLOUD UI开源项目是基于Element UI二次开发的Vue.js组件库，提供企业软件开发时常用的组件、过滤器及指令等。FIT2CLOUD UI开源项目地址为：<em>github.com/fit2cloud-ui</em>。</p> 
<p style="text-align:left">KubeOperator项目前端重构过程耗时4个月，新的前端架构对大量基础组件进行抽象，并且会在未来持续优化和改进。新的前端界面在通用组件封装、基础组件抽象等方面投入了大量资源，让用户的操作更加简单方便。</p> 
<p style="text-align:left"><img alt height="1586" src="https://oscimg.oschina.net/oscnet/up-75167af6627d932dd76a93bf8d8294d2983.png" width="2878" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">▲ 图1 KubeOperator v3.7.0版本主界面</p> 
<p style="text-align:left"><span style="color:#fc6554">■ </span>资源创建模块优化，资源之间进行关联</p> 
<p style="text-align:left">在KubeOperator v3.7.0版本中，用户创建主机时，如果没有SSH凭据可以在创建主机的过程中直接创建SSH凭据，无需返回至凭据管理栏目进行创建，极大地提升了用户体验。</p> 
<p style="text-align:left"><img alt height="1584" src="https://oscimg.oschina.net/oscnet/up-17ba7d6f9bf71f0f3a1494c5f7edaf3c42e.png" width="2878" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">▲ 图2 在KubeOperator v3.7.0版本中进行主机创建</p> 
<p style="text-align:left"><span style="color:#fc6554">■</span> 修改布局。例如项目管理，树形结构展示使得项目展现更加直观，同时可在项目管理界面进行资源授权操作。</p> 
<p style="text-align:left"><img alt height="1584" src="https://oscimg.oschina.net/oscnet/up-44c6e6b9e06a17dd4128b507add077a1e24.png" width="2878" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">▲ 图3 KubeOperator v3.7.0项目列表界面</p> 
<p style="text-align:left"><span style="color:#fc6554">■ </span>统一表格布局，支持高级搜索功能</p> 
<p style="text-align:left"><img alt height="1570" src="https://oscimg.oschina.net/oscnet/up-d808594e074aa860ad5ebe8549300f21378.png" width="2878" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">▲ 图4 KubeOperator v3.7.0主机列表界面</p> 
<p style="text-align:left"><span style="color:#fc6554">■ </span> 统一资源创建编辑页面</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-8deed32e3a1c789278feba6c4a563fc171d.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center">▲ 图5 KubeOperator v3.7.0备份账号创建页面</p> 
<h2 style="text-align:left">功能优化</h2> 
<p style="text-align:left"><span style="color:#fc6554">■ </span>Kubernetes支持v1.20.4、v1.18.18版本；</p> 
<p style="text-align:left"><span style="color:#fc6554">■ </span>Docker支持v19.03.15版本；</p> 
<p style="text-align:left"><span style="color:#fc6554">■</span> ETCD支持v3.4.14版本。</p> 
<h2 style="text-align:left">Bug修复</h2> 
<p style="text-align:left"><span style="color:#fc6554">■ </span>更新基础镜像版本，修复相关漏洞；</p> 
<p style="text-align:left"><span style="color:#fc6554">■ </span>修复创建vSphere可用区失败的问题；</p> 
<p style="text-align:left"><span style="color:#fc6554">■</span> 修复获取Project失败的问题；</p> 
<p style="text-align:left"><span style="color:#fc6554">■ </span>修复不同分辨率下监控界面Chart显示异常的问题。</p>
                                        </div>
                                      
</div>
            