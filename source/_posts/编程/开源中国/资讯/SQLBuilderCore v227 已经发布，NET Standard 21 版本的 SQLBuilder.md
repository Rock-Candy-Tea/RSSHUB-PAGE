
---
title: 'SQLBuilder.Core v2.2.7 已经发布，NET Standard 2.1 版本的 SQLBuilder'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1120'
author: 开源中国
comments: false
date: Sun, 17 Oct 2021 18:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1120'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SQLBuilder.Core v2.2.7 已经发布，NET Standard 2.1 版本的 SQLBuilder</p> 
<p><strong>此版本更新内容包括：</strong></p> 
<ol> 
 <li>优化 ConfigurationManager，支持 appsettings 自定义环境变量 “APPSETTINGS_ENVIRONMENT”；</li> 
 <li>优化仓储构造函数，添加 “configuration” 可选参数，用于支持自定义 I Configuration；</li> 
 <li>重命名 SetConfigurationFile -> SetConfiguration，重载 SetConfiguration；</li> 
 <li>新增 FormattableString 扩展类；</li> 
 <li>重载 IRepository 部分接口并实现，支持 FormattableString 内插 sql 语句；</li> 
 <li>移除 IRepository 的 Close 方法，以 Dispose 方法替代；新增 AutoDispose 属性、UseAutoDispose 方法；</li> 
 <li>优化仓储数据库连接释放逻辑，支持共享连接模式；</li> 
 <li>优化 AddSqlBuilder 扩展，新增 AddRepository、AddAllRepository、GetConnectionInformation、CreateRepositoryFactory 扩展方法；</li> 
 <li>升级 nuget 依赖引用包到最新版本；</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/zqlovejyc/SQLBuilder.Core/releases/v2.2.7">https://gitee.com/zqlovejyc/SQLBuilder.Core/releases/v2.2.7</a></p>
                                        </div>
                                      
</div>
            