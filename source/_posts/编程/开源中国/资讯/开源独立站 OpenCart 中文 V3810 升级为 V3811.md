
---
title: '开源独立站 OpenCart 中文 V3.8.1.0 升级为 V3.8.1.1'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.opencart.cn/storage/uploads/image/2022/05/10/3c39222c5720122048652918046fac6c.png'
author: 开源中国
comments: false
date: Tue, 10 May 2022 06:16:00 GMT
thumbnail: 'https://www.opencart.cn/storage/uploads/image/2022/05/10/3c39222c5720122048652918046fac6c.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>点击“作者”名称 关注我们</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0"><strong>独立站 OpenCart</strong>——外贸平台自建站/跨境电商独立站专用系统。安装方便，功能强大，操作简单</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0"><strong>前言</strong>：随着OpenCart中文/国际专业版系统的销量增长，客户对独立站OpenCart系统提出了一些非常有用的优化建议，产品研发团队根据客户的需求，新迭代了新的版本。</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">接下来看看我们从3.8.1.0版本 到 3.8.1.1版本都新增、优化、修复了哪些功能？</p> 
<p style="color:#3d464d; margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0"><strong>01 | 新增功能</strong></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">（1）支持后台管理员：admin 目录修改文件名</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/05/10/3c39222c5720122048652918046fac6c.png" referrerpolicy="no-referrer"></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">出于安全考虑，OpenCart专业版3.8.1.1中可自定义后台目录名称。</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">管理员根据自身需要，设置非常规的后台入口地址。——该功能可以有效防止黑客暴力破解密码！</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0"> </p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">（2）发票功能（仅适用国内环境）</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/05/10/663cedaf16be1c2d3c959c960052efb5.png" referrerpolicy="no-referrer"></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">新版本OpenCart支持付款流程中开票</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">开票步骤如下：</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">1、后台开启开具发票功能</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">2、买家提交订单时填写开票信息 </p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">3、提交订单成功后，卖家后台可看到开票信息，根据开票信息开发票</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">4、发票以附件形式上传到订单，买家在订单详情页可以下载附件。</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">订单开票演示如下图：</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/05/10/c102233b2534c5c96ad6fdc911fa777c.png" referrerpolicy="no-referrer"></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0"> </p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">（3）默认PC主题模板 支持多配色切换功能</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">可以在主题模板中设置不同的主题颜色，目前一共有5中主题颜色可供选择。</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/05/10/1291d3e6d48c2f77558741e20a1361f0.png" referrerpolicy="no-referrer"></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">后台操作位置：模块管理→模板主题→点击“编辑”主题→主题色选择</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0"> </p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">（4）集成 Sentry 用于异常收集—提升系统稳定性</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/05/10/a0d77d2d698462eb059a41a31169c715.png" referrerpolicy="no-referrer"></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">Sentry日志监控，可以收集各类错误信息，并且反馈出来，更方便调试或者及时捕捉系统问题</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">注<span>：需要自己搭建Sentry日志监控，OpenCart专业版仅集成了接口</span></p> 
<p style="color:#3d464d; margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0"><strong>02 | 优化功能</strong></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">（1）升级 nexmo，vonage 短信模块</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">（2）移除 BearyChat 支持</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">（3）缩略图白边优化</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">之前：假设原图尺寸为 500x300，目标尺寸400x400，图片等比例缩小后宽有400，而高度没有400， 那么就会将高度不够的地方填充白色（如下图所示）</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/05/10/d0d7ec1c602f9ea2d8720b46b563e181.png" referrerpolicy="no-referrer"></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">现在：图片会以窄边为基准填充满，缩放到400*400，裁剪长边，不会出现空白。（如下图所示）</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/05/10/8131cdcb11a77388df2b90914d991547.png" referrerpolicy="no-referrer"></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0"> </p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">（4）优惠券添加前台是否显示选择</p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">卖家在后台营销推广中可以选择，商城前台是否展示优惠券</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/05/10/63599151750f145accf84aae0b9a38f1.png" referrerpolicy="no-referrer"></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">后台操作位置：营销推广 → 优惠券</p> 
<p style="color:#3d464d; margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0"><strong>03 | 修复功能</strong></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">（1）后台日期选择器交互（包含所有涉及日期的地方）</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/05/10/c41b5062cb8d82b1ac9794ebc95ebb18.png" referrerpolicy="no-referrer"></p> 
<p style="color:#3d464d; margin-left:0; margin-right:0">（2）修复 商品分类页面，子分类链接有分页参数，导致商品列表为空的问题<br> （3）修复 phinx 升级脚本</p>
                                        </div>
                                      
</div>
            