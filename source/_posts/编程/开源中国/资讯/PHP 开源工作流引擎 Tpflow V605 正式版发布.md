
---
title: 'PHP 开源工作流引擎 Tpflow V6.0.5 正式版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.kancloud.cn/22/90/2290f7485b3313118cad77491215a362_346x172.png'
author: 开源中国
comments: false
date: Tue, 31 May 2022 08:29:00 GMT
thumbnail: 'https://img.kancloud.cn/22/90/2290f7485b3313118cad77491215a362_346x172.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:start"><img alt src="https://img.kancloud.cn/22/90/2290f7485b3313118cad77491215a362_346x172.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">欢迎使用 Tpflow V6.0 工作流引擎</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left"><span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#b4aea4; background-color:#ffffff; color:#525252">TpFlow 工作流引擎是一套规范化的流程管理系统，基于业务而驱动系统生命力的一套引擎。彻底释放整个信息管理系统的的活力，让系统更具可用性，智能应用型，便捷设计性。Tpflow 团队致力于打造中国最优秀的 PHP 工作流引擎。</span></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left"><strong><span data-darkreader-inline-color style="--darkreader-inline-color:#e88a36; color:#e67e22">坚持这么多年，都在开发工作流，你还不来点个赞吗 </span><a href="https://gitee.com/ntdgg/tpflow">https://gitee.com/ntdgg/tpflow</a><span data-darkreader-inline-color style="--darkreader-inline-color:#e88a36; color:#e67e22"><a href="https://gitee.com/ntdgg/tpflow%C2%A0"> </a>支持下我们吧！</span></strong></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify"><strong>V6.0.5版本更新日志：</strong></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify"><strong>1、修复用户接口信息；</strong></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify">修复了用户接口不能调用，同时将where 条件改为 数组查询条件；</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify"><strong>2、增加用户接口流程分页数据</strong></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify">将用户流程查询接口，支持分页查询，$page $limit 默认值为10条数据为一页</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify"><strong>3、增加我的流程接口</strong></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify">增加了wfMysend 我发起得流程接口，调用可以采用Api::wfMysend</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify"><strong>4、修复部分BUG</strong></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify">修复部分系统已知得BUG问题</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify"><strong>5、增加流程校验功能</strong></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify">增加流程接口连接得权限校验避免无权限用户提交审核</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify"><strong>6、版本内容优化</strong></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d3cfc9; color:#222222; margin-left:0px; margin-right:0px; text-align:justify">对部分版本细节进行优化更新</p> 
<p> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">😍 新增奖励计划</h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">Tpflow 流程引擎、SFDP 超级表单、Fkreport 三个框架引擎，我们已经开源了 5 年之久，从底层架构到设计开发，Ui 改版。随着开源的不断深入，鼓励更多用户参与开源社区的治理工作，我们深知，专业软件使用起来必然会有很多问题，鼓励用户进步，参与，改进。即日起：流之云科技成立专项资金，用于推动中国开源生态，促进开源软件进步。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">1、提交建设性 Issue 并被官方采纳的，奖励 10 元红包；</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">2、提交 BUG Issue 并提交修复 PR 的，奖励 30 元红包；</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">3、提交视频教程、文字教程的，宣传文章的，奖励 50 元红包；【需要发布到自己的自媒体平台，图文并茂】；</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">4、推广开源软件，综合活跃读评论数，大于 1000 的，奖励官方会员账号一个价值 188;</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left">5、提交第三方解决方案，整合改版第三方框架的，比如 laravel、GO 等等，奖励 1000 元红包；</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left"><strong>6.0.4 版本更新内容</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#c8c3bc; background-color:#ffffff; color:#333333">【增加】增加按钮配置自定义</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#c8c3bc; background-color:#ffffff; color:#333333">【优化】修复几项错误</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">【<span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#c8c3bc; background-color:#ffffff; color:#333333">优化】</span>调用方法</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#c8c3bc; background-color:#ffffff; color:#333333">【优化】流程抄送优化</span></p> </li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left">♨️6.0 新增得特性功能</h1> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">基于<span> </span><code><AntV X6></code><span> </span>新版图形引擎，让流程设计更加专业</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>步骤可视化拖动设计</li> 
   <li>消息步骤 处理消息逻辑实务，知晓业务等</li> 
   <li>逻辑步骤 支持多线处理步骤</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0"><code><Auto></code><span> </span>自动化执行</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>根据业务逻辑可自动化执行步骤信息</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">全新属性设计界面<span> </span><code>步骤更清晰</code><span> </span><code>设计更简单</code></p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>取消无意义得设置项</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">废弃事务模型</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>事务 SQL 在 6.0 版本后正式取消，可采用事件处理</li> 
  </ul> </li> 
