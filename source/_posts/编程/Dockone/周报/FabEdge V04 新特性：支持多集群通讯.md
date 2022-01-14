
---
title: 'FabEdge V0.4 新特性：支持多集群通讯'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/img_convert/458297b630f8df51ca96f3b72bdaa1b1.webp?x-oss-process=image/format,png'
author: Dockone
comments: false
date: 2022-01-14 15:08:24
thumbnail: 'https://img-blog.csdnimg.cn/img_convert/458297b630f8df51ca96f3b72bdaa1b1.webp?x-oss-process=image/format,png'
---

<div>   
<br>边缘计算是指在靠近物或数据源头的⼀侧，采用网络、计算、存储、应用核心能力为⼀体的开放平台，就近提供最近端服务。其应用程序在边缘侧发起，产生更快的网络服务响应，满足行业在实时业务、应⽤智能、安全与隐私保护等方面的基本需求。边缘计算处于物理实体和⼯业连接之间，或处于物理实体的顶端。<br>
<br>​<img src="https://img-blog.csdnimg.cn/img_convert/458297b630f8df51ca96f3b72bdaa1b1.webp?x-oss-process=image/format,png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>根据计算能力大小，边缘计算可以分为两⼤类： <br>
轻边缘：计算能力受限，网络条件差，业务单⼀，数量庞⼤，地理位置分散，⽐如智慧小区，车联网，无人机等。 <br>
重边缘：计算能力相对充足，网络条件相对稳定，业务复杂，可靠性，安全性有⼀定要求，比如5G MEC，工业互联网，智慧城市等。<br>
<br><img src="https://img-blog.csdnimg.cn/img_convert/d63ec4bfd32ed35297f5abffbf3b6d38.webp?x-oss-process=image/format,png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>FabEdge 是⼀个基于 kubernetes 构建的，专注于边缘计算场景的容器网络⽅案，解决了边缘计算场景下⽹络管理复杂，割裂互不通信，缺少拓扑感知能力，无法提供就近访问等问题，使能云边、边边之间的业务协同。FabEdge 支持 KubeEdge，SuperEdge， OpenYurt 等边缘计算框架管理的轻量边缘节点。在最新发布的V0.4版中，加⼊对重边缘，也就是边缘集群的⽀持，完成了对所有边缘场景的全覆盖。<br>
<br><img src="https://img-blog.csdnimg.cn/img_convert/cead1b1553f57572875cef2cb76b7278.webp?x-oss-process=image/format,png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>以上图为例，共有三个集群，集群 blue 是 host 集群，负责管理其它集群的通讯；集群 red，green 是两个成员集群，会上报本集群的网络配置信息到 host 集群 blue。将集群 red 和 green 加入 community1 后，FabEdge 会自动建立集群 red 和 green 之间的隧道，允许两个集群之间的 pod 和 service 之间的互访。<br>
<br>FabEdge 多集群通讯的的交互过程见下图：<br>
<br><img src="https://img-blog.csdnimg.cn/img_convert/5f30f520cf10ff4917d39e2f42a38efb.webp?x-oss-process=image/format,png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<ol><li><br>在 host 集群中先创建集群 green 和 red，获取相应 token。</li><li><br>使⽤获取的token注册集群 green 和 red。</li><li><br>集群 green 和 red 汇报本集群网络端点信息到host集群。</li><li><br>将集群 green 和 red 加⼊⼀个 community。</li><li><br>集群 green 和 red 定时从 host 集群拉取远程的端点信息。</li><li><br>host集群根据 community 信息，为集群 green 和 red 下发相关的端点信息到成员集群 operator。</li><li><br>成员集群 green 和red的 operator 为自己 connector 更新 configmap。</li><li><br>成员集群 green 和 red 的 connector 根据⾃⼰的 configmap 发起到对⽅的隧道。</li><li><br>隧道建⽴成功后，成员集群 green 和 red 可以互相通讯。</li></ol><br>
<br><strong>FabEdge 相关资料</strong><br>
<br><a href="https://mp.weixin.qq.com/s?__biz=MzIzNzA5NzM3Ng==&mid=2651867138&idx=1&sn=5eb87839f41ce918f81540d4d01530d6&chksm=f32930cdc45eb9dbb090bfbe2464bddde7fdda62960254898e35e485854cd3d4ff450cf3ba40&scene=21#wechat_redirect">聚焦支持边缘弱网环境，博云开源FabEdge边缘网络方案</a><br>
<br><a href="https://mp.weixin.qq.com/s?__biz=MzIzNzA5NzM3Ng==&mid=2651869043&idx=1&sn=1d34f09bb434d12dac33eb77f61f12ea&chksm=f32937bcc45ebeaaa8d4ba38825149a8cb65888519bc6c5c4daa66073fffe082456ccb123db9&scene=21#wechat_redirect">FabEdge V0.2 快速安装指南，大幅降低使用门槛</a><br>
<br><a href="https://mp.weixin.qq.com/s?__biz=MzIzNzA5NzM3Ng==&mid=2651868928&idx=1&sn=41491dbbd5063f18f81194a6a2cdeb2e&chksm=f32937cfc45ebed996ebb17e9892f81ee9c96bc2dd0657ef4982d0437cabcc1e69a73858c250&scene=21#wechat_redirect">#社区例会# 第一期 | 视频回看+资料下载</a><br>
<br><a href="https://mp.weixin.qq.com/s?__biz=MzIzNzA5NzM3Ng==&mid=2651869317&idx=1&sn=1934713d19415787d62d063de42d9cff&chksm=f329284ac45ea15c35bf790e4ee11d80c4931ff4d34344abbe0d49f94fb828d1dbcdc4befff0&scene=21#wechat_redirect">#社区例会# 第二期 | V0.2 安装部署过程介绍及实操</a><br>
<br><a href="https://mp.weixin.qq.com/s?__biz=MzIzNzA5NzM3Ng==&mid=2651869576&idx=1&sn=cf75ff077ed7fa78ade1caefe0127211&chksm=f3292947c45ea0519ec9649a68212c075a6f5b994e202bb12c33c57f01f39b09bb247442cd85&scene=21#wechat_redirect">#社区例会# 第三期 | V0.3版本前瞻，实操演示快速上手</a><br>
<br>Github：<br>
<a href="https://github.com/FabEdge/fabedge" rel="nofollow" target="_blank">https://github.com/FabEdge/fabedge</a><br>
<br>官方网站：<br>
<a href="http://www.fabedge.io/" rel="nofollow" target="_blank">http://www.fabedge.io</a><br>
<br>视频回看汇总：<br>
<a href="https://space.bilibili.com/524926244" rel="nofollow" target="_blank">https://space.bilibili.com/524926244</a><br>
<br>点击<a href="https://www.bocloud.com.cn/?source=baidu&plan=ppc&unit=ppc&keyword=boyun&bd_vid=8215255806342678375">BoCloud博云</a>了解更多解决方案
                                
                                                              
</div>
            