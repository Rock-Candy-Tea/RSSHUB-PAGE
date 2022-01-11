
---
title: '谐云DevOps产品可信源管理从容应对Apache Log4j2高危漏洞'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220105/41fa6015bfa356a9c2119ed18959d6ee.png'
author: Dockone
comments: false
date: 2022-01-11 06:10:16
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220105/41fa6015bfa356a9c2119ed18959d6ee.png'
---

<div>   
<br>2021年12月10日，国家信息安全漏洞共享平台（CNVD）收录了Apache Log4j2远程代码执行漏洞（CNVD-2021-95914）,攻击者利用该漏洞，可在未授权的情况下远程执行代码。Log4j作为目前最优秀的Java日志记录工具框架之一，被大量用于业务系统开发，影响面极为广泛。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220105/41fa6015bfa356a9c2119ed18959d6ee.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220105/41fa6015bfa356a9c2119ed18959d6ee.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>产品介绍<br>
<br>可信源管理从项目持续集成、发版门禁源头堵截高危漏洞上线，维护应用依赖版本库，当发现漏洞后可以直接创建工单针对性修复。平台支持定期从中央漏洞库拉取漏洞，在流水线运行过程中对使用到的依赖包做扫描校验，在申请发布前的对发布版本做扫描拦截，扫描范围包括漏洞、基线、可信源匹配，可信源冲突、门禁。在代码合并前经过多人审批，并设置分支保护权限，从而规避相应风险，提高安全等级。<br>
<br>建立可信漏洞库<br>
<br>定期从中央漏洞库拉取漏洞导入系统，支持全量同步、增量同步和手动同步。在收到漏洞后可以进行漏洞影响分析，查看漏洞的关联应用血缘和可信源血缘，并发送预警通知。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220105/dca6c6c55a4a85fa827f4c2743c81087.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220105/dca6c6c55a4a85fa827f4c2743c81087.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>（漏洞管理-列表）<br>
2021年12月10日，Log4j漏洞发布后可信源产品捕获该漏洞，平台管理员可以设置漏洞解决方案并且为相关应用责任人创建工单。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220105/8fdfecc1e5f4a59c2697ba7bc33e0dd1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220105/8fdfecc1e5f4a59c2697ba7bc33e0dd1.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>（漏洞管理-漏洞详情）<br>
<br>漏洞血缘关系，火眼金睛让高危项目无处遁形<br>
<br>平台可以维护可信源依赖的版本库，包含可信源相关的所有依赖的版本。当漏洞到来时候可以系统可将漏洞影响的所有可信源版本关联出来。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220105/42979c7acad21ba776a0dc3da3618248.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220105/42979c7acad21ba776a0dc3da3618248.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>（漏洞管理-可信源血缘）<br>
平台维护每个应用的依赖的版本库，包含线上基线版本。当漏洞到来时候可以系统可将漏洞影响的所有所有版本关联出来，管理员针对受影响应用可一键发起工单，通知对应应用研发团队处理。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220105/e7884cf9238ed54a37cc1a9ea14143a0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220105/e7884cf9238ed54a37cc1a9ea14143a0.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>（漏洞管理-应用可信源）<br>
<br>源码级扫描，源头阻断高危依赖包上线<br>
<br>在应用发布的流水线上，通过配置获取应用依赖 流程节点，可分析Java应用依赖并记录在可信源数据库中，可以配置可信源扫描流水线环节，包括黑名单扫描、漏洞门禁扫、可信源基线扫描、可信源匹配扫描、可信源冲突扫描、可信源依赖差异扫描，进行应用全方位的依赖安全分析。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220105/5e1bbfa561fc319f128e7d7aebd32c20.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220105/5e1bbfa561fc319f128e7d7aebd32c20.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>（流水线配置）<br>
流水线执行后可查看可信源分析报告，如下图对应Log4j的依赖已发现在报告中。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220105/95b5371634605d8a9c85d4d67d9b7daa.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220105/95b5371634605d8a9c85d4d67d9b7daa.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>（流水线检查报告）<br>
对于应用生产发布需要提交发布申请，发布申请会进行必要的申请审核，当有高危依赖漏洞时，无法发布生产环节，从源头阻断漏洞的上线。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220105/9280536ed662a8f32b905bdc1d85c249.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220105/9280536ed662a8f32b905bdc1d85c249.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>（工单-检查项）<br>
<br>修复方式<br>
<br>临时修复建议：选择任意一种方式即可<br>
杜绝外网访问<br>
jvm参数 -Dlog4j2.formatMsgNoLookups=true <br>
log4j2.formatMsgNoLookups=True <br>
系统环境变量<br>
FORMAT_MESSAGES_PATTERN_DISABLE_LOOKUPS 设置为true <br>
<br>通用修复建议：<br>
使用 log4j2 最新安全版本：<br>
<a href="https://github.com/apache/logging-log4j2/releases/tag/log4j-2.15.0-rc2" rel="nofollow" target="_blank">https://github.com/apache/logg ... 0-rc2</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    <a href="http://dockone.io/uploads/article/20220105/932e8c8c3a52e731698a228122402558.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220105/932e8c8c3a52e731698a228122402558.png" class="img-polaroid" alt="首图.png" referrerpolicy="no-referrer"></a>
                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            