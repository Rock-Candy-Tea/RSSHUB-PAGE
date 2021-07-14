
---
title: 'StreamX v1.1.1 发布，Flink 开发脚手架、流批一体平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ebb54cc349a2272fe1cc4dfade259fc929f.png'
author: 开源中国
comments: false
date: Wed, 14 Jul 2021 09:23:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ebb54cc349a2272fe1cc4dfade259fc929f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <div style="text-align:left"> 
  <h1 style="text-align:center"><img alt height="200" src="https://oscimg.oschina.net/oscnet/up-ebb54cc349a2272fe1cc4dfade259fc929f.png" referrerpolicy="no-referrer"></h1> 
  <h2 style="text-align:center">Make Flink|Spark easier!!!</h2> 
 </div> 
 <p style="text-align:center"><img src="https://img.shields.io/github/stars/streamxhub/streamx" referrerpolicy="no-referrer"> <img src="https://img.shields.io/github/forks/streamxhub/streamx" referrerpolicy="no-referrer"> <img src="https://img.shields.io/github/issues/streamxhub/streamx" referrerpolicy="no-referrer"> <img src="https://img.shields.io/github/downloads/streamxhub/streamx/total" referrerpolicy="no-referrer"> <img src="https://img.shields.io/github/languages/count/streamxhub/streamx" referrerpolicy="no-referrer"></p> 
 <p style="text-align:center"> </p> 
</div> 
<p><span style="background-color:#ffffff; color:#333333">        大数据技术如今发展的如火如荼,已呈现百花齐放欣欣向荣的景象,实时处理流域 </span><code>Apache Spark</code><span style="background-color:#ffffff; color:#333333"> 和 </span><code>Apache Flink</code><span style="background-color:#ffffff; color:#333333"> 更是一个伟大的进步,尤其是</span><code>Apache Flink</code><span style="background-color:#ffffff; color:#333333">被普遍认为是下一代大数据流计算引擎, 我们在使用 </span><code>Flink</code><span style="background-color:#ffffff; color:#333333"> 时发现从编程模型, 启动配置到运维管理都有很多可以抽象共用的地方, 我们将一些好的经验固化下来并结合业内的最佳实践, 通过不断努力终于诞生了今天的框架 —— </span><code>StreamX</code><span style="background-color:#ffffff; color:#333333">, 项目的初衷是 —— 让 </span><code>Flink</code><span style="background-color:#ffffff; color:#333333"> 开发更简单, 使用</span><code>StreamX</code><span style="background-color:#ffffff; color:#333333">开发,可以极大降低学习成本和开发门槛, 让开发者只用关心最核心的业务,</span><code>StreamX</code><span style="background-color:#ffffff; color:#333333"> 规范了项目的配置,鼓励函数式编程,定义了最佳的编程方式,提供了一系列开箱即用的</span><code>Connectors</code><span style="background-color:#ffffff; color:#333333">,标准化了配置、开发、测试、部署、监控、运维的整个过程, 提供</span><code>scala</code><span style="background-color:#ffffff; color:#333333">和</span><code>java</code><span style="background-color:#ffffff; color:#333333">两套api, 其最终目的是打造一个一站式大数据平台,流批一体的解决方案.</span></p> 
<p><span style="background-color:#ffffff; color:#333333">        </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstreamxhub%2Fstreamx" target="_blank">StreamX</a><span style="background-color:#ffffff; color:#333333"> </span>遵循 Apache-2.0 开源协议,将会是个长期更新的活跃项目,欢迎大家提交<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstreamxhub%2Fstreamx%2Fpulls" target="_blank">PR</a> 或 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstreamxhub%2Fstreamx%2Fissues%2Fnew%2Fchoose" target="_blank">Issue</a>。喜欢请给个 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstreamxhub%2Fstreamx%2Fstargazers" target="_blank">Star</a>。您的支持是我们最大的动力, 该项目从开源以来受到不少朋友的关注和认可,表示感谢,已陆续有来自金融,在线教育,数据分析,车联网,智能广告,地产等公司的朋友在使用或二开,也不乏来自一线大厂的朋友在研究使用,继本次小版本升级之后,会大力推进k8s部署的支持,元数据的打通和实时数仓的支持.欢迎更多的开发者加入一块贡献,只有坚持做下去,并且做好才有意义,如果眼下还是一团薪薪之火,大家的热情一定可以让她烈焰燎原起来.</p> 
<p style="text-align:left"><strong>更新日志</strong><br> ​​​​​<strong>1.</strong> kerberos 自动续期bug修复  <br> <strong>2.</strong> 参数配置优先级相关bug修复(flink-conf.yaml中参数优先级比页面任务级别优先级大)<br> <strong>3.</strong> 标准apache flink任务在编辑时mainClass不回显的bug修复<br> <strong>4.</strong>  邮件发送参数设置相关bug修复<br> <strong>5.</strong> parallelism和slot参数设置不生效bug修复<br> <strong>6.</strong> 项目在下载maven 依赖时发生错误导致任务名称全被修改的bug修复<br> <strong>7.</strong> 用户登录返回前端的用户登录信息带有"盐",优化修复 (issue/240)<br> <strong>8.</strong> 修复启动脚本中可能存在的找不到jdk环境的bug (issue/238)<br> <strong>9.</strong> 新增消息推送,构建失败,任务失败消息推送到前端</p> 
<h1 style="text-align:left"><strong>功能列表</strong></h1> 
<ul> 
 <li><strong>开发脚手架</strong></li> 
