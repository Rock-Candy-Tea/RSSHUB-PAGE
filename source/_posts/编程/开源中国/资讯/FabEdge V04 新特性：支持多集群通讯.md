
---
title: 'FabEdge V0.4 新特性：支持多集群通讯'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic3.zhimg.com/80/v2-589415c510dd57fd296f257b77b2025a_1440w.jpg'
author: 开源中国
comments: false
date: Thu, 13 Jan 2022 13:45:00 GMT
thumbnail: 'https://pic3.zhimg.com/80/v2-589415c510dd57fd296f257b77b2025a_1440w.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">边缘计算是指在靠近物或数据源头的⼀侧，采用网络、计算、存储、应用核心能力为⼀体的开放平台，就近提供最近端服务。其应用程序在边缘侧发起，产生更快的网络服务响应，满足行业在实时业务、应⽤智能、安全与隐私保护等方面的基本需求。边缘计算处于物理实体和⼯业连接之间，或处于物理实体的顶端。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://pic3.zhimg.com/80/v2-589415c510dd57fd296f257b77b2025a_1440w.jpg" width="718" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">根据计算能力大小，边缘计算可以分为两⼤类：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong>轻边缘</strong>：计算能力受限，网络条件差，业务单⼀，数量庞⼤，地理位置分散，⽐如智慧小区，车联网，无人机等。</li> 
 <li><strong>重边缘</strong>：计算能力相对充足，网络条件相对稳定，业务复杂，可靠性，安全性有⼀定要求，比如5G MEC，工业互联网，智慧城市等。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://pic4.zhimg.com/80/v2-e5a192258c957c3228b0c939a0a33907_1440w.jpg" width="710" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">FabEdge 是⼀个基于 kubernetes 构建的，专注于边缘计算场景的容器网络⽅案，解决了边缘计算场景下⽹络管理复杂，割裂互不通信，缺少拓扑感知能力，无法提供就近访问等问题，使能云边、边边之间的业务协同。FabEdge支持 KubeEdge，SuperEdge， OpenYurt 等边缘计算框架管理的轻量边缘节点。<strong>在最新发布的V0.4版中，加⼊对重边缘，也就是边缘集群的⽀持，完成了对所有边缘场景的全覆盖。</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://pic3.zhimg.com/80/v2-35f86f577967702de5906acc6d25e45e_1440w.jpg" width="717" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">以上图为例，共有三个集群，集群 blue 是 host 集群，负责管理其它集群的通讯；集群 red，green 是两个成员集群，会上报本集群的网络配置信息到 host 集群 blue。将集群 red 和 green 加入 community1 后，FabEdge会自动建立集群 red 和 green 之间的隧道，允许两个集群之间的 pod 和 service 之间的互访。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">FabEdge 多集群通讯的的交互过程见下图：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://pic2.zhimg.com/80/v2-fc366d91a9132008470e28b8c2a2afd1_1440w.jpg" width="706" referrerpolicy="no-referrer"></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">1. 在 host 集群中先创建集群 green 和 red，获取相应 token。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">2. 使⽤获取的token注册集群 green 和 red。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">3. 集群 green 和 red 汇报本集群网络端点信息到host集群。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">4. 将集群 green 和 red 加⼊⼀个 community。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">5. 集群 green 和 red 定时从 host 集群拉取远程的端点信息。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">6. host集群根据 community 信息，为集群 green 和 red 下发相关的端点信息到成员集群 operator。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">7. 成员集群 green 和red的 operator 为自己 connector 更新 configmap。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">8. 成员集群 green 和 red 的 connector 根据⾃⼰的 configmap 发起到对⽅的隧道。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">9. 隧道建⽴成功后，成员集群 green 和 red 可以互相通讯。</p>
                                        </div>
                                      
</div>
            