
---
title: 'Apache Linkis(Incubating) 计算中间件 1.1.2 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic4.zhimg.com/80/v2-4447af569f1c9bb2860f9d9a99b0b383_720w.jpg'
author: 开源中国
comments: false
date: Tue, 12 Jul 2022 17:29:00 GMT
thumbnail: 'https://pic4.zhimg.com/80/v2-4447af569f1c9bb2860f9d9a99b0b383_720w.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0"><strong>Linkis 1.1.2 版本简介</strong></p> 
<p style="margin-left:0; margin-right:0">GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fapache%2Fincubator-linkis" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>github.com/apache/incub</span><span style="background-color:transparent; color:transparent">ator-linkis</span></a></p> 
<p style="margin-left:0; margin-right:0"><strong>本次发布主要支持在无 HDFS 的环境下进行精简化部署（支持部分引擎），方便更轻量化的学习使用和调试；新增对数据迁移工具 Sqoop 引擎的支持；异常处理日志优化；部分安全漏洞组件升级等；修复社区反馈的已知 bug。</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>主要功能如下：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>支持在无HDFS的环境下进行精简化部署（支持部分引擎），方便更轻量化的学习使用和调试</li> 
 <li>新增对数据迁移工具 Sqoop 引擎的支持</li> 
 <li>优化日志等，提高问题排查效率</li> 
 <li>修复用户越权等接口的安全问题</li> 
 <li>部分依赖包的升级和社区已知问题修复</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>缩写：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>COMMON: Linkis Common</li> 
 <li>EC: Engineconn</li> 
 <li>ECM: EngineConnManager</li> 
 <li>ECP: EngineConnPlugin</li> 
 <li>DMS: Data Source Manager Service</li> 
 <li>MDS: MetaData Manager Service</li> 
 <li>LM: Linkis Manager</li> 
 <li>PS: Linkis Public Service</li> 
 <li>PE: Linkis Public Enhancement</li> 
 <li>RPC: Linkis Common RPC</li> 
 <li>CG: Linkis Computation Governance</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>版本新特性</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[Deployment]Linkis-1804,1811,1841,1843,1846,1933 支持在无HDFS的环境下进行精简化部署（支持部分引擎），方便更轻量化的学习使用和调试</li> 
 <li>[PS]Linkis-1949 增加未完成作业的列表接口 (/listundone)，并利用定时调度优化查询性能</li> 
 <li>[BML]Linkis-1811,1843 BML物料服务新增对本地文件系统存储模式部署的支持</li> 
 <li>[Common]Linkis-1887 RPC模块Sender支持修改负载均衡 Ribbon 等参数</li> 
 <li>[Common]Linkis-2059 使用任务task id 作为日志中的 trace id</li> 
 <li>[EC]Linkis-1971 EC AsyncExecutor 支持设置并行 Job Group 的个数</li> 
 <li>[Engine]Linkis-2109 新增对数据迁移工具 Sqoop 引擎的支持</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>功能增强</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[ECP]Linkis-2074 Flink 引擎支持自定义配置</li> 
 <li>[Deployment]Linkis-1841 支持用户部署时关闭对 Spark/Hive/HDFS 环境检测</li> 
 <li>[Deployment]Linkis-1971 修复在多块网卡机器部署时，自动获取ip错误的问题</li> 
 <li>[Entrance]Linkis-1941 Entrance 支持将原始的 jobId 传递给 EngineConn 和 LinkisManager</li> 
 <li>[Entrance]Linkis-2045 重构EntranceInterceptor实现类中脚本类型和运行类型匹配关系</li> 
 <li>[RPC]Linkis-1903 修改 RPC 模块异常处理逻辑，透传 EngineConnPlugin 异常的原始错误信息</li> 
 <li>[RPC]Linkis-1905 增加参数支持传递 LoadBalancer 的参数，比如 Ribbon</li> 
 <li>[Orchestrator]Linkis-1937 编排器任务调度器creator配置参数支持配置多个Creator值</li> 
 <li>[PE][Linkis-1959 ContextService 增加必要的日志打印，方便错误排查</li> 
 <li>[EC]Linkis-1942 EC支持将taskID塞入到底层引擎的conf中，方便做任务的血缘分析关联到具体的linkis任务</li> 
 <li>[EC]Linkis-1973 Task 的执行错误日志获取方式由 cat 改为 tail -1000 控制日志数量，避免全量加载大文件</li> 
 <li>[CG,PE]Linkis-2014 增加配置 add/get/delete，优化同步锁</li> 
 <li>[Common]Linkis-2016 调整cglib依赖的使用，将 cglib 依赖替换为 spring 内置的cglib</li> 
 <li>[Gateway]Linkis-2071 HTTP请求Header中增加 GatewayURL属性值</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>修复功能</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[Engine]Linkis-1931 修复 Python 错误加载的是Pyspark的函数，非单机Python本身的函数问题</li> 
 <li>[Deployment]Linkis-1853 修复安装初始化 DDL 报错的问题</li> 
 <li>[UDF]Linkis-1893 为 udf 相关接口增加用户权限校验</li> 
 <li>[EC]Linkis-1933 给非 deploy 用户组的用户执行作业增加 resultSet 的写权限</li> 
 <li>[EC]Linkis-1846 修复 ResultSet 配置本地路径无效的问题</li> 
 <li>[EC]Linkis-1966 使用 System.properties 替换 System.ev</li> 
 <li>[EC-Python]Linkis-2131 修复 Python 引擎由于 pandas 引入导致异常的问题</li> 
 <li>[PS]Linkis-1840 下载 csv 格式数据时，增加灵活选择，防止数据格式错乱</li> 
 <li>[Orchestrator]Linkis-1992 修复 Orchestrator Reheater 模块的并发问题</li> 
 <li>[PE]Linkis-2032 配置接口的优化，获取Label的配置参数时，修改为直接获取Key-value对</li> 
 <li>[Web]Linkis-2036 管理台ECM 页面实例显示问题修复</li> 
 <li>[Web]Linkis-1895 资源页面显示问题修复</li> 
 <li>[ECP]Linkis-2027 修复 ECP 物料下载字节截取导致的异常错误</li> 
 <li>[ECP]Linkis-2088 修复 hive task 运行过程中存在进度回退的问题</li> 
 <li>[ECP]Linkis-2090 修复 Python3 找不到的问题</li> 
 <li>[CG]Linkis-1751 脚本自定义变量运行类型和后缀约束配置化</li> 
 <li>[CG]Linkis-2034 对超时任务的描述信息不匹配的修复</li> 
 <li>[CG]Linkis-2100 优化高并发下的 db 死锁问题</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>安全相关</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[UDF]Linkis-1893 修复 udf 部分接口（/udf/list，/udf/tree/add，/udf/tree/update）的用户越权问题</li> 
 <li>[PS]Linkis-1869 修复 Linkis PlublicService 相关接口越权问题</li> 
 <li>[PS]Linkis-2086 方法 /updateCategoryInfo 增加权限校验</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>依赖变更</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[MDS]Linkis-1947 mys2168ql-connector-java 从 5.1.34 升级到 8.0.16</li> 
 <li>[ECP]Linkis-1951 hive-jdbc 从 1.2.1 升级至 2.3.3</li> 
 <li>[ECP]Linkis-1968 protobuf-java 版本升级至 3.15.8</li> 
 <li>[ECP]Linkis-2021 移除 Flink 模块的一些冗余依赖包</li> 
 <li>[RPC]Linkis-2018 统一 json4s 的版本</li> 
 <li>[Web]Linkis-2336 引入web组件jsencrypt-3.2.1的依赖，作为登陆密码加解密工具</li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>详细指引</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>本版本总览:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Flinkis.apache.org%2Fzh-CN%2Fdocs%2Flatest%2Frelease" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>linkis.apache.org/zh-CN</span><span style="background-color:transparent; color:transparent">/docs/latest/release</span></a></li> 
 <li>详细安装部署见指引：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Flinkis.apache.org%2Fzh-CN%2Fdocs%2Flatest%2Fdeployment%2Fquick_deploy" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>linkis.apache.org/zh-CN</span><span style="background-color:transparent; color:transparent">/docs/latest/deployment/quick_deploy</span></a></li> 
 <li>官方下载链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Flinkis.apache.org%2Fzh-CN%2Fdownload%2Fmain" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>linkis.apache.org/zh-CN</span><span style="background-color:transparent; color:transparent">/download/main</span></a></li> 
</ul> 
<p style="margin-left:0; margin-right:0">贡献者寄语</p> 
<p style="margin-left:0; margin-right:0">Apache Linkis(incubating) 1.1.2的发布离不开Linkis社区的贡献者,感谢所有的社区贡献者，包括但不仅限于以下Contributors（排名不分先后）:</p> 
<p style="margin-left:0; margin-right:0">Alexyang, David hua, GodfreyGuo, Jack Xu, Zosimer, allenlliu, ericlu, huapan123456, husofskyzy, iture123, legendtkl, luxl@chinatelecom.cn, maidangdang44, peacewong, pengfeiwei, seedscoder, weixiao, xiaojie19852006, めぐみん, 李为</p> 
<p><img src="https://pic4.zhimg.com/80/v2-4447af569f1c9bb2860f9d9a99b0b383_720w.jpg" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><strong>— END —</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>如何成为社区贡献者</strong></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><strong>1<span> </span></strong>► 官方文档贡献。发现文档的不足、优化文档，持续更新文档等方式参与社区贡献。通过文档贡献，让开发者熟悉如何提交PR和真正参与到社区的建设。参考攻略：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmp.weixin.qq.com%2Fs%253F__biz%253DMzI4MDkxNzUxMg%253D%253D%2526mid%253D2247488838%2526idx%253D1%2526sn%253D3599cbb009751af44ba46720b0b60cf7%2526chksm%253Debb07621dcc7ff37405c5c7ab36193c44ba543d4854b01a23cbc66a12440472a3a0adbc85c5b%2526scene%253D21%2523wechat_redirect" target="_blank">保姆级教程：如何成为Apache Linkis文档贡献者</a></p> 
<p style="margin-left:0; margin-right:0"><strong>2<span> </span></strong>►代码贡献。我们梳理了社区中简单并且容易入门的的任务，非常适合新人做代码贡献。请查阅新手任务列表：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fapache%2Fincubator-linkis%2Fissues%2F1161" target="_blank"><span style="background-color:transparent; color:transparent">https://</span><span>github.com/apache/incub</span><span style="background-color:transparent; color:transparent">ator-linkis/issues/1161</span></a></p> 
<p style="margin-left:0; margin-right:0"><strong>3<span> </span></strong>►内容贡献：发布WeDataSphere开源组件相关的内容，包括但不限于安装部署教程、使用经验、案例实践等，形式不限，请投稿给小助手。例如：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmp.weixin.qq.com%2Fs%253F__biz%253DMzI4MDkxNzUxMg%253D%253D%2526mid%253D2247488722%2526idx%253D1%2526sn%253D6069ac14a2e0ec6f09acb8c8a471914f%2526chksm%253Debb077b5dcc7fea3fcb2df95de0b3a99ecf1f73a86b8c036f1c36c17cce30c1d36b38866fec0%2526scene%253D21%2523wechat_redirect" target="_blank">技术干货 | Linkis实践：新引擎实现流程解析</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmp.weixin.qq.com%2Fs%253F__biz%253DMzI4MDkxNzUxMg%253D%253D%2526mid%253D2247488695%2526idx%253D1%2526sn%253D4020e1bccb565d518c0731b26b9a76ac%2526chksm%253Debb077d0dcc7fec65c3052051f3a7d6d51b160fa82b5b89c06e1e0180080bb85949683f31a32%2526scene%253D21%2523wechat_redirect" target="_blank">技术干货 | Prophecis保姆级部署教程</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmp.weixin.qq.com%2Fs%253F__biz%253DMzI4MDkxNzUxMg%253D%253D%2526mid%253D2247488005%2526idx%253D1%2526sn%253Ddf78dfb77f475c2d1ef7ee69568db5c7%2526chksm%253Debb07162dcc7f8749a421038dd51abd7befb08aba8354846d87c61982db6a1ba520d99fd391b%2526scene%253D21%2523wechat_redirect" target="_blank">社区开发者专栏 | MariaCarrie：Linkis1.0.2安装及使用指南</a></li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong>4<span> </span></strong>►社区答疑：积极在社区中进行答疑、分享技术、帮助开发者解决问题等；</p> 
<p style="margin-left:0; margin-right:0"><strong>5<span> </span></strong>►其他：积极参与社区活动、成为社区志愿者、帮助社区宣传、为社区发展提供有效建议等；</p>
                                        </div>
                                      
</div>
            