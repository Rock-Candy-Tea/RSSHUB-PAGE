
---
title: '开源独立站 OpenCart 中文更新 _ 商品管理功能（第 6 期）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.opencart.cn/storage/uploads/image/2022/04/19/550e87a673672b6a21a9814a4d119078.png'
author: 开源中国
comments: false
date: Wed, 20 Apr 2022 09:48:00 GMT
thumbnail: 'https://www.opencart.cn/storage/uploads/image/2022/04/19/550e87a673672b6a21a9814a4d119078.png'
---

<div>   
<div class="content">
                                                                                            <p><strong>OpenCart中文</strong></p> 
<p style="margin-left:0; margin-right:0">旗下产品——OpenCart免费版、OpenCart国际专业版、OpenCart中文专业版、OpenCart专业版多商家</p> 
<p style="margin-left:0; margin-right:0"><strong>前言</strong>：前几期，我们说了独立站OpenCart专业版中的<strong>界面更新、注册登录、短信验证、商品导入、订单发货功能</strong>，这些都是用户最为关注的重点功能。</p> 
<p style="margin-left:0; margin-right:0">作为一个电商系统，<strong>商品管理</strong>作为系统中的三大核心（物流、资金流、信息流）支柱功能之一，这篇文章来说一下OpenCart商品管理中的功能。</p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>01、OpenCart介绍</strong></p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/550e87a673672b6a21a9814a4d119078.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">独立站OpenCart是<strong>全球主流的，开源电商独立站建站</strong>系统。是与Magento、Wordpress齐名的全球三大开源电商建站系统。</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/cffe294a083559c5778bf63461ff685f.jpg" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">OpenCart采用领先的<strong>MVC系统架构</strong>，易扩展和二次开发。代码清晰，H5+C3全响应式。</p> 
<p style="margin-left:0; margin-right:0">系统支持全球多个语言、货币种类，能<strong>适应更多外贸市场</strong></p> 
<p style="margin-left:0; margin-right:0">有着<strong>易扩展，易维护</strong>的特点， 代码清晰规范，二开快捷。</p> 
<p style="margin-left:0; margin-right:0"><span>✦✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>02、功能模块介绍</strong></p> 
<p style="margin-left:0; margin-right:0">商品功能模块中，主要有一下几大功能版块：</p> 
<p style="margin-left:0; margin-right:0"><strong>1|商品分类</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>主要用于对商城中商品分类进行管理</strong>，支持设置多级类目、子类目</p> 
<p style="margin-left:0; margin-right:0">可以点击新增、编辑分类名称、分类描述、Meta Tag 标题/关键词等信息</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/de5babbe287a4873053d87125d7d0c26.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>2|商品管理</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>商品目录功能下的核心功能</strong>、可以创建、查看、编辑平台所有的商品信息，可以根据商品状态、价格、分类等信息对商品进行筛选。</p> 
<p style="margin-left:0; margin-right:0">该功能下有商品采集器，<strong>可以进行商品采集</strong>，目前支持京东、淘宝、亚马逊、Ebay等平台的商品采集。</p> 
<p style="margin-left:0; margin-right:0">商品管理中，还有<a href="https://www.oschina.net/news/188901" target="_blank"><strong>商品导入导出</strong></a>功能，这个在之前的文章中提到过。<span>（点击查看相应文章）</span></p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/1005de571b59cb315c0d9b828331b630.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>3|基础数据</strong></p> 
<p style="margin-left:0; margin-right:0">基础数据<strong>可以管理商品中的基础参数信息</strong>，在这里可以新增商品规格，添加商品属性，新增商品品牌。例如尺寸、版本、颜色、商品属性信息。<strong>可以更全面完整地描述商品信息</strong>。</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/a80f7b1de72a0e73b6d6872d0d1377e6.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>4|商品咨询&评论</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>商品咨询主要针对，未购买的用户</strong>。能够让客户将对问题公开出来，其他浏览该商品的用户也能看到商家回答内容的内容，从而提升商品转化率。</p> 
<p style="margin-left:0; margin-right:0"><strong>商品评论则主要针对已购买的用</strong><strong>户</strong></p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/9e57db8aa6ff694623a68c5c18bea9a7.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/bb14a2ddbf14e86d0885e450d15299ca.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>03、功能细节介绍</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>1|重点迭代功能</strong></p> 
<p style="margin-left:0; margin-right:0">- 商品管理模块中，增加<strong>按商品分类筛</strong><strong>选</strong>功能</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/8dfa0e5f2602e72b697d0f870833a3b4.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">-<span> </span><strong>商品详情页分享</strong>js 脚本——按语言自动切换</p> 
<p style="margin-left:0; margin-right:0">中文自动使用 bshare (支持 https 网站),可以分享到第三方平台，其它语言使用原 addThis 分享到FaceBook,Twitter,linkedin等平台</p> 
<p style="margin-left:0; margin-right:0">这个场景适用于经营多个国家的电商网站，系统可以根据用户选择的语言切换不同的分享方式</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/58395977fad35290468cb347cf5e6751.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">- 商品分类<strong>自动翻译多语言</strong>：开启“机器翻译”后可以将商品分类、分类详情翻译成其他语言</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/bf555eb8f1a960c20907feb6b9a3cd19.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">- 商品列表页<strong>快速编辑商品</strong>：上下架、价格、名称、库存：可以方便的在商品列表页面，编辑商品的常用信息，无需进入编辑详情页</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/374ad823508b5581d2477d3cae9599f3.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p style="margin-left:0; margin-right:0">- 支持<strong>商品主图视频播放</strong>：进入商品编辑页面，可以上传商品主图视频</p> 
<p style="margin-left:0; margin-right:0">- 商品<strong>详情页有二维码</strong>，方便手机扫码后打开网页购物</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/5e41d4278f1ad14008fd398046dd32fa.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>2|重点优化功能</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>在使用体验上我们优化了以下内容：</strong></p> 
<p style="margin-left:0; margin-right:0">1. 可在后台<strong>自定义商品销量</strong>，商品销量在前端展示</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/ccf93b65c0bc8c615156cb49fd69bbbb.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">2.<span> </span><strong>优化</strong>商品<strong>保存等待时间过长</strong>问题</p> 
<p style="margin-left:0; margin-right:0">3. 简化商品保存代码逻辑，<strong>加快商品保存速度</strong>，代码更易读</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/04/19/b891b7e205c577b23cf9cd80892c2035.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">4.<span> </span><strong>优化商品编辑页</strong>，减少商品编辑操作步骤</p> 
<p style="margin-left:0; margin-right:0">5. 多规格/子商品主图一个页面上传,<span> </span><strong>批量设置价格</strong><strong>库存</strong>,自动生成不同类型商品</p> 
<p style="margin-left:0; margin-right:0">为了能了解OpenCart3.8国际专业版系统的优秀特色，强烈建议您试用一下，推荐您下载以下三款OpenCart系统进行试用/对比/测试：</p> 
<p style="margin-left:0; margin-right:0">1.<span> </span><strong>OpenCart英文原版</strong></p> 
<p style="margin-left:0; margin-right:0">2.<span> </span><strong>OpenCart3.8中文/国际免费版</strong></p> 
<p style="margin-left:0; margin-right:0">3.<span> </span><strong>OpenCart3.8中文专业版demo站</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>往期推荐</strong></p> 
<p style="margin-left:0; margin-right:0">1<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F298" target="_blank"><span>《DIY定制产品设计 也配拥有独立站！》</span></a></p> 
<p style="margin-left:0; margin-right:0">2<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F296" target="_blank"><span>《2022年个人怎样做跨境电商？》</span></a></p> 
<p style="margin-left:0; margin-right:0">想了解独立站怎么做？想了解OpenCart网站设计？</p> 
<p style="margin-left:0; margin-right:0">使用过程中遇到问题？对OpenCart有新的功能需求？</p> 
<p style="margin-left:0; margin-right:0">网站定制化需求？<strong>欢迎随时联系我们！</strong></p>
                                        </div>
                                      
</div>
            