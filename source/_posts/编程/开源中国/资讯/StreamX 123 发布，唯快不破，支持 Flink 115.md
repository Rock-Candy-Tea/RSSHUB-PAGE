
---
title: 'StreamX 1.2.3 发布，唯快不破，支持 Flink 1.15'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-41fc9f55dc5ccfdaa187fb3f5c32035a038.png'
author: 开源中国
comments: false
date: Sat, 07 May 2022 03:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-41fc9f55dc5ccfdaa187fb3f5c32035a038.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px; margin-right:0px; text-align:center"><img alt height="460" src="https://oscimg.oschina.net/oscnet/up-41fc9f55dc5ccfdaa187fb3f5c32035a038.png" width="100%" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0px; margin-right:0px; text-align:center"><span style="color:#0052ff"><span><span>G</span><span>i</span><span>t</span><span>e</span><span>e</span><span>:</span><span> </span><span> </span><span>h</span><span>t</span><span>t</span><span>p</span><span>s</span><span>:</span><span>/</span><span>/</span><span>g</span><span>i</span><span>t</span><span>e</span><span>e</span><span>.</span><span>c</span><span>o</span><span>m</span><span>/</span><span>s</span><span>t</span><span>r</span><span>e</span><span>a</span><span>m</span><span>x</span><span>h</span><span>u</span><span>b</span><span>/</span><span>s</span><span>t</span><span>r</span><span>e</span><span>a</span><span>m</span><span>x</span></span></span></p> 
<p style="color:#333333; margin-left:0px; margin-right:0px; text-align:center"><span style="color:#0052ff"><span><span>G</span><span>i</span><span>t</span><span>h</span><span>u</span><span>b</span><span>:</span><span> </span><span><span> </span></span><span>h</span><span>t</span><span>t</span><span>p</span><span>s</span><span>:</span><span>/</span><span>/</span><span>g</span><span>i</span><span>t</span><span>h</span><span>u</span><span>b</span><span>.</span><span>c</span><span>o</span><span>m</span><span>/</span><span>s</span><span>t</span><span>r</span><span>e</span><span>a</span><span>m</span><span>x</span><span>h</span><span>u</span><span>b</span><span>/</span><span>s</span><span>t</span><span>r</span><span>e</span><span>a</span><span>m</span><span>x</span></span></span><br>  </p> 
<div style="margin-left:0px; margin-right:0px; text-align:left">
 <span><span style="color:#333333"><span><span>S</span><span>t</span><span>r</span><span>e</span><span>a</span><span>m</span><span>X</span><span><span> </span></span><span>让</span><span>流</span><span>处</span><span>理</span><span>更</span><span>简</span><span>单</span><span>，</span><span>F</span><span>l</span><span>i</span><span>n</span><span>k</span><span><span> </span></span><span>&</span><span><span> </span></span><span>S</span><span>p</span><span>a</span><span>r</span><span>k</span><span><span> </span></span><span>极</span><span>速</span><span>开</span><span>发</span><span>框</span><span>架</span><span>，</span><span>流</span><span>批</span><span>一</span><span>体</span><span>一</span><span>站</span><span>式</span><span>大</span><span>数</span><span>据</span><span>平</span><span>台</span><span>。今天</span></span></span></span>
 <span style="background-color:#ffffff; color:#222222">迎来了</span>
 <strong style="color:#222222"><span style="color:#0052ff"> </span></strong>
 <span style="background-color:#ffffff; color:#222222">1.2.3 Release 版本的正式发布！本次</span>
 <span style="background-color:#ffffff; color:#222222">增加了诸多新特性，修复了一些 bug ，对 StreamX 的易用性、稳定性等方面进行了加强，欢迎大家下载使用！</span>
