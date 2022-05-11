
---
title: 'Carina 全新版本 V0.10 发布 ：支持裸盘作为存储卷'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static001.geekbang.org/infoq/bf/bf834f493bffc19d6c1b638f81ffda0c.jpeg?x-oss-process=image/resize,p_80/auto-orient,1'
author: 开源中国
comments: false
date: Wed, 11 May 2022 15:49:00 GMT
thumbnail: 'https://static001.geekbang.org/infoq/bf/bf834f493bffc19d6c1b638f81ffda0c.jpeg?x-oss-process=image/resize,p_80/auto-orient,1'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="margin-left:auto; margin-right:auto; text-align:center"> 
 <div style="margin-left:auto; margin-right:auto">
  <img src="https://static001.geekbang.org/infoq/bf/bf834f493bffc19d6c1b638f81ffda0c.jpeg?x-oss-process=image/resize,p_80/auto-orient,1" referrerpolicy="no-referrer">
 </div> 
</div> 
<p style="margin-left:0; margin-right:0"><strong>Carina</strong> 是由博云主导并发起的云原生本地存储项目（GitHub 地址为：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxie.infoq.cn%2Flink%3Ftarget%3Dhttps%253A%252F%252Fgithub.com%252Fcarina-io%252Fcarina" target="_blank">https://github.com/carina-io/carina</a>），目前已经进入 CNCF 全景图。</p> 
<p style="margin-left:0; margin-right:0"><strong>Carina</strong> 旨在为云原生环境中的有状态应用提供<strong>高性能</strong>、<strong>免运维</strong>的本地存储解决方案，具体存储卷生命周期管理、本地设备管理、智能调度等能力。Carina 作为博云容器云平台的组件之一，<strong>已经在多个金融机构的生产环境中稳定运行多年</strong>。</p> 
<hr> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong>重大喜讯！！！重大喜讯 ！！！重大喜讯！！！</strong></p> 
<p style="margin-left:0px; margin-right:0px">Carina 项目组于 4 月 28 日发布了 V0.10.0 版本。该版本实现了诸多升级迭代，笔者将通过本篇文章给大家初步介绍 Carina 的全新版本。</p> 
<h2 style="margin-left:0; margin-right:0">版本重要变更</h2> 
<p style="margin-left:0; margin-right:0">Carina V0.10.0 版本对如下内容进行了改动或升级：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">支持将裸盘挂载到容器内直接使用</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">velero 备份存储卷支持</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 CRD 资源 NodeStorageResource 替代原将磁盘设备注册到 Node 节点</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">变更 sc 及 pod 中自定义字段</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">使用 job 生成 webhook 证书，替代原有脚本生成证书方式</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">移除代码内置 csi.proto 文件并升级 CSI_VERSION=1.5</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">增加更多的英文文档，Carina 支持中英双文档</p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0">版本详细介绍</h2> 
<p style="margin-left:0; margin-right:0">完整的参数介绍请见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxie.infoq.cn%2Flink%3Ftarget%3Dhttps%253A%252F%252Fgithub.com%252Fcarina-io%252Fcarina%252Fblob%252Fmain%252Fdocs%252Fmanual_zh%252Fconfigrations.md" target="_blank">https://github.com/carina-io/carina/blob/main/docs/manual_zh/configrations.md</a></p> 
<p style="margin-left:0; margin-right:0">下表是本次更新中的参数变更：</p> 
<div style="margin-left:auto; margin-right:auto; text-align:center"> 
 <div style="margin-left:auto; margin-right:auto">
  <img src="https://static001.geekbang.org/infoq/64/641ea1ee874658dce11e99296b0265c9.png" referrerpolicy="no-referrer">
 </div> 
</div> 
<ul> 
 <li>新增 CRD 资源 NodeStorageResource，该功能为节点注册的替代功能，该资源反应了对应节点上的磁盘及 LVM 卷等信息，该资源对于用户来说为只读资源。</li> 
</ul> 
<div style="margin-left:auto; margin-right:auto; text-align:center"> 
 <div style="margin-left:auto; margin-right:auto">
  <img src="https://static001.geekbang.org/infoq/6e/6e16e62616b8a8df6f5d7499d199b5db.png" referrerpolicy="no-referrer">
 </div> 
</div> 
<ul> 
 <li>用 velero 备份存储卷，详细信息参考文档</li> 
</ul> 
<div style="margin-left:auto; margin-right:auto; text-align:center"> 
 <div style="margin-left:auto; margin-right:auto">
  <img src="https://static001.geekbang.org/infoq/7e/7ef79309091c7c3db24c95b9ee72e4a2.png" referrerpolicy="no-referrer">
 </div> 
</div> 
<p style="margin-left:0; margin-right:0"> </p> 
<h2 style="margin-left:0; margin-right:0">裸盘支持</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">裸盘设计文档请见：https://github.com/carina-io/carina/blob/main/docs/design/design-raw-manger.md</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">裸盘测试文档请见：https://github.com/carina-io/carina/blob/main/docs/manual_zh/raw-manager.md</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">定义配置文件，规定某些磁盘作为裸盘提供服务</p> </li> 
</ul> 
<div style="margin-left:auto; margin-right:auto; text-align:center"> 
 <div style="margin-left:auto; margin-right:auto">
  <img src="https://static001.geekbang.org/infoq/43/4398893c84722e7c93c312f1923b9610.png" referrerpolicy="no-referrer">
 </div> 
</div> 
<ul> 
 <li>简单演示</li> 
</ul> 
<div style="margin-left:auto; margin-right:auto; text-align:center"> 
 <div style="margin-left:auto; margin-right:auto">
  <img src="https://static001.geekbang.org/infoq/91/918f9b88b83b1f9c9949465c20a7536a.gif" referrerpolicy="no-referrer">
 </div> 
</div>
                                        </div>
                                      
</div>
            