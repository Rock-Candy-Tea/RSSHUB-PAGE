
---
title: 'CrateDB 4.6.3 发布，分布式 SQL 数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8200'
author: 开源中国
comments: false
date: Sat, 11 Sep 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8200'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>CrateDB 4.6.3 现已发布。Crate 是一个开源的大规模的可伸缩的数据存储系统，无需任何系统管理需求。提供强大的搜索功能。用于存储各种表格数据、非结构化数据和二进制对象。并可通过 SQL 进行检索。易于安装和使用，支持高可用性和实时大规模并行访问和处理。Crate 特别适合用于 Docker 环境中。</p> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong>注意</strong></p> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">如果要升级群集，则必须先运行 CrateDB 4.0.2 或更高版本，然后才能升级到 4.6.3。官方建议在升级到 4.6.3 之前先升级到最新的 4.3 版本。支持从 <span style="color: rgb(0, 0, 0); font-family: Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: 0.3px; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;">4.5.x</span> 到 4.6.3的滚动升级。升级之前，建议先<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrate.io%2Fdocs%2Fcrate%2Freference%2Fen%2Flatest%2Fadmin%2Fsnapshots.html" rel="nofollow" target="_blank">备份你的数据</a>。</p> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong>Fixes</strong></p> 
 <ul> 
  <li> <p style="margin-top:0px; margin-bottom:0px"><span style="box-sizing:border-box"><span style="line-height:1.5em">修复了 4.2 中引入的性能回归问题，该问题导致在顶部视图或虚拟表上带有 LIMIT 的查询、以及带有 ORDER BY 的查询变得缓慢。</span></span></p> </li> 
  <li> <p style="margin-top:0px; margin-bottom:0px"><span style="box-sizing:border-box"><span style="line-height:1.5em">修复了管理控制台 Query View 功能的问题。它生成的查询在标识符周围有额外的引号。</span></span></p> </li> 
  <li> <p style="margin-top:0px; margin-bottom:0px"><span style="box-sizing:border-box"><span style="line-height:1.5em">修复了在节点启动期间早期使用 HTTP 接口时，可能导致客户端收到 400 Bad Request 错误的问题。</span></span></p> </li> 
  <li> <p style="margin-top: 0px; margin-bottom: 0px;"><span style="box-sizing: border-box;"><span style="line-height: 1.5em;"><span style="background-color: rgb(255, 255, 255);">修复了使用 UNION </span>语句选择具有不同内部类型的多个对象列时，导致值损坏的问题。</span></span></p> </li> 
  <li> <p style="margin-top:0px; margin-bottom:0px"><span style="box-sizing:border-box"><span style="line-height:1.5em">修复了一个问题，在 CrateDB 4.6.2 版本中，如果对象数据类型定义的子列标识符含有空格，则会导致验证异常；或者在 CrateDB 4.2.0 到 4.6.1 版本中出现不可用对象类型列（写入/读取失败）。</span></span></p> </li> 
 </ul> 
 <p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrate.io%2Fdocs%2Fcrate%2Freference%2Fen%2F4.6%2Fappendices%2Frelease-notes%2F4.6.3.html" rel="nofollow" target="_blank">https://crate.io/docs/crate/reference/en/4.6/appendices/release-notes/4.6.3.html</a> </p> 
</div>
                                        </div>
                                      
</div>
            