
---
title: 'PHP 开源工作流引擎 Tpflow V5.1.2 正式版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.kancloud.cn/22/90/2290f7485b3313118cad77491215a362_346x172.png'
author: 开源中国
comments: false
date: Wed, 13 Oct 2021 08:24:00 GMT
thumbnail: 'https://img.kancloud.cn/22/90/2290f7485b3313118cad77491215a362_346x172.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt src="https://img.kancloud.cn/22/90/2290f7485b3313118cad77491215a362_346x172.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">欢迎使用 Tpflow V5.1.2 工作流引擎</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#525252">TpFlow工作流引擎是一套规范化的流程管理系统，基于业务而驱动系统生命力的一套引擎。彻底释放整个信息管理系统的的活力，让系统更具可用性，智能应用型，便捷设计性。Tpflow团队致力于打造中国最优秀的PHP工作流引擎。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#525252">本次更新主要对流程事件进行更新，同时新增了工作流结束节点</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#e67e22">坚持这么多年，都在开发工作流，你还不来点个赞吗 </span><a href="https://gitee.com/ntdgg/tpflow">https://gitee.com/ntdgg/tpflow</a><span style="color:#e67e22"><a href="https://gitee.com/ntdgg/tpflow%C2%A0"> </a>支持下我们吧！</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><strong>持续开源：<span> </span><span style="background-color:#ffffff">即日起：凡在tpflow开源软件上提交BUG修复，PR（2个以上）、我们将VIP权限双手奉上，参与开源，共同进步！</span></strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong>关于5.1.2 版本更新内容</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="background-color:#ffffff; color:#333333">【优化】会签部分错误修复</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">【优化】部分细节优化</span></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong>关于5.1.1 版本更新内容</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="background-color:#ffffff; color:#333333">【优化】流程设计器重复链接问题；</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">【优化】workflow.js部分脚本问题；</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">【优化】优化设计器的部分界面；</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">【新增】流程事件管理接口；</span></li> 
 <li><span style="color:#525252">【新增】流程结束接口；</span></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#525252">特别注意：本次升级需手动增加一张数据表：</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-sql"><span style="color:#d73a49">CREATE</span> <span style="color:#d73a49">TABLE</span> <span style="color:#032f62">`t_wf_event`</span>  (
  <span style="color:#032f62">`id`</span> <span>int</span>(<span>11</span>) <span style="color:#d73a49">NOT</span> <span style="color:#005cc5">NULL</span> AUTO_INCREMENT <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'主键'</span>,
  <span style="color:#032f62">`type`</span> <span>varchar</span>(<span>50</span>) <span style="color:#d73a49">DEFAULT</span> <span style="color:#005cc5">NULL</span>,
  <span style="color:#032f62">`act`</span> <span>varchar</span>(<span>60</span>) <span style="color:#d73a49">DEFAULT</span> <span style="color:#005cc5">NULL</span>,
  <span style="color:#032f62">`code`</span> longtext <span style="color:#d73a49">DEFAULT</span> <span style="color:#005cc5">NULL</span>  <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'代码'</span>,
  <span style="color:#032f62">`uid`</span> <span>int</span>(<span>11</span>)  <span style="color:#d73a49">DEFAULT</span> <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">' 用户id'</span>,
  <span style="color:#032f62">`uptime`</span> <span>int</span>(<span>11</span>) <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">DEFAULT</span> <span style="color:#005cc5">NULL</span> <span style="color:#d73a49">COMMENT</span> <span style="color:#032f62">'更新时间'</span>,
  PRIMARY <span style="color:#d73a49">KEY</span> (<span style="color:#032f62">`id`</span>) <span style="color:#d73a49">USING</span> BTREE
) <span style="color:#d73a49">ENGINE</span>=<span style="color:#d73a49">InnoDB</span> AUTO_INCREMENT=<span>1</span> <span style="color:#d73a49">DEFAULT</span> <span style="color:#d73a49">CHARSET</span>=utf8;</code></pre> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong>关于5.1.0 版本更新内容</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="background-color:#ffffff; color:#333333">【优化】优化了流程编辑时候的Db报错；</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">【优化】优化了流程设计时候，无步骤时候的信息报错；</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">【优化】优化了部分流程设计；</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">【新增】流程删除接口；</span></li> 
 <li><span style="color:#525252">【修复】修复了demo中的数据库字段缺失；</span></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#525252">特别注意：本次升级可无缝升级到新版</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong>关于5.0.9版本更新内容</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="background-color:#ffffff; color:#333333">【优化】userData接口重新优化调整；</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">【优化】List接口新增分页调用方法；</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">【新增】tmp模板方法；</span><span style="color:#525252">-><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cojz8.com%2Farticle%2F175" target="_blank">穿越吧</a></span></li> 
 <li><span style="color:#525252">【优化】优化部分接口数据</span></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong>关于5.0.8版本更新内容</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="background-color:#ffffff; color:#333333">【界面】重新优化设计界面，新增栅格背景；</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">【优化】API数据接口；</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">【新增】协同模式；</span></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><strong>官方全新出品整合Tpflow5.1.3 Gadmin 3.0企业级低代码开发平台</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><strong>Demo网址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.gadmin8.com" target="_blank">https://www.gadmin8.com</a></strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>设计器截图：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-7a0f472047b33963e8bd6252ecb70c05d1c.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-e5551491f318923a4f4b54c995492ef6009.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">主要特性</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>基于 <code><jsPlumb></code> 可视化设计流程图 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>支持可视化界面设计</li> 
   <li>支持拖拽式流程绘制</li> 
   <li>三布局便捷调整</li> 
   <li>基于<code>workflow.5.0.js</code> <code>workflow.5.0.css </code>引擎</li> 
  </ul> </li> 
 <li>超级强大的API 对接功能 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li><code>WfDo</code> 工作流直API接口</li> 
   <li><code>designapi</code> 工作流设计器API接口</li> 
   <li><code>wfapi </code>工作流管理API接口</li> 
   <li><code>wfAccess </code>静态调用API接口</li> 
  </ul> </li> 
 <li>完善的流引擎机制 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>规范的命名空间，可拓展的集成化开发</li> 
   <li>支持 直线式、会签式、转出式、同步审批式等多格式的工作流格式</li> 
   <li>支持自定义事务驱动</li> 
   <li>支持各种ORM接口</li> 
   <li>业务驱动接口</li> 
  </ul> </li> 
 <li>提供基于 <code>Thinkphp6.0.X</code> 的样例Demo</li> 
 <li>提供完整的设计手册</li> 
