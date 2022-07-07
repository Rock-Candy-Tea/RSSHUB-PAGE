
---
title: '跨境独立站 OpenCart 中文更新 _ 商品多规格配置（第 11 期）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.opencart.cn/storage/uploads/image/2022/07/06/476324900497b838c8620503a48cc9f3.png'
author: 开源中国
comments: false
date: Thu, 07 Jul 2022 02:19:00 GMT
thumbnail: 'https://www.opencart.cn/storage/uploads/image/2022/07/06/476324900497b838c8620503a48cc9f3.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">点击 “作者” 名称 关注我们</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>独立站 OpenCart</strong>—— 外贸平台自建站 / 跨境电商独立站专用系统。安装方便，功能强大，操作简单</p> 
<p style="margin-left:0; margin-right:0"><strong>前言</strong>：在独立站OpenCart中，配置商品的多规格是卖家在商品售卖过程中，非常重要的一个环节</p> 
<p style="margin-left:0; margin-right:0">跨境电商独立站OpenCart中，我们开发了强大的多规格设置功能。几乎可以兼容一切商品属性类型，让您的独立站不再受限于售卖的商品类型</p> 
<p style="margin-left:0; margin-right:0">这篇文章带大家了解一下，OpenCart中文是如何配置商品的多规格？如何设置商品的规格的？</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><strong>01 | 规格管理功能简介</strong></p> 
<p style="margin-left:0; margin-right:0">多规格功能，可以帮助卖家，更便捷的添加商品类型、属性等信息（比如商品的颜色、尺寸、型号等）。卖家可以在后台，轻松的编辑或管理商品的属性类型信息</p> 
<p style="margin-left:0; margin-right:0">多规格功能，可以帮助客户在购买商品时，更直观的选择自己中意的商品类型</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/476324900497b838c8620503a48cc9f3.png" width="739" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">多规格商品体验链接</p> 
<p style="margin-left:0; margin-right:0">OpenCart中文专业版：<u><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmall.opencart.cn%2Fproduct-%25E5%25A4%258F%25E5%25AD%25A32021%25E6%2596%25B0%25E6%25AC%25BE%25E9%259F%25A9%25E7%2589%2588%25E5%25AE%25BD%25E6%259D%25BE%25E4%25B8%258A%25E8%25A1%25A3v%25E9%25A2%2586%25E5%25BF%2583%25E6%259C%25BA%25E9%2594%2581%25E9%25AA%25A8%25E8%25AE%25BE%25E8%25AE%25A1%25E6%2584%259F%25E5%25B0%258F%25E4%25BC%2597%25E6%259D%25A1%25E7%25BA%25B9%25E7%259F%25AD%25E8%25A2%2596t%25E6%2581%25A4%25E5%25A5%25B3" target="_blank"><span>点击查看</span></a></u></p> 
<p style="margin-left:0; margin-right:0">OpenCart国际专业版：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimall.opencart.cn%2Findex.php%3Froute%3Dproduct%2Fproduct%26product_id%3D29" target="_blank"><u>点击查看</u></a></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">【商品类型】配置方式有两种：</p> 
<p style="margin-left:0; margin-right:0"><strong>一、后台常用规格中创建</strong></p> 
<p style="margin-left:0; margin-right:0">商品目录→基础数据→常用规格</p> 
<p style="margin-left:0; margin-right:0"><strong>二、创建商品时新建规格</strong></p> 
<p style="margin-left:0; margin-right:0">后台商品管理→上传商品→多规格（可保存为常用规格）</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><strong>02 | 常用规格中创建 </strong></p> 
<p style="margin-left:0; margin-right:0">创建路径：商品目录→基础数据→常用规格→添加分组</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/9d5bed72ed5f6359ff04436c24b4c5c4.png" width="416" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">注：分组名称建议用大类。如服装、百货、鞋子等</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">以鞋子为例:</p> 
<table cellspacing="0" class="table-box" style="border-collapse:collapse; display:table; margin-bottom:10px; width:100%"> 
 <tbody> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">1</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">点击“<strong>添加分组”</strong>输入名称——鞋子</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">2</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">点击添加规格，输入<strong>“规格名称”</strong>——颜色（规格名称以鞋子参数为准）</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">3</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">点击添加<strong>“规格值”</strong>——红色、白色等</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">4</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">您也可添加多个<strong>“规格名称”</strong>，如鞋码，鞋码的规格值。添加完成后点击保存！</p> </td> 
  </tr> 
 </tbody> 
