
---
title: '十年开源感想，Furion v4.1.11 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0804/191119_HETj_2720166.jpg'
author: 开源中国
comments: false
date: Thu, 04 Aug 2022 17:12:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0804/191119_HETj_2720166.jpg'
---

<div>   
<div class="content">
                                                                                            <h2>坑坑坑坑</h2> 
<p>Furion 在 2022年07月25日发布 v4.0.0 版本，<strong>支持所有历史版本升级到该版本</strong>，在此之前已花费了 22 天的时间去测试，去改进。</p> 
<p><strong>万万没想到的是，大量的旧项目在这期间都选择了升级，短短一周时间 Nuget 安装量暴增了 30万，但问题也随之而来，由于使用者项目用法千奇百怪，导致一些项目升级之后无法正常运行或出现了比较严重的 Bug。</strong></p> 
<p>所以，自那天开始，终日疲于处理各种升级兼容问题，修复了近 20 个 Bug，做了诸多改进，总算实现了真正的无缝升级。</p> 
<h2>开源感想</h2> 
<p><img src="https://static.oschina.net/uploads/space/2022/0804/191119_HETj_2720166.jpg" referrerpolicy="no-referrer"></p> 
<p>自 2012年注册了 Github 之后，每一年都推出一款开源项目，持续了 10 年，在此期间见证了中国开源乃至国际开源的发展历程，感触良多。</p> 
<p>1. <strong>开源是一把双刃刀，处理得当名利双收，处理不妥道德谴责，佛系开源不痛不痒。</strong></p> 
<p>2. <strong>做开源最难的不是零到一的过程，而是持续维护的勇气。</strong></p> 
<p>3. <strong>开源如同人的脸，好坏一面便知，缺点可能会受到嘲讽批评，优点也会收获赞扬尊重。别担心，他们正在塑造更好的你。</strong></p> 
<p>4.<strong> 在国内做开源是一件很考验人的耐力活，你会在短时间内因为使用者的各种问题导致情绪复杂多变，仿佛在甲亢甲减这种现代病的边缘徘徊。</strong></p> 
<p>5. <strong>当你停止提交代码的次数越多，那么离放弃这个项目不远了。</strong></p> 
<p>还有很多很多感想，今天就略写几条~</p> 
<h2>本期更新</h2> 
<ul> 
 <li> <p><strong>新特性</strong></p> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>[新增]<span> </span><strong><code>Furion.Xunit</code><span> </span>拓展包，正式实现<span> </span><code>Xunit</code><span> </span>单元测试完整支持<span> </span><code>Furion</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/063a034edd089e88d501af4c09251611476fd238" target="_blank">063a034e</a></strong></li> 
   <li>[新增]<span> </span><code>services.AddMonitorLogging()</code><span> </span>日志监视器服务，支持非常灵活的日志操作<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/81df742b2784a18fbf4060fe30cc5151909c3cab" target="_blank">81df742</a></li> 
   <li>[新增]<span> </span><strong><code>Serve.Run(silence: true)</code><span> </span>等一系列强大的静默启动功能<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5JBSQ" target="_blank">#I5JBSQ</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5J98T" target="_blank">#I5J98T</a><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/7cced443ca1cdcb29226c71274e087ec2a6135ef" target="_blank">7cced4</a></strong></li> 
   <li>[新增]<span> </span><code>SpecificationDocumentBuilder.GetOpenApiGroups()</code><span> </span>方法获取底层的规范化接口分组信息<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/4ff03c5f8342c4d9b26fb1336cd78936ab189f5e" target="_blank">4ff03c5</a></li> 
   <li>[新增]<span> </span><code>logger.ScopeContext()</code><span> </span>配置日志上下文功能<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5JC0D" target="_blank">#I5JC0D</a></li> 
   <li>[新增]<span> </span>跨域配置<span> </span><code>CorsAccessorSettings.SignalRSupport</code><span> </span>配置选项，支持配置<span> </span><code>SignalR</code><span> </span>跨域<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5JREM" target="_blank">#I5JREM</a></li> 
   <li>[新增]<span> </span>事件总线<span> </span><code>UseUtcTimestamp</code><span> </span>选项配置，可选择使用<span> </span><code>DateTime.UtcNow</code><span> </span>还是<span> </span><code>DateTime.Now</code>，默认是<span> </span><code>DateTime.Now</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5JSEU" target="_blank">#I5JSEU</a></li> 
   <li>[新增]<span> </span>规范化文档<span> </span><code>[OperationId]</code><span> </span>配置，解决自定义<span> </span><code>Swagger UI</code><span> </span>不能正确显示路由问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5K1IB" target="_blank">#I5K1IB</a></li> 
   <li>[新增]<span> </span>远程请求<span> </span><code>IHttpDispatchProxy</code><span> </span>方式全局拦截支持多态（继承）<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5K8FS" target="_blank">#I5K8FS</a></li> 
  </ul> </li> 
 <li> <p><strong>突破性变化</strong></p> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>[新增]<span> </span><code>Furion.Xunit</code><span> </span>拓展包，正式实现<span> </span><code>Xunit</code><span> </span>单元测试完整支持<span> </span><code>Furion</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/063a034edd089e88d501af4c09251611476fd238" target="_blank">063a034e</a></li> 
   <li>[移除]<span> </span><code>Furion.Extras.DatabaseAccessor.SqlSugar</code><span> </span>拓展插件中的<span> </span><code>[SqlSugarUnitOfWork]</code><span> </span>工作单元特性，将使用通用工作单元替换，<strong><a href="https://dotnetchina.gitee.io/furion/docs/tran#92631-%E8%87%AA%E5%8A%A8%E7%AE%A1%E7%90%86">查看最新实现文档</a></strong></li> 
   <li>[移除]<span> </span><code>Inject.Create()</code><span> </span>方法，再也不需要了，框架提供了无敌强大的<span> </span><code>Serve.Run()</code><span> </span>静默启动方式<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/200848eda8c2e419c0b5be83f7768a257f3c88bd" target="_blank">200848e</a></li> 
   <li>[调整]<span> </span><code>Serve.Run</code><span> </span>的<span> </span><code>ConfigureConfiguration</code><span> </span>方法参数，由<span> </span><code>configuration => &#123;&#125;</code><span> </span>改为<span> </span><code>(environment, configuration) => &#123;&#125;</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/83c97bb5a19d6fc4e51cfe05f635675d26067d45" target="_blank">83c97bb</a></li> 
  </ul> </li> 
 <li> <p><strong>问题修复</strong></p> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>[修复]<span> </span><code>[LoggingMonitor]</code><span> </span>异常消息日志级别为<span> </span><code>Information</code><span> </span>错误问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/ab46cdf534433f45d39ce4d3ee7c71ca84707140" target="_blank">ab46cdf</a></li> 
   <li>[修复]<span> </span>新版本日志组件频繁提示文件占用问题，将文件独占锁改为共享锁<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5J3S6" target="_blank">#I5J3S6</a></li> 
   <li>[修复]<span> </span>配置数据库日志读写器为<span> </span><code>EFCore</code><span> </span>时控制台出现无限打印问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5J474" target="_blank">#I5J474</a></li> 
   <li>[修复]<span> </span><code>[LoggingMonitor]</code><span> </span>针对<span> </span><code>byte[]</code><span> </span>类型参数输出过大问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/5380f3551de69f8607ca0fc33c950103c7ed8174" target="_blank">5380f35</a></li> 
   <li>[修复]<span> </span>友好异常和规范化结果丢失了原始<span> </span><code>ErrorCode</code><span> </span>问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5IX2R" target="_blank">#I5IX2R</a></li> 
   <li>[修复]<span> </span>新版本日志组件自定义数据库读写器注入<span> </span><code>IRepository</code><span> </span>仓储导致死循环问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5IX2R" target="_blank">#I5IX2R</a></li> 
   <li>[修复]<span> </span><code>Mvc</code><span> </span>默认手动验证和<span> </span><code>Furion</code><span> </span>全局验证冲突问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/2a06c39c1d0a032bbc317e25a22c646babce2a60" target="_blank">2a06c39</a></li> 
   <li>[修复]<span> </span><code>Serve.Run()</code><span> </span>模式不支持<span> </span><code>SuperSocket</code><span> </span>第三方包问题，原生是支持的。<a href="https://gitee.com/dotnetchina/Furion/commit/186ca0a35d696f58d9e696094848a560074cdf6f" target="_blank">186ca0a</a></li> 
   <li>[修复]<span> </span><code>SignalR</code><span> </span>跨域错误问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5JREM" target="_blank">#I5JREM</a></li> 
   <li>[修复]<span> </span><code>[LoggingMonitor]</code><span> </span>将<span> </span><code>Oops.Oh</code><span> </span>和<span> </span><code>Oops.Bah</code><span> </span>记录到了错误日志中，默认应该是<span> </span><code>Information</code><span> </span>且提供可配置<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5JZ1H" target="_blank">#I5JZ1H</a></li> 
   <li>[修复]<span> </span>自定义<span> </span><code>Swagger UI</code><span> </span>之后个别<span> </span><code>UI</code><span> </span>要求必须配置<span> </span><code>operationId</code>，否则出现<span> </span><code>guid</code><span> </span>序号<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5K1IB" target="_blank">#I5K1IB</a></li> 
   <li>[修复]<span> </span>主动抛出<span> </span><code>NotFoundResult</code><span> </span>和<span> </span><code>NotFoundObjectResult</code><span> </span>无效问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5KALZ" target="_blank">#I5KALZ</a></li> 
   <li>[修复]<span> </span><code>[LoggingMonitor]</code><span> </span>解析方法参数但前端未传入时出现错误问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5KC5P" target="_blank">#I5KC5P</a></li> 
   <li>[修复]<span> </span><code>[LoggingMonitor]</code><span> </span>无法序列化<span> </span><code>IQueryable</code><span> </span>返回值问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5KJD1" target="_blank">#I5KJD1</a></li> 
   <li>[修复]<span> </span><code>[LoggingMonitor]</code><span> </span>不能记录全局验证错误问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/b44087dcc7dbe9992b8f4518e0b0cf4ed61c56bb" target="_blank">b44087d</a></li> 
   <li>[修复]<span> </span><code>[LoggingMonitor]</code><span> </span>存在注册顺序差异问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/b44087dcc7dbe9992b8f4518e0b0cf4ed61c56bb" target="_blank">b44087d</a></li> 
  </ul> </li> 
</ul>
                                        </div>
                                      
</div>
            