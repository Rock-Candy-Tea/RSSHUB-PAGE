
---
title: 'OpenCart 中文更新 _ 短信验证消息配置（第 4 期）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.opencart.cn/storage/uploads/image/2022/03/29/17ae4318115738827402b6331eb38b81.png'
author: 开源中国
comments: false
date: Wed, 06 Apr 2022 01:38:00 GMT
thumbnail: 'https://www.opencart.cn/storage/uploads/image/2022/03/29/17ae4318115738827402b6331eb38b81.png'
---

<div>   
<div class="content">
                                                                                            <p><strong>OpenCart</strong>——PHP 开源跨境外贸电商独立站系统，安装方便，功能强大，操作简单</p> 
<p style="margin-left:0; margin-right:0"><strong>前言：</strong>短信功能——作为OpenCart独立站运营，营销环节最常用的功能，同样也是用户登录最重要的步骤。配置短信是独立站卖家们的“必修课”。</p> 
<p style="margin-left:0; margin-right:0">最近，经常有客户询问我们如何配置OpenCart短信模板，今天就来给大家介绍一下。完整的OpenCart配置短信的步骤！</p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>01、手机短信功能模块</strong></p> 
<p style="margin-left:0; margin-right:0">简单来说，短信配置一共分3为个步骤：</p> 
<p style="margin-left:0; margin-right:0">1、第三方短信平台申请API接口</p> 
<p style="margin-left:0; margin-right:0">2、在短信平台里，配置短信签名、模板</p> 
<p style="margin-left:0; margin-right:0">3、将相关信息/APIKEY回填到OpenCart后台</p> 
<p style="margin-left:0; margin-right:0"><strong>1/进入短信模块</strong></p> 
<p style="margin-left:0; margin-right:0">OpenCart后台：系统设置→参数设置→手机短信</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/17ae4318115738827402b6331eb38b81.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>2/设置短信登录</strong></p> 
<p style="margin-left:0; margin-right:0">OpenCart后台：系统设置→网店设置→登录注册设置</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/b53118e656817147c880f511c060b180.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>3/支持对接平台？</strong></p> 
<p style="margin-left:0; margin-right:0">目前，OpenCart3.8短信接口支持以下4个平台，可以点击下方网站链接注册，获取接口账号和密钥</p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong><span>云片</span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yunpian.com%2F" target="_blank">https://www.yunpian.com/</a></span></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong>阿里云短信（原阿里大鱼）</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.aliyun.com%2Fproduct%2Fsms" target="_blank">https://www.aliyun.com/product/sms</a></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong>c123</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.c123.com%2F" target="_blank">http://www.c123.com/</a></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><strong>Nexmo:</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nexmo.com%2F" target="_blank">https://www.nexmo.com/</a></p> 
<p style="margin-left:0px; margin-right:0px"><span>✦</span><span>✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>02、云片短信平台</strong></p> 
<p style="margin-left:0; margin-right:0">我们较为推荐使用云片，由于我们的客户多为跨境电商卖家。云片的国内外短信都支持！</p> 
<p style="margin-left:0; margin-right:0">首先，需要到云片网站注册申请短信接口。</p> 
<p style="margin-left:0; margin-right:0">1. 在云片管理后台首页（如下图）即可看到APIKEY</p> 
<p style="margin-left:0; margin-right:0">将其填入后台手机短信配置即可</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/17876a6920e53490cb906a50e7b2a097.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">2. OpenCart后台云片配置如下，将APIKEY填好即可！</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/50aea61a5590f9a4fc63595d5c55add8.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">3. 在云片的设置→账户设置里</p> 
<p style="margin-left:0; margin-right:0">填写开发者信息，个人或者企业</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/fa13e3fa95ba4c2e19ac7b6ef9aeef94.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">4. 填写了开发者信息后，就可以添加短信签名</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/0966ae19b609cca89e2687d5cd10b734.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">5. 将申请好的签名回填到后台</p> 
<p style="margin-left:0; margin-right:0">功能模块→手机短信→选项设置→短信签名</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/2758d6646f0d784a45028b7221f0af34.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">6. 增加了签名后，可以填写短信模板</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/0b3190a17a75f2f3d4b814b4ef5d0d29.png" referrerpolicy="no-referrer"></p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/ca4c78f349751576e6dae81028faad97.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:left">注意：</p> 
<p style="margin-left:0; margin-right:0; text-align:left">1、新增短信模板，如果云片有子账号，请确定发送账号跟操作账号是否一致！选择短信签名、短信类型，设置短信内容，提交审核。<br> 2、系统使用的变量符号是 英文&#123;code&#125;，云片是#code#，符号需注意，内容一致！</p> 
<p style="margin-left:0; margin-right:0"><span>✦✦</span></p> 
<p style="margin-left:0; margin-right:0"><strong>03、阿里云短信平台</strong></p> 
<p style="margin-left:0; margin-right:0">首先，在阿里云短信（原阿里大鱼）注册申请短信接口。</p> 
<p style="margin-left:0; margin-right:0">操作步骤和云片相同，在后台短信集成安装阿里云短信，将对应数据填入后台，状态启用保存</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/0d9575ea8a17e357956e52af3b2cc1f5.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">阿里云短信和云片配置的区别：</p> 
<p style="margin-left:0; margin-right:0">1、云片是输入短信模板内容</p> 
<p style="margin-left:0; margin-right:0">2、 阿里云短信，是将阿里云短信平台已审核通过的模板CODE，填到后台</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/35ebdb78217140887efa44acee95fd6b.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">1. 在阿里云平台获取 AccessKey ID 和 AccessKey Secret，复制到OpenCart后台</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/c557e71fad70a1145032a7b9da3ee1de.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">2. 按照正常流程添加签名、添加模板</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/215f4f3441640bda3cc52e9f2d90faa5.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">这里注意，如果选择短信验证，阿里云需要选择变量属性，如果是商品降价类通知，请选其他</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/0da752ee18ce3855ca6245c74840b3dd.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">3. 模板审核通过后，将 <strong>模板CODE</strong> 复制到OpenCart后台短信配置页面</p> 
<p><img src="https://www.opencart.cn/storage/uploads/image/2022/03/29/d63190ccdf92aaa24ff1aa9e09f49864.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">最后回到后台，按照如下步骤：</p> 
<p style="margin-left:0; margin-right:0">参数设置→手机短信→选项设置</p> 
<p style="margin-left:0; margin-right:0">将平台短信规则文本，填写到后台对应字段中即可</p> 
<p style="margin-left:0; margin-right:0">使用过程中遇到问题？对OpenCart有新的功能需求？网站定制化需求？</p> 
<p style="margin-left:0px; margin-right:0px"><strong>欢迎随时联系我们！</strong></p> 
<p style="margin-left:0px; margin-right:0px"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>相关阅读</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Fproducts_update" target="_blank"><strong>opencart中文产品更新动态</strong></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2. <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opencart.cn%2Farticles%2F296" target="_blank">《跨境电商独立站靠谱吗？》</a></strong></p>
                                        </div>
                                      
</div>
            