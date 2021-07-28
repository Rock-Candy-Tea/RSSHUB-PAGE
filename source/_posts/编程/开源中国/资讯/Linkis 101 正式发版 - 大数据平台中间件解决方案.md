
---
title: 'Linkis 1.0.1 正式发版 - 大数据平台中间件解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2114'
author: 开源中国
comments: false
date: Wed, 28 Jul 2021 09:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2114'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><strong>Linkis 1.0.1</strong><strong>对Linkis1.0.0版本发现Bug和影响性能，便利性的问题进行了修复和增强，欢迎更新升级。</strong></p> 
<p style="text-align:center"><strong>Linkis 1.0.1</strong></p> 
<p>    Linkis 1.0.1 作为1.0.0的修复版本，这次版本主要修复了高并发场景下的性能bug，以及优化资源管理模块,<span style="background-color:white"><span style="color:#c53d41">以及修复多个已发现的bug，</span></span>并优化Spark引擎支持 FATE使用。</p> 
<p><span style="background-color:white">    FATE (Federated AI Technology Enabler) </span><span style="background-color:white">是微众银行</span><span style="background-color:white">AI</span><span style="background-color:white">部门发起的开源项目，为联邦学习生态系统提供了可靠的安全计算框架</span><span style="background-color:white">(</span>https://github.com/FederatedAI/FATE)。</p> 
<p style="text-align:left"><strong>Abbreviations</strong><strong>（关键字缩写）:</strong><br> <strong>CGS</strong>: Computation Governance Services（计算治理服务）<br> <strong>PES</strong>: Public Enhancement Services（公共增强服务）<br> <strong>MGS</strong>: Microservice Governance Services（微服务治理服务）</p> 
<p style="text-align:center"><strong>增强</strong></p> 
<ul> 
 <li style="text-align:left"><strong>[Commons]</strong> Linkis-HTTPClient在上传文件时支持设置ContentType.</li> 
 <li style="text-align:left"><strong>[Commons]</strong> Linkis-HttpClient支持兼容Response的content为空.</li> 
 <li style="text-align:left"><strong>[Commons]</strong> HDFS FileSystem对象支持进行缓存.</li> 
 <li style="text-align:left"><strong>[Commons]</strong> 优化Shoutdown兼容windows操作系统.</li> 
 <li style="text-align:left"><strong>[Orchestrator]</strong> ioClient支持隔离单独的Orchestrator.</li> 
 <li style="text-align:left"><strong>[PES-JobHistory]</strong> JobHistory支持记录用户提交任务的原始代码.</li> 
 <li style="text-align:left"><strong>[PES-InstanceLabel]</strong> InstanceLabel模块支持增加和移除标签信息.</li> 
 <li style="text-align:left"><strong>[PES-ErrorCode]</strong> 优化错误码模块的初始化sql，移除id字段的默认值.</li> 
 <li style="text-align:left"><strong>[PES-Configuration] </strong>管理台的配置支持修改实时刷新缓存值.</li> 
 <li style="text-align:left"><strong>[PES-Configuration] </strong>管理台支持内存设置单位，默认单位是GB.</li> 
 <li style="text-align:left"><strong>[CGS-Entrance]</strong> 优化支持任务提交记录客户端IP信息，以方便链路分析.</li> 
 <li style="text-align:left"><strong>[CGS-LimkisMnagager ] </strong>ECM的租户标签应该不被移除的，方便重启时保留租户标签信息.</li> 
 <li style="text-align:left"><strong>[EnginePlugin-Spark]</strong> Spark EngineConn的启动参数支持设置原生参数去支持Fate使用，例如设置python版本.</li> 
</ul> 
<p style="text-align:center"><strong>Bug</strong><strong>修复</strong></p> 
<ul> 
 <li style="text-align:left"><strong><span style="background-color:white">[Commons]</span></strong><span style="background-color:white"> Logging </span><span style="background-color:white">是建议被优化, 因为如果用户传入的内容是null会导致空指针异常.</span></li> 
 <li style="text-align:left"><span style="background-color:white"><strong>[Commons]</strong> jackson-core-asl 包存在冲突， linkis1.0在兼容CDH版本时.</span></li> 
 <li style="text-align:left"><span style="background-color:white"><strong>[PES-UDF]</strong> UDFClient存在只能获取UDF不能获取方法函数的Bug.</span></li> 
 <li style="text-align:left"><span style="background-color:white"><strong>[PES-BML] </strong>优化BML EngineConnHook的执行顺序，修复资源文件不可读问题.</span></li> 
 <li style="text-align:left"><span style="background-color:white"><strong>[PES-Configuration]</strong> Linkis管理台在设置JDBC参数时，保存会出错.</span></li> 
 <li style="text-align:left"><span style="background-color:white"><strong>[CGS-Entrance] </strong>当一个任务包含千条sql时，存在错误执行的Bug.</span></li> 
 <li style="text-align:left"><span style="background-color:white"><strong>[CGS-Entrance] </strong>当sql的limit超过5000时任务会执行失败.</span></li> 
 <li style="text-align:left"><span style="background-color:white"><strong>[CGS-Entrance]</strong> 在压测同时运行一万个任务时，日志存在记录不全的情况.</span></li> 
 <li style="text-align:left"><span style="background-color:white"><strong>[CGS-Entrance]</strong> 在压测10000个任务时存在任务处在 Inited/Running/Scheduled不更新的情况.</span></li> 
 <li style="text-align:left"><span style="background-color:white"><strong>[CGS-LimkisMnagager]</strong> 当管理台设置引擎为2时，在schedulis进行调度时存在会启动18个引擎的情况.</span></li> 
 <li style="text-align:left"><span style="background-color:white"><strong>[CGS-LimkisMnagager]</strong> ECM管理存在concurrent label的值为空问题.</span></li> 
 <li style="text-align:left"><span style="background-color:white"><strong>[EnginePlugin-Hive] </strong>当kill 一个复杂的Hive任务时，存在不能kill Yarn上任务的偶发情况.</span></li> 
</ul> 
<p style="text-align:center"><strong>贡献者</strong></p> 
<p style="text-align:left">Linkis 1.0.1 的发布离不开 WeDataSphere 社区的贡献者。在此感谢各位社区的贡献者!</p> 
<p style="text-align:center"><strong>云资源</strong></p> 
<p style="text-align:justify"><span style="color:#24292e">腾讯云：</span></p> 
<p style="text-align:justify"><em><span style="color:#0080ff">https://osp-1257653870.cos.ap-guangzhou.myqcloud.com/WeDatasphere/Linkis/1.0.1/wedatasphere-linkis-1.0.1-combined-package-dist.tar.gz</span></em></p>
                                        </div>
                                      
</div>
            