
---
title: '.NET 6 刚刚预览版，你却 _躺平_了？Furion v2.8.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
author: 开源中国
comments: false
date: Tue, 08 Jun 2021 17:16:00 GMT
thumbnail: 'https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:center"><img height="80" src="https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/furionlogo.png" width="127" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <p style="text-align:center"><a href="https://gitee.com/dotnetchina/Furion/stargazers"><img alt="star" src="https://gitee.com/dotnetchina/Furion/badge/star.svg?theme=gvp" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina/Furion/members"><img alt="fork" src="https://gitee.com/dotnetchina/Furion/badge/fork.svg?theme=gvp" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fstargazers" target="_blank"><img alt="GitHub stars" src="https://img.shields.io/github/stars/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fnetwork" target="_blank"><img alt="GitHub forks" src="https://img.shields.io/github/forks/MonkSoul/Furion?logo=github" referrerpolicy="no-referrer"></a> <a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/badge/license-Apache2-yellow" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/Furion.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a></p> 
</div> 
<div style="text-align:left"> 
 <p style="text-align:center">让 .NET 开发更简单，更通用，更流行。</p> 
</div> 
<h2>框架特点</h2> 
<ul> 
 <li><strong>全新面貌</strong>：基于 <code>.NET5/6</code> 平台，没有历史包袱</li> 
 <li><strong>极易入门</strong>：只需要一个 <code>Inject()</code> 即可完成配置</li> 
 <li><strong>极速开发</strong>：内置丰富的企业应用开发功能</li> 
 <li><strong>极少依赖</strong>：框架只依赖两个第三方包</li> 
 <li><strong>极其灵活</strong>：轻松面对多变复杂的需求</li> 
 <li><strong>极易维护</strong>：采用独特的架构思想，只为长久维护设计</li> 
 <li><strong>完整文档</strong>：提供完善的开发文档</li> 