</div> 
<p> </p> 
<h1 style="margin-left:0px; margin-right:0px"><span style="color:#0052ff"><strong> 1.重要更新</strong></span></h1> 
<p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff; color:#222222">在 1.2.3 版本中，StreamX 支持了 </span><span style="background-color:#ffffff; color:#0052ff"><strong>最新的 Apache Flink 1.15.0</strong></span><span style="background-color:#ffffff; color:#222222"> ，在使用上还是一如既往的简洁丝滑。同时支持了</span><strong><span style="background-color:#ffffff; color:#0052ff"> Scala 2.11 / 2.12</span></strong><span><span style="background-color:#ffffff; color:#222222"> 从此可以自由的选择 Scala、重新划分了 Datastream Connector 模块、使得项目结构更清晰合理，增加了 ES 5 / 6 / 7 的 Datastream Connector ，开放了RESTApi 能力, 使得 StreamX 可以很方便的和其他系统集成。并且修复了一些 bug<span> </span></span>。具体明细如下:</span></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li> <p><span><span>新增</span>对 Scala 2.12 的支持 </span></p> </li> 
 <li> <p><span><span>新增<span>对</span></span> Flink 1.15<span><span> </span>的</span><span>支持</span><span> </span></span></p> </li> 
 <li> <p><span><span>新增 RestApi 与外部系统的集成能力</span></span></p> </li> 
 <li> <p><span>新增 ES 5 / 6 / 7 <span>Datastream</span><span> connector</span></span></p> </li> 
 <li> <p><span>新</span><span>增</span><span><span> </span>Flink Cluster 集群管理 ( yarn | k8s )</span></p> </li> 
 <li> <p><span>新增 Flink SQL <span>Pulsar</span><span> </span>connector</span></p> </li> 
 <li> <p><span>新增 </span><span>F</span><span>li</span><span>nk SQL </span><span>Http</span><span> </span><span>c</span><span>onnecto</span><span>r</span></p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:center"> </p> 
