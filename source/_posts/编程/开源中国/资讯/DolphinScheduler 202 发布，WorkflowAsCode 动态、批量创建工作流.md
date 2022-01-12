
---
title: 'DolphinScheduler 2.0.2 发布，WorkflowAsCode 动态、批量创建工作流'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e25d28d9e40d60460a8165fa79e387beb03.png'
author: 开源中国
comments: false
date: Wed, 12 Jan 2022 11:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e25d28d9e40d60460a8165fa79e387beb03.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0px; margin-right:0px"><img height="383" src="https://oscimg.oschina.net/oscnet/up-e25d28d9e40d60460a8165fa79e387beb03.png" width="900" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p style="color:#000000; margin-left:0; margin-right:0"><span>千呼万唤中，WorkflowAsCode 功能终于在 2.0.2 版本中如约上线，为有动态、批量创建和更新工作流需求的用户带来福音。</span></p> 
 <p style="color:#000000; margin-left:0; margin-right:0"><span>此外，新版本还新增企业微信告警群聊会话消息推送，简化了元数据初始化流程，并修复了旧版本中强制终止后服务重启失败，添加 Hive 数据源失败等问题。</span></p> 
</blockquote> 
<h1 style="margin-left:0px; margin-right:0px">01 新功能</h1> 
<h2>1 WorkflowAsCode</h2> 
<p><span>首先在新功能上，2.0.2 版本重磅发布了 PythonGatewayServer， 这是一个 Workflow-as-code 的服务端，与 apiServer 等服务的启动方式相同。</span></p> 
<p><span>启用 PythonGatewayServer 后，所有 Python API 的请求都会发送到 PythonGatewayServer。Workflow-as-code 让用户可以通过 Python API 创建工作流，对于有动态、批量地创建和更新工作流的用户来说是一个好消息。通过 Workflow-as-code 创建的工作流与其他工作流一样，都可以在 web UI 查看。</span></p> 
<p><span>以下为一个 Workflow-as-code 测试用例：</span></p> 
<pre style="margin-left:0; margin-right:.5em; text-align:left"><code><span style="color:#48be66"># 定义工作流属性，包括名称、调度周期、开始时间、使用租户等信息</span>
<span style="color:#c33795">with</span> ProcessDefinition<span style="color:#8b86c9">(</span>
    name=<span style="color:#e6424b">"tutorial"</span><span style="color:#8b86c9">,</span>
    schedule=<span style="color:#e6424b">"0 0 0 * * ? *"</span><span style="color:#8b86c9">,</span>
    start_time=<span style="color:#e6424b">"2021-01-01"</span><span style="color:#8b86c9">,</span>
    tenant=<span style="color:#e6424b">"tenant_exists"</span><span style="color:#8b86c9">,</span>
<span style="color:#8b86c9">)</span> <span style="color:#c33795">as</span> pd<span style="color:#8b86c9">:</span>
    <span style="color:#48be66"># 定义4个任务，4个都是 shell 任务，shell 任务的必填参数为任务名、命令信息，这里都是 echo 的 shell 命令</span>
    task_parent = Shell<span style="color:#8b86c9">(</span>name=<span style="color:#e6424b">"task_parent"</span><span style="color:#8b86c9">,</span> command=<span style="color:#e6424b">"echo hello pydolphinscheduler"</span><span style="color:#8b86c9">)</span>
    task_child_one = Shell<span style="color:#8b86c9">(</span>name=<span style="color:#e6424b">"task_child_one"</span><span style="color:#8b86c9">,</span> command=<span style="color:#e6424b">"echo 'child one'"</span><span style="color:#8b86c9">)</span>
    task_child_two = Shell<span style="color:#8b86c9">(</span>name=<span style="color:#e6424b">"task_child_two"</span><span style="color:#8b86c9">,</span> command=<span style="color:#e6424b">"echo 'child two'"</span><span style="color:#8b86c9">)</span>
    task_union = Shell<span style="color:#8b86c9">(</span>name=<span style="color:#e6424b">"task_union"</span><span style="color:#8b86c9">,</span> command=<span style="color:#e6424b">"echo union"</span><span style="color:#8b86c9">)</span>

    <span style="color:#48be66"># 定义任务间依赖关系</span>
    <span style="color:#48be66"># 这里将 task_child_one，task_child_two 先声明成一个任务组，通过 python 的 list 声明</span>
    task_group = <span style="color:#8b86c9">[</span>task_child_one<span style="color:#8b86c9">,</span> task_child_two<span style="color:#8b86c9">]</span>
    <span style="color:#48be66"># 使用 set_downstream 方法将任务组 task_group 声明成 task_parent 的下游，如果想要声明上游则使用 set_upstream</span>
    task_parent<span style="color:#8b86c9">.</span>set_downstream<span style="color:#8b86c9">(</span>task_group<span style="color:#8b86c9">)</span>

    <span style="color:#48be66"># 使用位操作符 << 将任务 task_union 声明成 task_group 的下游，同时支持通过位操作符 >> 声明</span>
    task_union << task_group</code></pre> 
<p><span>上面的代码运行后，可以在 web UI 看到的工作流如下：</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>                  --> task_child_one
                /                    \
task_parent -->                        -->  task_union
                \                   /
                  --> task_child_two</code>
