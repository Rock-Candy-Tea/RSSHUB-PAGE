
---
title: 'Apache Airflow 2.1.4 发布，Airbnb 开源的调度系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4778'
author: 开源中国
comments: false
date: Mon, 20 Sep 2021 07:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4778'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p><span style="background-color:#ffffff; color:#333333">Apache Airflow 2.1.4  已正式发布，Airflow 是一个灵活、可扩展的工作流自动化和调度系统，可编集和管理数百 PB 的数据流。项目可轻松编排复杂的计算工作流，通过智能调度、数据库和依赖关系管理、错误处理和日志记录，Airflow 可以对从单个服务器到大规模集群的资源进行自动化管理。Airflow 采用 Python 编写，具有高扩展性，能够运行其他语言编写的任务，并允许与常用的体系结构和项目集成，如 AWS S3、Docker、Kubernetes、MySQL、PostgresSQL 等。</span></p> 
 <p><span style="background-color:#ffffff; color:#333333"><strong>主要更新内容</strong></span></p> 
 <ul> 
  <li><span style="background-color:#ffffff; color:#333333">修复弃用错误消息而不是使其静音 </span></li> 
  <li><span style="background-color:#ffffff; color:#333333">限制调度程序创建的排队 dagruns 的数量</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">修复 DagRun 执行顺序从排队到运行没有被正确遵循</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">修复 max_active_runs 不允许将排队的 dagruns 移动到运行状态</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">避免为没有权限的用户重定向循环</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">当用户没有角色时避免无限重定向循环</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">修复图形 TI 模态上的日志链接</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">如果用户没有权限，隐藏变量导入表单</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">改进 dag/task 并发检查</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">修复清除任务实例端点重置所有 DAG 运行错误</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">修复传递给视图的错误参数 </span></li> 
  <li><span style="background-color:#ffffff; color:#333333">修复 LocalTask​​Job 中导致错误的 Sentry 处理程序 </span></li> 
  <li><span style="background-color:#ffffff; color:#333333">限制 colorlog 版本（6.x 不兼容）</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">仅在悬停时显示暂停/取消暂停工具提示 </span></li> 
  <li><span style="background-color:#ffffff; color:#333333">改进具有开放组的 dag 的图形视图加载时间 </span></li> 
  <li><span style="background-color:#ffffff; color:#333333">增加运行列的宽度 </span></li> 
  <li><span style="background-color:#ffffff; color:#333333">修复运行 tis 时的错误查询</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">将 root 添加到树刷新 url </span></li> 
  <li><span style="background-color:#ffffff; color:#333333">不要从 UI 中删除正在运行的 DAG</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">提高提供程序包功能的可发现性</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">不要让 create_dagrun 覆盖显式 run_id</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">错误修复：pid 重置回归以允许在心跳后启动任务</span></li> 
  <li><span style="background-color:#ffffff; color:#333333">在运行时删除 pod 时将任务状态设置为失败 </span></li> 
  <li><span style="background-color:#ffffff; color:#333333">建议内核不要缓存 Airflow 生成的日志文件 </span></li> 
  <li><span style="background-color:#ffffff; color:#333333">在 _check_for_stalled_adopted_tasks 方法中对采用的任务进行排序 </span></li> 
  <li><span style="background-color:#ffffff; color:#333333">修复 MySQLdb 驱动程序的 DagRunState 枚举查询</span></li> 
 </ul> 
 <p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202109.mbox%2F%253Cpony-762f1fed708bdb04af3f52cafbce77c382effa7a-9170b6b70b16c8f755e1b108079c587323d22225%40announce.apache.org%253E" target="_blank">更新公告</a>。</p> 
</div>
                                        </div>
                                      
</div>
            