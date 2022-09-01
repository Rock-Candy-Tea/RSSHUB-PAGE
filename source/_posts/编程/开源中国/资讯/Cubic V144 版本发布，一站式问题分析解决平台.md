
---
title: 'Cubic V1.4.4 版本发布，一站式问题分析解决平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cors.zfour.workers.dev/?http://pic.jiagoujishu.com/article/application.png'
author: 开源中国
comments: false
date: Thu, 01 Sep 2022 08:41:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://pic.jiagoujishu.com/article/application.png'
---

<div>   
<div class="content">
                                                                                            <h2>一、Cubic是什么</h2> 
<p>还在为线上问题而烦恼吗？ Cubic 致力于<strong>一站式问题分析解决平台</strong></p> 
<p><code>Cubic</code> 一站式问题定位平台，以agent的方式无侵入接入应用，提供各种指标，动态线程堆栈追踪，完整集成arthas功能模块，致力于应用级监控，帮助开发人员快速定位问题。</p> 
<p>官方网站：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcubic.jiagoujishu.com%2F" target="_blank">https://cubic.jiagoujishu.com</a></p> 
<p>Gitee: <a href="https://gitee.com/dromara/cubic">https://gitee.com/dromara/cubic</a></p> 
<p>Github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fcubic" target="_blank">https://github.com/dromara/cubic</a></p> 
<p>Demo: <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F47.104.79.116%3A6080%2F" target="_blank">http://47.104.79.116:6080</a></p> 
<p>特性：</p> 
<ul> 
 <li>1、兼容性：整体监控不管你是IDC、ECS、Docker部署，都可完美兼容</li> 
 <li>2、易用： 无需任何配置，开箱即用，基于agent无侵入接入，升级应用端无感知</li> 
 <li>3、强大： 支持对应用的基础监控、堆栈监控、线程池监控等等</li> 
 <li>4、高扩展：提供良好的扩展接口，给你自主选择</li> 
</ul> 
<h2>二、此次版本更新主要功能：</h2> 
<p>1、增加<code>用户管理模块</code> 用于管理用户权限及信息</p> 
<p>2、优化<code>线程栈历史记录</code> 对历史堆栈信息进行数据高度压缩，减少通信负载</p> 
<p>3、优化 <code>线程池监控</code> 切入原生JDK线程池，对原生数据进行无缝监控</p> 
<p>4、优化<code>proxy</code>代理层数据连接池，加速数据读写速度</p> 
<h2>三、功能展示</h2> 
<p>1、实例中心</p> 
<p><img alt="实例中心" src="https://cors.zfour.workers.dev/?http://pic.jiagoujishu.com/article/application.png" referrerpolicy="no-referrer"></p> 
<p>2、基础信息</p> 
<p><img alt="基础信息" src="https://cors.zfour.workers.dev/?http://pic.jiagoujishu.com/article/base.png" referrerpolicy="no-referrer"></p> 
<p>3、依赖监控</p> 
<p><img alt="依赖监控" src="https://cors.zfour.workers.dev/?http://pic.jiagoujishu.com/article/jarmonitor.png" referrerpolicy="no-referrer"></p> 
<p>4、Arthas命令</p> 
<p><img alt="Arthas命令1" src="https://cors.zfour.workers.dev/?http://pic.jiagoujishu.com/article/arthas1.png" referrerpolicy="no-referrer"></p> 
<p><img alt="arthas2" src="https://cors.zfour.workers.dev/?http://pic.jiagoujishu.com/article/arthas2.png" referrerpolicy="no-referrer"></p> 
<p>5、线程池监控</p> 
<p><img alt="线程池监控" src="https://cors.zfour.workers.dev/?http://pic.jiagoujishu.com/article/threadpool.png" referrerpolicy="no-referrer"></p> 
<p>6、实时线程栈</p> 
<p><img alt="实时线程栈" src="https://cors.zfour.workers.dev/?http://pic.jiagoujishu.com/article/dump.png" referrerpolicy="no-referrer"></p> 
<p>7、历史线程栈</p> 
<p><img alt="历史线程栈" src="https://cors.zfour.workers.dev/?http://pic.jiagoujishu.com/article/historydump.png" referrerpolicy="no-referrer"></p> 
<p>8、用户管理</p> 
<p><img alt="用户管理" src="https://cors.zfour.workers.dev/?http://pic.jiagoujishu.com/%E5%AE%9E%E4%BE%8B%E4%B8%AD%E5%BF%83.png" referrerpolicy="no-referrer"></p> 
<h2>四、开发中的功能</h2> 
<p>详细时间请查看： <a href="https://gitee.com/dromara/cubic/board">https://gitee.com/dromara/cubic/board</a></p> 
<table> 
 <thead> 
  <tr> 
   <th>功能名称</th> 
   <th>版本</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>线程栈分析</td> 
   <td>V1.5</td> 
  </tr> 
  <tr> 
   <td>公共报警模块</td> 
   <td>V1.5</td> 
  </tr> 
  <tr> 
   <td>火焰图</td> 
   <td>V1.5</td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            