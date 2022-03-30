
---
title: 'OpenCart 中文更新 _ 批量导入导出合集（第 3 期）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.opencart.cn/storage/uploads/image/2022/03/24/4f892bdd400b400fdddfc34fa5a6cbdd.png'
author: 开源中国
comments: false
date: Wed, 30 Mar 2022 11:08:00 GMT
thumbnail: 'https://www.opencart.cn/storage/uploads/image/2022/03/24/4f892bdd400b400fdddfc34fa5a6cbdd.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>OpenCart</strong>——PHP 开源电商独立站系统。安装方便，功能强大，操作简单</p> 
<p><strong>前言</strong></p> 
<p style="margin-left:0; margin-right:0">之前我们介绍了 OpenCart3.8专业版中，最常被卖家接触到，也是最常被提及的一些功能，例如用户注册登录模块、模板主题、工作台、左侧菜单、后台搜索</p> 
<p style="margin-left:0; margin-right:0">这次我们将侧重独立站运营常用的功能，介绍OpenCart独立站电商建站系统中，相关数据（商品/客户/统计数据）的导入导出功能</p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>01、商品批量导入/导出</strong></p> 
<p style="margin-left:0; margin-right:0">为了能更方便地管理商品，OpenCart后台商品可进行批量导入导出，数据有两种类型，分别为基础数据和商品数据。导出的方式有两种，可选择按商品ID导出，也可选择分批导出。</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/24/4f892bdd400b400fdddfc34fa5a6cbdd.png" width="1144" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">基础数据和商品数据如果没有参考模板，建议先上传一个商品和配置基础数据。导出来之后查看数据格式，按照导出的表格格式来填写。</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/24/04878def4cd994b4a321989fc671b1c9.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">注意事项：</p> 
<p style="margin-left:0; margin-right:0"><strong>1. 基础数据导入导出</strong>：指商品的基础数据，比如：属性、分类、选项、类型等；</p> 
<p style="margin-left:0; margin-right:0"><strong>2. 商品数据导入导出：</strong>指商品的数据，比如：名称、描述、价格、库存等内容；</p> 
<p style="margin-left:0; margin-right:0"><strong>3. 按商品ID导出：</strong>每个商品有个独立的ID，比如1~100，便导出ID为1~100的商品；</p> 
<p style="margin-left:0; margin-right:0"><strong>4. 分批次导出：</strong>一次导出的数量，导出的批次，比如第一次导出10个，第二次导出20个，是按商品ID从小到大的顺序导出。</p> 
<p style="margin-left:0; margin-right:0"><span>✦✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>02、批量评论导入</strong></p> 
<p style="margin-left:0; margin-right:0">OpenCart后台中新上架的商品，由于商品评价数较少，会影响商品成交转化。这时候就需要将平台的真实评论，导入该商品中进行补充，从而提升转化。</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/24/c922fd8c024ddcb0c47f6b11abc03e14.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>导入步骤：</strong></p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">进入<strong>商品目录</strong>模块点击“商品评论”</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">点击下载模板，将评价信息填入表中    </p> </li> 
 <li> <p style="margin-left:0; margin-right:0">点击导入，选择表格文件后确认</p> </li> 
</ol> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/24/06b7e68990c34fb4626903f58bb6e819.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">导入评论样式</p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>03、客户资料导出</strong></p> 
<p style="margin-left:0; margin-right:0">OpenCart独立站店铺运营中，对客户进行分析可以使我们更了解用户的需求。通过对<strong>客户注册地址、客户等级、客户注册时间、客户注册来源</strong>等信息的分析，可以得出非常多有价值的运营建议。</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/24/6efe2c6173719c2724406c027f80efaf.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>导出步骤：</strong></p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">进入<strong>客户管理</strong>模块，筛选目标客户</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">勾选想要导出的客户，点击导出即可 </p> </li> 
</ol> 
<p style="margin-left:0; margin-right:0"><span>✦✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>04、统计报表导入导出</strong></p> 
<p style="margin-left:0; margin-right:0">为了能更好地查看商城相关数据，做好商城整体的运营规划，可以使用OpenCart后台“<strong>统计报表</strong>”功能，查看商城中的各项指标是否正常。</p> 
<p style="margin-left:0; margin-right:0">报表类型有以下几种可以选择：</p> 
<p style="margin-left:0; margin-right:0"><strong>1. 客户维度报表：</strong></p> 
<p style="margin-left:0; margin-right:0">客户余额报表、客户活动报表、客户搜索报表</p> 
<p style="margin-left:0; margin-right:0"><strong>2. 订单维度：</strong></p> 
<p style="margin-left:0; margin-right:0">订单报表、税额报表</p> 
<p style="margin-left:0; margin-right:0"><strong>3. 商品维度：</strong></p> 
<p style="margin-left:0; margin-right:0">商品配送报表、商品退换报表、商品销售报表、商品浏览报表、商品购买报表</p> 
<p style="margin-left:0; margin-right:0"><strong>4. 营销维度：</strong></p> 
<p style="margin-left:0; margin-right:0">奖励积分报表、折扣统计报表</p> 
<p style="margin-left:0; margin-right:0">* 导出的文件时CSV格式</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/24/60342ff4336948d45fefce919b62c8be.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>导出步骤：</strong></p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">进入对应模块点击“统计报表”模块选择统计报表</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">选择报表类型，最后点击右侧导出</p> </li> 
</ol> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/24/1b9fdeaadf0202cd8d579f9c0ee177c0.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">报表样式如图</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0; text-align:left"><strong style="color:#3d464d">关注我们，定期分享开源建站系统——<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2F" target="_blank">opencart中文</a>最新动态！</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>相关阅读</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Fproducts_update" target="_blank"><strong>opencart中文产品更新动态</strong></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2. <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F291" target="_blank"><strong>《OpenCart V3.8.1专业版正式发布》</strong></a></p>
                                        </div>
                                      
</div>
            