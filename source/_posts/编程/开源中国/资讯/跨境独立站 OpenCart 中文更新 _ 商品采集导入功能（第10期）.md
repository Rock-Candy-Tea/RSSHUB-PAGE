
---
title: '跨境独立站 OpenCart 中文更新 _ 商品采集导入功能（第10期）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.opencart.cn/storage/uploads/image/2022/06/22/a102388ec7a9f2de3c1d3ddac10b4c0d.png'
author: 开源中国
comments: false
date: Thu, 23 Jun 2022 06:16:00 GMT
thumbnail: 'https://www.opencart.cn/storage/uploads/image/2022/06/22/a102388ec7a9f2de3c1d3ddac10b4c0d.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">点击 “作者” 名称 关注我们</span></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><strong>独立站OpenCart</strong>——外贸平台自建站/跨境电商独立站专用系统。安装方便，功能强大，操作简单</p> 
<p style="margin-left:0; margin-right:0"><strong>前言</strong>：快速上架商品，是跨境独立站卖家，日常独立站运营中非常重要的工作之一</p> 
<p style="margin-left:0; margin-right:0">OpenCart专业版中，给商家开发了非常好用的商品采集、商品导入功能。帮助独立站卖家能够又快又好的，快速上架商品！</p> 
<p style="margin-left:0; margin-right:0">这篇文章就来说说，如何使用OpenCart做采集？以及如何快速的批量导入商品?</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"> </p> 
<p style="margin-left:0; margin-right:0"><strong>01 | 如何进行商品采集？</strong></p> 
<p style="margin-left:0; margin-right:0">OpenCart商品采集——支持采集多个主流店铺商品，例如 京东、天猫、淘宝、Ebay、AliExpress、 苏宁易购等多个平台</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/06/22/a102388ec7a9f2de3c1d3ddac10b4c0d.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">采集操作流程：商品管理→商品采集→输入采集链接→开始采集</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">采集操作界面说明：</p> 
<p style="margin-left:0; margin-right:0">1、强制重采：如果该商品链接已被采集过，再次采集时注意勾选“强制重采”，如未勾选“强制重采”点击“开始采集”，会覆盖之前同一个采集链接的商品内容</p> 
<p style="margin-left:0; margin-right:0">2、开始采集：如果该商品链接未被采集，直接点击开始采集即可</p> 
<p style="margin-left:0; margin-right:0">3、发布按钮：采集后点击即可立即发布商品的按钮</p> 
<p style="margin-left:0; margin-right:0">4、查看采集结果：采集商品的ID、平台、SKU以及产品名称和描述等内容。</p> 
<p style="margin-left:0; margin-right:0">5、使用说明：支持平台以及参考链接（链接可能已失效）</p> 
<p style="margin-left:0; margin-right:0">6、根据筛选条件，进行采集商品的筛选</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">注：因为平台限制或规则变化，采集时可能会出现详情页图片无法采集的问题</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"> </p> 
<p style="margin-left:0; margin-right:0"><strong>02 | 如何进行商品批量导入？</strong></p> 
<p style="margin-left:0; margin-right:0">对于跨进电商独立站卖家来说。商品批量导入功能，是快速批量上架商品的另一个选择</p> 
<p style="margin-left:0; margin-right:0">首先为了获得表格格式，需要先从商品列表中导出数据，按照导出表格的格式，填写导入商品的格式。</p> 
<p style="margin-left:0; margin-right:0">商品数据分为“基础数据”和“商品数据”，需要使用两种模板分别导入。</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/06/22/160906db64af870baeb5af6a9d839ebb.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">导入/导出操作流程：商品管理→商品批量导入/导出</p> 
<p style="margin-left:0; margin-right:0">导入导出操作界面说明：</p> 
<p style="margin-left:0; margin-right:0">1、基础数据导入导出：指商品基础的参数信息数据，比如：商品的属性、分类、尺寸、颜色、选项等维度信息；</p> 
<p style="margin-left:0; margin-right:0">2、商品数据导入导出：指商品的详细数据，比如：名称、描述、价格、库存等内容</p> 
<p style="margin-left:0; margin-right:0">3、按商品 ID 导出：每个商品有个独立的ID，比如选择1~100，便导出 ID为 1~100 的商品</p> 
<p style="margin-left:0; margin-right:0">4、分批次导出：一次导出的数量，导出的批次，比如第一次导出10个，第二次导出20个，则是按商品ID从小到大的顺序导出</p> 
<p style="margin-left:0; margin-right:0">注：导入商品时，将要导入商品数据填入正确的位置。如：Product ID（ID具有唯一性，不可与之前的商品ID一样）、Categories、Image等数据</p> 
<p style="margin-left:0; margin-right:0">Image 需先将图片上传到 FTP，在 FTP 获取图片路径，复制到 Image 这一栏对应的商品！</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0; text-align:left"><strong>往期推荐：</strong></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0; text-align:left">1、<a href="https://www.oschina.net/news/199075">《独立站 OpenCart 多语言功能（第 9 期）》</a></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0; text-align:left">2、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F308" target="_blank">《免费开源独立站有哪些？建站系统如何选？》</a></p> 
<p style="margin-left:0; margin-right:0">跨境独立站是什么?想了解OpenCart中文？</p> 
<p style="margin-left:0; margin-right:0">什么是“独立站”怎么建站?独立站怎么推广？</p> 
<p style="margin-left:0; margin-right:0">建一个外贸独立站大约多少钱？<strong>有问题？欢迎随时联系我们！</strong></p> 
<p> </p>
                                        </div>
                                      
</div>
            