</ul> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>完善的流引擎机制 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>规范的命名空间，可拓展的集成化开发</li> 
   <li>支持 直线式、会签式、转出式、同步审批式等多格式的工作流格式</li> 
   <li>支持自定义事务驱动</li> 
   <li>支持各种 ORM 接口</li> 
   <li>业务驱动接口</li> 
  </ul> </li> 
 <li>提供基于<span> </span><code>Thinkphp6.0.X</code><span> </span>的样例 Demo</li> 
 <li>提供完整的设计手册</li> 
 <li>支持 PHP8.0</li> 
</ul> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left"><span data-darkreader-inline-color style="--darkreader-inline-color:#e95849; color:#e74c3c"><strong>官方全新出品整合 Tpflow6.0.4 Gadmin 5.0 企业级低代码开发平台</strong></span></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left"><span data-darkreader-inline-color style="--darkreader-inline-color:#e95849; color:#e74c3c"><strong>Demo 网址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.gadmin8.com" target="_blank">https://www.gadmin8.com</a></strong></span></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">✈️ 技术架构图 & 产品截图</h1> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left"><img src="https://www.gadmin8.com/img/tpflow_er.jpg" referrerpolicy="no-referrer"></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left"><img src="https://www.gadmin8.com/img/tpflow_1.png" referrerpolicy="no-referrer"></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#b7b1a7; color:#40485b; margin-left:0px; margin-right:0px; text-align:left"><img src="https://www.gadmin8.com/img/tpflow_2.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">主要特性</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>基于 <code><jsPlumb></code> 可视化设计流程图 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>支持可视化界面设计</li> 
   <li>支持拖拽式流程绘制</li> 
   <li>三布局便捷调整</li> 
   <li>基于<span> </span><code>workflow.5.0.js</code> <code>workflow.5.0.css </code>引擎</li> 
  </ul> </li> 
 <li>超级强大的 API 对接功能 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li><code>WfDo</code> 工作流直 API 接口</li> 
   <li><code>designapi</code> 工作流设计器 API 接口</li> 
   <li><code>wfapi </code>工作流管理 API 接口</li> 
   <li><code>wfAccess </code>静态调用 API 接口</li> 
  </ul> </li> 
 <li>完善的流引擎机制 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>规范的命名空间，可拓展的集成化开发</li> 
   <li>支持 直线式、会签式、转出式、同步审批式等多格式的工作流格式</li> 
   <li>支持自定义事务驱动</li> 
   <li>支持各种 ORM 接口</li> 
   <li>业务驱动接口</li> 
  </ul> </li> 
 <li>提供基于 <code>Thinkphp6.0.X</code> 的样例 Demo</li> 
 <li>提供完整的设计手册</li> 
</ul> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">5.0 有的新特性及功能</p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>基于<span> </span><code><Entrust></code><span> </span>驱动的代理模式管理模块 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>可以随心调用工作流管理模式</li> 
   <li>可以代理工作流的审核审批人员</li> 
  </ul> </li> 
 <li><code><LoadClass></code> 支持自定义的业务驱动模式 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>业务办理前，办理后的的各种业务流程处理</li> 
  </ul> </li> 
 <li>全新的工作流设计界面 <code>步骤更清晰</code> <code>设计更简单</code> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>独立化步骤显示</li> 
   <li>TAB 式步骤属性配置</li> 
   <li>步骤审批、步骤模式更加清晰</li> 
  </ul> </li> 
 <li>环形审批流模式 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>解决以往 A 发起人 ->B 审核人 ->C 核准人 ->A 发起人完结 的环型审批流</li> 
  </ul> </li> 
</ul>
                                        </div>
                                      
</div>
            