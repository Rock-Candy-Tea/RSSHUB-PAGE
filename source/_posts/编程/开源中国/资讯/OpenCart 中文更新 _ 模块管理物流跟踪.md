
---
title: 'OpenCart 中文更新 _ 模块管理物流跟踪'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f86a2b4f39c17f2be286264c475accee5b6.png'
author: 开源中国
comments: false
date: Wed, 23 Mar 2022 11:09:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f86a2b4f39c17f2be286264c475accee5b6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>前言</strong>：为了能让OpenCart 外贸平台自建站的卖家能第一时间掌握发货信息，能让消费者能及时查看商品物流动态。OpenCart 跨境电商独立站，支持了国内外多种快递跟踪、物流跟踪的API接口，今天为您介绍如何配置对接这些物流信息平台！</p> 
<p style="margin-left:0; margin-right:0"><strong><span>开源软件版本：OpenCart专业版_</span></strong><span><strong>V3.8.1.0</strong></span></p> 
<p style="margin-left:0; margin-right:0">目前OpenCart专业版，支持对接3家快递平台。分别为：快递100平台 、快递鸟平台和AfterShip 物流跟踪。这些快递平台共计对接了500+的快递物流品牌。</p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><span><strong>一、安装物流模块</strong></span></p> 
<p style="margin-left:0; margin-right:0"><span style="background-color:rgba(0, 0, 0, 0); color:#6a6a6a">进入OpenCart 后台</span></p> 
<p style="margin-left:0; margin-right:0"><span style="background-color:rgba(0, 0, 0, 0); color:#6a6a6a">第一步：点击模块管理，选择通用模块：</span></p> 
<p><img alt height="410" src="https://oscimg.oschina.net/oscnet/up-f86a2b4f39c17f2be286264c475accee5b6.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span style="background-color:rgba(0, 0, 0, 0); color:#6a6a6a">第二步：搜索模块名称，进行<strong>安装</strong>或<strong>编辑</strong></span></p> 
<p><img alt height="223" src="https://oscimg.oschina.net/oscnet/up-449b1e14dd6d3630cb11d6df16f1b188e41.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span style="background-color:rgba(0, 0, 0, 0); color:#6a6a6a">目前支持三种快递物流跟踪方式：AfterShip 物流跟踪、快递100订单快递跟踪、快递鸟订单快递跟踪</span></p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>二、</strong><span><strong>物流信息对接</strong></span></p> 
<p style="margin-left:0; margin-right:0"><strong>1//AfterShip</strong></p> 
<p style="margin-left:0; margin-right:0">AfterShip 配置流程 如图：</p> 
<p><img alt height="292" src="https://oscimg.oschina.net/oscnet/up-4dd2bfeaba470703ff16bc9570c5ff6e5cd.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>第一步：</strong>申请<span style="background-color:rgba(0, 0, 0, 0); color:#3e3e3e">AfterShip账号</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="background-color:rgba(0, 0, 0, 0); color:#3e3e3e"><span style="background-color:rgba(1, 0, 0, 0); color:#6a6a6a">第二步：</span></span></strong><span style="background-color:rgba(0, 0, 0, 0); color:#3e3e3e"><span style="background-color:rgba(1, 0, 0, 0); color:#6a6a6a">将授权码填写到后台 保存</span></span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="background-color:rgba(0, 0, 0, 0); color:#3e3e3e"><span style="background-color:rgba(1, 0, 0, 0); color:#6a6a6a"><span style="background-color:rgba(0, 0, 0, 0); color:#6a6a6a">第三步：</span></span></span></strong><span style="background-color:rgba(0, 0, 0, 0); color:#3e3e3e"><span style="background-color:rgba(1, 0, 0, 0); color:#6a6a6a"><span style="background-color:rgba(0, 0, 0, 0); color:#6a6a6a"><span style="background-color:rgba(1, 0, 0, 0); color:#3e3e3e">AfterShip</span>中配置可用快递公司，配置成功后点击同步</span></span></span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="background-color:rgba(0, 0, 0, 0); color:#3e3e3e"><span style="background-color:rgba(1, 0, 0, 0); color:#6a6a6a"><span style="background-color:rgba(0, 0, 0, 0); color:#6a6a6a"><span style="background-color:rgba(1, 0, 0, 0); color:#6a6a6a">第四步：</span></span></span></span></strong><span style="background-color:rgba(0, 0, 0, 0); color:#3e3e3e"><span style="background-color:rgba(1, 0, 0, 0); color:#6a6a6a"><span style="background-color:rgba(0, 0, 0, 0); color:#6a6a6a"><span style="background-color:rgba(1, 0, 0, 0); color:#6a6a6a">回到OpenCart后台查看是否配置成功</span></span></span></span></p> 
<p style="margin-left:0; margin-right:0"><span style="background-color:rgba(0, 0, 0, 0); color:#3e3e3e">AfterShip账号</span>申请地址：https://accounts.aftership.com/register</p> 
<p style="margin-left:0; margin-right:0; text-align:left">AfterShip 获取 API 路径和添加物流公司路径：</p> 
<p><img alt height="343" src="https://oscimg.oschina.net/oscnet/up-29ba954f9151943fdb772b62a4f4fae7301.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">点击查看大图</p> 
<p style="margin-left:0; margin-right:0"><span style="background-color:rgba(0, 0, 0, 0); color:#3e3e3e">特别注意： AfterShip 有7天免费试用时间。在后台使用AfterShip物流跟踪方式后，如果突然在发货时无法添加单号，请核实是否免费期限已到期！</span></p> 
<p style="margin-left:0; margin-right:0"><strong>2//快递100</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>第一步：</strong>登录注册快递100</p> 
<p><img alt height="82" src="https://oscimg.oschina.net/oscnet/up-7c52c99a03bc009078e815b2a243ef18cf7.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">快递100 API申请地址：http://www.kuaidi100.com/openapi/index.shtml</p> 
<p style="margin-left:0; margin-right:0">第二步：点击接口信息-获取授权信息</p> 
<p><img alt height="247" src="https://oscimg.oschina.net/oscnet/up-9b8a5bd3caf43dfaa7d44003e8cd12f5758.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">将客户授权 key 和 实时查询 customer 复制到后台快递100订单快递跟踪处</p> 
<p><img alt height="434" src="https://oscimg.oschina.net/oscnet/up-a460de3f9f4e67311f5c1013a919d187461.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">在功能模块下搜索快递100订单快递跟踪</p> 
<p style="margin-left:0; margin-right:0"><strong>第三步：</strong>点击安装之后，再点击编辑进入：</p> 
<p style="margin-left:0; margin-right:0"><strong style="color:#3e3e3e">第四步：</strong>复制参数到此处，如果该页面未有快递公司，可以点击 + 添加：</p> 
<p><img alt height="395" src="https://oscimg.oschina.net/oscnet/up-3f8bf6167915fbb92704b1e48cb374f6a24.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">快递公司代码必须是填写规定的代码不能任意填写，详情可点击下方链接，查询配置添加。</p> 
<p style="margin-left:0; margin-right:0">https://poll.kuaidi100.com/manager/page/document/kdbm</p> 
<p style="margin-left:0; margin-right:0">快递100 免费版暂不支持主流快递物流公司，比如：EMS，邮政，顺丰，四通一达和国际快递物流，因平台不定时升级，可能数据会有变化，具体请咨询 快递100 平台客服</p> 
<p style="margin-left:0; margin-right:0"><strong>3//快递鸟</strong></p> 
<p style="margin-left:0; margin-right:0">快递鸟 API申请地址：http://kdniao.com/</p> 
<p style="margin-left:0; margin-right:0"><strong>第一步：</strong>在平台上申请通过后可以获取 授权key和商户ID填到后台</p> 
<p style="margin-left:0; margin-right:0"><strong><span style="background-color:rgba(0, 0, 0, 0); color:#3e3e3e">第二步：</span></strong>复制参数到此处，如果该页面未有快递公司，可以点击 “+” 添加：</p> 
<p><img alt height="339" src="https://oscimg.oschina.net/oscnet/up-494de9a0cc468826ad7ad9119fcd6fdfff9.png" width="750" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">快递公司代码必须是填写规定的代码不能任意填写，详情可以到http://kdniao.com/查询配置添加</p> 
<p style="margin-left:0; margin-right:0; text-align:left">注：</p> 
<p style="margin-left:0; margin-right:0; text-align:left">1.快递鸟免费版限制：快递鸟免费版只支持百世、申通、圆通、天天，具体可以联系快递鸟客服咨询。</p> 
<p style="margin-left:0; margin-right:0; text-align:left">2.基础版和企业版区别：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.kdniao.com%2Fmembership" target="_blank">http://www.kdniao.com/membership</a></p> 
<p style="margin-left:0; margin-right:0; text-align:left">3.快递100免费版限制：每天最多100单，不能频繁请求；不支持四通一达顺丰ems邮政等主流快递；要添加友情链接（必需），具体请咨询快递100客服。</p> 
<p style="margin-left:0; margin-right:0; text-align:left">4.快递100免费版没有商户ID，但是企业版需要填商户ID，商户ID 即快递100后台的 实时查询编码。</p> 
<p style="margin-left:0; margin-right:0; text-align:left">5.因快递平台系统更新问题，请在配置时咨询快递100或快递鸟免费版和付费版支持快递公司具体信息，以他们最新的为准。</p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>三、</strong><span><strong>注意事项</strong></span></p> 
<p style="margin-left:0; margin-right:0">所有跨境电商用户，都需要根据自身产品特点选择适合自己的物流方式。例如：大件商品（家具类）不适合邮政包裹</p> 
<p style="margin-left:0; margin-right:0">其次，在淡旺季也要灵活使用不同的物流模式，可有效降低物流成本。 例如：淡季就选择中邮小包降低成本；旺季或者大促节日选择时效性快的物流方式</p> 
<p style="margin-left:0; margin-right:0">最后，需要提供不同的物流方式，供客户自主选择，提升购物体验</p> 
<p style="margin-left:0; margin-right:0">中文专业版<span style="background-color:rgba(0, 0, 0, 0); color:#3e3e3e">演示</span></p> 
<p style="margin-left:0; margin-right:0">前台：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F280" target="_blank">http://mall.opencart.cn</a></p> 
<p style="margin-left:0; margin-right:0">后台：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F284" target="_blank"><u>http://mall.opencart.cn/admin</u></a></p> 
<p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F284" target="_blank"><span style="color:#6a6a6a">账号密码均为：demo</span></a></p> 
<p style="margin-left:0; margin-right:0">国际专业版演示</p> 
<p style="margin-left:0; margin-right:0">前台：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F280" target="_blank">http://imall.opencart.cn</a></p> 
<p style="margin-left:0; margin-right:0">后台：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F284" target="_blank">http://imall.opencart.cn/admin</a></p> 
<p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F284" target="_blank"><span style="color:#6a6a6a">账号密码均为：demo</span></a></p> 
<p style="margin-left:0; margin-right:0"><strong>相关阅读</strong></p> 
<p style="margin-left:0; margin-right:0">1<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F288" target="_blank"><u>《跨境电商物流模式有哪些？》</u></a></p> 
<p style="margin-left:0; margin-right:0">2<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F291" target="_blank"><u>《OpenCart V3.8.1正式发布》</u></a></p>
                                        </div>
                                      
</div>
            