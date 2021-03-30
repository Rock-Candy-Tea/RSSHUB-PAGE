
---
title: 'vn.py 发布 v2.2.0，融航 AMS 资管平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-tt.byteimg.com/origin/pgc-image/4a6de586620642978905493da2a82449?from=pc'
author: 开源中国
comments: false
date: Tue, 30 Mar 2021 11:10:00 GMT
thumbnail: 'https://p3-tt.byteimg.com/origin/pgc-image/4a6de586620642978905493da2a82449?from=pc'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">本周四发布了vn.py的2.2.0版本，本次更新的内容主要是<strong>优化了对于融航AMS资管平台的支持</strong>，采用最新版本融航API封装重构，并增加了对Linux系统（Ubuntu 20.04）的自动编译安装功能。</p> 
<p style="text-align:start">和之前一样，对于使用VN Studio的用户，启动VN Station后，直接点击界面右下角的【更新】按钮就能完成自动更新升级，对于没有安装的用户，请下载VNStudio-2.2.0，体验一键安装的量化交易Python发行版，下载链接：</p> 
<p style="text-align:center"><span style="background-color:#a5c8ff">https://download.vnpy.com/vnstudio-2.2.0.exe</span></p> 
<p style="text-align:start"><strong><u>融航AMS资管平台</u></strong></p> 
<p style="text-align:start">融航AMS资管平台（下称“融航”）是目前国内期货领域<strong>市场占有率最高的资管系统</strong>（都没有之一了），主要的用户群体包括：</p> 
<ul> 
 <li>期货公司：资产管理部（永安期货）、经纪业务部、风险子公司</li> 
 <li>基金公司：公募基金（大成基金）、私募基金</li> 
 <li>MOM和FOF产品（平安资管）</li> 
 <li>大宗商品现货交易商（杉杉物产）</li> 
</ul> 
<p style="text-align:start">对于许多期货投资者来说，可能最为熟悉的是这两套系统：</p> 
<p style="text-align:start"><strong>期货柜台系统（后台）</strong></p> 
<ul> 
 <li> 
  <ul> 
   <li>提供账户管理、交易报盘、验资验券、每日结算等功能；</li> 
   <li>常见的比如CTP、恒生、飞马、易盛等；</li> 
  </ul> </li> 
</ul> 
<p style="text-align:start"><strong>期货交易软件（前台）</strong></p> 
<ul> 
 <li> 
  <ul> 
   <li>提供行情显示、委托挂撤、持仓资金跟踪、资讯查询等功能；</li> 
   <li>常见的比如文华、TB、MC、vn.py等。</li> 
  </ul> </li> 
</ul> 
<p style="text-align:start">对于资金量不大的个人投资者来说，有了期货柜台和交易软件后，就已经能够充分满足交易的需求。</p> 
<p style="text-align:start">但对于资金体量更大且交易策略（不只是量化）更加复杂的机构投资者，除了上述的前后台系统外，还需要引入融航这样额外的中台系统来提供<strong>更加丰富的资产管理功能</strong>：</p> 
<ul> 
 <li>多通道和多账户的<strong>统一管理</strong>，支持对接各家期货公司的各种柜台系统；</li> 
 <li>多市场<strong>联合风控</strong>（证券、期货、期权）： 
  <ul> 
   <li>事前风控，如：仓位敞口限制、委托流量控制；</li> 
   <li>事中风控，如：保证金占用上限、自成交管理；</li> 
   <li>事后风控，如：最大回撤限制、VaR指标计算；</li> 
  </ul> </li> 
 <li>合规流程管理，交易业务<strong>角色拆分</strong>： 
  <ul> 
   <li>交易员：根据既定策略执行具体交易（包括主观和量化）；</li> 
   <li>风控员：根据规则实时监控风险，并有权暂停交易；</li> 
   <li>管理员：创建角色和设置权限，必要时应急交易处置；</li> 
  </ul> </li> 
 <li>每个交易员绩效的<strong>独立核算</strong>： 
  <ul> 
   <li>实时更新的账户信息；</li> 
   <li>收盘自动生成每日报表。</li> 
  </ul> </li> 
