
---
title: 'Hikyuu 1.2.0 发布，高性能量化交易研究框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=705'
author: 开源中国
comments: false
date: Tue, 11 Jan 2022 23:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=705'
---

<div>   
<div class="content">
                                                                                            <p><strong style="color:#333333">Hikyuu 1.2.0 已发布，这是一款量化交易研究框架。该版本更新如下：</strong></p> 
<ol> 
 <li>HikyuuTdx 执行导入时自动保存配置，避免第一次使用 hikyuu 必须退出先退出 Hikyuutdx 的问题</li> 
 <li>增加创业板 301 开头股票代码</li> 
 <li>修复 window 显示缩放时 Hikyuutdx 显示不全的问题</li> 
 <li>修复 HHVLLV/LLVBARS/HHVBARS 计算错误</li> 
 <li>优化指标重设上下文时的计算，上下文未变化的情况下由指标本身计算标识判断是否重计算</li> 
 <li>修复分笔、分时数据转换 to_df 函数无效的问题</li> 
 <li>HikyuuTdx 导入至 hdf5 时增加数据保护，遇到出错的表直接删除，下次可自动恢复导入</li> 
 <li>修复使用通达信的权息数据后复权失效的问题</li> 
 <li>remove hikyuu_extern_libs submodule, windows下HDF5, mysql改用下载依赖包的方式</li> 
 <li>优化 HikyuuTDX GUI控制台日志，捕获子进程日志输出</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Hikyuu 是一款基于 C++/Python 的高性能开源量化交易研究框架，用于策略分析及回测（目前用于国内股票市场）。与其他量化平台或回测软件相比，其独特性在于：将完整的策略分解为不同的组件，通过重用不同的方面策略，最大化的减轻编写策略的负担，如常见的止损和资金管理策略，只需要简单指定已有的止损或资金管理策略等，即可完成不同的策略组合；同时，可自由遍历所有股票，对策略效果进行综合的统计分析。如下面的示例，简单更好不同的资金管理策略。入门示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnbviewer.jupyter.org%2Fgithub%2Ffasiondog%2Fhikyuu%2Fblob%2Fmaster%2Fhikyuu%2Fexamples%2Fnotebook%2F000-Index.ipynb%3Fflush_cache%3DTrue" target="_blank">https://nbviewer.jupyter.org/github/fasiondog/hikyuu/blob/master/hikyuu/examples/notebook/000-Index.ipynb?flush_cache=True</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更多信息，参见项目主页：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhikyuu.org%2F" target="_blank">https://hikyuu.org</a> or <span> </span><a href="http://fasiondog.gitee.io/hikyuu/">http://fasiondog.gitee.io/hikyuu</a></p>
                                        </div>
                                      
</div>
            