<p style="margin-left:0px; margin-right:0px; text-align:center"><img alt src="https://oscimg.oschina.net/oscnet/up-9ceff5ac9630dcba294e0e9e7c61fd9b268.jpg" referrerpolicy="no-referrer"><br>  </p> 
<h1><span style="color:#0052ff"><strong>2.修复增强</strong></span></h1> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复 hadoop 3 环境下 kerberos 认证续期相关的 bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复项目编译可能存在的不能输出日志的 bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复 tm managed memory参数设置不能为0的 bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复 jobId 为 0**0 导致任务恢复时不能正确识别 savepoint 的 bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复项目修改后未出现编译按钮, 不能重新编译项目的bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>增强在添加 Flink Home 时对 scala 版本的验证</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>重构 Datastream connector模块,模块和包名重新划分</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>连接器的示例程序迁移至 streamx-quickstart</span><br>  </p> </li> 
</ul> 
<h1><span style="color:#0052ff"><strong>3.已有能力</strong></span></h1> 
<p><strong>系统管理</strong><br>     [√] 用户管理, 新增,修改,删除,多租户支持<br>     [√] 角色管理, 新增,修改,删除<br>     [√] 菜单管理, 新增,修改,删除, 权限管理(到按钮级别的权限控制)<br>     [√] REST Token 管理</p> 
<p><strong>项目管理</strong><br>     [√] 项目创建,删除(目前只支持git)<br>     [√] 项目编译,实时查看编译日志<br>     [√] 项目列表过滤查询,分页</p> 
<p><strong>作业管理</strong><br>     [√] 作业创建，删除，编辑，更新，保存，常规参数配置<br>     [√] 作业启动，停止，重启，删除，火焰图(非flink内置)<br>     [√] 停止时自动savePoint,启动时从savePoint恢复<br>     [√] 作业列表的查看，过滤，分页。<br>     [√] 可视化 Flink SQL 编辑器,格式化，语法校验，保存<br>     [√] flinkSQL 任务多版本的支持<br>     [√] yarn-per-job 部署模式<br>     [√] yarn-application 部署模式<br>     [√] yarn-session部署模式<br>     [√] k8s-native-application 部署模式<br>     [√] k8s-native-session 部署模式<br>     [√] standalone 部署模式<br>     [√] 任务历史版本备份和回滚<br>     [√] 任务启动失败的日志在线查看<br>     [√] 任务依赖管理,支持标准maven pom坐标的依赖和手动上传jar<br>     [√] 任务实时状态显示(实际任务保持一致)<br>     [√] 任务监控,失败告警,发送邮件通知,自动重启<br>     [√] 本地上传jar任务的支持<br>     [√] 操作接口开放(REST请求可以控制任务启动|停止|savePoint等) <br>     [√] 告警,重启策略, 针对checkpoint连续失败的处理(邮件告警|重启)<br>     [√] 支持所有 Flink sql connector<br>     [√] 支持所有 Flink UDF</p> 
<p><br> <strong>兼容性</strong><br>     [√] Hadoop 2 / 3 的支持<br>     [√] kerberos的认证支持<br>     [√] 多版本flink的支持(flink 1.12.x,1.13.x, 1.14.x, 1.15.0)<br>     [√] Scala 2.11 / 2.12 的支持</p> 
<h1><span style="color:#0052ff"><strong>4.感谢贡献者</strong></span></h1> 
<p style="color:#222222; margin-left:0px; margin-right:0px"><span>StreamX 的发展离不开社区的 C</span><span style="background-color:#ffffff; color:#000000">ontributor</span><span> 们的付出的积极努力,<span> </span>本次又涌现一批积极的开发者<span>, </span></span><span style="color:#0052ff">Flink 1.15</span><span><span> </span><span style="background-color:#ffffff; color:#222222">、</span><span> </span></span><span style="color:#0052ff">RestAp</span><span>i<span style="background-color:#ffffff; color:#222222">、</span><span> </span></span><span style="color:#0052ff">Datastream connector重构</span><span><span style="background-color:#ffffff; color:#222222">、</span><span> </span></span><span style="color:#0052ff">Flink Cluster 管理 </span><span>等几个核心特性都是社区的开发者独立贡献的<span>, 特别感谢</span> </span><span style="color:#0052ff">@lvshaokang @<span>lzyyy</span><span> </span>@wangqingrong @xxyykkxx</span><span> 在上述核心特性中所作的努力, </span><strong><span style="color:#0052ff">真诚感谢本次所有参与开发测试讨论的小伙伴</span></strong><span><span>,</span> 以下为 Contributor 名单, 排名不分先后</span></p> 
<p style="color:#222222; margin-left:0px; margin-right:0px"><span>ChunFu<span style="background-color:#ffffff; color:#222222">、</span><span>Gilliam</span><span style="background-color:#ffffff; color:#222222">、</span><span>benjobs</span><span style="background-color:#ffffff; color:#222222">、</span><span>chengyuan</span><span style="background-color:#ffffff; color:#222222">、</span><span>huzk</span><span style="background-color:#ffffff; color:#222222">、</span><span>lvshaokang</span><span style="background-color:#ffffff; color:#222222">、</span><span>lzyyy</span><span style="background-color:#ffffff; color:#222222">、</span><span>sober</span><span style="background-color:#ffffff; color:#222222">、</span><span>wangqingrong</span><span style="background-color:#ffffff; color:#222222">、</span><span>wangrui</span><span style="background-color:#ffffff; color:#222222">、</span><span>xxyykkxx</span><span style="background-color:#ffffff; color:#222222">、</span><span>阿洋</span></span><br>  </p> 
<h1><span style="color:#0052ff"><strong>5.加入我们</strong></span></h1> 
<p><span style="background-color:#ffffff; color:#222222">StreamX 遵循 Apache-2.0 开源协议，将会是个长期更新的活跃项目，自项目开源以来就受到很多同行的关注和认可，目前已经登记生产使用的用户有:<span> </span><strong>尚硅谷</strong>,<span> </span><strong>INMOBI</strong>,<span> </span><strong>JOYME</strong><span> </span>,<span> </span><strong>联通数科</strong><strong>... </strong>更有<strong>百度</strong>这样的一线大厂。StreamX 开源刚满一年，目前全网累计</span><strong style="color:#222222"><span style="color:#0052ff"> 2k star</span></strong><span style="background-color:#ffffff; color:#222222">，</span><span style="background-color:#ffffff; color:#0052ff"><strong><span>贡献者共计36位，总代码量已经突破11万行</span></strong></span><span style="background-color:#ffffff; color:#333333">。StreamX<span> </span></span><span style="background-color:#ffffff; color:#222222">于 2021 年 11 月荣获开源中国</span><span style="background-color:#ffffff; color:#0052ff"><strong>「最有价值开源项目」</strong></span><span style="background-color:#ffffff; color:#222222">。随后荣获</span><span style="background-color:#ffffff; color:#333333">「2021 年度 OSC 中国开源项目评选」</span><span style="background-color:#ffffff; color:#222222">的</span><strong style="color:#222222"><span style="color:#0052ff">「最受欢迎项目」</span></strong><span style="background-color:#ffffff; color:#222222">， 目前已经陆续有多家IT教育机构出相关课程</span><span style="background-color:#ffffff; color:#222222">, 感谢大家支持, 我们会继续努力,  坚信未来会更好。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:center"><img alt height="336" src="https://oscimg.oschina.net/oscnet/up-f18f96cd4196031bcb7a4f1726f9e5823cb.png" width="100%" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:center"><span style="background-color:#ffffff; color:#888888">       [贡献者墙]</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:center"><img alt height="255" src="https://oscimg.oschina.net/oscnet/up-bfe8fa291531921615f2762c11e530bbed8.png" width="100%" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="background-color:#ffffff; color:#888888">       [StreamX 用户墙]</span></p> 
<p> </p> 
<p style="color:#222222; margin-left:0px; margin-right:0px"><span>流批一体，流式数仓，数据湖是大数据领域的趋势，StreamX 虽离这个目标还有一段距离，但我们始终坚信: 道阻且长，行则将至，行而不辍，未来可期。我们会积极进取，做好相关功能持续迭代优化，和社区所有小伙伴一起努力进一步建设好社区，让 StreamX 成为一个功能完善，体验更佳，用户更多的产品，再获得更多认可。</span><span>真诚欢迎热爱开源的伙伴加入到社区中来，为做一个优秀实用的好项目献上一份自己的力量。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:center"><img alt height="810" src="https://oscimg.oschina.net/oscnet/up-4e21d9ec16e8c0483d9ada8e944b8e5b99b.jpg" width="100%" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><strong style="color:#888888">「2021 最受欢迎开源项目」</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="color:#333333"><span><span>附</span><span>:</span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="color:#333333"><span><span>S</span><span>t</span><span>r</span><span>e</span><span>a</span><span>m</span><span>x</span><span><span> </span></span><span>官</span><span>网</span><span>:</span><span> </span><span> </span></span></span><span style="color:#0052ff"><span><span>ht</span><span>t</span><span>p</span><span>:</span><span>/</span><span>/</span><span>s</span><span>t</span><span>r</span><span>e</span><span>a</span><span>m</span><span>x</span><span>h</span><span>u</span><span>b</span><span>.</span><span>c</span><span>o</span><span>m</span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="color:#333333"><span><span>G</span><span>i</span><span>t</span><span>h</span><span>u</span><span>b</span><span>:</span><span> </span></span></span><span style="color:#7b0c00"><span><span> </span></span></span><span style="color:#0052ff"><span><span>ht</span><span>t</span><span>p</span><span>s</span><span>:</span><span>/</span><span>/</span><span>g</span><span>i</span><span>t</span><span>h</span><span>u</span><span>b</span><span>.</span><span>c</span><span>o</span><span>m</span><span>/</span><span>s</span><span>t</span><span>r</span><span>e</span><span>a</span><span>m</span><span>x</span><span>h</span><span>u</span><span>b</span><span>/</span><span>s</span><span>t</span><span>r</span><span>e</span><span>a</span><span>m</span><span>x</span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="color:#333333"><span><span>G</span><span>i</span><span>t</span><span>e</span><span>e</span><span>:</span><span> </span><span> </span></span></span><span style="color:#0052ff"><span><span>ht</span><span>t</span><span>p</span><span>s</span><span>:</span><span>/</span><span>/</span><span>g</span><span>i</span><span>t</span><span>e</span><span>e</span><span>.</span><span>c</span><span>o</span><span>m</span><span>/</span><span>s</span><span>t</span><span>r</span><span>e</span><span>a</span><span>m</span><span>x</span><span>h</span><span>u</span><span>b</span><span>/</span><span>s</span><span>t</span><span>r</span><span>e</span><span>a</span><span>m</span><span>x</span></span></span></p>
                                        </div>
                                      
</div>
            