</ul> 
<p style="text-align:start">融航提供了<strong>和CTP兼容的API接口</strong>，所以对于前台交易软件来说，大部分时候只需要简单替换dll动态链接库文件，就能快速实现和融航资管中台的对接，vn.py也是之前就已经通过这种方式支持了融航。</p> 
<p style="text-align:start">本次更新基于融航最新版本的API（兼容CTP 6.3.19）重构封装，解决了最近两个月社区论坛和Github上用户多次反馈的老版本兼容性问题，重构后增加了独立的融航API的Python封装子模块<strong>vnpy.api.rohon</strong>。</p> 
<p style="text-align:start">同时除了Windows系统外也增加了对Linux系统（Ubuntu 20.04）的支持，只需使用Github仓库中提供的install.sh脚本即可实现全自动的编译安装。</p> 
<p style="text-align:start">融航接口和CTP接口的dll文件存在重名的情况，<strong>因此请勿同时加载</strong>。连接融航接口时所需的登录信息和CTP高度相似，如下图所示：</p> 
<div style="text-align:start">
 <img alt="vn.py发布v2.2.0 - 融航AMS资管平台" src="https://p3-tt.byteimg.com/origin/pgc-image/4a6de586620642978905493da2a82449?from=pc" referrerpolicy="no-referrer">
</div> 
<p style="text-align:start">最后关于期货穿透式认证需要注意的几点：</p> 
<ul> 
 <li>vn.py连接融航进行交易在穿透式认证中属于【中继】模式，而不再是连接柜台（CTP、恒生等）进行交易时的【直连】模式，所以在申请穿透式认证测试填表时不要选错；</li> 
 <li>融航官方提供类似SimNow的测试环境，联系其客服即可快速申请测试账户；</li> 
 <li>融航接口的【经纪商代码】不再是纯数字形态，而是可以包含英文和数字的字符串（如上图中的RohonDemo）；</li> 
 <li>和CTP等柜台不同，融航系统内的账户和穿透式认证信息存在绑定关系，<strong>每个账户都需要独立申请穿透式认证测试，</strong>所以上图中的【产品名称】和【授权编码】对于其他账户来说是完全没用的！！！</li> 
</ul> 
<p style="text-align:start"><strong><u>MarketRadar增加条件提醒通知功能</u></strong></p> 
<p style="text-align:start">在基于用户自定义公式实时计算指标规则的基础上，MarketRadar模块新增条件信号实时扫描和提醒通知功能：</p> 
<div style="text-align:start">
 <img alt="vn.py发布v2.2.0 - 融航AMS资管平台" src="https://p1-tt.byteimg.com/origin/pgc-image/09aa5f8af35141dc8ff0c353b8cd6c03?from=pc" referrerpolicy="no-referrer">
</div> 
<p style="text-align:start">找到要添加条件触发的指标规则行，点击最左侧的规则名称按钮：</p> 
<div style="text-align:start">
 <img alt="vn.py发布v2.2.0 - 融航AMS资管平台" src="https://p1-tt.byteimg.com/origin/pgc-image/1075056a90f3496690975e563d784967?from=pc" referrerpolicy="no-referrer">
</div> 
<p style="text-align:start">在弹出的对话框中，输入触发条件的具体信息，包括信号类型（大于、小于、等于）、目标数值和通知方式（声音、邮件），如下图所示：</p> 
<div style="text-align:start">
 <img alt="vn.py发布v2.2.0 - 融航AMS资管平台" src="https://p6-tt.byteimg.com/origin/pgc-image/d370a06cb3d24403b803c2b62498a645?from=pc" referrerpolicy="no-referrer"> 
 <p> </p> 
</div> 
<p style="text-align:start">在底部中间的监控组件中即可看到当前处于实时监控中的条件信号：</p> 
<div style="text-align:start">
 <img alt="vn.py发布v2.2.0 - 融航AMS资管平台" src="https://p3-tt.byteimg.com/origin/pgc-image/b061c185c4bc46db82a9324e5674e10d?from=pc" referrerpolicy="no-referrer">
