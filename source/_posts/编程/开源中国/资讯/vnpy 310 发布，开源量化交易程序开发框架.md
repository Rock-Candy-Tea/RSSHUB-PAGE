
---
title: 'vn.py 3.1.0 发布，开源量化交易程序开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6571'
author: 开源中国
comments: false
date: Sat, 14 May 2022 07:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6571'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">vn.py 是基于 Python 的开源量化交易程序开发框架，起源于国内私募的自主量化交易系统，目前已经成长为一套全功能的交易程序开发框架。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333"><strong>3.1.0 版本更新内容如下：</strong></span></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>新增</strong></h2> 
<ol style="margin-left:0; margin-right:0"> 
 <li>新增恒生云UF2.0证券仿真环境交易接口vnpy_uf</li> 
 <li>新增火象投教仿真环境交易接口vnpy_hx</li> 
</ol> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>调整</strong></h2> 
<ol style="margin-left:0; margin-right:0"> 
 <li>升级tzlocal库的版本到4.2，消除get_localzone()函数的warning</li> 
 <li>完善代码中函数和变量类型提示</li> 
 <li>使用QtCore.Signal代替老的QtCore.pyqtSignal</li> 
 <li>优化vnpy_rohon接口的委托成交相关细节功能</li> 
 <li>更新vnpy_xtp到2.2.32.2.0版本XTP API，支持上交所新债系统</li> 
 <li>优化vnpy_mongodb的数据写入速度，基于pymongo 4.0版本的批量写入功能</li> 
 <li>增加vnpy_ctp对于委托函数返回值为非0（请求发送失败）状态的处理</li> 
 <li>对vnpy_ctastrategy和vnpy_ctabacktester的策略模板下拉框中内容，改为基于首字母排序</li> 
</ol> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>修复</strong></h2> 
<ol style="margin-left:0; margin-right:0"> 
 <li>修复vnpy_optionmaster模块希腊值监控组件的数据刷新问题</li> 
 <li>修复vnpy_mongodb由于时间戳的时区信息确实，导致的数据加载范围问题</li> 
 <li>修复vnpy_tts的sdist源代码打包缺失lib文件的问题</li> 
 <li>修复vnpy_rqdata由于查询返回数据为NaN导致的解析问题</li> 
</ol> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvnpy%2Fvnpy%2Freleases%2Ftag%2F3.1.0" target="_blank">https://github.com/vnpy/vnpy/releases/tag/3.1.0</a></p>
                                        </div>
                                      
</div>
            