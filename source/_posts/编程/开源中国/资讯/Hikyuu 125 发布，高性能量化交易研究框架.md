
---
title: 'Hikyuu 1.2.5 发布，高性能量化交易研究框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e7dd52fc299308cd845d44f66a87e5a6926.png'
author: 开源中国
comments: false
date: Sun, 04 Sep 2022 08:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e7dd52fc299308cd845d44f66a87e5a6926.png'
---

<div>   
<div class="content">
                                                                                            <p><strong>Hikyuu 是一款基于 C++/Python 的高性能开源量化交易研究框架</strong>，用于快速策略分析及回测。与其他量化平台或回测软件相比，具备：</p> 
<ol> 
 <li>超快的回测速度（百万级别K线1~2秒完成A股全市场计算）；</li> 
 <li>对完整的系统交易理念进行抽象，并分解为不同的组件，通过重用不同的方面策略，最大化的减轻编写策略的负担。</li> 
</ol> 
<p>更多信息，参见项目主页: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhikyuu.org" target="_blank">https://hikyuu.org</a> 或 <a href="http://fasiondog.gitee.io/hikyuu">http://fasiondog.gitee.io/hikyuu</a></p> 
<p><strong>Hikyuu 1.2.5 已发布，该版本更新如下：</strong></p> 
<ol> 
 <li>增加北京交易所数据</li> 
 <li>改进数据下载，补充 pytdx 缺失的部分数据</li> 
 <li>恢复财务数据下载</li> 
 <li>优化 HikyuuTdx 界面</li> 
</ol> 
<p><img alt height="311" src="https://oscimg.oschina.net/oscnet/up-e7dd52fc299308cd845d44f66a87e5a6926.png" width="600" referrerpolicy="no-referrer"></p> 
<p>5. 增加 start_insight_sdk.py, 从华泰 insight 获取实时数据</p> 
<p>该文件在安装目录 gui 子目录下，使用 python 直接运行，运行前需要拥有华泰 insight 账户（可去华泰 insight 官网或客户经理处申请），且需要手工修改该文件最后的 login 函数，填入自己的账户与密码，如下图所示：</p> 
<p><img alt height="233" src="https://oscimg.oschina.net/oscnet/up-28138f96f8b523ca50fb09a28848e0d01e0.png" width="300" referrerpolicy="no-referrer"></p> 
<ol start="6"> 
 <li>完善 hikyuuTdx 中 nng 消息的启停与释放，修复因未完全释放导致再次启动可能出现的被占用的情况</li> 
 <li>hku_catch 增加指示重新抛出异常的参数</li> 
 <li>修正 demo，调整因升级导致的接口名称变化</li> 
</ol>
                                        </div>
                                      
</div>
            