
---
title: 'Apache Airflow 2.2.0 发布，Airbnb 开源的调度系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8482'
author: 开源中国
comments: false
date: Wed, 13 Oct 2021 06:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8482'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Apache Airflow 2.2.0  已正式发布，Airflow 是一个灵活、可扩展的工作流自动化和调度系统，可编集和管理数百 PB 的数据流。项目可轻松编排复杂的计算工作流，通过智能调度、数据库和依赖关系管理、错误处理和日志记录，Airflow 可以对从单个服务器到大规模集群的资源进行自动化管理。Airflow 采用 Python 编写，具有高扩展性，能够运行其他语言编写的任务，并允许与常用的体系结构和项目集成，如 AWS S3、Docker、Kubernetes、MySQL、PostgresSQL 等。</span></p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>新功能 
  <ul> 
   <li>AIP-39: 为 Airflow 添加（可定制的）时间表类，以实现更丰富的调度行为</li> 
   <li>AIP-40: 添加可延迟的 "异步" 任务</li> 
   <li>添加 Docker 任务流装饰器</li> 
   <li><span style="background-color:#ffffff; color:#182026">在仪表盘上显示来自本地设置的警报信息</span></li> 
   <li>使用 json-schema 的高级参数</li> 
   <li>能够测试来自 UI 或 API 的连接</li> 
   <li>将 Next Run 添加到 UI</li> 
   <li>添加默认权重规则配置选项</li> 
   <li>添加日历字段以在触发时选择 DAG 的执行日期</li> 
   <li>允许为 BashOperator 设置特定的 cwd</li> 
   <li>在 DAG 视图中显示导入错误</li> 
  </ul> </li> 
 <li>改进 
  <ul> 
   <li>改进 Airflow 用户界面的</li> 
   <li>将 processor_poll_interval 更名为 scheduler_idle_sleep_time</li> 
   <li>检查日志级别的允许值</li> 
   <li>修复使用 dagrun_conf 触发不存在的 dag 时的错误</li> 
   <li>为 TaskInstanceModelView 添加 muldelete 动作</li> 
   <li>避免在清除 DB 安装期间导入 DAG</li> 
   <li>要求在 DAG 权限上 can_edit，以修改 TaskInstances 和 DagRuns </li> 
   <li>使 Kubernetes 工作描述适合于一个日志行为 </li> 
   <li>如果任务实例的状态为空或未定义，总是画出边界 </li> 
   <li>改进了对僵尸任务的日志处理</li> 
  </ul> </li> 
 <li>bug 修复 
  <ul> 
   <li>使 REST API 补丁用户端点的工作方式与 UI 相同 </li> 
   <li>为已清除的任务正确设置 start_date </li> 
   <li>在对其状态运行更新之前，确保 task_instance 存在 </li> 
   <li>使 AirflowDateTimePickerWidget 成为必填字段 </li> 
   <li>在删除旧的渲染任务字段时，重试陷入僵局的事务 </li> 
   <li>修复重试延迟为零时 retry_exponential_backoff 除以零的错误 </li> 
   <li>改进 UI 处理日期的方式 </li> 
   <li>错误修正：dag_bag.get_dag 应返回 None，而不是引发异常 </li> 
   <li>只有当任务是一个有效的实例时才会显示任务模版 </li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fairflow.apache.org%2Fdocs%2Fapache-airflow%2F2.2.0%2Fchangelog.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            