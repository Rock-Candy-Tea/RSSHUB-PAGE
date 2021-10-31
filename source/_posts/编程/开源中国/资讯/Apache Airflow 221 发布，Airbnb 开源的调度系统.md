
---
title: 'Apache Airflow 2.2.1 发布，Airbnb 开源的调度系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1712'
author: 开源中国
comments: false
date: Sun, 31 Oct 2021 09:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1712'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Apache Airflow 2.2.1  已正式发布，Airflow 是一个灵活、可扩展的工作流自动化和调度系统，可编集和管理数百 PB 的数据流。项目可轻松编排复杂的计算工作流，通过智能调度、数据库和依赖关系管理、错误处理和日志记录，Airflow 可以对从单个服务器到大规模集群的资源进行自动化管理。Airflow 采用 Python 编写，具有高扩展性，能够运行其他语言编写的任务，并允许与常用的体系结构和项目集成，如 AWS S3、Docker、Kubernetes、MySQL、PostgresSQL 等。</span></p> 
<p><strong><span style="background-color:#ffffff; color:#333333">主要更新内容</span></strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333">修复调度程序中的意外提交错误</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">添加 DagRun.logical_date 作为属性</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">任务完成时清除 ti.next_method 和 ti.next_kwargs</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">更快的 PostgreSQL 数据库迁移到 Airflow 2.2</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">删除 Swagger2Specification._set_defaults 类方法中不正确的类型注释</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">将 TriggererJob 添加到作业检查命令</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">当下一次运行为 None 时隐藏工具提示</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">使用数据间隔兼容层创建 TI 上下文 </span></li> 
 <li><span style="background-color:#ffffff; color:#333333">修复排队的 dag 运行更改 catchup=False 行为</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">当 dag 或任务完成时，将详细信息添加到日志记录中</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">警告不支持的 Python 3.10 </span></li> 
 <li><span style="background-color:#ffffff; color:#333333">通过使用 max_active_runs 限制排队的 dagrun 创建来修复追赶 </span></li> 
 <li><span style="background-color:#ffffff; color:#333333">缺少序列化 dag 时防止调度程序崩溃 </span></li> 
 <li><span style="background-color:#ffffff; color:#333333">不要为其他数据库安装 SQLAlchemy/Pendulum 适配器</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">解决方法 libstdcpp TLS 错误</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">将 ds、ts 等改回使用逻辑日期</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">确保任务状态在标记为失败/成功/跳过时不会改变 </span></li> 
 <li><span style="background-color:#ffffff; color:#333333">将触发器页面标签重命名为逻辑日期 </span></li> 
 <li><span style="background-color:#ffffff; color:#333333">允许 Param 支持默认值 None</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">从数据库反序列化时升级旧的 DAG/任务参数格式</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">不要将 ENV 和 _cmd 烘焙到非 sudo 的 tmp 配置中 </span></li> 
 <li><span style="background-color:#ffffff; color:#333333">CLI：如果缺少 args，则在加载 DAG 之前回填命令失败 </span></li> 
 <li><span style="background-color:#ffffff; color:#333333">错误修复：插入到 task_fail 时空执行日期违反 NOT NULL </span></li> 
 <li><span style="background-color:#ffffff; color:#333333">尝试在 upgradeb 中移动 "悬空" 行</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">SchedulerJob._process_executor_events 中的行锁 TI 查询 </span></li> 
 <li><span style="background-color:#ffffff; color:#333333">修复 Airflow 2.2.0 中的 XCom.delete 错误 </span></li> 
 <li><span style="background-color:#ffffff; color:#333333">在启动触发器之前检查 python 版本</span></li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202110.mbox%2F%253Cpony-a91d7954915ddb513bbfb7c4d7912a06fa376da3-c70cc35b5eed8de43d0b2607568c2858ede4d417%40announce.apache.org%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            