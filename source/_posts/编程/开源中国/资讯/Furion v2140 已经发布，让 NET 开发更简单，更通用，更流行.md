
---
title: 'Furion v2.14.0 已经发布，让 .NET 开发更简单，更通用，更流行'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3923'
author: 开源中国
comments: false
date: Sun, 18 Jul 2021 11:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3923'
---

<div>   
<div class="content">
                                                                                            <p>Furion v2.14.0 已经发布，让 .NET 开发更简单，更通用，更流行</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li> <p><strong>新特性</strong></p> 
  <ul> 
   <li>[新增] 简易字符串模板功能，支持远程请求、数据库模块、日志模块、事件总线模块、定时任务模块、异常模块、数据校验模块 <a href="https://gitee.com/dotnetchina/Furion/issues/I402BL" target="_blank">#I402BL</a></li> 
   <li>[新增] <code>404</code> 状态码规范化默认处理 <a href="https://gitee.com/dotnetchina/Furion/issues/I408F5" target="_blank">#I408F5</a></li> 
   <li>[新增] 定时任务 <code>ISpareTimeWorker</code> 声明方式支持异步方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I40KWR" target="_blank">#I40KWR</a></li> 
   <li>[新增] 自动配置二级虚拟目录 <a href="https://gitee.com/dotnetchina/Furion/pulls/354" target="_blank">!354</a></li> 
  </ul> </li> 
 <li> <p><strong>突破性变化</strong></p> 
  <ul> 
   <li>[升级] <strong>框架依赖 <code>SDK</code> 为 <code>.NET 5.0.8</code> 版本</strong></li> 
   <li>[移除] <code>Db.GetNewDbContext()</code> 静态方法 <a href="https://gitee.com/dotnetchina/Furion/issues/I400BK" target="_blank">#I400BK</a></li> 
   <li>[移除] 数据库模块时态表拓展支持 <a href="https://gitee.com/dotnetchina/Furion/issues/I405HI" target="_blank">#I405HI</a></li> 
   <li>[调整] <code>IJsonSerializerProvider</code> 接口参数，新增 <code>inherit</code> 参数 <a href="https://gitee.com/dotnetchina/Furion/issues/I3ZQU5" target="_blank">#I3ZQU5</a></li> 
   <li>[调整] <code>AppSettings</code> 配置的 <code>LogEntityFrameworkCoreSqlExecuteCommand</code> 名称为 <code>OutputOriginalSqlExecuteLog</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I40VVE" target="_blank">#I40VVE</a></li> 
  </ul> </li> 
 <li> <p><strong>问题修复</strong></p> 
  <ul> 
   <li>[修复] <code>Worker Services</code> 定时任务边界值问题导致跳过单次任务 <a href="https://gitee.com/dotnetchina/Furion/issues/I405NI" target="_blank">#I405NI</a></li> 
   <li>[修复] <code>Worker Services</code> 独立发布后程序集扫描失效 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I3ZH3X" target="_blank">#I3ZH3X</a></li> 
   <li>[修复] 远程请求如果配置了 <code>Client</code> 客户端但传入了空 <code>RequestUrl</code> 地址导致异常问题 <a href="https://gitee.com/dotnetchina/Furion/issues/I40BC6" target="_blank">#I40BC6</a></li> 
   <li>[修复] 规范化结果篡改非短路端状态码出现异常 bug <a href="https://gitee.com/dotnetchina/Furion/issues/I408F5" target="_blank">#I408F5</a></li> 
  </ul> </li> 
 <li> <p><strong>其他更改</strong></p> 
  <ul> 
   <li>[优化] <code>App.GetServiceProvider(type)</code> 解析服务性能 <a href="https://gitee.com/dotnetchina/Furion/issues/I40KXN" target="_blank">#I40KXN</a></li> 
   <li>[调整] 视图引擎保存成文件流默认缓存区大小，从 <code>4096</code> 提升至 <code>8192</code> <a href="https://gitee.com/dotnetchina/Furion/issues/I40KH5" target="_blank">#I40KH5</a></li> 
  </ul> </li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/dotnetchina/Furion/releases/v2.14.0">https://gitee.com/dotnetchina/Furion/releases/v2.14.0</a></p>
                                        </div>
                                      
</div>
            