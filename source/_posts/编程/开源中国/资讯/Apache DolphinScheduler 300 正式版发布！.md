
---
title: 'Apache DolphinScheduler 3.0.0 正式版发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic4.zhimg.com/80/v2-a87b37f82b2fcb2d7d0273ebedcea48b_720w.png?source=d16d100b'
author: 开源中国
comments: false
date: Wed, 10 Aug 2022 10:38:00 GMT
thumbnail: 'https://pic4.zhimg.com/80/v2-a87b37f82b2fcb2d7d0273ebedcea48b_720w.png?source=d16d100b'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0; text-align:start"> 
 <p><span>​</span>点亮 ⭐️ Star · 照亮开源之路</p> 
 <p><strong>GitHub:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdolphinscheduler" target="_blank">https://github.com/apache/dolphinscheduler</a></strong></p> 
 <p><img alt src="https://pic4.zhimg.com/80/v2-a87b37f82b2fcb2d7d0273ebedcea48b_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p><strong>版本发布</strong> 2022/8/10</p> 
 <p>2022 年 8 月 10 日，Apache DolphinScheduler 在经过 3.0.0 alpha、3.0.0-beta-1、3.0.0-beta-2 不断验证之后，终于迎来了社区期盼已久的第三个大版本！</p> 
 <p>3.0.0 正式版本发生了自发版以来的最大幅度变动，新增了众多全新功能和特性，旨在为用户带来全新的体验和更多价值。</p> 
 <p>经过迭代的 3.0.0 正式版与此前 3.0.0 alpha 版本更新文中所描述的主要功能和特性更新、优化项和 Bug 修复大致一致，<strong>包括“更快、更强、更现代化、更易维护”这四个关键词总结</strong>。</p> 
 <p>对于版本迭代后新增的功能和优化，本文将再做补充。</p> 
 <p><strong>关键词：更快、更强、更现代化、更易维护</strong></p> 
 <p>3.0.0 的关键字不变，**“更快、更强、更现代化、更易维护”**的特点相信大家在使用中可以体验到。</p> 
 <ul> 
  <li> <p><strong>更快</strong>：重构了 UI 界面，新 UI 不仅用户响应速度提高数十倍，开发者构建速度提高数百倍；</p> </li> 
  <li> <p><strong>更强：</strong>带来了许多振奋人心的新功能，如数据质量保证、自定义时区、新增多个任务支持和多个告警插件；</p> </li> 
  <li> <p><strong>更现代化</strong>：新 UI 除了更快外，大到页面布局，细到图标样式都更加现代化；</p> </li> 
  <li> <p><strong>更易维护</strong>：后端服务拆分更加符合容器化和微服务化的发展趋势，还能明确各个服务的职责，让维护更加简单。</p> </li> 
 </ul> 
 <h1 style="text-align:center"><strong>新功能和新特性</strong></h1> 
 <p style="text-align:center"><strong>前文已有详细描述的新功能和新特性包括：</strong></p> 
 <p style="text-align:center"><img alt src="https://pic4.zhimg.com/80/v2-71492d2ffae611480aa086fc432b3c38_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p> </p> 
 <p>3.0.0 最大的变化是引入了新的 UI，切换语言页面无需重新加载，并且新增了深色主题。新 UI 使用了 Vue3，TSX，Vite 相关技术栈。对比旧版 UI，新 UI 不仅更加现代化，操作也更加人性化，前端的鲁棒性也更强，使用户在编译时一旦发现代码中的问题，可以对接口参数进行校验，从而使前端代码更加健壮。</p> 
 <p> </p> 
 <p>此外，新架构和新技术栈不仅能让用户在操作 Apache DolphinScheduler 时响应速度有数十倍的提升，同时开发者本地编译和启动 UI 的速度有了数百倍的提升，这将大大缩短开发者调试和打包代码所需的时间。</p> 
 <p style="text-align:center"><strong>新 UI 使用体验：</strong></p> 
 <p style="text-align:center"><img alt src="https://pic3.zhimg.com/80/v2-3d77252d9f717ea409d9277110c53172_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p style="text-align:center">​本地启动耗时对比</p> 
 <p style="text-align:center"> </p> 
 <p style="text-align:center"><img alt src="https://pica.zhimg.com/80/v2-375afa8e1911dbe545db02fb375f91c0_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p style="text-align:center">​项目管理页面</p> 
 <p style="text-align:center"> </p> 
 <p style="text-align:center"><img alt src="https://pic2.zhimg.com/80/v2-8260c388a7dbdea4208bc165580bc63b_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p style="text-align:center">​工作流定义页面</p> 
 <p style="text-align:center"> </p> 
 <p style="text-align:center"><img alt src="https://pic2.zhimg.com/80/v2-701172b7963550db05c1fb1d21f252c9_720w.jpg?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p style="text-align:center">​shell 任务页面</p> 
 <p style="text-align:center"> </p> 
 <p style="text-align:center"><img alt src="https://pic3.zhimg.com/80/v2-5cb01e20846ec6301076983237af3d10_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p style="text-align:center">​MySQL 数据源页面</p> 
 <h1 style="text-align:center"><strong>AWS 支持</strong></h1> 
 <p>随着 Apache DolphinScheduler 用户群体越来越丰富，吸引了很多海外用户。但在海外业务场景下，用户在调研过程中发现有两个影响用户便捷体验 Apache DolphinScheduler 的点，一个是时区问题，另一个则是对海外云厂商，尤其是对 AWS 的支持不足。此版本中，我们决定对 AWS 较为重要的组件进行支持，目前已经涵盖 Amazon EMR 和 Amazon Redshift 两个 AWS 的任务类型，以及实现了资源中心支持 Amazon S3 存储。</p> 
 <ul> 
  <li>针对 <strong>Amazon EMR</strong>，我们创建了一个新的任务类型，并提供了其 Run Job Flow 的功能，允许用户向 Amazon EMR 提交多个 steps 作业，并指定使用的资源数量。</li> 
 </ul> 
 <p>详情可见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdolphinscheduler.apache.org%2Fzh-cn%2Fdocs%2Flatest%2Fuser_doc%2Fguide%2Ftask%2Femr.html" target="_blank">https://dolphinscheduler.apache.org/zh-cn/docs/latest/user_doc/guide/task/emr.html</a></p> 
 <p style="text-align:center"><img alt src="https://pic2.zhimg.com/80/v2-cf960d07c47be02eb5537f4a3e2c3672_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p style="text-align:center">Amazon EMR 任务定义</p> 
 <p style="text-align:center"> </p> 
 <ul> 
  <li>对于 <strong>Amazon Redshift</strong>，我们目前在 SQL 任务类型中扩展了对 Amazon Redshift 数据源的支持，现在用户可以在 SQL 任务中选择 Redshift 数据源来运行 Amazon Redshift 任务。</li> 
 </ul> 
 <p style="text-align:center"><img alt src="https://pic3.zhimg.com/80/v2-0de9adbf94db60641e4ef10debd931b1_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p style="text-align:center">Amazon Redshift 支持</p> 
 <ul> 
  <li>对于 <strong>Amazon S3</strong>，我们扩展了 Apache DolphinScheduler 的资源中心，使其不仅能支持本地资源、HDFS 资源存储，同时支持 Amazon S3 作为资源中心的储存。详情可见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdolphinscheduler.apache.org%2Fzh-cn%2Fdocs%2Flatest%2Fuser_doc%2Fguide%2Fresource.html" target="_blank">https://dolphinscheduler.apache.org/zh-cn/docs/latest/user_doc/guide/resource.html</a> 中的 `resource.storage.type`</li> 
 </ul> 
 <p>后续我们将支持更多 AWS 任务，敬请期待。</p> 
 <h2><strong>服务拆分</strong></h2> 
 <p>全新的 UI 是 3.0.0 前端的最大变化，而后端最大的变化就是对服务进行拆分。考虑到容器和微服务的概念越来越火热，Apache DolphinScheduler 开发者做出了重大决定：对后端服务进行拆分。按照职能，我们将服务拆分成了以下几部分：</p> 
 <ul> 
  <li> <p>master-server: master服务</p> </li> 
  <li> <p>worker-server: worker服务</p> </li> 
  <li> <p>api-server: API服务</p> </li> 
  <li> <p>alert-server: 告警服务</p> </li> 
  <li> <p>standalone-server: standalone用于快速体验 dolphinscheduler 功能</p> </li> 
  <li> <p>ui: UI资源</p> </li> 
  <li> <p>bin: 快速启动脚本，主要是启动各个服务的脚本</p> </li> 
  <li> <p>tools: 工具相关脚本，主要包含数据库创建，更新脚本</p> </li> 
 </ul> 
 <p>所以的服务都可以通过</p> 
 <pre><code>`bin/dolphinscheduler-daemon.sh`