</div> 
<p style="text-align:left">当条件满足后信号会被<strong>立即触发</strong>（并自动从监控表中移除），此时会在<strong>右下角的日志区域输出相关提示信息</strong>，并根据之前用户的选择播放声音通知或者发送邮件提醒。</p> 
<p style="text-align:left">目前条件信号不提供缓存功能，程序关闭后就会消失，每次重启VN Trader后需要重新创建。当不再需要某个信号时，点击最左侧【删除】按钮，即可移除对应的条件信号。</p> 
<p style="text-align:start"><strong><u>其他更新</u></strong></p> 
<p style="text-align:start"><strong>策略模块</strong></p> 
<ol> 
 <li>CTA策略模块增加对净仓交易模式的支持，只需在继承CtaTemplate父类实现交易策略时，调用buy/sell/short/cover函数传入可选参数net=True即可，另外请注意净仓交易模式和锁仓交易模式互斥，因此参数lock必须传False（或者不传）。</li> 
</ol> 
<p style="text-align:left"><strong><u>CHANGELOG</u></strong></p> 
<p style="text-align:start"><strong>修复</strong></p> 
<ol> 
 <li>修复DataManager查询数据库中K线数据范围时，开始和结束日期相反的问题；</li> 
 <li>修复CoinbaseGateway的行情订单簿在更新时，已经撤单的档位不删除的问题；</li> 
 <li>修复BybitGateway对于USDT本位永续合约，浮点数委托量会被转换为0的问题；</li> 
 <li>修复BinanceGateway/BinancesGateway的ConnectionResetError问题，通过关闭HTTP连接的keep-alive功能实现；</li> 
 <li>修复HuobisGateway在USDT本位模式下时，浮点数合约乘数转换出错的问题；</li> 
 <li>修复PostgreSQL数据库对接层中，save_tick_data函数由于访问interval导致保存出错的问题；</li> 
 <li>修复DataRecorder模块中add_bar_recording下保存录制用合约配置错误的问题；</li> 
 <li>修复PostgreSQL数据库对接层中，由于事务执行失败导致的后续报错问题，创建数据库对象时设置自动回滚模式（autorollback=True）；</li> 
 <li>修复DataManager自动更新数据时，查询数据范围由于调用老版本函数导致的错误；</li> 
 <li>修复RQData下载获取的历史数据浮点数精度问题；</li> 
 <li>修复BarGenerator在合成N小时K线时，收盘价、成交量、持仓量字段缺失的问题；</li> 
 <li>修复K线图表底层组件ChartWidget当绘制数据较少时，坐标轴时间点显示重复的问题；</li> 
 <li>修复SpreadTrading模块生成的价差盘口数据的时区信息缺失问题；</li> 
 <li>修复IbGateway的现货贵金属行情数据缺失最新价和时间戳的问题；</li> 
 <li>修复BarGenerator在合成小时级别K线时，成交量字段部分缺失的问题；</li> 
 <li>修复vnpy.rpc模块启用非对称加密后无法正常退出的问题；</li> 
 <li>修复BinancesGateway持仓更新时由于包含多条方向记录导致的持仓错误问题；</li> 
</ol> 
<p style="text-align:start"><strong>调整</strong></p> 
<ol> 
 <li>修改vnpy.chart下ChartItem为按需绘制，大幅缩短图表第一次显示出来的耗时；</li> 
 <li>修改IbGateway的历史数据查询功能，包括所有可用时间（即欧美晚上的电子交易时段）；</li> 
 <li>修改DataRecorder的数据入库为定时批量写入，提高录制大量合约数据时的写入性能；</li> 
</ol> 
<p style="text-align:start"><strong>新增</strong></p> 
<ol> 
 <li>新增IbGateway连接断开后的自动重连功能（每10秒检查）；</li> 
 <li>新增双边报价业务相关的底层数据结构和功能函数；</li> 
 <li>新增开平转换器OffsetConverter的净仓交易模式；</li> 
 <li>新增CtaStrategy模块策略模板的委托时的净仓交易可选参数；</li> 
 <li>新增CtaStrategy模块回测引擎中的全年交易日可选参数；</li> 
 <li>新增ChartWizard模块对于价差行情图表的显示支持；</li> 
 <li>新增MarketRadar模块的雷达信号条件提醒功能；</li> 
</ol>
                                        </div>
                                      
</div>
            