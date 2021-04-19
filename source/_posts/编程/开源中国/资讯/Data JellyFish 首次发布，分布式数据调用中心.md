
---
title: 'Data JellyFish 首次发布，分布式数据调用中心'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gblobscdn.gitbook.com/assets%2F-MM-uv7u2JRCBT04nRgz%2F-MM-uyu2zevkRTtF4Hfk%2F-MM-yuoqoM_1ehkqPIva%2Fimage.png?alt=media&token=fe8f239a-a522-4890-aff0-98360c2fbe48'
author: 开源中国
comments: false
date: Mon, 19 Apr 2021 07:32:00 GMT
thumbnail: 'https://gblobscdn.gitbook.com/assets%2F-MM-uv7u2JRCBT04nRgz%2F-MM-uyu2zevkRTtF4Hfk%2F-MM-yuoqoM_1ehkqPIva%2Fimage.png?alt=media&token=fe8f239a-a522-4890-aff0-98360c2fbe48'
---

<div>   
<div class="content">
                                                                    
                                                        <div>
 Data JellyFish 译文（数据水母）是数据调度中心，实现系统与系统之间，服务与服务之间，与第三方之间的数据100%准实时同步。
</div> 
<div> 
 <h3><strong>用途</strong></h3> 
 <ol> 
  <li> <p>与第三方的数据同步</p> </li> 
  <li> <p>内部系统之间的数据同步</p> </li> 
 </ol> 
 <h3><strong>特性</strong></h3> 
 <ol> 
  <li> <p>数据100%传输，不丢失任何一条数据</p> </li> 
  <li> <p>实时性高，相比定时任务每5分钟，半天，一天，而言，在秒级实现同步</p> </li> 
  <li> <p>对接成本低，增量同步时提供一个增量查询接口，全量同步时提供一个全量查询接口</p> </li> 
  <li> <p>无中心化的分布式任务，实现任务分片能力，达到并发处理，实现快速调度的目的</p> </li> 
  <li> <p>每一条数据都有同步的成功或失败记录，历史可查</p> </li> 
  <li> <p>自定义重试策略，固定时长，指数级重试</p> </li> 
  <li> <p>完善的监控信息，有多少同步了，有多少未同步，</p> </li> 
 </ol> 
 <h3><strong>原理</strong></h3> 
 <p>以系统A同步数据到系统B为例，A系统提供一个http接口，实现数据增量或全量的抓取，”Data JellyFish 数据高度中心“ 简称 "DJ" ，DJ 启动生产者任务线 程T1调用A系统的http接口，将数据存储在自己的中间表中，同时，DJ启动消费者任务线程T2调用B系统提供的另一个接受数据的HTTP接口，来完成数据调度</p> 
 <h3><strong>架构图</strong></h3> 
 <p><img src="https://gblobscdn.gitbook.com/assets%2F-MM-uv7u2JRCBT04nRgz%2F-MM-uyu2zevkRTtF4Hfk%2F-MM-yuoqoM_1ehkqPIva%2Fimage.png?alt=media&token=fe8f239a-a522-4890-aff0-98360c2fbe48" width="727" referrerpolicy="no-referrer"></p> 
 <h3><strong>传统数据同步方案比较</strong></h3> 
 <ol> 
  <li> <p>RCP, http协议直接访问第三方，内存中重试三次后，消息丢失</p> </li> 
  <li> <p>定时任务数据同步，延迟高，无分片并发能力</p> </li> 
  <li> <p>MQ,Kafka等，研发对接（保证数据准确传输的）成本高，无流水记录，无法直接回塑</p> </li> 
  <li> <p>每次数据对接都需要重复开发，不具备可用性</p> </li> 
 </ol> 
 <h3><strong>样例图</strong></h3> 
 <p><img src="https://images.gitee.com/uploads/images/2021/0127/221506_57af30a6_5139840.png" width="727" referrerpolicy="no-referrer"></p> 
 <p><img src="https://images.gitee.com/uploads/images/2021/0127/221540_35b289eb_5139840.png" width="727" referrerpolicy="no-referrer"></p> 
 <h3><strong>问题反馈</strong></h3> 
 <p>微信号: freedom-Union<br> 邮件交流： kobe96688@126.com<br> 报告issue: <a href="https://gitee.com/alenfive/data-jelly-fish/issues" target="_blank">https://gitee.com/alenfive/data-jelly-fish/issues</a></p> 
 <p>​<img alt="屏幕截图.png" src="https://images.gitee.com/uploads/images/2020/0915/183440_93549b7f_5139840.png" referrerpolicy="no-referrer"></p> 
</div>
                                        </div>
                                      
</div>
            