</code></pre> 
 <p>的方式进行启动或者停止。</p> 
 <h2><strong>数据质量保证</strong></h2> 
 <p>此版本中，用户们从 2.0.0 开始就期待已久的数据质量保证应用功能上线，解决了从源头同步的数据条数准确性，单表或多表周均、月均波动超过阈值告警等数据质量问题。Apache DolphinScheduler 此前版本解决了将任务以特定顺序和时间运行的问题，但数据运行完之后对数据的质量一直没有较为通用的衡量标准，用户需要付出额外的开发成本。</p> 
 <p>现在，3.0.0 已经实现了数据质量原生支持，用户可以直接通过配置的方式，轻松实现数据质量监控，在保证工作流运行的前提下，保证运行结果的准确性。</p> 
 <p style="text-align:center"><img alt src="https://pic2.zhimg.com/80/v2-eec512d2573e2872054f85a07e61e2bd_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p>​</p> 
 <p style="text-align:center"><img alt src="https://pic3.zhimg.com/80/v2-5cb01e20846ec6301076983237af3d10_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p>​</p> 
 <h2><strong>任务组</strong></h2> 
 <p>任务组主要用于控制任务实例并发并明确组内优先级。用户在新建任务定义时，可配置当前任务对应的任务组，并配置任务在任务组内运行的优先级。当任务配置了任务组后，任务的执行除了要满足上游任务全部成功外，还需要满足当前任务组正在运行的任务小于资源池的大小。当大于或者等于资源池大小时，任务会进入等待状态等待下一次检查。当任务组中多个任务同时进到待运行队列中时，会先运行优先级高的任务。</p> 
 <p>详见 链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdolphinscheduler.apache.org%2Fzh-cn%2Fdocs%2F3.0.0%2Fuser_doc%2Fguide%2Fresource.html" target="_blank">https://dolphinscheduler.apache.org/zh-cn/docs/3.0.0/user_doc/guide/resource.html</a></p> 
 <p style="text-align:center"><img alt src="https://pic3.zhimg.com/80/v2-66023c717a03227323cf9907ef99f92d_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p>​</p> 
 <h2><strong>自定义时区</strong></h2> 
 <p>在 3.0.0 之前版本，Apache DolphinScheduler 默认的时间是 UTC+8 时区，但随着用户群体扩大，海外用户和在海外开展跨时区业务的用户在使用中经常被时区所困扰。3.0.0 支持时区切换后，失去问题迎刃而解，满足海外用户和出海业务伙伴的需求。例如，如当企业业务涉及的时区包含东八区和西五区，想要使用同一个 DolphinScheduler 集群时，可以分别创建多个用户，每个用户使用自己当地时区，对应 DolphinScheduler 对象显示的时间均会切换为对应时区的当地时间，更加符合当地开发者的使用习惯。</p> 
 <p>详见 链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdolphinscheduler.apache.org%2Fzh-cn%2Fdocs%2F3.0.0%2Fuser_doc%2Fguide%2Fhowto%2Fgeneral-setting.html" target="_blank">https://dolphinscheduler.apache.org/zh-cn/docs/3.0.0/user_doc/guide/howto/general-setting.html</a></p> 
 <p style="text-align:center"><img alt src="https://pic2.zhimg.com/80/v2-e6f19ad8d203f7074f16df3a3a1311bc_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p>​</p> 
 <h2><strong>任务定义列表</strong></h2> 
 <p>使用 Apache DolphinScheduler 3.0.0 此前版本，用户如果想要操作任务，需要先找到对应的工作流，并在工作流中定位到任务的位置之后才能编辑。然而，当工作流数量变多或单个工作流有较多的任务时，找到对应任务的过程将会变得非常痛苦，这不是 Apache DolphinScheduler 所追求的 easy to use 理念。所以，我们在 3.0.0 中增加了任务定义页面，让用户可以通过任务名称快速定位到任务，并对任务进行操作，轻松实现批量任务变更。</p> 
 <p>详见 链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdolphinscheduler.apache.org%2Fzh-cn%2Fdocs%2F3.0.0%2Fuser_doc%2Fguide%2Fproject%2Ftask-instance.html" target="_blank">https://dolphinscheduler.apache.org/zh-cn/docs/3.0.0/user_doc/guide/project/task-instance.html</a></p> 
 <p style="text-align:center"><img alt src="https://pica.zhimg.com/80/v2-3789139155a7f7dd74f6217d5a721c57_720w.jpg?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p>​</p> 
 <h2><strong>新告警类型支持</strong></h2> 
 <p>在 3.0.0 中，告警类型也进行了扩展，我们增加了对 Telegram、Webexteams 告警类型的支持。</p> 
 <p style="text-align:center"><img alt src="https://pica.zhimg.com/80/v2-0de9adbf94db60641e4ef10debd931b1_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p>​</p> 
 <h1><strong>Python API 新功能</strong></h1> 
 <p>3.0.0 中，Python API 最大的变化是将对应的 PythonGatewayServer 集成到了 API-Server 服务, 并将其重命名 PythonGatewayService, 现在用户在启动 api-server 时会默认启动 PythonGatewayService；如果不想要启动 PythonGatewayService，可以将 application.yaml 中的 python-gateway.enabled 设置成 false。</p> 
 <p>此外, Python API 还增加了 CLI 和 configuration 模块。Configuration 模块允许用户修改 Python API 默认的配置, 如修改工作流默认的用户名、worker 分组等内容, 可以通过环境变量、直接修改文件、Python 动态修改来改变值。</p> 
 <pre><code># environment variable