</ul> 
<p>    [<span style="background-color:#ffffff; color:#242424">✅</span>] 简化八股文编程步骤,更便捷的api,全新的编程体验                     [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] DataStream和flink SQL一致的编程体检                                      [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 约定优于配置,封装配置信息和env环境信息                                 [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 常用connector二次封装,开箱即用                                                [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] DataStream和flink Sql方法扩展,更丝滑的操作支持                    [重要特性]</p> 
<ul> 
 <li><strong>系统管理</strong></li> 
</ul> 
<p>    [<span style="background-color:#ffffff; color:#242424">✅</span>] 用户管理, 新增,修改,删除,多租户支持<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 角色管理, 新增,修改,删除<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 菜单管理, 新增,修改,删除, 给角色分配权限,到按钮级别的权限控制</p> 
<ul> 
 <li><strong>项目管理</strong></li> 
</ul> 
<p>    [<span style="background-color:#ffffff; color:#242424">✅</span>] 项目创建,删除(目前只支持git)                                                      [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 项目编译,实时查看编译日志                                                         [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 项目列表过滤查询,分页</p> 
<ul> 
 <li><strong>作业管理</strong></li> 
</ul> 
<p>    [<span style="background-color:#ffffff; color:#242424">✅</span>] 作业启动，停止，重启，删除，火焰图(非flink内置)                   [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 停止时自动savePoint,启动时从savePoint恢复                             [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 自动记录每次任务checkpoint的路径信息,启动时自动恢复         [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 可视化 Flink SQL 编辑器,格式化，语法校验，保存                     [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] flinkSQL 任务多版本的支持                                                            [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] application 部署模式                                                                       [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 多版本flink的支持(flink 1.11.x,1.12.x,1.13.0)                                   [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 任务历史版本备份于和回滚                                                            [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 任务依赖管理,支持标准maven pom坐标的依赖和手动上传jar    [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 任务实时状态显示与实际任务保持一致                                         [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 任务监控,失败告警,发送邮件通知,自动重启                                  [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 针对checkpoint连续失败的处理(邮件告警|重启)                          [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] kerberos的认证支持                                                                        [重要特性]<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 作业创建，删除，编辑，更新，保存，常规参数配置。<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 任务启动失败的日志在线查看<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] yarn pre job 部署模式<br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 作业列表的查看，过滤，分页。</p> 
<p><strong>Notebook:</strong><br>     [<span style="background-color:#ffffff; color:#242424">✅</span>] 实验性功能,在线作业编写运行</p> 
<p><strong>Next version:</strong><br>     [<span style="background-color:#ffffff; color:#242424">❎</span>] 本地上传jar任务的支持<br>     [<span style="background-color:#ffffff; color:#242424">❎</span>] 操作接口开放(rest请求可以控制任务启动|停止|savePoint等)<br>     [<span style="background-color:#ffffff; color:#242424">❎</span>] 其他反馈的bug修复</p> 
<p><strong>大版本功能:</strong></p> 
<p>    [<span style="background-color:#ffffff; color:#242424">❎</span>] 容器化部署(docker), k8s 部署模式<br>     [<span style="background-color:#ffffff; color:#242424">❎</span>] SQL 的在线开发增强，智能提示,数据采样, 测试, 运行<br>     [<span style="background-color:#ffffff; color:#242424">❎</span>] 元数据支持<br>     [<span style="background-color:#ffffff; color:#242424">❎</span>] 定时任务集成(针对批作业定时调度)<br>     [<span style="background-color:#ffffff; color:#242424">❎</span>] 单点部署故障解决,HA高可用</p> 
<h2 style="text-align:left"><strong>重要特性</strong></h2> 
<ol> 
 <li><strong>开发脚手架</strong></li> 
 <li><strong>多版本Flink支持(多版本无缝支持1.11.x,1.12.x,1.13.x)</strong></li> 
 <li><strong>一系列开箱即用的connectors</strong></li> 
 <li><strong>支持项目编译功能(maven 编译)</strong></li> 
 <li><strong>在线参数配置</strong></li> 
 <li><strong>支持 Applicaion 模式， Yarn-Per-Job 模式启动</strong></li> 
 <li><strong>快捷的日常操作(任务启动,停止,savepoint,从savepoint恢复)</strong></li> 
 <li><strong>支持火焰图</strong></li> 
 <li><strong>支持 notebook (在线任务开发)</strong></li> 
 <li><strong>项目配置和依赖版本化管理</strong></li> 
 <li><strong>在线管理依赖(maven pom)和自定义jar</strong></li> 
 <li><strong>Flink SQL WebIDE</strong></li> 
 <li><strong>支持 Catalog、Hive</strong></li> 
 <li><strong>任务失败告警和重试重启</strong></li> 
</ol> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-0a291f09cc4abdf87175574936060dd07d5.png" width="1600" referrerpolicy="no-referrer"></p> 
<h1 style="text-align:left">软件架构</h1> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-b7e90cc994a3e2622b63f12c15bc73c3b5e.png" width="1200" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">项目地址</h2> 
<p style="text-align:left">官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.streamxhub.com" target="_blank">http://www.streamxhub.com</a></p> 
<p style="text-align:left">Github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstreamxhub%2Fstreamx" target="_blank">streamxhub/streamx: Make Flink|Spark easier!!! (github.com)</a></p> 
<p style="text-align:left">Gitee: <a href="https://gitee.com/benjobs/streamx">benjobs/StreamX (gitee.com)</a></p> 
<h1 style="text-align:left">快速上手</h1> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.streamxhub.com%2Fzh%2Fdoc%2Fguide%2Fquickstart%2F" target="_blank">快速上手开发 | StreamX (streamxhub.com)</a></p> 
   <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.streamxhub.com%2Fzh%2Fdoc%2Fconsole%2Fquickstart%2F" target="_blank">平台快速使用 | StreamX (streamxhub.com)</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            