</ul> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">5.0 有的新特性及功能</p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>基于<code><Entrust></code>驱动的代理模式管理模块 
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
   <li>TAB式步骤属性配置</li> 
   <li>步骤审批、步骤模式更加清晰</li> 
  </ul> </li> 
 <li>环形审批流模式 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>解决以往A发起人->B审核人->C核准人->A发起人完结 的环型审批流</li> 
  </ul> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">官方教程连接</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cojz8.com%2Farticle%2F119" target="_blank">https://www.cojz8.com/article/119</a> Tpflow3.1版本工作流设计-----教程一</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cojz8.com%2Farticle%2F120" target="_blank">https://www.cojz8.com/article/120</a> 工作流集成及API接口文档---教程二</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cojz8.com%2Farticle%2F121" target="_blank">https://www.cojz8.com/article/121</a> Tpflow工作流引擎在事务方面的表现</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cojz8.com%2Farticle%2F123" target="_blank">https://www.cojz8.com/article/123</a> 工作流类型详解---教程三</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cojz8.com%2Farticle%2F124" target="_blank">https://www.cojz8.com/article/124</a> 工作流实战教程----教程四</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">相关链接</h3> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官方博客：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.cojz8.com%2F" target="_blank">http://www.cojz8.com/</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">演示站点：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftpflow.cojz8.com%2F" target="_blank">http://tpflow.cojz8.com/</a></p>
                                        </div>
                                      
</div>
            