export PYDS_JAVA_GATEWAY_ADDRESS="192.168.1.1"
export PYDS_WORKFLOW_USER="custom-user"
# file change
Directly change ~/pydolphinscheudler/config.yaml
# CLI
pydolphinscheduler config --set java_gateway.address 192.168.1.1
pydolphinscheduler config --set java_gateway.address 192.168.1.1 --set java_gateway.port 25334
</code></pre> 
 <p>目前 CLI 只有 version 和 config 两个子命令, 用于确认当前版本以及增删配置文件。后续，我们将引入更加多功能，方便用户通过命令行操作 DolphinScheduler。</p> 
 <pre><code># version
pydolphinscheduler verison
# 3.0.0
# config
pydolphinscheduler config --get java_gateway.address --get java_gateway.port
# The output look like below:
# java_gateway.address = 127.0.0.1
# java_gateway.port = 25333
pydolphinscheduler config --set java_gateway.address 192.168.1.1 --set java_gateway.port 25334
</code></pre> 
 <p>值得注意的是，Python API 还支持新增和上传资源中心文件功能，方便资源管理；支持同一个 project 不同 workflow 写入不同名称；增加集成测试，让测试更加便捷。</p> 
 <h1><strong>此前版本未公布的功能和特性更新</strong></h1> 
 <p>支持 Flink 任务类型</p> 
 <p>在该版本中，我们扩展了 Flink 任务类型，使其支持运行 Flink SQL 任务，其使用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsql-client.sh" target="_blank">sql-client.sh</a> 提交任务。在此前的版本中, 我们仅支持通过 flink cli 的方式提交任务, 这种方式需要结合资源中心, 将资源文件提交到资源中心, 然后在任务定义页面引用改资源, 对于版本化和用户透明都不是十分友好. 随着 flink sql 逐渐成为 flink 使用者的主流, 加之直接在编辑页面写 sql 更加用户透明, 我们采纳了向社区贡献的 flink sql 功能. 3.0.0 以后的版本用户可以更加方便的使用 flink 任务了。</p> 
 <p>更多详情查看：[flink sql client](<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnightlies.apache.org%2Fflink%2Fflink-docs-master%2Fdocs%2Fdev%2Ftable%2Fsqlclient%2F" target="_blank">https://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sqlclient/</a>)</p> 
 <p>对应 PR：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdolphinscheduler%2Fpull%2F9840" target="_blank">https://github.com/apache/dolphinscheduler/pull/9840</a></p> 
 <p><img alt src="https://pic2.zhimg.com/80/v2-7c14a1af29880967b1281cae8999db65_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p>​</p> 
 <h2>新增 Zepplin 任务类型</h2> 
 <p>在该版本中，我们增加了 Zeppelin 任务类型，用于创建并执行 Zeppelin 类型任务。Worker 执行该任务时，会通过 Zeppelin Cient API 触发 Zeppelin Notebook 段落。</p> 
 <p>对应PR：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdolphinscheduler%2Fpull%2F9810" target="_blank">https://github.com/apache/dolphinscheduler/pull/9810</a></p> 
 <p><img alt src="https://pic3.zhimg.com/80/v2-ba3e897528d0adcf643fa3a59a011214_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p>​</p> 
 <h2>Bash 传参功能</h2> 
 <p>新版本还新增了通过 bash 传参的功能，如果你想在下游任务中使用 bash 变量而不是常量值 export 参数，你可以在通过 setValue 和 Bash 变量实现，它更加灵活，可以让你动态地获取现有的本地或 HTTP 资源获取设定变量。</p> 
 <p>可以使用类似的语法</p> 
 <pre><code>lines_num=$(wget https://raw.githubusercontent.com/apache/dolphinscheduler/dev/README.md -q -O - | wc -l | xargs)echo "#&#123;setValue(set_val_var=$&#123;lines_num&#125;)&#125;"
</code></pre> 
 <h2>允许用户上传没有后缀的文件</h2> 
 <p>之前资源中心只能上传有后缀的文件，在 3.0.0 版本后，我们支持用户上传没有后缀的文件。</p> 
 <h2>其他功能增强</h2> 
 <p>除了上述功能新增外，3.0.0 版本还进行了很多细节功能增强，如重构任务插件、数据源插件模块，让扩展更简单；恢复了对 Spark SQL 的支持；E2E 测试已经完美兼容新 UI 等。</p> 
 <p><strong>主要优化项</strong></p> 
 <ul> 
  <li> <p>任务后端插件优化，新插件只需要修改插件自带的模块</p> </li> 
  <li> <p>在工作流下提交/创建 cron 时验证结束时间和开始时间</p> </li> 
  <li> <p>Dependent 添加依赖时可以选择全局项目</p> </li> 
  <li> <p>AlertSender 优化及关闭优化，如 MasterServer</p> </li> 
  <li> <p>增加 slot 条件查询数据库, 减少返回数据记录</p> </li> 
  <li> <p>通过将 python gatewar 迁移到 apiserver 来精简 dist 包</p> </li> 
  <li> <p>[python] 将 pythonGatewayServer 迁移到 api 服务器</p> </li> 
  <li> <p>[python] 添加缺失的配置和连接远程服务器文档</p> </li> 
  <li> <p>[Master/Worker] 将任务 ack 更改为运行回调</p> </li> 
  <li> <p>[Master] 添加任务事件线程池</p> </li> 
 </ul> 
 <p><strong>主要 Bug 修复</strong></p> 
 <ul> 
  <li> <p>修复使用 S3a Minio 创建租户失败的问题</p> </li> 
  <li> <p>修复文本文件 busy 的问题</p> </li> 
  <li> <p>修复项目授权时生成一个重复授权项目的问题</p> </li> 
  <li> <p>修复因无法连接到 postgresql 而启动服务器失败的问题</p> </li> 
  <li> <p>修复消息显示找不到数据源插件“Spark”的问题</p> </li> 
  <li> <p>修复 MapReduce 生成的命令内置参数位置错误的问题</p> </li> 
  <li> <p>解决更改参数用户，队列在 ProcessDefinition 中失效的问题</p> </li> 
  <li> <p>解决使用依赖组件的进程无法在测试和生产环境之间迁移</p> </li> 
  <li> <p>解决了资源文件删除条件的问题</p> </li> 
  <li> <p>修复编辑复制节点的表单时影响原始节点数据的问题</p> </li> 
  <li> <p>解决了 Worker 资源耗尽并导致停机的问题</p> </li> 
  <li> <p>解决了某些类型的警报无法显示项目名称的问题</p> </li> 
  <li> <p>3.0.0 各个部署方式出现的问题</p> </li> 
  <li> <p>任务组为空时页面报错问题</p> </li> 
  <li> <p>treemap 视图深度错误问题</p> </li> 
  <li> <p>告警信息不明确问题：告警组为空时报错信息不明确，批量删除工作流有异常时报错信息不明确，租户内容错长的错误提示，删除</p> </li> 
  <li> <p>参数校验问题：数据源中心的参数校验问题，修改密码时密码不一致提示，发告警前校验 alert scriptb</p> </li> 
  <li> <p>Python api：不能设置 release state 问题，本地参数有值但是校验失败问题</p> </li> 
  <li> <p>token 查询不遵循时区问题</p> </li> 
  <li> <p>修复 HTTPS 和 HTTP 字符串识别问题</p> </li> 
  <li> <p>修复 alert server 健康监测失效问题</p> </li> 
  <li> <p>修复 condition 任务分支失败问题</p> </li> 
  <li> <p>修复 docker 镜像不支持多平台问题</p> </li> 
  <li> <p>修复带有任务组优先级的工作流创建时不能正确写数据库的问题</p> </li> 
  <li> <p>master 任务的失效问题</p> </li> 
  <li> <p>修复串行等待不运行的问题</p> </li> 
  <li> <p>时区问题：调度时区错误问题，日志增加时区支持</p> </li> 
  <li> <p>重新运行、暂停工作流实例失败问题</p> </li> 
  <li> <p>资源中心实例化失败问题</p> </li> 
  <li> <p>修复邮件告警模板分隔线问题</p> </li> 
  <li> <p>修复Standalone模式下数据初始化问题</p> </li> 
  <li> <p>修复监控中心DB不存在时的页面展示问题</p> </li> 
  <li> <p>修复创建工作流参数无效问题</p> </li> 
  <li> <p>修复K8S部署时zookeeper端口异常问题</p> </li> 
  <li> <p>修复Standalone模式下服务启动失败问题</p> </li> 
  <li> <p>修复LDAP登录失败问题</p> </li> 
  <li> <p>Python api: 修复同一个项目下不同工作流的任务组件名称不支持重名问题</p> </li> 
  <li> <p>Python api: 修复SQL任务组件SQL类型错误问题</p> </li> 
  <li> <p>修复资源文件重命名表单异常问题</p> </li> 
  <li> <p>修复根据定时设置获取工作流可执行时间错误问题</p> </li> 
  <li> <p>升级了Logback、Log4j等模块依赖</p> </li> 
  <li> <p>修复任务失败问题</p> </li> 
  <li> <p>修复好HDFS NPE 问题</p> </li> 
  <li> <p>修复任务组异常导致master死锁问题</p> </li> 
  <li> <p>修复一些列稳定性问题</p> </li> 
 </ul> 
 <h1>文档修改</h1> 
 <ul> 
  <li> <p>更正部署文档</p> </li> 
  <li> <p>修复、更新部分使用文档：WebexTeams 中文文档，本地参数、全局参数文档，Kubernetes FAQ 文档，Spark 注意事项文档，DataX 使用文档，删除 Flink API 文档，修复 open-api 的错误，修复数据质量中的错误文档；新增 stand-alone 切换数据库文档；新增 shell 中判断 Yarn 运行状态文档；新增更新系统截图; 参数传递、全局参数、参数优先级文档，告警组件向导、Telegram、钉钉告警文档，告警FAQ文档，Shell组件文档，Switch任务组件文档，资源中心配置详情文档，工作流定义补数文档</p> </li> 
  <li> <p>更正部分开发文档：明确支持的操作系统，修复开发环境搭建文档，新增自己构建 docker 镜像文档</p> </li> 
 </ul> 
 <h1>Release note</h1> 
 <p>GitHub: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdolphinscheduler%2Freleases%2Ftag%2F3.0.0" target="_blank">https://github.com/apache/dolphinscheduler/releases/tag/3.0.0</a></p> 
 <p><strong>下载：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdolphinscheduler.apache.org%2Fen-us%2Fdownload%2Fdownload.html" target="_blank">https://dolphinscheduler.apache.org/en-us/download/download.html</a></p> 
 <p>感谢贡献者</p> 
 <p>Aaron Lin、Amy0104、Assert、BaoLiang、Benedict Jin、BenjaminWenqiYu、Brennan Fox、Dannila、Desperado2、Devosend、DingPengfei、DuChaoJiaYou、EdwardYang、Eric Gao、Frank Chen、GaoTianDuo、HanayoZz、HeChuan、HomminLee、Hua Jiang、Hwting、Ivan0626、Jeff Zhan、Jiajie Zhong、JieguangZhou、Jiezhi.G、JinYong Li、J·Y、Kerwin、Kevin.Shin、KingsleyY、Kirs、KyoYang、LinKai、LiuBodong、LongJGun、Luke Yan、Lyle Shaw、Manhua、Martin Huang、Maxwell、Molin Wang、<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2FMr.An" target="_blank">Mr.An</a>、OS、PJ Fanning、Paul Zhang、QuakeWang、ReonYu、SbloodyS、Sheldon、Shiwen Cheng、ShuiMuNianHuaLP、ShuoTiann、SongTao Zhuang、Stalary、Sunny Lei、Tom、Town、Tq、WangJPLeo、Wenjun Ruan、X&Z、XiaochenNan、Yanbin Lin、Yao WANG、Yiming Guo、Zonglei Dong、aCodingAddict、aaronlinv、aiwenmo、caishunfeng、calvin、calvinit、cheney、chouc、chuxing、czeming、devosend、exmy、gaojun2048、guodong、guoshupei、hjli、hstdream、huangxiaohai、janeHe13、jegger、jiachuan.zhu、jon-qj、juzimao、kezhenxu94、labbomb、leiwingqueen、lgcareer、lhjzmn、lidongdai、lifeng、lilyzhou、litiliu、liubo1990、liudi1184、longtb、lvshaokang、lyq、mans2singh、mask、mazhong、mgduoduo、myangle1120、naziD、nobolity、ououtt、ouyangyewei、pinkhello、qianli2022、qinchaofeng、rickchengx、rockfang、ronyang1985、seagle、shuai hou、simsicon、sneh-wha、songjianet、sparklezzz、springmonster、sq-q、syyangs799、uh001、wangbowen、wangqiang、wangxj3、wangyang、wangyizhi、wind、worry、wqxs、xiangzihao、xiaodi wang、xiaoguaiguai、xuhhui、yangyunxi、yc322、yihong、yimaixinchen、youzipi、zchong、zekai-li、zhang、zhangxinruu、zhanqian、zhuxt2015、zixi0825、zwZjut、天仇、小张、弘树丶、张俊杰、旭旭同學、时光、旺阳、王强、百岁、秋天、罗铭涛、阿福Chris、陈家名、陈爽、飞侠美如画</p> 
 <p><strong>参与贡献</strong></p> 
 <p>随着国内开源的迅猛崛起，Apache DolphinScheduler 社区迎来蓬勃发展，为了做更好用、易用的调度，真诚欢迎热爱开源的伙伴加入到开源社区中来，为中国开源崛起献上一份自己的力量，让本土开源走向全球。</p> 
 <p>参与 DolphinScheduler 社区有非常多的参与贡献的方式，包括：</p> 
 <p><img alt src="https://pic1.zhimg.com/80/v2-c175a385f6e53650ae9e10a621f84dff_720w.png?source=d16d100b" referrerpolicy="no-referrer"></p> 
 <p>​</p> 
 <p>贡献第一个PR(文档、代码) 我们也希望是简单的，第一个PR用于熟悉提交的流程和社区协作以及感受社区的友好度。</p> 
 <p>社区汇总了以下适合新手的问题列表：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdolphinscheduler%2Fissues%2F5689" target="_blank">https://github.com/apache/dolphinscheduler/issues/5689</a></p> 
 <p>非新手问题列表：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdolphinscheduler%2Fissues%3Fq%3Dis%253Aopen%2Bis%253Aissue%2Blabel%253A%2522volunteer%2Bwanted%2522" target="_blank">https://github.com/apache/dolphinscheduler/issues?q=is%3Aopen+is%3Aissue+label%3A"volunteer+wanted"</a></p> 
 <p>如何参与贡献链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdolphinscheduler.apache.org%2Fzh-cn%2Fcommunity%2Fdevelopment%2Fcontribute.html" target="_blank">https://dolphinscheduler.apache.org/zh-cn/community/development/contribute.html</a></p> 
 <p>来吧，DolphinScheduler开源社区需要您的参与，为中国开源崛起添砖加瓦吧，哪怕只是小小的一块瓦，汇聚起来的力量也是巨大的。</p> 
 <p>参与开源可以近距离与各路高手切磋，迅速提升自己的技能。</p> 
 <p>来吧，开源社区非常期待您的参与。</p> 
 <p><strong>活动推荐</strong></p> 
 <p>Apache DolphinScheduler社区联合了Apache Kylin社区，共同举办Meetup主题为《大数据底座的构建与展望，助力企业数字化转型》即将重磅开启！我们也有幸邀请到了来自伊利、T3出行、白鲸开源、Apache Kylin社区等企业的资深大数据工程师与开发者，从数据分析引擎、数据调度、数字化转型、维护开源视角等话题探讨在两个开源项目的开发实践。</p> 
</div>
                                        </div>
                                      
</div>
            