</pre> 
<h2 style="margin-left:0px; margin-right:0px"><span style="color:#000000">2 企业微信告警方式支持群聊消息推送</span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>在此前版本中，微信告警方式仅支持消息通知方式；在 2.0.2 版本中，用户在使用企业微信的告警时，支持进行应用内以群聊会话消息推送的方式推送给用户。</span></p> 
<h1>02 优化</h1> 
<h2 style="margin-left:0px; margin-right:0px"><span style="color:#000000">1 简化元数据初始化流程</span></h2> 
<p><span>首次安装 Apache DolphinScheduler 时，运行 create-dolphinscheduler.sh 需要从最早的版本逐步升级到当前版本。</span><span>为了更方便快捷地初始化元数据流程，2.0.2 版本让用户可以直接安装当前版本的数据库脚本，提升安装速度。</span></p> 
<h2>2 删除补数日期中的“+1”（天）</h2> 
<p><span>删除了补数日期中的“+1”天，以避免补数时 UI 日期总显示 +1 给用户造成的困惑。</span></p> 
<h1 style="margin-left:0px; margin-right:0px"><span style="color:#000000">03 Bug 修复</span></h1> 
<p><span>[#7661] 修复 logger 在 worker 中的内存泄漏<br> [#7750 ]兼容历史版本数据源连接信息<br> [#7705] 内存限制导致从 1.3.5 升级到 2.0.2 出现错误<br> [#7786] 强制终止后服务重启失败<br> [#7660] 流程定义版本创建时间错误<br> [#7607] 执行 PROCEDURE 节点失败<br> [#7639] 在通用配置项中添加 quartz 和 zookeeper 默认配置<br> [#7654] 在依赖节点中，出现不属于当前项目的选项时报错<br> [#7658] 工作流复制错误<br> [#7609] worker sendResult 成功但 master 未收到错误时，工作流始终在运行<br> [#7554] </span><span>Standalone Server 中的 H2 会在数分钟后自动重启，导致数据异常丢失</span></p> 
<p><span>[#7434] 执行 MySQL 建表语句报错<br> [#7537] 依赖节点重试延迟不起作用<br> [#7392] 添加 Hive 数据源失败</span></p> 
<p><strong><span>下载：</span></strong><span>https://dolphinscheduler.apache.org/zh-cn/download/download.html</span></p> 
<p><strong><span>Release Note：</span></strong><span>https://github.com/apache/dolphinscheduler/releases/tag/2.0.2</span></p> 
<h1 style="margin-left:0px; margin-right:0px"><span style="color:#000000">04 致谢</span></h1> 
<p><span>一如既往地，感谢所有为 2.0.2版本建言献策并付诸行动的 Contributor（排名不分先后），是你们的智慧和付出让 Apache DolphinScheduler 更加符合用户的使用需求。</span></p> 
<p><img height="169" src="https://oscimg.oschina.net/oscnet/up-105d8279314696022505873c9cdb9205fdb.png" width="723" referrerpolicy="no-referrer"></p> 
<h1>05 参与贡献</h1> 
<p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff; color:#353535">随着国内开源的迅猛崛起，Apache DolphinScheduler 社区迎来蓬勃发展，为了做更好用、易用的调度，真诚欢迎热爱开源的伙伴加入到开源社区中来，为中国开源崛起献上一份自己的力量，让本土开源走向全球。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">参与 DolphinScheduler 社区有非常多的参与贡献的方式，包括：</span></p> 
<p><img height="39" src="https://oscimg.oschina.net/oscnet/up-1b1c71112f19b282831f08a4636e15fa04e.png" width="833" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">贡献第一个PR(文档、代码) 我们也希望是简单的，第一个PR用于熟悉提交的流程和社区协作以及感受社区的友好度。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">社区汇总了以下适合新手的问题列表：https://github.com/apache/dolphinscheduler/issues/5689</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">非新手问题列表：https://github.com/apache/dolphinscheduler/issues?q=is%3Aopen+is%3Aissue+label%3A%22volunteer+wanted%22</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">如何参与贡献链接：https://dolphinscheduler.apache.org/zh-cn/community/development/contribute.html</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">来吧，DolphinScheduler开源社区需要您的参与，为中国开源崛起添砖加瓦吧，哪怕只是小小的一块瓦，汇聚起来的力量也是巨大的。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0052ff">参与开源可以近距离与各路高手切磋，迅速提升自己的技能，如果您想参与贡献，我们有个贡献者种子孵化群，可以添加社区小助手</span><span style="color:#0052ff">微信(Leonard-ds) 手把手教会您( 贡献者不分水平高低，有问必答，关键是有一颗愿意贡献的心 )。添加小助手微信时请说明想参与贡献。</span></p> 
<p style="text-align:center"><span><strong>社区官网</strong></span><strong><span>https://dolphinscheduler.apache.org/</span></strong></p> 
<p style="text-align:center"><strong><span>代码仓地址</span></strong><strong><span>https://github.com/apache/dolphinscheduler</span></strong></p> 
<p style="text-align:center"><span><strong><strong>您的 Star，是 </strong>Apache DolphinScheduler <strong>为爱发电的动力❤️ </strong>～</strong></span></p> 
<p style="text-align:center"> </p> 
<p style="text-align:center"><span style="color:#0052ff"><strong><span>投稿请添加</span></strong><strong><span>社区小助手微信</span></strong></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:center"><span style="color:#0052ff"><strong><span>(Leonard-ds)</span></strong></span></p>
                                        </div>
                                      
</div>
            