
---
title: 'vn.py 3.2.0 发布，开源量化交易程序开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6534'
author: 开源中国
comments: false
date: Mon, 27 Jun 2022 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6534'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">vn.py 是基于 Python 的开源量化交易程序开发框架，起源于国内私募的自主量化交易系统，目前已经成长为一套全功能的交易程序开发框架。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>3.2.0 版本更新内容如下：</strong></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>新增</strong></h2> 
<ol style="margin-left:0; margin-right:0"> 
 <li>添加广州期货交易所枚举值字段GFEX</li> 
 <li>新增CTP期权（ETF）穿透式测试接口vnpy_sopttest</li> 
 <li>新增Currency.CAD（加元）枚举值</li> 
 <li>新增Exchange.TSE（多伦多交易所）和Exchange.AMEX（美洲交易所）枚举值</li> 
 <li>新增vnpy_taos，涛思数据TDengine时序数据库适配器</li> 
 <li>新增vnpy_timescaledb，TimescaleDB时序数据库适配器</li> 
</ol> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>调整</strong></h2> 
<ol style="margin-left:0; margin-right:0"> 
 <li>更新vnpy_ctp/vnpy_ctptest支持广州期货交易所</li> 
 <li>更新vnpy_tora的现货API接口到最新版本：API_Python3.7_交易_v4.0.3_20220222</li> 
 <li>更新vnpy_tora的期权API接口到最新版本：API_Python3.7_v1.3.2_20211201</li> 
 <li>更新vnpy_esunny/vnpy_tap添加关闭接口时对于API退出函数的调用</li> 
 <li>移除vnpy_ctastrategy/vnpy_ctabacktester/vnpy_optionmaster的反向合约支持</li> 
 <li>增加vnpy_ib对于沪股通、深股通、多伦多交易所、美洲交易所的支持</li> 
 <li>增加vnpy_ib对于指数行情数据的支持</li> 
 <li>添加vnpy_ctastrategy策略交易管理界面的策略实例查找功能</li> 
</ol> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>修复</strong></h2> 
<ol style="margin-left:0; margin-right:0"> 
 <li>修复vnpy_mongodb中K线数据量统计的问题（使用新的count_documents函数）</li> 
 <li>修复由于PySide6对象销毁先于__del__调用，导致的BaseMonitor衍生组件无法自动保存界面状态的问题 </li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvnpy%2Fvnpy%2Freleases%2Ftag%2F3.2.0" target="_blank">https://github.com/vnpy/vnpy/releases/tag/3.2.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            