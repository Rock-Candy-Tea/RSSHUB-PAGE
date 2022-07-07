
---
title: 'Dolphin Scheduler 3.0.0-beta-2 发布，LDAP 登录失败等问题已修复'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ba0c616a48712105f12d03da34735963240.png'
author: 开源中国
comments: false
date: Thu, 07 Jul 2022 10:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ba0c616a48712105f12d03da34735963240.png'
---

<div>   
<div class="content">
                                                                                            <p><img height="383" src="https://oscimg.oschina.net/oscnet/up-ba0c616a48712105f12d03da34735963240.png" width="900" referrerpolicy="no-referrer"></p> 
<p>  </p>
<p>  </p>
<p style="margin-left:0; margin-right:0"><span>近日，Apache Dolphin Scheduler 迎来了 3.0.0-beta-2 版本的正式发布。新版本主要针对 3.0.0-beta-1 进行了代码和文档的修复，具体更新详见下文。</span></p> 
<p></p> 
<p></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:center"><strong>1</strong> Bug 修复</h2> 
<p style="text-align:center">Bug Fix</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复邮件告警模板分隔线问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复Standalone模式下数据初始化问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复监控中心DB不存在时的页面展示问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复创建工作流参数无效问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复K8S部署时zookeeper端口异常问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复Standalone模式下服务启动失败问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复LDAP登录失败问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Python API: 修复同一个项目下不同工作流的任务组件名称不支持重名问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Python API: 修复SQL任务组件SQL类型错误问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复资源文件重命名表单异常问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复根据定时设置获取工作流可执行时间错误问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>升级了Logback、Log4j等模块依赖</span></p> </li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px; text-align:center"><strong>2 </strong><span>文档修改</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:center">Document Revision</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span>更正部署文档</span></p> </li> 
 <li> <p><span>更新使用文档：参数传递、全局参数、参数优先级文档，告警组件向导、Telegram、钉钉告警文档，告警FAQ文档，Shell组件文档，Switch任务组件文档，资源中心配置详情文档，工作流定义补数文档  </span></p> </li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px; text-align:center"><strong>3 </strong><span>具体修改</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:center">Details</p> 
<p><span>可以在 https://github.com/apache/dolphinscheduler/releases/tag/3.0.0-beta-2 中找到全部修改记录。</span></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:center"><strong>4 </strong><span>资源下载</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:center">Assets</p> 
<p><span>https://dolphinscheduler.apache.org/zh-cn/download/download.html</span></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:center"><strong>5 </strong><span>致谢</span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:center">Acknowledgement</p> 
<p><span>感谢所有 3.0.0-beta-2 版本的贡献者（按首字母排序），是你们的不懈努力让社区不断进步！</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:center"><span>aiwenmo, Amy0104, chuxing, Desperado2, Devosend, Eric Gao, guodong, HomminLee, Hwting, Jiajie Zhong, juzimao, Kerwin, liubo1990, Mr.An, PJ Fanning, QuakeWang, songjianet, Wenjun Ruan, xiangzihao, Yiming Guo, 阿福Chris, 陈家名, 旺阳</span></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:center"><span><strong>参与贡献</strong></span></h2> 
<p style="margin-left:0px; margin-right:0px; text-align:center"><span style="background-color:#feffff">随着国内开源的迅猛崛起，Apache DolphinScheduler 社区迎来蓬勃发展，为了做更好用、易用的调度，真诚欢迎热爱开源的伙伴加入到开源社区中来，为中国开源崛起献上一份自己的力量，让本土开源走向全球。</span></p> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#000000">参与 DolphinScheduler 社区有非常多的参与贡献的方式，包括：</span></p> 
<p><img height="39" src="https://oscimg.oschina.net/oscnet/up-ea758b6473d04cb40d07c825a8c874043fd.png" width="833" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">贡献第一个PR(文档、代码) 我们也希望是简单的，第一个PR用于熟悉提交的流程和社区协作以及感受社区的友好度。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">社区汇总了以下适合新手的问题列表：https://github.com/apache/dolphinscheduler/issues/5689</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">非新手问题列表：https://github.com/apache/dolphinscheduler/issues?q=is%3Aopen+is%3Aissue+label%3A%22volunteer+wanted%22</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">如何参与贡献链接：https://dolphinscheduler.apache.org/zh-cn/docs/development/contribute.html</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">来吧，DolphinScheduler开源社区需要您的参与，为中国开源崛起添砖加瓦吧，哪怕只是小小的一块瓦，汇聚起来的力量也是巨大的。</span></p> 
<p style="margin-left:0; margin-right:0"><span><span style="color:#0052ff">参与开源可以近距离与各路高手切磋，迅速提升自己的技能，如果您想参与贡献，我们有个贡献者种子孵化群，可以添加社区小助手</span><span style="color:#0052ff">微信(Leonard-ds) ，手把手教会您( 贡献者不分水平高低，有问必答，关键是有一颗愿意贡献的心 )。</span></span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#0052ff">添加小助手微信时请说明想参与贡献。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">来吧，开源社区非常期待您的参与。</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            