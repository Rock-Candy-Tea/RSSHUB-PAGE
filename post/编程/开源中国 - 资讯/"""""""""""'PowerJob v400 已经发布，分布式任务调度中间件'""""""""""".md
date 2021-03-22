
---
title: """""""""""'PowerJob v4.0.0 已经发布，分布式任务调度中间件'"""""""""""
categories: 
    - 编程
    - 开源中国 - 资讯
author: 开源中国 - 资讯
comments: false
date: Mon, 22 Mar 2021 01:04:00 GMT
thumbnail: ''
---

<div>   
<div class="content">
                                                                                            <p>PowerJob v4.0.0 已经发布，分布式任务调度中间件</p> 
<p>此版本更新内容包括：</p> 
<h1>PowerJob 主框架</h1> 
<h2>Features</h2> 
<ul> 
 <li>支持任务复制、工作流复制，提升配置效率</li> 
 <li>支持单应用下启动多个 powerjob-worker</li> 
 <li>使用 kryo 替换 jackson-cbor 作为默认的序列化框架，提升通讯性能的同时降低依赖冲突的可能性</li> 
 <li>工作流能力基础升级，支持任务重复导入、参数个性化、节点禁用、失败跳过</li> 
 <li>工作流能力运维能力升级，支持节点标记成功、原地重试</li> 
 <li>工作流配置界面升级，使用 AntV-G6 重写工作流画布组件，并抽取为单独模块 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerJob%2Fpower-workflow" target="_blank">power-workflow</a></li> 
</ul> 
<h2>Compatibility</h2> 
<blockquote> 
 <p>PowerJob 4.x 是框架向新时代和新目标迈进的一个版本，因此做了大幅度的改动。同时由于一些功能上的升级与变更，框架不得不产生一些 broken change。不过不用担心，我们提供了一系列方案帮助您完成升级。</p> 
</blockquote> 
<ul> 
 <li>PowerJob 4.x 改动一览：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fpowerjob%2Fguidence%2Fuyf17o%23lznVx" target="_blank">点击查看</a></li> 
 <li>PowerJob 4.x 升级指南：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fpowerjob%2Fguidence%2Fdd5hpe%23lU4oI" target="_blank">点击查看</a></li> 
</ul> 
<h2>Acknowledgements</h2> 
<blockquote> 
 <p>真的非常感谢大家的辛勤付出～</p> 
</blockquote> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FEcho009" target="_blank">Echo from CVTE</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhaodeezhu" target="_blank">Max from CVTE</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjjnnzb" target="_blank">宁远</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Forgs%2FPowerJob%2Fpeople" target="_blank">ocean23、读钓等其他 Team PowerJob 成员</a></li> 
</ul> 
<h1>PowerJob 官方处理器</h1> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhttps%2F%2Fwww.yuque.com%2Fpowerjob%2Fguidence%2Fofficial_processor" target="_blank">点击查看使用教程</a></p> 
<h2>Features</h2> 
<ul> 
 <li>新发布：Spring 数据源 SQL 处理器</li> 
 <li>新发布：Dynamic 数据源 SQL 处理器</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/KFCFans/PowerJob/releases/v4.0.0">https://gitee.com/KFCFans/PowerJob/releases/v4.0.0</a></p>
                                        </div>
                                      
</div>
            