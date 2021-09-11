
---
title: 'Linkis 1.0.2 正式发布，大数据平台中间件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4721'
author: 开源中国
comments: false
date: Fri, 10 Sep 2021 16:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4721'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>Linkis-1.0.2作为Linkis 1.0.1的增强版，主要实现了FlinkEngineConn，将Flink引入Linkis生态，关键特性如下：</p> 
 <p>实现了FlinkEngineConn，支持Flink SQL和Flink Jar应用的编写、调试、发布与监控；</p> 
 <p>实现了LinkisManagerClient，支持将调试好的流式应用通过LinkisManagerClient发布给LinkisManager进行常驻型提交执行</p> 
 <p><strong>缩略用语:</strong></p> 
 <p>CGS: Computation Governance Services<br> PES: Public Enhancement Services<br> MGS: Microservice Governance Services</p> 
 <p><strong>新特性</strong></p> 
 <p>EngineConn</p> 
 <p>[CGS-LinkisOnceEngineconn] 实现了OnceEngineExecutor，用于提供对流式应用的支持；</p> 
 <p>EngineConnPlugin</p> 
 <p>[CGS-EngineConnPlugin-Flink] 支持Flink引擎<br> [CGS-EngineConnPlugin-Flink] 支持执行Flink SQL和Flink Jar应用<br> [CGS-EngineConnPlugin-Flink] Flink EngineConn多数据源支持<br> [CGS-EngineConnPlugin-Flink] Flink Metrics监控支持</p> 
 <p>ComputationClient</p> 
 <p>[CGS-LinkisComputationClient] 实现了LinkisManagerClient，支持将调试好的流式应用通过LinkisManagerClient发布给LinkisManager进行常驻型提交执行。</p> 
 <p><strong>功能增强</strong></p> 
 <p>1. [CGS-LinkisManager] label中的域名支持'-'符号。<br> 2. [MGS-LinkisServiceGateway] 修复linkis gateway弱密码问题。<br> 3. [CGS-LinkisEngineconnManager] 服务同时支持ip地址和域名。<br> 4. [CGS-LinkisEntrance] 移除instance-label client相关依赖, 解决gateway router中的域名和IP判断异常问题， 移除pom中对pentaho-aggdesigner-algorithm jar的依赖。<br> 5. [PES-LinkisBmlServer] 默认下载用户更改为jvm user, 同时支持通过参数配置默认下载用户</p> 
 <p><strong>Bug修复</strong></p> 
 <p>1. [CGS-LinkisMnagager] 修复并发引擎顺序执行bug<br> 2. [CGS-LinkisEngineconn] 修复一个会造成冗余线程被创建的bug<br> 3. [CGS-EngineConnPlugin-Hive] 修复一个Hive3.0的编译问题<br> 4. [CGS-EngineConnPlugin-Flink] 修复一个Flink-EnginePlugin的编译问题<br> 5. [CGS-EngineConnPlugin-Hive] [CGS-EnginePlugin-Spark] 修复Spark和hive的兼容性问题</p> 
 <p><strong>下载地址（腾讯云）:</strong></p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fosp-1257653870.cos.ap-guangzhou.myqcloud.com%2FWeDatasphere%2FLinkis%2F1.0.2%2Fwedatasphere-linkis-1.0.2-combined-package-dist.tar.gz" target="_blank">Linkis-1.0.2 Compiled (.tar.gz)</a></p> 
 <div> 
  <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong>开源链接:</strong></p> 
  <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2FLinkis" style="box-sizing: inherit; background-color: transparent; color: rgb(52, 111, 182); text-decoration: none;" target="_blank">https://github.com/WeBankFinTech/Linkis</a><br> <a href="https://gitee.com/WeBank/Linkis" style="box-sizing: inherit; background-color: transparent; color: rgb(52, 111, 182); text-decoration: none;" target="_blank">https://gitee.com/WeBank/Linkis</a></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            