</ul> 
<h2>功能模块</h2> 
<p><img src="https://gitee.com/dotnetchina/Furion/raw/master/handbook/static/img/functions.png" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<ul> 
 <li> <p><strong>新特性</strong></p> 
  <ul> 
   <li>[新增] <code>Db.GetMSRepository()</code> 获取主从库仓储静态方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I3UBSJ">#I3UBSJ</a></li> 
   <li>[新增] 工作单元特性，支持静态类强制性开启共享事务 <a href="https://gitee.com/dotnetchina/Furion/issues/I3S9N8">#I3S9N8</a></li> 
   <li>[新增] <code>EFCore</code> 执行 <code>sql</code> 模式打印日志 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SE8X">#I3SE8X</a></li> 
   <li>[新增] 远程请求支持默认 <code>HttpClient</code> 配置 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SI17">#I3SI17</a></li> 
   <li>[新增] 新增 <code>短 ID</code> 生成功能 <a href="https://gitee.com/dotnetchina/Furion/issues/I3T7JP">#I3T7JP</a></li> 
   <li>[新增] <code>[SensitiveDetection]</code> 支持配置替换敏感词汇 <a href="https://gitee.com/dotnetchina/Furion/issues/I3THIA">#I3THIA</a></li> 
   <li>[新增] <code>SpecificationDocumentBuilder.DocumentGroups</code> 和 <code>SpecificationDocumentBuilder.CheckApiDescriptionInCurrentGroup(currentGroup, apiDescription)</code> 公开方法<a href="https://gitee.com/dotnetchina/Furion/issues/I3UDSY">#I3UDSY</a></li> 
  </ul> </li> 
 <li> <p><strong>突破性变化</strong></p> 
  <ul> 
   <li>[重构] 自动扫描 <code>.json</code> 和 <code>.xml</code> 文件并加载到配置中的代码和规则，同时移除默认 <code>.xml</code> 文件加载，只保留 <code>.json</code> 文件 <a href="https://gitee.com/dotnetchina/Furion/issues/I3UJ3L">#I3UJ3L</a></li> 
   <li>[重构] 分布式连续 <code>GUID</code> 代码 <a href="https://gitee.com/dotnetchina/Furion/issues/I3UBK0">#I3UBK0</a></li> 
   <li>[调整] <strong><code>Scoped.CreateUnitOfWork</code> 名称为 <code>Scoped.CreateUow</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3SJPU">#I3SJPU</a></strong></li> 
   <li>[调整] <code>JWTEncryption.Validate</code> 返回值，支持返回 <code>TokenValidationResult</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I3S2ND">#I3S2ND</a></li> 
  </ul> </li> 
 <li> <p><strong>问题修复</strong></p> 
  <ul> 
   <li>[修复] <code>[DataValidation]</code> 和 <code>[SensitiveDetection]</code> 多语言应用失效 <a href="https://gitee.com/dotnetchina/Furion/issues/I3UH6U">#I3UH6U</a></li> 
   <li>[修复] <code>Scoped</code> 系列方法异步出现 <code>Task is cancel</code> 情况 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SJF6">#I3SJF6</a></li> 
   <li>[修复] <code>Mysql</code> 数据库的 <code>ToPagedList</code> 方法返回的结果进行遍历出现 <code>MySqlConnection is aleady use</code> 问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SJQ3">#I3SJQ3</a></li> 
   <li>[修复] <code>tool/cli.psl</code> 没有包含项目名称 <a href="https://gitee.com/dotnetchina/Furion/issues/I3S1T6">#I3S1T6</a></li> 
   <li>[修复] 远程请求做上传文件时，没有传入 <code>Body</code>，程序直接跳过 <a href="https://gitee.com/dotnetchina/Furion/issues/I3TKFH">#I3TKFH</a></li> 
   <li>[修复] 远程请求 <code>multipart/form-data</code> 内容分割符缺失 <a href="https://gitee.com/dotnetchina/Furion/issues/I3TNO9">#I3TNO9</a></li> 
  </ul> </li> 
 <li> <p><strong>其他更改</strong></p> 
  <ul> 
   <li>[改进] 支持规范化结果中间件判断是否跳过规范化结果 <a href="https://gitee.com/dotnetchina/Furion/issues/I3T2AA">#I3T2AA</a></li> 
   <li>[调整] 更新部分列 <code>UpdateIncludeNowAsync</code> 具有二义性 <a href="https://gitee.com/dotnetchina/Furion/issues/I3RW9Q">#I3RW9Q</a></li> 
   <li>[优化] <strong>框架底层性能，大大减少内存占用和溢出情况，启动内存从之前 <code>136M</code> 下将到 <code>86M</code></strong></li> 
   <li>[其他] 删除无用代码，优化不规范命名等</li> 
  </ul> </li> 
 <li> <p><strong>文档变化</strong></p> 
  <ul> 
   <li>[新增] <code>Inject</code> 说明文档 <a href="https://gitee.com/dotnetchina/Furion/issues/I3TITA">#I3TITA</a></li> 
   <li>[更新] 4.2.9 的示例代码文档，方法没有放在 class 中 <a href="https://gitee.com/dotnetchina/Furion/issues/I3S9T5">#I3S9T5</a></li> 
   <li>[修正] 规范化结果 6.5.6 多分组排序图片引用错误 <a href="https://gitee.com/dotnetchina/Furion/issues/I3UBOQ">#I3UBOQ</a></li> 
   <li>[更新] 静态类 <code>Scoped</code> 文档</li> 
  </ul> </li> 
 <li> <p><strong>问答答疑</strong></p> 
  <ul> 
   <li>[答疑] 默认 <code>MasterDbContextLocator</code> 不随自定义的参数生成 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SDBB">#I3SDBB</a></li> 
   <li>[答疑] 事件总线中订阅处理程序类获取不到用户信息，这个正常吗 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SS0U">#I3SS0U</a></li> 
   <li>[答疑] 在有多租户过滤器的情况下，是否有一种方式查询全量的数据 <a href="https://gitee.com/dotnetchina/Furion/issues/I3T0VI">#I3T0VI</a></li> 
   <li>[答疑] mysql 使用 <code>&"tools/cli.ps1"</code> 页面化加载表结构失败 <a href="https://gitee.com/dotnetchina/Furion/issues/I3T4F8">#I3T4F8</a></li> 
   <li>[答疑] 其他 Web 层的 Startup 优先执行 <a href="https://gitee.com/dotnetchina/Furion/issues/I3T8IP">#I3T8IP</a></li> 
   <li>[答疑] 辅助角色服务实现建议 <a href="https://gitee.com/dotnetchina/Furion/issues/I3T906">#I3T906</a></li> 
   <li>[答疑] 开启 <code>easy connection</code> 后同一内网地址浏览器可以正常访问，远程请求则无法访问<a href="https://gitee.com/dotnetchina/Furion/issues/I3TA2U">#I3TA2U</a></li> 
   <li>[答疑] <code>scope.ServiceProvider.GetService<IOtherService></code>不存在 <a href="https://gitee.com/dotnetchina/Furion/issues/I3TQMV">#I3TQMV</a></li> 
   <li>[答疑] 能否在 WPF 项目中使用呢？ <a href="https://gitee.com/dotnetchina/Furion/issues/I3TMCC">#I3TMCC</a></li> 
   <li>[答疑] <code>Dapper</code> 多个数据源 <a href="https://gitee.com/dotnetchina/Furion/issues/I3TM9B">#I3TM9B</a></li> 
   <li>[答疑] <code>L.GetSelectCulture()</code> 方法异常 <a href="https://gitee.com/dotnetchina/Furion/issues/I3TQS4">#I3TQS4</a></li> 
   <li>[答疑] 循环中使用 <code>IDGen.NextID()</code> 得到的结果并不是连续的 <a href="https://gitee.com/dotnetchina/Furion/issues/I3UAF6">#I3UAF6</a></li> 
   <li>[答疑] 模块化动态加载插件支持通配符匹配.dll <a href="https://gitee.com/dotnetchina/Furion/issues/I3UDT8">#I3UDT8</a></li> 
   <li>[答疑] <code>MVC</code> 模式，在 <code>Controller</code> 里快捷方式创建 <code>View</code> 页面出错 <a href="https://gitee.com/dotnetchina/Furion/issues/I3UFGB">#I3UFGB</a></li> 
   <li>[答疑] 数据库迁移没有种子数据 <a href="https://gitee.com/dotnetchina/Furion/issues/I3UI7G">#I3UI7G</a></li> 
   <li>[答疑] <code>SpareTimeAttribute</code> 中 根据 Cron 表达式 自动匹配 Cron 表达式格式化方式 <a href="https://gitee.com/dotnetchina/Furion/issues/I3UTKQ">#I3UTKQ</a></li> 
  </ul> </li> 
 <li> <p><strong>不做实现</strong></p> 
  <ul> 
   <li>[废弃] 添加令牌桶限流算法 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SCDV">#I3SCDV</a></li> 
   <li>[废弃] 定时任务立即执行需求 <a href="https://gitee.com/dotnetchina/Furion/issues/I3SF4A">#I3SF4A</a></li> 
   <li>[废弃] 文档建议 关于 reids 和 es 、消息队列的 <a href="https://gitee.com/dotnetchina/Furion/issues/I3T90I">#I3T90I</a></li> 
   <li>[废弃] IP 高频率请求限制 <a href="https://gitee.com/dotnetchina/Furion/issues/I3UHE1">#I3UHE1</a></li> 
   <li>[废弃] <code>Url</code> 转发大模块 <a href="https://gitee.com/dotnetchina/Furion/issues/I3TZHO">#I3TZHO</a></li> 
  </ul> </li> 