</table> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/580e89606261e2c311165ae5cc43192f.png" width="1139" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">规格配置完成之后，就需要将其应用到对应的商品中！</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><strong>a.商品配置规格</strong></p> 
<p style="margin-left:0; margin-right:0">编辑商品路径：商品目录→商品管理→基本设置→商品类型</p> 
<p style="margin-left:0; margin-right:0">页面下拉，可以看到有单规格商品和多规格商品选项，当商品有多规格时，请选择多规格商品</p> 
<p style="margin-left:0; margin-right:0">这里可以看到刚刚保存的常用规格，根据商品来选择“规格”，如鞋子：</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/529c3e26c5090b06a96faf1cf8214998.png" width="468" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">这里展示了鞋子所有的规格值，点击使用</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/c74e5b009e86970ecd838adadcd008b4.png" width="580" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">如果，当前鞋子所需的规格值还不完善。添加规格后，可点击右侧的<strong>“添加值”</strong>继续手动创建</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/4c9071fe25c91557f0c8667749dbdae1.png" width="1092" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">当商品规格值多时，可以批量设置规格数据！</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><strong>b.批量设置规格</strong></p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/cbcea1c2ee2a6434366bb96b306afc2a.png" width="1008" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">比如</p> 
<table cellspacing="0" class="table-box" style="border-collapse:collapse; display:table; margin-bottom:10px; width:100%"> 
 <tbody> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">1</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">颜色红色/尺码35/商品型号123开头（数据会默认在123后叠加，如123-1,123-2）</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">2</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">SKU值258开头（数据如型号一致，会默认叠加）、销售价格、成本价以及库存数量等</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">3</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#3e3e3e; border-style:none; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0">按需设置后，点击“批量设置”即可</p> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">批量设置后，下图可以看到设置的数据</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/998a662e28fb16db01f244fb48ea8014.png" width="1023" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><strong>03 | 创建商品时-新建规格</strong></p> 
<p style="margin-left:0; margin-right:0">当每种商品规格不一致时，可能创建常用规格数据会过多</p> 
<p style="margin-left:0; margin-right:0">这时，可直接在每个“商品管理”页去创建只属于它的规格值。</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0"><strong>操作步骤如下</strong></p> 
<p style="margin-left:0; margin-right:0">1. 在编辑商品基本设置下方，找到<strong>“商品类型”</strong>，选择多规格商品，点击添加规格</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/0109fd463e1f2e4a3fdf0512a913fe93.png" width="422" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">2. 输入规格名称，点击保存（以颜色为例）</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/7a0fc2a1193ea8256e343876d1f24996.png" width="898" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">3. 点击添加值</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/52a6a84bac1a6d60952cdd1c5f5b6e6f.png" width="806" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">4. 输入颜色的规格值，点击保存（以红色为例）</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/51bf077ec01e9f2f61f36e28d8eb6044.png" width="476" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">5. 根据需求选择是否继续添加规格</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/dd2fc1ab91faf9dd385cd3215017f396.png" width="589" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">注意：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">规格值可以<strong>同时添加多个</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">双击<strong>“规格值”可修改名称</strong>，也可以上传尺码图片</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">两个规格之间排序可上下移动，影响位置在左下方红色框位置</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果在这里添加的规格后续可能会常用，也可以存为<strong>常用规格</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">所有配置完成之后，记得保存该商品！</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"> </p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/ff8b2ed2fcfaa7535bab5565bcbc4b10.png" width="1080" referrerpolicy="no-referrer"></p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/07/06/856470413d992f8262ec6e351e822d19.png" width="503" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p style="color:#3d464d; margin-left:0; margin-right:0; text-align:left"><strong>往期推荐：</strong></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0; text-align:left">1、<a href="https://www.oschina.net/news/200538">《 OpenCart 中文 | 商品多规格配置 第 10 期》</a></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0; text-align:left">2、<a href="https://www.oschina.net/news/199075">《 OpenCart 中文 | 多语言功能 第 9 期》</a></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0">跨境独立站是什么?想了解OpenCart中文？</p> 
<p style="margin-left:0; margin-right:0">什么是“独立站”怎么建站?独立站怎么推广？</p> 
<p style="margin-left:0; margin-right:0">建一个外贸独立站大约多少钱？<strong>有问题？欢迎随时联系我们！</strong></p>
                                        </div>
                                      
</div>
            