</ul> 
<h2>贡献者画像</h2> 
<p><img alt="Giteye chart" src="https://chart.giteye.net/gitee/dotnetchina/Furion/ZS49EPL6.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">文档地址</h2> 
<ul> 
 <li>国内文档：<a href="https://dotnetchina.gitee.io/furion" target="_blank">https://dotnetchina.gitee.io/furion</a></li> 
 <li>国外文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffurion.pro%2F" target="_blank">https://furion.pro</a></li> 
</ul> 
<h2 style="text-align:left">项目地址</h2> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmonksoul%2FFurion" target="_blank">https://github.com/monksoul/Furion</a></li> 
 <li>Docker：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fr%2Fmonksoul%2Ffurion" target="_blank">https://hub.docker.com/r/monksoul/furion</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFurion" target="_blank">https://www.nuget.org/packages/Furion</a></li> 
</ul> 
<p style="text-align:left"><a href="https://gitee.com/dotnetchina/Furion">Furion</a><span style="background-color:#ffffff; color:#333333"> 遵循 </span><a href="https://gitee.com/dotnetchina/Furion/blob/master/LICENSE">Apache-2.0</a><span style="background-color:#ffffff; color:#333333"> 开源协议，欢迎大家提交 </span><a href="https://gitee.com/dotnetchina/Furion/pulls">PR</a><span style="background-color:#ffffff; color:#333333"> 或 </span><a href="https://gitee.com/dotnetchina/Furion/issues/new">Issue</a><span style="background-color:#ffffff; color:#333333">。喜欢可以给个 </span><a href="https://gitee.com/dotnetchina/Furion/stargazers">Star</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            